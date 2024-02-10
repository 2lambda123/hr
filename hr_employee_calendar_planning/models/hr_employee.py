# -*- coding: utf-8 -*-
# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    calendar_ids = fields.One2many(
        comodel_name="hr.employee.calendar",
        inverse_name="employee_id",
        string="Calendar planning",
    )

    def _regenerate_calendar(self):
        """Regenerates the employee's calendar based on their assigned work schedule.
        Parameters:
            - self (object): The current employee record.
        Returns:
            - None: The function does not return any value.
        Processing Logic:
            - Creates a new resource calendar if the employee does not have one or if their current calendar is active.
            - Deletes all existing attendance lines in the employee's calendar.
            - Loops through each work schedule assigned to the employee.
            - For each work schedule, loops through the attendance lines in the corresponding resource calendar.
            - Creates a new attendance line in the employee's calendar with the same details as the corresponding line in the resource calendar.
            - The attendance line's date range is set to match the work schedule's start and end dates."""
        
        self.ensure_one()
        if not self.calendar_id or self.calendar_id.active:
            self.calendar_id = self.env['resource.calendar'].create({
                'active': False,
                'name': _(
                    'Auto generated calendar for employee'
                ) + ' %s' % self.id,
            }).id
        else:
            self.calendar_id.attendance_ids.unlink()
        vals_list = []
        for line in self.calendar_ids:
            for calendar_line in line.calendar_id.attendance_ids:
                vals_list.append((0, 0, {
                    'name': calendar_line.name,
                    'dayofweek': calendar_line.dayofweek,
                    'hour_from': calendar_line.hour_from,
                    'hour_to': calendar_line.hour_to,
                    'date_from': line.date_start,
                    'date_to': line.date_end,
                }))
        self.calendar_id.attendance_ids = vals_list


class HrEmployeeCalendar(models.Model):
    _name = 'hr.employee.calendar'

    date_start = fields.Date(
        string="Start",
    )
    date_end = fields.Date(
        string="End",
    )
    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Employee",
        required=True,
    )
    calendar_id = fields.Many2one(
        comodel_name="resource.calendar",
        string="Working Time",
        required=True,
    )

    _sql_constraints = [
        ('date_consistency',
         'CHECK(date_start <= date_end)',
         'Date end should be higher than date start'),
    ]

    @api.constrains('date_start', 'date_end')
    def _check_date(self):
        """Employee calendars should not overlap"""
        for calendar in self:
            domain = [
                ('date_start', '<=', calendar.date_end),
                ('date_end', '>=', calendar.date_start),
                ('employee_id', '=', calendar.employee_id.id),
                ('id', '!=', calendar.id),
            ]
            if ncalendars := self.search_count(domain):
                raise ValidationError(_(
                    "You can't have 2 overlaping calendars!"))

    def create(self, vals):
        """"Creates a new record for an employee's calendar and regenerates the calendar for that employee."
        Parameters:
            - vals (dict): A dictionary containing the values for the new record.
        Returns:
            - record (object): The newly created record for the employee's calendar.
        Processing Logic:
            - Calls the create method from the parent class.
            - Regenerates the calendar for the employee.
            - Returns the newly created record."""
        
        record = super(HrEmployeeCalendar, self).create(vals)
        record.employee_id._regenerate_calendar()
        return record

    def write(self, vals):
        """"Updates the values of the current record and regenerates the calendar for the related employee(s)."
        Parameters:
            - vals (dict): Dictionary of fields to update.
        Returns:
            - bool: True if the record is successfully updated, False otherwise.
        Processing Logic:
            - Calls the write method of the parent class.
            - Loops through the mapped employee(s).
            - Calls the _regenerate_calendar method for each employee.
            - Returns the result of the write method."""
        
        res = super(HrEmployeeCalendar, self).write(vals)
        for employee in self.mapped('employee_id'):
            employee._regenerate_calendar()
        return res
