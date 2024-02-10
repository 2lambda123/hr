# -*- coding: utf-8 -*-
# © 2014 Eficent
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrPayslipEmployees(models.TransientModel):

    _inherit = 'hr.payslip.employees'

    @api.multi
    def compute_sheet(self):
        """Computes the payslip sheet for employees.
        Parameters:
            - self (object): The current object.
        Returns:
            - res (object): The result of the computation.
        Processing Logic:
            - Get the payslip run from the context.
            - If a move date is provided, find the corresponding period.
            - Update the payslip's move date and period.
            - Return the result of the computation."""
        

        res = super(HrPayslipEmployees, self).compute_sheet()
        payslip_run = self.env['hr.payslip.run'].browse(
            self.env.context['active_id'])
        if move_date := payslip_run.move_date:
            period_obj = self.env['account.period']
            if period_ids := period_obj.find(dt=move_date):
                period_id = period_ids[0]
            else:
                period_id = False
            payslip_run.slip_ids.write({
                'move_date': move_date,
                'period_id': period_id.id,
            })
        return res
