app_name = "mis_3r4cace"
app_title = "Mis 3R4Cace"
app_publisher = "Binyam Abebaw"
app_description = "3R MIS system"
app_color = "grey"
app_email = "binigashaw@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
 	{
 		"name": "mis_3r4cace",
 		"logo": "http://3r4cace.org:8001/files/3rlogod587a2.png",
 		"title": "Mis 3R4Cace"
# 		"route": "/mis_3r4cace",
# 		"has_permission": "mis_3r4cace.api.permission.has_app_permission"
 	}
 ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mis_3r4cace/css/mis_3r4cace.css"
# app_include_js = "/assets/mis_3r4cace/js/mis_3r4cace.js"
app_include_js = [
     "/assets/mis_3r4cace/js/map_defaults.js"
    # ...
]

# include js, css files in header of web template
# web_include_css = "/assets/mis_3r4cace/css/mis_3r4cace.css"
# web_include_js = "/assets/mis_3r4cace/js/mis_3r4cace.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mis_3r4cace/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mis_3r4cace/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mis_3r4cace.utils.jinja_methods",
# 	"filters": "mis_3r4cace.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mis_3r4cace.install.before_install"
# after_install = "mis_3r4cace.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mis_3r4cace.uninstall.before_uninstall"
# after_uninstall = "mis_3r4cace.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mis_3r4cace.utils.before_app_install"
# after_app_install = "mis_3r4cace.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mis_3r4cace.utils.before_app_uninstall"
# after_app_uninstall = "mis_3r4cace.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mis_3r4cace.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mis_3r4cace.tasks.all"
# 	],
# 	"daily": [
# 		"mis_3r4cace.tasks.daily"
# 	],
# 	"hourly": [
# 		"mis_3r4cace.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mis_3r4cace.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mis_3r4cace.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mis_3r4cace.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mis_3r4cace.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mis_3r4cace.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mis_3r4cace.utils.before_request"]
# after_request = ["mis_3r4cace.utils.after_request"]

# Job Events
# ----------
# before_job = ["mis_3r4cace.utils.before_job"]
# after_job = ["mis_3r4cace.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mis_3r4cace.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

