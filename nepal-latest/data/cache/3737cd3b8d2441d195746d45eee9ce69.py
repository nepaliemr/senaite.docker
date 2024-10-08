# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.patient/src/senaite/patient/skins/templates/senaite_patient_widgets/temporaryidentifierwidget.pt'

__tokens = {1329: (u'field/required|nothing', 32, 35), 1387: (u" python: required and 'required' or Non", 33, 34), 1462: (u'd python: errors.get(fieldNam', 34, 33), 1625: (u'python:field.getEditAccessor(here)() or {}', 37, 29), 1705: (u' python:here.session_restore_value(fieldName, values', 38, 36), 1786: (u"e python: values.get('value', values.get('value_auto', ''", 39, 26), 1877: (u'to values/value_auto|stri', 40, 30), 1936: (u'emp values/temporary|not', 41, 29), 1994: (u"temp python:value_temp in ['true','1','on',Tr", 42, 28), 2072: (u"class python: value_temp and 'temporary-id'", 43, 26), 2148: (u'_class string:form form-inline field ArchetypesTemporaryIdentifierWidget TemporaryIdentifier ${css', 44, 25), 2278: (u'equired field/required', 45, 23), 2338: (u'd_marker field/auto_', 46, 28), 2389: (u'  catalog fie', 47, 20), 2447: (u'css_class', 48, 32), 2486: (u' string:archetypes-fieldname-${fieldName', 49, 28), 2568: (u'e string:${fieldNam', 50, 39), 2793: (u'python:field.widget.get_input_widget_attributes(context, field, value)', 57, 40), 2897: (u'python:widget_attrs', 58, 31), 3159: (u'value_temp', 66, 41), 3208: (u' string:${fieldName}_temporar', 67, 37), 3274: (u'd string:${fieldName}_tempora', 68, 34), 3347: (u'string:${fieldName}_temporary', 70, 37), 3547: (u'string:${fieldName}_value_auto', 76, 36), 3615: (u' string:${value_auto', 77, 36), 3781: (u'string:${catalog}', 81, 37), 3897: (u'string:${auto_id_marker}', 83, 37), 3987: (u'required', 86, 48), 4050: (u'error_id', 87, 46), 4206: (u'context/widgets/string/macros/edit', 93, 28), 4206: (u'context/widgets/string/macros/edit', 93, 28), 378: (u'python:field.getEditAccessor(here)() or {}', 10, 33), 462: (u' python:here.session_restore_value(fieldName, values', 11, 40), 555: (u's python:request.get(fieldName, session_value', 12, 38), 635: (u'nt python:field.get_linked_patient(he', 13, 31), 709: (u"ary python:values.get('tempora", 14, 32), 773: (u'lues python:cached_values or v', 15, 28), 989: (u'python:not temporary', 20, 26), 939: (u'python:patient is None', 19, 25), 865: (u"python:patient and patient.absolute_url() or ''", 18, 32), 1041: (u'values/value|nothing', 21, 29), 1108: (u'python:temporary', 24, 29), 1153: (u"python: '{} (temp)'.format(values.get('value'))", 25, 27), 223: (u'here/main_template/macros/master', 5, 21), 223: (u'here/main_template/macros/master', 5, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047357904 = u'master'
_static_140168047034320 = {u'class': u'senaite-queryselect-widget-input', }
_static_140168006551120 = {u'type': u'hidden', u'name': u'config_auto_id_marker', u'value': u'string:${auto_id_marker}', }
_static_140168015868560 = {u'type': u'hidden', u'name': u'string:${fieldName}_value_auto', u'value': u'string:${value_auto}', }
_static_140168036940752 = {u'class': u'fieldErrorBox', }
_static_140168026327696 = {u'id': u'string:${fieldName}_temporary', u'checked': u'value_temp', u'type': u'checkbox', u'class': u'mr-1', u'name': u'string:${fieldName}_temporary', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047658896 = {u'href': u'#', }
_static_140168026327568 = {u'class': u'form-group', }
_static_140168036938640 = u'edit'
_static_140168257770128 = {}
_static_140168015764560 = set([])
_static_140168015692176 = {u'class': u'form-group mr-2', }
_static_140168015870608 = {u'for': u'string:${fieldName}_temporary', }
_static_140168037498768 = {u'data-fieldname': u'string:${fieldName}', u'class': u'form form-inline field ArchetypesTemporaryIdentifierWidget TemporaryIdentifier', u'id': u'string:archetypes-fieldname-${fieldName}', }
_static_140168006550544 = {u'type': u'hidden', u'name': u'config_catalog', u'value': u'string:${catalog}', }
_static_140168006550416 = {u'class': u'fieldErrorBox', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016770768
            __attrs_140168016770768 = _static_140168257770128
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168006674128
            __attrs_140168006674128 = _static_140168257770128
            __backup_required_140168026332112 = get('required', __marker)

            # <Value u'field/required|nothing' (32:35)> -> __value
            __token = 1329
            try:
                __zt_tmp = __attrs_140168006674128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/required|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_required_140168036812752 = get('required', __marker)

            # <Value u"python: required and 'required' or None" (33:34)> -> __value
            __token = 1387
            try:
                __zt_tmp = __attrs_140168006674128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" required and 'required' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_error_id_140168047842384 = get('error_id', __marker)

            # <Value u'python: errors.get(fieldName)' (34:33)> -> __value
            __token = 1462
            try:
                __zt_tmp = __attrs_140168006674128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' errors.get(fieldName)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['error_id'] = __value
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6a157f90> name=None at 7f7b6a157590> -> __attrs_140168015692688
            __attrs_140168015692688 = _static_140168037498768
            __backup_values_140168047005904 = get('values', __marker)

            # <Value u'python:field.getEditAccessor(here)() or {}' (37:29)> -> __value
            __token = 1625
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)() or {}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['values'] = __value
            __backup_session_values_140168037227472 = get('session_values', __marker)

            # <Value u'python:here.session_restore_value(fieldName, values)' (38:36)> -> __value
            __token = 1705
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'here.session_restore_value(fieldName, values)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['session_values'] = __value
            __backup_value_140168047243920 = get('value', __marker)

            # <Value u"python: values.get('value', values.get('value_auto', ''))" (39:26)> -> __value
            __token = 1786
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" values.get('value', values.get('value_auto', ''))", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_value_auto_140168026222416 = get('value_auto', __marker)

            # <Value u'values/value_auto|string:' (40:30)> -> __value
            __token = 1877
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'values/value_auto|string:', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value_auto'] = __value
            __backup_value_temp_140168047764432 = get('value_temp', __marker)

            # <Value u'values/temporary|nothing' (41:29)> -> __value
            __token = 1936
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'values/temporary|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value_temp'] = __value
            __backup_value_temp_140168036813392 = get('value_temp', __marker)

            # <Value u"python:value_temp in ['true','1','on',True,1]" (42:28)> -> __value
            __token = 1994
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"value_temp in ['true','1','on',True,1]", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value_temp'] = __value
            __backup_css_class_140168026330512 = get('css_class', __marker)

            # <Value u"python: value_temp and 'temporary-id' or ''" (43:26)> -> __value
            __token = 2072
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" value_temp and 'temporary-id' or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['css_class'] = __value
            __backup_css_class_140168026329680 = get('css_class', __marker)

            # <Value u'string:form form-inline field ArchetypesTemporaryIdentifierWidget TemporaryIdentifier ${css_class}' (44:25)> -> __value
            __token = 2148
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'form form-inline field ArchetypesTemporaryIdentifierWidget TemporaryIdentifier ${css_class}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['css_class'] = __value
            __backup_required_140168036812176 = get('required', __marker)

            # <Value u'field/required|nothing' (45:23)> -> __value
            __token = 2278
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/required|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_auto_id_marker_140168036811600 = get('auto_id_marker', __marker)

            # <Value u'field/auto_id_marker' (46:28)> -> __value
            __token = 2338
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/auto_id_marker', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['auto_id_marker'] = __value
            __backup_catalog_140168083170448 = get('catalog', __marker)

            # <Value u'field/catalog' (47:20)> -> __value
            __token = 2389
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/catalog', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['catalog'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037496592
            __default_140168037496592 = _DEFAULT_MARKER

            # <Substitution u'css_class' (48:32)> -> __attr_class
            __token = 2447
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('path', u'css_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'form form-inline field ArchetypesTemporaryIdentifierWidget TemporaryIdentifier', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037497616
            __default_140168037497616 = _DEFAULT_MARKER

            # <Substitution u'string:archetypes-fieldname-${fieldName}' (49:28)> -> __attr_id
            __token = 2486
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'archetypes-fieldname-${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037498512
            __default_140168037498512 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}' (50:39)> -> __attr_data_fieldname
            __token = 2568
            try:
                __zt_tmp = __attrs_140168015692688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140168208991440('string', u'${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_fieldname is not None):
                __append((u' data-fieldname="%s"' % __attr_data_fieldname))
            __append(u'>\n\n        <!-- Input text field -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68c8c190> name=None at 7f7b68c8cd90> -> __attrs_140168015693008
            __attrs_140168015693008 = _static_140168015692176

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group mr-2">\n\n          <!-- QUERYSELECT -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa6ffd0> name=None at 7f7b6aa6ff10> -> __attrs_140168047030480
            __attrs_140168047030480 = _static_140168047034320
            __backup_widget_attrs_140168036813904 = get('widget_attrs', __marker)

            # <Value u'python:field.widget.get_input_widget_attributes(context, field, value)' (57:40)> -> __value
            __token = 2793
            try:
                __zt_tmp = __attrs_140168047030480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.widget.get_input_widget_attributes(context, field, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['widget_attrs'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Value u'python:widget_attrs' (58:31)> -> __cache_140168047031120
            __token = 2897
            try:
                __zt_tmp = __attrs_140168047030480
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168047031120 = _static_140168208991440('python', u'widget_attrs', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if (u'class' not in __chain(__cache_140168047031120)):
                __append(u' class="senaite-queryselect-widget-input"')
            __attr_140168047032720 = __cache_140168047031120
            for (name, value, ) in __attr_140168047032720.items():
                if ((name not in _static_140168015764560) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'>\n            <!-- ReactJS controlled component -->\n          </div>')
            if (__backup_widget_attrs_140168036813904 is __marker):
                del econtext['widget_attrs']
            else:
                econtext['widget_attrs'] = __backup_widget_attrs_140168036813904
            __append(u'\n        </div>\n\n        <!-- Temporary checkbox -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b696b0a10> name=None at 7f7b696b06d0> -> __attrs_140168026328208
            __attrs_140168026328208 = _static_140168026327568

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b696b0a90> name=None at 7f7b696b0cd0> -> __attrs_140168015868368
            __attrs_140168015868368 = _static_140168026327696

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="checkbox" class="mr-1"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015870032
            __default_140168015870032 = _DEFAULT_MARKER

            # <Boolean u'value_temp' (66:41)> -> __attr_checked
            __token = 3159
            try:
                __zt_tmp = __attrs_140168015868368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_140168208991440('path', u'value_temp', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = u'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((u' checked="%s"' % __attr_checked))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015869712
            __default_140168015869712 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}_temporary' (67:37)> -> __attr_name
            __token = 3208
            try:
                __zt_tmp = __attrs_140168015868368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('string', u'${fieldName}_temporary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015870992
            __default_140168015870992 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}_temporary' (68:34)> -> __attr_id
            __token = 3274
            try:
                __zt_tmp = __attrs_140168015868368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'${fieldName}_temporary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'/>\n\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b68cb7a90> name=None at 7f7b68cb72d0> -> __attrs_140168015871120
            __attrs_140168015871120 = _static_140168015870608

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015871504
            __default_140168015871504 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}_temporary' (70:37)> -> __attr_for
            __token = 3347
            try:
                __zt_tmp = __attrs_140168015871120
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_for = _static_140168208991440('string', u'${fieldName}_temporary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_for is not None):
                __append((u' for="%s"' % __attr_for))
            __append(u'>')
            __stream_140168015869136 = []
            __append_140168015869136 = __stream_140168015869136.append
            __append_140168015869136(u'Temporary')
            __msgid_140168015869136 = __re_whitespace(''.join(__stream_140168015869136)).strip()
            if __msgid_140168015869136:
                __append(translate(__msgid_140168015869136, mapping=None, default=__msgid_140168015869136, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        </div>\n\n        <!-- Auto generated ID -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68cb7290> name=None at 7f7b68cb7fd0> -> __attrs_140168006551568
            __attrs_140168006551568 = _static_140168015868560

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015869904
            __default_140168015869904 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}_value_auto' (76:36)> -> __attr_name
            __token = 3547
            try:
                __zt_tmp = __attrs_140168006551568
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('string', u'${fieldName}_value_auto', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015871824
            __default_140168015871824 = _DEFAULT_MARKER

            # <Substitution u'string:${value_auto}' (77:36)> -> __attr_value
            __token = 3615
            try:
                __zt_tmp = __attrs_140168006551568
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('string', u'${value_auto}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n\n        <!-- Input elements with config options -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b683d4410> name=None at 7f7b683d4350> -> __attrs_140168006552592
            __attrs_140168006552592 = _static_140168006550544

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="config_catalog"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168006551504
            __default_140168006551504 = _DEFAULT_MARKER

            # <Substitution u'string:${catalog}' (81:37)> -> __attr_value
            __token = 3781
            try:
                __zt_tmp = __attrs_140168006552592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('string', u'${catalog}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b683d4650> name=None at 7f7b683d4f50> -> __attrs_140168006551440
            __attrs_140168006551440 = _static_140168006551120

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="config_auto_id_marker"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168006549648
            __default_140168006549648 = _DEFAULT_MARKER

            # <Substitution u'string:${auto_id_marker}' (83:37)> -> __attr_value
            __token = 3897
            try:
                __zt_tmp = __attrs_140168006551440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('string', u'${auto_id_marker}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      </div>')
            if (__backup_catalog_140168083170448 is __marker):
                del econtext['catalog']
            else:
                econtext['catalog'] = __backup_catalog_140168083170448
            if (__backup_auto_id_marker_140168036811600 is __marker):
                del econtext['auto_id_marker']
            else:
                econtext['auto_id_marker'] = __backup_auto_id_marker_140168036811600
            if (__backup_required_140168036812176 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168036812176
            if (__backup_css_class_140168026329680 is __marker):
                del econtext['css_class']
            else:
                econtext['css_class'] = __backup_css_class_140168026329680
            if (__backup_css_class_140168026330512 is __marker):
                del econtext['css_class']
            else:
                econtext['css_class'] = __backup_css_class_140168026330512
            if (__backup_value_temp_140168036813392 is __marker):
                del econtext['value_temp']
            else:
                econtext['value_temp'] = __backup_value_temp_140168036813392
            if (__backup_value_temp_140168047764432 is __marker):
                del econtext['value_temp']
            else:
                econtext['value_temp'] = __backup_value_temp_140168047764432
            if (__backup_value_auto_140168026222416 is __marker):
                del econtext['value_auto']
            else:
                econtext['value_auto'] = __backup_value_auto_140168026222416
            if (__backup_value_140168047243920 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168047243920
            if (__backup_session_values_140168037227472 is __marker):
                del econtext['session_values']
            else:
                econtext['session_values'] = __backup_session_values_140168037227472
            if (__backup_values_140168047005904 is __marker):
                del econtext['values']
            else:
                econtext['values'] = __backup_values_140168047005904
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b683d4390> name=None at 7f7b683d4fd0> -> __attrs_140168036940112
            __attrs_140168036940112 = _static_140168006550416

            # <Value u'required' (86:48)> -> __condition
            __token = 3987
            try:
                __zt_tmp = __attrs_140168036940112
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="fieldErrorBox"></div>')
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6a0cfbd0> name=None at 7f7b6a0cf510> -> __attrs_140168036939536
            __attrs_140168036939536 = _static_140168036940752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="fieldErrorBox">')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036938320
            __default_140168036938320 = _DEFAULT_MARKER

            # <Value u'error_id' (87:46)> -> __cache_140168036941392
            __token = 4050
            try:
                __zt_tmp = __attrs_140168036939536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168036941392 = _static_140168208991440('path', u'error_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'error_id' (87:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a0cfd50> -> __condition
            __expression = __cache_140168036941392

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168036941392
                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n      ')
            if (__backup_error_id_140168047842384 is __marker):
                del econtext['error_id']
            else:
                econtext['error_id'] = __backup_error_id_140168047842384
            if (__backup_required_140168036812752 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168036812752
            if (__backup_required_140168026332112 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168026332112
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168006672976
            __attrs_140168006672976 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026307856
            __attrs_140168026307856 = _static_140168257770128
            __backup_macroname_140168056021632 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a0cf390> name=None at 7f7b6a0cfa10> -> __value
            __value = _static_140168036938640
            econtext['macroname'] = __value

            # <Value u'context/widgets/string/macros/edit' (93:28)> -> __macro
            __token = 4206
            try:
                __zt_tmp = __attrs_140168026307856
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 4206
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168056021632 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168056021632
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
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016772048
            __attrs_140168016772048 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016769296
            __attrs_140168016769296 = _static_140168257770128
            __backup_values_140168016948688 = get('values', __marker)

            # <Value u'python:field.getEditAccessor(here)() or {}' (10:33)> -> __value
            __token = 378
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)() or {}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['values'] = __value
            __backup_session_values_140168026332048 = get('session_values', __marker)

            # <Value u'python:here.session_restore_value(fieldName, values)' (11:40)> -> __value
            __token = 462
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'here.session_restore_value(fieldName, values)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['session_values'] = __value
            __backup_cached_values_140168047287504 = get('cached_values', __marker)

            # <Value u'python:request.get(fieldName, session_values)' (12:38)> -> __value
            __token = 555
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'request.get(fieldName, session_values)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['cached_values'] = __value
            __backup_patient_140168047308496 = get('patient', __marker)

            # <Value u'python:field.get_linked_patient(here)' (13:31)> -> __value
            __token = 635
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.get_linked_patient(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['patient'] = __value
            __backup_temporary_140168046866320 = get('temporary', __marker)

            # <Value u"python:values.get('temporary')" (14:32)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"values.get('temporary')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['temporary'] = __value
            __backup_values_140168026331024 = get('values', __marker)

            # <Value u'python:cached_values or values' (15:28)> -> __value
            __token = 773
            try:
                __zt_tmp = __attrs_140168016769296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'cached_values or values', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['values'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab08790> name=None at 7f7b6ab08c10> -> __attrs_140168006672528
            __attrs_140168006672528 = _static_140168047658896

            # <Value u'python:not temporary' (20:26)> -> __condition
            __token = 989
            try:
                __zt_tmp = __attrs_140168006672528
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'not temporary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value u'python:patient is None' (19:25)> at 7f7b683f2c50> -> __cache_140168006675536

                # <Value u'python:patient is None' (19:25)> -> __cache_140168006675536
                __token = 939
                try:
                    __zt_tmp = __attrs_140168006672528
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168006675536 = _static_140168208991440('python', u'patient is None', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __cache_140168006675536 = not __cache_140168006675536
                __condition = __cache_140168006675536
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168083170064
                    __default_140168083170064 = _DEFAULT_MARKER

                    # <Substitution u"python:patient and patient.absolute_url() or ''" (18:32)> -> __attr_href
                    __token = 865
                    try:
                        __zt_tmp = __attrs_140168006672528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('python', u"patient and patient.absolute_url() or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168006675024
                __attrs_140168006675024 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168006673744
                __default_140168006673744 = _DEFAULT_MARKER

                # <Value u'values/value|nothing' (21:29)> -> __cache_140168006675152
                __token = 1041
                try:
                    __zt_tmp = __attrs_140168006675024
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168006675152 = _static_140168208991440('path', u'values/value|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'values/value|nothing' (21:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b683f2590> -> __condition
                __expression = __cache_140168006675152

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168006675152
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n        ')
                __condition = __cache_140168006675536
                if __condition:
                    __append(u'</a>')
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168006674896
            __attrs_140168006674896 = _static_140168257770128

            # <Value u'python:temporary' (24:29)> -> __condition
            __token = 1108
            try:
                __zt_tmp = __attrs_140168006674896
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'temporary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168006672464
                __default_140168006672464 = _DEFAULT_MARKER

                # <Value u"python: '{} (temp)'.format(values.get('value'))" (25:27)> -> __cache_140168006675344
                __token = 1153
                try:
                    __zt_tmp = __attrs_140168006674896
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168006675344 = _static_140168208991440('python', u" '{} (temp)'.format(values.get('value'))", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u"python: '{} (temp)'.format(values.get('value'))" (25:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b683f24d0> -> __condition
                __expression = __cache_140168006675344

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168006675344
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>')
            __append(u'\n\n      ')
            if (__backup_values_140168026331024 is __marker):
                del econtext['values']
            else:
                econtext['values'] = __backup_values_140168026331024
            if (__backup_temporary_140168046866320 is __marker):
                del econtext['temporary']
            else:
                econtext['temporary'] = __backup_temporary_140168046866320
            if (__backup_patient_140168047308496 is __marker):
                del econtext['patient']
            else:
                econtext['patient'] = __backup_patient_140168047308496
            if (__backup_cached_values_140168047287504 is __marker):
                del econtext['cached_values']
            else:
                econtext['cached_values'] = __backup_cached_values_140168047287504
            if (__backup_session_values_140168026332048 is __marker):
                del econtext['session_values']
            else:
                econtext['session_values'] = __backup_session_values_140168026332048
            if (__backup_values_140168016948688 is __marker):
                del econtext['values']
            else:
                econtext['values'] = __backup_values_140168016948688
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047356560
            __attrs_140168047356560 = _static_140168257770128
            __previous_i18n_domain_140168047356240 = __i18n_domain
            __i18n_domain = u'senaite.patient'
            __backup_macroname_140168055200336 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aabefd0> name=None at 7f7b6aabe750> -> __value
            __value = _static_140168047357904
            econtext['macroname'] = __value

            # <Value u'here/main_template/macros/master' (5:21)> -> __macro
            __token = 223
            try:
                __zt_tmp = __attrs_140168047356560
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 223
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055200336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055200336
            __i18n_domain = __previous_i18n_domain_140168047356240
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_view': render_view, 'render': render, }