# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/browser/viewlets/templates/languageselector.pt'

__tokens = {82: (u'view/get_language_info', 3, 29), 128: (u'lang_info/available', 4, 22), 560: (u'lang_info/languages', 15, 31), 606: (u' context/@@plone_context_state/current_base_ur', 16, 25), 690: (u'languages', 17, 33), 738: (u'lang/code', 18, 36), 784: (u' request/QUERY_STRIN', 19, 35), 841: (u"  python:filter(lambda x: x and not x.startswith('set_language'), qs.split('&'", 20, 34), 956: (u'am string:set_language=${co', 21, 33), 1020: (u"ams python:'&'.join(params + [lang_par", 22, 32), 1095: (u'ed   lang/sel', 23, 31), 1145: (u'lass  string:language-$', 24, 30), 1205: (u"ent    python: selected and 'currentLanguage active ", 25, 29), 1302: (u'string:${current}${codeclass}', 26, 35), 1386: (u'lang/native|lang/name', 29, 30), 1444: (u'string:${base_url}?${new_params}', 30, 34), 1502: (u' string:${current} dropdown-ite', 31, 24), 1559: (u'e na', 32, 23), 1599: (u'name', 33, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574133886160 = {u'class': u'string:${current}${codeclass}', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574270574224 = {u'class': u'dropdown', }
_static_140574255111120 = {u'class': u'fas fa-globe', u'aria-hidden': u'true', }
_static_140574254648272 = {u'href': u'', u'class': u'string:${current} dropdown-item', u'title': u'name', }
_static_140574267286480 = {u'class': u'dropdown-menu dropdown-menu-right', }
_static_140574442558096 = {}
_static_140574267355536 = {u'class': u'd-inline-block', }
_static_140574284375312 = {u'data-toggle': u'dropdown', u'aria-haspopup': u'true', u'type': u'button', u'class': u'btn btn-outline-dark btn-sm dropdown-toggle', u'aria-expanded': u'false', }
_static_140574397981968 = __compile_zt_expr
_static_140574267288272 = {u'class': u'caret', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff453190> name=None at 7fd9ff453890> -> __attrs_140574267383760
            __attrs_140574267383760 = _static_140574267355536

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="d-inline-block">\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff764e90> name=None at 7fd9ff764ed0> -> __attrs_140574282110864
            __attrs_140574282110864 = _static_140574270574224
            __backup_lang_info_140574267330512 = get('lang_info', __marker)

            # <Value u'view/get_language_info' (3:29)> -> __value
            __token = 82
            try:
                __zt_tmp = __attrs_140574282110864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/get_language_info', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['lang_info'] = __value

            # <Value u'lang_info/available' (4:22)> -> __condition
            __token = 128
            try:
                __zt_tmp = __attrs_140574282110864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'lang_info/available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574267430288 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="dropdown">\n    ')

                # <Static value=<_ast.Dict object at 0x7fda0048e510> name=None at 7fda0048ed90> -> __attrs_140574255109392
                __attrs_140574255109392 = _static_140574284375312

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button class="btn btn-outline-dark btn-sm dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9fe8a5bd0> name=None at 7fd9fe8a5550> -> __attrs_140574254004496
                __attrs_140574254004496 = _static_140574255111120

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="fas fa-globe" aria-hidden="true"></span>\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff442ad0> name=None at 7fd9ff4424d0> -> __attrs_140574267287952
                __attrs_140574267287952 = _static_140574267288272

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="caret"></span>\n    </button>\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4423d0> name=None at 7fd9ff442f10> -> __attrs_140574133872784
                __attrs_140574133872784 = _static_140574267286480
                __backup_languages_140574123779152 = get('languages', __marker)

                # <Value u'lang_info/languages' (15:31)> -> __value
                __token = 560
                try:
                    __zt_tmp = __attrs_140574133872784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'lang_info/languages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_base_url_140574123780496 = get('base_url', __marker)

                # <Value u'context/@@plone_context_state/current_base_url' (16:25)> -> __value
                __token = 606
                try:
                    __zt_tmp = __attrs_140574133872784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'context/@@plone_context_state/current_base_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['base_url'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="dropdown-menu dropdown-menu-right">\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269062800
                __attrs_140574269062800 = _static_140574442558096
                __backup_lang_140574255167632 = get('lang', __marker)

                # <Value u'languages' (17:33)> -> __iterator
                __token = 690
                try:
                    __zt_tmp = __attrs_140574269062800
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'languages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574269061776, ) = getitem('repeat')(u'lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9f7509cd0> name=None at 7fd9f75093d0> -> __attrs_140574134355664
                    __attrs_140574134355664 = _static_140574133886160
                    __backup_code_140574123780432 = get('code', __marker)

                    # <Value u'lang/code' (18:36)> -> __value
                    __token = 738
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/code', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_qs_140574123780240 = get('qs', __marker)

                    # <Value u'request/QUERY_STRING' (19:35)> -> __value
                    __token = 784
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'request/QUERY_STRING', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['qs'] = __value
                    __backup_params_140574123781264 = get('params', __marker)

                    # <Value u"python:filter(lambda x: x and not x.startswith('set_language'), qs.split('&'))" (20:34)> -> __value
                    __token = 841
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"filter(lambda x: x and not x.startswith('set_language'), qs.split('&'))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['params'] = __value
                    __backup_lang_param_140574123781712 = get('lang_param', __marker)

                    # <Value u'string:set_language=${code}' (21:33)> -> __value
                    __token = 956
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('string', u'set_language=${code}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['lang_param'] = __value
                    __backup_new_params_140574123781648 = get('new_params', __marker)

                    # <Value u"python:'&'.join(params + [lang_param])" (22:32)> -> __value
                    __token = 1020
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"'&'.join(params + [lang_param])", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['new_params'] = __value
                    __backup_selected_140574123751888 = get('selected', __marker)

                    # <Value u'lang/selected' (23:31)> -> __value
                    __token = 1095
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/selected', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_140574123751952 = get('codeclass', __marker)

                    # <Value u'string:language-${code}' (24:30)> -> __value
                    __token = 1145
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('string', u'language-${code}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_140574123751824 = get('current', __marker)

                    # <Value u"python: selected and 'currentLanguage active ' or ''" (25:29)> -> __value
                    __token = 1205
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u" selected and 'currentLanguage active ' or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574253163088
                    __default_140574253163088 = _DEFAULT_MARKER

                    # <Substitution u'string:${current}${codeclass}' (26:35)> -> __attr_class
                    __token = 1302
                    try:
                        __zt_tmp = __attrs_140574134355664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'${current}${codeclass}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe834bd0> name=None at 7fd9fe834610> -> __attrs_140574267458128
                    __attrs_140574267458128 = _static_140574254648272
                    __backup_name_140574123634576 = get('name', __marker)

                    # <Value u'lang/native|lang/name' (29:30)> -> __value
                    __token = 1386
                    try:
                        __zt_tmp = __attrs_140574267458128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/native|lang/name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['name'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256078928
                    __default_140574256078928 = _DEFAULT_MARKER

                    # <Substitution u'string:${base_url}?${new_params}' (30:34)> -> __attr_href
                    __token = 1444
                    try:
                        __zt_tmp = __attrs_140574267458128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${base_url}?${new_params}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256080208
                    __default_140574256080208 = _DEFAULT_MARKER

                    # <Substitution u'string:${current} dropdown-item' (31:24)> -> __attr_class
                    __token = 1502
                    try:
                        __zt_tmp = __attrs_140574267458128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'${current} dropdown-item', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574133619792
                    __default_140574133619792 = _DEFAULT_MARKER

                    # <Substitution u'name' (32:23)> -> __attr_title
                    __token = 1559
                    try:
                        __zt_tmp = __attrs_140574267458128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140574397981968('path', u'name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255631760
                    __attrs_140574255631760 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255629968
                    __default_140574255629968 = _DEFAULT_MARKER

                    # <Value u'name' (33:31)> -> __cache_140574284438224
                    __token = 1599
                    try:
                        __zt_tmp = __attrs_140574255631760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574284438224 = _static_140574397981968('path', u'name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'name' (33:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda0049d790> -> __condition
                    __expression = __cache_140574284438224

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574284438224
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n          </a>')
                    if (__backup_name_140574123634576 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140574123634576
                    __append(u'\n        </div>')
                    if (__backup_current_140574123751824 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_140574123751824
                    if (__backup_codeclass_140574123751952 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_140574123751952
                    if (__backup_selected_140574123751888 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140574123751888
                    if (__backup_new_params_140574123781648 is __marker):
                        del econtext['new_params']
                    else:
                        econtext['new_params'] = __backup_new_params_140574123781648
                    if (__backup_lang_param_140574123781712 is __marker):
                        del econtext['lang_param']
                    else:
                        econtext['lang_param'] = __backup_lang_param_140574123781712
                    if (__backup_params_140574123781264 is __marker):
                        del econtext['params']
                    else:
                        econtext['params'] = __backup_params_140574123781264
                    if (__backup_qs_140574123780240 is __marker):
                        del econtext['qs']
                    else:
                        econtext['qs'] = __backup_qs_140574123780240
                    if (__backup_code_140574123780432 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_140574123780432
                    __append(u'\n      ')
                    ____index_140574269061776 -= 1
                    if (____index_140574269061776 > 0):
                        __append('')
                if (__backup_lang_140574255167632 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140574255167632
                __append(u'\n    </div>')
                if (__backup_base_url_140574123780496 is __marker):
                    del econtext['base_url']
                else:
                    econtext['base_url'] = __backup_base_url_140574123780496
                if (__backup_languages_140574123779152 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_140574123779152
                __append(u'\n  </div>')
                __i18n_domain = __previous_i18n_domain_140574267430288
            if (__backup_lang_info_140574267330512 is __marker):
                del econtext['lang_info']
            else:
                econtext['lang_info'] = __backup_lang_info_140574267330512
            __append(u'\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }