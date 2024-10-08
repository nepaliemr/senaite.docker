# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/textarea_input.pt'

__tokens = {245: (u'view/id', 7, 22), 277: (u' view/nam', 8, 23), 312: (u's view/kla', 9, 23), 1107: (u'         ', 28, 3), 1141: (u'         ', 29, 2), 949: (u'        tabin', 24, 11), 907: (u'       disabl', 23, 12), 1179: (u'             ', 30, 5), 1222: (u'              ', 31, 5), 348: (u'le view/st', 10, 22), 384: (u'tle view/t', 11, 21), 419: (u'lang view', 12, 19), 456: (u'click view/o', 13, 21), 499: (u'lclick view/ond', 14, 23), 546: (u'usedown view/onm', 15, 23), 592: (u'nmouseup view/', 16, 20), 638: (u'mouseover view/o', 17, 21), 686: (u'nmousemove view/', 18, 20), 733: (u' onmouseout vie', 19, 18), 779: (u'  onkeypress vi', 20, 17), 824: (u'    onkeydown ', 21, 15), 866: (u'       onkey', 22, 12), 990: (u'          on', 25, 9), 1029: (u'           ', 26, 7), 1069: (u'           on', 27, 8), 1265: (u'             ', 32, 3), 1321: (u'view/value', 33, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240906803024 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906997584 = {u'accesskey': u'', u'cols': u'', u'onmousedown': u'view/onmousedown', u'disabled': u'', u'onchange': u'view/onchange', u'id': u'', u'style': u'view/style', u'rows': u'', u'title': u'view/title', u'readonly': u'', u'onselect': u'view/onselect', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'onblur': u'view/onblur', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'class': u'', u'lang': u'view/lang', u'name': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'', }

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

            # <Static value=<_ast.Dict object at 0x7f8c616ed750> name=None at 7f8c616ed150> -> __attrs_140240906776912
            __attrs_140240906776912 = _static_140240906803024
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c6171cf50> name=None at 7f8c6171ca90> -> __attrs_140240907128656
            __attrs_140240907128656 = _static_140240906997584

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append(u'<textarea')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917094544
            __default_140240917094544 = _DEFAULT_MARKER

            # <Substitution u'view/id' (7:22)> -> __attr_id
            __token = 245
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917097744
            __default_140240917097744 = _DEFAULT_MARKER

            # <Substitution u'view/name' (8:23)> -> __attr_name
            __token = 277
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'view/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917094992
            __default_140240917094992 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (9:23)> -> __attr_class
            __token = 312
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917095504
            __default_140240917095504 = _DEFAULT_MARKER

            # <Substitution u'view/cols' (28:3)> -> __attr_cols
            __token = 1107
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_cols = _static_140241087907024('path', u'view/cols', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_cols = __quote(__attr_cols, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_cols is not None):
                __append((u' cols="%s"' % __attr_cols))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906850832
            __default_140240906850832 = _DEFAULT_MARKER

            # <Substitution u'view/rows' (29:2)> -> __attr_rows
            __token = 1141
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_rows = _static_140241087907024('path', u'view/rows', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_rows = __quote(__attr_rows, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_rows is not None):
                __append((u' rows="%s"' % __attr_rows))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906851280
            __default_140240906851280 = _DEFAULT_MARKER

            # <Substitution u'view/tabindex' (24:11)> -> __attr_tabindex
            __token = 949
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((u' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852048
            __default_140240906852048 = _DEFAULT_MARKER

            # <Boolean u'view/disabled' (23:12)> -> __attr_disabled
            __token = 907
            try:
                __zt_tmp = __attrs_140240907128656
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

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906854032
            __default_140240906854032 = _DEFAULT_MARKER

            # <Boolean u'view/readonly' (30:5)> -> __attr_readonly
            __token = 1179
            try:
                __zt_tmp = __attrs_140240907128656
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

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906850896
            __default_140240906850896 = _DEFAULT_MARKER

            # <Substitution u'view/accesskey' (31:5)> -> __attr_accesskey
            __token = 1222
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140241087907024('path', u'view/accesskey', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((u' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906853776
            __default_140240906853776 = _DEFAULT_MARKER

            # <Substitution u'view/style' (10:22)> -> __attr_style
            __token = 348
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906853840
            __default_140240906853840 = _DEFAULT_MARKER

            # <Substitution u'view/title' (11:21)> -> __attr_title
            __token = 384
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852368
            __default_140240906852368 = _DEFAULT_MARKER

            # <Substitution u'view/lang' (12:19)> -> __attr_lang
            __token = 419
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906854160
            __default_140240906854160 = _DEFAULT_MARKER

            # <Substitution u'view/onclick' (13:21)> -> __attr_onclick
            __token = 456
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((u' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906853392
            __default_140240906853392 = _DEFAULT_MARKER

            # <Substitution u'view/ondblclick' (14:23)> -> __attr_ondblclick
            __token = 499
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((u' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852752
            __default_140240906852752 = _DEFAULT_MARKER

            # <Substitution u'view/onmousedown' (15:23)> -> __attr_onmousedown
            __token = 546
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((u' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906852176
            __default_140240906852176 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseup' (16:20)> -> __attr_onmouseup
            __token = 592
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((u' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906850384
            __default_140240906850384 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseover' (17:21)> -> __attr_onmouseover
            __token = 638
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((u' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240916649168
            __default_140240916649168 = _DEFAULT_MARKER

            # <Substitution u'view/onmousemove' (18:20)> -> __attr_onmousemove
            __token = 686
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((u' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240916804112
            __default_140240916804112 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseout' (19:18)> -> __attr_onmouseout
            __token = 733
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((u' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906721744
            __default_140240906721744 = _DEFAULT_MARKER

            # <Substitution u'view/onkeypress' (20:17)> -> __attr_onkeypress
            __token = 779
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((u' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907126288
            __default_140240907126288 = _DEFAULT_MARKER

            # <Substitution u'view/onkeydown' (21:15)> -> __attr_onkeydown
            __token = 824
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907128720
            __default_140240907128720 = _DEFAULT_MARKER

            # <Substitution u'view/onkeyup' (22:12)> -> __attr_onkeyup
            __token = 866
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907126992
            __default_140240907126992 = _DEFAULT_MARKER

            # <Substitution u'view/onfocus' (25:9)> -> __attr_onfocus
            __token = 990
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((u' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907126224
            __default_140240907126224 = _DEFAULT_MARKER

            # <Substitution u'view/onblur' (26:7)> -> __attr_onblur
            __token = 1029
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((u' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907128144
            __default_140240907128144 = _DEFAULT_MARKER

            # <Substitution u'view/onchange' (27:8)> -> __attr_onchange
            __token = 1069
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((u' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907125264
            __default_140240907125264 = _DEFAULT_MARKER

            # <Substitution u'view/onselect' (32:3)> -> __attr_onselect
            __token = 1265
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140241087907024('path', u'view/onselect', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((u' onselect="%s"' % __attr_onselect))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906804624
            __default_140240906804624 = _DEFAULT_MARKER

            # <Value u'view/value' (33:16)> -> __cache_140240906803792
            __token = 1321
            try:
                __zt_tmp = __attrs_140240907128656
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240906803792 = _static_140241087907024('path', u'view/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/value' (33:16)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616edb50> -> __condition
            __expression = __cache_140240906803792

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240906803792
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</textarea>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }