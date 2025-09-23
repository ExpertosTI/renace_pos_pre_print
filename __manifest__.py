# -*- coding: utf-8 -*-
# RENACE.TECH - https://renace.tech
# @author: Adderly Marte <adderlymarte@renace.tech>
# License LGPL-3
{
    'name': 'POS Pre Impresión',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Pre Impresión de Recibos""",
    'description': """
          Permite imprimir una pre-cuenta en el punto de venta minorista similar al punto de venta tipo restaurante.
    """,
    'author': 'RENACE.TECH',
    'maintainer': 'Adderly Marte <adderlymarte@renace.tech>',
    'website': 'https://renace.tech',
    'support': 'adderlymarte@renace.tech',
    #'price': 25.00,
    #'currency': 'USD',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
        'pos_restaurant'
    ],
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': [
        'static/description/images/parameters.png',
        'static/description/images/function.png',
        'static/description/images/function_one.png',
        'static/description/images/my_logo.png'
    ],
    'module_type': 'official',
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: