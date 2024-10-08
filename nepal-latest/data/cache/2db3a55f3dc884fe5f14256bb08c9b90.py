# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/select_input.pt'

__tokens = {218: (u'view/id', 5, 27), 255: (u' string:${view/name}:lis', 6, 28), 310: (u's view/kla', 7, 28), 1022: (u'        tabin', 22, 16), 975: (u'       disabl', 21, 17), 1204: (u'            m', 26, 12), 1247: (u'         ', 27, 7), 351: (u'le view/st', 8, 27), 392: (u'tle view/t', 9, 26), 432: (u'lang view', 10, 24), 474: (u'click view/o', 11, 26), 522: (u'lclick view/ond', 12, 28), 574: (u'usedown view/onm', 13, 28), 625: (u'nmouseup view/', 14, 25), 676: (u'mouseover view/o', 15, 26), 729: (u'nmousemove view/', 16, 25), 781: (u' onmouseout vie', 17, 23), 832: (u'  onkeypress vi', 18, 22), 882: (u'    onkeydown ', 19, 20), 929: (u'       onkey', 20, 17), 1068: (u'          on', 23, 14), 1112: (u'           ', 24, 12), 1157: (u'           on', 25, 13), 1305: (u'view/items', 28, 24), 1387: (u'item/selected', 30, 24), 1430: (u'item/id', 31, 28), 1469: (u' item/valu', 32, 30), 1504: (u'item/content', 33, 22), 1582: (u'not:item/selected', 35, 24), 1629: (u'item/id', 36, 28), 1668: (u' item/valu', 37, 30), 1703: (u'item/content', 38, 22), 1840: (u'string:${view/name}-empty-marker', 42, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906501136 = {u'type': u'hidden', u'name': u'field-empty-marker', u'value': u'1', }
_static_140240906501776 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240906501968 = {u'onmousedown': u'view/onmousedown', u'disabled': u'', u'onchange': u'view/onchange', u'id': u'', u'size': u'', u'style': u'view/style', u'title': u'view/title', u'onmousemove': u'view/onmousemove', u'onmouseup': u'view/onmouseup', u'onfocus': u'view/onfocus', u'onblur': u'view/onblur', u'multiple': u'', u'onclick': u'view/onclick', u'onmouseout': u'view/onmouseout', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'onmouseover': u'view/onmouseover', u'class': u'', u'lang': u'view/lang', u'name': u'', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'tabindex': u'', }
_static_140241133802128 = {}
_static_140240906773008 = {u'selected': u'selected', u'id': u'', u'value': u'', }
_static_140240906829136 = {u'id': u'', u'value': u'', }

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

            # <Static value=<_ast.Dict object at 0x7f8c616a3e90> name=None at 7f8c616a39d0> -> __attrs_140240906501328
            __attrs_140240906501328 = _static_140240906501776
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c616a3f50> name=None at 7f8c616a3950> -> __attrs_140240906535824
            __attrs_140240906535824 = _static_140240906501968

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907126288
            __default_140240907126288 = _DEFAULT_MARKER

            # <Substitution u'view/id' (5:27)> -> __attr_id
            __token = 218
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907126416
            __default_140240907126416 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}:list' (6:28)> -> __attr_name
            __token = 255
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('string', u'${view/name}:list', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907125072
            __default_140240907125072 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (7:28)> -> __attr_class
            __token = 310
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907128144
            __default_140240907128144 = _DEFAULT_MARKER

            # <Substitution u'view/tabindex' (22:16)> -> __attr_tabindex
            __token = 1022
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140241087907024('path', u'view/tabindex', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((u' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907125264
            __default_140240907125264 = _DEFAULT_MARKER

            # <Boolean u'view/disabled' (21:17)> -> __attr_disabled
            __token = 975
            try:
                __zt_tmp = __attrs_140240906535824
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

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907127952
            __default_140240907127952 = _DEFAULT_MARKER

            # <Boolean u'view/multiple' (26:12)> -> __attr_multiple
            __token = 1204
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_140241087907024('path', u'view/multiple', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = u''
            else:
                if __attr_multiple:
                    __attr_multiple = u'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((u' multiple="%s"' % __attr_multiple))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907125136
            __default_140240907125136 = _DEFAULT_MARKER

            # <Substitution u'view/size' (27:7)> -> __attr_size
            __token = 1247
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_140241087907024('path', u'view/size', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((u' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907128080
            __default_140240907128080 = _DEFAULT_MARKER

            # <Substitution u'view/style' (8:27)> -> __attr_style
            __token = 351
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907127440
            __default_140240907127440 = _DEFAULT_MARKER

            # <Substitution u'view/title' (9:26)> -> __attr_title
            __token = 392
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907127056
            __default_140240907127056 = _DEFAULT_MARKER

            # <Substitution u'view/lang' (10:24)> -> __attr_lang
            __token = 432
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907127248
            __default_140240907127248 = _DEFAULT_MARKER

            # <Substitution u'view/onclick' (11:26)> -> __attr_onclick
            __token = 474
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((u' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240971117520
            __default_140240971117520 = _DEFAULT_MARKER

            # <Substitution u'view/ondblclick' (12:28)> -> __attr_ondblclick
            __token = 522
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((u' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906534992
            __default_140240906534992 = _DEFAULT_MARKER

            # <Substitution u'view/onmousedown' (13:28)> -> __attr_onmousedown
            __token = 574
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((u' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906535312
            __default_140240906535312 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseup' (14:25)> -> __attr_onmouseup
            __token = 625
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((u' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906536400
            __default_140240906536400 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseover' (15:26)> -> __attr_onmouseover
            __token = 676
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((u' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906536976
            __default_140240906536976 = _DEFAULT_MARKER

            # <Substitution u'view/onmousemove' (16:25)> -> __attr_onmousemove
            __token = 729
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((u' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906536528
            __default_140240906536528 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseout' (17:23)> -> __attr_onmouseout
            __token = 781
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((u' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906538768
            __default_140240906538768 = _DEFAULT_MARKER

            # <Substitution u'view/onkeypress' (18:22)> -> __attr_onkeypress
            __token = 832
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((u' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906536464
            __default_140240906536464 = _DEFAULT_MARKER

            # <Substitution u'view/onkeydown' (19:20)> -> __attr_onkeydown
            __token = 882
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906536592
            __default_140240906536592 = _DEFAULT_MARKER

            # <Substitution u'view/onkeyup' (20:17)> -> __attr_onkeyup
            __token = 929
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906535440
            __default_140240906535440 = _DEFAULT_MARKER

            # <Substitution u'view/onfocus' (23:14)> -> __attr_onfocus
            __token = 1068
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140241087907024('path', u'view/onfocus', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((u' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906535696
            __default_140240906535696 = _DEFAULT_MARKER

            # <Substitution u'view/onblur' (24:12)> -> __attr_onblur
            __token = 1112
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140241087907024('path', u'view/onblur', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((u' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906535888
            __default_140240906535888 = _DEFAULT_MARKER

            # <Substitution u'view/onchange' (25:13)> -> __attr_onchange
            __token = 1157
            try:
                __zt_tmp = __attrs_140240906535824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140241087907024('path', u'view/onchange', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((u' onchange="%s"' % __attr_onchange))
            __append(u'>\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917728016
            __attrs_140240917728016 = _static_140241133802128
            __backup_item_140240906826960 = get('item', __marker)

            # <Value u'view/items' (28:24)> -> __iterator
            __token = 1305
            try:
                __zt_tmp = __attrs_140240917728016
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/items', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240917728144, ) = getitem('repeat')(u'item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <Static value=<_ast.Dict object at 0x7f8c616e6210> name=None at 7f8c616e6450> -> __attrs_140240906829072
                __attrs_140240906829072 = _static_140240906773008

                # <Value u'item/selected' (30:24)> -> __condition
                __token = 1387
                try:
                    __zt_tmp = __attrs_140240906829072
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'item/selected', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906773712
                    __default_140240906773712 = _DEFAULT_MARKER

                    # <Substitution u'item/id' (31:28)> -> __attr_id
                    __token = 1430
                    try:
                        __zt_tmp = __attrs_140240906829072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('path', u'item/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906773264
                    __default_140240906773264 = _DEFAULT_MARKER

                    # <Substitution u'item/value' (32:30)> -> __attr_value
                    __token = 1469
                    try:
                        __zt_tmp = __attrs_140240906829072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'item/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' selected="selected">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906774352
                    __default_140240906774352 = _DEFAULT_MARKER

                    # <Value u'item/content' (33:22)> -> __cache_140240906577424
                    __token = 1504
                    try:
                        __zt_tmp = __attrs_140240906829072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906577424 = _static_140241087907024('path', u'item/content', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/content' (33:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e6410> -> __condition
                    __expression = __cache_140240906577424

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'label')
                    else:
                        __content = __cache_140240906577424
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option\n   >')

                # <Static value=<_ast.Dict object at 0x7f8c616f3d50> name=None at 7f8c616f3090> -> __attrs_140240906826320
                __attrs_140240906826320 = _static_140240906829136

                # <Value u'not:item/selected' (35:24)> -> __condition
                __token = 1582
                try:
                    __zt_tmp = __attrs_140240906826320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('not', u'item/selected', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906829712
                    __default_140240906829712 = _DEFAULT_MARKER

                    # <Substitution u'item/id' (36:28)> -> __attr_id
                    __token = 1629
                    try:
                        __zt_tmp = __attrs_140240906826320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('path', u'item/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906826704
                    __default_140240906826704 = _DEFAULT_MARKER

                    # <Substitution u'item/value' (37:30)> -> __attr_value
                    __token = 1668
                    try:
                        __zt_tmp = __attrs_140240906826320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'item/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906827536
                    __default_140240906827536 = _DEFAULT_MARKER

                    # <Value u'item/content' (38:22)> -> __cache_140240906828752
                    __token = 1703
                    try:
                        __zt_tmp = __attrs_140240906826320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906828752 = _static_140241087907024('path', u'item/content', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/content' (38:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616f35d0> -> __condition
                    __expression = __cache_140240906828752

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'label')
                    else:
                        __content = __cache_140240906828752
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option\n >')
                ____index_140240917728144 -= 1
                if (____index_140240917728144 > 0):
                    __append('')
            if (__backup_item_140240906826960 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140240906826960
            __append(u'\n</select>\n')

            # <Static value=<_ast.Dict object at 0x7f8c616a3c10> name=None at 7f8c616a3810> -> __attrs_140240927272912
            __attrs_140240927272912 = _static_140240906501136

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917725264
            __default_140240917725264 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}-empty-marker' (42:28)> -> __attr_name
            __token = 1840
            try:
                __zt_tmp = __attrs_140240927272912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('string', u'${view/name}-empty-marker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u' type="hidden" value="1" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }