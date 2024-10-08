# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.patient/src/senaite/patient/skins/templates/senaite_patient_widgets/agedobwidget.pt'

__tokens = {1982: (u'python:field.getEditAccessor(here)()', 46, 33), 2060: (u' python:here.session_restore_value(fieldName, values', 47, 40), 2146: (u's python:session_values or valu', 48, 31), 2208: (u'ob python: values', 49, 27), 2265: (u'ted python: value', 50, 35), 2323: (u'ated python: valu', 51, 35), 2382: (u'years string:${fieldName}.years:ignore_empty:', 52, 35), 2470: (u'months string:${fieldName}.months:ignore_empty', 53, 35), 2557: (u'ld_days string:${fieldName}.days:ignore_empt', 54, 32), 2641: (u'ield_dob string:${fieldName}.dob:ignore_emp', 55, 30), 2729: (u'_selector string:${fieldName}.selector:ignore_em', 56, 34), 2828: (u'inal_value string:${fieldName}.original:ignore_e', 57, 39), 2912: (u'   required field/requ', 58, 23), 2973: (u' current_age python:field.', 59, 25), 3032: (u'        years python:current_age.years if curre', 60, 18), 3113: (u'        months python:current_age.months if curr', 61, 18), 3193: (u'           days python:current_age.days if cur', 62, 15), 3280: (u'   age_supported python:widget.i', 63, 23), 3350: (u'       years_only python:widg', 64, 19), 3417: (u'        years_only python:years_only and y', 65, 18), 3498: (u'        show_months p', 66, 18), 3556: (u'           show_days ', 67, 15), 3696: (u"python:required and '1' or '0'", 70, 43), 3771: (u' string:${fieldName', 71, 43), 3846: (u'required', 72, 52), 3960: (u'age_supported', 75, 54), 4115: (u'string:${fieldName}_age_selector', 80, 33), 4176: (u' python:age_selecte', 81, 27), 4221: (u'e string:${subfield_selecto', 82, 23), 4294: (u'string:${fieldName}_age_selector', 83, 39), 4518: (u'string:${fieldName}_dob_selector', 90, 33), 4579: (u' python:not age_selecte', 91, 27), 4628: (u'e string:${subfield_selecto', 92, 23), 4701: (u'string:${fieldName}_dob_selector', 93, 39), 5078: (u'age_supported', 101, 30), 4926: (u'string:${fieldName}_age_controls', 99, 34), 4996: (u" python:'display:none' if not age_selected else '", 100, 36), 5349: (u'string:${subfield_years}', 107, 43), 5611: (u'string:${subfield_years}', 112, 40), 5668: (u' string:${subfield_years', 113, 31), 5726: (u'e yea', 114, 31), 5768: (u"ed python:required and 'required' or N", 115, 33), 5912: (u'show_months', 118, 67), 6017: (u'string:${subfield_months}', 120, 43), 6392: (u'e mont', 127, 31), 6275: (u'string:${subfield_months}', 125, 40), 6333: (u' string:${subfield_months', 126, 31), 6431: (u"pe python: 'number' if show_months else 'hidd", 128, 29), 6580: (u'show_days', 131, 67), 6683: (u'string:${subfield_days}', 133, 43), 7050: (u'e da', 140, 31), 6937: (u'string:${subfield_days}', 138, 40), 6993: (u' string:${subfield_days', 139, 31), 7087: (u"pe python: 'number' if show_days else 'hidd", 141, 29), 7395: (u"python: widget.get_date(dob) if dob else ''", 148, 33), 7244: (u'string:${fieldName}_dob_controls', 146, 34), 7314: (u" python:'display:none' if age_selected else '", 147, 36), 7668: (u"python: 'is-invalid' if dob_estimated else ''", 152, 47), 7760: (u' python: widget.attrs(here, field', 153, 45), 8177: (u'     python:widget_', 160, 20), 7863: (u'string:${subfield_dob}', 155, 28), 7916: (u' string:${subfield_dob', 156, 29), 7973: (u"d python:required and 'required' or No", 157, 32), 8043: (u'ue python: va', 158, 28), 8088: (u"ass python: 'form-control form-control-sm {}'.format(invalid_cl", 159, 27), 8240: (u'dob_estimated', 162, 34), 8556: (u'string:${subfield_original_value}', 170, 38), 8630: (u' string:${subfield_original_value', 171, 39), 8705: (u'e string:${valu', 172, 39), 9234: (u'string:${fieldName}-dob-fallback', 180, 38), 9297: (u' string:${fieldName}-dob-fallback:recor', 181, 29), 9368: (u'e string:${valu', 182, 29), 9541: (u'context/widgets/string/macros/edit', 189, 28), 9541: (u'context/widgets/string/macros/edit', 189, 28), 425: (u'python:field.getAccessor(here)()', 11, 31), 486: (u' python: values[0', 12, 27), 541: (u'd python: values[', 13, 35), 597: (u'ed python: values', 14, 35), 651: (u'age python:field.get_age(h', 15, 32), 708: (u'ears python:current_age.years if current_age el', 16, 25), 787: (u'onths python:current_age.months if current_age e', 17, 25), 865: (u'  days python:current_age.days if current_age ', 18, 22), 942: (u'  value python: widget.ulocalized_time(dob, context=here, request=request) if dob', 19, 22), 1095: (u'python:not dob_estimated', 22, 29), 1151: (u'value', 23, 29), 1248: (u'python:dob_estimated', 27, 38), 1302: (u'python:years', 28, 31), 1348: (u'years', 29, 31), 1495: (u'python:months', 32, 31), 1542: (u'months', 33, 31), 1692: (u'python:days', 36, 31), 1737: (u'days', 37, 31), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168015765072 = {u'class': u'input-group-prepend', }
_static_140168047842960 = {u'class': u'text-secondary', }
_static_140168036485584 = {u'class': u'input-group-text', u'for': u'string:${subfield_years}', }
_static_140168027539344 = {u'style': u'min-width:130px;max-width:130px', u'name': u'string:${subfield_dob}', u'required': u"python:required and 'required' or None", u'value': u'python: value', u'class': u"python: 'form-control form-control-sm {}'.format(invalid_class)", u'type': u'date', u'id': u'string:${subfield_dob}', }
_static_140168016890512 = {u'checked': u'python:age_selected', u'type': u'radio', u'id': u'string:${fieldName}_age_selector', u'value': u'age', u'name': u'string:${subfield_selector}', }
_static_140168047222160 = {u'class': u'text-secondary', }
_static_140168037782480 = {u'style': u'display:none;visibility:hidden;', u'type': u'text', u'id': u'string:${fieldName}-dob-fallback', u'value': u'string:${value}', u'name': u'string:${fieldName}-dob-fallback:record', }
_static_140168037692688 = {u'class': u'input-group-prepend ml-1', }
_static_140168036813776 = set([])
_static_140168037854352 = {u'name': u'string:${subfield_days}', u'min': u'0', u'max': u'31', u'value': u'', u'class': u'form-control form-control-sm', u'type': u"python: 'number' if show_days else 'hidden'", u'id': u'string:${subfield_days}', u'size': u'3', }
_static_140168037782288 = u'edit'
_static_140168208992144 = __C2ZContextWrapper
_static_140168015862160 = {u'data-fieldname': u'string:${fieldName}', u'data-required': u"python:required and '1' or '0'", u'class': u'field AgeDoBWidget text-left', }
_static_140168027538832 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168037692560 = {u'style': u"python:'display:none' if age_selected else ''", u'id': u'string:${fieldName}_dob_controls', }
_static_140168016891216 = {u'class': u'form-group mb-0', }
_static_140168036707088 = {u'class': u'input-group-prepend ml-1', }
_static_140168036672528 = {u'class': u'text-secondary', }
_static_140168037752656 = {u'type': u'hidden', u'id': u'string:${subfield_original_value}', u'value': u'string:${value}', u'name': u'string:${subfield_original_value}', }
_static_140168036485264 = {u'name': u'string:${subfield_years}', u'min': u'0', u'max': u'150', u'required': u"python:required and 'required' or None", u'value': u'years', u'class': u'form-control form-control-sm', u'type': u'number', u'id': u'string:${subfield_years}', u'size': u'3', }
_static_140168036805072 = {u'for': u'string:${fieldName}_dob_selector', }
_static_140168257770128 = {}
_static_140168036704528 = {u'name': u'string:${subfield_months}', u'min': u'0', u'max': u'12', u'value': u'', u'class': u'form-control form-control-sm', u'type': u"python: 'number' if show_months else 'hidden'", u'id': u'string:${subfield_months}', u'size': u'3', }
_static_140168015662672 = u'master'
_static_140168037750288 = {u'class': u'form-control form-control-sm text-danger border-danger', }
_static_140168208991440 = __compile_zt_expr
_static_140168015779856 = {u'for': u'string:${fieldName}_age_selector', }
_static_140168037852240 = {u'class': u'input-group-text', u'for': u'string:${subfield_days}', }
_static_140168036706320 = {u'class': u'input-group-text', u'for': u'string:${subfield_months}', }
_static_140168036803664 = {u'style': u"python:'display:none' if not age_selected else ''", u'id': u'string:${fieldName}_age_controls', }
_static_140168015761872 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168026368912 = {u'class': u'fieldErrorBox', }
_static_140168037252752 = {u'class': u'', }
_static_140168015781456 = {u'checked': u'python:not age_selected', u'type': u'radio', u'id': u'string:${fieldName}_dob_selector', u'value': u'dob', u'name': u'string:${subfield_selector}', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046973776
            __attrs_140168046973776 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026290128
            __attrs_140168026290128 = _static_140168257770128
            __backup_values_140168015660048 = get('values', __marker)

            # <Value u'python:field.getEditAccessor(here)()' (46:33)> -> __value
            __token = 1982
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['values'] = __value
            __backup_session_values_140168015662352 = get('session_values', __marker)

            # <Value u'python:here.session_restore_value(fieldName, values)' (47:40)> -> __value
            __token = 2060
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'here.session_restore_value(fieldName, values)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['session_values'] = __value
            __backup_values_140168037249232 = get('values', __marker)

            # <Value u'python:session_values or values' (48:31)> -> __value
            __token = 2146
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'session_values or values', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['values'] = __value
            __backup_dob_140168037252880 = get('dob', __marker)

            # <Value u'python: values[0]' (49:27)> -> __value
            __token = 2208
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' values[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['dob'] = __value
            __backup_age_selected_140168046974480 = get('age_selected', __marker)

            # <Value u'python: values[1]' (50:35)> -> __value
            __token = 2265
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' values[1]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['age_selected'] = __value
            __backup_dob_estimated_140168037251408 = get('dob_estimated', __marker)

            # <Value u'python: values[2]' (51:35)> -> __value
            __token = 2323
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' values[2]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['dob_estimated'] = __value
            __backup_subfield_years_140168037250512 = get('subfield_years', __marker)

            # <Value u'string:${fieldName}.years:ignore_empty:record' (52:35)> -> __value
            __token = 2382
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.years:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_years'] = __value
            __backup_subfield_months_140168046976272 = get('subfield_months', __marker)

            # <Value u'string:${fieldName}.months:ignore_empty:record' (53:35)> -> __value
            __token = 2470
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.months:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_months'] = __value
            __backup_subfield_days_140168046974736 = get('subfield_days', __marker)

            # <Value u'string:${fieldName}.days:ignore_empty:record' (54:32)> -> __value
            __token = 2557
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.days:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_days'] = __value
            __backup_subfield_dob_140168047220496 = get('subfield_dob', __marker)

            # <Value u'string:${fieldName}.dob:ignore_empty:record' (55:30)> -> __value
            __token = 2641
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.dob:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_dob'] = __value
            __backup_subfield_selector_140168047221968 = get('subfield_selector', __marker)

            # <Value u'string:${fieldName}.selector:ignore_empty:record' (56:34)> -> __value
            __token = 2729
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.selector:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_selector'] = __value
            __backup_subfield_original_value_140168047220880 = get('subfield_original_value', __marker)

            # <Value u'string:${fieldName}.original:ignore_empty:record' (57:39)> -> __value
            __token = 2828
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${fieldName}.original:ignore_empty:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['subfield_original_value'] = __value
            __backup_required_140168047221136 = get('required', __marker)

            # <Value u'field/required|nothing' (58:23)> -> __value
            __token = 2912
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'field/required|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['required'] = __value
            __backup_current_age_140168006674448 = get('current_age', __marker)

            # <Value u'python:field.get_age(here)' (59:25)> -> __value
            __token = 2973
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.get_age(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['current_age'] = __value
            __backup_years_140168006673488 = get('years', __marker)

            # <Value u"python:current_age.years if current_age else ''" (60:18)> -> __value
            __token = 3032
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"current_age.years if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['years'] = __value
            __backup_months_140168026288720 = get('months', __marker)

            # <Value u"python:current_age.months if current_age else ''" (61:18)> -> __value
            __token = 3113
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"current_age.months if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['months'] = __value
            __backup_days_140168026290384 = get('days', __marker)

            # <Value u"python:current_age.days if current_age else ''" (62:15)> -> __value
            __token = 3193
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"current_age.days if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['days'] = __value
            __backup_age_supported_140168026291984 = get('age_supported', __marker)

            # <Value u'python:widget.is_age_supported()' (63:23)> -> __value
            __token = 3280
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'widget.is_age_supported()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['age_supported'] = __value
            __backup_years_only_140168026290320 = get('years_only', __marker)

            # <Value u'python:widget.is_years_only()' (64:19)> -> __value
            __token = 3350
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'widget.is_years_only()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['years_only'] = __value
            __backup_years_only_140168026291792 = get('years_only', __marker)

            # <Value u'python:years_only and years and years >= 1' (65:18)> -> __value
            __token = 3417
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'years_only and years and years >= 1', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['years_only'] = __value
            __backup_show_months_140168026289360 = get('show_months', __marker)

            # <Value u'python:not years_only' (66:18)> -> __value
            __token = 3498
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'not years_only', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['show_months'] = __value
            __backup_show_days_140168026289872 = get('show_days', __marker)

            # <Value u'python:not years_only' (67:15)> -> __value
            __token = 3556
            try:
                __zt_tmp = __attrs_140168026290128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'not years_only', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['show_days'] = __value
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68cb5990> name=None at 7f7b68cb5d10> -> __attrs_140168037628496
            __attrs_140168037628496 = _static_140168015862160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field AgeDoBWidget text-left"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037626256
            __default_140168037626256 = _DEFAULT_MARKER

            # <Substitution u"python:required and '1' or '0'" (70:43)> -> __attr_data_required
            __token = 3696
            try:
                __zt_tmp = __attrs_140168037628496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_required = _static_140168208991440('python', u"required and '1' or '0'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_required = __quote(__attr_data_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_required is not None):
                __append((u' data-required="%s"' % __attr_data_required))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037626960
            __default_140168037626960 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}' (71:43)> -> __attr_data_fieldname
            __token = 3771
            try:
                __zt_tmp = __attrs_140168037628496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140168208991440('string', u'${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_fieldname is not None):
                __append((u' data-fieldname="%s"' % __attr_data_fieldname))
            __append(u'>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b696bab90> name=None at 7f7b696ba210> -> __attrs_140168016891088
            __attrs_140168016891088 = _static_140168026368912

            # <Value u'required' (72:52)> -> __condition
            __token = 3846
            try:
                __zt_tmp = __attrs_140168016891088
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="fieldErrorBox"></div>')
            __append(u'\n\n          <!-- Age / DoB toggle radio -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b68db0d50> name=None at 7f7b68db0790> -> __attrs_140168016890256
            __attrs_140168016890256 = _static_140168016891216

            # <Value u'age_supported' (75:54)> -> __condition
            __token = 3960
            try:
                __zt_tmp = __attrs_140168016890256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'age_supported', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="form-group mb-0">\n            <!-- age selector -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68db0a90> name=None at 7f7b68db0f10> -> __attrs_140168015780752
                __attrs_140168015780752 = _static_140168016890512

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="radio" value="age"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037225488
                __default_140168037225488 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_age_selector' (80:33)> -> __attr_id
                __token = 4115
                try:
                    __zt_tmp = __attrs_140168015780752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${fieldName}_age_selector', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015778128
                __default_140168015778128 = _DEFAULT_MARKER

                # <Boolean u'python:age_selected' (81:27)> -> __attr_checked
                __token = 4176
                try:
                    __zt_tmp = __attrs_140168015780752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_140168208991440('python', u'age_selected', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = u'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((u' checked="%s"' % __attr_checked))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015778640
                __default_140168015778640 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_selector}' (82:23)> -> __attr_name
                __token = 4221
                try:
                    __zt_tmp = __attrs_140168015780752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_selector}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))
                __append(u' />\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68ca1810> name=None at 7f7b68ca19d0> -> __attrs_140168015781264
                __attrs_140168015781264 = _static_140168015779856

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015777936
                __default_140168015777936 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_age_selector' (83:39)> -> __attr_for
                __token = 4294
                try:
                    __zt_tmp = __attrs_140168015781264
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140168208991440('string', u'${fieldName}_age_selector', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u'>')
                __stream_140168015778256 = []
                __append_140168015778256 = __stream_140168015778256.append
                __append_140168015778256(u'Age')
                __msgid_140168015778256 = __re_whitespace(''.join(__stream_140168015778256)).strip()
                if __msgid_140168015778256:
                    __append(translate(__msgid_140168015778256, mapping=None, default=__msgid_140168015778256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n\n            <!-- dob selector -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68ca1e50> name=None at 7f7b68ca1890> -> __attrs_140168036803408
                __attrs_140168036803408 = _static_140168015781456

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="radio" value="dob"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036804112
                __default_140168036804112 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_dob_selector' (90:33)> -> __attr_id
                __token = 4518
                try:
                    __zt_tmp = __attrs_140168036803408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${fieldName}_dob_selector', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036803152
                __default_140168036803152 = _DEFAULT_MARKER

                # <Boolean u'python:not age_selected' (91:27)> -> __attr_checked
                __token = 4579
                try:
                    __zt_tmp = __attrs_140168036803408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_140168208991440('python', u'not age_selected', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = u'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((u' checked="%s"' % __attr_checked))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036803280
                __default_140168036803280 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_selector}' (92:23)> -> __attr_name
                __token = 4628
                try:
                    __zt_tmp = __attrs_140168036803408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_selector}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))
                __append(u' />\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6a0ae9d0> name=None at 7f7b6a0ae8d0> -> __attrs_140168036805648
                __attrs_140168036805648 = _static_140168036805072

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036803088
                __default_140168036803088 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_dob_selector' (93:39)> -> __attr_for
                __token = 4701
                try:
                    __zt_tmp = __attrs_140168036805648
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140168208991440('string', u'${fieldName}_dob_selector', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u'>')
                __stream_140168036806544 = []
                __append_140168036806544 = __stream_140168036806544.append
                __append_140168036806544(u'Date of Birth')
                __msgid_140168036806544 = __re_whitespace(''.join(__stream_140168036806544)).strip()
                if __msgid_140168036806544:
                    __append(translate(__msgid_140168036806544, mapping=None, default=__msgid_140168036806544, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n\n          </div>')
            __append(u'\n\n          <!-- Age input area (keep outer container for visibility toggle) -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a0ae450> name=None at 7f7b6a0ae890> -> __attrs_140168037650576
            __attrs_140168037650576 = _static_140168036803664

            # <Value u'age_supported' (101:30)> -> __condition
            __token = 5078
            try:
                __zt_tmp = __attrs_140168037650576
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'age_supported', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037652752
                __default_140168037652752 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}_age_controls' (99:34)> -> __attr_id
                __token = 4926
                try:
                    __zt_tmp = __attrs_140168037650576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${fieldName}_age_controls', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037652816
                __default_140168037652816 = _DEFAULT_MARKER

                # <Substitution u"python:'display:none' if not age_selected else ''" (100:36)> -> __attr_style
                __token = 4996
                try:
                    __zt_tmp = __attrs_140168037650576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_style = _static_140168208991440('python', u"'display:none' if not age_selected else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_style is not None):
                    __append((u' style="%s"' % __attr_style))
                __append(u'>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68c9d1d0> name=None at 7f7b68c9dfd0> -> __attrs_140168015762448
                __attrs_140168015762448 = _static_140168015761872

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n\n              <!-- Years -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b68c9de50> name=None at 7f7b68c9d910> -> __attrs_140168015763344
                __attrs_140168015763344 = _static_140168015765072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6a0609d0> name=None at 7f7b68c9d190> -> __attrs_140168036485392
                __attrs_140168036485392 = _static_140168036485584

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label class="input-group-text"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036484944
                __default_140168036484944 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_years}' (107:43)> -> __attr_for
                __token = 5349
                try:
                    __zt_tmp = __attrs_140168036485392
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140168208991440('string', u'${subfield_years}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u'>')
                __stream_140168015762960 = []
                __append_140168015762960 = __stream_140168015762960.append
                __append_140168015762960(u'Years')
                __msgid_140168015762960 = __re_whitespace(''.join(__stream_140168015762960)).strip()
                if __msgid_140168015762960:
                    __append(translate(__msgid_140168015762960, mapping=None, default=__msgid_140168015762960, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n              </div>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a060890> name=None at 7f7b68c9de10> -> __attrs_140168036705744
                __attrs_140168036705744 = _static_140168036485264

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="number" min=\'0\' max=\'150\' size=\'3\' class="form-control form-control-sm"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036484560
                __default_140168036484560 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_years}' (112:40)> -> __attr_id
                __token = 5611
                try:
                    __zt_tmp = __attrs_140168036705744
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_years}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046894608
                __default_140168046894608 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_years}' (113:31)> -> __attr_name
                __token = 5668
                try:
                    __zt_tmp = __attrs_140168036705744
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_years}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046893392
                __default_140168046893392 = _DEFAULT_MARKER

                # <Substitution u'years' (114:31)> -> __attr_value
                __token = 5726
                try:
                    __zt_tmp = __attrs_140168036705744
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'years', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046894160
                __default_140168046894160 = _DEFAULT_MARKER

                # <Substitution u"python:required and 'required' or None" (115:33)> -> __attr_required
                __token = 5768
                try:
                    __zt_tmp = __attrs_140168036705744
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_required = _static_140168208991440('python', u"required and 'required' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_required is not None):
                    __append((u' required="%s"' % __attr_required))
                __append(u'/>\n\n              <!-- Months -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a096b10> name=None at 7f7b6a096f90> -> __attrs_140168036705424
                __attrs_140168036705424 = _static_140168036707088

                # <Value u'show_months' (118:67)> -> __condition
                __token = 5912
                try:
                    __zt_tmp = __attrs_140168036705424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'show_months', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend ml-1">\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a096810> name=None at 7f7b6a096790> -> __attrs_140168036705168
                    __attrs_140168036705168 = _static_140168036706320

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label class="input-group-text"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036705552
                    __default_140168036705552 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_months}' (120:43)> -> __attr_for
                    __token = 6017
                    try:
                        __zt_tmp = __attrs_140168036705168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140168208991440('string', u'${subfield_months}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((u' for="%s"' % __attr_for))
                    __append(u'>')
                    __stream_140168036706064 = []
                    __append_140168036706064 = __stream_140168036706064.append
                    __append_140168036706064(u'Months')
                    __msgid_140168036706064 = __re_whitespace(''.join(__stream_140168036706064)).strip()
                    if __msgid_140168036706064:
                        __append(translate(__msgid_140168036706064, mapping=None, default=__msgid_140168036706064, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</label>\n              </div>')
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a096110> name=None at 7f7b6a0966d0> -> __attrs_140168037693200
                __attrs_140168037693200 = _static_140168036704528

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037694864
                __default_140168037694864 = _DEFAULT_MARKER

                # <Substitution u'months' (127:31)> -> __attr_value
                __token = 6392
                try:
                    __zt_tmp = __attrs_140168037693200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'months', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, "'", '&#39;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u" value='%s'" % __attr_value))
                __append(u' min=\'0\' max=\'12\' size=\'3\' class="form-control form-control-sm"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037694032
                __default_140168037694032 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_months}' (125:40)> -> __attr_id
                __token = 6275
                try:
                    __zt_tmp = __attrs_140168037693200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_months}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037693776
                __default_140168037693776 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_months}' (126:31)> -> __attr_name
                __token = 6333
                try:
                    __zt_tmp = __attrs_140168037693200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_months}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037693456
                __default_140168037693456 = _DEFAULT_MARKER

                # <Substitution u"python: 'number' if show_months else 'hidden'" (128:29)> -> __attr_type
                __token = 6431
                try:
                    __zt_tmp = __attrs_140168037693200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_type = _static_140168208991440('python', u" 'number' if show_months else 'hidden'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_type = __quote(__attr_type, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_type is not None):
                    __append((u' type="%s"' % __attr_type))
                __append(u'/>\n\n              <!-- Days -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a187510> name=None at 7f7b6a1874d0> -> __attrs_140168037853712
                __attrs_140168037853712 = _static_140168037692688

                # <Value u'show_days' (131:67)> -> __condition
                __token = 6580
                try:
                    __zt_tmp = __attrs_140168037853712
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'show_days', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend ml-1">\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a1ae450> name=None at 7f7b6a1aeed0> -> __attrs_140168037852688
                    __attrs_140168037852688 = _static_140168037852240

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label class="input-group-text"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037851216
                    __default_140168037851216 = _DEFAULT_MARKER

                    # <Substitution u'string:${subfield_days}' (133:43)> -> __attr_for
                    __token = 6683
                    try:
                        __zt_tmp = __attrs_140168037852688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140168208991440('string', u'${subfield_days}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((u' for="%s"' % __attr_for))
                    __append(u'>')
                    __stream_140168037854992 = []
                    __append_140168037854992 = __stream_140168037854992.append
                    __append_140168037854992(u'Days')
                    __msgid_140168037854992 = __re_whitespace(''.join(__stream_140168037854992)).strip()
                    if __msgid_140168037854992:
                        __append(translate(__msgid_140168037854992, mapping=None, default=__msgid_140168037854992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</label>\n              </div>')
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1aec90> name=None at 7f7b6a1ae390> -> __attrs_140168027221840
                __attrs_140168027221840 = _static_140168037854352

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027218512
                __default_140168027218512 = _DEFAULT_MARKER

                # <Substitution u'days' (140:31)> -> __attr_value
                __token = 7050
                try:
                    __zt_tmp = __attrs_140168027221840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'days', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, "'", '&#39;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u" value='%s'" % __attr_value))
                __append(u' min=\'0\' max=\'31\' size=\'3\' class="form-control form-control-sm"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027219664
                __default_140168027219664 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_days}' (138:40)> -> __attr_id
                __token = 6937
                try:
                    __zt_tmp = __attrs_140168027221840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'${subfield_days}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027218768
                __default_140168027218768 = _DEFAULT_MARKER

                # <Substitution u'string:${subfield_days}' (139:31)> -> __attr_name
                __token = 6993
                try:
                    __zt_tmp = __attrs_140168027221840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${subfield_days}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027220496
                __default_140168027220496 = _DEFAULT_MARKER

                # <Substitution u"python: 'number' if show_days else 'hidden'" (141:29)> -> __attr_type
                __token = 7087
                try:
                    __zt_tmp = __attrs_140168027221840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_type = _static_140168208991440('python', u" 'number' if show_days else 'hidden'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_type = __quote(__attr_type, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_type is not None):
                    __append((u' type="%s"' % __attr_type))
                __append(u'/>\n            </div>\n          </div>')
            __append(u'\n\n          <!-- DoB input field -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a187490> name=None at 7f7b6a187410> -> __attrs_140168027221072
            __attrs_140168027221072 = _static_140168037692560
            __backup_value_140168026288912 = get('value', __marker)

            # <Value u"python: widget.get_date(dob) if dob else ''" (148:33)> -> __value
            __token = 7395
            try:
                __zt_tmp = __attrs_140168027221072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" widget.get_date(dob) if dob else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027221520
            __default_140168027221520 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}_dob_controls' (146:34)> -> __attr_id
            __token = 7244
            try:
                __zt_tmp = __attrs_140168027221072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'${fieldName}_dob_controls', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027220752
            __default_140168027220752 = _DEFAULT_MARKER

            # <Substitution u"python:'display:none' if age_selected else ''" (147:36)> -> __attr_style
            __token = 7314
            try:
                __zt_tmp = __attrs_140168027221072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140168208991440('python', u"'display:none' if age_selected else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))
            __append(u'>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b697d8590> name=None at 7f7b697d8190> -> __attrs_140168027537488
            __attrs_140168027537488 = _static_140168027538832

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b697d8790> name=None at 7f7b697d83d0> -> __attrs_140168037750992
            __attrs_140168037750992 = _static_140168027539344
            __backup_invalid_class_140168016931728 = get('invalid_class', __marker)

            # <Value u"python: 'is-invalid' if dob_estimated else ''" (152:47)> -> __value
            __token = 7668
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u" 'is-invalid' if dob_estimated else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['invalid_class'] = __value
            __backup_widget_attrs_140168046974672 = get('widget_attrs', __marker)

            # <Value u'python: widget.attrs(here, field)' (153:45)> -> __value
            __token = 7760
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' widget.attrs(here, field)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['widget_attrs'] = __value

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Value u'python:widget_attrs' (160:20)> -> __cache_140168037751824
            __token = 8177
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037751824 = _static_140168208991440('python', u'widget_attrs', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if (u'type' not in __chain(__cache_140168037751824)):
                __append(u' type="date"')
            if (u'style' not in __chain(__cache_140168037751824)):
                __append(u' style="min-width:130px;max-width:130px"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027540624
            __default_140168027540624 = _DEFAULT_MARKER

            # <Substitution u'string:${subfield_dob}' (155:28)> -> __attr_id
            __token = 7863
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'${subfield_dob}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_id is not None) and (u'id' not in __chain(__cache_140168037751824))):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027540112
            __default_140168027540112 = _DEFAULT_MARKER

            # <Substitution u'string:${subfield_dob}' (156:29)> -> __attr_name
            __token = 7916
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('string', u'${subfield_dob}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_name is not None) and (u'name' not in __chain(__cache_140168037751824))):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027540368
            __default_140168027540368 = _DEFAULT_MARKER

            # <Substitution u"python:required and 'required' or None" (157:32)> -> __attr_required
            __token = 7973
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_140168208991440('python', u"required and 'required' or None", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_required is not None) and (u'required' not in __chain(__cache_140168037751824))):
                __append((u' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037748944
            __default_140168037748944 = _DEFAULT_MARKER

            # <Substitution u'python: value' (158:28)> -> __attr_value
            __token = 8043
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('python', u' value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_value is not None) and (u'value' not in __chain(__cache_140168037751824))):
                __append((u' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037752784
            __default_140168037752784 = _DEFAULT_MARKER

            # <Substitution u"python: 'form-control form-control-sm {}'.format(invalid_class)" (159:27)> -> __attr_class
            __token = 8088
            try:
                __zt_tmp = __attrs_140168037750992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('python', u" 'form-control form-control-sm {}'.format(invalid_class)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and (u'class' not in __chain(__cache_140168037751824))):
                __append((u' class="%s"' % __attr_class))
            __attr_140168037751568 = __cache_140168037751824
            for (name, value, ) in __attr_140168037751568.items():
                if ((name not in _static_140168036813776) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'/>')
            if (__backup_widget_attrs_140168046974672 is __marker):
                del econtext['widget_attrs']
            else:
                econtext['widget_attrs'] = __backup_widget_attrs_140168046974672
            if (__backup_invalid_class_140168016931728 is __marker):
                del econtext['invalid_class']
            else:
                econtext['invalid_class'] = __backup_invalid_class_140168016931728
            __append(u'\n\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6a195610> name=None at 7f7b6a195510> -> __attrs_140168037750672
            __attrs_140168037750672 = _static_140168037750288

            # <Value u'dob_estimated' (162:34)> -> __condition
            __token = 8240
            try:
                __zt_tmp = __attrs_140168037750672
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'dob_estimated', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="form-control form-control-sm text-danger border-danger">\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037751952
                __attrs_140168037751952 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168037752400 = []
                __append_140168037752400 = __stream_140168037752400.append
                __append_140168037752400(u'Estimated')
                __msgid_140168037752400 = __re_whitespace(''.join(__stream_140168037752400)).strip()
                if __msgid_140168037752400:
                    __append(translate(__msgid_140168037752400, mapping=None, default=__msgid_140168037752400, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n              </div>')
            __append(u'\n            </div>\n\n            <!-- Keep track of the old value -->\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b6a195f50> name=None at 7f7b6a195d90> -> __attrs_140168037782864
            __attrs_140168037782864 = _static_140168037752656

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037784400
            __default_140168037784400 = _DEFAULT_MARKER

            # <Substitution u'string:${subfield_original_value}' (170:38)> -> __attr_id
            __token = 8556
            try:
                __zt_tmp = __attrs_140168037782864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'${subfield_original_value}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037781904
            __default_140168037781904 = _DEFAULT_MARKER

            # <Substitution u'string:${subfield_original_value}' (171:39)> -> __attr_name
            __token = 8630
            try:
                __zt_tmp = __attrs_140168037782864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('string', u'${subfield_original_value}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037782096
            __default_140168037782096 = _DEFAULT_MARKER

            # <Substitution u'string:${value}' (172:39)> -> __attr_value
            __token = 8705
            try:
                __zt_tmp = __attrs_140168037782864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('string', u'${value}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u"/>\n\n            <!-- Field not visible for when the value is set automatically by\n                 others through JS. When a value is set to this field, agedob widget\n                 automatically updates the value from the dob_control and selects\n                 the proper radiobutton. Note we don't use a hidden field here, cause\n                 'onchange' is not triggered for hidden fields -->\n            ")

            # <Static value=<_ast.Dict object at 0x7f7b6a19d3d0> name=None at 7f7b6a19d390> -> __attrs_140168037878736
            __attrs_140168037878736 = _static_140168037782480

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="text" style="display:none;visibility:hidden;"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037783312
            __default_140168037783312 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}-dob-fallback' (180:38)> -> __attr_id
            __token = 9234
            try:
                __zt_tmp = __attrs_140168037878736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'${fieldName}-dob-fallback', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037785232
            __default_140168037785232 = _DEFAULT_MARKER

            # <Substitution u'string:${fieldName}-dob-fallback:record' (181:29)> -> __attr_name
            __token = 9297
            try:
                __zt_tmp = __attrs_140168037878736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('string', u'${fieldName}-dob-fallback:record', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037879376
            __default_140168037879376 = _DEFAULT_MARKER

            # <Substitution u'string:${value}' (182:29)> -> __attr_value
            __token = 9368
            try:
                __zt_tmp = __attrs_140168037878736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('string', u'${value}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n          </div>')
            if (__backup_value_140168026288912 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168026288912
            __append(u'\n        </div>\n      ')
            if (__backup_show_days_140168026289872 is __marker):
                del econtext['show_days']
            else:
                econtext['show_days'] = __backup_show_days_140168026289872
            if (__backup_show_months_140168026289360 is __marker):
                del econtext['show_months']
            else:
                econtext['show_months'] = __backup_show_months_140168026289360
            if (__backup_years_only_140168026291792 is __marker):
                del econtext['years_only']
            else:
                econtext['years_only'] = __backup_years_only_140168026291792
            if (__backup_years_only_140168026290320 is __marker):
                del econtext['years_only']
            else:
                econtext['years_only'] = __backup_years_only_140168026290320
            if (__backup_age_supported_140168026291984 is __marker):
                del econtext['age_supported']
            else:
                econtext['age_supported'] = __backup_age_supported_140168026291984
            if (__backup_days_140168026290384 is __marker):
                del econtext['days']
            else:
                econtext['days'] = __backup_days_140168026290384
            if (__backup_months_140168026288720 is __marker):
                del econtext['months']
            else:
                econtext['months'] = __backup_months_140168026288720
            if (__backup_years_140168006673488 is __marker):
                del econtext['years']
            else:
                econtext['years'] = __backup_years_140168006673488
            if (__backup_current_age_140168006674448 is __marker):
                del econtext['current_age']
            else:
                econtext['current_age'] = __backup_current_age_140168006674448
            if (__backup_required_140168047221136 is __marker):
                del econtext['required']
            else:
                econtext['required'] = __backup_required_140168047221136
            if (__backup_subfield_original_value_140168047220880 is __marker):
                del econtext['subfield_original_value']
            else:
                econtext['subfield_original_value'] = __backup_subfield_original_value_140168047220880
            if (__backup_subfield_selector_140168047221968 is __marker):
                del econtext['subfield_selector']
            else:
                econtext['subfield_selector'] = __backup_subfield_selector_140168047221968
            if (__backup_subfield_dob_140168047220496 is __marker):
                del econtext['subfield_dob']
            else:
                econtext['subfield_dob'] = __backup_subfield_dob_140168047220496
            if (__backup_subfield_days_140168046974736 is __marker):
                del econtext['subfield_days']
            else:
                econtext['subfield_days'] = __backup_subfield_days_140168046974736
            if (__backup_subfield_months_140168046976272 is __marker):
                del econtext['subfield_months']
            else:
                econtext['subfield_months'] = __backup_subfield_months_140168046976272
            if (__backup_subfield_years_140168037250512 is __marker):
                del econtext['subfield_years']
            else:
                econtext['subfield_years'] = __backup_subfield_years_140168037250512
            if (__backup_dob_estimated_140168037251408 is __marker):
                del econtext['dob_estimated']
            else:
                econtext['dob_estimated'] = __backup_dob_estimated_140168037251408
            if (__backup_age_selected_140168046974480 is __marker):
                del econtext['age_selected']
            else:
                econtext['age_selected'] = __backup_age_selected_140168046974480
            if (__backup_dob_140168037252880 is __marker):
                del econtext['dob']
            else:
                econtext['dob'] = __backup_dob_140168037252880
            if (__backup_values_140168037249232 is __marker):
                del econtext['values']
            else:
                econtext['values'] = __backup_values_140168037249232
            if (__backup_session_values_140168015662352 is __marker):
                del econtext['session_values']
            else:
                econtext['session_values'] = __backup_session_values_140168015662352
            if (__backup_values_140168015660048 is __marker):
                del econtext['values']
            else:
                econtext['values'] = __backup_values_140168015660048
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036672400
            __attrs_140168036672400 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037782544
            __attrs_140168037782544 = _static_140168257770128
            __backup_macroname_140168055966128 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a19d310> name=None at 7f7b6a19d490> -> __value
            __value = _static_140168037782288
            econtext['macroname'] = __value

            # <Value u'context/widgets/string/macros/edit' (189:28)> -> __macro
            __token = 9541
            try:
                __zt_tmp = __attrs_140168037782544
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 9541
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055966128 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055966128
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015660112
            __attrs_140168015660112 = _static_140168257770128
            __append(u'\n      ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046975312
                __attrs_140168046975312 = _static_140168257770128
                __backup_values_140168015661648 = get('values', __marker)

                # <Value u'python:field.getAccessor(here)()' (11:31)> -> __value
                __token = 425
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'field.getAccessor(here)()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['values'] = __value
                __backup_dob_140168046976080 = get('dob', __marker)

                # <Value u'python: values[0]' (12:27)> -> __value
                __token = 486
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u' values[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['dob'] = __value
                __backup_age_selected_140168046973456 = get('age_selected', __marker)

                # <Value u'python: values[1]' (13:35)> -> __value
                __token = 541
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u' values[1]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['age_selected'] = __value
                __backup_dob_estimated_140168046973584 = get('dob_estimated', __marker)

                # <Value u'python: values[2]' (14:35)> -> __value
                __token = 597
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u' values[2]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['dob_estimated'] = __value
                __backup_current_age_140168046975632 = get('current_age', __marker)

                # <Value u'python:field.get_age(here)' (15:32)> -> __value
                __token = 651
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'field.get_age(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['current_age'] = __value
                __backup_years_140168046973264 = get('years', __marker)

                # <Value u"python:current_age.years if current_age else ''" (16:25)> -> __value
                __token = 708
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"current_age.years if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['years'] = __value
                __backup_months_140168046974800 = get('months', __marker)

                # <Value u"python:current_age.months if current_age else ''" (17:25)> -> __value
                __token = 787
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"current_age.months if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['months'] = __value
                __backup_days_140168046976784 = get('days', __marker)

                # <Value u"python:current_age.days if current_age else ''" (18:22)> -> __value
                __token = 865
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"current_age.days if current_age else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['days'] = __value
                __backup_value_140168046975760 = get('value', __marker)

                # <Value u"python: widget.ulocalized_time(dob, context=here, request=request) if dob else ''" (19:22)> -> __value
                __token = 942
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" widget.ulocalized_time(dob, context=here, request=request) if dob else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>\n\n        <!-- Date of birth -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037251728
                __attrs_140168037251728 = _static_140168257770128

                # <Value u'python:not dob_estimated' (22:29)> -> __condition
                __token = 1095
                try:
                    __zt_tmp = __attrs_140168037251728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'not dob_estimated', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037252432
                    __attrs_140168037252432 = _static_140168257770128

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037252176
                    __default_140168037252176 = _DEFAULT_MARKER

                    # <Value u'value' (23:29)> -> __cache_140168037250192
                    __token = 1151
                    try:
                        __zt_tmp = __attrs_140168037252432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037250192 = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'value' (23:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a11b790> -> __condition
                    __expression = __cache_140168037250192

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span/>')
                    else:
                        __content = __cache_140168037250192
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n        </span>')
                __append(u'\n\n        <!-- Age (estimated) -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a11be90> name=None at 7f7b6a11bcd0> -> __attrs_140168037250256
                __attrs_140168037250256 = _static_140168037252752

                # <Value u'python:dob_estimated' (27:38)> -> __condition
                __token = 1248
                try:
                    __zt_tmp = __attrs_140168037250256
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'dob_estimated', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047220176
                    __attrs_140168047220176 = _static_140168257770128

                    # <Value u'python:years' (28:31)> -> __condition
                    __token = 1302
                    try:
                        __zt_tmp = __attrs_140168047220176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'years', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047221392
                        __attrs_140168047221392 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047222352
                        __default_140168047222352 = _DEFAULT_MARKER

                        # <Value u'years' (29:31)> -> __cache_140168047220816
                        __token = 1348
                        try:
                            __zt_tmp = __attrs_140168047221392
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047220816 = _static_140168208991440('path', u'years', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'years' (29:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa9df50> -> __condition
                        __expression = __cache_140168047220816

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>')
                        else:
                            __content = __cache_140168047220816
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa9dd90> name=None at 7f7b6aa9d310> -> __attrs_140168047220688
                        __attrs_140168047220688 = _static_140168047222160

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="text-secondary">')
                        __stream_140168047221904 = []
                        __append_140168047221904 = __stream_140168047221904.append
                        __append_140168047221904(u'Years')
                        __msgid_140168047221904 = __re_whitespace(''.join(__stream_140168047221904)).strip()
                        if u'patient_dob_years':
                            __append(translate(u'patient_dob_years', mapping=None, default=__msgid_140168047221904, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </span>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026342032
                    __attrs_140168026342032 = _static_140168257770128

                    # <Value u'python:months' (32:31)> -> __condition
                    __token = 1495
                    try:
                        __zt_tmp = __attrs_140168026342032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'months', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036671696
                        __attrs_140168036671696 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036674192
                        __default_140168036674192 = _DEFAULT_MARKER

                        # <Value u'months' (33:31)> -> __cache_140168036672208
                        __token = 1542
                        try:
                            __zt_tmp = __attrs_140168036671696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036672208 = _static_140168208991440('path', u'months', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'months' (33:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a08e110> -> __condition
                        __expression = __cache_140168036672208

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>')
                        else:
                            __content = __cache_140168036672208
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a08e410> name=None at 7f7b6a08e710> -> __attrs_140168036672144
                        __attrs_140168036672144 = _static_140168036672528

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="text-secondary">')
                        __stream_140168036672848 = []
                        __append_140168036672848 = __stream_140168036672848.append
                        __append_140168036672848(u'Months')
                        __msgid_140168036672848 = __re_whitespace(''.join(__stream_140168036672848)).strip()
                        if u'patient_dob_months':
                            __append(translate(u'patient_dob_months', mapping=None, default=__msgid_140168036672848, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </span>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036673488
                    __attrs_140168036673488 = _static_140168257770128

                    # <Value u'python:days' (36:31)> -> __condition
                    __token = 1692
                    try:
                        __zt_tmp = __attrs_140168036673488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'days', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047843728
                        __attrs_140168047843728 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047842640
                        __default_140168047842640 = _DEFAULT_MARKER

                        # <Value u'days' (37:31)> -> __cache_140168036672016
                        __token = 1737
                        try:
                            __zt_tmp = __attrs_140168047843728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036672016 = _static_140168208991440('path', u'days', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'days' (37:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab35250> -> __condition
                        __expression = __cache_140168036672016

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>')
                        else:
                            __content = __cache_140168036672016
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab35690> name=None at 7f7b6ab35190> -> __attrs_140168006675152
                        __attrs_140168006675152 = _static_140168047842960

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="text-secondary">')
                        __stream_140168047841616 = []
                        __append_140168047841616 = __stream_140168047841616.append
                        __append_140168047841616(u'Days')
                        __msgid_140168047841616 = __re_whitespace(''.join(__stream_140168047841616)).strip()
                        if u'patient_dob_days':
                            __append(translate(u'patient_dob_days', mapping=None, default=__msgid_140168047841616, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </span>')
                    __append(u'\n        </span>')
                __append(u'\n      </span>')
                if (__backup_value_140168046975760 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168046975760
                if (__backup_days_140168046976784 is __marker):
                    del econtext['days']
                else:
                    econtext['days'] = __backup_days_140168046976784
                if (__backup_months_140168046974800 is __marker):
                    del econtext['months']
                else:
                    econtext['months'] = __backup_months_140168046974800
                if (__backup_years_140168046973264 is __marker):
                    del econtext['years']
                else:
                    econtext['years'] = __backup_years_140168046973264
                if (__backup_current_age_140168046975632 is __marker):
                    del econtext['current_age']
                else:
                    econtext['current_age'] = __backup_current_age_140168046975632
                if (__backup_dob_estimated_140168046973584 is __marker):
                    del econtext['dob_estimated']
                else:
                    econtext['dob_estimated'] = __backup_dob_estimated_140168046973584
                if (__backup_age_selected_140168046973456 is __marker):
                    del econtext['age_selected']
                else:
                    econtext['age_selected'] = __backup_age_selected_140168046973456
                if (__backup_dob_140168046976080 is __marker):
                    del econtext['dob']
                else:
                    econtext['dob'] = __backup_dob_140168046976080
                if (__backup_values_140168015661648 is __marker):
                    del econtext['values']
                else:
                    econtext['values'] = __backup_values_140168015661648
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015662416
            __attrs_140168015662416 = _static_140168257770128
            __previous_i18n_domain_140168015659216 = __i18n_domain
            __i18n_domain = u'senaite.patient'
            __backup_macroname_140168055483200 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b68c84e50> name=None at 7f7b68c84a90> -> __value
            __value = _static_140168015662672
            econtext['macroname'] = __value

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140168015662416
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055483200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055483200
            __i18n_domain = __previous_i18n_domain_140168015659216
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_view': render_view, 'render': render, }