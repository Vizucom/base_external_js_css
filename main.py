# -*- coding: utf-8 -*-

import openerp.addons.web.controllers.main as main
from openerp.addons.web import http as http
openerpweb = http
from openerp.addons.web.controllers.main import manifest_list, db_monodb_redirect, redirect_with_hash, html_template, module_boot
import simplejson
from extras import css_extras, js_extras

class Home(main.Home):
    _cp_path = '/'

    @openerpweb.httprequest
    def index(self, req, s_action=None, db=None, **kw):
        db, redir = db_monodb_redirect(req)
        if redir:
            return redirect_with_hash(req, redir)

        js = "\n        ".join('<script type="text/javascript" src="%s"></script>' % i for i in manifest_list(req, 'js', db=db))
        css = "\n        ".join('<link rel="stylesheet" href="%s">' % i for i in manifest_list(req, 'css', db=db))

        # Load the extra files
        js += "\n        ".join('<script type="text/javascript" src="%s"></script>' % i for i in js_extras)
        css += "\n        ".join('<link rel="stylesheet" href="%s">' % i for i in css_extras)

        r = html_template % {
            'js': js,
            'css': css,
            'modules': simplejson.dumps(module_boot(req, db=db)),
            'init': 'var wc = new s.web.WebClient();wc.appendTo($(document.body));'
        }
        return r