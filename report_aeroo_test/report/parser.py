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

import logging
logger = logging.getLogger('report_aeroo')

from openerp.report import report_sxw
from openerp.report.report_sxw import rml_parse

class Parser(rml_parse):
    def __init__(self, cr, uid, name, context):
        super(self.__class__, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'hello_world': self.hello_world,
        })

    def hello_world(self, name):
        return "Hello, %s!" % name

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
