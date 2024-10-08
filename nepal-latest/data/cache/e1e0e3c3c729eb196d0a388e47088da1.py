# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.z3cform-3.2.4-py2.7.egg/plone/app/z3cform/templates/layout.pt'

__tokens = {469: (u'view/label', 12, 58), 550: (u'view/contents', 13, 58), 261: (u'here/main_template/macros/master', 6, 23), 261: (u'here/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240963270160 = {u'id': u'content-core', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140241133802128 = {}
_static_140240917092240 = {u'class': u'documentFirstHeading', }
_static_140240906426064 = u'master'

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917093200
            __attrs_140240917093200 = _static_140241133802128
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c620bd790> name=None at 7f8c620bda10> -> __attrs_140240917091728
            __attrs_140240917091728 = _static_140240917092240

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1 class="documentFirstHeading">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917090512
            __default_140240917090512 = _DEFAULT_MARKER

            # <Value u'view/label' (12:58)> -> __cache_140240917090704
            __token = 469
            try:
                __zt_tmp = __attrs_140240917091728
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240917090704 = _static_140241087907024('path', u'view/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/label' (12:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c620bd9d0> -> __condition
            __expression = __cache_140240917090704

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'Title')
            else:
                __content = __cache_140240917090704
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</h1>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c64cc7610> name=None at 7f8c64cc7810> -> __attrs_140240916643536
            __attrs_140240916643536 = _static_140240963270160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="content-core">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240918270160
            __default_140240918270160 = _DEFAULT_MARKER

            # <Value u'view/contents' (13:58)> -> __cache_140240917091088
            __token = 550
            try:
                __zt_tmp = __attrs_140240916643536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240917091088 = _static_140241087907024('path', u'view/contents', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/contents' (13:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c621ea550> -> __condition
            __expression = __cache_140240917091088

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240917091088
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n        ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906427664
            __attrs_140240906427664 = _static_140241133802128
            __previous_i18n_domain_140240906427408 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140240933904464 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c616916d0> name=None at 7f8c61691bd0> -> __value
            __value = _static_140240906426064
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917090832
                __attrs_140240917090832 = _static_140241133802128
                __append(u'\n        ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_main'] = _deque((__fill_main, ))

            # <Value u'here/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140240906427664
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'here/main_template/macros/master', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240933904464 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240933904464
            __i18n_domain = __previous_i18n_domain_140240906427408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_main': render_main, 'render': render, }