# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/skins/senaite_templates/senaite_widgets/referencewidget.pt'

__tokens = {1347: (u'python:field.getEditAccessor(here)() or []', 33, 32), 1430: (u' python:here.session_restore_value(fieldName, value', 34, 39), 1521: (u'e python:request.get(fieldName, session_valu', 35, 37), 1598: (u'ue python:cached_value or va', 36, 29), 1662: (u'red field/required|not', 37, 31), 1720: (u"ired python: required and 'required' or", 38, 30), 1795: (u'or_id python:errors.get(fiel', 39, 29), 1862: (u'domain field/widget/i18n_domain|context/i18n_domain|strin', 40, 31), 1967: (u'not: widget/render_own_label | nothing', 42, 36), 2083: (u'python:fieldName', 44, 37), 2133: (u'python:widget.Label(here)', 45, 31), 2267: (u'field/required', 48, 33), 2467: (u'python:widget.Description(here)', 52, 42), 2591: (u'string:${fieldName}_help', 54, 37), 2541: (u'description', 53, 41), 2801: (u'python:field.widget.get_input_widget_attributes(context, field, value)', 62, 38), 3199: (u'   python:widget_at', 66, 26), 2906: (u'python:fieldName', 63, 32), 2958: (u" python: test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + widget.klas", 64, 34), 3139: (u"d python:required and '1' or '", 65, 41), 3339: (u'required', 70, 50), 3404: (u'error_id', 71, 48), 3560: (u'context/widgets/string/macros/edit', 77, 28), 3560: (u'context/widgets/string/macros/edit', 77, 28), 443: (u'python:accessor()', 12, 29), 489: (u' python:widget.get_value(context, field, value', 13, 27), 616: (u'refs', 15, 30), 688: (u'python:widget.render_reference(context, field, ref)', 16, 42), 776: (u'python:rendered', 17, 34), 903: (u'rendered', 19, 45), 970: (u'python:not rendered', 21, 34), 1056: (u'string:broken reference ${ref}', 22, 44), 1123: (u'ref', 23, 35), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168046848912 = {u'class': u'formQuestion', u'for': u'python:fieldName', }
_static_140168046859280 = {u'class': u'p-1 mb-1 mr-1 bg-light border rounded', }
_static_140168036700496 = {u'class': u'formHelp', u'id': u'string:${fieldName}_help', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168016766672 = {u'title': u'string:broken reference ${ref}', }
_static_140168047244816 = set([])
_static_140168025889744 = {u'class': u'fieldErrorBox', }
_static_140168016765008 = {u'class': u'text-danger', }
_static_140168046860560 = {u'class': u'd-inline-block', }
_static_140168257770128 = {}
_static_140168037627792 = u'master'
_static_140168047172048 = {u'class': u'required', u'title': u'Required', }
_static_140168047806672 = u'edit'
_static_140168026308688 = {u'class': u'list-unstyled d-table-row', }
_static_140168047172816 = {u'data-required': u"python:required and '1' or '0'", u'id': u'python:fieldName', u'class': u"python: test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + widget.klass", }
_static_140168025890128 = {u'class': u'fieldErrorBox', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026312336
            __attrs_140168026312336 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046862032
            __attrs_140168046862032 = _static_140168257770128
            __backup_value_140168026221328 = get('value', __marker)

            # <Value u'python:field.getEditAccessor(here)() or []' (33:32)> -> __value
            __token = 1347
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)() or []', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_session_value_140168037968144 = get('session_value', __marker)

            # <Value u'python:here.session_restore_value(fieldName, value)' (34:39)> -> __value
            __token = 1430
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'here.session_restore_value(fieldName, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['session_value'] = __value
            __backup_cached_value_140168047000400 = get('cached_value', __marker)

            # <Value u'python:request.get(fieldName, session_value)' (35:37)> -> __value
            __token = 1521
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'request.get(fieldName, session_value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['cached_value'] = __value
            __backup_value_140168047372624 = get('value', __marker)

            # <Value u'python:cached_value or value' (36:29)> -> __value
            __token = 1598
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'cached_value or value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_required_140168047530384 = get('required', __marker)

            # <Value u'field/required|nothing' (37:31)> -> __value
            __token = 1662
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/required|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_required_140168026344336 = get('required', __marker)

            # <Value u"python: required and 'required' or None" (38:30)> -> __value
            __token = 1720
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" required and 'required' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_error_id_140168046999376 = get('error_id', __marker)

            # <Value u'python:errors.get(fieldName)' (39:29)> -> __value
            __token = 1795
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'errors.get(fieldName)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['error_id'] = __value
            __backup_i18n_domain_140168047358800 = get('i18n_domain', __marker)

            # <Value u'field/widget/i18n_domain|context/i18n_domain|string:plone' (40:31)> -> __value
            __token = 1862
            try:
                __zt_tmp = __attrs_140168046862032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/widget/i18n_domain|context/i18n_domain|string:plone', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['i18n_domain'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046848464
            __attrs_140168046848464 = _static_140168257770128

            # <Value u'not: widget/render_own_label | nothing' (42:36)> -> __condition
            __token = 1967
            try:
                __zt_tmp = __attrs_140168046848464
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('not', u' widget/render_own_label | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa42b90> name=None at 7f7b6aa42450> -> __attrs_140168047171792
                __attrs_140168047171792 = _static_140168046848912

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label class="formQuestion"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047172432
                __default_140168047172432 = _DEFAULT_MARKER

                # <Substitution u'python:fieldName' (44:37)> -> __attr_for
                __token = 2083
                try:
                    __zt_tmp = __attrs_140168047171792
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140168208991440('python', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u'>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047170256
                __attrs_140168047170256 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047170704
                __default_140168047170704 = _DEFAULT_MARKER

                # <Value u'python:widget.Label(here)' (45:31)> -> __cache_140168047172688
                __token = 2133
                try:
                    __zt_tmp = __attrs_140168047170256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047172688 = _static_140168208991440('python', u'widget.Label(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:widget.Label(here)' (45:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa91710> -> __condition
                __expression = __cache_140168047172688

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span />')
                else:
                    __content = __cache_140168047172688
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa919d0> name=None at 7f7b6aa91390> -> __attrs_140168036702416
                __attrs_140168036702416 = _static_140168047172048

                # <Value u'field/required' (48:33)> -> __condition
                __token = 2267
                try:
                    __zt_tmp = __attrs_140168036702416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'field/required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="required"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036701776
                    __default_140168036701776 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b6aa914d0> at 7f7b6aa91410> -> __attr_title
                    __attr_title = u'Required'
                    __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>&nbsp;</span>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a095150> name=None at 7f7b6a095410> -> __attrs_140168036702800
                __attrs_140168036702800 = _static_140168036700496
                __backup_description_140168026221968 = get('description', __marker)

                # <Value u'python:widget.Description(here)' (52:42)> -> __value
                __token = 2467
                try:
                    __zt_tmp = __attrs_140168036702800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'widget.Description(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['description'] = __value

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="formHelp"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036703760
                __default_140168036703760 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_help' (54:37)> -> __attr_id
                __token = 2591
                try:
                    __zt_tmp = __attrs_140168036702800
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${fieldName}_help', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036700752
                __default_140168036700752 = _DEFAULT_MARKER

                # <Value u'description' (53:41)> -> __cache_140168036702608
                __token = 2541
                try:
                    __zt_tmp = __attrs_140168036702800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168036702608 = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'description' (53:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a095fd0> -> __condition
                __expression = __cache_140168036702608

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n              Help\n            ')
                else:
                    __content = __cache_140168036702608
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>')
                if (__backup_description_140168026221968 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_140168026221968
                __append(u'\n          </label>\n        ')
            __append(u'\n\n        <!-- Reference -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa91cd0> name=None at 7f7b6aa915d0> -> __attrs_140168025890320
            __attrs_140168025890320 = _static_140168047172816
            __backup_widget_attrs_140168026327312 = get('widget_attrs', __marker)

            # <Value u'python:field.widget.get_input_widget_attributes(context, field, value)' (62:38)> -> __value
            __token = 2801
            try:
                __zt_tmp = __attrs_140168025890320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.widget.get_input_widget_attributes(context, field, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['widget_attrs'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Value u'python:widget_attrs' (66:26)> -> __cache_140168025887568
            __token = 3199
            try:
                __zt_tmp = __attrs_140168025890320
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168025887568 = _static_140168208991440('python', u'widget_attrs', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036702992
            __default_140168036702992 = _DEFAULT_MARKER

            # <Substitution u'python:fieldName' (63:32)> -> __attr_id
            __token = 2906
            try:
                __zt_tmp = __attrs_140168025890320
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('python', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_id is not None) and (u'id' not in __chain(__cache_140168025887568))):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036701968
            __default_140168036701968 = _DEFAULT_MARKER

            # <Substitution u"python: test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + widget.klass" (64:34)> -> __attr_class
            __token = 2958
            try:
                __zt_tmp = __attrs_140168025890320
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('python', u" test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + widget.klass", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and (u'class' not in __chain(__cache_140168025887568))):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025888464
            __default_140168025888464 = _DEFAULT_MARKER

            # <Substitution u"python:required and '1' or '0'" (65:41)> -> __attr_data_required
            __token = 3139
            try:
                __zt_tmp = __attrs_140168025890320
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_required = _static_140168208991440('python', u"required and '1' or '0'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_required = __quote(__attr_data_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_data_required is not None) and (u'data-required' not in __chain(__cache_140168025887568))):
                __append((u' data-required="%s"' % __attr_data_required))
            __attr_140168025888848 = __cache_140168025887568
            for (name, value, ) in __attr_140168025888848.items():
                if ((name not in _static_140168047244816) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'>\n          <!-- ReactJS controlled component -->\n        </div>')
            if (__backup_widget_attrs_140168026327312 is __marker):
                del econtext['widget_attrs']
            else:
                econtext['widget_attrs'] = __backup_widget_attrs_140168026327312
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b69645bd0> name=None at 7f7b69645650> -> __attrs_140168025888400
            __attrs_140168025888400 = _static_140168025889744

            # <Value u'required' (70:50)> -> __condition
            __token = 3339
            try:
                __zt_tmp = __attrs_140168025888400
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="fieldErrorBox"></div>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b69645d50> name=None at 7f7b696457d0> -> __attrs_140168047808208
            __attrs_140168047808208 = _static_140168025890128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="fieldErrorBox">')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025889616
            __default_140168025889616 = _DEFAULT_MARKER

            # <Value u'error_id' (71:48)> -> __cache_140168025889872
            __token = 3404
            try:
                __zt_tmp = __attrs_140168047808208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168025889872 = _static_140168208991440('path', u'error_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'error_id' (71:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b69645c10> -> __condition
            __expression = __cache_140168025889872

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168025889872
                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n      ')
            if (__backup_i18n_domain_140168047358800 is __marker):
                del econtext['i18n_domain']
            else:
                econtext['i18n_domain'] = __backup_i18n_domain_140168047358800
            if (__backup_error_id_140168046999376 is __marker):
                del econtext['error_id']
            else:
                econtext['error_id'] = __backup_error_id_140168046999376
            if (__backup_required_140168026344336 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168026344336
            if (__backup_required_140168047530384 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168047530384
            if (__backup_value_140168047372624 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168047372624
            if (__backup_cached_value_140168047000400 is __marker):
                del econtext['cached_value']
            else:
                econtext['cached_value'] = __backup_cached_value_140168047000400
            if (__backup_session_value_140168037968144 is __marker):
                del econtext['session_value']
            else:
                econtext['session_value'] = __backup_session_value_140168037968144
            if (__backup_value_140168026221328 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168026221328
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046858448
            __attrs_140168046858448 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047807312
            __attrs_140168047807312 = _static_140168257770128
            __backup_macroname_140168057026032 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6ab2c8d0> name=None at 7f7b6ab2cc90> -> __value
            __value = _static_140168047806672
            econtext['macroname'] = __value

            # <Value u'context/widgets/string/macros/edit' (77:28)> -> __macro
            __token = 3560
            try:
                __zt_tmp = __attrs_140168047807312
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 3560
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057026032 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057026032
            __append(u'\n    ')
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
            __slot_inside = econtext[u'__slot_inside'].pop()
        except:
            __slot_inside = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026310736
            __attrs_140168026310736 = _static_140168257770128
            __append(u'\n      ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026310096
                __attrs_140168026310096 = _static_140168257770128
                __backup_value_140168046982480 = get('value', __marker)

                # <Value u'python:accessor()' (12:29)> -> __value
                __token = 443
                try:
                    __zt_tmp = __attrs_140168026310096
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'accessor()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value
                __backup_refs_140168037564880 = get('refs', __marker)

                # <Value u'python:widget.get_value(context, field, value)' (13:27)> -> __value
                __token = 489
                try:
                    __zt_tmp = __attrs_140168026310096
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'widget.get_value(context, field, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['refs'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b696ac050> name=None at 7f7b696aca90> -> __attrs_140168026309200
                __attrs_140168026309200 = _static_140168026308688

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="list-unstyled d-table-row">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa45910> name=None at 7f7b6aa456d0> -> __attrs_140168046862096
                __attrs_140168046862096 = _static_140168046860560
                __backup_ref_140168047359824 = get('ref', __marker)

                # <Value u'refs' (15:30)> -> __iterator
                __token = 616
                try:
                    __zt_tmp = __attrs_140168046862096
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'refs', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168046858640, ) = getitem('repeat')(u'ref', __iterator)
                econtext['ref'] = None
                for __item in __iterator:
                    econtext['ref'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="d-inline-block">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046859856
                    __attrs_140168046859856 = _static_140168257770128
                    __backup_rendered_140168047284560 = get('rendered', __marker)

                    # <Value u'python:widget.render_reference(context, field, ref)' (16:42)> -> __value
                    __token = 688
                    try:
                        __zt_tmp = __attrs_140168046859856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u'widget.render_reference(context, field, ref)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['rendered'] = __value
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa45410> name=None at 7f7b6aa45450> -> __attrs_140168016767696
                    __attrs_140168016767696 = _static_140168046859280

                    # <Value u'python:rendered' (17:34)> -> __condition
                    __token = 776
                    try:
                        __zt_tmp = __attrs_140168016767696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'rendered', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="p-1 mb-1 mr-1 bg-light border rounded">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016767184
                        __attrs_140168016767184 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016765392
                        __default_140168016765392 = _DEFAULT_MARKER

                        # <Value u'rendered' (19:45)> -> __cache_140168016766800
                        __token = 903
                        try:
                            __zt_tmp = __attrs_140168016767184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168016766800 = _static_140168208991440('path', u'rendered', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'rendered' (19:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68d92810> -> __condition
                        __expression = __cache_140168016766800

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>')
                        else:
                            __content = __cache_140168016766800
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n              </div>')
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7f7b68d92050> name=None at 7f7b68d92a50> -> __attrs_140168016768144
                    __attrs_140168016768144 = _static_140168016765008

                    # <Value u'python:not rendered' (21:34)> -> __condition
                    __token = 970
                    try:
                        __zt_tmp = __attrs_140168016768144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'not rendered', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="text-danger">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b68d926d0> name=None at 7f7b68d922d0> -> __attrs_140168046847440
                        __attrs_140168046847440 = _static_140168016766672

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046848656
                        __default_140168046848656 = _DEFAULT_MARKER

                        # <Substitution u'string:broken reference ${ref}' (22:44)> -> __attr_title
                        __token = 1056
                        try:
                            __zt_tmp = __attrs_140168046847440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140168208991440('string', u'broken reference ${ref}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016766864
                        __default_140168016766864 = _DEFAULT_MARKER

                        # <Value u'ref' (23:35)> -> __cache_140168016765840
                        __token = 1123
                        try:
                            __zt_tmp = __attrs_140168046847440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168016765840 = _static_140168208991440('path', u'ref', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'ref' (23:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68d92650> -> __condition
                        __expression = __cache_140168016765840

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168016765840
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n              </div>')
                    __append(u'\n            ')
                    if (__backup_rendered_140168047284560 is __marker):
                        del econtext['rendered']
                    else:
                        econtext['rendered'] = __backup_rendered_140168047284560
                    __append(u'\n          </li>')
                    ____index_140168046858640 -= 1
                    if (____index_140168046858640 > 0):
                        __append('\n          ')
                if (__backup_ref_140168047359824 is __marker):
                    del econtext['ref']
                else:
                    econtext['ref'] = __backup_ref_140168047359824
                __append(u'\n        </ul>\n      </div>')
                if (__backup_refs_140168037564880 is __marker):
                    del econtext['refs']
                else:
                    econtext['refs'] = __backup_refs_140168037564880
                if (__backup_value_140168046982480 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168046982480
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n    ')
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037628496
            __attrs_140168037628496 = _static_140168257770128
            __previous_i18n_domain_140168037629456 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140168080669184 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a177790> name=None at 7f7b6a177d90> -> __value
            __value = _static_140168037627792
            econtext['macroname'] = __value

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140168037628496
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168080669184 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168080669184
            __i18n_domain = __previous_i18n_domain_140168037629456
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_view': render_view, 'render': render, }