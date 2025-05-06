# Copyright (c) 2025, Binyam Abebaw and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestESRMData(UnitTestCase):
	"""
	Unit tests for ESRMData.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestESRMData(IntegrationTestCase):
	"""
	Integration tests for ESRMData.
	Use this class for testing interactions between multiple components.
	"""

	pass
