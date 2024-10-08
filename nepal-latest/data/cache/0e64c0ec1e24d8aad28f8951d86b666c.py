# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/languageselector.pt'

__tokens = {29: (u'view/available', 1, 29), 473: (u'view/languages', 18, 30), 517: (u' context/@@plone_context_state/current_base_ur', 19, 28), 602: (u'languages', 21, 33), 645: (u'lang/code', 23, 30), 683: (u' request/QUERY_STRIN', 24, 27), 736: (u"s python:filter(lambda x: x and not x.startswith('set_language'), qs.split('&'", 25, 30), 851: (u'am string:set_language=${co', 26, 33), 915: (u"ams python:'&'.join(params + [lang_par", 27, 32), 988: (u'cted lang/sel', 28, 29), 1037: (u'class string:language-$', 29, 29), 1094: (u"urrent python: selected and 'currentLanguage active dropdown-item' or 'dropdow", 30, 26), 1211: (u"nt_item python: selected and 'text-ligh", 31, 30), 1296: (u'string:${codeclass} ${current}', 32, 35), 1381: (u'lang/native|lang/name', 34, 30), 1439: (u'string:${base_url}?${new_params}', 35, 34), 1507: (u' string:${current_item} text-decoration-non', 36, 34), 1586: (u'e na', 37, 33), 1626: (u'name', 38, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574267989008 = {u'class': u'dropdown', }
_static_140574442558096 = {}
_static_140574268005904 = {u'aria-labelledby': u'portal-languageselector', u'role': u'menu', u'class': u'dropdown-menu dropdown-menu-right', }
_static_140574284370384 = {u'href': u'#', u'class': u'string:${current_item} text-decoration-none', u'title': u'name', }
_static_140574268006160 = {u'class': u'fas fa-globe', }
_static_140574397981968 = __compile_zt_expr
_static_140574284371600 = {u'class': u'string:${codeclass} ${current}', }
_static_140574270229520 = {u'data-toggle': u'dropdown', u'href': u'#', u'class': u'nav-link dropdown-toggle', u'aria-expanded': u'false', u'aria-haspopup': u'true', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267988944
            __attrs_140574267988944 = _static_140574442558096

            # <Value u'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_140574267988944
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'view/available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4edc10> name=None at 7fd9ff4ed1d0> -> __attrs_140574267988304
                __attrs_140574267988304 = _static_140574267989008

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav class="dropdown">\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff710c10> name=None at 7fd9ff710b50> -> __attrs_140574270227728
                __attrs_140574270227728 = _static_140574270229520
                __previous_i18n_domain_140574270230032 = __i18n_domain
                __i18n_domain = u'plone'

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f1f10> name=None at 7fd9ff4f1490> -> __attrs_140574268004176
                __attrs_140574268004176 = _static_140574268006160

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-globe"></i>\n    </a>')
                __i18n_domain = __previous_i18n_domain_140574270230032
                __append(u'\n\n    <!-- Available Languages -->\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f1e10> name=None at 7fd9ff4f1650> -> __attrs_140574268006288
                __attrs_140574268006288 = _static_140574268005904
                __backup_languages_140574284461840 = get('languages', __marker)

                # <Value u'view/languages' (18:30)> -> __value
                __token = 473
                try:
                    __zt_tmp = __attrs_140574268006288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/languages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_base_url_140574275597520 = get('base_url', __marker)

                # <Value u'context/@@plone_context_state/current_base_url' (19:28)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_140574268006288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'context/@@plone_context_state/current_base_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['base_url'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="dropdown-menu dropdown-menu-right" role="menu" aria-labelledby="portal-languageselector">\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284372304
                __attrs_140574284372304 = _static_140574442558096
                __backup_lang_140574275637136 = get('lang', __marker)

                # <Value u'languages' (21:33)> -> __iterator
                __token = 602
                try:
                    __zt_tmp = __attrs_140574284372304
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'languages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574284370896, ) = getitem('repeat')(u'lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda0048d690> name=None at 7fda0048da10> -> __attrs_140574270227280
                    __attrs_140574270227280 = _static_140574284371600
                    __backup_code_140574270171152 = get('code', __marker)

                    # <Value u'lang/code' (23:30)> -> __value
                    __token = 645
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/code', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_qs_140574284389264 = get('qs', __marker)

                    # <Value u'request/QUERY_STRING' (24:27)> -> __value
                    __token = 683
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'request/QUERY_STRING', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['qs'] = __value
                    __backup_params_140574284358032 = get('params', __marker)

                    # <Value u"python:filter(lambda x: x and not x.startswith('set_language'), qs.split('&'))" (25:30)> -> __value
                    __token = 736
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"filter(lambda x: x and not x.startswith('set_language'), qs.split('&'))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['params'] = __value
                    __backup_lang_param_140574270397200 = get('lang_param', __marker)

                    # <Value u'string:set_language=${code}' (26:33)> -> __value
                    __token = 851
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('string', u'set_language=${code}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['lang_param'] = __value
                    __backup_new_params_140574284463952 = get('new_params', __marker)

                    # <Value u"python:'&'.join(params + [lang_param])" (27:32)> -> __value
                    __token = 915
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"'&'.join(params + [lang_param])", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['new_params'] = __value
                    __backup_selected_140574284460496 = get('selected', __marker)

                    # <Value u'lang/selected' (28:29)> -> __value
                    __token = 988
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/selected', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_140574284463376 = get('codeclass', __marker)

                    # <Value u'string:language-${code}' (29:29)> -> __value
                    __token = 1037
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('string', u'language-${code}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_140574266160784 = get('current', __marker)

                    # <Value u"python: selected and 'currentLanguage active dropdown-item' or 'dropdown-item'" (30:26)> -> __value
                    __token = 1094
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u" selected and 'currentLanguage active dropdown-item' or 'dropdown-item'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['current'] = __value
                    __backup_current_item_140574267940176 = get('current_item', __marker)

                    # <Value u"python: selected and 'text-light' or ''" (31:30)> -> __value
                    __token = 1211
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u" selected and 'text-light' or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['current_item'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284371920
                    __default_140574284371920 = _DEFAULT_MARKER

                    # <Substitution u'string:${codeclass} ${current}' (32:35)> -> __attr_class
                    __token = 1296
                    try:
                        __zt_tmp = __attrs_140574270227280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'${codeclass} ${current}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda0048d1d0> name=None at 7fd9ff32f410> -> __attrs_140574267915216
                    __attrs_140574267915216 = _static_140574284370384
                    __backup_name_140574284431888 = get('name', __marker)

                    # <Value u'lang/native|lang/name' (34:30)> -> __value
                    __token = 1381
                    try:
                        __zt_tmp = __attrs_140574267915216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'lang/native|lang/name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['name'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267914896
                    __default_140574267914896 = _DEFAULT_MARKER

                    # <Substitution u'string:${base_url}?${new_params}' (35:34)> -> __attr_href
                    __token = 1439
                    try:
                        __zt_tmp = __attrs_140574267915216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${base_url}?${new_params}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267914768
                    __default_140574267914768 = _DEFAULT_MARKER

                    # <Substitution u'string:${current_item} text-decoration-none' (36:34)> -> __attr_class
                    __token = 1507
                    try:
                        __zt_tmp = __attrs_140574267915216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'${current_item} text-decoration-none', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267914512
                    __default_140574267914512 = _DEFAULT_MARKER

                    # <Substitution u'name' (37:33)> -> __attr_title
                    __token = 1586
                    try:
                        __zt_tmp = __attrs_140574267915216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140574397981968('path', u'name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267912528
                    __attrs_140574267912528 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267913552
                    __default_140574267913552 = _DEFAULT_MARKER

                    # <Value u'name' (38:31)> -> __cache_140574267914320
                    __token = 1626
                    try:
                        __zt_tmp = __attrs_140574267912528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267914320 = _static_140574397981968('path', u'name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'name' (38:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4db2d0> -> __condition
                    __expression = __cache_140574267914320

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574267914320
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n          </a>')
                    if (__backup_name_140574284431888 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140574284431888
                    __append(u'\n        </div>')
                    if (__backup_current_item_140574267940176 is __marker):
                        del econtext['current_item']
                    else:
                        econtext['current_item'] = __backup_current_item_140574267940176
                    if (__backup_current_140574266160784 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_140574266160784
                    if (__backup_codeclass_140574284463376 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_140574284463376
                    if (__backup_selected_140574284460496 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140574284460496
                    if (__backup_new_params_140574284463952 is __marker):
                        del econtext['new_params']
                    else:
                        econtext['new_params'] = __backup_new_params_140574284463952
                    if (__backup_lang_param_140574270397200 is __marker):
                        del econtext['lang_param']
                    else:
                        econtext['lang_param'] = __backup_lang_param_140574270397200
                    if (__backup_params_140574284358032 is __marker):
                        del econtext['params']
                    else:
                        econtext['params'] = __backup_params_140574284358032
                    if (__backup_qs_140574284389264 is __marker):
                        del econtext['qs']
                    else:
                        econtext['qs'] = __backup_qs_140574284389264
                    if (__backup_code_140574270171152 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_140574270171152
                    __append(u'\n      ')
                    ____index_140574284370896 -= 1
                    if (____index_140574284370896 > 0):
                        __append('')
                if (__backup_lang_140574275637136 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140574275637136
                __append(u'\n    </div>')
                if (__backup_base_url_140574275597520 is __marker):
                    del econtext['base_url']
                else:
                    econtext['base_url'] = __backup_base_url_140574275597520
                if (__backup_languages_140574284461840 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_140574284461840
                __append(u'\n  </nav>\n')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }