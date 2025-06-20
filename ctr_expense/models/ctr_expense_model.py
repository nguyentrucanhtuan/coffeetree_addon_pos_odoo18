from odoo import models, fields

class CtrExpense(models.Model):
    _name = "ctr.expense"
    _description = "Chi phí nội bộ"

    name = fields.Char(string="Tên chi phí", required=True)
    date = fields.Datetime(string="Ngày giờ chi", required=True, default=fields.Datetime.now)
    amount = fields.Float(string="Số tiền", required=True)
    expense_type_id = fields.Many2one('expense.type', string="Loại chi phí", required=True)
    note = fields.Text(string="Ghi chú")
    payment_type = fields.Selection([
        ('cash', 'Tiền mặt'),
        ('bank', 'Chuyển khoản'),
    ], string="Loại thanh toán", default='cash', required=True)
