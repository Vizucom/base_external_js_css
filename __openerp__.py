# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Load external JS/CSS files',
    'category': 'Utility',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['website'],
    'description': """
Load external JS/CSS files
==========================
 * Allows you to specify a list of external JS/CSS files to load from e.g. another server.
 * Doing this in 8.0 is a lot simpler than in 7.0, now you just need to extend a template with the necessary <link> and <script> tags.
""",
    'data': [
        'views/external_resources.xml',
    ],
}
