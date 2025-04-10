// Copyright (c) 2025, Binyam Abebaw and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Subproject Beneficiary", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Subproject Beneficiary', {
    kebele: function(frm) {
        frm.set_query('subproject', function() {
            return {
                filters: {
                    kebele: frm.doc.kebele
                }
            };
        });
    }
});