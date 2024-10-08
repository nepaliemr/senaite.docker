# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/membertools.pt'

__tokens = {95: (u'here/@@plone_context_state/is_toolbar_visible', 3, 33), 165: (u' view/anonymou', 4, 23), 203: (u'python:not isAnon and not toolbar_visible', 5, 20), 413: (u'python:view.user_actions and not view.anonymous', 10, 21), 573: (u'view/homelink_url', 13, 30), 621: (u'view/user_name', 14, 28), 806: (u'view/user_actions', 18, 33), 858: (u'string:membertools-${action/id}', 19, 33), 955: (u'action/href', 21, 38), 1007: (u' action/link_target|nothin', 22, 39), 1066: (u'action/title', 23, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574270467792 = {u'data-toggle': u'dropdown', u'href': u'view/homelink_url', u'id': u'user-name', u'class': u'dropdown-toggle', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574270453648 = {u'href': u'', u'target': u'action/link_target|nothing', }
_static_140574270464720 = {u'class': u'dropdown pull-right', u'id': u'portal-membertools', }
_static_140574270454416 = {u'id': u'string:membertools-${action/id}', }
_static_140574442558096 = {}
_static_140574270565136 = {u'id': u'portal-membertools-wrapper', }
_static_140574270450128 = {u'aria-labelledby': u'dropdownMenu', u'role': u'menu', u'class': u'dropdown-menu', }
_static_140574270451536 = {u'class': u'caret', }
_static_140574397981968 = __compile_zt_expr
_static_140574270566032 = {u'class': u'hiddenStructure', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff762b10> name=None at 7fd9ff762450> -> __attrs_140574270565072
            __attrs_140574270565072 = _static_140574270565136
            __backup_toolbar_visible_140574284339408 = get('toolbar_visible', __marker)

            # <Value u'here/@@plone_context_state/is_toolbar_visible' (3:33)> -> __value
            __token = 95
            try:
                __zt_tmp = __attrs_140574270565072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'here/@@plone_context_state/is_toolbar_visible', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['toolbar_visible'] = __value
            __backup_isAnon_140574257222864 = get('isAnon', __marker)

            # <Value u'view/anonymous' (4:23)> -> __value
            __token = 165
            try:
                __zt_tmp = __attrs_140574270565072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/anonymous', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isAnon'] = __value

            # <Value u'python:not isAnon and not toolbar_visible' (5:20)> -> __condition
            __token = 203
            try:
                __zt_tmp = __attrs_140574270565072
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'not isAnon and not toolbar_visible', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270563984 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-membertools-wrapper">\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff762e90> name=None at 7fd9ff762bd0> -> __attrs_140574270562896
                __attrs_140574270562896 = _static_140574270566032

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="hiddenStructure">')
                __stream_140574270564752 = []
                __append_140574270564752 = __stream_140574270564752.append
                __append_140574270564752(u'Member tools')
                __msgid_140574270564752 = __re_whitespace(''.join(__stream_140574270564752)).strip()
                if u'heading_member_tools':
                    __append(translate(u'heading_member_tools', mapping=None, default=__msgid_140574270564752, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff74a2d0> name=None at 7fd9ff74a590> -> __attrs_140574270465360
                __attrs_140574270465360 = _static_140574270464720

                # <Value u'python:view.user_actions and not view.anonymous' (10:21)> -> __condition
                __token = 413
                try:
                    __zt_tmp = __attrs_140574270465360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'view.user_actions and not view.anonymous', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="dropdown pull-right" id="portal-membertools">\n      ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff74aed0> name=None at 7fd9ff4d5550> -> __attrs_140574270448528
                    __attrs_140574270448528 = _static_140574270467792

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a id="user-name" class="dropdown-toggle" data-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270465104
                    __default_140574270465104 = _DEFAULT_MARKER

                    # <Substitution u'view/homelink_url' (13:30)> -> __attr_href
                    __token = 573
                    try:
                        __zt_tmp = __attrs_140574270448528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'view/homelink_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>\n         ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270450256
                    __attrs_140574270450256 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270451280
                    __default_140574270451280 = _DEFAULT_MARKER

                    # <Value u'view/user_name' (14:28)> -> __cache_140574270449232
                    __token = 621
                    try:
                        __zt_tmp = __attrs_140574270450256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574270449232 = _static_140574397981968('path', u'view/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/user_name' (14:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff746c90> -> __condition
                    __expression = __cache_140574270449232

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>John</span>')
                    else:
                        __content = __cache_140574270449232
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n         ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff746f50> name=None at 7fd9ff746e10> -> __attrs_140574270451088
                    __attrs_140574270451088 = _static_140574270451536

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="caret"></span>\n      </a>\n      ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff7469d0> name=None at 7fd9ff746910> -> __attrs_140574270454608
                    __attrs_140574270454608 = _static_140574270450128

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff747a90> name=None at 7fd9ff747f10> -> __attrs_140574270452496
                    __attrs_140574270452496 = _static_140574270454416
                    __backup_action_140574257223760 = get('action', __marker)

                    # <Value u'view/user_actions' (18:33)> -> __iterator
                    __token = 806
                    try:
                        __zt_tmp = __attrs_140574270452496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'view/user_actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574270454480, ) = getitem('repeat')(u'action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270451920
                        __default_140574270451920 = _DEFAULT_MARKER

                        # <Substitution u'string:membertools-${action/id}' (19:33)> -> __attr_id
                        __token = 858
                        try:
                            __zt_tmp = __attrs_140574270452496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140574397981968('string', u'membertools-${action/id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>\n              ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff747790> name=None at 7fd9ff747610> -> __attrs_140574284372112
                        __attrs_140574284372112 = _static_140574270453648

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284371536
                        __default_140574284371536 = _DEFAULT_MARKER

                        # <Substitution u'action/href' (21:38)> -> __attr_href
                        __token = 955
                        try:
                            __zt_tmp = __attrs_140574284372112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140574397981968('path', u'action/href', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284372176
                        __default_140574284372176 = _DEFAULT_MARKER

                        # <Substitution u'action/link_target|nothing' (22:39)> -> __attr_target
                        __token = 1007
                        try:
                            __zt_tmp = __attrs_140574284372112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_140574397981968('path', u'action/link_target|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((u' target="%s"' % __attr_target))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270452880
                        __default_140574270452880 = _DEFAULT_MARKER

                        # <Value u'action/title' (23:30)> -> __cache_140574270452112
                        __token = 1066
                        try:
                            __zt_tmp = __attrs_140574284372112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270452112 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'action/title' (23:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff747890> -> __condition
                        __expression = __cache_140574270452112

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                  action title\n              ')
                        else:
                            __content = __cache_140574270452112
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</a>\n          </li>')
                        ____index_140574270454480 -= 1
                        if (____index_140574270454480 > 0):
                            __append('\n          ')
                    if (__backup_action_140574257223760 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140574257223760
                    __append(u'\n      </ul>\n  </div>')
                __append(u'\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140574270563984
            if (__backup_isAnon_140574257222864 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140574257222864
            if (__backup_toolbar_visible_140574284339408 is __marker):
                del econtext['toolbar_visible']
            else:
                econtext['toolbar_visible'] = __backup_toolbar_visible_140574284339408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }