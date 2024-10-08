# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/worksheet/views/../templates/worksheets.pt'

__tokens = {399: (u'view/icon | nothing', 10, 28), 453: (u'view/icon', 11, 33), 503: (u'view/title', 12, 37), 603: (u'python:view.can_add()', 16, 26), 744: (u'string:${context/absolute_url}/worksheet_add', 20, 37), 946: (u"python:context.portal_type == 'WorksheetFolder'", 24, 32), 1110: (u'view/getTemplateInstruments', 27, 39), 1692: (u'view/getAnalysts', 40, 38), 1826: (u'alist', 42, 42), 1891: (u'python:option', 44, 33), 1946: (u'python:option', 45, 40), 1992: (u'python:alist.getValue(option)', 46, 31), 2436: (u'view/getWorksheetTemplates', 55, 42), 2585: (u'wstlist', 57, 44), 2663: (u'python:option', 59, 42), 2711: (u'python:wstlist.getValue(option)', 60, 33), 3207: (u'view/getInstruments', 70, 44), 3351: (u'instrlist', 72, 44), 3431: (u'python:option', 74, 42), 3479: (u'python:instrlist.getValue(option)', 75, 33), 3727: (u'python:view.context_actions.keys()', 81, 48), 3899: (u'add_item', 84, 44), 3943: (u' add_ite', 85, 34), 3986: (u"f python:view.context_actions[add_item]['url", 86, 32), 4289: (u'view/contents_table', 97, 34), 176: (u'here/main_template/macros/master', 4, 23), 176: (u'here/main_template/macros/master', 4, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140574268002896 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'data-live-search': u'true', u'name': u'template', u'class': u'template selectpicker', }
_static_140574256072976 = {u'value': u'python:option', }
_static_140574267458320 = u'master'
_static_140574256157584 = {u'value': u'python:option', }
_static_140574256074000 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'data-live-search': u'true', u'name': u'instrument', u'class': u'instrument selectpicker form-control form-control-sm', }
_static_140574255215824 = {u'value': u'', }
_static_140574397981968 = __compile_zt_expr
_static_140574267347344 = {u'value': u'', }
_static_140574270401936 = {u'value': u'', }
_static_140574256072144 = {u'class': u'input-group input-group-append', }
_static_140574256157840 = {u'id': u'folderlisting-main-table', }
_static_140574267402704 = {u'class': u'input-group-text', }
_static_140574255066704 = {u'class': u'worksheet_add_controls mb-2', }
_static_140574284435984 = {u'href': u"python:view.context_actions[add_item]['url']", u'type': u'submit', u'class': u'btn btn-sm btn-primary', u'value': u'add_item', u'name': u'add_item', }
_static_140574442558096 = {}
_static_140574255164176 = {u'class': u'input-group-prepend', }
_static_140574257251984 = {u'type': u'hidden', u'class': u'templateinstruments', u'value': u'view/getTemplateInstruments', }
_static_140574255215120 = {u'class': u'input-group input-group-append', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574270472720 = {u'src': u'view/icon', }
_static_140574267349072 = {u'class': u'input-group input-group-append', }
_static_140574255098512 = {u'action': u'string:${context/absolute_url}/worksheet_add', u'method': u'POST', u'class': u'form form-inline', u'name': u'worksheet-add-form', }
_static_140574267903632 = {u'value': u'python:option', }
_static_140574268059728 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140574284481104 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'data-live-search': u'true', u'name': u'analyst', u'class': u'analyst selectpicker', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267458192
            __attrs_140574267458192 = _static_140574442558096
            __previous_i18n_domain_140574267459408 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140574268967904 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fd9ff46c310> name=None at 7fd9ff46c4d0> -> __value
            __value = _static_140574267458320
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270472464
                __attrs_140574270472464 = _static_140574442558096
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270472528
                __attrs_140574270472528 = _static_140574442558096

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1>\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff74c210> name=None at 7fd9ff74cf10> -> __attrs_140574270390480
                __attrs_140574270390480 = _static_140574270472720

                # <Value u'view/icon | nothing' (10:28)> -> __condition
                __token = 399
                try:
                    __zt_tmp = __attrs_140574270390480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/icon | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270474832
                    __default_140574270474832 = _DEFAULT_MARKER

                    # <Substitution u'view/icon' (11:33)> -> __attr_src
                    __token = 453
                    try:
                        __zt_tmp = __attrs_140574270390480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_140574397981968('path', u'view/icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((u' src="%s"' % __attr_src))
                    __append(u'/>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255063952
                __attrs_140574255063952 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255063568
                __default_140574255063568 = _DEFAULT_MARKER

                # <Value u'view/title' (12:37)> -> __cache_140574255066960
                __token = 503
                try:
                    __zt_tmp = __attrs_140574255063952
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574255066960 = _static_140574397981968('path', u'view/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/title' (12:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe89ac90> -> __condition
                __expression = __cache_140574255066960

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140574255066960
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n      </h1>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9fe89ae50> name=None at 7fd9ff74c250> -> __attrs_140574255098064
                __attrs_140574255098064 = _static_140574255066704

                # <Value u'python:view.can_add()' (16:26)> -> __condition
                __token = 603
                try:
                    __zt_tmp = __attrs_140574255098064
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'view.can_add()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="worksheet_add_controls mb-2">\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe8a2a90> name=None at 7fd9fe8a2850> -> __attrs_140574255096528
                    __attrs_140574255096528 = _static_140574255098512

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form class="form form-inline" name="worksheet-add-form" method="POST"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255098640
                    __default_140574255098640 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/absolute_url}/worksheet_add' (20:37)> -> __attr_action
                    __token = 744
                    try:
                        __zt_tmp = __attrs_140574255096528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140574397981968('string', u'${context/absolute_url}/worksheet_add', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n\n          <!-- N.B. the class is picked up by bika.lims.worksheet.get_template_instrument -->\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9feab0690> name=None at 7fd9feab0250> -> __attrs_140574255109968
                    __attrs_140574255109968 = _static_140574257251984

                    # <Value u"python:context.portal_type == 'WorksheetFolder'" (24:32)> -> __condition
                    __token = 946
                    try:
                        __zt_tmp = __attrs_140574255109968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"context.portal_type == 'WorksheetFolder'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden" class="templateinstruments"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255109904
                        __default_140574255109904 = _DEFAULT_MARKER

                        # <Substitution u'view/getTemplateInstruments' (27:39)> -> __attr_value
                        __token = 1110
                        try:
                            __zt_tmp = __attrs_140574255109968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140574397981968('path', u'view/getTemplateInstruments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'/>')
                    __append(u'\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4ff050> name=None at 7fd9fe8a51d0> -> __attrs_140574255164112
                    __attrs_140574255164112 = _static_140574268059728

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe8b2b10> name=None at 7fd9fe8b26d0> -> __attrs_140574267401040
                    __attrs_140574267401040 = _static_140574255164176

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff45e9d0> name=None at 7fd9ff45e450> -> __attrs_140574284480592
                    __attrs_140574284480592 = _static_140574267402704

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-text">')
                    __stream_140574267402512 = []
                    __append_140574267402512 = __stream_140574267402512.append
                    __append_140574267402512(u'\n                Create new worksheet\n              ')
                    __msgid_140574267402512 = __re_whitespace(''.join(__stream_140574267402512)).strip()
                    if __msgid_140574267402512:
                        __append(translate(__msgid_140574267402512, mapping=None, default=__msgid_140574267402512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n            </div>\n            <!-- Analyst -->\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda004a8250> name=None at 7fda004a8310> -> __attrs_140574267349008
                    __attrs_140574267349008 = _static_140574284481104
                    __backup_alist_140574272098000 = get('alist', __marker)

                    # <Value u'view/getAnalysts' (40:38)> -> __value
                    __token = 1692
                    try:
                        __zt_tmp = __attrs_140574267349008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'view/getAnalysts', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['alist'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select name="analyst" class="analyst selectpicker" data-style="dropdown-toggle btn-sm btn-light border rounded-0" data-live-search="true">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff451190> name=None at 7fd9ff451450> -> __attrs_140574267348816
                    __attrs_140574267348816 = _static_140574267347344

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option value="">')
                    __stream_140574267348496 = []
                    __append_140574267348496 = __stream_140574267348496.append
                    __append_140574267348496(u'Select analyst')
                    __msgid_140574267348496 = __re_whitespace(''.join(__stream_140574267348496)).strip()
                    if __msgid_140574267348496:
                        __append(translate(__msgid_140574267348496, mapping=None, default=__msgid_140574267348496, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</option>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267348176
                    __attrs_140574267348176 = _static_140574442558096
                    __backup_option_140574267398096 = get('option', __marker)

                    # <Value u'alist' (42:42)> -> __iterator
                    __token = 1826
                    try:
                        __zt_tmp = __attrs_140574267348176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'alist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574267347088, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d8e90> name=None at 7fd9ff4d8350> -> __attrs_140574268005520
                        __attrs_140574268005520 = _static_140574267903632

                        # <Value u'python:option' (44:33)> -> __condition
                        __token = 1891
                        try:
                            __zt_tmp = __attrs_140574268005520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('python', u'option', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<option')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284443408
                            __default_140574284443408 = _DEFAULT_MARKER

                            # <Substitution u'python:option' (45:40)> -> __attr_value
                            __token = 1946
                            try:
                                __zt_tmp = __attrs_140574268005520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140574397981968('python', u'option', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267347792
                            __default_140574267347792 = _DEFAULT_MARKER

                            # <Value u'python:alist.getValue(option)' (46:31)> -> __cache_140574267349840
                            __token = 1992
                            try:
                                __zt_tmp = __attrs_140574268005520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574267349840 = _static_140574397981968('python', u'alist.getValue(option)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:alist.getValue(option)' (46:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff451e90> -> __condition
                            __expression = __cache_140574267349840

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574267349840
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</option>')
                        __append(u'\n              ')
                        ____index_140574267347088 -= 1
                        if (____index_140574267347088 > 0):
                            __append('')
                    if (__backup_option_140574267398096 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140574267398096
                    __append(u'\n            </select>')
                    if (__backup_alist_140574272098000 is __marker):
                        del econtext['alist']
                    else:
                        econtext['alist'] = __backup_alist_140574272098000
                    __append(u'\n            <!-- Worksheet Template -->\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff451850> name=None at 7fd9ff4513d0> -> __attrs_140574268006224
                    __attrs_140574268006224 = _static_140574267349072

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-append">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4f1250> name=None at 7fd9ff4f1810> -> __attrs_140574270399568
                    __attrs_140574270399568 = _static_140574268002896
                    __backup_wstlist_140574268932496 = get('wstlist', __marker)

                    # <Value u'view/getWorksheetTemplates' (55:42)> -> __value
                    __token = 2436
                    try:
                        __zt_tmp = __attrs_140574270399568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'view/getWorksheetTemplates', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['wstlist'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select name="template" class="template selectpicker" data-style="dropdown-toggle btn-sm btn-light border rounded-0" data-live-search="true">\n                ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff73ad90> name=None at 7fd9ff73a090> -> __attrs_140574270401552
                    __attrs_140574270401552 = _static_140574270401936

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option value="">')
                    __stream_140574270401168 = []
                    __append_140574270401168 = __stream_140574270401168.append
                    __append_140574270401168(u'Select template')
                    __msgid_140574270401168 = __re_whitespace(''.join(__stream_140574270401168)).strip()
                    if __msgid_140574270401168:
                        __append(translate(__msgid_140574270401168, mapping=None, default=__msgid_140574270401168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</option>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574256073808
                    __attrs_140574256073808 = _static_140574442558096
                    __backup_option_140574267396496 = get('option', __marker)

                    # <Value u'wstlist' (57:44)> -> __iterator
                    __token = 2585
                    try:
                        __zt_tmp = __attrs_140574256073808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'wstlist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574256073936, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9fe990910> name=None at 7fd9fe990d50> -> __attrs_140574256074128
                        __attrs_140574256074128 = _static_140574256072976

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256073488
                        __default_140574256073488 = _DEFAULT_MARKER

                        # <Substitution u'python:option' (59:42)> -> __attr_value
                        __token = 2663
                        try:
                            __zt_tmp = __attrs_140574256074128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140574397981968('python', u'option', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256072784
                        __default_140574256072784 = _DEFAULT_MARKER

                        # <Value u'python:wstlist.getValue(option)' (60:33)> -> __cache_140574256073744
                        __token = 2711
                        try:
                            __zt_tmp = __attrs_140574256074128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574256073744 = _static_140574397981968('python', u'wstlist.getValue(option)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:wstlist.getValue(option)' (60:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe990c90> -> __condition
                        __expression = __cache_140574256073744

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574256073744
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                ')
                        ____index_140574256073936 -= 1
                        if (____index_140574256073936 > 0):
                            __append('')
                    if (__backup_option_140574267396496 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140574267396496
                    __append(u'\n              </select>')
                    if (__backup_wstlist_140574268932496 is __marker):
                        del econtext['wstlist']
                    else:
                        econtext['wstlist'] = __backup_wstlist_140574268932496
                    __append(u'\n            </div>\n            <!-- Instrument -->\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe9905d0> name=None at 7fd9fe9907d0> -> __attrs_140574256074384
                    __attrs_140574256074384 = _static_140574256072144

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-append">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe990d10> name=None at 7fd9fe9903d0> -> __attrs_140574255215376
                    __attrs_140574255215376 = _static_140574256074000
                    __backup_instrlist_140574272096848 = get('instrlist', __marker)

                    # <Value u'view/getInstruments' (70:44)> -> __value
                    __token = 3207
                    try:
                        __zt_tmp = __attrs_140574255215376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'view/getInstruments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['instrlist'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select name="instrument" class="instrument selectpicker form-control form-control-sm" data-style="dropdown-toggle btn-sm btn-light border rounded-0" data-live-search="true">\n                ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe8bf4d0> name=None at 7fd9fe8bf090> -> __attrs_140574255218320
                    __attrs_140574255218320 = _static_140574255215824

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option value="">')
                    __stream_140574255215760 = []
                    __append_140574255215760 = __stream_140574255215760.append
                    __append_140574255215760(u'Select instrument')
                    __msgid_140574255215760 = __re_whitespace(''.join(__stream_140574255215760)).strip()
                    if __msgid_140574255215760:
                        __append(translate(__msgid_140574255215760, mapping=None, default=__msgid_140574255215760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</option>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574256159696
                    __attrs_140574256159696 = _static_140574442558096
                    __backup_option_140574255078992 = get('option', __marker)

                    # <Value u'instrlist' (72:44)> -> __iterator
                    __token = 3351
                    try:
                        __zt_tmp = __attrs_140574256159696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'instrlist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574256156880, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9fe9a5390> name=None at 7fd9fe9a5750> -> __attrs_140574256157008
                        __attrs_140574256157008 = _static_140574256157584

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256156752
                        __default_140574256156752 = _DEFAULT_MARKER

                        # <Substitution u'python:option' (74:42)> -> __attr_value
                        __token = 3431
                        try:
                            __zt_tmp = __attrs_140574256157008
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140574397981968('python', u'option', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256159376
                        __default_140574256159376 = _DEFAULT_MARKER

                        # <Value u'python:instrlist.getValue(option)' (75:33)> -> __cache_140574256157200
                        __token = 3479
                        try:
                            __zt_tmp = __attrs_140574256157008
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574256157200 = _static_140574397981968('python', u'instrlist.getValue(option)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:instrlist.getValue(option)' (75:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe9a51d0> -> __condition
                        __expression = __cache_140574256157200

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574256157200
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                ')
                        ____index_140574256156880 -= 1
                        if (____index_140574256156880 > 0):
                            __append('')
                    if (__backup_option_140574255078992 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140574255078992
                    __append(u'\n              </select>')
                    if (__backup_instrlist_140574272096848 is __marker):
                        del econtext['instrlist']
                    else:
                        econtext['instrlist'] = __backup_instrlist_140574272096848
                    __append(u'\n            </div>\n            <!-- Add button -->\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe8bf210> name=None at 7fd9fe8bfb10> -> __attrs_140574256159888
                    __attrs_140574256159888 = _static_140574255215120

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-append">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574256160336
                    __attrs_140574256160336 = _static_140574442558096
                    __backup_add_item_140574268936080 = get('add_item', __marker)

                    # <Value u'python:view.context_actions.keys()' (81:48)> -> __iterator
                    __token = 3727
                    try:
                        __zt_tmp = __attrs_140574256160336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('python', u'view.context_actions.keys()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574256160144, ) = getitem('repeat')(u'add_item', __iterator)
                    econtext['add_item'] = None
                    for __item in __iterator:
                        econtext['add_item'] = __item
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda0049d210> name=None at 7fda0049de10> -> __attrs_140574270613648
                        __attrs_140574270613648 = _static_140574284435984

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="submit" class="btn btn-sm btn-primary"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270614736
                        __default_140574270614736 = _DEFAULT_MARKER

                        # <Substitution u'add_item' (84:44)> -> __attr_name
                        __token = 3899
                        try:
                            __zt_tmp = __attrs_140574270613648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140574397981968('path', u'add_item', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270613776
                        __default_140574270613776 = _DEFAULT_MARKER

                        # <Substitution u'add_item' (85:34)> -> __attr_value
                        __token = 3943
                        try:
                            __zt_tmp = __attrs_140574270613648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140574397981968('path', u'add_item', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270613328
                        __default_140574270613328 = _DEFAULT_MARKER

                        # <Substitution u"python:view.context_actions[add_item]['url']" (86:32)> -> __attr_href
                        __token = 3986
                        try:
                            __zt_tmp = __attrs_140574270613648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140574397981968('python', u"view.context_actions[add_item]['url']", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'/>\n              ')
                        ____index_140574256160144 -= 1
                        if (____index_140574256160144 > 0):
                            __append('')
                    if (__backup_add_item_140574268936080 is __marker):
                        del econtext['add_item']
                    else:
                        econtext['add_item'] = __backup_add_item_140574268936080
                    __append(u'\n            </div>\n          </div>\n\n        </form>\n      </div>')
                __append(u'\n    ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270473360
                __attrs_140574270473360 = _static_140574442558096
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9fe9a5490> name=None at 7fd9fe9a5510> -> __attrs_140574270612048
                __attrs_140574270612048 = _static_140574256157840

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="folderlisting-main-table">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574256157648
                __default_140574256157648 = _DEFAULT_MARKER

                # <Value u'view/contents_table' (97:34)> -> __cache_140574255216912
                __token = 4289
                try:
                    __zt_tmp = __attrs_140574270612048
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574255216912 = _static_140574397981968('path', u'view/contents_table', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/contents_table' (97:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe9a5090> -> __condition
                __expression = __cache_140574255216912

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574255216912
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'here/main_template/macros/master' (4:23)> -> __macro
            __token = 176
            try:
                __zt_tmp = __attrs_140574267458192
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140574397981968('path', u'here/main_template/macros/master', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __token = 176
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140574268967904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140574268967904
            __i18n_domain = __previous_i18n_domain_140574267459408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }