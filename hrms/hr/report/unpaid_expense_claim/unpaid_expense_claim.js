// Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Unpaid Expense Claim"] = {
	filters: [
		{
			fieldname: "employee",
			label: __("Employee"),
			fieldtype: "Link",
			options: "Employee",
		},
	],
};
