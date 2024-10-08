# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/skins/bika/bika_widgets/selection.pt'

__tokens = {1613: (u'python:field.Vocabulary(context)', 38, 42), 1687: (u' python:len(vocab', 39, 40), 1755: (u'w context/@@at_selection_widg', 40, 48), 1831: (u'on python:selectionview.getSelected(vocab, val', 41, 43), 1921: (u'mat python:widget.fo', 42, 39), 1986: (u"python:(vlen &lt; 4 and format == 'flex') or (format == 'radi", 44, 37), 2093: (u'fieldName', 45, 41), 2211: (u'not: widget/render_own_label | nothing', 49, 40), 2322: (u'python:widget.Label(here)', 50, 43), 2493: (u'field/required', 53, 45), 2740: (u'python:widget.Description(here)', 57, 53), 2886: (u'string:${fieldName}_help', 59, 48), 2825: (u'description', 58, 52), 3096: (u'vocab', 65, 45), 3259: (u'fieldName', 69, 52), 3319: (u' string:${fieldName}_${repeat/item/number', 70, 49), 3416: (u"d python:item in selection and 'checked' or No", 71, 53), 3516: (u'ue i', 72, 50), 3734: (u'string:${fieldName}_${repeat/item/number}', 77, 51), 3605: (u'python:vocab.getValue(item)', 75, 44), 3915: (u"python:(vlen >= 4 and format == 'flex') or (format in ('select', 'pulldown'))", 85, 42), 4089: (u'not: widget/render_own_label | nothing', 89, 42), 4197: (u'python:fieldName', 90, 47), 4259: (u'python:widget.Label(here)', 91, 43), 4430: (u'field/required', 94, 45), 4677: (u'python:widget.Description(here)', 98, 53), 4823: (u'string:${fieldName}_help', 100, 48), 4762: (u'description', 99, 52), 5039: (u'fieldName', 106, 49), 5096: (u' fieldNam', 107, 46), 5160: (u'vocab', 109, 49), 5221: (u'item', 110, 54), 5283: (u" python:item in selection and 'selected' or Non", 111, 56), 5378: (u'python:vocab.getValue(item)', 112, 45), 1474: (u'field_macro|context/widgets/field/macros/edit', 35, 30), 1474: (u'field_macro|context/widgets/field/macros/edit', 35, 30), 5696: (u'context/widgets/selection/macros/edit', 127, 30), 5696: (u'context/widgets/selection/macros/edit', 127, 30), 714: (u"python:getKssClasses(fieldName,\n                              templateId='widgets/selection', macro='selection-field-view')", 19, 34), 872: (u' context/UID|nothin', 21, 33), 929: (u'kss_class', 22, 34), 970: (u' string:parent-fieldname-$fieldName-$ui', 23, 30), 1092: (u'python:field.Vocabulary(context)', 25, 34), 1159: (u' python:accessor(', 26, 33), 1213: (u'y python:context.displayValue(vocab, value, widge', 27, 34), 1351: (u'display', 29, 39), 497: (u'context/@@kss_field_decorator_view', 16, 39), 570: (u' nocall:kssClassesView/getKssClassesInlineEditabl', 17, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168026312144 = u'edit'
_static_140168046938960 = {u'selected': u"python:item in selection and 'selected' or None", u'value': u'item', }
_static_140168026309584 = u'edit'
_static_140168047007952 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168037143376 = {u'for': u'string:${fieldName}_${repeat/item/number}', }
_static_140168036762320 = {u'checked': u"python:item in selection and 'checked' or None", u'name': u'fieldName', u'value': u'item', u'class': u'noborder blurrable', u'type': u'radio', u'id': u'string:${fieldName}_${repeat/item/number}', }
_static_140168026654992 = {u'class': u'kss_class', u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168036459984 = {u'class': u'required', u'title': u'Required', }
_static_140168257770128 = {}
_static_140168047286544 = {u'id': u'fieldName', }
_static_140168037145232 = {u'class': u'formQuestion', u'for': u'python:fieldName', }
_static_140168015867088 = {u'class': u'formHelp', u'id': u'string:${fieldName}_help', }
_static_140168037145424 = {u'name': u'fieldName', u'id': u'fieldName', }
_static_140168036461456 = {u'class': u'formHelp', u'id': u'string:${fieldName}_help', }
_static_140168015698512 = {u'class': u'formQuestion label', }
_static_140168015865616 = {u'class': u'required', u'title': u'Required', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026653968
            __attrs_140168026653968 = _static_140168257770128
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026309136
            __attrs_140168026309136 = _static_140168257770128
            __backup_macroname_140168055940032 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b696ac3d0> name=None at 7f7b696ac6d0> -> __value
            __value = _static_140168026309584
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026311312
                __attrs_140168026311312 = _static_140168257770128
                __backup_vocab_140168026653328 = get('vocab', __marker)

                # <Value u'python:field.Vocabulary(context)' (38:42)> -> __value
                __token = 1613
                try:
                    __zt_tmp = __attrs_140168026311312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'field.Vocabulary(context)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['vocab'] = __value
                __backup_vlen_140168026652880 = get('vlen', __marker)

                # <Value u'python:len(vocab)' (39:40)> -> __value
                __token = 1687
                try:
                    __zt_tmp = __attrs_140168026311312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'len(vocab)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['vlen'] = __value
                __backup_selectionview_140168026656656 = get('selectionview', __marker)

                # <Value u'context/@@at_selection_widget' (40:48)> -> __value
                __token = 1755
                try:
                    __zt_tmp = __attrs_140168026311312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/@@at_selection_widget', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['selectionview'] = __value
                __backup_selection_140168026652944 = get('selection', __marker)

                # <Value u'python:selectionview.getSelected(vocab, value)' (41:43)> -> __value
                __token = 1831
                try:
                    __zt_tmp = __attrs_140168026311312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'selectionview.getSelected(vocab, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['selection'] = __value
                __backup_format_140168026312272 = get('format', __marker)

                # <Value u'python:widget.format' (42:39)> -> __value
                __token = 1921
                try:
                    __zt_tmp = __attrs_140168026311312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'widget.format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['format'] = __value
                __append(u'\n\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaad910> name=None at 7f7b696ac750> -> __attrs_140168015697872
                __attrs_140168015697872 = _static_140168047286544

                # <Value u"python:(vlen < 4 and format == 'flex') or (format == 'radio')" (44:37)> -> __condition
                __token = 1986
                try:
                    __zt_tmp = __attrs_140168015697872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u"(vlen < 4 and format == 'flex') or (format == 'radio')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015699152
                    __default_140168015699152 = _DEFAULT_MARKER

                    # <Substitution u'fieldName' (45:41)> -> __attr_id
                    __token = 2093
                    try:
                        __zt_tmp = __attrs_140168015697872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n\n                    <!-- Radio when the vocab is short < 4 -->\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b68c8da50> name=None at 7f7b68c8dc90> -> __attrs_140168015696848
                    __attrs_140168015696848 = _static_140168015698512

                    # <Value u'not: widget/render_own_label | nothing' (49:40)> -> __condition
                    __token = 2211
                    try:
                        __zt_tmp = __attrs_140168015696848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u' widget/render_own_label | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="formQuestion label">\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015697296
                        __attrs_140168015697296 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015698064
                        __default_140168015698064 = _DEFAULT_MARKER

                        # <Value u'python:widget.Label(here)' (50:43)> -> __cache_140168015698256
                        __token = 2322
                        try:
                            __zt_tmp = __attrs_140168015697296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168015698256 = _static_140168208991440('python', u'widget.Label(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:widget.Label(here)' (50:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68c8d610> -> __condition
                        __expression = __cache_140168015698256

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span />')
                        else:
                            __content = __cache_140168015698256
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a05a5d0> name=None at 7f7b6a05a9d0> -> __attrs_140168036458960
                        __attrs_140168036458960 = _static_140168036459984

                        # <Value u'field/required' (53:45)> -> __condition
                        __token = 2493
                        try:
                            __zt_tmp = __attrs_140168036458960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('path', u'field/required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036459344
                            __default_140168036459344 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b6a05a290> at 7f7b6a05a590> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'>&nbsp;</span>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a05ab90> name=None at 7f7b6a05aa10> -> __attrs_140168036459408
                        __attrs_140168036459408 = _static_140168036461456
                        __backup_description_140168015698384 = get('description', __marker)

                        # <Value u'python:widget.Description(here)' (57:53)> -> __value
                        __token = 2740
                        try:
                            __zt_tmp = __attrs_140168036459408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'widget.Description(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['description'] = __value

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="formHelp"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036459664
                        __default_140168036459664 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}_help' (59:48)> -> __attr_id
                        __token = 2886
                        try:
                            __zt_tmp = __attrs_140168036459408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}_help', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036460944
                        __default_140168036460944 = _DEFAULT_MARKER

                        # <Value u'description' (58:52)> -> __cache_140168036462352
                        __token = 2825
                        try:
                            __zt_tmp = __attrs_140168036459408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036462352 = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'description' (58:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a05aed0> -> __condition
                        __expression = __cache_140168036462352

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                          Help\n                        ')
                        else:
                            __content = __cache_140168036462352
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                        if (__backup_description_140168015698384 is __marker):
                            del econtext['description']
                        else:
                            econtext['description'] = __backup_description_140168015698384
                        __append(u'\n                    </div>')
                    __append(u'\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036765456
                    __attrs_140168036765456 = _static_140168257770128
                    __backup_item_140168015699920 = get('item', __marker)

                    # <Value u'vocab' (65:45)> -> __iterator
                    __token = 3096
                    try:
                        __zt_tmp = __attrs_140168036765456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'vocab', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168036763984, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append(u'\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a0a42d0> name=None at 7f7b6a0a4050> -> __attrs_140168036764944
                        __attrs_140168036764944 = _static_140168036762320

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="noborder blurrable" type="radio"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036765264
                        __default_140168036765264 = _DEFAULT_MARKER

                        # <Substitution u'fieldName' (69:52)> -> __attr_name
                        __token = 3259
                        try:
                            __zt_tmp = __attrs_140168036764944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036765392
                        __default_140168036765392 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}_${repeat/item/number}' (70:49)> -> __attr_id
                        __token = 3319
                        try:
                            __zt_tmp = __attrs_140168036764944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}_${repeat/item/number}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036762000
                        __default_140168036762000 = _DEFAULT_MARKER

                        # <Boolean u"python:item in selection and 'checked' or None" (71:53)> -> __attr_checked
                        __token = 3416
                        try:
                            __zt_tmp = __attrs_140168036764944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140168208991440('python', u"item in selection and 'checked' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = u'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((u' checked="%s"' % __attr_checked))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036765200
                        __default_140168036765200 = _DEFAULT_MARKER

                        # <Substitution u'item' (72:50)> -> __attr_value
                        __token = 3516
                        try:
                            __zt_tmp = __attrs_140168036764944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' />\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a101350> name=None at 7f7b6a1019d0> -> __attrs_140168037144016
                        __attrs_140168037144016 = _static_140168037143376

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<label')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037142928
                        __default_140168037142928 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}_${repeat/item/number}' (77:51)> -> __attr_for
                        __token = 3734
                        try:
                            __zt_tmp = __attrs_140168037144016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_for = _static_140168208991440('string', u'${fieldName}_${repeat/item/number}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_for is not None):
                            __append((u' for="%s"' % __attr_for))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036762960
                        __default_140168036762960 = _DEFAULT_MARKER

                        # <Value u'python:vocab.getValue(item)' (75:44)> -> __cache_140168036765008
                        __token = 3605
                        try:
                            __zt_tmp = __attrs_140168037144016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036765008 = _static_140168208991440('python', u'vocab.getValue(item)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:vocab.getValue(item)' (75:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a0a4690> -> __condition
                        __expression = __cache_140168036765008

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168036765008
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</label>\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037144400
                        __attrs_140168037144400 = _static_140168257770128

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<br />\n\n                    ')
                        ____index_140168036763984 -= 1
                        if (____index_140168036763984 > 0):
                            __append('')
                    if (__backup_item_140168015699920 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168015699920
                    __append(u'\n\n                </span>')
                __append(u'\n\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015697168
                __attrs_140168015697168 = _static_140168257770128

                # <Value u"python:(vlen >= 4 and format == 'flex') or (format in ('select', 'pulldown'))" (85:42)> -> __condition
                __token = 3915
                try:
                    __zt_tmp = __attrs_140168015697168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u"(vlen >= 4 and format == 'flex') or (format in ('select', 'pulldown'))", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n                    <!-- Pulldown when longer -->\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a101a90> name=None at 7f7b6a101210> -> __attrs_140168037146256
                    __attrs_140168037146256 = _static_140168037145232

                    # <Value u'not: widget/render_own_label | nothing' (89:42)> -> __condition
                    __token = 4089
                    try:
                        __zt_tmp = __attrs_140168037146256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u' widget/render_own_label | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<label class="formQuestion"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037142736
                        __default_140168037142736 = _DEFAULT_MARKER

                        # <Substitution u'python:fieldName' (90:47)> -> __attr_for
                        __token = 4197
                        try:
                            __zt_tmp = __attrs_140168037146256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_for = _static_140168208991440('python', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_for is not None):
                            __append((u' for="%s"' % __attr_for))
                        __append(u'>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015867344
                        __attrs_140168015867344 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015865744
                        __default_140168015865744 = _DEFAULT_MARKER

                        # <Value u'python:widget.Label(here)' (91:43)> -> __cache_140168037442192
                        __token = 4259
                        try:
                            __zt_tmp = __attrs_140168015867344
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168037442192 = _static_140168208991440('python', u'widget.Label(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:widget.Label(here)' (91:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68cb6d50> -> __condition
                        __expression = __cache_140168037442192

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span />')
                        else:
                            __content = __cache_140168037442192
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b68cb6710> name=None at 7f7b68cb6810> -> __attrs_140168015864720
                        __attrs_140168015864720 = _static_140168015865616

                        # <Value u'field/required' (94:45)> -> __condition
                        __token = 4430
                        try:
                            __zt_tmp = __attrs_140168015864720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('path', u'field/required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015866704
                            __default_140168015866704 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b68cb6b10> at 7f7b68cb6a90> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'>&nbsp;</span>')
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b68cb6cd0> name=None at 7f7b68cb62d0> -> __attrs_140168046937424
                        __attrs_140168046937424 = _static_140168015867088
                        __backup_description_140168026309456 = get('description', __marker)

                        # <Value u'python:widget.Description(here)' (98:53)> -> __value
                        __token = 4677
                        try:
                            __zt_tmp = __attrs_140168046937424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'widget.Description(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['description'] = __value

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="formHelp"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046937808
                        __default_140168046937808 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}_help' (100:48)> -> __attr_id
                        __token = 4823
                        try:
                            __zt_tmp = __attrs_140168046937424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}_help', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015866768
                        __default_140168015866768 = _DEFAULT_MARKER

                        # <Value u'description' (99:52)> -> __cache_140168015867280
                        __token = 4762
                        try:
                            __zt_tmp = __attrs_140168046937424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168015867280 = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'description' (99:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68cb6f90> -> __condition
                        __expression = __cache_140168015867280

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                          Help\n                        ')
                        else:
                            __content = __cache_140168015867280
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                        if (__backup_description_140168026309456 is __marker):
                            del econtext['description']
                        else:
                            econtext['description'] = __backup_description_140168026309456
                        __append(u'\n                    </label>')
                    __append(u'\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a101b50> name=None at 7f7b6a101f50> -> __attrs_140168046939280
                    __attrs_140168046939280 = _static_140168037145424

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046937552
                    __default_140168046937552 = _DEFAULT_MARKER

                    # <Substitution u'fieldName' (106:49)> -> __attr_name
                    __token = 5039
                    try:
                        __zt_tmp = __attrs_140168046939280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046936656
                    __default_140168046936656 = _DEFAULT_MARKER

                    # <Substitution u'fieldName' (107:46)> -> __attr_id
                    __token = 5096
                    try:
                        __zt_tmp = __attrs_140168046939280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa58b50> name=None at 7f7b6aa589d0> -> __attrs_140168037920016
                    __attrs_140168037920016 = _static_140168046938960
                    __backup_item_140168036461648 = get('item', __marker)

                    # <Value u'vocab' (109:49)> -> __iterator
                    __token = 5160
                    try:
                        __zt_tmp = __attrs_140168037920016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'vocab', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168037918992, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037919632
                        __default_140168037919632 = _DEFAULT_MARKER

                        # <Substitution u'item' (110:54)> -> __attr_value
                        __token = 5221
                        try:
                            __zt_tmp = __attrs_140168037920016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037918224
                        __default_140168037918224 = _DEFAULT_MARKER

                        # <Boolean u"python:item in selection and 'selected' or None" (111:56)> -> __attr_selected
                        __token = 5283
                        try:
                            __zt_tmp = __attrs_140168037920016
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

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046940048
                        __default_140168046940048 = _DEFAULT_MARKER

                        # <Value u'python:vocab.getValue(item)' (112:45)> -> __cache_140168046939216
                        __token = 5378
                        try:
                            __zt_tmp = __attrs_140168037920016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168046939216 = _static_140168208991440('python', u'vocab.getValue(item)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:vocab.getValue(item)' (112:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa58950> -> __condition
                        __expression = __cache_140168046939216

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168046939216
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>')
                        ____index_140168037918992 -= 1
                        if (____index_140168037918992 > 0):
                            __append('\n                        ')
                    if (__backup_item_140168036461648 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168036461648
                    __append(u'\n\n                    </select>\n\n                ')
                __append(u'\n\n            ')
                if (__backup_format_140168026312272 is __marker):
                    del econtext['format']
                else:
                    econtext['format'] = __backup_format_140168026312272
                if (__backup_selection_140168026652944 is __marker):
                    del econtext['selection']
                else:
                    econtext['selection'] = __backup_selection_140168026652944
                if (__backup_selectionview_140168026656656 is __marker):
                    del econtext['selectionview']
                else:
                    econtext['selectionview'] = __backup_selectionview_140168026656656
                if (__backup_vlen_140168026652880 is __marker):
                    del econtext['vlen']
                else:
                    econtext['vlen'] = __backup_vlen_140168026652880
                if (__backup_vocab_140168026653328 is __marker):
                    del econtext['vocab']
                else:
                    econtext['vocab'] = __backup_vocab_140168026653328
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro|context/widgets/field/macros/edit' (35:30)> -> __macro
            __token = 1474
            try:
                __zt_tmp = __attrs_140168026309136
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro|context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1474
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055940032 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055940032
            __append(u'\n\n    ')
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026309392
            __attrs_140168026309392 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015697360
            __attrs_140168015697360 = _static_140168257770128
            __backup_macroname_140168055941392 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b696acdd0> name=None at 7f7b68c8d8d0> -> __value
            __value = _static_140168026312144
            econtext['macroname'] = __value

            # <Value u'context/widgets/selection/macros/edit' (127:30)> -> __macro
            __token = 5696
            try:
                __zt_tmp = __attrs_140168015697360
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/selection/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 5696
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055941392 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055941392
            __append(u'\n    </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_selection_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b69700910> name=None at 7f7b69700890> -> __attrs_140168026653776
            __attrs_140168026653776 = _static_140168026654992
            __backup_kss_class_140168026366032 = get('kss_class', __marker)

            # <Value u"python:getKssClasses(fieldName,\n                              templateId='widgets/selection', macro='selection-field-view')" (19:34)> -> __value
            __token = 714
            try:
                __zt_tmp = __attrs_140168026653776
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"getKssClasses(fieldName,\n                              templateId='widgets/selection', macro='selection-field-view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kss_class'] = __value
            __backup_uid_140168026367568 = get('uid', __marker)

            # <Value u'context/UID|nothing' (21:33)> -> __value
            __token = 872
            try:
                __zt_tmp = __attrs_140168026653776
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026655120
            __default_140168026655120 = _DEFAULT_MARKER

            # <Substitution u'kss_class' (22:34)> -> __attr_class
            __token = 929
            try:
                __zt_tmp = __attrs_140168026653776
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('path', u'kss_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026654096
            __default_140168026654096 = _DEFAULT_MARKER

            # <Substitution u'string:parent-fieldname-$fieldName-$uid' (23:30)> -> __attr_id
            __token = 970
            try:
                __zt_tmp = __attrs_140168026653776
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n            ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026654224
                __attrs_140168026654224 = _static_140168257770128
                __backup_vocab_140168026653200 = get('vocab', __marker)

                # <Value u'python:field.Vocabulary(context)' (25:34)> -> __value
                __token = 1092
                try:
                    __zt_tmp = __attrs_140168026654224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'field.Vocabulary(context)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['vocab'] = __value
                __backup_value_140168026653520 = get('value', __marker)

                # <Value u'python:accessor()' (26:33)> -> __value
                __token = 1159
                try:
                    __zt_tmp = __attrs_140168026654224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'accessor()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value
                __backup_display_140168026655760 = get('display', __marker)

                # <Value u'python:context.displayValue(vocab, value, widget)' (27:34)> -> __value
                __token = 1213
                try:
                    __zt_tmp = __attrs_140168026654224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'context.displayValue(vocab, value, widget)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['display'] = __value

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026654928
                __default_140168026654928 = _DEFAULT_MARKER

                # <Value u'display' (29:39)> -> __cache_140168026654544
                __token = 1351
                try:
                    __zt_tmp = __attrs_140168026654224
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168026654544 = _static_140168208991440('path', u'display', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'display' (29:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b69700b50> -> __condition
                __expression = __cache_140168026654544

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span />')
                else:
                    __content = __cache_140168026654544
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                if (__backup_display_140168026655760 is __marker):
                    del econtext['display']
                else:
                    econtext['display'] = __backup_display_140168026655760
                if (__backup_value_140168026653520 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168026653520
                if (__backup_vocab_140168026653200 is __marker):
                    del econtext['vocab']
                else:
                    econtext['vocab'] = __backup_vocab_140168026653200
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n        </span>')
            if (__backup_uid_140168026367568 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168026367568
            if (__backup_kss_class_140168026366032 is __marker):
                del econtext['kss_class']
            else:
                econtext['kss_class'] = __backup_kss_class_140168026366032
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026367184
            __attrs_140168026367184 = _static_140168257770128
            __backup_kssClassesView_140168047006224 = get('kssClassesView', __marker)

            # <Value u'context/@@kss_field_decorator_view' (16:39)> -> __value
            __token = 497
            try:
                __zt_tmp = __attrs_140168026367184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@kss_field_decorator_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kssClassesView'] = __value
            __backup_getKssClasses_140168036940816 = get('getKssClasses', __marker)

            # <Value u'nocall:kssClassesView/getKssClassesInlineEditable' (17:37)> -> __value
            __token = 570
            try:
                __zt_tmp = __attrs_140168026367184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('nocall', u'kssClassesView/getKssClassesInlineEditable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['getKssClasses'] = __value
            __append(u'\n        ')
            __token = None
            render_selection_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    ')
            if (__backup_getKssClasses_140168036940816 is __marker):
                del econtext['getKssClasses']
            else:
                econtext['getKssClasses'] = __backup_getKssClasses_140168036940816
            if (__backup_kssClassesView_140168047006224 is __marker):
                del econtext['kssClassesView']
            else:
                econtext['kssClassesView'] = __backup_kssClassesView_140168047006224
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

            # <Static value=<_ast.Dict object at 0x7f7b6aa698d0> name=None at 7f7b6aa69ad0> -> __attrs_140168047008400
            __attrs_140168047008400 = _static_140168047007952
            __previous_i18n_domain_140168047006544 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n/home/campbell/Plone/zeocluster/parts/omelette/Products/Archetypes/skins/archetypes/widgets/selection.pt\n')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047008016
            __attrs_140168047008016 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047009104
            __attrs_140168047009104 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title>\n</head>\n\n')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047007760
            __attrs_140168047007760 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- Selection Widgets -->\n\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n</body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168047006544
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_selection_field_view': render_selection_field_view, u'render_view': render_view, 'render': render, }