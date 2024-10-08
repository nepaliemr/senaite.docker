# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.listing/src/senaite/app/listing/templates/listing.pt'

__tokens = {428: (u'provider:senaite.listingtabletitle', 10, 67), 632: (u'provider:senaite.listingtabledescription', 14, 73), 828: (u'provider:senaite.abovelistingtable', 18, 67), 942: (u'view/contents_table', 20, 34), 1044: (u'provider:senaite.belowlistingtable', 22, 67), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574275642640 = {u'id': u'folderlisting-main-table', }
_static_140574275633552 = {u'id': u'viewlet-listing-table-title', }
_static_140574275597712 = u'master'
_static_140574442558096 = {}
_static_140574275635216 = {u'id': u'viewlet-listing-table-description', }
_static_140574275644176 = {u'id': u'viewlet-below-content-table', }
_static_140574397981968 = __compile_zt_expr
_static_140574275637072 = {u'id': u'viewlet-above-listing-table', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275597840
            __attrs_140574275597840 = _static_140574442558096
            __previous_i18n_domain_140574275597968 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140574272136768 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fd9ffc2f590> name=None at 7fd9ffc2f5d0> -> __value
            __value = _static_140574275597712
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275599632
                __attrs_140574275599632 = _static_140574442558096
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc38190> name=None at 7fd9ffc38150> -> __attrs_140574275634064
                __attrs_140574275634064 = _static_140574275633552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-listing-table-title">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275633360
                __default_140574275633360 = _DEFAULT_MARKER

                # <Value u'provider:senaite.listingtabletitle' (10:67)> -> __cache_140574275600272
                __token = 428
                try:
                    __zt_tmp = __attrs_140574275634064
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574275600272 = _static_140574397981968('provider', u'senaite.listingtabletitle', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.listingtabletitle' (10:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda00047790> -> __condition
                __expression = __cache_140574275600272

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574275600272
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n    ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275599056
                __attrs_140574275599056 = _static_140574442558096
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc38810> name=None at 7fd9ffc387d0> -> __attrs_140574275635856
                __attrs_140574275635856 = _static_140574275635216

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-listing-table-description">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275635024
                __default_140574275635024 = _DEFAULT_MARKER

                # <Value u'provider:senaite.listingtabledescription' (14:73)> -> __cache_140574275634704
                __token = 632
                try:
                    __zt_tmp = __attrs_140574275635856
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574275634704 = _static_140574397981968('provider', u'senaite.listingtabledescription', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.listingtabledescription' (14:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc38690> -> __condition
                __expression = __cache_140574275634704

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574275634704
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n    ')
            _slots = econtext[u'__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275635920
                __attrs_140574275635920 = _static_140574442558096
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc38f50> name=None at 7fd9ffc38f10> -> __attrs_140574275641872
                __attrs_140574275641872 = _static_140574275637072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-above-listing-table">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275636880
                __default_140574275636880 = _DEFAULT_MARKER

                # <Value u'provider:senaite.abovelistingtable' (18:67)> -> __cache_140574275636560
                __token = 828
                try:
                    __zt_tmp = __attrs_140574275641872
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574275636560 = _static_140574397981968('provider', u'senaite.abovelistingtable', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.abovelistingtable' (18:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc38dd0> -> __condition
                __expression = __cache_140574275636560

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574275636560
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc3a510> name=None at 7fd9ffc3a4d0> -> __attrs_140574275643280
                __attrs_140574275643280 = _static_140574275642640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="folderlisting-main-table">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275642448
                __default_140574275642448 = _DEFAULT_MARKER

                # <Value u'view/contents_table' (20:34)> -> __cache_140574275642128
                __token = 942
                try:
                    __zt_tmp = __attrs_140574275643280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574275642128 = _static_140574397981968('path', u'view/contents_table', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/contents_table' (20:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc3a390> -> __condition
                __expression = __cache_140574275642128

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n      ')
                else:
                    __content = __cache_140574275642128
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc3ab10> name=None at 7fd9ffc3aad0> -> __attrs_140574275644816
                __attrs_140574275644816 = _static_140574275644176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="viewlet-below-content-table">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275643984
                __default_140574275643984 = _DEFAULT_MARKER

                # <Value u'provider:senaite.belowlistingtable' (22:67)> -> __cache_140574275643664
                __token = 1044
                try:
                    __zt_tmp = __attrs_140574275644816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574275643664 = _static_140574397981968('provider', u'senaite.belowlistingtable', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.belowlistingtable' (22:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc3a990> -> __condition
                __expression = __cache_140574275643664

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574275643664
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140574275597840
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140574397981968('path', u'here/main_template/macros/master', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140574272136768 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140574272136768
            __i18n_domain = __previous_i18n_domain_140574275597968
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }