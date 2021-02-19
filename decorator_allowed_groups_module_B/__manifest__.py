# Copyright (C) 2021-Today: GRAP (<http://www.grap.coop/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Test Module B",
    'summary': """Dummy module for test""",
    'author': 'GRAP, Odoo Community Association (OCA)',
    'website': "https://github.com/OCA/server-tools/",
    'category': 'Technical',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'decorator_allowed_groups_module_A',
    ],
    'installable': True
}