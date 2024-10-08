# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/menu.pt'

__tokens = {40: (u'context/@@plone', 1, 40), 91: (u'ploneview/showToolbar', 2, 33), 195: (u'options/actions', 5, 34), 269: (u'action/id', 8, 29), 308: (u' python:view.is_action_selected(action', 9, 28), 377: (u'string:contentview-${action/id}', 10, 27), 439: (u" python:selected and 'active nav-item' or 'nav-item", 11, 29), 563: (u'action/url', 15, 32), 608: (u' action/link_target|nothin', 16, 33), 668: (u's string:${action/cssClass} nav-li', 17, 31), 737: (u'action/title', 18, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574284364752 = {u'id': u'string:contentview-${action/id}', u'class': u"python:selected and 'active nav-item' or 'nav-item'", }
_static_140574284362448 = {u'href': u'#', u'target': u'action/link_target|nothing', u'class': u'string:${action/cssClass} nav-link', }
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267894928
            __attrs_140574267894928 = _static_140574442558096
            __backup_ploneview_140574284347920 = get('ploneview', __marker)

            # <Value u'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140574267894928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@plone', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value u'ploneview/showToolbar' (2:33)> -> __condition
            __token = 91
            try:
                __zt_tmp = __attrs_140574267894928
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'ploneview/showToolbar', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574267892496 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267892432
                __attrs_140574267892432 = _static_140574442558096
                __backup_action_140574284347856 = get('action', __marker)

                # <Value u'options/actions' (5:34)> -> __iterator
                __token = 195
                try:
                    __zt_tmp = __attrs_140574267892432
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'options/actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574267892688, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n\n    <!-- Contentviews -->\n    ')

                    # <Static value=<_ast.Dict object at 0x7fda0048bbd0> name=None at 7fda0048b690> -> __attrs_140574284364880
                    __attrs_140574284364880 = _static_140574284364752
                    __backup_actionid_140574284345936 = get('actionid', __marker)

                    # <Value u'action/id' (8:29)> -> __value
                    __token = 269
                    try:
                        __zt_tmp = __attrs_140574284364880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'action/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['actionid'] = __value
                    __backup_selected_140574257142096 = get('selected', __marker)

                    # <Value u'python:view.is_action_selected(action)' (9:28)> -> __value
                    __token = 308
                    try:
                        __zt_tmp = __attrs_140574284364880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u'view.is_action_selected(action)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284365648
                    __default_140574284365648 = _DEFAULT_MARKER

                    # <Substitution u'string:contentview-${action/id}' (10:27)> -> __attr_id
                    __token = 377
                    try:
                        __zt_tmp = __attrs_140574284364880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140574397981968('string', u'contentview-${action/id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284361808
                    __default_140574284361808 = _DEFAULT_MARKER

                    # <Substitution u"python:selected and 'active nav-item' or 'nav-item'" (11:29)> -> __attr_class
                    __token = 439
                    try:
                        __zt_tmp = __attrs_140574284364880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('python', u"selected and 'active nav-item' or 'nav-item'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284362256
                    __attrs_140574284362256 = _static_140574442558096
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda0048b2d0> name=None at 7fda0048b950> -> __attrs_140574267987664
                    __attrs_140574267987664 = _static_140574284362448

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284363280
                    __default_140574284363280 = _DEFAULT_MARKER

                    # <Substitution u'action/url' (15:32)> -> __attr_href
                    __token = 563
                    try:
                        __zt_tmp = __attrs_140574267987664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'action/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284364176
                    __default_140574284364176 = _DEFAULT_MARKER

                    # <Substitution u'action/link_target|nothing' (16:33)> -> __attr_target
                    __token = 608
                    try:
                        __zt_tmp = __attrs_140574267987664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140574397981968('path', u'action/link_target|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((u' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267986960
                    __default_140574267986960 = _DEFAULT_MARKER

                    # <Substitution u'string:${action/cssClass} nav-link' (17:31)> -> __attr_class
                    __token = 668
                    try:
                        __zt_tmp = __attrs_140574267987664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'${action/cssClass} nav-link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267988816
                    __attrs_140574267988816 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267989520
                    __default_140574267989520 = _DEFAULT_MARKER

                    # <Value u'action/title' (18:29)> -> __cache_140574267986000
                    __token = 737
                    try:
                        __zt_tmp = __attrs_140574267988816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267986000 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/title' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ed910> -> __condition
                    __expression = __cache_140574267986000

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'View name')
                    else:
                        __content = __cache_140574267986000
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n        </a>\n      \n    </li>')
                    if (__backup_selected_140574257142096 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140574257142096
                    if (__backup_actionid_140574284345936 is __marker):
                        del econtext['actionid']
                    else:
                        econtext['actionid'] = __backup_actionid_140574284345936
                    __append(u'\n\n  ')
                    ____index_140574267892688 -= 1
                    if (____index_140574267892688 > 0):
                        __append('')
                if (__backup_action_140574284347856 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140574284347856
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140574267892496
            if (__backup_ploneview_140574284347920 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140574284347920
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }