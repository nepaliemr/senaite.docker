# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/contentmenu/templates/contentmenu.pt'

__tokens = {68: (u'view/menu', 3, 15), 37: (u'view/available', 2, 13), 141: (u'menu', 6, 30), 337: (u'menuItem/submenu', 11, 28), 387: (u' not:menuItem/extra/hideChildren | not:submenu | nothin', 12, 32), 474: (u'r menuItem/extra/', 13, 29), 249: (u" python:has_dropdown and 'nav-item dropdown' or 'nav-item", 10, 29), 201: (u'menuItem/extra/id', 9, 27), 829: (u'menuItem/action', 21, 32), 878: (u' menuItem/extra/class | nothin', 22, 32), 942: (u's python:state_class and state_class or ', 23, 31), 597: (u'not:has_dropdown', 17, 24), 1009: (u'not:has_action', 24, 23), 645: (u'string:#${menuItem/extra/id}', 18, 30), 705: (u' menuItem/descriptio', 19, 30), 757: (u's string:label-${state_class} nav-li', 20, 29), 1099: (u'string:${menuItem/extra/class} tb-state', 27, 32), 1257: (u'menuItem/extra/stateTitle | nothing', 29, 25), 1172: (u"python:has_action and css_class or css_class + ' nav-link'", 28, 32), 1317: (u'menuItem/extra/stateTitle', 30, 23), 1516: (u'not:menuItem/extra/hideChildren | not:submenu | nothing', 38, 26), 1833: (u'not:menuItem/extra/stateTitle | nothing', 44, 29), 1901: (u'menuItem/title', 45, 27), 2175: (u'menuItem/extra/stateTitle | nothing', 53, 29), 2105: (u'string:${menuItem/extra/class} tb-state', 52, 36), 2239: (u'menuItem/extra/stateTitle', 54, 27), 2537: (u'submenu', 61, 41), 2406: (u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator} dropdown-item', 60, 39), 2960: (u'subMenuItem/action', 69, 45), 2680: (u'subMenuItem/action', 65, 35), 2735: (u' subMenuItem/descriptio', 66, 35), 2792: (u'd subMenuItem/extra/id | nothi', 67, 31), 2859: (u'ss string:${subMenuItem/extra/class|nothing} nav-l', 68, 33), 3041: (u'subMenuItem/title', 71, 35), 3344: (u'not:subMenuItem/action', 79, 29), 3212: (u'subMenuItem/extra/id | nothing', 77, 33), 3279: (u' subMenuItem/extra/class | nothin', 78, 35), 3462: (u'subMenuItem/title', 82, 39)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574268028880 = {u'class': u"python:has_action and css_class or css_class + ' nav-link'", }
_static_140574397982672 = __C2ZContextWrapper
_static_140574284366608 = {u'aria-haspopup': u'true', u'aria-expanded': u'false', u'id': u'navbarDropdown', u'href': u'#', u'role': u'button', u'data-toggle': u'dropdown', u'class': u'nav-link dropdown-toggle', }
_static_140574267914768 = {u'class': u'', }
_static_140574442558096 = {}
_static_140574267986320 = {u'class': u'string:${subMenuItem/extra/class|nothing} nav-link', u'href': u'#', u'id': u'subMenuItem/extra/id | nothing', u'aria-expanded': u'false', u'title': u'subMenuItem/description', }
_static_140574268029328 = {u'class': u'nav-item dropdown', u'aria-hidden': u'true', }
_static_140574268016336 = {u'class': u'nav-item', u'id': u'menuItem/extra/id', }
_static_140574267890640 = {u'class': u'', }
_static_140574397981968 = __compile_zt_expr
_static_140574267988816 = {u'class': u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator} dropdown-item', }
_static_140574267888528 = {u'class': u'dropdown-menu', }
_static_140574284333328 = {u'href': u'#', u'class': u'string:label-${state_class} nav-link', u'title': u'menuItem/description', }
_static_140574267932752 = {u'id': u'subMenuItem/extra/id | nothing', u'class': u'subMenuItem/extra/class | nothing', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257218064
            __attrs_140574257218064 = _static_140574442558096
            __backup_menu_140574257220944 = get('menu', __marker)

            # <Value u'view/menu' (3:15)> -> __value
            __token = 68
            try:
                __zt_tmp = __attrs_140574257218064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/menu', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['menu'] = __value

            # <Value u'view/available' (2:13)> -> __condition
            __token = 37
            try:
                __zt_tmp = __attrs_140574257218064
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'view/available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574257219024 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275635152
                __attrs_140574275635152 = _static_140574442558096
                __backup_menuItem_140574282109520 = get('menuItem', __marker)

                # <Value u'menu' (6:30)> -> __iterator
                __token = 141
                try:
                    __zt_tmp = __attrs_140574275635152
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'menu', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574268017040, ) = getitem('repeat')(u'menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append(u'\n\n    ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4f46d0> name=None at 7fd9ff4f4d10> -> __attrs_140574268017424
                    __attrs_140574268017424 = _static_140574268016336
                    __backup_submenu_140574284483344 = get('submenu', __marker)

                    # <Value u'menuItem/submenu' (11:28)> -> __value
                    __token = 337
                    try:
                        __zt_tmp = __attrs_140574268017424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'menuItem/submenu', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_has_dropdown_140574275637136 = get('has_dropdown', __marker)

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (12:32)> -> __value
                    __token = 387
                    try:
                        __zt_tmp = __attrs_140574268017424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['has_dropdown'] = __value
                    __backup_identifier_140574267903312 = get('identifier', __marker)

                    # <Value u'menuItem/extra/id' (13:29)> -> __value
                    __token = 474
                    try:
                        __zt_tmp = __attrs_140574268017424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'menuItem/extra/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['identifier'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268017680
                    __default_140574268017680 = _DEFAULT_MARKER

                    # <Substitution u"python:has_dropdown and 'nav-item dropdown' or 'nav-item'" (10:29)> -> __attr_class
                    __token = 249
                    try:
                        __zt_tmp = __attrs_140574268017424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('python', u"has_dropdown and 'nav-item dropdown' or 'nav-item'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'nav-item', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268016208
                    __default_140574268016208 = _DEFAULT_MARKER

                    # <Substitution u'menuItem/extra/id' (9:27)> -> __attr_id
                    __token = 201
                    try:
                        __zt_tmp = __attrs_140574268017424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140574397981968('path', u'menuItem/extra/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n      <!-- Menu Item -->\n      ')

                    # <Static value=<_ast.Dict object at 0x7fda00484110> name=None at 7fda00484b50> -> __attrs_140574284334800
                    __attrs_140574284334800 = _static_140574284333328
                    __backup_has_action_140574284461584 = get('has_action', __marker)

                    # <Value u'menuItem/action' (21:32)> -> __value
                    __token = 829
                    try:
                        __zt_tmp = __attrs_140574284334800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'menuItem/action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['has_action'] = __value
                    __backup_state_class_140574282112848 = get('state_class', __marker)

                    # <Value u'menuItem/extra/class | nothing' (22:32)> -> __value
                    __token = 878
                    try:
                        __zt_tmp = __attrs_140574284334800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'menuItem/extra/class | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_140574267884752 = get('state_class', __marker)

                    # <Value u"python:state_class and state_class or ''" (23:31)> -> __value
                    __token = 942
                    try:
                        __zt_tmp = __attrs_140574284334800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"state_class and state_class or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <Value u'not:has_dropdown' (17:24)> -> __condition
                    __token = 597
                    try:
                        __zt_tmp = __attrs_140574284334800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('not', u'has_dropdown', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <Negate value=<Value u'not:has_action' (24:23)> at 7fda00484050> -> __cache_140574284333136

                        # <Value u'not:has_action' (24:23)> -> __cache_140574284333136
                        __token = 1009
                        try:
                            __zt_tmp = __attrs_140574284334800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574284333136 = _static_140574397981968('not', u'has_action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __cache_140574284333136 = not __cache_140574284333136
                        __condition = __cache_140574284333136
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284333776
                            __default_140574284333776 = _DEFAULT_MARKER

                            # <Substitution u'string:#${menuItem/extra/id}' (18:30)> -> __attr_href
                            __token = 645
                            try:
                                __zt_tmp = __attrs_140574284334800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140574397981968('string', u'#${menuItem/extra/id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                            if (__attr_href is not None):
                                __append((u' href="%s"' % __attr_href))

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284336720
                            __default_140574284336720 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<Substitution u'menuItem/description' (19:30)> at 7fda00484cd0> -> __attr_title

                            # <Substitution u'menuItem/description' (19:30)> -> __attr_title
                            __token = 705
                            try:
                                __zt_tmp = __attrs_140574284334800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_title = _static_140574397981968('path', u'menuItem/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284335312
                            __default_140574284335312 = _DEFAULT_MARKER

                            # <Substitution u'string:label-${state_class} nav-link' (20:29)> -> __attr_class
                            __token = 757
                            try:
                                __zt_tmp = __attrs_140574284334800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('string', u'label-${state_class} nav-link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4f77d0> name=None at 7fd9ff4f7a50> -> __attrs_140574268030800
                        __attrs_140574268030800 = _static_140574268028880
                        __backup_css_class_140574257219984 = get('css_class', __marker)

                        # <Value u'string:${menuItem/extra/class} tb-state' (27:32)> -> __value
                        __token = 1099
                        try:
                            __zt_tmp = __attrs_140574268030800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('string', u'${menuItem/extra/class} tb-state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['css_class'] = __value

                        # <Value u'menuItem/extra/stateTitle | nothing' (29:25)> -> __condition
                        __token = 1257
                        try:
                            __zt_tmp = __attrs_140574268030800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268030224
                            __default_140574268030224 = _DEFAULT_MARKER

                            # <Substitution u"python:has_action and css_class or css_class + ' nav-link'" (28:32)> -> __attr_class
                            __token = 1172
                            try:
                                __zt_tmp = __attrs_140574268030800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('python', u"has_action and css_class or css_class + ' nav-link'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268030480
                            __default_140574268030480 = _DEFAULT_MARKER

                            # <Value u'menuItem/extra/stateTitle' (30:23)> -> __cache_140574268029648
                            __token = 1317
                            try:
                                __zt_tmp = __attrs_140574268030800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574268029648 = _static_140574397981968('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'menuItem/extra/stateTitle' (30:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f7950> -> __condition
                            __expression = __cache_140574268029648

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n          State title\n        ')
                            else:
                                __content = __cache_140574268029648
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>')
                        if (__backup_css_class_140574257219984 is __marker):
                            del econtext['css_class']
                        else:
                            econtext['css_class'] = __backup_css_class_140574257219984
                        __append(u'\n      ')
                        __condition = __cache_140574284333136
                        if __condition:
                            __append(u'</a>')
                    if (__backup_state_class_140574267884752 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140574267884752
                    if (__backup_state_class_140574282112848 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140574282112848
                    if (__backup_has_action_140574284461584 is __marker):
                        del econtext['has_action']
                    else:
                        econtext['has_action'] = __backup_has_action_140574284461584
                    __append(u'\n\n      <!-- dropdown menu -->\n      ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4f7990> name=None at 7fd9ff4f7610> -> __attrs_140574284368272
                    __attrs_140574284368272 = _static_140574268029328

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (38:26)> -> __condition
                    __token = 1516
                    try:
                        __zt_tmp = __attrs_140574284368272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="nav-item dropdown" aria-hidden="true">\n\n          ')

                        # <Static value=<_ast.Dict object at 0x7fda0048c310> name=None at 7fda0048c650> -> __attrs_140574267914000
                        __attrs_140574267914000 = _static_140574284366608

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4dba10> name=None at 7fd9ff4dbc10> -> __attrs_140574267913232
                        __attrs_140574267913232 = _static_140574267914768

                        # <Value u'not:menuItem/extra/stateTitle | nothing' (44:29)> -> __condition
                        __token = 1833
                        try:
                            __zt_tmp = __attrs_140574267913232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('not', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267913296
                            __default_140574267913296 = _DEFAULT_MARKER

                            # <Value u'menuItem/title' (45:27)> -> __cache_140574267914256
                            __token = 1901
                            try:
                                __zt_tmp = __attrs_140574267913232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574267914256 = _static_140574397981968('path', u'menuItem/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'menuItem/title' (45:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4db550> -> __condition
                            __expression = __cache_140574267914256

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n              Menu Title\n            ')
                            else:
                                __content = __cache_140574267914256
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>')
                        __append(u'\n            <!-- State Title -->\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d5bd0> name=None at 7fd9ff4d5dd0> -> __attrs_140574267891088
                        __attrs_140574267891088 = _static_140574267890640

                        # <Value u'menuItem/extra/stateTitle | nothing' (53:29)> -> __condition
                        __token = 2175
                        try:
                            __zt_tmp = __attrs_140574267891088
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267891472
                            __default_140574267891472 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/class} tb-state' (52:36)> -> __attr_class
                            __token = 2105
                            try:
                                __zt_tmp = __attrs_140574267891088
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('string', u'${menuItem/extra/class} tb-state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267888592
                            __default_140574267888592 = _DEFAULT_MARKER

                            # <Value u'menuItem/extra/stateTitle' (54:27)> -> __cache_140574267889872
                            __token = 2239
                            try:
                                __zt_tmp = __attrs_140574267891088
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574267889872 = _static_140574397981968('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'menuItem/extra/stateTitle' (54:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d5c90> -> __condition
                            __expression = __cache_140574267889872

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n              State title\n            ')
                            else:
                                __content = __cache_140574267889872
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>')
                        __append(u'\n          </a>\n\n          ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d5390> name=None at 7fd9ff4d5a50> -> __attrs_140574267987600
                        __attrs_140574267987600 = _static_140574267888528

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="dropdown-menu">\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4edb50> name=None at 7fd9ff4ed150> -> __attrs_140574267987216
                        __attrs_140574267987216 = _static_140574267988816
                        __backup_subMenuItem_140574267885008 = get('subMenuItem', __marker)

                        # <Value u'submenu' (61:41)> -> __iterator
                        __token = 2537
                        try:
                            __zt_tmp = __attrs_140574267987216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('path', u'submenu', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574267989456, ) = getitem('repeat')(u'subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267989520
                            __default_140574267989520 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator} dropdown-item' (60:39)> -> __attr_class
                            __token = 2406
                            try:
                                __zt_tmp = __attrs_140574267987216
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('string', u'${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator} dropdown-item', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>\n            ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff4ed190> name=None at 7fd9ff4edd50> -> __attrs_140574257141392
                            __attrs_140574257141392 = _static_140574267986320

                            # <Value u'subMenuItem/action' (69:45)> -> __condition
                            __token = 2960
                            try:
                                __zt_tmp = __attrs_140574257141392
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'subMenuItem/action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257141968
                                __default_140574257141968 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/action' (65:35)> -> __attr_href
                                __token = 2680
                                try:
                                    __zt_tmp = __attrs_140574257141392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140574397981968('path', u'subMenuItem/action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))
                                __append(u' aria-expanded="false"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257142224
                                __default_140574257142224 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution u'subMenuItem/description' (66:35)> at 7fd9fea95b90> -> __attr_title

                                # <Substitution u'subMenuItem/description' (66:35)> -> __attr_title
                                __token = 2735
                                try:
                                    __zt_tmp = __attrs_140574257141392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_140574397981968('path', u'subMenuItem/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_title is not None):
                                    __append((u' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257141456
                                __default_140574257141456 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (67:31)> -> __attr_id
                                __token = 2792
                                try:
                                    __zt_tmp = __attrs_140574257141392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140574397981968('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257139984
                                __default_140574257139984 = _DEFAULT_MARKER

                                # <Substitution u'string:${subMenuItem/extra/class|nothing} nav-link' (68:33)> -> __attr_class
                                __token = 2859
                                try:
                                    __zt_tmp = __attrs_140574257141392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140574397981968('string', u'${subMenuItem/extra/class|nothing} nav-link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>\n              ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267936144
                                __attrs_140574267936144 = _static_140574442558096

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267932880
                                __default_140574267932880 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (71:35)> -> __cache_140574267935632
                                __token = 3041
                                try:
                                    __zt_tmp = __attrs_140574267936144
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574267935632 = _static_140574397981968('path', u'subMenuItem/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (71:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4e0cd0> -> __condition
                                __expression = __cache_140574267935632

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                Title\n              ')
                                else:
                                    __content = __cache_140574267935632
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'\n            </a>')
                            __append(u'\n            ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff4e0050> name=None at 7fd9ff4e0e10> -> __attrs_140574267885392
                            __attrs_140574267885392 = _static_140574267932752

                            # <Value u'not:subMenuItem/action' (79:29)> -> __condition
                            __token = 3344
                            try:
                                __zt_tmp = __attrs_140574267885392
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u'subMenuItem/action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267935568
                                __default_140574267935568 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (77:33)> -> __attr_id
                                __token = 3212
                                try:
                                    __zt_tmp = __attrs_140574267885392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140574397981968('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267885712
                                __default_140574267885712 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/class | nothing' (78:35)> -> __attr_class
                                __token = 3279
                                try:
                                    __zt_tmp = __attrs_140574267885392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140574397981968('path', u'subMenuItem/extra/class | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>\n              ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267885584
                                __attrs_140574267885584 = _static_140574442558096

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267885328
                                __default_140574267885328 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (82:39)> -> __cache_140574267887248
                                __token = 3462
                                try:
                                    __zt_tmp = __attrs_140574267885584
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574267887248 = _static_140574397981968('path', u'subMenuItem/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (82:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d4250> -> __condition
                                __expression = __cache_140574267887248

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                Title\n              ')
                                else:
                                    __content = __cache_140574267887248
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n            </span>')
                            __append(u'\n          </div>')
                            ____index_140574267989456 -= 1
                            if (____index_140574267989456 > 0):
                                __append('\n            ')
                        if (__backup_subMenuItem_140574267885008 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_140574267885008
                        __append(u'\n        </div>\n      </div>')
                    __append(u'\n\n    </li>')
                    if (__backup_identifier_140574267903312 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_140574267903312
                    if (__backup_has_dropdown_140574275637136 is __marker):
                        del econtext['has_dropdown']
                    else:
                        econtext['has_dropdown'] = __backup_has_dropdown_140574275637136
                    if (__backup_submenu_140574284483344 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_140574284483344
                    __append(u'\n  ')
                    ____index_140574268017040 -= 1
                    if (____index_140574268017040 > 0):
                        __append('')
                if (__backup_menuItem_140574282109520 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_140574282109520
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140574257219024
            if (__backup_menu_140574257220944 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_140574257220944
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }