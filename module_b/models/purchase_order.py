# # # Copyright (C) 2021-Today: GRAP (<http://www.grap.coop/>)
# # # @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# # # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# from odoo import api, models


# class PurchaseOrder(models.Model):
#     _inherit = "purchase.order"

#     def function_B_overloaded_no_redecorated(self):
#         return super().function_B_overloaded_no_redecorated()

#     @api.allowed_groups("base.group_multi_currency")
#     def function_C_overloaded_with_new_group(self):
#         return super().function_C_overloaded_with_new_group()

#     @api.allowed_groups()
#     def function_D_overloaded_group_removed(self):
#         return super().function_D_overloaded_group_removed()