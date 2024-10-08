# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/portlets/templates/navigation_recurse.pt'

__tokens = {347: (u'children', 9, 30), 396: (u'node/show_children', 10, 38), 453: (u' node/childre', 11, 37), 505: (u'  python:len(children)', 12, 36), 566: (u'   node/get', 13, 35), 616: (u'url node/getRemot', 14, 34), 672: (u'url  node/useRemoteUrl | no', 15, 33), 738: (u'      nocall:nod', 16, 32), 793: (u'       python:bootstrapview.get_icon_fo', 17, 31), 871: (u'e       node/por', 18, 30), 926: (u'ent      node/cu', 19, 29), 981: (u'path      node/cur', 20, 28), 1038: (u"ass        python:is_current and ' ac", 21, 27), 1114: (u"xtr_class   python:is_in_path and ' exp", 22, 26), 1192: (u"folder_class python:show_children and ' fol", 23, 25), 1274: (u'rmalizeString nocall: context/plone_utils/n', 24, 24), 1483: (u'python:bottomLevel &lt;= 0 or level &lt;= botto', 26, 25), 1366: (u'string:nav-item${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', 25, 32), 1578: (u'string:senaite-state-${node/normalized_review_state}', 28, 38), 1674: (u" python:'senaite-contenttype-' + normalizeString(item_type", 29, 42), 1771: (u"s python:is_current and item_class + ' active' or item_cla", 30, 36), 1870: (u'python:use_remote_url and item_remote_url or item_url', 32, 34), 1959: (u' node/Titl', 33, 34), 2005: (u's string:$item_class${li_class}${li_extr_class}${li_folder_class} $item_type_class nav-li', 34, 33), 2173: (u'python: level==1', 36, 37), 2275: (u'item_icon', 38, 44), 2420: (u'node/Title', 42, 33), 2556: (u'python: level>1', 46, 41), 2704: (u'item_icon', 49, 46), 2858: (u'node/Title', 53, 35), 2997: (u'has_children', 58, 35), 3125: (u'python: len(children) > 0 and show_children and bottomLevel and level < bottomLevel or True', 60, 31), 3050: (u"python:'nav submenu nav-level-'+str(level)", 59, 38), 3262: (u"python:view.recurse(children=sorted(children, key=lambda n: n.get('Title')), level=level+1, bottomLevel=bottomLevel)", 61, 43), 26: (u'options/level|python:0', 1, 26), 78: (u' options/children | nothin', 2, 28), 137: (u'l options/bottomLevel | nothi', 3, 30), 201: (u'ew nocall:context/@@bootstrapv', 4, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574270175696 = {u'class': u"python:'nav submenu nav-level-'+str(level)", }
_static_140574284336592 = {u'class': u'text-truncate', }
_static_140574267904976 = {u'class': u'node-icon', }
_static_140574442558096 = {}
_static_140574267905232 = {u'class': u'node-title', }
_static_140574270173328 = {u'class': u'child-title', }
_static_140574268004432 = {u'class': u'string:nav-item${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', }
_static_140574266167056 = {u'href': u'python:use_remote_url and item_remote_url or item_url', u'class': u'string:$item_class${li_class}${li_extr_class}${li_folder_class} $item_type_class nav-link', u'title': u'node/Title', }
_static_140574397981968 = __compile_zt_expr
_static_140574284437328 = {u'class': u'child-icon', }

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

    def render_nav_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270225680
            __attrs_140574270225680 = _static_140574442558096
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268003856
            __attrs_140574268003856 = _static_140574442558096
            __backup_node_140574266162640 = get('node', __marker)

            # <Value u'children' (9:30)> -> __iterator
            __token = 347
            try:
                __zt_tmp = __attrs_140574268003856
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'children', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574268002832, ) = getitem('repeat')(u'node', __iterator)
            econtext['node'] = None
            for __item in __iterator:
                econtext['node'] = __item
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f1850> name=None at 7fd9ff4f1f10> -> __attrs_140574268004240
                __attrs_140574268004240 = _static_140574268004432
                __backup_show_children_140574284463952 = get('show_children', __marker)

                # <Value u'node/show_children' (10:38)> -> __value
                __token = 396
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/show_children', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['show_children'] = __value
                __backup_children_140574284358480 = get('children', __marker)

                # <Value u'node/children' (11:37)> -> __value
                __token = 453
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/children', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['children'] = __value
                __backup_has_children_140574284447312 = get('has_children', __marker)

                # <Value u'python:len(children)>0' (12:36)> -> __value
                __token = 505
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'len(children)>0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['has_children'] = __value
                __backup_item_url_140574270302480 = get('item_url', __marker)

                # <Value u'node/getURL' (13:35)> -> __value
                __token = 566
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/getURL', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_remote_url_140574284341008 = get('item_remote_url', __marker)

                # <Value u'node/getRemoteUrl' (14:34)> -> __value
                __token = 616
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/getRemoteUrl', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['item_remote_url'] = __value
                __backup_use_remote_url_140574270300240 = get('use_remote_url', __marker)

                # <Value u'node/useRemoteUrl | nothing' (15:33)> -> __value
                __token = 672
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/useRemoteUrl | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['use_remote_url'] = __value
                __backup_item_140574284437520 = get('item', __marker)

                # <Value u'nocall:node/item' (16:32)> -> __value
                __token = 738
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u'node/item', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['item'] = __value
                __backup_item_icon_140574284474192 = get('item_icon', __marker)

                # <Value u'python:bootstrapview.get_icon_for(item)' (17:31)> -> __value
                __token = 793
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'bootstrapview.get_icon_for(item)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['item_icon'] = __value
                __backup_item_type_140574281971984 = get('item_type', __marker)

                # <Value u'node/portal_type' (18:30)> -> __value
                __token = 871
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/portal_type', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_is_current_140574270397200 = get('is_current', __marker)

                # <Value u'node/currentItem' (19:29)> -> __value
                __token = 926
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/currentItem', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['is_current'] = __value
                __backup_is_in_path_140574284346640 = get('is_in_path', __marker)

                # <Value u'node/currentParent' (20:28)> -> __value
                __token = 981
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'node/currentParent', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['is_in_path'] = __value
                __backup_li_class_140574266161040 = get('li_class', __marker)

                # <Value u"python:is_current and ' active' or ''" (21:27)> -> __value
                __token = 1038
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"is_current and ' active' or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['li_class'] = __value
                __backup_li_extr_class_140574257219728 = get('li_extr_class', __marker)

                # <Value u"python:is_in_path and ' expanded' or ''" (22:26)> -> __value
                __token = 1114
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"is_in_path and ' expanded' or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['li_extr_class'] = __value
                __backup_li_folder_class_140574284359632 = get('li_folder_class', __marker)

                # <Value u"python:show_children and ' folderish' or ''" (23:25)> -> __value
                __token = 1192
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"show_children and ' folderish' or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['li_folder_class'] = __value
                __backup_normalizeString_140574284360848 = get('normalizeString', __marker)

                # <Value u'nocall: context/plone_utils/normalizeString' (24:24)> -> __value
                __token = 1274
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u' context/plone_utils/normalizeString', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['normalizeString'] = __value

                # <Value u'python:bottomLevel <= 0 or level <= bottomLevel' (26:25)> -> __condition
                __token = 1483
                try:
                    __zt_tmp = __attrs_140574268004240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'bottomLevel <= 0 or level <= bottomLevel', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268003152
                    __default_140574268003152 = _DEFAULT_MARKER

                    # <Substitution u'string:nav-item${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}' (25:32)> -> __attr_class
                    __token = 1366
                    try:
                        __zt_tmp = __attrs_140574268004240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'nav-item${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257251728
                    __attrs_140574257251728 = _static_140574442558096
                    __backup_item_class_140574284339536 = get('item_class', __marker)

                    # <Value u'string:senaite-state-${node/normalized_review_state}' (28:38)> -> __value
                    __token = 1578
                    try:
                        __zt_tmp = __attrs_140574257251728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('string', u'senaite-state-${node/normalized_review_state}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __backup_item_type_class_140574284461840 = get('item_type_class', __marker)

                    # <Value u"python:'senaite-contenttype-' + normalizeString(item_type)" (29:42)> -> __value
                    __token = 1674
                    try:
                        __zt_tmp = __attrs_140574257251728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"'senaite-contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_class_140574284340176 = get('item_class', __marker)

                    # <Value u"python:is_current and item_class + ' active' or item_class" (30:36)> -> __value
                    __token = 1771
                    try:
                        __zt_tmp = __attrs_140574257251728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"is_current and item_class + ' active' or item_class", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __append(u'\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff330f10> name=None at 7fd9ff330450> -> __attrs_140574266164048
                    __attrs_140574266164048 = _static_140574266167056

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266163408
                    __default_140574266163408 = _DEFAULT_MARKER

                    # <Substitution u'python:use_remote_url and item_remote_url or item_url' (32:34)> -> __attr_href
                    __token = 1870
                    try:
                        __zt_tmp = __attrs_140574266164048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('python', u'use_remote_url and item_remote_url or item_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266166288
                    __default_140574266166288 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution u'node/Title' (33:34)> at 7fd9ff330850> -> __attr_title

                    # <Substitution u'node/Title' (33:34)> -> __attr_title
                    __token = 1959
                    try:
                        __zt_tmp = __attrs_140574266164048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140574397981968('path', u'node/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266167184
                    __default_140574266167184 = _DEFAULT_MARKER

                    # <Substitution u'string:$item_class${li_class}${li_extr_class}${li_folder_class} $item_type_class nav-link' (34:33)> -> __attr_class
                    __token = 2005
                    try:
                        __zt_tmp = __attrs_140574266164048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'$item_class${li_class}${li_extr_class}${li_folder_class} $item_type_class nav-link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266166544
                    __attrs_140574266166544 = _static_140574442558096

                    # <Value u'python: level==1' (36:37)> -> __condition
                    __token = 2173
                    try:
                        __zt_tmp = __attrs_140574266166544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u' level==1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d93d0> name=None at 7fd9ff4d9990> -> __attrs_140574267904400
                        __attrs_140574267904400 = _static_140574267904976

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="node-icon">\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267907856
                        __attrs_140574267907856 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267904592
                        __default_140574267904592 = _DEFAULT_MARKER

                        # <Value u'item_icon' (38:44)> -> __cache_140574267904464
                        __token = 2275
                        try:
                            __zt_tmp = __attrs_140574267907856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574267904464 = _static_140574397981968('path', u'item_icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item_icon' (38:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d9650> -> __condition
                        __expression = __cache_140574267904464

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<img/>')
                        else:
                            __content = __cache_140574267904464
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n              </span>\n              ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d94d0> name=None at 7fd9ff4d9d50> -> __attrs_140574284336336
                        __attrs_140574284336336 = _static_140574267905232

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="node-title">')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267906192
                        __default_140574267906192 = _DEFAULT_MARKER

                        # <Value u'node/Title' (42:33)> -> __cache_140574267908048
                        __token = 2420
                        try:
                            __zt_tmp = __attrs_140574284336336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574267908048 = _static_140574397981968('path', u'node/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'node/Title' (42:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d9c50> -> __condition
                        __expression = __cache_140574267908048

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                Selected Item Title\n              ')
                        else:
                            __content = __cache_140574267908048
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n            ')
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284336912
                    __attrs_140574284336912 = _static_140574442558096

                    # <Value u'python: level>1' (46:41)> -> __condition
                    __token = 2556
                    try:
                        __zt_tmp = __attrs_140574284336912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u' level>1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda00484dd0> name=None at 7fda00484e90> -> __attrs_140574284438416
                        __attrs_140574284438416 = _static_140574284336592

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="text-truncate">\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda0049d750> name=None at 7fda0049dc10> -> __attrs_140574284437136
                        __attrs_140574284437136 = _static_140574284437328

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="child-icon">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270177168
                        __attrs_140574270177168 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270173584
                        __default_140574270173584 = _DEFAULT_MARKER

                        # <Value u'item_icon' (49:46)> -> __cache_140574284435984
                        __token = 2704
                        try:
                            __zt_tmp = __attrs_140574270177168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574284435984 = _static_140574397981968('path', u'item_icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item_icon' (49:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff703690> -> __condition
                        __expression = __cache_140574284435984

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<img/>')
                        else:
                            __content = __cache_140574284435984
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </span>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff703090> name=None at 7fd9ff7034d0> -> __attrs_140574270174672
                        __attrs_140574270174672 = _static_140574270173328

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="child-title">')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270177232
                        __default_140574270177232 = _DEFAULT_MARKER

                        # <Value u'node/Title' (53:35)> -> __cache_140574284437200
                        __token = 2858
                        try:
                            __zt_tmp = __attrs_140574270174672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574284437200 = _static_140574397981968('path', u'node/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'node/Title' (53:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff7031d0> -> __condition
                        __expression = __cache_140574284437200

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Selected Item Title')
                        else:
                            __content = __cache_140574284437200
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n              </div>\n            ')
                    __append(u'\n          </a>\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284334928
                    __attrs_140574284334928 = _static_140574442558096

                    # <Value u'has_children' (58:35)> -> __condition
                    __token = 2997
                    try:
                        __zt_tmp = __attrs_140574284334928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'has_children', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff7039d0> name=None at 7fd9ff7037d0> -> __attrs_140574270176848
                        __attrs_140574270176848 = _static_140574270175696

                        # <Value u'python: len(children) > 0 and show_children and bottomLevel and level < bottomLevel or True' (60:31)> -> __condition
                        __token = 3125
                        try:
                            __zt_tmp = __attrs_140574270176848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('python', u' len(children) > 0 and show_children and bottomLevel and level < bottomLevel or True', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<ul')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270176656
                            __default_140574270176656 = _DEFAULT_MARKER

                            # <Substitution u"python:'nav submenu nav-level-'+str(level)" (59:38)> -> __attr_class
                            __token = 3050
                            try:
                                __zt_tmp = __attrs_140574270176848
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('python', u"'nav submenu nav-level-'+str(level)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>\n              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270228752
                            __attrs_140574270228752 = _static_140574442558096

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270226960
                            __default_140574270226960 = _DEFAULT_MARKER

                            # <Value u"python:view.recurse(children=sorted(children, key=lambda n: n.get('Title')), level=level+1, bottomLevel=bottomLevel)" (61:43)> -> __cache_140574270227408
                            __token = 3262
                            try:
                                __zt_tmp = __attrs_140574270228752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574270227408 = _static_140574397981968('python', u"view.recurse(children=sorted(children, key=lambda n: n.get('Title')), level=level+1, bottomLevel=bottomLevel)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u"python:view.recurse(children=sorted(children, key=lambda n: n.get('Title')), level=level+1, bottomLevel=bottomLevel)" (61:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff710b50> -> __condition
                            __expression = __cache_140574270227408

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span />')
                            else:
                                __content = __cache_140574270227408
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'\n            </ul>')
                        __append(u'\n          ')
                    __append(u'\n\n        ')
                    if (__backup_item_class_140574284340176 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_140574284340176
                    if (__backup_item_type_class_140574284461840 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140574284461840
                    if (__backup_item_class_140574284339536 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_140574284339536
                    __append(u'\n      </li>')
                if (__backup_normalizeString_140574284360848 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140574284360848
                if (__backup_li_folder_class_140574284359632 is __marker):
                    del econtext['li_folder_class']
                else:
                    econtext['li_folder_class'] = __backup_li_folder_class_140574284359632
                if (__backup_li_extr_class_140574257219728 is __marker):
                    del econtext['li_extr_class']
                else:
                    econtext['li_extr_class'] = __backup_li_extr_class_140574257219728
                if (__backup_li_class_140574266161040 is __marker):
                    del econtext['li_class']
                else:
                    econtext['li_class'] = __backup_li_class_140574266161040
                if (__backup_is_in_path_140574284346640 is __marker):
                    del econtext['is_in_path']
                else:
                    econtext['is_in_path'] = __backup_is_in_path_140574284346640
                if (__backup_is_current_140574270397200 is __marker):
                    del econtext['is_current']
                else:
                    econtext['is_current'] = __backup_is_current_140574270397200
                if (__backup_item_type_140574281971984 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_140574281971984
                if (__backup_item_icon_140574284474192 is __marker):
                    del econtext['item_icon']
                else:
                    econtext['item_icon'] = __backup_item_icon_140574284474192
                if (__backup_item_140574284437520 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140574284437520
                if (__backup_use_remote_url_140574270300240 is __marker):
                    del econtext['use_remote_url']
                else:
                    econtext['use_remote_url'] = __backup_use_remote_url_140574270300240
                if (__backup_item_remote_url_140574284341008 is __marker):
                    del econtext['item_remote_url']
                else:
                    econtext['item_remote_url'] = __backup_item_remote_url_140574284341008
                if (__backup_item_url_140574270302480 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_140574270302480
                if (__backup_has_children_140574284447312 is __marker):
                    del econtext['has_children']
                else:
                    econtext['has_children'] = __backup_has_children_140574284447312
                if (__backup_children_140574284358480 is __marker):
                    del econtext['children']
                else:
                    econtext['children'] = __backup_children_140574284358480
                if (__backup_show_children_140574284463952 is __marker):
                    del econtext['show_children']
                else:
                    econtext['show_children'] = __backup_show_children_140574284463952
                __append(u'\n    ')
                ____index_140574268002832 -= 1
                if (____index_140574268002832 > 0):
                    __append('')
            if (__backup_node_140574266162640 is __marker):
                del econtext['node']
            else:
                econtext['node'] = __backup_node_140574266162640
            __append(u'\n  ')
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270224336
            __attrs_140574270224336 = _static_140574442558096
            __backup_level_140574284462736 = get('level', __marker)

            # <Value u'options/level|python:0' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574270224336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/level|python:0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['level'] = __value
            __backup_children_140574270188560 = get('children', __marker)

            # <Value u'options/children | nothing' (2:28)> -> __value
            __token = 78
            try:
                __zt_tmp = __attrs_140574270224336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/children | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['children'] = __value
            __backup_bottomLevel_140574284445520 = get('bottomLevel', __marker)

            # <Value u'options/bottomLevel | nothing' (3:30)> -> __value
            __token = 137
            try:
                __zt_tmp = __attrs_140574270224336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/bottomLevel | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['bottomLevel'] = __value
            __backup_bootstrapview_140574266163152 = get('bootstrapview', __marker)

            # <Value u'nocall:context/@@bootstrapview' (4:31)> -> __value
            __token = 201
            try:
                __zt_tmp = __attrs_140574270224336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('nocall', u'context/@@bootstrapview', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['bootstrapview'] = __value
            __previous_i18n_domain_140574270225168 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __append(u'\n\n  ')
            __token = None
            render_nav_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140574270225168
            if (__backup_bootstrapview_140574266163152 is __marker):
                del econtext['bootstrapview']
            else:
                econtext['bootstrapview'] = __backup_bootstrapview_140574266163152
            if (__backup_bottomLevel_140574284445520 is __marker):
                del econtext['bottomLevel']
            else:
                econtext['bottomLevel'] = __backup_bottomLevel_140574284445520
            if (__backup_children_140574270188560 is __marker):
                del econtext['children']
            else:
                econtext['children'] = __backup_children_140574270188560
            if (__backup_level_140574284462736 is __marker):
                del econtext['level']
            else:
                econtext['level'] = __backup_level_140574284462736
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_nav_main': render_nav_main, 'render': render, }