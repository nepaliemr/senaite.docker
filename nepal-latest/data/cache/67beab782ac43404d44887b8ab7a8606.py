# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/dexterity/templates/container.pt'

__tokens = {469: (u'view/widgets/values|nothing', 13, 34), 535: (u"python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", 14, 36), 678: (u'widget/@@ploneform-render-widget', 15, 47), 795: (u'view/groups|nothing', 19, 36), 853: (u"python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", 20, 37), 962: (u'group/label', 21, 31), 1018: (u'group/widgets/values', 22, 40), 1088: (u'widget/@@ploneform-render-widget', 23, 47), 1260: (u'python:False', 28, 53), 1383: (u'nocall:context/folder_listing', 30, 34), 1427: (u' view/macros/listing|view/index/macros/listin', 30, 78), 1516: (u'listing_macro', 31, 40), 1516: (u'listing_macro', 31, 40), 261: (u'context/@@main_template/macros/master', 6, 23), 261: (u'context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240750204752 = {u'id': u'folder-listing', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240612230224 = u'master'
_static_140241133802128 = {}
_static_140240766772496 = {u'id': u"python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", }
_static_140240759775056 = u'listing_macro'

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240604787408
            __attrs_140240604787408 = _static_140241133802128
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240766772560
            __attrs_140240766772560 = _static_140241133802128
            __backup_widget_140240767224784 = get('widget', __marker)

            # <Value u'view/widgets/values|nothing' (13:34)> -> __iterator
            __token = 469
            try:
                __zt_tmp = __attrs_140240766772560
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/widgets/values|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240766773648, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240764557072
                __attrs_140240764557072 = _static_140241133802128

                # <Value u"python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)" (14:36)> -> __condition
                __token = 535
                try:
                    __zt_tmp = __attrs_140240764557072
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u"widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240766773968
                    __attrs_140240766773968 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766773008
                    __default_140240766773008 = _DEFAULT_MARKER

                    # <Value u'widget/@@ploneform-render-widget' (15:47)> -> __cache_140240766772624
                    __token = 678
                    try:
                        __zt_tmp = __attrs_140240766773968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240766772624 = _static_140241087907024('path', u'widget/@@ploneform-render-widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/@@ploneform-render-widget' (15:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c59162810> -> __condition
                    __expression = __cache_140240766772624

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240766772624
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n          ')
                __append(u'\n        ')
                ____index_140240766773648 -= 1
                if (____index_140240766773648 > 0):
                    __append('')
            if (__backup_widget_140240767224784 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240767224784
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c59162510> name=None at 7f8c59162ed0> -> __attrs_140240766773456
            __attrs_140240766773456 = _static_140240766772496
            __backup_group_140240748635280 = get('group', __marker)

            # <Value u'view/groups|nothing' (19:36)> -> __iterator
            __token = 795
            try:
                __zt_tmp = __attrs_140240766773456
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/groups|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240766771856, ) = getitem('repeat')(u'group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append(u'<fieldset')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766775056
                __default_140240766775056 = _DEFAULT_MARKER

                # <Substitution u"python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')" (20:37)> -> __attr_id
                __token = 853
                try:
                    __zt_tmp = __attrs_140240766773456
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140241087907024('python', u"''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240766774800
                __attrs_140240766774800 = _static_140241133802128

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append(u'<legend>')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766772688
                __default_140240766772688 = _DEFAULT_MARKER

                # <Value u'group/label' (21:31)> -> __cache_140240766773712
                __token = 962
                try:
                    __zt_tmp = __attrs_140240766774800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240766773712 = _static_140241087907024('path', u'group/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'group/label' (21:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c591620d0> -> __condition
                __expression = __cache_140240766773712

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240766773712
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</legend>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240750206864
                __attrs_140240750206864 = _static_140241133802128
                __backup_widget_140240767334096 = get('widget', __marker)

                # <Value u'group/widgets/values' (22:40)> -> __iterator
                __token = 1018
                try:
                    __zt_tmp = __attrs_140240750206864
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'group/widgets/values', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240750205456, ) = getitem('repeat')(u'widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240750203792
                    __attrs_140240750203792 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240750203472
                    __default_140240750203472 = _DEFAULT_MARKER

                    # <Value u'widget/@@ploneform-render-widget' (23:47)> -> __cache_140240750203344
                    __token = 1088
                    try:
                        __zt_tmp = __attrs_140240750203792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240750203344 = _static_140241087907024('path', u'widget/@@ploneform-render-widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/@@ploneform-render-widget' (23:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58195450> -> __condition
                    __expression = __cache_140240750203344

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240750203344
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n          ')
                    ____index_140240750205456 -= 1
                    if (____index_140240750205456 > 0):
                        __append('')
                if (__backup_widget_140240767334096 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_140240767334096
                __append(u'\n        </fieldset>')
                ____index_140240766771856 -= 1
                if (____index_140240766771856 > 0):
                    __append('\n        ')
            if (__backup_group_140240748635280 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140240748635280
            __append(u'\n\n        <!-- hide contents listing -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c58195750> name=None at 7f8c581958d0> -> __attrs_140240750204560
            __attrs_140240750204560 = _static_140240750204752

            # <Value u'python:False' (28:53)> -> __condition
            __token = 1260
            try:
                __zt_tmp = __attrs_140240750204560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'False', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append(u'<fieldset id="folder-listing">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240750204624
                __attrs_140240750204624 = _static_140241133802128
                __previous_i18n_domain_140240750206032 = __i18n_domain
                __i18n_domain = u'plone'

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append(u'<legend>')
                __stream_140240750204816 = []
                __append_140240750204816 = __stream_140240750204816.append
                __append_140240750204816(u'Contents')
                __msgid_140240750204816 = __re_whitespace(''.join(__stream_140240750204816)).strip()
                if __msgid_140240750204816:
                    __append(translate(__msgid_140240750204816, mapping=None, default=__msgid_140240750204816, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</legend>')
                __i18n_domain = __previous_i18n_domain_140240750206032
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240759774544
                __attrs_140240759774544 = _static_140241133802128
                __backup_view_140240767223440 = get('view', __marker)

                # <Value u'nocall:context/folder_listing' (30:34)> -> __value
                __token = 1383
                try:
                    __zt_tmp = __attrs_140240759774544
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('nocall', u'context/folder_listing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['view'] = __value
                __backup_listing_macro_140240756360784 = get('listing_macro', __marker)

                # <Value u'view/macros/listing|view/index/macros/listing' (30:78)> -> __value
                __token = 1427
                try:
                    __zt_tmp = __attrs_140240759774544
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('path', u'view/macros/listing|view/index/macros/listing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['listing_macro'] = __value
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240759772112
                __attrs_140240759772112 = _static_140241133802128
                __backup_macroname_140240751966320 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f8c58ab5f50> name=None at 7f8c58ab5590> -> __value
                __value = _static_140240759775056
                econtext['macroname'] = __value

                # <Value u'listing_macro' (31:40)> -> __macro
                __token = 1516
                try:
                    __zt_tmp = __attrs_140240759772112
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140241087907024('path', u'listing_macro', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __token = 1516
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140240751966320 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140240751966320
                __append(u'\n          ')
                if (__backup_listing_macro_140240756360784 is __marker):
                    del econtext['listing_macro']
                else:
                    econtext['listing_macro'] = __backup_listing_macro_140240756360784
                if (__backup_view_140240767223440 is __marker):
                    del econtext['view']
                else:
                    econtext['view'] = __backup_view_140240767223440
                __append(u'\n        </fieldset>')
            __append(u'\n\n      ')
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240612230352
            __attrs_140240612230352 = _static_140241133802128
            __previous_i18n_domain_140240612230160 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140240752987024 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c4fe00450> name=None at 7f8c4fe00890> -> __value
            __value = _static_140240612230224
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240604787472
                __attrs_140240604787472 = _static_140241133802128
                __append(u'\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140240612230352
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240752987024 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240752987024
            __i18n_domain = __previous_i18n_domain_140240612230160
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_content_core': render_content_core, 'render': render, }