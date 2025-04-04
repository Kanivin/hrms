# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# MIT License. See license.txt


import frappe


def execute():
	frappe.reload_doc("setup", "doctype", "employee")

	if frappe.db.has_column("Employee", "reason_for_resignation"):
		frappe.db.sql(
			""" UPDATE `tabEmployee`
            SET reason_for_leaving = reason_for_resignation
            WHERE status = 'Left' and reason_for_leaving is null and reason_for_resignation is not null
        """
		)
