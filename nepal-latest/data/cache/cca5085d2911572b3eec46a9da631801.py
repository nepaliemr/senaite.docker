# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/listingactions.pt'

__tokens = {92: (u'python:view.get_context_actions()', 2, 26), 199: (u'action/url', 4, 28), 239: (u" python:'mx-2 btn btn-sm btn-light %s' % action.get('css_class', ''", 5, 28), 338: (u'action/icon|nothing', 6, 28), 385: (u'icon', 7, 26), 445: (u'icon', 9, 31), 478: (u'action/title', 10, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574270359376 = {u'class': u'd-inline-block align-middle', }
_static_140574270361296 = {u'href': u'action/url', u'class': u"python:'mx-2 btn btn-sm btn-light %s' % action.get('css_class', '')", }
_static_140574442558096 = {}
_static_140574270215376 = {u'class': u'listing-actions-viewlet d-inline-block align-middle', }
_static_140574284475856 = {u'src': u'icon', u'height': u'16', }
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

            # <Static value=<_ast.Dict object at 0x7fd9ff70d4d0> name=None at 7fd9ff70d890> -> __attrs_140574270360848
            __attrs_140574270360848 = _static_140574270215376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="listing-actions-viewlet d-inline-block align-middle">\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff730750> name=None at 7fd9ff7301d0> -> __attrs_140574270357712
            __attrs_140574270357712 = _static_140574270359376
            __backup_action_140574267988112 = get('action', __marker)

            # <Value u'python:view.get_context_actions()' (2:26)> -> __iterator
            __token = 92
            try:
                __zt_tmp = __attrs_140574270357712
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('python', u'view.get_context_actions()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574270359952, ) = getitem('repeat')(u'action', __iterator)
            econtext['action'] = None
            for __item in __iterator:
                econtext['action'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="d-inline-block align-middle">\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff730ed0> name=None at 7fd9ff7303d0> -> __attrs_140574284473616
                __attrs_140574284473616 = _static_140574270361296

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284475408
                __default_140574284475408 = _DEFAULT_MARKER

                # <Substitution u'action/url' (4:28)> -> __attr_href
                __token = 199
                try:
                    __zt_tmp = __attrs_140574284473616
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('path', u'action/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284473296
                __default_140574284473296 = _DEFAULT_MARKER

                # <Substitution u"python:'mx-2 btn btn-sm btn-light %s' % action.get('css_class', '')" (5:28)> -> __attr_class
                __token = 239
                try:
                    __zt_tmp = __attrs_140574284473616
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140574397981968('python', u"'mx-2 btn btn-sm btn-light %s' % action.get('css_class', '')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7fda004a6dd0> name=None at 7fda004a6c90> -> __attrs_140574267882320
                __attrs_140574267882320 = _static_140574284475856
                __backup_icon_140574266168336 = get('icon', __marker)

                # <Value u'action/icon|nothing' (6:28)> -> __value
                __token = 338
                try:
                    __zt_tmp = __attrs_140574267882320
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'action/icon|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['icon'] = __value

                # <Value u'icon' (7:26)> -> __condition
                __token = 385
                try:
                    __zt_tmp = __attrs_140574267882320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img height="16"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267882064
                    __default_140574267882064 = _DEFAULT_MARKER

                    # <Substitution u'icon' (9:31)> -> __attr_src
                    __token = 445
                    try:
                        __zt_tmp = __attrs_140574267882320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_140574397981968('path', u'icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((u' src="%s"' % __attr_src))
                    __append(u'/>')
                if (__backup_icon_140574266168336 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140574266168336
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267882512
                __attrs_140574267882512 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267882448
                __default_140574267882448 = _DEFAULT_MARKER

                # <Value u'action/title' (10:25)> -> __cache_140574267881808
                __token = 478
                try:
                    __zt_tmp = __attrs_140574267882512
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267881808 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'action/title' (10:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d3350> -> __condition
                __expression = __cache_140574267881808

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574267881808
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n    </a>\n  </div>')
                ____index_140574270359952 -= 1
                if (____index_140574270359952 > 0):
                    __append('\n  ')
            if (__backup_action_140574267988112 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_140574267988112
            __append(u'\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }