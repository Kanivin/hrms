// Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Attendance", {
	refresh(frm) {
		if (frm.doc.__islocal && !frm.doc.attendance_date) {
			frm.set_value("attendance_date", frappe.datetime.get_today());
		}

		frm.set_query("employee", () => {
			return {
				query: "kanierp.controllers.queries.employee_query",
			};
		});
	},
});
