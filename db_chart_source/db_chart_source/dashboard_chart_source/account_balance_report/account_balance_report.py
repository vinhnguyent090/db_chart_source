# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
from itertools import groupby
from operator import itemgetter
import frappe
from frappe.core.page.dashboard.dashboard import cache_source
from frappe.utils import add_to_date, date_diff, getdate, nowdate
from erpnext.accounts.report.financial_statements import (get_period_list, get_columns, get_data)
from erpnext.accounts.report.profit_and_loss_statement.profit_and_loss_statement import get_net_profit_loss

@frappe.whitelist()
@cache_source
def get(filters=None):
	company = filters.get("company")

	to_date = nowdate()
	filters = frappe._dict({
		"from_fiscal_year" : 2019,
		"to_fiscal_year" : 2019,
		"periodicity": "Monthly",
		"accumulated_values": 1,
		"company": company
	})

	period_list = get_period_list(filters.from_fiscal_year, filters.to_fiscal_year,
		filters.periodicity, filters.accumulated_values, filters.company)

	income = get_data(filters.company, "Income", "Credit", period_list, filters = filters,
		accumulated_values=filters.accumulated_values,
		ignore_closing_entries=True, ignore_accumulated_values_for_fy= True)

	expense = get_data(filters.company, "Expense", "Debit", period_list, filters=filters,
		accumulated_values=filters.accumulated_values,
		ignore_closing_entries=True, ignore_accumulated_values_for_fy= True)

	net_profit_loss = get_net_profit_loss(income, expense, period_list, filters.company, filters.presentation_currency)

	data = []
	data.extend(income or [])
	data.extend(expense or [])
	if net_profit_loss:
		data.append(net_profit_loss)

	columns = get_columns(filters.periodicity, period_list, filters.accumulated_values, filters.company)

	chart = get_chart_data(filters, columns, income, expense, net_profit_loss)

	return columns, data, None, chart



def get_chart_data(filters, columns, income, expense, net_profit_loss):
	labels = [d.get("label") for d in columns[2:]]

	income_data, expense_data, net_profit = [], [], []

	for p in columns[2:]:
		if income:
			income_data.append(income[-2].get(p.get("fieldname")))
		if expense:
			expense_data.append(expense[-2].get(p.get("fieldname")))
		if net_profit_loss:
			net_profit.append(net_profit_loss.get(p.get("fieldname")))

	datasets = []
	if income_data:
		datasets.append({'name': 'Income', 'values': income_data})
	if expense_data:
		datasets.append({'name': 'Expense', 'values': expense_data})
	if net_profit:
		datasets.append({'name': 'Net Profit/Loss', 'values': net_profit})

	chart = {
		"data": {
			'labels': labels,
			'datasets': datasets
		}
	}

	if not filters.accumulated_values:
		chart["type"] = "bar"
	else:
		chart["type"] = "line"

	return chart
