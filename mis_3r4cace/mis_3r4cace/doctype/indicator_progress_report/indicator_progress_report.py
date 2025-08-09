# Copyright (c) 2025, Binyam Abebaw and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class IndicatorProgressReport(Document):
	def after_insert(self):
		update_indicator_totals(self.name_of_indicator, self.year)

	def on_update_after_submit(self):
		update_indicator_totals(self.name_of_indicator, self.year)
	
	def after_delete(self):
		update_indicator_totals(self.name_of_indicator, self.year)

def update_indicator_totals(indicator_id, fiscal_year):
	# Fetch all progress entries for this indicator
	progress_entries = frappe.get_all(
		"Indicator Progress Report",
		filters={"name_of_indicator": indicator_id, "year":fiscal_year },
		fields=["male", "female"]
	)

	# Sum up male and female values
	male = sum(entry["male"] or 0 for entry in progress_entries)
	female = sum(entry["female"] or 0 for entry in progress_entries)
	total = male + female
    
	# Update the Indicator Report document
	frappe.db.set_value("Indicator Report", {"name_of_indicator": indicator_id, "fiscal_year": fiscal_year},{
		"male": male,
		"female": female,
		"total": total
	})
	#pass
