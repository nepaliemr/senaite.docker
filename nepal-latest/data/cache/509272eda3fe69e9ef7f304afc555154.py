# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.spotlight/src/senaite/app/spotlight/templates/spotlight_viewlet.pt'

__tokens = {47: (u'string:${view/css_class}', 2, 27), 99: (u' string:${view/css_style', 3, 26), 1925: (u'context/@@plone_portal_state/portal', 70, 23), 1986: (u'string:${portal/absolute_url}/++resource++senaite.app.spotlight.static/js/senaite.app.spotlight.js', 71, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574270391760 = {u'id': u'search-results-wrapper', u'class': u'col-sm-12', }
_static_140574266169104 = {u'class': u'row', }
_static_140574270599632 = {u'class': u'', }
_static_140574255168848 = {u'href': u'<%- url %>', u'class': u'link', }
_static_140574284374544 = {u'style': u'string:${view/css_style}', u'id': u'spotlight', u'class': u'string:${view/css_class}', }
_static_140574266169040 = {u'name': u'spotlight-search-field', u'placeholder': u'Search', u'value': u'', u'class': u'form-control form-control-lg', u'autocomplete': u'off', u'autofocus': '', u'type': u'text', u'id': u'spotlight-search-field', }
_static_140574268004496 = {u'src': u'#', u'type': u'text/javascript', }
_static_140574442558096 = {}
_static_140574257196880 = {u'class': u'input-group col-sm-12', }
_static_140574270169680 = {u'class': u'input-group-append', }
_static_140574268916880 = {u'id': u'spotlight-search-form', u'name': u'spotlight-searchform', }
_static_140574270569808 = {u'type': u'button', u'id': u'spotlight-clear-button', u'class': u'btn btn-secondary btn-lg', }
_static_140574270301712 = {u'class': u'fas fa-times', }
_static_140574282112272 = {u'href': u'<%- parent_url %>', u'class': u'link', }
_static_140574270167056 = {u'href': u'<%- url %>', u'class': u'link', }
_static_140574397981968 = __compile_zt_expr
_static_140574257193552 = {u'id': u'search-field', u'class': u'row', }
_static_140574284436304 = {u'type': u'text/template', u'id': u'item-template', }
_static_140574268022224 = {u'type': u'text/template', u'id': u'results-template', }

import re
import functools
from itertools import chain as __chain
from sys import exc_clear as __exc_clear
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_4_8_10_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        decode = econtext['__decode']
        convert = econtext['__convert']
        translate = econtext['__translate']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fda0048e210> name=None at 7fda0048ec50> -> __attrs_140574268918288
            __attrs_140574268918288 = _static_140574284374544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="spotlight"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268917264
            __default_140574268917264 = _DEFAULT_MARKER

            # <Substitution u'string:${view/css_class}' (2:27)> -> __attr_class
            __token = 47
            try:
                __zt_tmp = __attrs_140574268918288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140574397981968('string', u'${view/css_class}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268919312
            __default_140574268919312 = _DEFAULT_MARKER

            # <Substitution u'string:${view/css_style}' (3:26)> -> __attr_style
            __token = 99
            try:
                __zt_tmp = __attrs_140574268918288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140574397981968('string', u'${view/css_style}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))
            __append(u'>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff5d0490> name=None at 7fd9ff5d0ad0> -> __attrs_140574268917968
            __attrs_140574268917968 = _static_140574268916880

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form id="spotlight-search-form" name="spotlight-searchform">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa2250> name=None at 7fd9ff5d06d0> -> __attrs_140574257195600
            __attrs_140574257195600 = _static_140574257193552

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="search-field" class="row">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa2f50> name=None at 7fd9feaa2ad0> -> __attrs_140574257195216
            __attrs_140574257195216 = _static_140574257196880

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group col-sm-12">\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff3316d0> name=None at 7fd9ff331610> -> __attrs_140574270172624
            __attrs_140574270172624 = _static_140574266169040
            __previous_i18n_domain_140574270172176 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input id="spotlight-search-field" autofocus autocomplete="off" class="form-control form-control-lg" name="spotlight-search-field" type="text" value=""')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270169488
            __default_140574270169488 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff7027d0> at 7fd9ff702b90> -> __attr_placeholder
            __attr_placeholder = u'Search'
            __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_placeholder is not None):
                __append((u' placeholder="%s"' % __attr_placeholder))
            __append(u'/>')
            __i18n_domain = __previous_i18n_domain_140574270172176
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff702250> name=None at 7fd9ff702e50> -> __attrs_140574270569552
            __attrs_140574270569552 = _static_140574270169680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-append">\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9ff763d50> name=None at 7fd9ff763e90> -> __attrs_140574270300304
            __attrs_140574270300304 = _static_140574270569808

            # <button ... (0:0)
            # --------------------------------------------------------
            __append(u'<button id="spotlight-clear-button" class="btn btn-secondary btn-lg" type="button">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9ff722610> name=None at 7fd9ff722750> -> __attrs_140574270390864
            __attrs_140574270390864 = _static_140574270301712

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-times"></i>\n          </button>\n        </div>\n      </div>\n    </div>\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff331710> name=None at 7fd9feaa2fd0> -> __attrs_140574270390928
            __attrs_140574270390928 = _static_140574266169104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff7385d0> name=None at 7fd9ff738310> -> __attrs_140574268018896
            __attrs_140574268018896 = _static_140574270391760

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="search-results-wrapper" class="col-sm-12"></div>\n    </div>\n  </form>\n\n  <!-- Backbone Templates -->\n\n  <!-- Result Table Template -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4f5dd0> name=None at 7fd9ff4f5f50> -> __attrs_140574270601936
            __attrs_140574270601936 = _static_140574268022224

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/template" id="results-template">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff76b1d0> name=None at 7fd9ff76b590> -> __attrs_140574270602960
            __attrs_140574270602960 = _static_140574270599632

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u"<table class=''>\n      ")

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284437392
            __attrs_140574284437392 = _static_140574442558096

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append(u'<thead>\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284438288
            __attrs_140574284438288 = _static_140574442558096

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268003984
            __attrs_140574268003984 = _static_140574442558096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th></th>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268004816
            __attrs_140574268004816 = _static_140574442558096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th>')
            __stream_140574268004176 = []
            __append_140574268004176 = __stream_140574268004176.append
            __append_140574268004176(u'Title')
            __msgid_140574268004176 = __re_whitespace(''.join(__stream_140574268004176)).strip()
            if __msgid_140574268004176:
                __append(translate(__msgid_140574268004176, mapping=None, default=__msgid_140574268004176, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268004752
            __attrs_140574268004752 = _static_140574442558096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th>')
            __stream_140574268004048 = []
            __append_140574268004048 = __stream_140574268004048.append
            __append_140574268004048(u'ID')
            __msgid_140574268004048 = __re_whitespace(''.join(__stream_140574268004048)).strip()
            if __msgid_140574268004048:
                __append(translate(__msgid_140574268004048, mapping=None, default=__msgid_140574268004048, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268941776
            __attrs_140574268941776 = _static_140574442558096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th>')
            __stream_140574268942672 = []
            __append_140574268942672 = __stream_140574268942672.append
            __append_140574268942672(u'Location')
            __msgid_140574268942672 = __re_whitespace(''.join(__stream_140574268942672)).strip()
            if __msgid_140574268942672:
                __append(translate(__msgid_140574268942672, mapping=None, default=__msgid_140574268942672, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268940752
            __attrs_140574268940752 = _static_140574442558096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th>')
            __stream_140574268943248 = []
            __append_140574268943248 = __stream_140574268943248.append
            __append_140574268943248(u'Description')
            __msgid_140574268943248 = __re_whitespace(''.join(__stream_140574268943248)).strip()
            if __msgid_140574268943248:
                __append(translate(__msgid_140574268943248, mapping=None, default=__msgid_140574268943248, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n        </tr>\n      </thead>\n    </table>\n  </script>\n\n  <!-- Result Row Template -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda0049d350> name=None at 7fda0049dc90> -> __attrs_140574268942352
            __attrs_140574268942352 = _static_140574284436304

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/template" id="item-template">\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270168784
            __attrs_140574270168784 = _static_140574442558096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n      <%= icon %>\n    </td>\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270166480
            __attrs_140574270166480 = _static_140574442558096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff701810> name=None at 7fd9ff701350> -> __attrs_140574255168016
            __attrs_140574255168016 = _static_140574270167056

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="link" href="<%- url %>"><%- title_or_id %></a>\n    </td>\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255166736
            __attrs_140574255166736 = _static_140574442558096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9fe8b3d50> name=None at 7fd9fe8b3350> -> __attrs_140574255166672
            __attrs_140574255166672 = _static_140574255168848

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="link" href="<%- url %>"><%- id %></a>\n    </td>\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255167888
            __attrs_140574255167888 = _static_140574442558096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n      ')

            # <Static value=<_ast.Dict object at 0x7fda00265d10> name=None at 7fda00265890> -> __attrs_140574268983568
            __attrs_140574268983568 = _static_140574282112272

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="link" href="<%- parent_url %>"><%- parent_title %></a>\n    </td>\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268985104
            __attrs_140574268985104 = _static_140574442558096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266168656
            __attrs_140574266168656 = _static_140574442558096

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span><%- description %></span>\n    </td>\n  </script>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4f1890> name=None at 7fd9ff4f1e10> -> __attrs_140574270600080
            __attrs_140574270600080 = _static_140574268004496
            __backup_portal_140574270570384 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (70:23)> -> __value
            __token = 1925
            try:
                __zt_tmp = __attrs_140574270600080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal'] = __value

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284377040
            __default_140574284377040 = _DEFAULT_MARKER

            # <Substitution u'string:${portal/absolute_url}/++resource++senaite.app.spotlight.static/js/senaite.app.spotlight.js' (71:24)> -> __attr_src
            __token = 1986
            try:
                __zt_tmp = __attrs_140574270600080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${portal/absolute_url}/++resource++senaite.app.spotlight.static/js/senaite.app.spotlight.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u' type="text/javascript">\n  </script>')
            if (__backup_portal_140574270570384 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140574270570384
            __append(u'\n\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }