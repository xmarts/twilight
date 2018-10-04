# © 2018 Hibou Corp.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hibou RMAs for Sale Orders',
    'version': '11.0.1.0.0',
    'category': 'Sale',
    'author': "Hibou Corp.",
    'license': 'AGPL-3',
    'website': 'https://hibou.io/',
    'depends': [
        'rma',
        'sale',
        'sales_team',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/rma_views.xml',
        'wizard/rma_lines_views.xml',
    ],
    'demo': [
        'data/rma_demo.xml',
    ],
    'installable': True,
    'application': False,
 }
