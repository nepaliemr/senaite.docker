# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/sections.pt'

__tokens = {193: (u'view/portal_tabs', 5, 26), 228: (u'portal_tabs', 6, 17), 559: (u'python:view.selected_portal_tab', 19, 33), 630: (u'view/portal_tabs', 21, 36), 711: (u"python:action['id'] == selected_tab", 23, 33), 775: (u'action/available|nothing', 24, 27), 875: (u'action/url', 26, 34), 921: (u" python:selected and 'active nav-link' or 'nav-link", 27, 34), 1008: (u'e action/description|action/tit', 28, 33), 1075: (u'action/title', 29, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574268029200 = {u'class': u'dropdown-menu dropdown-menu-right', }
_static_140574268063696 = {u'data-toggle': u'dropdown', u'href': u'#', u'class': u'nav-link dropdown-toggle', u'aria-expanded': u'false', u'aria-haspopup': u'true', }
_static_140574257190224 = {u'class': u'dropdown', }
_static_140574442558096 = {}
_static_140574270161744 = {u'href': u'#', u'class': u'nav-link', u'title': u'action/description|action/title', }
_static_140574281970384 = {u'class': u'fas fa-th', }
_static_140574281972112 = {u'class': u'nav-item', }
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267989712
            __attrs_140574267989712 = _static_140574442558096
            __backup_portal_tabs_140574284346384 = get('portal_tabs', __marker)

            # <Value u'view/portal_tabs' (5:26)> -> __value
            __token = 193
            try:
                __zt_tmp = __attrs_140574267989712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/portal_tabs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal_tabs'] = __value

            # <Value u'portal_tabs' (6:17)> -> __condition
            __token = 228
            try:
                __zt_tmp = __attrs_140574267989712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'portal_tabs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574267988944 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9feaa1550> name=None at 7fda07a59410> -> __attrs_140574268063312
                __attrs_140574268063312 = _static_140574257190224

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav class="dropdown">\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4fffd0> name=None at 7fd9ff4ff310> -> __attrs_140574268060816
                __attrs_140574268060816 = _static_140574268063696

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n      ')

                # <Static value=<_ast.Dict object at 0x7fda002432d0> name=None at 7fda00243950> -> __attrs_140574268030480
                __attrs_140574268030480 = _static_140574281970384

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-th"></i>\n    </a>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f7910> name=None at 7fd9ff4f7950> -> __attrs_140574281971600
                __attrs_140574281971600 = _static_140574268029200
                __backup_selected_tab_140574495067088 = get('selected_tab', __marker)

                # <Value u'python:view.selected_portal_tab' (19:33)> -> __value
                __token = 559
                try:
                    __zt_tmp = __attrs_140574281971600
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'view.selected_portal_tab', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['selected_tab'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="dropdown-menu dropdown-menu-right">\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574281971536
                __attrs_140574281971536 = _static_140574442558096
                __backup_action_140574284462096 = get('action', __marker)

                # <Value u'view/portal_tabs' (21:36)> -> __iterator
                __token = 630
                try:
                    __zt_tmp = __attrs_140574281971536
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'view/portal_tabs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574281972176, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda00243990> name=None at 7fda00243dd0> -> __attrs_140574493576016
                    __attrs_140574493576016 = _static_140574281972112
                    __backup_selected_140574267885008 = get('selected', __marker)

                    # <Value u"python:action['id'] == selected_tab" (23:33)> -> __value
                    __token = 711
                    try:
                        __zt_tmp = __attrs_140574493576016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"action['id'] == selected_tab", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <Value u'action/available|nothing' (24:27)> -> __condition
                    __token = 775
                    try:
                        __zt_tmp = __attrs_140574493576016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'action/available|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="nav-item">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff700350> name=None at 7fd9ff700210> -> __attrs_140574270162128
                        __attrs_140574270162128 = _static_140574270161744

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270162896
                        __default_140574270162896 = _DEFAULT_MARKER

                        # <Substitution u'action/url' (26:34)> -> __attr_href
                        __token = 875
                        try:
                            __zt_tmp = __attrs_140574270162128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140574397981968('path', u'action/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270163344
                        __default_140574270163344 = _DEFAULT_MARKER

                        # <Substitution u"python:selected and 'active nav-link' or 'nav-link'" (27:34)> -> __attr_class
                        __token = 921
                        try:
                            __zt_tmp = __attrs_140574270162128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140574397981968('python', u"selected and 'active nav-link' or 'nav-link'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'nav-link', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270164816
                        __default_140574270164816 = _DEFAULT_MARKER

                        # <Substitution u'action/description|action/title' (28:33)> -> __attr_title
                        __token = 1008
                        try:
                            __zt_tmp = __attrs_140574270162128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140574397981968('path', u'action/description|action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284368912
                        __attrs_140574284368912 = _static_140574442558096

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284368464
                        __default_140574284368464 = _DEFAULT_MARKER

                        # <Value u'action/title' (29:31)> -> __cache_140574270164944
                        __token = 1075
                        try:
                            __zt_tmp = __attrs_140574284368912
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270164944 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'action/title' (29:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda0048ce10> -> __condition
                        __expression = __cache_140574270164944

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574270164944
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n          </a>\n        </li>')
                    if (__backup_selected_140574267885008 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140574267885008
                    __append(u'\n      ')
                    ____index_140574281972176 -= 1
                    if (____index_140574281972176 > 0):
                        __append('')
                if (__backup_action_140574284462096 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140574284462096
                __append(u'\n    </ul>')
                if (__backup_selected_tab_140574495067088 is __marker):
                    del econtext['selected_tab']
                else:
                    econtext['selected_tab'] = __backup_selected_tab_140574495067088
                __append(u'\n  </nav>\n\n')
                __i18n_domain = __previous_i18n_domain_140574267988944
            if (__backup_portal_tabs_140574284346384 is __marker):
                del econtext['portal_tabs']
            else:
                econtext['portal_tabs'] = __backup_portal_tabs_140574284346384
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }