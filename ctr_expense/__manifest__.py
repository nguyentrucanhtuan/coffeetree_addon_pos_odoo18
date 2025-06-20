{
    'name': 'Chi phí nội bộ',
    'version': '1.0',
    'summary': 'Quản lý chi phí vận hành nội bộ',
    'author': 'CoffeeTree',
    'category': 'Accounting',
    'depends': ['base'],
    'data': [
        'views/expense_views.xml',
        'views/expense_type_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
