# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document

# import frappe
import kanierp


class IncomeTaxSlab(Document):
	def validate(self):
		if self.company:
			self.currency = kanierp.get_company_currency(self.company)
