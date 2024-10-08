# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/browser/viewlets/templates/content.pt'

__tokens = {146: (u'view/contents_table', 5, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574255627792 = {u'class': u'mt-3 listing-table', }
_static_140574256157008 = {u'id': u'impress-contents-table', }
_static_140574272152784 = {u'class': u'col-sm-12', }
_static_140574397981968 = __compile_zt_expr
_static_140574397982672 = __C2ZContextWrapper

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
            __append(u'<!-- CONTENTS -->\n')

            # <Static value=<_ast.Dict object at 0x7fd9ff8e64d0> name=None at 7fd9f757c950> -> __attrs_140574267349712
            __attrs_140574267349712 = _static_140574272152784

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9fe923e10> name=None at 7fd9fe9235d0> -> __attrs_140574270172880
            __attrs_140574270172880 = _static_140574255627792

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mt-3 listing-table">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9fe9a5150> name=None at 7fd9ff469d10> -> __attrs_140574257315600
            __attrs_140574257315600 = _static_140574256157008

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="impress-contents-table">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267447376
            __default_140574267447376 = _DEFAULT_MARKER

            # <Value u'view/contents_table' (5:32)> -> __cache_140574133885456
            __token = 146
            try:
                __zt_tmp = __attrs_140574257315600
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574133885456 = _static_140574397981968('path', u'view/contents_table', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/contents_table' (5:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f7509450> -> __condition
            __expression = __cache_140574133885456

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n    ')
            else:
                __content = __cache_140574133885456
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n  </div>\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }