# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 Callino - Wolfgang Pichler
#    (<http://www.agilebg.com>)
#    @author Alex Comba <alex.comba@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Delivery Optional Delivery Line",
    'version': '9.0.0',
    'category': 'Sales Management',
    'description': """
This module does allow you do not automatically add a delivery line on sale orders
    """,
    'author': "Callino Software Engineering",
    'website': 'http://www.callino.at',
    'license': 'AGPL-3',
    'depends': [
        'delivery',
    ],
    'data': [
        'delivery_view.xml',
    ],
    'installable': True
}
