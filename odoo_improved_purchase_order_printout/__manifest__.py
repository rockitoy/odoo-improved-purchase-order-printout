# -*- coding: utf-8 -*-
# Copyright (C) 2019-present  Technaureus Info Solutions(<http://www.technaureus.com/>)

{
    'name': 'Odoo Improved Purchase order Printout',
    'version': '12.0.0.0',
    'category': 'Purchases',
    'summary': 'Purchase order Shipping Address',
    'description': 'Shipping Address in Purchase Order Print',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'depends': ['purchase', 'purchase_requisition'],
    'data': [
        'report/purchase_order_templates.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
