# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.CMFPlone-5.2.14-py2.7.egg/Products/CMFPlone/browser/templates/description.pt'

__tokens = {73: (u'context/Description', 2, 28), 143: (u'description', 4, 19), 111: (u'description', 3, 17)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574284480784 = {u'class': u'documentDescription description', }

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

            # <Static value=<_ast.Dict object at 0x7fda004a8110> name=None at 7fda004a89d0> -> __attrs_140574284437328
            __attrs_140574284437328 = _static_140574284480784
            __backup_description_140574284374416 = get('description', __marker)

            # <Value u'context/Description' (2:28)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_140574284437328
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/Description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value u'description' (4:19)> -> __condition
            __token = 143
            try:
                __zt_tmp = __attrs_140574284437328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentDescription description">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284483600
                __default_140574284483600 = _DEFAULT_MARKER

                # <Value u'description' (3:17)> -> __cache_140574284482000
                __token = 111
                try:
                    __zt_tmp = __attrs_140574284437328
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574284482000 = _static_140574397981968('path', u'description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'description' (3:17)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda004a87d0> -> __condition
                __expression = __cache_140574284482000

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n  Description\n')
                else:
                    __content = __cache_140574284482000
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>')
            if (__backup_description_140574284374416 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140574284374416
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }