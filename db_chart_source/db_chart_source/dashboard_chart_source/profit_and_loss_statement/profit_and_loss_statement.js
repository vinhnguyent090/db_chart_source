frappe.dashboard_chart_sources["Profit and Loss Statement"] = {
	"method_path": "db_chart_source.db_chart_source.dashboard_chart_source.profit_and_loss_statement.profit_and_loss_statement.get",
	"filters": [
		{
			"fieldname": "company",
			"label": "Company",
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1
		}
		,{
			"fieldname":"from_fiscal_year",
			"label": "Start Year",
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd": 1
		},
		{
			"fieldname":"to_fiscal_year",
			"label": "End Year",
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd": 1
		},
		{
			"fieldname": "periodicity",
			"label": "Periodicity",
			"fieldtype": "Select",
			"options": [
				{ "value": "Monthly", "label": "Monthly" },
				{ "value": "Quarterly", "label": "Quarterly" },
				{ "value": "Half-Yearly", "label": "Half-Yearly" },
				{ "value": "Yearly", "label": "Yearly" }
			],
			"default": "Monthly",
			"reqd": 1
		}
	],
	"is_time_series": true
};
