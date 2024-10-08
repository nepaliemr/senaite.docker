# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Zope-4.8.10-py2.7.egg/Products/Five/utilities/browser/manage_interfaces.pt'

__tokens = {27: (u'context/manage_page_header', 1, 27), 99: (u'context/manage_tabs', 2, 27), 193: (u'context/@@edit-markers.html/main', 6, 30), 193: (u'context/@@edit-markers.html/main', 6, 30), 267: (u'context/manage_page_footer', 10, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240605377680 = {u'class': u'container-fluid', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140241133802128 = {}
_static_140240792007376 = u'main'

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240605380176
            __attrs_140240605380176 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240605378832
            __default_140240605378832 = _DEFAULT_MARKER

            # <Value u'context/manage_page_header' (1:27)> -> __cache_140240612748304
            __token = 27
            try:
                __zt_tmp = __attrs_140240605380176
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240612748304 = _static_140241087907024('path', u'context/manage_page_header', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c621b2f50> -> __condition
            __expression = __cache_140240612748304

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1>PAGE HEADER</h1>')
            else:
                __content = __cache_140240612748304
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606021712
            __attrs_140240606021712 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240780687376
            __default_140240780687376 = _DEFAULT_MARKER

            # <Value u'context/manage_tabs' (2:27)> -> __cache_140240605379024
            __token = 99
            try:
                __zt_tmp = __attrs_140240606021712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240605379024 = _static_140241087907024('path', u'context/manage_tabs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4f777b50> -> __condition
            __expression = __cache_140240605379024

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h2>TABS</h2>')
            else:
                __content = __cache_140240605379024
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c4f777490> name=None at 7f8c4f777450> -> __attrs_140240605378960
            __attrs_140240605378960 = _static_140240605377680

            # <main ... (0:0)
            # --------------------------------------------------------
            __append(u'<main class="container-fluid">\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792008144
            __attrs_140240792008144 = _static_140241133802128
            __backup_macroname_140240960656160 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c5a9732d0> name=None at 7f8c5a973050> -> __value
            __value = _static_140240792007376
            econtext['macroname'] = __value

            # <Value u'context/@@edit-markers.html/main' (6:30)> -> __macro
            __token = 193
            try:
                __zt_tmp = __attrs_140240792008144
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'context/@@edit-markers.html/main', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 193
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240960656160 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240960656160
            __append(u'\n\n</main>\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792009744
            __attrs_140240792009744 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240792009040
            __default_140240792009040 = _DEFAULT_MARKER

            # <Value u'context/manage_page_footer' (10:27)> -> __cache_140240792008656
            __token = 267
            try:
                __zt_tmp = __attrs_140240792009744
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240792008656 = _static_140241087907024('path', u'context/manage_page_footer', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/manage_page_footer' (10:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a973b50> -> __condition
            __expression = __cache_140240792008656

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1>PAGE FOOTER</h1>')
            else:
                __content = __cache_140240792008656
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }