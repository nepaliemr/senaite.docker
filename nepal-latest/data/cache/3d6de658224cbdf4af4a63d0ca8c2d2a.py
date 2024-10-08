# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/submit_input.pt'

__tokens = {218: (u'view/id', 6, 26), 254: (u' view/nam', 7, 27), 293: (u's view/kla', 8, 27), 901: (u'         v', 21, 14), 1251: (u'             a', 29, 10), 333: (u'le view/st', 9, 26), 372: (u'ang view/', 10, 24), 413: (u'lick view/on', 11, 26), 460: (u'click view/ondb', 12, 28), 511: (u'sedown view/onmo', 13, 28), 561: (u'mouseup view/o', 14, 25), 611: (u'ouseover view/on', 15, 26), 663: (u'mousemove view/o', 16, 25), 714: (u'onmouseout view', 17, 23), 764: (u' onkeypress vie', 18, 22), 813: (u'   onkeydown v', 19, 20), 859: (u'      onkeyu', 20, 17), 944: (u'       disabl', 22, 16), 990: (u'        tabin', 23, 15), 1035: (u'          on', 24, 13), 1078: (u'           ', 25, 11), 1122: (u'           on', 26, 12), 1168: (u'            r', 27, 11), 1209: (u'        ', 28, 5), 1298: (u'             ', 30, 8)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907024 = __compile_zt_expr
_static_140240906535568 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240906827088 = {u'accesskey': u'', u'onmousedown': u'view/onmousedown', u'disabled': u'view/disabled', u'alt': u'view/alt', u'onchange': u'view/onchange', u'id': u'', u'style': u'view/style', u'readonly': u'view/readonly', u'onselect': u'view/onselect', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'type': u'submit', u'onblur': u'view/onblur', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'class': u'', u'lang': u'view/lang', u'name': u'', u'value': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'view/tabindex', }
_static_140241087907728 = __C2ZContextWrapper

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

            # <Static value=<_ast.Dict object at 0x7f8c616ac290> name=None at 7f8c616accd0> -> __attrs_140240906536080
            __attrs_140240906536080 = _static_140240906535568
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c616f3550> name=None at 7f8c616f31d0> -> __attrs_140240963269712
            __attrs_140240963269712 = _static_140240906827088

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907067344
            __default_140240907067344 = _DEFAULT_MARKER

            # <Substitution u'view/id' (6:26)> -> __attr_id
            __token = 218
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907065488
            __default_140240907065488 = _DEFAULT_MARKER

            # <Substitution u'view/name' (7:27)> -> __attr_name
            __token = 254
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'view/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907066256
            __default_140240907066256 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (8:27)> -> __attr_class
            __token = 293
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907065104
            __default_140240907065104 = _DEFAULT_MARKER

            # <Substitution u'view/value' (21:14)> -> __attr_value
            __token = 901
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'view/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907066128
            __default_140240907066128 = _DEFAULT_MARKER

            # <Substitution u'view/accesskey' (29:10)> -> __attr_accesskey
            __token = 1251
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140241087907024('path', u'view/accesskey', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((u' accesskey="%s"' % __attr_accesskey))
            __append(u' type="submit"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907066448
            __default_140240907066448 = _DEFAULT_MARKER

            # <Substitution u'view/style' (9:26)> -> __attr_style
            __token = 333
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907064848
            __default_140240907064848 = _DEFAULT_MARKER

            # <Substitution u'view/lang' (10:24)> -> __attr_lang
            __token = 372
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907063376
            __default_140240907063376 = _DEFAULT_MARKER

            # <Substitution u'view/onclick' (11:26)> -> __attr_onclick
            __token = 413
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((u' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907065872
            __default_140240907065872 = _DEFAULT_MARKER

            # <Substitution u'view/ondblclick' (12:28)> -> __attr_ondblclick
            __token = 460
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((u' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907067088
            __default_140240907067088 = _DEFAULT_MARKER

            # <Substitution u'view/onmousedown' (13:28)> -> __attr_onmousedown
            __token = 511
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((u' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907064656
            __default_140240907064656 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseup' (14:25)> -> __attr_onmouseup
            __token = 561
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((u' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907064976
            __default_140240907064976 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseover' (15:26)> -> __attr_onmouseover
            __token = 611
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((u' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907129296
            __default_140240907129296 = _DEFAULT_MARKER

            # <Substitution u'view/onmousemove' (16:25)> -> __attr_onmousemove
            __token = 663
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((u' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907131728
            __default_140240907131728 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseout' (17:23)> -> __attr_onmouseout
            __token = 714
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((u' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907131856
            __default_140240907131856 = _DEFAULT_MARKER

            # <Substitution u'view/onkeypress' (18:22)> -> __attr_onkeypress
            __token = 764
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((u' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907131152
            __default_140240907131152 = _DEFAULT_MARKER

            # <Substitution u'view/onkeydown' (19:20)> -> __attr_onkeydown
            __token = 813
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907132624
            __default_140240907132624 = _DEFAULT_MARKER

            # <Substitution u'view/onkeyup' (20:17)> -> __attr_onkeyup
            __token = 859
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907131920
            __default_140240907131920 = _DEFAULT_MARKER

            # <Boolean u'view/disabled' (22:16)> -> __attr_disabled
            __token = 944
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_140241087907024('path', u'view/disabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = u'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((u' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907132560
            __default_140240907132560 = _DEFAULT_MARKER

            # <Substitution u'view/tabindex' (23:15)> -> __attr_tabindex
            __token = 990
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((u' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907129104
            __default_140240907129104 = _DEFAULT_MARKER

            # <Substitution u'view/onfocus' (24:13)> -> __attr_onfocus
            __token = 1035
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((u' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907129168
            __default_140240907129168 = _DEFAULT_MARKER

            # <Substitution u'view/onblur' (25:11)> -> __attr_onblur
            __token = 1078
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((u' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907132368
            __default_140240907132368 = _DEFAULT_MARKER

            # <Substitution u'view/onchange' (26:12)> -> __attr_onchange
            __token = 1122
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((u' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917395856
            __default_140240917395856 = _DEFAULT_MARKER

            # <Boolean u'view/readonly' (27:11)> -> __attr_readonly
            __token = 1168
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_140241087907024('path', u'view/readonly', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = u'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((u' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140241185996880
            __default_140241185996880 = _DEFAULT_MARKER

            # <Substitution u'view/alt' (28:5)> -> __attr_alt
            __token = 1209
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_140241087907024('path', u'view/alt', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((u' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240971208592
            __default_140240971208592 = _DEFAULT_MARKER

            # <Substitution u'view/onselect' (30:8)> -> __attr_onselect
            __token = 1298
            try:
                __zt_tmp = __attrs_140240963269712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140241087907024('path', u'view/onselect', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((u' onselect="%s"' % __attr_onselect))
            __append(u' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }