# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/skins/senaite_templates/prefs_main_template.pt'

__tokens = {250: (u"python:request.set('disable_border',1)", 6, 39), 335: (u" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 45), 468: (u'n controlPanel/maySeeSomeConfigle', 8, 47), 554: (u"ne python:request.set('disable_plone.leftcolumn',", 9, 49), 656: (u"two python:request.set('disable_plone.rightcolumn'", 10, 48), 895: (u'here/portlet_prefs/macros/portlet', 16, 32), 895: (u'here/portlet_prefs/macros/portlet', 16, 32), 1351: (u'nothing', 26, 80), 1178: (u'context/@@main_template/macros/content', 24, 40), 1178: (u'context/@@main_template/macros/content', 24, 40), 85: (u'context/@@main_template/macros/master', 2, 30), 85: (u'context/@@main_template/macros/master', 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574442558096 = {}
_static_140574270567056 = u'content'
_static_140574270165456 = u'master'
_static_140574269059664 = u'portlet'
_static_140574397981968 = __compile_zt_expr

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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_prefs_configlet_main = econtext[u'__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_column_two_slot = econtext[u'__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_top_slot = econtext[u'__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_prefs_configlet_wrapper = econtext[u'__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_prefs_configlet_content = econtext[u'__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270168784
            __attrs_140574270168784 = _static_140574442558096
            __previous_i18n_domain_140574270167504 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270235024
            __attrs_140574270235024 = _static_140574442558096
            __backup_macroname_140574265964736 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fd9ff7011d0> name=None at 7fd9ff701e50> -> __value
            __value = _static_140574270165456
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270236688
                __attrs_140574270236688 = _static_140574442558096
                __append(u'\n      ')
                if (__slot_top_slot is None):

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270237648
                    __attrs_140574270237648 = _static_140574442558096
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269061648
                    __attrs_140574269061648 = _static_140574442558096
                    __backup_dummy_140574270303184 = get('dummy', __marker)

                    # <Value u"python:request.set('disable_border',1)" (6:39)> -> __value
                    __token = 250
                    try:
                        __zt_tmp = __attrs_140574269061648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"request.set('disable_border',1)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_140574272160720 = get('controlPanel', __marker)

                    # <Value u"python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:45)> -> __value
                    __token = 335
                    try:
                        __zt_tmp = __attrs_140574269061648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_show_leftcolumn_140574272097488 = get('show_leftcolumn', __marker)

                    # <Value u'controlPanel/maySeeSomeConfiglets' (8:47)> -> __value
                    __token = 468
                    try:
                        __zt_tmp = __attrs_140574269061648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'controlPanel/maySeeSomeConfiglets', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['show_leftcolumn'] = __value
                    __backup_disable_column_one_140574270570192 = get('disable_column_one', __marker)

                    # <Value u"python:request.set('disable_plone.leftcolumn', 1)" (9:49)> -> __value
                    __token = 554
                    try:
                        __zt_tmp = __attrs_140574269061648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_140574272186256 = get('disable_column_two', __marker)

                    # <Value u"python:request.set('disable_plone.rightcolumn', 1)" (10:48)> -> __value
                    __token = 656
                    try:
                        __zt_tmp = __attrs_140574269061648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"request.set('disable_plone.rightcolumn', 1)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_140574272186256 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_140574272186256
                    if (__backup_disable_column_one_140574270570192 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_140574270570192
                    if (__backup_show_leftcolumn_140574272097488 is __marker):
                        del econtext['show_leftcolumn']
                    else:
                        econtext['show_leftcolumn'] = __backup_show_leftcolumn_140574272097488
                    if (__backup_controlPanel_140574272160720 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_140574272160720
                    if (__backup_dummy_140574270303184 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_140574270303184
                    __append(u'\n      ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_portlets_two_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270236112
                __attrs_140574270236112 = _static_140574442558096
                __append(u'\n      ')
                if (__slot_column_two_slot is None):

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269060752
                    __attrs_140574269060752 = _static_140574442558096
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269061200
                    __attrs_140574269061200 = _static_140574442558096
                    __backup_macroname_140574269051360 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7fd9ff5f3250> name=None at 7fd9ff5f3e10> -> __value
                    __value = _static_140574269059664
                    econtext['macroname'] = __value

                    # <Value u'here/portlet_prefs/macros/portlet' (16:32)> -> __macro
                    __token = 895
                    try:
                        __zt_tmp = __attrs_140574269061200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140574397981968('path', u'here/portlet_prefs/macros/portlet', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __token = 895
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140574269051360 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140574269051360
                    __append(u'\n      ')
                else:
                    __slot_column_two_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_portlets_two_slot'] = _deque((__fill_portlets_two_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269059344
                __attrs_140574269059344 = _static_140574442558096
                __append(u'\n      ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269062288
                    __attrs_140574269062288 = _static_140574442558096
                    __append(u'\n        ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270567760
                        __attrs_140574270567760 = _static_140574442558096
                        __append(u'\n\n          ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270569360
                        __attrs_140574270569360 = _static_140574442558096
                        __backup_macroname_140574269052000 = get('macroname', __marker)

                        # <Static value=<_ast.Str object at 0x7fd9ff763290> name=None at 7fd9ff763250> -> __value
                        __value = _static_140574270567056
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getitem = econtext.__getitem__
                            get = econtext.get

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284462032
                            __attrs_140574284462032 = _static_140574442558096
                            __append(u'\n              ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270393744
                                __attrs_140574270393744 = _static_140574442558096

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270391120
                                __default_140574270391120 = _DEFAULT_MARKER

                                # <Value u'nothing' (26:80)> -> __cache_140574270390928
                                __token = 1351
                                try:
                                    __zt_tmp = __attrs_140574270393744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574270390928 = _static_140574397981968('path', u'nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'nothing' (26:80)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff738450> -> __condition
                                __expression = __cache_140574270390928

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                Page body text\n              ')
                                else:
                                    __content = __cache_140574270390928
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append(u'\n            ')
                        _slots = econtext[u'__slot_main'] = _deque((__fill_main, ))

                        # <Value u'context/@@main_template/macros/content' (24:40)> -> __macro
                        __token = 1178
                        try:
                            __zt_tmp = __attrs_140574270569360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140574397981968('path', u'context/@@main_template/macros/content', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __token = 1178
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140574269052000 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140574269052000
                        __append(u'\n\n        ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append(u'\n      ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            # <Value u'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_140574270235024
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140574397981968('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140574265964736 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140574265964736
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140574270167504
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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_master': render_master, 'render': render, }