# -*- coding: utf-8 -*-
{
    'name': "Botón de Impresión de Factura POS",
    'author': 'Adderly Marte',
    'website': 'https://renace.tech',
    'maintainer': 'Adderly Marte',
    'version': '18.0.0.1',
    'category': 'Punto de Venta',
    'sequence': 75,
    'summary': 'Botón de Impresión de Factura POS cerca del Botón de Acción',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'renace_pos_pre_print/static/src/js/pos_print_bill_button.js',
            'renace_pos_pre_print/static/src/xml/pos_print_bill_button.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}
