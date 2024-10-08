# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/contentviews.pt'

__tokens = {40: (u'context/@@plone', 1, 40), 91: (u'ploneview/showToolbar', 2, 33), 183: (u'view/tabSet1', 5, 29), 231: (u'python: view.menu_template(actions=actions)', 6, 32), 324: (u'view/tabSet2', 9, 29), 372: (u'python: view.menu_template(actions=actions)', 10, 32), 530: (u'provider:plone.contentmenu', 15, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257313872
            __attrs_140574257313872 = _static_140574442558096
            __backup_ploneview_140574275635088 = get('ploneview', __marker)

            # <Value u'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140574257313872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@plone', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value u'ploneview/showToolbar' (2:33)> -> __condition
            __token = 91
            try:
                __zt_tmp = __attrs_140574257313872
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'ploneview/showToolbar', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574257315152 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268052944
                __attrs_140574268052944 = _static_140574442558096
                __backup_actions_140574257312592 = get('actions', __marker)

                # <Value u'view/tabSet1' (5:29)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_140574268052944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/tabSet1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267988944
                __attrs_140574267988944 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257192336
                __default_140574257192336 = _DEFAULT_MARKER

                # <Value u'python: view.menu_template(actions=actions)' (6:32)> -> __cache_140574257190224
                __token = 231
                try:
                    __zt_tmp = __attrs_140574267988944
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574257190224 = _static_140574397981968('python', u' view.menu_template(actions=actions)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'python: view.menu_template(actions=actions)' (6:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa10d0> -> __condition
                __expression = __cache_140574257190224

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140574257190224
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
                if (__backup_actions_140574257312592 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140574257312592
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268051728
                __attrs_140574268051728 = _static_140574442558096
                __backup_actions_140574268053008 = get('actions', __marker)

                # <Value u'view/tabSet2' (9:29)> -> __value
                __token = 324
                try:
                    __zt_tmp = __attrs_140574268051728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/tabSet2', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267986704
                __attrs_140574267986704 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267987600
                __default_140574267987600 = _DEFAULT_MARKER

                # <Value u'python: view.menu_template(actions=actions)' (10:32)> -> __cache_140574267988624
                __token = 372
                try:
                    __zt_tmp = __attrs_140574267986704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267988624 = _static_140574397981968('python', u' view.menu_template(actions=actions)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'python: view.menu_template(actions=actions)' (10:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ed650> -> __condition
                __expression = __cache_140574267988624

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140574267988624
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
                if (__backup_actions_140574268053008 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140574268053008
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267989136
                __attrs_140574267989136 = _static_140574442558096
                __append(u'\n    <!-- Workflow, Display, Portlets -->\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267989904
                __attrs_140574267989904 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267987408
                __default_140574267987408 = _DEFAULT_MARKER

                # <Value u'provider:plone.contentmenu' (15:32)> -> __cache_140574267988880
                __token = 530
                try:
                    __zt_tmp = __attrs_140574267989904
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267988880 = _static_140574397981968('provider', u'plone.contentmenu', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:plone.contentmenu' (15:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ed8d0> -> __condition
                __expression = __cache_140574267988880

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140574267988880
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  \n\n')
                __i18n_domain = __previous_i18n_domain_140574257315152
            if (__backup_ploneview_140574275635088 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140574275635088
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }