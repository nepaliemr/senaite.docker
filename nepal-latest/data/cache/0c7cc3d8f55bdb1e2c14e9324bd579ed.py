# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.databox/src/senaite/databox/browser/templates/databox_view.pt'

__tokens = {461: (u'provider:senaite.databox.js', 11, 66), 560: (u'view/render_databox_controls', 14, 34), 660: (u'provider:senaite.abovelistingtable', 16, 67), 774: (u'view/contents_table', 18, 34), 876: (u'provider:senaite.belowlistingtable', 20, 67), 261: (u'context/main_template/macros/master', 6, 23), 261: (u'context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240907111632 = {u'id': u'viewlet-below-content-table', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906500880 = u'master'
_static_140240917093968 = {u'id': u'viewlet-above-listing-table', }
_static_140241133802128 = {}
_static_140240906537232 = {u'id': u'folderlisting-main-table', }
_static_140240906424400 = {u'id': u'viewlet-senaite-databox-js', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906139536
            __attrs_140240906139536 = _static_140241133802128
            __previous_i18n_domain_140240907419024 = __i18n_domain
            __i18n_domain = u'senaite.databox'
            __backup_macroname_140240935300224 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c616a3b10> name=None at 7f8c616a3a10> -> __value
            __value = _static_140240906500880
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906827344
                __attrs_140240906827344 = _static_140241133802128
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c61691050> name=None at 7f8c61691110> -> __attrs_140240906424528
                __attrs_140240906424528 = _static_140240906424400

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-senaite-databox-js">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906426576
                __default_140240906426576 = _DEFAULT_MARKER

                # <Value u'provider:senaite.databox.js' (11:66)> -> __cache_140240906425360
                __token = 461
                try:
                    __zt_tmp = __attrs_140240906424528
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906425360 = _static_140241087907024('provider', u'senaite.databox.js', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.databox.js' (11:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61691a90> -> __condition
                __expression = __cache_140240906425360

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240906425360
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n\n      <!-- Databox Controls -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906425680
                __attrs_140240906425680 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906425744
                __default_140240906425744 = _DEFAULT_MARKER

                # <Value u'view/render_databox_controls' (14:34)> -> __cache_140240906427600
                __token = 560
                try:
                    __zt_tmp = __attrs_140240906425680
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906427600 = _static_140241087907024('path', u'view/render_databox_controls', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/render_databox_controls' (14:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61691810> -> __condition
                __expression = __cache_140240906427600

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div/>')
                else:
                    __content = __cache_140240906427600
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c620bde50> name=None at 7f8c620bd590> -> __attrs_140240917093264
                __attrs_140240917093264 = _static_140240917093968

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-above-listing-table">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917093776
                __default_140240917093776 = _DEFAULT_MARKER

                # <Value u'provider:senaite.abovelistingtable' (16:67)> -> __cache_140240917091088
                __token = 660
                try:
                    __zt_tmp = __attrs_140240917093264
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240917091088 = _static_140241087907024('provider', u'senaite.abovelistingtable', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.abovelistingtable' (16:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c620bda90> -> __condition
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
                __append(u'</div>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c616ac910> name=None at 7f8c616ac290> -> __attrs_140240906774608
                __attrs_140240906774608 = _static_140240906537232

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="folderlisting-main-table">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906538192
                __default_140240906538192 = _DEFAULT_MARKER

                # <Value u'view/contents_table' (18:34)> -> __cache_140240917090576
                __token = 774
                try:
                    __zt_tmp = __attrs_140240906774608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240917090576 = _static_140241087907024('path', u'view/contents_table', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/contents_table' (18:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616ac3d0> -> __condition
                __expression = __cache_140240917090576

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n      ')
                else:
                    __content = __cache_140240917090576
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c61738cd0> name=None at 7f8c617388d0> -> __attrs_140240907111440
                __attrs_140240907111440 = _static_140240907111632

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-below-content-table">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907109136
                __default_140240907109136 = _DEFAULT_MARKER

                # <Value u'provider:senaite.belowlistingtable' (20:67)> -> __cache_140240906773904
                __token = 876
                try:
                    __zt_tmp = __attrs_140240907111440
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906773904 = _static_140241087907024('provider', u'senaite.belowlistingtable', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.belowlistingtable' (20:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e64d0> -> __condition
                __expression = __cache_140240906773904

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240906773904
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'context/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140240906139536
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'context/main_template/macros/master', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240935300224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240935300224
            __i18n_domain = __previous_i18n_domain_140240907419024
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }