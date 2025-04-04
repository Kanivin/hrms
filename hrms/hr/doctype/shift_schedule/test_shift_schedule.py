# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase

# On FrappeTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class TestShiftSchedule(FrappeTestCase):
	"""
	Integration tests for ShiftSchedule.
	Use this class for testing interactions between multiple components.
	"""

	pass
