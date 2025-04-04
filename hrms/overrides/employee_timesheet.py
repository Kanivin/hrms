# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from kanierp.projects.doctype.timesheet.timesheet import Timesheet


class EmployeeTimesheet(Timesheet):
	def set_status(self):
		self.status = {"0": "Draft", "1": "Submitted", "2": "Cancelled"}[str(self.docstatus or 0)]

		if self.per_billed == 100:
			self.status = "Billed"

		if self.salary_slip:
			self.status = "Payslip"

		if self.sales_invoice and self.salary_slip:
			self.status = "Completed"
