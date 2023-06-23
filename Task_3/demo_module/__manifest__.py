{
    'name': 'Demo Module',
    'version': '1.0',
    'summary': 'Demo Module for Odoo 16',
    'description': 'A demo module with object demo.demo and views.',
    'depends': ['base'],
    'author': 'Serhii Miroshnychenko',
    'license': 'LGPL-3',
    'data': [
        'views/demo_demo_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}