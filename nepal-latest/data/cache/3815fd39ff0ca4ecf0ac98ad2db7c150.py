# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.z3cform-3.2.4-py2.7.egg/plone/app/z3cform/templates/singlecheckboxbool_input.pt'

__tokens = {139: (u'view/items', 4, 23), 173: (u' python:list(items', 5, 22), 225: (u'x python:len(items) ==', 6, 31), 344: (u'python:len(items) > 0', 9, 21), 306: (u'single_checkbox', 8, 20), 277: (u'view/id', 7, 25), 414: (u'items', 11, 24), 447: (u'python:single_checkbox and view.id or None', 12, 26), 674: (u'item/checked', 16, 24), 716: (u'item/id', 17, 28), 754: (u' item/nam', 18, 29), 795: (u's view/kla', 19, 29), 1793: (u'        ', 40, 6), 921: (u'itle view/', 22, 26), 1564: (u'         tabi', 35, 16), 1516: (u'        disab', 34, 17), 1750: (u'             ', 39, 12), 1837: (u'              ', 41, 11), 837: (u'ue item/va', 20, 28), 879: (u'yle view/s', 21, 27), 962: (u' lang vie', 23, 24), 1005: (u'nclick view/', 24, 26), 1054: (u'blclick view/on', 25, 28), 1107: (u'ousedown view/on', 26, 28), 1159: (u'onmouseup view', 27, 25), 1211: (u'nmouseover view/', 28, 26), 1265: (u'onmousemove view', 29, 25), 1318: (u'  onmouseout vi', 30, 23), 1370: (u'   onkeypress v', 31, 22), 1421: (u'     onkeydown', 32, 20), 1469: (u'        onke', 33, 17), 1611: (u'           o', 36, 14), 1656: (u'           ', 37, 12), 1702: (u'            o', 38, 13), 1886: (u'             ', 42, 9), 2096: (u'not:item/checked', 46, 24), 2142: (u'item/id', 47, 28), 2180: (u' item/nam', 48, 29), 2221: (u's view/kla', 49, 29), 3219: (u'        ', 70, 6), 2347: (u'itle view/', 52, 26), 2990: (u'         tabi', 65, 16), 2942: (u'        disab', 64, 17), 3176: (u'             ', 69, 12), 3263: (u'              ', 71, 11), 2263: (u'ue item/va', 50, 28), 2305: (u'yle view/s', 51, 27), 2388: (u' lang vie', 53, 24), 2431: (u'nclick view/', 54, 26), 2480: (u'blclick view/on', 55, 28), 2533: (u'ousedown view/on', 56, 28), 2585: (u'onmouseup view', 57, 25), 2637: (u'nmouseover view/', 58, 26), 2691: (u'onmousemove view', 59, 25), 2744: (u'  onmouseout vi', 60, 23), 2796: (u'   onkeypress v', 61, 22), 2847: (u'     onkeydown', 62, 20), 2895: (u'        onke', 63, 17), 3037: (u'           o', 66, 14), 3082: (u'           ', 67, 12), 3128: (u'            o', 68, 13), 3312: (u'             ', 72, 9), 3400: (u'item/id', 74, 29), 3447: (u'item/label', 75, 37), 3562: (u'item/required', 78, 25), 3691: (u'item/description', 80, 50), 3841: (u'string:${view/name}-empty-marker', 85, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240764048784 = {u'class': u'required horizontal', u'title': u'Required', }
_static_140240604787536 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240752316816 = {u'accesskey': u'', u'onmousedown': u'view/onmousedown', u'disabled': u'', u'alt': u'', u'onchange': u'view/onchange', u'id': u'', u'style': u'view/style', u'checked': u'checked', u'title': u'', u'readonly': u'', u'onselect': u'view/onselect', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'type': u'checkbox', u'onblur': u'view/onblur', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'class': u'', u'lang': u'view/lang', u'name': u'', u'value': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'', }
_static_140240764050000 = {u'class': u'label', }
_static_140240766773584 = {u'accesskey': u'', u'onmousedown': u'view/onmousedown', u'disabled': u'', u'alt': u'', u'onchange': u'view/onchange', u'id': u'', u'style': u'view/style', u'title': u'', u'readonly': u'', u'onselect': u'view/onselect', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'type': u'checkbox', u'onblur': u'view/onblur', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'class': u'', u'lang': u'view/lang', u'name': u'', u'value': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'', }
_static_140240612230928 = {u'for': u'', }
_static_140240612231696 = {u'type': u'hidden', u'name': u'field-empty-marker', u'value': u'1', }
_static_140240604788880 = {u'id': u'view/id', }
_static_140240764049872 = {u'class': u'formHelp', }
_static_140240612232656 = {u'class': u'option', u'id': u'python:single_checkbox and view.id or None', }

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

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7350> name=None at 7f8c4f6e7390> -> __attrs_140240604788240
            __attrs_140240604788240 = _static_140240604787536
            __backup_items_140240612230800 = get('items', __marker)

            # <Value u'view/items' (4:23)> -> __value
            __token = 139
            try:
                __zt_tmp = __attrs_140240604788240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/items', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_140240612229456 = get('items', __marker)

            # <Value u'python:list(items)' (5:22)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140240604788240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'list(items)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_140240610144720 = get('single_checkbox', __marker)

            # <Value u'python:len(items) == 1' (6:31)> -> __value
            __token = 225
            try:
                __zt_tmp = __attrs_140240604788240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'len(items) == 1', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7890> name=None at 7f8c4f6e7a50> -> __attrs_140240604788816
            __attrs_140240604788816 = _static_140240604788880

            # <Value u'python:len(items) > 0' (9:21)> -> __condition
            __token = 344
            try:
                __zt_tmp = __attrs_140240604788816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'len(items) > 0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value u'single_checkbox' (8:20)> at 7f8c4f6e7dd0> -> __cache_140240604790224

                # <Value u'single_checkbox' (8:20)> -> __cache_140240604790224
                __token = 306
                try:
                    __zt_tmp = __attrs_140240604788816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240604790224 = _static_140241087907024('path', u'single_checkbox', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __cache_140240604790224 = not __cache_140240604790224
                __condition = __cache_140240604790224
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604790480
                    __default_140240604790480 = _DEFAULT_MARKER

                    # <Substitution u'view/id' (7:25)> -> __attr_id
                    __token = 277
                    try:
                        __zt_tmp = __attrs_140240604788816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>')
                __append(u'\n ')

                # <Static value=<_ast.Dict object at 0x7f8c4fe00dd0> name=None at 7f8c4fe00d90> -> __attrs_140240612230352
                __attrs_140240612230352 = _static_140240612232656
                __backup_item_140240780123280 = get('item', __marker)

                # <Value u'items' (11:24)> -> __iterator
                __token = 414
                try:
                    __zt_tmp = __attrs_140240612230352
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'items', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240612230864, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="option"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612232272
                    __default_140240612232272 = _DEFAULT_MARKER

                    # <Substitution u'python:single_checkbox and view.id or None' (12:26)> -> __attr_id
                    __token = 447
                    try:
                        __zt_tmp = __attrs_140240612230352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('python', u'single_checkbox and view.id or None', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n  ')

                    # <Static value=<_ast.Dict object at 0x7f8c58399190> name=None at 7f8c583991d0> -> __attrs_140240766775056
                    __attrs_140240766775056 = _static_140240752316816

                    # <Value u'item/checked' (16:24)> -> __condition
                    __token = 674
                    try:
                        __zt_tmp = __attrs_140240766775056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'item/checked', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793574480
                        __default_140240793574480 = _DEFAULT_MARKER

                        # <Substitution u'item/id' (17:28)> -> __attr_id
                        __token = 716
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140241087907024('path', u'item/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793572752
                        __default_140240793572752 = _DEFAULT_MARKER

                        # <Substitution u'item/name' (18:29)> -> __attr_name
                        __token = 754
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140241087907024('path', u'item/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793572432
                        __default_140240793572432 = _DEFAULT_MARKER

                        # <Substitution u'view/klass' (19:29)> -> __attr_class
                        __token = 795
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793574224
                        __default_140240793574224 = _DEFAULT_MARKER

                        # <Substitution u'view/alt' (40:6)> -> __attr_alt
                        __token = 1793
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140241087907024('path', u'view/alt', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793573392
                        __default_140240793573392 = _DEFAULT_MARKER

                        # <Substitution u'view/title' (22:26)> -> __attr_title
                        __token = 921
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793573456
                        __default_140240793573456 = _DEFAULT_MARKER

                        # <Substitution u'view/tabindex' (35:16)> -> __attr_tabindex
                        __token = 1564
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((u' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793574160
                        __default_140240793574160 = _DEFAULT_MARKER

                        # <Boolean u'view/disabled' (34:17)> -> __attr_disabled
                        __token = 1516
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_140241087907024('path', u'view/disabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = u''
                        else:
                            if __attr_disabled:
                                __attr_disabled = u'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((u' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793571920
                        __default_140240793571920 = _DEFAULT_MARKER

                        # <Boolean u'view/readonly' (39:12)> -> __attr_readonly
                        __token = 1750
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_140241087907024('path', u'view/readonly', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = u''
                        else:
                            if __attr_readonly:
                                __attr_readonly = u'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((u' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793575056
                        __default_140240793575056 = _DEFAULT_MARKER

                        # <Substitution u'view/accesskey' (41:11)> -> __attr_accesskey
                        __token = 1837
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_140241087907024('path', u'view/accesskey', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((u' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793575120
                        __default_140240793575120 = _DEFAULT_MARKER

                        # <Substitution u'item/value' (20:28)> -> __attr_value
                        __token = 837
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140241087907024('path', u'item/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' checked="checked"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240777716944
                        __default_140240777716944 = _DEFAULT_MARKER

                        # <Substitution u'view/style' (21:27)> -> __attr_style
                        __token = 879
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((u' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610144912
                        __default_140240610144912 = _DEFAULT_MARKER

                        # <Substitution u'view/lang' (23:24)> -> __attr_lang
                        __token = 962
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((u' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610144592
                        __default_140240610144592 = _DEFAULT_MARKER

                        # <Substitution u'view/onclick' (24:26)> -> __attr_onclick
                        __token = 1005
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((u' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610147408
                        __default_140240610147408 = _DEFAULT_MARKER

                        # <Substitution u'view/ondblclick' (25:28)> -> __attr_ondblclick
                        __token = 1054
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((u' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610147216
                        __default_140240610147216 = _DEFAULT_MARKER

                        # <Substitution u'view/onmousedown' (26:28)> -> __attr_onmousedown
                        __token = 1107
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((u' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610146128
                        __default_140240610146128 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseup' (27:25)> -> __attr_onmouseup
                        __token = 1159
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((u' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610144976
                        __default_140240610144976 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseover' (28:26)> -> __attr_onmouseover
                        __token = 1211
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((u' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610145872
                        __default_140240610145872 = _DEFAULT_MARKER

                        # <Substitution u'view/onmousemove' (29:25)> -> __attr_onmousemove
                        __token = 1265
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((u' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766771344
                        __default_140240766771344 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseout' (30:23)> -> __attr_onmouseout
                        __token = 1318
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((u' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766773904
                        __default_140240766773904 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeypress' (31:22)> -> __attr_onkeypress
                        __token = 1370
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((u' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766772496
                        __default_140240766772496 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeydown' (32:20)> -> __attr_onkeydown
                        __token = 1421
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((u' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766771728
                        __default_140240766771728 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeyup' (33:17)> -> __attr_onkeyup
                        __token = 1469
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((u' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766772880
                        __default_140240766772880 = _DEFAULT_MARKER

                        # <Substitution u'view/onfocus' (36:14)> -> __attr_onfocus
                        __token = 1611
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((u' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766773008
                        __default_140240766773008 = _DEFAULT_MARKER

                        # <Substitution u'view/onblur' (37:12)> -> __attr_onblur
                        __token = 1656
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((u' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766773328
                        __default_140240766773328 = _DEFAULT_MARKER

                        # <Substitution u'view/onchange' (38:13)> -> __attr_onchange
                        __token = 1702
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((u' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766771792
                        __default_140240766771792 = _DEFAULT_MARKER

                        # <Substitution u'view/onselect' (42:9)> -> __attr_onselect
                        __token = 1886
                        try:
                            __zt_tmp = __attrs_140240766775056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_140241087907024('path', u'view/onselect', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((u' onselect="%s"' % __attr_onselect))
                        __append(u' />')

                    # <Static value=<_ast.Dict object at 0x7f8c59162950> name=None at 7f8c59162a50> -> __attrs_140240762817872
                    __attrs_140240762817872 = _static_140240766773584

                    # <Value u'not:item/checked' (46:24)> -> __condition
                    __token = 2096
                    try:
                        __zt_tmp = __attrs_140240762817872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('not', u'item/checked', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756768528
                        __default_140240756768528 = _DEFAULT_MARKER

                        # <Substitution u'item/id' (47:28)> -> __attr_id
                        __token = 2142
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140241087907024('path', u'item/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756767440
                        __default_140240756767440 = _DEFAULT_MARKER

                        # <Substitution u'item/name' (48:29)> -> __attr_name
                        __token = 2180
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140241087907024('path', u'item/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756768144
                        __default_140240756768144 = _DEFAULT_MARKER

                        # <Substitution u'view/klass' (49:29)> -> __attr_class
                        __token = 2221
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756766096
                        __default_140240756766096 = _DEFAULT_MARKER

                        # <Substitution u'view/alt' (70:6)> -> __attr_alt
                        __token = 3219
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140241087907024('path', u'view/alt', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756768080
                        __default_140240756768080 = _DEFAULT_MARKER

                        # <Substitution u'view/title' (52:26)> -> __attr_title
                        __token = 2347
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756768272
                        __default_140240756768272 = _DEFAULT_MARKER

                        # <Substitution u'view/tabindex' (65:16)> -> __attr_tabindex
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((u' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755173008
                        __default_140240755173008 = _DEFAULT_MARKER

                        # <Boolean u'view/disabled' (64:17)> -> __attr_disabled
                        __token = 2942
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_140241087907024('path', u'view/disabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = u''
                        else:
                            if __attr_disabled:
                                __attr_disabled = u'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((u' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755171856
                        __default_140240755171856 = _DEFAULT_MARKER

                        # <Boolean u'view/readonly' (69:12)> -> __attr_readonly
                        __token = 3176
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_140241087907024('path', u'view/readonly', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = u''
                        else:
                            if __attr_readonly:
                                __attr_readonly = u'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((u' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755172240
                        __default_140240755172240 = _DEFAULT_MARKER

                        # <Substitution u'view/accesskey' (71:11)> -> __attr_accesskey
                        __token = 3263
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_140241087907024('path', u'view/accesskey', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((u' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755173072
                        __default_140240755173072 = _DEFAULT_MARKER

                        # <Substitution u'item/value' (50:28)> -> __attr_value
                        __token = 2263
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140241087907024('path', u'item/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755173968
                        __default_140240755173968 = _DEFAULT_MARKER

                        # <Substitution u'view/style' (51:27)> -> __attr_style
                        __token = 2305
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((u' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755175248
                        __default_140240755175248 = _DEFAULT_MARKER

                        # <Substitution u'view/lang' (53:24)> -> __attr_lang
                        __token = 2388
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((u' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755173776
                        __default_140240755173776 = _DEFAULT_MARKER

                        # <Substitution u'view/onclick' (54:26)> -> __attr_onclick
                        __token = 2431
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((u' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755174608
                        __default_140240755174608 = _DEFAULT_MARKER

                        # <Substitution u'view/ondblclick' (55:28)> -> __attr_ondblclick
                        __token = 2480
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((u' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755173584
                        __default_140240755173584 = _DEFAULT_MARKER

                        # <Substitution u'view/onmousedown' (56:28)> -> __attr_onmousedown
                        __token = 2533
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((u' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755172688
                        __default_140240755172688 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseup' (57:25)> -> __attr_onmouseup
                        __token = 2585
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((u' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755172048
                        __default_140240755172048 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseover' (58:26)> -> __attr_onmouseover
                        __token = 2637
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((u' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755172816
                        __default_140240755172816 = _DEFAULT_MARKER

                        # <Substitution u'view/onmousemove' (59:25)> -> __attr_onmousemove
                        __token = 2691
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((u' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755174544
                        __default_140240755174544 = _DEFAULT_MARKER

                        # <Substitution u'view/onmouseout' (60:23)> -> __attr_onmouseout
                        __token = 2744
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((u' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762817296
                        __default_140240762817296 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeypress' (61:22)> -> __attr_onkeypress
                        __token = 2796
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((u' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762814992
                        __default_140240762814992 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeydown' (62:20)> -> __attr_onkeydown
                        __token = 2847
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((u' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762815568
                        __default_140240762815568 = _DEFAULT_MARKER

                        # <Substitution u'view/onkeyup' (63:17)> -> __attr_onkeyup
                        __token = 2895
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((u' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762815760
                        __default_140240762815760 = _DEFAULT_MARKER

                        # <Substitution u'view/onfocus' (66:14)> -> __attr_onfocus
                        __token = 3037
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((u' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762816144
                        __default_140240762816144 = _DEFAULT_MARKER

                        # <Substitution u'view/onblur' (67:12)> -> __attr_onblur
                        __token = 3082
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((u' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762817936
                        __default_140240762817936 = _DEFAULT_MARKER

                        # <Substitution u'view/onchange' (68:13)> -> __attr_onchange
                        __token = 3128
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((u' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762818192
                        __default_140240762818192 = _DEFAULT_MARKER

                        # <Substitution u'view/onselect' (72:9)> -> __attr_onselect
                        __token = 3312
                        try:
                            __zt_tmp = __attrs_140240762817872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_140241087907024('path', u'view/onselect', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((u' onselect="%s"' % __attr_onselect))
                        __append(u' />')
                    __append(u'\n  ')

                    # <Static value=<_ast.Dict object at 0x7f8c4fe00710> name=None at 7f8c4fe00310> -> __attrs_140240762816272
                    __attrs_140240762816272 = _static_140240612230928

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766773776
                    __default_140240766773776 = _DEFAULT_MARKER

                    # <Substitution u'item/id' (74:29)> -> __attr_for
                    __token = 3400
                    try:
                        __zt_tmp = __attrs_140240762816272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140241087907024('path', u'item/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((u' for="%s"' % __attr_for))
                    __append(u'>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ec9a50> name=None at 7f8c58ec93d0> -> __attrs_140240764048208
                    __attrs_140240764048208 = _static_140240764050000

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="label">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764049616
                    __default_140240764049616 = _DEFAULT_MARKER

                    # <Value u'item/label' (75:37)> -> __cache_140240604881040
                    __token = 3447
                    try:
                        __zt_tmp = __attrs_140240764048208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240604881040 = _static_140241087907024('path', u'item/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/label' (75:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58d9cb90> -> __condition
                    __expression = __cache_140240604881040

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Label')
                    else:
                        __content = __cache_140240604881040
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ec9590> name=None at 7f8c58ec9690> -> __attrs_140240764051088
                    __attrs_140240764051088 = _static_140240764048784

                    # <Value u'item/required' (78:25)> -> __condition
                    __token = 3562
                    try:
                        __zt_tmp = __attrs_140240764051088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'item/required', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="required horizontal"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764048016
                        __default_140240764048016 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f8c58ec9510> at 7f8c58ec9210> -> __attr_title
                        __attr_title = u'Required'
                        __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>&nbsp;</span>')
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ec99d0> name=None at 7f8c58ec9910> -> __attrs_140240612398736
                    __attrs_140240612398736 = _static_140240764049872

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="formHelp">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764050128
                    __default_140240764050128 = _DEFAULT_MARKER

                    # <Value u'item/description' (80:50)> -> __cache_140240764048080
                    __token = 3691
                    try:
                        __zt_tmp = __attrs_140240612398736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240764048080 = _static_140241087907024('path', u'item/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/description' (80:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58ec9f90> -> __condition
                    __expression = __cache_140240764048080

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Description')
                    else:
                        __content = __cache_140240764048080
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n  </label>\n </span>')
                    ____index_140240612230864 -= 1
                    if (____index_140240612230864 > 0):
                        __append('\n ')
                if (__backup_item_140240780123280 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140240780123280
                __append(u'\n')
                __condition = __cache_140240604790224
                if __condition:
                    __append(u'</span>')
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c4fe00a10> name=None at 7f8c4fe00c10> -> __attrs_140240612400592
            __attrs_140240612400592 = _static_140240612231696

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612400144
            __default_140240612400144 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}-empty-marker' (85:28)> -> __attr_name
            __token = 3841
            try:
                __zt_tmp = __attrs_140240612400592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('string', u'${view/name}-empty-marker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_140240610144720 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_140240610144720
            if (__backup_items_140240612229456 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_140240612229456
            if (__backup_items_140240612230800 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_140240612230800
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }