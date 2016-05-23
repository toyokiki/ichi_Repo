# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Rooms For (Hong Kong) Limited T/A OSCG
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    'name': 'Report Quotation Standard',
    'category': 'Reporting',
    'version': '9.0.1.0.0',
    'author': 'toyo-kiki',
    'website': 'https://www.toyo-kiki.co.jp/',
    'licence': 'AGPL-3',
    'depends': ['report_aeroo','sale','project'],
    'summary':"""Print Quotation from sales order using Aeroo Report""",
    'description': """
Print Quotaion from sales.order using Aeroo Report
    """,
    'data': [
        'report/report.xml',
    ],
    'installable': True,
    'applitcation': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
