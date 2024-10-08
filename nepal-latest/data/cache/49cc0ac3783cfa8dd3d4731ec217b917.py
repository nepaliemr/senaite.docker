# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/z3c.form-3.7.1-py2.7.egg/z3c/form/browser/text_display.pt'

__tokens = {173: (u'view/id', 5, 29), 213: (u' view/klas', 6, 31), 256: (u'e view/sty', 7, 30), 299: (u'le view/ti', 8, 29), 341: (u'ang view/', 9, 27), 385: (u'lick view/on', 10, 29), 435: (u'click view/ondb', 11, 31), 489: (u'sedown view/onmo', 12, 31), 542: (u'mouseup view/o', 13, 28), 595: (u'ouseover view/on', 14, 29), 650: (u'mousemove view/o', 15, 28), 704: (u'onmouseout view', 16, 26), 757: (u' onkeypress vie', 17, 25), 809: (u'   onkeydown v', 18, 23), 858: (u'      onkeyu', 19, 20), 918: (u'view/value', 20, 21), 939: (u'view/value', 20, 42)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907024 = __compile_zt_expr
_static_140241087907728 = __C2ZContextWrapper
_static_140240790062480 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240606442384 = {u'lang': u'view/lang', u'style': u'view/style', u'onmousedown': u'view/onmousedown', u'onmouseup': u'view/onmouseup', u'onmouseout': u'view/onmouseout', u'title': u'view/title', u'onkeypress': u'view/onkeypress', u'onkeydown': u'view/onkeydown', u'class': u'', u'onmousemove': u'view/onmousemove', u'onmouseover': u'view/onmouseover', u'onclick': u'view/onclick', u'onkeyup': u'view/onkeyup', u'ondblclick': u'view/ondblclick', u'id': u'', }
_static_140241133802128 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8c5a798590> name=None at 7f8c5a798a90> -> __attrs_140240790061776
            __attrs_140240790061776 = _static_140240790062480
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c4f87b390> name=None at 7f8c4f87b450> -> __attrs_140240764289296
            __attrs_140240764289296 = _static_140240606442384

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240750204816
            __default_140240750204816 = _DEFAULT_MARKER

            # <Substitution u'view/id' (5:29)> -> __attr_id
            __token = 173
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790920400
            __default_140240790920400 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (6:31)> -> __attr_class
            __token = 213
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790917840
            __default_140240790917840 = _DEFAULT_MARKER

            # <Substitution u'view/style' (7:30)> -> __attr_style
            __token = 256
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790920144
            __default_140240790920144 = _DEFAULT_MARKER

            # <Substitution u'view/title' (8:29)> -> __attr_title
            __token = 299
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790917904
            __default_140240790917904 = _DEFAULT_MARKER

            # <Substitution u'view/lang' (9:27)> -> __attr_lang
            __token = 341
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140241087907024('path', u'view/lang', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790920848
            __default_140240790920848 = _DEFAULT_MARKER

            # <Substitution u'view/onclick' (10:29)> -> __attr_onclick
            __token = 385
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140241087907024('path', u'view/onclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((u' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790918992
            __default_140240790918992 = _DEFAULT_MARKER

            # <Substitution u'view/ondblclick' (11:31)> -> __attr_ondblclick
            __token = 435
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140241087907024('path', u'view/ondblclick', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((u' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790920656
            __default_140240790920656 = _DEFAULT_MARKER

            # <Substitution u'view/onmousedown' (12:31)> -> __attr_onmousedown
            __token = 489
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140241087907024('path', u'view/onmousedown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((u' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790917264
            __default_140240790917264 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseup' (13:28)> -> __attr_onmouseup
            __token = 542
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140241087907024('path', u'view/onmouseup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((u' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790918608
            __default_140240790918608 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseover' (14:29)> -> __attr_onmouseover
            __token = 595
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140241087907024('path', u'view/onmouseover', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((u' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790917200
            __default_140240790917200 = _DEFAULT_MARKER

            # <Substitution u'view/onmousemove' (15:28)> -> __attr_onmousemove
            __token = 650
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140241087907024('path', u'view/onmousemove', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((u' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764292304
            __default_140240764292304 = _DEFAULT_MARKER

            # <Substitution u'view/onmouseout' (16:26)> -> __attr_onmouseout
            __token = 704
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140241087907024('path', u'view/onmouseout', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((u' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764292432
            __default_140240764292432 = _DEFAULT_MARKER

            # <Substitution u'view/onkeypress' (17:25)> -> __attr_onkeypress
            __token = 757
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140241087907024('path', u'view/onkeypress', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((u' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764289808
            __default_140240764289808 = _DEFAULT_MARKER

            # <Substitution u'view/onkeydown' (18:23)> -> __attr_onkeydown
            __token = 809
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140241087907024('path', u'view/onkeydown', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764292816
            __default_140240764292816 = _DEFAULT_MARKER

            # <Substitution u'view/onkeyup' (19:20)> -> __attr_onkeyup
            __token = 858
            try:
                __zt_tmp = __attrs_140240764289296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140241087907024('path', u'view/onkeyup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))
            __append(u'>')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240764290256
            __attrs_140240764290256 = _static_140241133802128

            # <Value u'view/value' (20:21)> -> __condition
            __token = 918
            try:
                __zt_tmp = __attrs_140240764290256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764292048
                __default_140240764292048 = _DEFAULT_MARKER

                # <Value u'view/value' (20:42)> -> __cache_140240764292368
                __token = 939
                try:
                    __zt_tmp = __attrs_140240764290256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240764292368 = _static_140241087907024('path', u'view/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/value' (20:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58f040d0> -> __condition
                __expression = __cache_140240764292368

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240764292368
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append(u'</span>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }