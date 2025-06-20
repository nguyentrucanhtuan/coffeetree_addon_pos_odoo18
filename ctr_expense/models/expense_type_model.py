from odoo import models, fields, api

class ExpenseType(models.Model):
    _name = "expense.type"
    _description = "Loại chi phí"

    name = fields.Char(string="Tên loại chi phí", required=True)
    code = fields.Char(string="Mã loại chi phí", required=True)
    description = fields.Text(string="Mô tả")
    active = fields.Boolean(string="Hoạt động", default=True)
    expense_count = fields.Integer(string="Số lượng chi phí", compute='_compute_expense_count')
    total_amount = fields.Float(string="Tổng chi phí", compute='_compute_total_amount')

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Mã loại chi phí phải là duy nhất!')
    ]

    @api.depends('expense_ids')
    def _compute_expense_count(self):
        for record in self:
            record.expense_count = len(record.expense_ids)

    @api.depends('expense_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.expense_ids.mapped('amount'))

    expense_ids = fields.One2many('ctr.expense', 'expense_type_id', string='Chi phí') 