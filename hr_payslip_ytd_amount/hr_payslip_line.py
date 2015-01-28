# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp


class hr_payslip_line(orm.Model):
    _inherit = 'hr.payslip.line'
    _columns = {
        'total_ytd': fields.float(
            'Total Year-to-date',
            digits_compute=dp.get_precision('Payroll'))
    }

    def name_get(self, cr, uid, ids, context=None):
        """
        Translate payslip line name in order to get a translated payslip
        """
        res = super(hr_payslip_line, self).name_get(
            cr, uid, ids, context=context)

        return [(line[0], _(line[1])) for line in res]
