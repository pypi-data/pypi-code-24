# Copyright 2017 Avoin.Systems
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# noinspection PyStatementEffect
{
    "name": "Report Wkhtmltopdf Param",
    "version": "11.0.1.0.1",
    "license": "AGPL-3",
    "summary": """
        Add new parameters for a paper format to be used by wkhtmltopdf
        command as arguments.
    """,
    "author": "Avoin.Systems,"
              "Eficent,"
              "Odoo Community Association (OCA)",
    "website": "https://avoin.systems",
    "category": "Technical Settings",
    "depends": [
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/paperformat.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "active": False,
}
