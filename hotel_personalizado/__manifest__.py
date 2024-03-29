# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Hotel Personalizado',
    'version': '10.0.1.1.0',
    'author': 'Anderson Martinez',
    'category': 'Generic Modules/Hotel',
    'website': '',
    'depends': ['hotel', 'hotel_folio_payment', 'hotel_restaurant'],
    'license': 'AGPL-3',
    'demo': [

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_personalizado.xml',
        'report/reservation_report.xml',
        'report/reservation_report_templates.xml',
        'report/invoice_report.xml'

    ],
    'images': ['static/description/logo.png'],
    'installable': True,
    'auto_install': False,
}
