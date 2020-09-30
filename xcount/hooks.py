# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "xcount"
app_title = "Xcount"
app_publisher = "XLevel Retail Systems Nigeria Ltd"
app_description = "Inventory reconciliation app for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@xlevelretail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xcount/css/xcount.css"
# app_include_js = "/assets/xcount/js/xcount.js"

# include js, css files in header of web template
# web_include_css = "/assets/xcount/css/xcount.css"
# web_include_js = "/assets/xcount/js/xcount.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Stock Reconciliation" : "public/js/stock_reconciliation.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "xcount.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "xcount.install.before_install"
# after_install = "xcount.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xcount.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Stock Reconciliation": {
		"before_submit": "xcount.events.stock_reconciliation.validate_items_and_stock_sheets"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xcount.tasks.all"
# 	],
# 	"daily": [
# 		"xcount.tasks.daily"
# 	],
# 	"hourly": [
# 		"xcount.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xcount.tasks.weekly"
# 	]
# 	"monthly": [
# 		"xcount.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "xcount.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xcount.event.get_events"
# }

