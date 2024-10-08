# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.Archetypes-1.16.6-py2.7.egg/Products/Archetypes/skins/archetypes/widgets/textarea.pt'

__tokens = {3993: (u'string:${fieldName}_text_format', 90, 36), 4055: (u' python:request.get(field_text_format, context.getContentType(fieldName)', 91, 29), 4154: (u"t python:getattr(field, 'getAllowedContentTypes', Fals", 92, 24), 4240: (u"ct python:get_act and get_act(here) or ('text/plain", 93, 28), 4320: (u"pes python:[t for t in allowable_ct if t.startswith('text", 94, 24), 4408: (u"type python:hasattr(field, 'getContentType') and field.getContentType(here) ", 95, 25), 4527: (u'python:len(mimetypes) > 1', 97, 34), 4723: (u'context/@@at_textarea_widget', 100, 43), 4792: (u' python:textareaview.getSelected(mimetypes, contenttype', 101, 39), 4887: (u'string:${fieldName}_text_format', 102, 37), 4958: (u' string:${fieldName}_text_forma', 103, 38), 5153: (u'python:contenttype not in mimetypes', 107, 35), 5105: (u'contentType', 106, 42), 5276: (u'mimetypes', 110, 37), 5400: (u'item', 112, 42), 5450: (u" python:item in selection and 'selected' or Non", 113, 44), 5320: (u'python:textareaview.lookupMime(item)', 111, 33), 5618: (u'python:len(mimetypes) == 1', 118, 34), 5767: (u'field_text_format', 122, 38), 5824: (u' python:mimetypes[0', 123, 38), 6503: (u'context/widgets/textarea/macros/area_edit', 142, 34), 6503: (u'context/widgets/textarea/macros/area_edit', 142, 34), 6387: (u'context/widgets/field/macros/edit', 139, 28), 6387: (u'context/widgets/field/macros/edit', 139, 28), 6128: (u'context/widgets/textarea/macros/area_edit', 132, 34), 6128: (u'context/widgets/textarea/macros/area_edit', 132, 34), 6208: (u'context/widgets/textarea/macros/area_format', 133, 34), 6208: (u'context/widgets/textarea/macros/area_format', 133, 34), 5999: (u'field_macro | context/widgets/field/macros/edit', 130, 28), 5999: (u'field_macro | context/widgets/field/macros/edit', 130, 28), 1131: (u"python:hasattr(value, 'isUnit')", 29, 23), 1188: (u' python:base and value.isBinary() or context.isBinary(fieldName', 30, 24), 1278: (u't python: not not base and value.getRaw() or val', 31, 24), 1353: (u'nt python: not binary and content or', 32, 23), 1423: (u"gth python:len(unicode(content, 'utf-", 33, 29), 1491: (u'only widget/append_only|no', 34, 25), 1546: (u'ength widget/maxlength|n', 35, 22), 1596: (u'tcname string:textCounter_${fie', 36, 18), 1655: (u"eypress string:textCounter(this, '${tcname}', ${max", 37, 19), 2213: (u"python:not append_only and content or ''", 48, 32), 1813: (u'fieldName', 41, 33), 1854: (u' fieldNam', 42, 30), 1897: (u's widget/co', 43, 31), 1942: (u'ws widget/r', 44, 30), 1994: (u'der widget/placeholder|not', 45, 36), 2059: (u'down python:test(maxlength, keypress, ', 46, 33), 2134: (u'keyup python:test(maxlength, keypress,', 47, 30), 2281: (u'content', 49, 25), 2342: (u'maxlength', 51, 32), 2711: (u"python:(int(maxlength) - content_length) + content.count('\\n')", 60, 45), 2819: (u'tcname', 61, 44), 2871: (u' remainin', 62, 44), 2923: (u'd string:maxlength_${fieldNam', 63, 40), 3054: (u'append_only', 67, 37), 3148: (u'widget/label', 69, 40), 3197: (u'string:HISTORY: ${label}', 70, 35), 3343: (u'python:(content_length &lt; 3', 74, 35), 3410: (u'accessor', 75, 33), 3548: (u'python:(content_length &gt;= 3', 77, 45), 3686: (u'widget/cols', 79, 51), 3749: (u' widget/row', 80, 50), 3626: (u'content', 78, 43), 606: (u"python:getKssClasses(fieldName,\n                              templateId='widgets/textarea', macro='textarea-field-view')", 17, 34), 762: (u' context/UID|nothin', 19, 33), 819: (u'kss_class', 20, 34), 860: (u' string:parent-fieldname-$fieldName-$ui', 21, 30), 979: (u'accessor', 23, 31), 390: (u'context/@@kss_field_decorator_view', 14, 39), 463: (u' nocall:kssClassesView/getKssClassesInlineEditabl', 15, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047220304 = u'area_edit'
_static_140168025886928 = {u'type': u'hidden', u'name': u'', u'value': u'', }
_static_140168015745232 = u'edit'
_static_140168046974160 = {u'class': u'kss_class', u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047243984 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168036673872 = {u'readonly': u'readonly', u'rows': u'widget/rows', u'cols': u'widget/cols', }
_static_140168047219664 = u'area_format'
_static_140168015748816 = {u'style': u'text-align: right; margin-right: 0.75em;', }
_static_140168047221456 = u'edit'
_static_140168257770128 = {}
_static_140168037252880 = {u'name': u'', u'value': u'', u'readonly': u'readonly', u'maxlength': u'4', u'type': u'text', u'id': u'string:maxlength_${fieldName}', u'size': u'4', }
_static_140168015747216 = {u'id': u'string:${fieldName}_text_format', u'name': u'string:${fieldName}_text_format', }
_static_140168047219216 = u'area_edit'
_static_140168015659152 = {u'rows': u'widget/rows', u'name': u'fieldName', u'cols': u'widget/cols', u'class': u'blurrable firstToFocus', u'onkeydown': u'python:test(maxlength, keypress, None)', u'onkeyup': u'python:test(maxlength, keypress, None)', u'placeholder': u'widget/placeholder|nothing', u'id': u'fieldName', }
_static_140168015703696 = {u'selected': u"python:item in selection and 'selected' or None", u'value': u'item', }
_static_140168015701840 = {u'selected': u'selected', u'value': u'', }

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

    def render_area_format(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015661648
            __attrs_140168015661648 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036672464
            __attrs_140168036672464 = _static_140168257770128
            __backup_field_text_format_140168037311184 = get('field_text_format', __marker)

            # <Value u'string:${fieldName}_text_format' (90:36)> -> __value
            __token = 3993
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}_text_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['field_text_format'] = __value
            __backup_contentType_140168036662736 = get('contentType', __marker)

            # <Value u'python:request.get(field_text_format, context.getContentType(fieldName))' (91:29)> -> __value
            __token = 4055
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'request.get(field_text_format, context.getContentType(fieldName))', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['contentType'] = __value
            __backup_get_act_140168037260880 = get('get_act', __marker)

            # <Value u"python:getattr(field, 'getAllowedContentTypes', False)" (92:24)> -> __value
            __token = 4154
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"getattr(field, 'getAllowedContentTypes', False)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['get_act'] = __value
            __backup_allowable_ct_140168016872144 = get('allowable_ct', __marker)

            # <Value u"python:get_act and get_act(here) or ('text/plain',)" (93:28)> -> __value
            __token = 4240
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"get_act and get_act(here) or ('text/plain',)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['allowable_ct'] = __value
            __backup_mimetypes_140168006709904 = get('mimetypes', __marker)

            # <Value u"python:[t for t in allowable_ct if t.startswith('text/')]" (94:24)> -> __value
            __token = 4320
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"[t for t in allowable_ct if t.startswith('text/')]", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['mimetypes'] = __value
            __backup_contenttype_140168047356112 = get('contenttype', __marker)

            # <Value u"python:hasattr(field, 'getContentType') and field.getContentType(here) or ''" (95:25)> -> __value
            __token = 4408
            try:
                __zt_tmp = __attrs_140168036672464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"hasattr(field, 'getContentType') and field.getContentType(here) or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['contenttype'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037644240
            __attrs_140168037644240 = _static_140168257770128

            # <Value u'python:len(mimetypes) > 1' (97:34)> -> __condition
            __token = 4527
            try:
                __zt_tmp = __attrs_140168037644240
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'len(mimetypes) > 1', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b68c99ed0> name=None at 7f7b68c99150> -> __attrs_140168015745296
                __attrs_140168015745296 = _static_140168015748816

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div style="text-align: right; margin-right: 0.75em;">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015748880
                __attrs_140168015748880 = _static_140168257770128

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label>')
                __stream_140168015749072 = []
                __append_140168015749072 = __stream_140168015749072.append
                __append_140168015749072(u'Format')
                __msgid_140168015749072 = __re_whitespace(''.join(__stream_140168015749072)).strip()
                if u'label_format':
                    __append(translate(u'label_format', mapping=None, default=__msgid_140168015749072, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b68c99890> name=None at 7f7b68c99c50> -> __attrs_140168015745616
                __attrs_140168015745616 = _static_140168015747216
                __backup_textareaview_140168036662160 = get('textareaview', __marker)

                # <Value u'context/@@at_textarea_widget' (100:43)> -> __value
                __token = 4723
                try:
                    __zt_tmp = __attrs_140168015745616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/@@at_textarea_widget', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['textareaview'] = __value
                __backup_selection_140168047122960 = get('selection', __marker)

                # <Value u'python:textareaview.getSelected(mimetypes, contenttype)' (101:39)> -> __value
                __token = 4792
                try:
                    __zt_tmp = __attrs_140168015745616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'textareaview.getSelected(mimetypes, contenttype)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['selection'] = __value

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015748752
                __default_140168015748752 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_text_format' (102:37)> -> __attr_id
                __token = 4887
                try:
                    __zt_tmp = __attrs_140168015745616
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${fieldName}_text_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015749008
                __default_140168015749008 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_text_format' (103:38)> -> __attr_name
                __token = 4958
                try:
                    __zt_tmp = __attrs_140168015745616
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}_text_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))
                __append(u'>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68c8e750> name=None at 7f7b68c8ee50> -> __attrs_140168015702352
                __attrs_140168015702352 = _static_140168015701840

                # <Value u'python:contenttype not in mimetypes' (107:35)> -> __condition
                __token = 5153
                try:
                    __zt_tmp = __attrs_140168015702352
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'contenttype not in mimetypes', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option selected="selected"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015703248
                    __default_140168015703248 = _DEFAULT_MARKER

                    # <Substitution u'contentType' (106:42)> -> __attr_value
                    __token = 5105
                    try:
                        __zt_tmp = __attrs_140168015702352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('path', u'contentType', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>\n              (no change)\n            </option>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68c8ee90> name=None at 7f7b68c8ec90> -> __attrs_140168025890320
                __attrs_140168025890320 = _static_140168015703696
                __backup_item_140168036659344 = get('item', __marker)

                # <Value u'mimetypes' (110:37)> -> __iterator
                __token = 5276
                try:
                    __zt_tmp = __attrs_140168025890320
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'mimetypes', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168025890064, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015700752
                    __default_140168015700752 = _DEFAULT_MARKER

                    # <Substitution u'item' (112:42)> -> __attr_value
                    __token = 5400
                    try:
                        __zt_tmp = __attrs_140168025890320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('path', u'item', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015700304
                    __default_140168015700304 = _DEFAULT_MARKER

                    # <Boolean u"python:item in selection and 'selected' or None" (113:44)> -> __attr_selected
                    __token = 5450
                    try:
                        __zt_tmp = __attrs_140168025890320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140168208991440('python', u"item in selection and 'selected' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = u'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((u' selected="%s"' % __attr_selected))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015702416
                    __default_140168015702416 = _DEFAULT_MARKER

                    # <Value u'python:textareaview.lookupMime(item)' (111:33)> -> __cache_140168015701008
                    __token = 5320
                    try:
                        __zt_tmp = __attrs_140168025890320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168015701008 = _static_140168208991440('python', u'textareaview.lookupMime(item)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:textareaview.lookupMime(item)' (111:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68c8ee10> -> __condition
                    __expression = __cache_140168015701008

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168015701008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option>')
                    ____index_140168025890064 -= 1
                    if (____index_140168025890064 > 0):
                        __append('\n            ')
                if (__backup_item_140168036659344 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140168036659344
                __append(u'\n          </select>')
                if (__backup_selection_140168047122960 is __marker):
                    del econtext['selection']
                else:
                    econtext['selection'] = __backup_selection_140168047122960
                if (__backup_textareaview_140168036662160 is __marker):
                    del econtext['textareaview']
                else:
                    econtext['textareaview'] = __backup_textareaview_140168036662160
                __append(u'\n        </div>\n        ')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015746256
            __attrs_140168015746256 = _static_140168257770128

            # <Value u'python:len(mimetypes) == 1' (118:34)> -> __condition
            __token = 5618
            try:
                __zt_tmp = __attrs_140168015746256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'len(mimetypes) == 1', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b696450d0> name=None at 7f7b69645850> -> __attrs_140168025888400
                __attrs_140168025888400 = _static_140168025886928

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025888464
                __default_140168025888464 = _DEFAULT_MARKER

                # <Substitution u'field_text_format' (122:38)> -> __attr_name
                __token = 5767
                try:
                    __zt_tmp = __attrs_140168025888400
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('path', u'field_text_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025890000
                __default_140168025890000 = _DEFAULT_MARKER

                # <Substitution u'python:mimetypes[0]' (123:38)> -> __attr_value
                __token = 5824
                try:
                    __zt_tmp = __attrs_140168025888400
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u'mimetypes[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u' />\n        ')
            __append(u'\n      ')
            if (__backup_contenttype_140168047356112 is __marker):
                del econtext['contenttype']
            else:
                econtext['contenttype'] = __backup_contenttype_140168047356112
            if (__backup_mimetypes_140168006709904 is __marker):
                del econtext['mimetypes']
            else:
                econtext['mimetypes'] = __backup_mimetypes_140168006709904
            if (__backup_allowable_ct_140168016872144 is __marker):
                del econtext['allowable_ct']
            else:
                econtext['allowable_ct'] = __backup_allowable_ct_140168016872144
            if (__backup_get_act_140168037260880 is __marker):
                del econtext['get_act']
            else:
                econtext['get_act'] = __backup_get_act_140168037260880
            if (__backup_contentType_140168036662736 is __marker):
                del econtext['contentType']
            else:
                econtext['contentType'] = __backup_contentType_140168036662736
            if (__backup_field_text_format_140168037311184 is __marker):
                del econtext['field_text_format']
            else:
                econtext['field_text_format'] = __backup_field_text_format_140168037311184
            __append(u'\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_search(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037251856
            __attrs_140168037251856 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047222224
            __attrs_140168047222224 = _static_140168257770128
            __backup_macroname_140168055549696 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa9dad0> name=None at 7f7b6aa9d850> -> __value
            __value = _static_140168047221456
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047222352
                __attrs_140168047222352 = _static_140168257770128
                __append(u'\n\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047218960
                __attrs_140168047218960 = _static_140168257770128
                __backup_macroname_140168055599824 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa9d210> name=None at 7f7b6aa9d310> -> __value
                __value = _static_140168047219216
                econtext['macroname'] = __value

                # <Value u'context/widgets/textarea/macros/area_edit' (142:34)> -> __macro
                __token = 6503
                try:
                    __zt_tmp = __attrs_140168047218960
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/widgets/textarea/macros/area_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 6503
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168055599824 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168055599824
                __append(u'\n\n        ')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'context/widgets/field/macros/edit' (139:28)> -> __macro
            __token = 6387
            try:
                __zt_tmp = __attrs_140168047222224
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 6387
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055549696 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055549696
            __append(u'\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_edit(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037323408
            __attrs_140168037323408 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025889744
            __attrs_140168025889744 = _static_140168257770128
            __backup_macroname_140168057196704 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b68c990d0> name=None at 7f7b69645a90> -> __value
            __value = _static_140168015745232
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025890448
                __attrs_140168025890448 = _static_140168257770128
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047219600
                __attrs_140168047219600 = _static_140168257770128
                __backup_macroname_140168055599664 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa9d650> name=None at 7f7b6aa9dcd0> -> __value
                __value = _static_140168047220304
                econtext['macroname'] = __value

                # <Value u'context/widgets/textarea/macros/area_edit' (132:34)> -> __macro
                __token = 6128
                try:
                    __zt_tmp = __attrs_140168047219600
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/widgets/textarea/macros/area_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 6128
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168055599664 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168055599664
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047220368
                __attrs_140168047220368 = _static_140168257770128
                __backup_macroname_140168055601104 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa9d3d0> name=None at 7f7b6aa9d090> -> __value
                __value = _static_140168047219664
                econtext['macroname'] = __value

                # <Value u'context/widgets/textarea/macros/area_format' (133:34)> -> __macro
                __token = 6208
                try:
                    __zt_tmp = __attrs_140168047220368
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/widgets/textarea/macros/area_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 6208
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168055601104 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168055601104
                __append(u'\n        ')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (130:28)> -> __macro
            __token = 5999
            try:
                __zt_tmp = __attrs_140168025889744
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 5999
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057196704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057196704
            __append(u'\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_area_edit(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046976336
            __attrs_140168046976336 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015659472
            __attrs_140168015659472 = _static_140168257770128
            __backup_base_140168006712272 = get('base', __marker)

            # <Value u"python:hasattr(value, 'isUnit')" (29:23)> -> __value
            __token = 1131
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"hasattr(value, 'isUnit')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['base'] = __value
            __backup_binary_140168037225616 = get('binary', __marker)

            # <Value u'python:base and value.isBinary() or context.isBinary(fieldName)' (30:24)> -> __value
            __token = 1188
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'base and value.isBinary() or context.isBinary(fieldName)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['binary'] = __value
            __backup_content_140168047811024 = get('content', __marker)

            # <Value u'python: not not base and value.getRaw() or value' (31:24)> -> __value
            __token = 1278
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' not not base and value.getRaw() or value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['content'] = __value
            __backup_content_140168037526736 = get('content', __marker)

            # <Value u"python: not binary and content or ''" (32:23)> -> __value
            __token = 1353
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" not binary and content or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['content'] = __value
            __backup_content_length_140168016875216 = get('content_length', __marker)

            # <Value u"python:len(unicode(content, 'utf-8'))" (33:29)> -> __value
            __token = 1423
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"len(unicode(content, 'utf-8'))", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['content_length'] = __value
            __backup_append_only_140168037258000 = get('append_only', __marker)

            # <Value u'widget/append_only|nothing' (34:25)> -> __value
            __token = 1491
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/append_only|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['append_only'] = __value
            __backup_maxlength_140168036459280 = get('maxlength', __marker)

            # <Value u'widget/maxlength|nothing' (35:22)> -> __value
            __token = 1546
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/maxlength|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['maxlength'] = __value
            __backup_tcname_140168036659856 = get('tcname', __marker)

            # <Value u'string:textCounter_${fieldName}' (36:18)> -> __value
            __token = 1596
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'textCounter_${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['tcname'] = __value
            __backup_keypress_140168037145296 = get('keypress', __marker)

            # <Value u"string:textCounter(this, '${tcname}', ${maxlength})" (37:19)> -> __value
            __token = 1655
            try:
                __zt_tmp = __attrs_140168015659472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u"textCounter(this, '${tcname}', ${maxlength})", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['keypress'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68c84090> name=None at 7f7b68c849d0> -> __attrs_140168036944592
            __attrs_140168036944592 = _static_140168015659152
            __backup_content_140168006712976 = get('content', __marker)

            # <Value u"python:not append_only and content or ''" (48:32)> -> __value
            __token = 2213
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"not append_only and content or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['content'] = __value

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append(u'<textarea class="blurrable firstToFocus"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036942672
            __default_140168036942672 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (41:33)> -> __attr_name
            __token = 1813
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036944528
            __default_140168036944528 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (42:30)> -> __attr_id
            __token = 1854
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943952
            __default_140168036943952 = _DEFAULT_MARKER

            # <Substitution u'widget/cols' (43:31)> -> __attr_cols
            __token = 1897
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_cols = _static_140168208991440('path', u'widget/cols', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_cols = __quote(__attr_cols, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_cols is not None):
                __append((u' cols="%s"' % __attr_cols))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036944144
            __default_140168036944144 = _DEFAULT_MARKER

            # <Substitution u'widget/rows' (44:30)> -> __attr_rows
            __token = 1942
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_rows = _static_140168208991440('path', u'widget/rows', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_rows = __quote(__attr_rows, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_rows is not None):
                __append((u' rows="%s"' % __attr_rows))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036942480
            __default_140168036942480 = _DEFAULT_MARKER

            # <Substitution u'widget/placeholder|nothing' (45:36)> -> __attr_placeholder
            __token = 1994
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_140168208991440('path', u'widget/placeholder|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((u' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036944912
            __default_140168036944912 = _DEFAULT_MARKER

            # <Substitution u'python:test(maxlength, keypress, None)' (46:33)> -> __attr_onkeydown
            __token = 2059
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140168208991440('python', u'test(maxlength, keypress, None)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((u' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943696
            __default_140168036943696 = _DEFAULT_MARKER

            # <Substitution u'python:test(maxlength, keypress, None)' (47:30)> -> __attr_onkeyup
            __token = 2134
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140168208991440('python', u'test(maxlength, keypress, None)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((u' onkeyup="%s"' % __attr_onkeyup))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015659408
            __default_140168015659408 = _DEFAULT_MARKER

            # <Value u'content' (49:25)> -> __cache_140168015662096
            __token = 2281
            try:
                __zt_tmp = __attrs_140168036944592
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168015662096 = _static_140168208991440('path', u'content', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'content' (49:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68c84710> -> __condition
            __expression = __cache_140168015662096

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'content')
            else:
                __content = __cache_140168015662096
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</textarea>')
            if (__backup_content_140168006712976 is __marker):
                del econtext['content']
            else:
                econtext['content'] = __backup_content_140168006712976
            __append(u'\n\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036943056
            __attrs_140168036943056 = _static_140168257770128

            # <Value u'maxlength' (51:32)> -> __condition
            __token = 2342
            try:
                __zt_tmp = __attrs_140168036943056
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'maxlength', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>')
                __stream_140168037278976_count = ''
                __stream_140168036942544 = []
                __append_140168036942544 = __stream_140168036942544.append
                __append_140168036942544(u'\n                ')
                __stream_140168037278976_count = []
                __append_140168037278976_count = __stream_140168037278976_count.append

                # <Static value=<_ast.Dict object at 0x7f7b6a11bf10> name=None at 7f7b6a11bc10> -> __attrs_140168037250576
                __attrs_140168037250576 = _static_140168037252880
                __backup_remaining_140168047760976 = get('remaining', __marker)

                # <Value u"python:(int(maxlength) - content_length) + content.count('\\n')" (60:45)> -> __value
                __token = 2711
                try:
                    __zt_tmp = __attrs_140168037250576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"(int(maxlength) - content_length) + content.count('\\n')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['remaining'] = __value

                # <input ... (0:0)
                # --------------------------------------------------------
                __append_140168037278976_count(u'<input readonly="readonly" type="text"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037249424
                __default_140168037249424 = _DEFAULT_MARKER

                # <Substitution u'tcname' (61:44)> -> __attr_name
                __token = 2819
                try:
                    __zt_tmp = __attrs_140168037250576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('path', u'tcname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append_140168037278976_count((u' name="%s"' % __attr_name))
                __append_140168037278976_count(u' maxlength="4" size="4"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037251344
                __default_140168037251344 = _DEFAULT_MARKER

                # <Substitution u'remaining' (62:44)> -> __attr_value
                __token = 2871
                try:
                    __zt_tmp = __attrs_140168037250576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'remaining', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append_140168037278976_count((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037251600
                __default_140168037251600 = _DEFAULT_MARKER

                # <Substitution u'string:maxlength_${fieldName}' (63:40)> -> __attr_id
                __token = 2923
                try:
                    __zt_tmp = __attrs_140168037250576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'maxlength_${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append_140168037278976_count((u' id="%s"' % __attr_id))
                __append_140168037278976_count(u' />')
                if (__backup_remaining_140168047760976 is __marker):
                    del econtext['remaining']
                else:
                    econtext['remaining'] = __backup_remaining_140168047760976
                __append_140168036942544(u'${count}')
                __stream_140168037278976_count = ''.join(__stream_140168037278976_count)
                __append_140168036942544(u'\n                characters remaining\n            ')
                __msgid_140168036942544 = __re_whitespace(''.join(__stream_140168036942544)).strip()
                if u'label_characters_remaining':
                    __append(translate(u'label_characters_remaining', mapping={u'count': __stream_140168037278976_count, }, default=__msgid_140168036942544, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>')
            __append(u'\n\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037326352
            __attrs_140168037326352 = _static_140168257770128

            # <Value u'append_only' (67:37)> -> __condition
            __token = 3054
            try:
                __zt_tmp = __attrs_140168037326352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'append_only', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append(u'<fieldset>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037324368
                __attrs_140168037324368 = _static_140168257770128
                __backup_label_140168047812496 = get('label', __marker)

                # <Value u'widget/label' (69:40)> -> __value
                __token = 3148
                try:
                    __zt_tmp = __attrs_140168037324368
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'widget/label', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['label'] = __value

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append(u'<legend>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037324944
                __default_140168037324944 = _DEFAULT_MARKER

                # <Value u'string:HISTORY: ${label}' (70:35)> -> __cache_140168037326096
                __token = 3197
                try:
                    __zt_tmp = __attrs_140168037324368
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037326096 = _static_140168208991440('string', u'HISTORY: ${label}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'string:HISTORY: ${label}' (70:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a12d150> -> __condition
                __expression = __cache_140168037326096

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n                label\n              ')
                else:
                    __content = __cache_140168037326096
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</legend>')
                if (__backup_label_140168047812496 is __marker):
                    del econtext['label']
                else:
                    econtext['label'] = __backup_label_140168047812496
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037326544
                __attrs_140168037326544 = _static_140168257770128

                # <Value u'python:(content_length < 333)' (74:35)> -> __condition
                __token = 3343
                try:
                    __zt_tmp = __attrs_140168037326544
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'(content_length < 333)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037325648
                    __default_140168037325648 = _DEFAULT_MARKER

                    # <Value u'accessor' (75:33)> -> __cache_140168037323664
                    __token = 3410
                    try:
                        __zt_tmp = __attrs_140168037326544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037323664 = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'accessor' (75:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a12d210> -> __condition
                    __expression = __cache_140168037323664

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'content')
                    else:
                        __content = __cache_140168037323664
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6a08e950> name=None at 7f7b6a08e350> -> __attrs_140168036673360
                __attrs_140168036673360 = _static_140168036673872

                # <Value u'python:(content_length >= 333)' (77:45)> -> __condition
                __token = 3548
                try:
                    __zt_tmp = __attrs_140168036673360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'(content_length >= 333)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <textarea ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<textarea readonly="readonly"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036671632
                    __default_140168036671632 = _DEFAULT_MARKER

                    # <Substitution u'widget/cols' (79:51)> -> __attr_cols
                    __token = 3686
                    try:
                        __zt_tmp = __attrs_140168036673360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_cols = _static_140168208991440('path', u'widget/cols', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_cols = __quote(__attr_cols, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_cols is not None):
                        __append((u' cols="%s"' % __attr_cols))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036674320
                    __default_140168036674320 = _DEFAULT_MARKER

                    # <Substitution u'widget/rows' (80:50)> -> __attr_rows
                    __token = 3749
                    try:
                        __zt_tmp = __attrs_140168036673360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_rows = _static_140168208991440('path', u'widget/rows', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_rows = __quote(__attr_rows, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_rows is not None):
                        __append((u' rows="%s"' % __attr_rows))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037323152
                    __default_140168037323152 = _DEFAULT_MARKER

                    # <Value u'content' (78:43)> -> __cache_140168037325712
                    __token = 3626
                    try:
                        __zt_tmp = __attrs_140168036673360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037325712 = _static_140168208991440('path', u'content', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'content' (78:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a12d590> -> __condition
                    __expression = __cache_140168037325712

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                      content\n                    ')
                    else:
                        __content = __cache_140168037325712
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</textarea>')
                __append(u'\n            </fieldset>')
            __append(u'\n\n      ')
            if (__backup_keypress_140168037145296 is __marker):
                del econtext['keypress']
            else:
                econtext['keypress'] = __backup_keypress_140168037145296
            if (__backup_tcname_140168036659856 is __marker):
                del econtext['tcname']
            else:
                econtext['tcname'] = __backup_tcname_140168036659856
            if (__backup_maxlength_140168036459280 is __marker):
                del econtext['maxlength']
            else:
                econtext['maxlength'] = __backup_maxlength_140168036459280
            if (__backup_append_only_140168037258000 is __marker):
                del econtext['append_only']
            else:
                econtext['append_only'] = __backup_append_only_140168037258000
            if (__backup_content_length_140168016875216 is __marker):
                del econtext['content_length']
            else:
                econtext['content_length'] = __backup_content_length_140168016875216
            if (__backup_content_140168037526736 is __marker):
                del econtext['content']
            else:
                econtext['content'] = __backup_content_140168037526736
            if (__backup_content_140168047811024 is __marker):
                del econtext['content']
            else:
                econtext['content'] = __backup_content_140168047811024
            if (__backup_binary_140168037225616 is __marker):
                del econtext['binary']
            else:
                econtext['binary'] = __backup_binary_140168037225616
            if (__backup_base_140168006712272 is __marker):
                del econtext['base']
            else:
                econtext['base'] = __backup_base_140168006712272
            __append(u'\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_textarea_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_inside = econtext[u'__slot_inside'].pop()
        except:
            __slot_inside = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f7b6aa614d0> name=None at 7f7b6aa61bd0> -> __attrs_140168046976080
            __attrs_140168046976080 = _static_140168046974160
            __backup_kss_class_140168026290704 = get('kss_class', __marker)

            # <Value u"python:getKssClasses(fieldName,\n                              templateId='widgets/textarea', macro='textarea-field-view')" (17:34)> -> __value
            __token = 606
            try:
                __zt_tmp = __attrs_140168046976080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"getKssClasses(fieldName,\n                              templateId='widgets/textarea', macro='textarea-field-view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kss_class'] = __value
            __backup_uid_140168026292112 = get('uid', __marker)

            # <Value u'context/UID|nothing' (19:33)> -> __value
            __token = 762
            try:
                __zt_tmp = __attrs_140168046976080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046975312
            __default_140168046975312 = _DEFAULT_MARKER

            # <Substitution u'kss_class' (20:34)> -> __attr_class
            __token = 819
            try:
                __zt_tmp = __attrs_140168046976080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('path', u'kss_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046973200
            __default_140168046973200 = _DEFAULT_MARKER

            # <Substitution u'string:parent-fieldname-$fieldName-$uid' (21:30)> -> __attr_id
            __token = 860
            try:
                __zt_tmp = __attrs_140168046976080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n            ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015662480
                __attrs_140168015662480 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015659984
                __default_140168015659984 = _DEFAULT_MARKER

                # <Value u'accessor' (23:31)> -> __cache_140168046973392
                __token = 979
                try:
                    __zt_tmp = __attrs_140168015662480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046973392 = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'accessor' (23:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa61050> -> __condition
                __expression = __cache_140168046973392

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>textarea</span>')
                else:
                    __content = __cache_140168046973392
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n        </span>')
            if (__backup_uid_140168026292112 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168026292112
            if (__backup_kss_class_140168026290704 is __marker):
                del econtext['kss_class']
            else:
                econtext['kss_class'] = __backup_kss_class_140168026290704
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037918288
            __attrs_140168037918288 = _static_140168257770128
            __backup_kssClassesView_140168047354896 = get('kssClassesView', __marker)

            # <Value u'context/@@kss_field_decorator_view' (14:39)> -> __value
            __token = 390
            try:
                __zt_tmp = __attrs_140168037918288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@kss_field_decorator_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kssClassesView'] = __value
            __backup_getKssClasses_140168026290640 = get('getKssClasses', __marker)

            # <Value u'nocall:kssClassesView/getKssClassesInlineEditable' (15:37)> -> __value
            __token = 463
            try:
                __zt_tmp = __attrs_140168037918288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('nocall', u'kssClassesView/getKssClassesInlineEditable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['getKssClasses'] = __value
            __append(u'\n        ')
            __token = None
            render_textarea_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    ')
            if (__backup_getKssClasses_140168026290640 is __marker):
                del econtext['getKssClasses']
            else:
                econtext['getKssClasses'] = __backup_getKssClasses_140168026290640
            if (__backup_kssClassesView_140168047354896 is __marker):
                del econtext['kssClassesView']
            else:
                econtext['kssClassesView'] = __backup_kssClassesView_140168047354896
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

            # <Static value=<_ast.Dict object at 0x7f7b6aaa32d0> name=None at 7f7b6aaa3310> -> __attrs_140168037919888
            __attrs_140168037919888 = _static_140168047243984
            __previous_i18n_domain_140168037918736 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037917584
            __attrs_140168037917584 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037917456
            __attrs_140168037917456 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title></head>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037919440
            __attrs_140168037919440 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- TextArea Widgets -->\n\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_area_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_area_format(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168037918736
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_area_format': render_area_format, u'render_search': render_search, u'render_edit': render_edit, u'render_area_edit': render_area_edit, u'render_textarea_field_view': render_textarea_field_view, u'render_view': render_view, 'render': render, }