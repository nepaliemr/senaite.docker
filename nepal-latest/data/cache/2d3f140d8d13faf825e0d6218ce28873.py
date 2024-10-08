# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.patient/src/senaite/patient/skins/templates/senaite_patient_widgets/fullnamewidget.pt'

__tokens = {1472: (u'python:field.getEditAccessor(here)() or {}', 31, 32), 1555: (u' python:here.session_restore_value(fieldName, value', 32, 39), 1646: (u'e python:request.get(fieldName, session_valu', 33, 37), 1723: (u'ue python:cached_value or va', 34, 29), 1788: (u"ame python: value.get('firstname',", 35, 32), 1860: (u"name python: value.get('middlename'", 36, 32), 1931: (u"tname python: value.get('lastname", 37, 29), 2000: (u'llname python: filter(None, [firstname, middlename, las', 38, 28), 2091: (u"ullname python: ' '.join(fullname)", 39, 27), 2172: (u'irstname string:${fieldName}.firstname:ignore_emp', 41, 36), 2268: (u'iddlename string:${fieldName}.middlename:ignore_em', 42, 36), 2363: (u'd_lastname string:${fieldName}.lastname:ignore_e', 43, 33), 2448: (u'   required field/requ', 45, 23), 2506: (u"    required python: required and 'requ", 46, 22), 2584: (u'   entry_mode python: field.widget.entry_m', 48, 23), 2667: (u" fullname_mode python: entry_mode in ['ful", 49, 25), 2752: (u'first_last_mode python: entry_mode', 50, 26), 2824: (u'      parts_mode python: not any([fullname_mode, ', 51, 20), 2912: (u'      i18n_domain field/widget/i18n_domain|context/i18n_d', 52, 20), 3087: (u"python:required and '1' or '0'", 55, 43), 3153: (u' string:${fieldName', 56, 34), 3228: (u'required', 57, 52), 3375: (u'not:fullname_mode', 60, 78), 3701: (u'string:${subfield_firstname}', 67, 38), 3770: (u' string:${subfield_firstname', 68, 39), 3840: (u'e firstna', 69, 39), 3894: (u'ed requi', 70, 41), 4151: (u'parts_mode', 77, 34), 4267: (u'string:${subfield_middlename}', 79, 38), 4337: (u' string:${subfield_middlename', 80, 39), 4408: (u'e middlena', 81, 39), 4463: (u'ed requi', 82, 41), 4546: (u'not:parts_mode', 84, 34), 4600: (u'string:${subfield_middlename}', 85, 38), 4670: (u' string:${subfield_middlename', 86, 39), 4741: (u'e middlena', 87, 39), 5061: (u'string:${subfield_lastname}', 95, 38), 5129: (u' string:${subfield_lastname', 96, 39), 5198: (u'e lastna', 97, 39), 5251: (u'ed requi', 98, 41), 5373: (u'fullname_mode', 102, 49), 5555: (u'string:${subfield_firstname}', 106, 38), 5624: (u' string:${subfield_firstname', 107, 39), 5694: (u'e fullna', 108, 39), 5747: (u'ed requi', 109, 41), 5916: (u'context/widgets/string/macros/edit', 117, 28), 5916: (u'context/widgets/string/macros/edit', 117, 28), 388: (u'python:field.getAccessor(here)() or {}', 10, 33), 463: (u" python:value.get('firstname', ''", 11, 35), 534: (u"e python:value.get('middlename', '", 12, 35), 604: (u"me python:value.get('lastname', ", 13, 32), 672: (u'ame python:filter(None, [firstname, middlename , lastna', 14, 31), 763: (u"name python:' '.join(fullname).st", 15, 30), 834: (u"_mode python:field.widget.entry_mode or '", 16, 31), 914: (u'format python:field.widget.view', 17, 31), 986: (u"me_mode python:entry_mode in ['full', 'fu", 18, 32), 1078: (u'value', 19, 39), 1117: (u'not:fullname_mode', 20, 31), 1165: (u'python: view_format % value', 21, 29), 1227: (u'fullname_mode', 22, 31), 1271: (u'fullname', 23, 29), 1339: (u'not:value', 26, 29), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168036459024 = {u'name': u'string:${subfield_firstname}', u'title': u'Firstname', u'type': u'text', u'required': u'required', u'value': u'firstname', u'class': u'form-control form-control-sm mb-1', u'placeholder': u'Firstname', u'id': u'string:${subfield_firstname}', }
_static_140168037141520 = {u'name': u'string:${subfield_lastname}', u'title': u'Lastname', u'type': u'text', u'required': u'required', u'value': u'lastname', u'class': u'form-control form-control-sm mb-1', u'placeholder': u'Lastname', u'id': u'string:${subfield_lastname}', }
_static_140168036461392 = {u'class': u'input-group d-flex d-inline-flex w-auto', }
_static_140168036938192 = u'master'
_static_140168047117136 = u'edit'
_static_140168037252048 = {u'name': u'string:${subfield_middlename}', u'title': u'Middlename', u'type': u'text', u'required': u'required', u'value': u'middlename', u'class': u'form-control form-control-sm mb-1', u'placeholder': u'Middlename', u'id': u'string:${subfield_middlename}', }
_static_140168036672656 = {u'class': u'fieldErrorBox', }
_static_140168047119632 = {u'name': u'string:${subfield_firstname}', u'title': u'title', u'type': u'text', u'required': u'required', u'value': u'fullname', u'placeholder': u'Fullname', u'id': u'string:${subfield_firstname}', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168036673872 = {u'data-fieldname': u'string:${fieldName}', u'data-required': u"python:required and '1' or '0'", u'class': u'field FullnameWidget text-left', }
_static_140168036944592 = {u'class': u'form-group', }
_static_140168257770128 = {}
_static_140168037140240 = {u'type': u'hidden', u'id': u'string:${subfield_middlename}', u'value': u'middlename', u'name': u'string:${subfield_middlename}', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037918288
            __attrs_140168037918288 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046974480
            __attrs_140168046974480 = _static_140168257770128
            __backup_value_140168015846864 = get('value', __marker)

            # <Value u'python:field.getEditAccessor(here)() or {}' (31:32)> -> __value
            __token = 1472
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)() or {}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_session_value_140168047252944 = get('session_value', __marker)

            # <Value u'python:here.session_restore_value(fieldName, value)' (32:39)> -> __value
            __token = 1555
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'here.session_restore_value(fieldName, value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['session_value'] = __value
            __backup_cached_value_140168046937104 = get('cached_value', __marker)

            # <Value u'python:request.get(fieldName, session_value)' (33:37)> -> __value
            __token = 1646
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'request.get(fieldName, session_value)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['cached_value'] = __value
            __backup_value_140168037920144 = get('value', __marker)

            # <Value u'python:cached_value or value' (34:29)> -> __value
            __token = 1723
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'cached_value or value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_firstname_140168037918096 = get('firstname', __marker)

            # <Value u"python: value.get('firstname', '')" (35:32)> -> __value
            __token = 1788
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" value.get('firstname', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['firstname'] = __value
            __backup_middlename_140168037918608 = get('middlename', __marker)

            # <Value u"python: value.get('middlename', '')" (36:32)> -> __value
            __token = 1860
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" value.get('middlename', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['middlename'] = __value
            __backup_lastname_140168037917328 = get('lastname', __marker)

            # <Value u"python: value.get('lastname', '')" (37:29)> -> __value
            __token = 1931
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" value.get('lastname', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['lastname'] = __value
            __backup_fullname_140168037918864 = get('fullname', __marker)

            # <Value u'python: filter(None, [firstname, middlename, lastname])' (38:28)> -> __value
            __token = 2000
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' filter(None, [firstname, middlename, lastname])', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname'] = __value
            __backup_fullname_140168047246928 = get('fullname', __marker)

            # <Value u"python: ' '.join(fullname).strip()" (39:27)> -> __value
            __token = 2091
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" ' '.join(fullname).strip()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname'] = __value
            __backup_subfield_firstname_140168047247184 = get('subfield_firstname', __marker)

            # <Value u'string:${fieldName}.firstname:ignore_empty:record' (41:36)> -> __value
            __token = 2172
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.firstname:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_firstname'] = __value
            __backup_subfield_middlename_140168047243792 = get('subfield_middlename', __marker)

            # <Value u'string:${fieldName}.middlename:ignore_empty:record' (42:36)> -> __value
            __token = 2268
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.middlename:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_middlename'] = __value
            __backup_subfield_lastname_140168047244432 = get('subfield_lastname', __marker)

            # <Value u'string:${fieldName}.lastname:ignore_empty:record' (43:33)> -> __value
            __token = 2363
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.lastname:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_lastname'] = __value
            __backup_required_140168047244560 = get('required', __marker)

            # <Value u'field/required|nothing' (45:23)> -> __value
            __token = 2448
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/required|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_required_140168047246480 = get('required', __marker)

            # <Value u"python: required and 'required' or None" (46:22)> -> __value
            __token = 2506
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" required and 'required' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_entry_mode_140168083094480 = get('entry_mode', __marker)

            # <Value u"python: field.widget.entry_mode or 'parts'" (48:23)> -> __value
            __token = 2584
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" field.widget.entry_mode or 'parts'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['entry_mode'] = __value
            __backup_fullname_mode_140168083093904 = get('fullname_mode', __marker)

            # <Value u"python: entry_mode in ['full', 'fullname']" (49:25)> -> __value
            __token = 2667
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" entry_mode in ['full', 'fullname']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname_mode'] = __value
            __backup_first_last_mode_140168083094608 = get('first_last_mode', __marker)

            # <Value u"python: entry_mode == 'first_last'" (50:26)> -> __value
            __token = 2752
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" entry_mode == 'first_last'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['first_last_mode'] = __value
            __backup_parts_mode_140168046976720 = get('parts_mode', __marker)

            # <Value u'python: not any([fullname_mode, first_last_mode])' (51:20)> -> __value
            __token = 2824
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' not any([fullname_mode, first_last_mode])', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['parts_mode'] = __value
            __backup_i18n_domain_140168046976848 = get('i18n_domain', __marker)

            # <Value u'field/widget/i18n_domain|context/i18n_domain|string:plone' (52:20)> -> __value
            __token = 2912
            try:
                __zt_tmp = __attrs_140168046974480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/widget/i18n_domain|context/i18n_domain|string:plone', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['i18n_domain'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a08e950> name=None at 7f7b6a08e990> -> __attrs_140168036672336
            __attrs_140168036672336 = _static_140168036673872

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field FullnameWidget text-left"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036673168
            __default_140168036673168 = _DEFAULT_MARKER

            # <Substitution u"python:required and '1' or '0'" (55:43)> -> __attr_data_required
            __token = 3087
            try:
                __zt_tmp = __attrs_140168036672336
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_required = _static_140168208991440('python', u"required and '1' or '0'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_required = __quote(__attr_data_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_required is not None):
                __append((u' data-required="%s"' % __attr_data_required))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036674192
            __default_140168036674192 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}' (56:34)> -> __attr_data_fieldname
            __token = 3153
            try:
                __zt_tmp = __attrs_140168036672336
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140168208991440('string', u'${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_fieldname is not None):
                __append((u' data-fieldname="%s"' % __attr_data_fieldname))
            __append(u'>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a08e490> name=None at 7f7b6a08eb50> -> __attrs_140168036672272
            __attrs_140168036672272 = _static_140168036672656

            # <Value u'required' (57:52)> -> __condition
            __token = 3228
            try:
                __zt_tmp = __attrs_140168036672272
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="fieldErrorBox"></div>')
            __append(u'\n\n          <!-- Firstname + lastname input area -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a05ab50> name=None at 7f7b6a05ae10> -> __attrs_140168036460816
            __attrs_140168036460816 = _static_140168036461392

            # <Value u'not:fullname_mode' (60:78)> -> __condition
            __token = 3375
            try:
                __zt_tmp = __attrs_140168036460816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('not', u'fullname_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group d-flex d-inline-flex w-auto">\n            <!-- Firstname -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a05a210> name=None at 7f7b6a05aa50> -> __attrs_140168037252240
                __attrs_140168037252240 = _static_140168036459024

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" title="Firstname"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037251856
                __default_140168037251856 = _DEFAULT_MARKER

                # <Translate msgid=u'label_firstname' node=<_ast.Str object at 0x7f7b6aabbf50> at 7f7b6aabb390> -> __attr_placeholder
                __attr_placeholder = u'Firstname'
                __attr_placeholder = translate(u'label_firstname', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_placeholder is not None):
                    __append((u' placeholder="%s"' % __attr_placeholder))
                __append(u' class="form-control form-control-sm mb-1"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037252880
                __default_140168037252880 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_firstname}' (67:38)> -> __attr_id
                __token = 3701
                try:
                    __zt_tmp = __attrs_140168037252240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_firstname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037252112
                __default_140168037252112 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_firstname}' (68:39)> -> __attr_name
                __token = 3770
                try:
                    __zt_tmp = __attrs_140168037252240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_firstname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037249104
                __default_140168037249104 = _DEFAULT_MARKER

                # <Substitution u'firstname' (69:39)> -> __attr_value
                __token = 3840
                try:
                    __zt_tmp = __attrs_140168037252240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'firstname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037249680
                __default_140168037249680 = _DEFAULT_MARKER

                # <Substitution u'required' (70:41)> -> __attr_required
                __token = 3894
                try:
                    __zt_tmp = __attrs_140168037252240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_required = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_required is not None):
                    __append((u' required="%s"' % __attr_required))
                __append(u'/>\n\n            <!-- Middlename -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a11bbd0> name=None at 7f7b6a11b850> -> __attrs_140168037139728
                __attrs_140168037139728 = _static_140168037252048

                # <Value u'parts_mode' (77:34)> -> __condition
                __token = 4151
                try:
                    __zt_tmp = __attrs_140168037139728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'parts_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="text" title="Middlename"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047149840
                    __default_140168047149840 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_middlename' node=<_ast.Str object at 0x7f7b6a11be50> at 7f7b6a11b610> -> __attr_placeholder
                    __attr_placeholder = u'Middlename'
                    __attr_placeholder = translate(u'label_middlename', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_placeholder is not None):
                        __append((u' placeholder="%s"' % __attr_placeholder))
                    __append(u' class="form-control form-control-sm mb-1"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047150608
                    __default_140168047150608 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_middlename}' (79:38)> -> __attr_id
                    __token = 4267
                    try:
                        __zt_tmp = __attrs_140168037139728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('string', u'${subfield_middlename}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047151568
                    __default_140168047151568 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_middlename}' (80:39)> -> __attr_name
                    __token = 4337
                    try:
                        __zt_tmp = __attrs_140168037139728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'${subfield_middlename}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047150416
                    __default_140168047150416 = _DEFAULT_MARKER

                    # <Substitution u'middlename' (81:39)> -> __attr_value
                    __token = 4408
                    try:
                        __zt_tmp = __attrs_140168037139728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('path', u'middlename', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037138896
                    __default_140168037138896 = _DEFAULT_MARKER

                    # <Substitution u'required' (82:41)> -> __attr_required
                    __token = 4463
                    try:
                        __zt_tmp = __attrs_140168037139728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_required = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_required is not None):
                        __append((u' required="%s"' % __attr_required))
                    __append(u'/>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a100710> name=None at 7f7b6a100690> -> __attrs_140168037140304
                __attrs_140168037140304 = _static_140168037140240

                # <Value u'not:parts_mode' (84:34)> -> __condition
                __token = 4546
                try:
                    __zt_tmp = __attrs_140168037140304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('not', u'parts_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037142032
                    __default_140168037142032 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_middlename}' (85:38)> -> __attr_id
                    __token = 4600
                    try:
                        __zt_tmp = __attrs_140168037140304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('string', u'${subfield_middlename}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037139984
                    __default_140168037139984 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_middlename}' (86:39)> -> __attr_name
                    __token = 4670
                    try:
                        __zt_tmp = __attrs_140168037140304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'${subfield_middlename}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037141968
                    __default_140168037141968 = _DEFAULT_MARKER

                    # <Substitution u'middlename' (87:39)> -> __attr_value
                    __token = 4741
                    try:
                        __zt_tmp = __attrs_140168037140304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('path', u'middlename', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>')
                __append(u'\n\n            <!-- Lastname -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a100c10> name=None at 7f7b6a100f10> -> __attrs_140168036944720
                __attrs_140168036944720 = _static_140168037141520

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" title="Lastname" class="form-control form-control-sm mb-1"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943440
                __default_140168036943440 = _DEFAULT_MARKER

                # <Translate msgid=u'label_lastname' node=<_ast.Str object at 0x7f7b6ab34dd0> at 7f7b6a0d0690> -> __attr_placeholder
                __attr_placeholder = u'Lastname'
                __attr_placeholder = translate(u'label_lastname', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_placeholder is not None):
                    __append((u' placeholder="%s"' % __attr_placeholder))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036942352
                __default_140168036942352 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_lastname}' (95:38)> -> __attr_id
                __token = 5061
                try:
                    __zt_tmp = __attrs_140168036944720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_lastname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943248
                __default_140168036943248 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_lastname}' (96:39)> -> __attr_name
                __token = 5129
                try:
                    __zt_tmp = __attrs_140168036944720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_lastname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943568
                __default_140168036943568 = _DEFAULT_MARKER

                # <Substitution u'lastname' (97:39)> -> __attr_value
                __token = 5198
                try:
                    __zt_tmp = __attrs_140168036944720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'lastname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036943760
                __default_140168036943760 = _DEFAULT_MARKER

                # <Substitution u'required' (98:41)> -> __attr_required
                __token = 5251
                try:
                    __zt_tmp = __attrs_140168036944720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_required = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_required is not None):
                    __append((u' required="%s"' % __attr_required))
                __append(u'/>\n          </div>')
            __append(u'\n\n          <!-- Fullname input area -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a0d0ad0> name=None at 7f7b6a0d0fd0> -> __attrs_140168036945744
            __attrs_140168036945744 = _static_140168036944592

            # <Value u'fullname_mode' (102:49)> -> __condition
            __token = 5373
            try:
                __zt_tmp = __attrs_140168036945744
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'fullname_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="form-group">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa84d10> name=None at 7f7b6aa84890> -> __attrs_140168047116560
                __attrs_140168047116560 = _static_140168047119632

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" placeholder="Fullname"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047117840
                __default_140168047117840 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_firstname}' (106:38)> -> __attr_id
                __token = 5555
                try:
                    __zt_tmp = __attrs_140168047116560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_firstname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047119568
                __default_140168047119568 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_firstname}' (107:39)> -> __attr_name
                __token = 5624
                try:
                    __zt_tmp = __attrs_140168047116560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_firstname}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047118544
                __default_140168047118544 = _DEFAULT_MARKER

                # <Substitution u'fullname' (108:39)> -> __attr_value
                __token = 5694
                try:
                    __zt_tmp = __attrs_140168047116560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'fullname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047117328
                __default_140168047117328 = _DEFAULT_MARKER

                # <Substitution u'required' (109:41)> -> __attr_required
                __token = 5747
                try:
                    __zt_tmp = __attrs_140168047116560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_required = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_required is not None):
                    __append((u' required="%s"' % __attr_required))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047118032
                __default_140168047118032 = _DEFAULT_MARKER

                # <Translate msgid=u'placeholder' node=<_ast.Str object at 0x7f7b6aa842d0> at 7f7b6aa84590> -> __attr_title
                __attr_title = u'title'
                __attr_title = translate(u'placeholder', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'/>\n          </div>')
            __append(u'\n\n        </div>\n      ')
            if (__backup_i18n_domain_140168046976848 is __marker):
                del econtext['i18n_domain']
            else:
                econtext['i18n_domain'] = __backup_i18n_domain_140168046976848
            if (__backup_parts_mode_140168046976720 is __marker):
                del econtext['parts_mode']
            else:
                econtext['parts_mode'] = __backup_parts_mode_140168046976720
            if (__backup_first_last_mode_140168083094608 is __marker):
                del econtext['first_last_mode']
            else:
                econtext['first_last_mode'] = __backup_first_last_mode_140168083094608
            if (__backup_fullname_mode_140168083093904 is __marker):
                del econtext['fullname_mode']
            else:
                econtext['fullname_mode'] = __backup_fullname_mode_140168083093904
            if (__backup_entry_mode_140168083094480 is __marker):
                del econtext['entry_mode']
            else:
                econtext['entry_mode'] = __backup_entry_mode_140168083094480
            if (__backup_required_140168047246480 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168047246480
            if (__backup_required_140168047244560 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168047244560
            if (__backup_subfield_lastname_140168047244432 is __marker):
                del econtext['subfield_lastname']
            else:
                econtext['subfield_lastname'] = __backup_subfield_lastname_140168047244432
            if (__backup_subfield_middlename_140168047243792 is __marker):
                del econtext['subfield_middlename']
            else:
                econtext['subfield_middlename'] = __backup_subfield_middlename_140168047243792
            if (__backup_subfield_firstname_140168047247184 is __marker):
                del econtext['subfield_firstname']
            else:
                econtext['subfield_firstname'] = __backup_subfield_firstname_140168047247184
            if (__backup_fullname_140168047246928 is __marker):
                del econtext['fullname']
            else:
                econtext['fullname'] = __backup_fullname_140168047246928
            if (__backup_fullname_140168037918864 is __marker):
                del econtext['fullname']
            else:
                econtext['fullname'] = __backup_fullname_140168037918864
            if (__backup_lastname_140168037917328 is __marker):
                del econtext['lastname']
            else:
                econtext['lastname'] = __backup_lastname_140168037917328
            if (__backup_middlename_140168037918608 is __marker):
                del econtext['middlename']
            else:
                econtext['middlename'] = __backup_middlename_140168037918608
            if (__backup_firstname_140168037918096 is __marker):
                del econtext['firstname']
            else:
                econtext['firstname'] = __backup_firstname_140168037918096
            if (__backup_value_140168037920144 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168037920144
            if (__backup_cached_value_140168046937104 is __marker):
                del econtext['cached_value']
            else:
                econtext['cached_value'] = __backup_cached_value_140168046937104
            if (__backup_session_value_140168047252944 is __marker):
                del econtext['session_value']
            else:
                econtext['session_value'] = __backup_session_value_140168047252944
            if (__backup_value_140168015846864 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168015846864
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037917648
            __attrs_140168037917648 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047117456
            __attrs_140168047117456 = _static_140168257770128
            __backup_macroname_140168053984704 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa84350> name=None at 7f7b6aa84810> -> __value
            __value = _static_140168047117136
            econtext['macroname'] = __value

            # <Value u'context/widgets/string/macros/edit' (117:28)> -> __macro
            __token = 5916
            try:
                __zt_tmp = __attrs_140168047117456
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 5916
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168053984704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168053984704
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037920208
            __attrs_140168037920208 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037920656
            __attrs_140168037920656 = _static_140168257770128
            __backup_value_140168083127824 = get('value', __marker)

            # <Value u'python:field.getAccessor(here)() or {}' (10:33)> -> __value
            __token = 388
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getAccessor(here)() or {}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_firstname_140168036940304 = get('firstname', __marker)

            # <Value u"python:value.get('firstname', '')" (11:35)> -> __value
            __token = 463
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"value.get('firstname', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['firstname'] = __value
            __backup_middlename_140168036813520 = get('middlename', __marker)

            # <Value u"python:value.get('middlename', '')" (12:35)> -> __value
            __token = 534
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"value.get('middlename', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['middlename'] = __value
            __backup_lastname_140168037311120 = get('lastname', __marker)

            # <Value u"python:value.get('lastname', '')" (13:32)> -> __value
            __token = 604
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"value.get('lastname', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['lastname'] = __value
            __backup_fullname_140168037304976 = get('fullname', __marker)

            # <Value u'python:filter(None, [firstname, middlename , lastname])' (14:31)> -> __value
            __token = 672
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'filter(None, [firstname, middlename , lastname])', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname'] = __value
            __backup_fullname_140168015698448 = get('fullname', __marker)

            # <Value u"python:' '.join(fullname).strip()" (15:30)> -> __value
            __token = 763
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"' '.join(fullname).strip()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname'] = __value
            __backup_entry_mode_140168047810192 = get('entry_mode', __marker)

            # <Value u"python:field.widget.entry_mode or 'parts'" (16:31)> -> __value
            __token = 834
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"field.widget.entry_mode or 'parts'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['entry_mode'] = __value
            __backup_view_format_140168036765200 = get('view_format', __marker)

            # <Value u'python:field.widget.view_format' (17:31)> -> __value
            __token = 914
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.widget.view_format', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['view_format'] = __value
            __backup_fullname_mode_140168026288848 = get('fullname_mode', __marker)

            # <Value u"python:entry_mode in ['full', 'fullname']" (18:32)> -> __value
            __token = 986
            try:
                __zt_tmp = __attrs_140168037920656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"entry_mode in ['full', 'fullname']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fullname_mode'] = __value
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037917456
            __attrs_140168037917456 = _static_140168257770128

            # <Value u'value' (19:39)> -> __condition
            __token = 1078
            try:
                __zt_tmp = __attrs_140168037917456
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047246672
                __attrs_140168047246672 = _static_140168257770128

                # <Value u'not:fullname_mode' (20:31)> -> __condition
                __token = 1117
                try:
                    __zt_tmp = __attrs_140168047246672
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('not', u'fullname_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047245456
                    __default_140168047245456 = _DEFAULT_MARKER

                    # <Value u'python: view_format % value' (21:29)> -> __cache_140168037917200
                    __token = 1165
                    try:
                        __zt_tmp = __attrs_140168047246672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037917200 = _static_140168208991440('python', u' view_format % value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python: view_format % value' (21:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aaa3f10> -> __condition
                    __expression = __cache_140168037917200

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168037917200
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047245392
                __attrs_140168047245392 = _static_140168257770128

                # <Value u'fullname_mode' (22:31)> -> __condition
                __token = 1227
                try:
                    __zt_tmp = __attrs_140168047245392
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'fullname_mode', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047246416
                    __default_140168047246416 = _DEFAULT_MARKER

                    # <Value u'fullname' (23:29)> -> __cache_140168047246608
                    __token = 1271
                    try:
                        __zt_tmp = __attrs_140168047245392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047246608 = _static_140168208991440('path', u'fullname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'fullname' (23:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aaa3a10> -> __condition
                    __expression = __cache_140168047246608

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168047246608
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n        ')
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047244304
            __attrs_140168047244304 = _static_140168257770128

            # <Value u'not:value' (26:29)> -> __condition
            __token = 1339
            try:
                __zt_tmp = __attrs_140168047244304
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('not', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            __append(u'\n      ')
            if (__backup_fullname_mode_140168026288848 is __marker):
                del econtext['fullname_mode']
            else:
                econtext['fullname_mode'] = __backup_fullname_mode_140168026288848
            if (__backup_view_format_140168036765200 is __marker):
                del econtext['view_format']
            else:
                econtext['view_format'] = __backup_view_format_140168036765200
            if (__backup_entry_mode_140168047810192 is __marker):
                del econtext['entry_mode']
            else:
                econtext['entry_mode'] = __backup_entry_mode_140168047810192
            if (__backup_fullname_140168015698448 is __marker):
                del econtext['fullname']
            else:
                econtext['fullname'] = __backup_fullname_140168015698448
            if (__backup_fullname_140168037304976 is __marker):
                del econtext['fullname']
            else:
                econtext['fullname'] = __backup_fullname_140168037304976
            if (__backup_lastname_140168037311120 is __marker):
                del econtext['lastname']
            else:
                econtext['lastname'] = __backup_lastname_140168037311120
            if (__backup_middlename_140168036813520 is __marker):
                del econtext['middlename']
            else:
                econtext['middlename'] = __backup_middlename_140168036813520
            if (__backup_firstname_140168036940304 is __marker):
                del econtext['firstname']
            else:
                econtext['firstname'] = __backup_firstname_140168036940304
            if (__backup_value_140168083127824 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168083127824
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036939088
            __attrs_140168036939088 = _static_140168257770128
            __previous_i18n_domain_140168036939472 = __i18n_domain
            __i18n_domain = u'senaite.patient'
            __backup_macroname_140168057354832 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a0cf1d0> name=None at 7f7b6a0cf410> -> __value
            __value = _static_140168036938192
            econtext['macroname'] = __value

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140168036939088
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057354832 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057354832
            __i18n_domain = __previous_i18n_domain_140168036939472
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_view': render_view, 'render': render, }