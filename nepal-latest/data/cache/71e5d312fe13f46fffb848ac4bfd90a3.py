# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/document_relateditems.pt'

__tokens = {76: (u'view/related_items', 3, 25), 116: (u'related', 4, 20), 275: (u'nocall:context/@@plone', 7, 37), 337: (u' nocall:context/@@plone_layou', 8, 38), 409: (u'g nocall:plone_view/normalizeStri', 9, 40), 483: (u'te nocall:context/@@plone_context_st', 10, 37), 562: (u"ion python:context.portal_registry.get('types_use_view_action_in_listings',", 11, 38), 767: (u'related', 14, 31), 827: (u'item/Description', 15, 50), 894: (u' item/portal_typ', 16, 49), 961: (u"  python:'contenttype-' + normalizeString(item_typ", 17, 48), 1062: (u'   item/review_state|python: context_state.workflow_stat', 18, 47), 1169: (u"ass python: 'state-' + normalizeString(item_wf_st", 19, 46), 1269: (u'     item/getURL|item/absolut', 20, 45), 1349: (u"      python:(item_type in use_view_action) and item_url+'/view' or it", 21, 44), 1470: (u'e      python:item.', 22, 43), 1550: (u'item_type', 23, 52), 1601: (u'item_url', 24, 39), 1695: (u"python:item.getURL() +'/@@images/image/icon'", 26, 42), 1778: (u'item_has_image', 27, 37), 1837: (u'string:$getIcon', 28, 43), 1856: (u' item/Descriptio', 28, 62), 1922: (u'string:$item_type_class $item_wf_state_class url', 29, 46), 2010: (u'item/pretty_title_or_id', 30, 37), 2158: (u'item/Description', 33, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574267901712 = {u'href': u'item_url', }
_static_140574266212112 = {u'src': u'string:$getIcon', u'alt': u'item/Description', u'class': u'thumb-icon', }
_static_140574442558096 = {}
_static_140574268016912 = {u'id': u'relatedItemBox', }
_static_140574267881552 = {u'title': u'item_type', }
_static_140574270360976 = {u'class': u'relatedItems', }
_static_140574284440720 = {u'class': u'discreet', }
_static_140574397981968 = __compile_zt_expr
_static_140574270360848 = {u'class': u'visualClear', u'id': u'clear-space-before-relatedItemBox', }
_static_140574270395408 = {u'class': u'string:$item_type_class $item_wf_state_class url', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff730d90> name=None at 7fd9ff4efed0> -> __attrs_140574270359376
            __attrs_140574270359376 = _static_140574270360976
            __backup_related_140574267899984 = get('related', __marker)

            # <Value u'view/related_items' (3:25)> -> __value
            __token = 76
            try:
                __zt_tmp = __attrs_140574270359376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/related_items', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['related'] = __value

            # <Value u'related' (4:20)> -> __condition
            __token = 116
            try:
                __zt_tmp = __attrs_140574270359376
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'related', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270359952 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="relatedItems">\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff730d10> name=None at 7fd9ff730310> -> __attrs_140574270357904
                __attrs_140574270357904 = _static_140574270360848

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear" id="clear-space-before-relatedItemBox"><!-- --></div>\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f4910> name=None at 7fd9ff4f40d0> -> __attrs_140574268017168
                __attrs_140574268017168 = _static_140574268016912
                __backup_plone_view_140574269031760 = get('plone_view', __marker)

                # <Value u'nocall:context/@@plone' (7:37)> -> __value
                __token = 275
                try:
                    __zt_tmp = __attrs_140574268017168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u'context/@@plone', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['plone_view'] = __value
                __backup_plone_layout_140574267906640 = get('plone_layout', __marker)

                # <Value u'nocall:context/@@plone_layout' (8:38)> -> __value
                __token = 337
                try:
                    __zt_tmp = __attrs_140574268017168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u'context/@@plone_layout', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['plone_layout'] = __value
                __backup_normalizeString_140574284341200 = get('normalizeString', __marker)

                # <Value u'nocall:plone_view/normalizeString' (9:40)> -> __value
                __token = 409
                try:
                    __zt_tmp = __attrs_140574268017168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u'plone_view/normalizeString', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['normalizeString'] = __value
                __backup_context_state_140574270458960 = get('context_state', __marker)

                # <Value u'nocall:context/@@plone_context_state' (10:37)> -> __value
                __token = 483
                try:
                    __zt_tmp = __attrs_140574268017168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u'context/@@plone_context_state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['context_state'] = __value
                __backup_use_view_action_140574267902480 = get('use_view_action', __marker)

                # <Value u"python:context.portal_registry.get('types_use_view_action_in_listings', [])" (11:38)> -> __value
                __token = 562
                try:
                    __zt_tmp = __attrs_140574268017168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"context.portal_registry.get('types_use_view_action_in_listings', [])", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['use_view_action'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="relatedItemBox">\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270166544
                __attrs_140574270166544 = _static_140574442558096

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header>')
                __stream_140574270165776 = []
                __append_140574270165776 = __stream_140574270165776.append
                __append_140574270165776(u'Related content')
                __msgid_140574270165776 = __re_whitespace(''.join(__stream_140574270165776)).strip()
                if u'label_related_items':
                    __append(translate(u'label_related_items', mapping=None, default=__msgid_140574270165776, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270168080
                __attrs_140574270168080 = _static_140574442558096

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267880720
                __attrs_140574267880720 = _static_140574442558096
                __backup_item_140574284340560 = get('item', __marker)

                # <Value u'related' (14:31)> -> __iterator
                __token = 767
                try:
                    __zt_tmp = __attrs_140574267880720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'related', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574267883024, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4d3850> name=None at 7fd9ff4d9ad0> -> __attrs_140574267882768
                    __attrs_140574267882768 = _static_140574267881552
                    __backup_desc_140574267903888 = get('desc', __marker)

                    # <Value u'item/Description' (15:50)> -> __value
                    __token = 827
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'item/Description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['desc'] = __value
                    __backup_item_type_140574267880336 = get('item_type', __marker)

                    # <Value u'item/portal_type' (16:49)> -> __value
                    __token = 894
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'item/portal_type', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_140574266211728 = get('item_type_class', __marker)

                    # <Value u"python:'contenttype-' + normalizeString(item_type)" (17:48)> -> __value
                    __token = 961
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"'contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_140574270348816 = get('item_wf_state', __marker)

                    # <Value u'item/review_state|python: context_state.workflow_state()' (18:47)> -> __value
                    __token = 1062
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'item/review_state|python: context_state.workflow_state()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_140574284338384 = get('item_wf_state_class', __marker)

                    # <Value u"python: 'state-' + normalizeString(item_wf_state)" (19:46)> -> __value
                    __token = 1169
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u" 'state-' + normalizeString(item_wf_state)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_url_140574284340816 = get('item_url', __marker)

                    # <Value u'item/getURL|item/absolute_url' (20:45)> -> __value
                    __token = 1269
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'item/getURL|item/absolute_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_url_140574268940432 = get('item_url', __marker)

                    # <Value u"python:(item_type in use_view_action) and item_url+'/view' or item_url" (21:44)> -> __value
                    __token = 1349
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"(item_type in use_view_action) and item_url+'/view' or item_url", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_has_image_140574284372304 = get('item_has_image', __marker)

                    # <Value u'python:item.getIcon' (22:43)> -> __value
                    __token = 1470
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u'item.getIcon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267879696
                    __default_140574267879696 = _DEFAULT_MARKER

                    # <Substitution u'item_type' (23:52)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_140574267882768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140574397981968('path', u'item_type', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4d8710> name=None at 7fd9ff4d80d0> -> __attrs_140574266209104
                    __attrs_140574266209104 = _static_140574267901712

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267903248
                    __default_140574267903248 = _DEFAULT_MARKER

                    # <Substitution u'item_url' (24:39)> -> __attr_href
                    __token = 1601
                    try:
                        __zt_tmp = __attrs_140574266209104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'item_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>\n                 ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff33bf10> name=None at 7fd9ff33bf50> -> __attrs_140574266210640
                    __attrs_140574266210640 = _static_140574266212112
                    __backup_getIcon_140574284361168 = get('getIcon', __marker)

                    # <Value u"python:item.getURL() +'/@@images/image/icon'" (26:42)> -> __value
                    __token = 1695
                    try:
                        __zt_tmp = __attrs_140574266210640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"item.getURL() +'/@@images/image/icon'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['getIcon'] = __value

                    # <Value u'item_has_image' (27:37)> -> __condition
                    __token = 1778
                    try:
                        __zt_tmp = __attrs_140574266210640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'item_has_image', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img class="thumb-icon"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266209040
                        __default_140574266209040 = _DEFAULT_MARKER

                        # <Substitution u'string:$getIcon' (28:43)> -> __attr_src
                        __token = 1837
                        try:
                            __zt_tmp = __attrs_140574266210640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140574397981968('string', u'$getIcon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266209168
                        __default_140574266209168 = _DEFAULT_MARKER

                        # <Substitution u'item/Description' (28:62)> -> __attr_alt
                        __token = 1856
                        try:
                            __zt_tmp = __attrs_140574266210640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140574397981968('path', u'item/Description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))
                        __append(u'>')
                    if (__backup_getIcon_140574284361168 is __marker):
                        del econtext['getIcon']
                    else:
                        econtext['getIcon'] = __backup_getIcon_140574284361168
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff739410> name=None at 7fd9ff7390d0> -> __attrs_140574270395856
                    __attrs_140574270395856 = _static_140574270395408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270396432
                    __default_140574270396432 = _DEFAULT_MARKER

                    # <Substitution u'string:$item_type_class $item_wf_state_class url' (29:46)> -> __attr_class
                    __token = 1922
                    try:
                        __zt_tmp = __attrs_140574270395856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'$item_type_class $item_wf_state_class url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270397712
                    __default_140574270397712 = _DEFAULT_MARKER

                    # <Value u'item/pretty_title_or_id' (30:37)> -> __cache_140574270396240
                    __token = 2010
                    try:
                        __zt_tmp = __attrs_140574270395856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574270396240 = _static_140574397981968('path', u'item/pretty_title_or_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/pretty_title_or_id' (30:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff739a50> -> __condition
                    __expression = __cache_140574270396240

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                          Item Title')
                    else:
                        __content = __cache_140574270396240
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fda0049e490> name=None at 7fda0049e590> -> __attrs_140574284443536
                    __attrs_140574284443536 = _static_140574284440720

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="discreet">')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284441424
                    __default_140574284441424 = _DEFAULT_MARKER

                    # <Value u'item/Description' (33:37)> -> __cache_140574270396624
                    __token = 2158
                    try:
                        __zt_tmp = __attrs_140574284443536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574270396624 = _static_140574397981968('path', u'item/Description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/Description' (33:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff739f90> -> __condition
                    __expression = __cache_140574270396624

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'description')
                    else:
                        __content = __cache_140574270396624
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n               </a>\n            </span>')
                    if (__backup_item_has_image_140574284372304 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_140574284372304
                    if (__backup_item_url_140574268940432 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140574268940432
                    if (__backup_item_url_140574284340816 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140574284340816
                    if (__backup_item_wf_state_class_140574284338384 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_140574284338384
                    if (__backup_item_wf_state_140574270348816 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_140574270348816
                    if (__backup_item_type_class_140574266211728 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140574266211728
                    if (__backup_item_type_140574267880336 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_140574267880336
                    if (__backup_desc_140574267903888 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_140574267903888
                    __append(u'\n          </li>')
                    ____index_140574267883024 -= 1
                    if (____index_140574267883024 > 0):
                        __append('\n          ')
                if (__backup_item_140574284340560 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140574284340560
                __append(u'\n        </ul>\n    </div>')
                if (__backup_use_view_action_140574267902480 is __marker):
                    del econtext['use_view_action']
                else:
                    econtext['use_view_action'] = __backup_use_view_action_140574267902480
                if (__backup_context_state_140574270458960 is __marker):
                    del econtext['context_state']
                else:
                    econtext['context_state'] = __backup_context_state_140574270458960
                if (__backup_normalizeString_140574284341200 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140574284341200
                if (__backup_plone_layout_140574267906640 is __marker):
                    del econtext['plone_layout']
                else:
                    econtext['plone_layout'] = __backup_plone_layout_140574267906640
                if (__backup_plone_view_140574269031760 is __marker):
                    del econtext['plone_view']
                else:
                    econtext['plone_view'] = __backup_plone_view_140574269031760
                __append(u'\n</div>')
                __i18n_domain = __previous_i18n_domain_140574270359952
            if (__backup_related_140574267899984 is __marker):
                del econtext['related']
            else:
                econtext['related'] = __backup_related_140574267899984
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }