# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/listing/display.pt'

__tokens = {202: (u'python:view.contents_table(editable=False)', 7, 34)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140241133802128 = {}
_static_140240792833872 = {u'class': u'col-sm-12', }
_static_140240603794576 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240792830736 = {u'class': u'row', }

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

            # <Static value=<_ast.Dict object at 0x7f8c4f5f4c90> name=None at 7f8c4f5f4910> -> __attrs_140240792833936
            __attrs_140240792833936 = _static_140240603794576
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c5aa3c310> name=None at 7f8c5aa3c250> -> __attrs_140240792831120
            __attrs_140240792831120 = _static_140240792830736

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c5aa3cf50> name=None at 7f8c5aa3cc10> -> __attrs_140240792833808
            __attrs_140240792833808 = _static_140240792833872

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240786685712
            __attrs_140240786685712 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762434192
            __default_140240762434192 = _DEFAULT_MARKER

            # <Value u'python:view.contents_table(editable=False)' (7:34)> -> __cache_140240792183824
            __token = 202
            try:
                __zt_tmp = __attrs_140240786685712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240792183824 = _static_140241087907024('python', u'view.contents_table(editable=False)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.contents_table(editable=False)' (7:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a99eb50> -> __condition
            __expression = __cache_140240792183824

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div/>')
            else:
                __content = __cache_140240792183824
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </div>\n  </div>\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }