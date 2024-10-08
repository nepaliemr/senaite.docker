# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/add_samples.pt'

__tokens = {81: (u'python:view.available()', 2, 20), 244: (u'python:view.get_add_url()', 8, 31), 487: (u'python:view.get_sample_add_number()', 15, 35), 748: (u'view/theme_view/icon_url/plus', 21, 35), 811: (u'python:1', 22, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574266208784 = {u'name': u'ar_count', u'min': u'1', u'max': u'99', u'value': u'python:view.get_sample_add_number()', u'type': u'number', u'class': u'form-control form-control-sm', }
_static_140574284461520 = {u'src': u'#', u'style': u'height:16px;', }
_static_140574267883472 = {u'class': u'add-samples-viewlet d-inline-block align-middle', }
_static_140574442558096 = {}
_static_140574266169040 = {u'class': u'input-group-append', }
_static_140574270216656 = {u'action': u'ar_add', u'method': u'GET', u'class': u'form-inline', }
_static_140574397981968 = __compile_zt_expr
_static_140574266170960 = {u'type': u'submit', u'class': u'btn btn-outline-secondary btn-sm', }
_static_140574266210448 = {u'class': u'input-group', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff4d3fd0> name=None at 7fd9ff4d3110> -> __attrs_140574270217296
            __attrs_140574270217296 = _static_140574267883472

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 81
            try:
                __zt_tmp = __attrs_140574270217296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'view.available()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270214672 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="add-samples-viewlet d-inline-block align-middle">\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff70d9d0> name=None at 7fd9ff70d990> -> __attrs_140574267997904
                __attrs_140574267997904 = _static_140574270216656

                # <form ... (0:0)
                # --------------------------------------------------------
                __append(u'<form method="GET" class="form-inline"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267995536
                __default_140574267995536 = _DEFAULT_MARKER

                # <Substitution u'python:view.get_add_url()' (8:31)> -> __attr_action
                __token = 244
                try:
                    __zt_tmp = __attrs_140574267997904
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140574397981968('python', u'view.get_add_url()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', u'ar_add', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((u' action="%s"' % __attr_action))
                __append(u'>\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff33b890> name=None at 7fd9ff4efc10> -> __attrs_140574266211344
                __attrs_140574266211344 = _static_140574266210448

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff33b210> name=None at 7fd9ff33bc90> -> __attrs_140574266171024
                __attrs_140574266171024 = _static_140574266208784

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="number" name="ar_count" min="1" max="99" class="form-control form-control-sm"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266168016
                __default_140574266168016 = _DEFAULT_MARKER

                # <Substitution u'python:view.get_sample_add_number()' (15:35)> -> __attr_value
                __token = 487
                try:
                    __zt_tmp = __attrs_140574266171024
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140574397981968('python', u'view.get_sample_add_number()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff3316d0> name=None at 7fd9ff3315d0> -> __attrs_140574266167696
                __attrs_140574266167696 = _static_140574266169040

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group-append">\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff331e50> name=None at 7fd9ff331890> -> __attrs_140574284460688
                __attrs_140574284460688 = _static_140574266170960

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="submit" class="btn btn-outline-secondary btn-sm">\n          ')

                # <Static value=<_ast.Dict object at 0x7fda004a35d0> name=None at 7fda004a3590> -> __attrs_140574268005904
                __attrs_140574268005904 = _static_140574284461520

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284461776
                __default_140574284461776 = _DEFAULT_MARKER

                # <Substitution u'view/theme_view/icon_url/plus' (21:35)> -> __attr_src
                __token = 748
                try:
                    __zt_tmp = __attrs_140574268005904
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140574397981968('path', u'view/theme_view/icon_url/plus', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))
                __append(u' style="height:16px;"/>\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268002832
                __attrs_140574268002832 = _static_140574442558096

                # <Negate value=<Value u'python:1' (22:30)> at 7fd9ff4f1bd0> -> __cache_140574268005328

                # <Value u'python:1' (22:30)> -> __cache_140574268005328
                __token = 811
                try:
                    __zt_tmp = __attrs_140574268002832
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574268005328 = _static_140574397981968('python', u'1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __cache_140574268005328 = not __cache_140574268005328
                __condition = __cache_140574268005328
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                __stream_140574268003536 = []
                __append_140574268003536 = __stream_140574268003536.append
                __append_140574268003536(u'Add Samples')
                __msgid_140574268003536 = __re_whitespace(''.join(__stream_140574268003536)).strip()
                if __msgid_140574268003536:
                    __append(translate(__msgid_140574268003536, mapping=None, default=__msgid_140574268003536, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __condition = __cache_140574268005328
                if __condition:
                    __append(u'</span>')
                __append(u'\n        </button>\n      </span>\n    </span>\n  </form>\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140574270214672
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }