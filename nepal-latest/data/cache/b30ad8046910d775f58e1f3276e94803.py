# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/listingdescription.pt'

__tokens = {46: (u'view/description', 2, 29), 84: (u'description', 3, 20), 194: (u'description', 6, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574267913680 = {u'class': u'text-secondary small', }
_static_140574268017424 = {u'class': u'row', }
_static_140574257290768 = {u'class': u'col-sm-12', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff4f4b10> name=None at 7fd9ff4f4950> -> __attrs_140574268018512
            __attrs_140574268018512 = _static_140574268017424
            __backup_description_140574284337744 = get('description', __marker)

            # <Value u'view/description' (2:29)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140574268018512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value u'description' (3:20)> -> __condition
            __token = 84
            try:
                __zt_tmp = __attrs_140574268018512
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9feab9e10> name=None at 7fd9feab9490> -> __attrs_140574257288272
                __attrs_140574257288272 = _static_140574257290768

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4db5d0> name=None at 7fd9ff4db050> -> __attrs_140574266168976
                __attrs_140574266168976 = _static_140574267913680

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="text-secondary small">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267915792
                __default_140574267915792 = _DEFAULT_MARKER

                # <Value u'description' (6:32)> -> __cache_140574267888976
                __token = 194
                try:
                    __zt_tmp = __attrs_140574266168976
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267888976 = _static_140574397981968('path', u'description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'description' (6:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d5c50> -> __condition
                __expression = __cache_140574267888976

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574267888976
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n  </div>\n</div>')
            if (__backup_description_140574284337744 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140574284337744
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }