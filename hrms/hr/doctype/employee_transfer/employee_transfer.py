# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate

from hrms.hr.utils import update_employee_work_history


class EmployeeTransfer(Document):
	def before_submit(self):
		if getdate(self.transfer_date) > getdate():
			frappe.throw(
				_("Employee Transfer cannot be submitted before Transfer Date"),
				frappe.DocstatusTransitionError,
			)

	def on_submit(self):
		employee = frappe.get_doc("Employee", self.employee)
		if self.create_new_employee_id:
			new_employee = frappe.copy_doc(employee)
			new_employee.name = None
			new_employee.employee_number = None
			new_employee = update_employee_work_history(
				new_employee, self.transfer_details, date=self.transfer_date
			)
			if self.new_company and self.company != self.new_company:
				new_employee.internal_work_history = []
				new_employee.date_of_joining = self.transfer_date
				new_employee.company = self.new_company
			# move user_id to new employee before insert
			if employee.user_id and not self.validate_user_in_details():
				new_employee.user_id = employee.user_id
				employee.db_set("user_id", "")
			new_employee.insert()
			self.db_set("new_employee_id", new_employee.name)
			# relieve the old employee
			employee.db_set("relieving_date", self.transfer_date)
			employee.db_set("status", "Left")
		else:
			employee = update_employee_work_history(employee, self.transfer_details, date=self.transfer_date)
			if self.new_company and self.company != self.new_company:
				employee.company = self.new_company
				employee.date_of_joining = self.transfer_date
			employee.save()

	def on_cancel(self):
		employee = frappe.get_doc("Employee", self.employee)
		if self.create_new_employee_id:
			if self.new_employee_id:
				frappe.throw(
					_("Please delete the Employee {0} to cancel this document").format(
						f"<a href='/app/Form/Employee/{self.new_employee_id}'>{self.new_employee_id}</a>"
					)
				)
			# mark the employee as active
			employee.status = "Active"
			employee.relieving_date = ""
		else:
			employee = update_employee_work_history(
				employee, self.transfer_details, date=self.transfer_date, cancel=True
			)
		if self.new_company != self.company:
			employee.company = self.company
		employee.save()

	def validate_user_in_details(self):
		for item in self.transfer_details:
			if item.fieldname == "user_id" and item.new != item.current:
				return True
		return False
