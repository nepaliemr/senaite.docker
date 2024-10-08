# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/listingtitle.pt'

__tokens = {143: (u'view/icon', 4, 32), 243: (u'view/title', 8, 19)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574267882896 = {u'class': u'd-inline-block align-middle', }
_static_140574442558096 = {}
_static_140574267907600 = {u'class': u'listing-title-viewlet d-inline-block', }
_static_140574397981968 = __compile_zt_expr
_static_140574267904912 = {u'class': u'd-inline-block align-middle', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff4d9e10> name=None at 7fd9ff4d94d0> -> __attrs_140574267904400
            __attrs_140574267904400 = _static_140574267907600

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="listing-title-viewlet d-inline-block">\n  <!-- icon -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4d9390> name=None at 7fd9ff4d9c50> -> __attrs_140574267883216
            __attrs_140574267883216 = _static_140574267904912

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="d-inline-block align-middle">\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267880272
            __attrs_140574267880272 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267879952
            __default_140574267879952 = _DEFAULT_MARKER

            # <Value u'view/icon' (4:32)> -> __cache_140574267881744
            __token = 143
            try:
                __zt_tmp = __attrs_140574267880272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574267881744 = _static_140574397981968('path', u'view/icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/icon' (4:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d33d0> -> __condition
            __expression = __cache_140574267881744

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img/>')
            else:
                __content = __cache_140574267881744
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n  </div>\n  <!-- title -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4d3d90> name=None at 7fd9ff4d3ad0> -> __attrs_140574267881360
            __attrs_140574267881360 = _static_140574267882896

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1 class="d-inline-block align-middle">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267883408
            __default_140574267883408 = _DEFAULT_MARKER

            # <Value u'view/title' (8:19)> -> __cache_140574267882064
            __token = 243
            try:
                __zt_tmp = __attrs_140574267881360
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574267882064 = _static_140574397981968('path', u'view/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/title' (8:19)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d3a10> -> __condition
            __expression = __cache_140574267882064

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n  ')
            else:
                __content = __cache_140574267882064
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</h1>\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }