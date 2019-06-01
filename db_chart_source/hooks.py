# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "db_chart_source"
app_title = "Db Chart Source"
app_publisher = "vinhnguyen.t090@gmail.com"
app_description = "Dashboard Chart Source"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vinhnguyen.t090@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/db_chart_source/css/db_chart_source.css"
# app_include_js = "/assets/db_chart_source/js/db_chart_source.js"

# include js, css files in header of web template
# web_include_css = "/assets/db_chart_source/css/db_chart_source.css"
# web_include_js = "/assets/db_chart_source/js/db_chart_source.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
# get_website_user_home_page = "db_chart_source.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "db_chart_source.install.before_install"
# after_install = "db_chart_source.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "db_chart_source.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"db_chart_source.tasks.all"
# 	],
# 	"daily": [
# 		"db_chart_source.tasks.daily"
# 	],
# 	"hourly": [
# 		"db_chart_source.tasks.hourly"
# 	],
# 	"weekly": [
# 		"db_chart_source.tasks.weekly"
# 	]
# 	"monthly": [
# 		"db_chart_source.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "db_chart_source.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "db_chart_source.event.get_events"
# }

