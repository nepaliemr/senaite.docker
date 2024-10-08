# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/text_input.pt'

__tokens = {329: (u'view/id', 7, 30), 369: (u' view/nam', 8, 31), 412: (u's view/kla', 9, 31), 500: (u'tle view/t', 11, 29), 543: (u'lang view', 12, 27), 1163: (u'        disab', 24, 19), 1407: (u'             ', 29, 14), 1452: (u'        ', 30, 8), 1213: (u'         tabi', 25, 18), 1498: (u'              ', 31, 13), 1595: (u'         ', 33, 6), 1642: (u'              ', 34, 10), 456: (u'le view/st', 10, 30), 1116: (u'          ', 23, 17), 588: (u'click view/o', 13, 29), 639: (u'lclick view/ond', 14, 31), 694: (u'usedown view/onm', 15, 31), 748: (u'nmouseup view/', 16, 28), 802: (u'mouseover view/o', 17, 29), 858: (u'nmousemove view/', 18, 28), 913: (u' onmouseout vie', 19, 26), 967: (u'  onkeypress vi', 20, 25), 1020: (u'    onkeydown ', 21, 23), 1070: (u'       onkey', 22, 20), 1262: (u'           o', 26, 16), 1309: (u'           ', 27, 14), 1357: (u'            o', 28, 15), 1549: (u'             ', 32, 11), 1696: (u'                ', 35, 11), 1755: (u'              autoc', 36, 13)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240906774224 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906452496 = {u'accesskey': u'', u'onmousedown': u'view/onmousedown', u'disabled': u'', u'autocapitalize': u'view/autocapitalize', u'alt': u'', u'onchange': u'view/onchange', u'id': u'', u'size': u'', u'style': u'', u'title': u'', u'readonly': u'', u'onselect': u'view/onselect', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'type': u'text', u'onblur': u'view/onblur', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'placeholder': u'view/placeholder', u'class': u'', u'lang': u'', u'name': u'', u'value': u'', u'maxlength': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'', }

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

            # <Static value=<_ast.Dict object at 0x7f8c616e66d0> name=None at 7f8c616e6610> -> __attrs_140240906773200
            __attrs_140240906773200 = _static_140240906774224
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c61697e10> name=None at 7f8c61697f50> -> __attrs_140240906997520
            __attrs_140240906997520 = _static_140240906452496

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852368
            __default_140240906852368 = _DEFAULT_MARKER

            # <Substitution u'view/id' (7:30)> -> __attr_id
            __token = 329
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906854160
            __default_140240906854160 = _DEFAULT_MARKER

            # <Substitution u'view/name' (8:31)> -> __attr_name
            __token = 369
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'view/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906853392
            __default_140240906853392 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (9:31)> -> __attr_class
            __token = 412
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852688
            __default_140240906852688 = _DEFAULT_MARKER

            # <Substitution u'view/title' (11:29)> -> __attr_title
            __token = 500
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852176
            __default_140240906852176 = _DEFAULT_MARKER

            # <Substitution u'view/lang' (12:27)> -> __attr_lang
            __token = 543
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906778000
            __default_140240906778000 = _DEFAULT_MARKER

            # <Boolean u'view/disabled' (24:19)> -> __attr_disabled
            __token = 1163
            try:
                __zt_tmp = __attrs_140240906997520
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

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906780112
            __default_140240906780112 = _DEFAULT_MARKER

            # <Boolean u'view/readonly' (29:14)> -> __attr_readonly
            __token = 1407
            try:
                __zt_tmp = __attrs_140240906997520
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

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906780304
            __default_140240906780304 = _DEFAULT_MARKER

            # <Substitution u'view/alt' (30:8)> -> __attr_alt
            __token = 1452
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_140241087907024('path', u'view/alt', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((u' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906850384
            __default_140240906850384 = _DEFAULT_MARKER

            # <Substitution u'view/tabindex' (25:18)> -> __attr_tabindex
            __token = 1213
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((u' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906776976
            __default_140240906776976 = _DEFAULT_MARKER

            # <Substitution u'view/accesskey' (31:13)> -> __attr_accesskey
            __token = 1498
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140241087907024('path', u'view/accesskey', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((u' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906780624
            __default_140240906780624 = _DEFAULT_MARKER

            # <Substitution u'view/size' (33:6)> -> __attr_size
            __token = 1595
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_140241087907024('path', u'view/size', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((u' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906779536
            __default_140240906779536 = _DEFAULT_MARKER

            # <Substitution u'view/maxlength' (34:10)> -> __attr_maxlength
            __token = 1642
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_140241087907024('path', u'view/maxlength', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((u' maxlength="%s"' % __attr_maxlength))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906777872
            __default_140240906777872 = _DEFAULT_MARKER

            # <Substitution u'view/style' (10:30)> -> __attr_style
            __token = 456
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906779856
            __default_140240906779856 = _DEFAULT_MARKER

            # <Substitution u'view/value' (23:17)> -> __attr_value
            __token = 1116
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'view/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' type="text"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906778640
            __default_140240906778640 = _DEFAULT_MARKER

            # <Substitution u'view/onclick' (13:29)> -> __attr_onclick
            __token = 588
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((u' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906779216
            __default_140240906779216 = _DEFAULT_MARKER

            # <Substitution u'view/ondblclick' (14:31)> -> __attr_ondblclick
            __token = 639
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((u' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917095888
            __default_140240917095888 = _DEFAULT_MARKER

            # <Substitution u'view/onmousedown' (15:31)> -> __attr_onmousedown
            __token = 694
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((u' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917098000
            __default_140240917098000 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseup' (16:28)> -> __attr_onmouseup
            __token = 748
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((u' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917096208
            __default_140240917096208 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseover' (17:29)> -> __attr_onmouseover
            __token = 802
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((u' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917097360
            __default_140240917097360 = _DEFAULT_MARKER

            # <Substitution u'view/onmousemove' (18:28)> -> __attr_onmousemove
            __token = 858
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((u' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917094800
            __default_140240917094800 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseout' (19:26)> -> __attr_onmouseout
            __token = 913
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((u' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917096784
            __default_140240917096784 = _DEFAULT_MARKER

            # <Substitution u'view/onkeypress' (20:25)> -> __attr_onkeypress
            __token = 967
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((u' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917097424
            __default_140240917097424 = _DEFAULT_MARKER

            # <Substitution u'view/onkeydown' (21:23)> -> __attr_onkeydown
            __token = 1020
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917098384
            __default_140240917098384 = _DEFAULT_MARKER

            # <Substitution u'view/onkeyup' (22:20)> -> __attr_onkeyup
            __token = 1070
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917095504
            __default_140240917095504 = _DEFAULT_MARKER

            # <Substitution u'view/onfocus' (26:16)> -> __attr_onfocus
            __token = 1262
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((u' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240948231568
            __default_140240948231568 = _DEFAULT_MARKER

            # <Substitution u'view/onblur' (27:14)> -> __attr_onblur
            __token = 1309
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((u' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906996048
            __default_140240906996048 = _DEFAULT_MARKER

            # <Substitution u'view/onchange' (28:15)> -> __attr_onchange
            __token = 1357
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((u' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906994128
            __default_140240906994128 = _DEFAULT_MARKER

            # <Substitution u'view/onselect' (32:11)> -> __attr_onselect
            __token = 1549
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140241087907024('path', u'view/onselect', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((u' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906995728
            __default_140240906995728 = _DEFAULT_MARKER

            # <Substitution u'view/placeholder' (35:11)> -> __attr_placeholder
            __token = 1696
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_140241087907024('path', u'view/placeholder', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((u' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906996304
            __default_140240906996304 = _DEFAULT_MARKER

            # <Substitution u'view/autocapitalize' (36:13)> -> __attr_autocapitalize
            __token = 1755
            try:
                __zt_tmp = __attrs_140240906997520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_autocapitalize = _static_140241087907024('path', u'view/autocapitalize', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_autocapitalize = __quote(__attr_autocapitalize, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_autocapitalize is not None):
                __append((u' autocapitalize="%s"' % __attr_autocapitalize))
            __append(u' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }