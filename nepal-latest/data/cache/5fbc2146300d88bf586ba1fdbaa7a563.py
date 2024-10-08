# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/sampleheader.pt'

__tokens = {61: (u"python:context.restrictedTraverse('@@senaite_view')", 2, 30), 135: (u' nocall:senaite_view/tes', 3, 21), 184: (u"s python:options.get('errors', {}) or ", 4, 22), 247: (u'ig python:view.get_configuratio', 5, 21), 314: (u"mns python:config.get('prominent_colum", 6, 31), 387: (u"umns python:config.get('standard_colu", 7, 29), 459: (u"ields python:config.get('prominent_fi", 8, 28), 530: (u"fields python:config.get('standard_f", 9, 26), 608: (u'_fields python:prominent_columns > 0 and len(prominent_fie', 10, 33), 707: (u'd_fields python:standard_columns > 0 and len(standard_fi', 11, 31), 802: (u"rd_fields python:config.get('show_standar", 12, 28), 872: (u"toggle_css python:'collapse show' if show_standard_fields else", 13, 17), 1095: (u'python:False', 20, 30), 1856: (u'python:view.can_manage_sample_fields()', 39, 43), 2008: (u"python:context.absolute_url() + '/manage-sample-fields'", 42, 36), 2226: (u'python:render_standard_fields', 47, 30), 2425: (u'python:show_standard_fields', 49, 46), 2695: (u'python:not show_standard_fields', 53, 46), 3108: (u'python:render_prominent_fields', 63, 28), 3255: (u'python:view.grouper(prominent_fields, prominent_columns)', 65, 34), 3356: (u'python:group', 66, 42), 3424: (u'python:view.get_field_info(name)', 67, 53), 3505: (u" python:fieldinfo.get('mode'", 68, 47), 3582: (u"l python:fieldinfo.get('html", 69, 46), 3660: (u"ld python:fieldinfo.get('fiel", 70, 46), 3739: (u"bel python:fieldinfo.get('lab", 71, 45), 3824: (u"tion python:fieldinfo.get('descript", 72, 50), 3912: (u"uired python:fieldinfo.get('requ", 73, 46), 4157: (u'description', 77, 48), 4267: (u'label', 79, 49), 4475: (u"python:mode == 'edit' and view.is_primary_bound(field)", 82, 50), 4939: (u'python:required', 90, 41), 5178: (u'python:html', 95, 57), 5341: (u'html', 98, 52), 5462: (u'python:not html', 101, 57), 5539: (u"python:mode in ['view', 'edit']", 102, 59), 5674: (u'python:view.render_widget(field, mode=mode)', 104, 48), 5674: (u'python:view.render_widget(field, mode=mode)', 104, 48), 6045: (u'python:render_standard_fields', 116, 28), 6111: (u'string:table-responsive ${toggle_css}', 117, 35), 6260: (u'python:view.grouper(standard_fields, standard_columns)', 119, 34), 6359: (u'python:group', 120, 42), 6427: (u'python:view.get_field_info(name)', 121, 53), 6508: (u" python:fieldinfo.get('mode'", 122, 47), 6585: (u"l python:fieldinfo.get('html", 123, 46), 6663: (u"ld python:fieldinfo.get('fiel", 124, 46), 6742: (u"bel python:fieldinfo.get('lab", 125, 45), 6827: (u"tion python:fieldinfo.get('descript", 126, 50), 6915: (u"uired python:fieldinfo.get('requ", 127, 46), 7185: (u'description', 131, 48), 7295: (u'label', 133, 49), 7503: (u"python:mode == 'edit' and view.is_primary_bound(field)", 136, 50), 7967: (u'python:required', 144, 41), 8239: (u'python:html', 149, 57), 8402: (u'html', 152, 52), 8523: (u'python:not html', 155, 57), 8600: (u"python:mode in ['view', 'edit']", 156, 59), 8735: (u'python:view.render_widget(field, mode=mode)', 158, 48), 8735: (u'python:view.render_widget(field, mode=mode)', 158, 48), 9008: (u'python:render_prominent_fields and render_standard_fields', 168, 33), 9131: (u'python:view.is_edit_allowed()', 170, 32), 9468: (u'context/@@plone_portal_state/portal', 183, 29), 9610: (u"python:portal.absolute_url() + '/senaite_widgets/datetimewidget.js'", 186, 28), 10592: (u'context/@@plone_portal_state/portal', 208, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168047766736 = {u'type': u'submit', u'class': u'btn btn-sm btn-primary mt-2', u'value': u'Save', u'name': u'sampleheader_form_save', }
_static_140168046848464 = {u'class': u'col-auto', }
_static_140168046849744 = {u'class': u'form-row', }
_static_140168027602256 = {u'media': u'screen', u'type': u'text/css', }
_static_140168046861968 = {u'class': u'fas fa-tasks', }
_static_140168047006608 = {u'type': u'hidden', u'name': u'sampleheader_form_submitted', u'value': u'1', }
_static_140168016766608 = {u'href': u"python:context.absolute_url() + '/manage-sample-fields'", u'class': u'text-decoration-none', u'target': u'_blank', }
_static_140168047811408 = u'python:view.render_widget(field, mode=mode)'
_static_140168026275280 = u'python:view.render_widget(field, mode=mode)'
_static_140168047808464 = {u'class': u'required', u'title': u'Required', }
_static_140168016765840 = {u'class': u'pr-3', }
_static_140168047808656 = {u'class': u'sampleheader-table table table-sm table-bordered', }
_static_140168047837712 = {u'id': u'toggle-show-icon', u'class': u'fas fa-window-maximize', }
_static_140168036617616 = {u'class': u'row', }
_static_140168047031120 = {u'class': u'sampleheader-table table table-sm table-bordered mb-1', }
_static_140168037656976 = {u'class': u'form-row', }
_static_140168047006224 = {u'method': u'post', u'class': u'senaite-form', u'id': u'senaite-sampleheader-form', u'novalidate': '', u'name': u'sampleheader_form', }
_static_140168026310160 = {u'id': u'toggle-hide-icon', u'class': u'fas fa-window-minimize d-none', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168025890064 = {u'data-toggle': u'tooltip', u'class': u'fas fa-sitemap small', u'title': u'Changes will be propagated to partitions', }
_static_140168025887376 = {u'class': u'required', u'title': u'Required', }
_static_140168047766800 = {u'style': u'width:200px;max-width:200px;', u'class': u'sampleheader-table-label bg-light text-truncate', }
_static_140168036616016 = {u'class': u'col-sm-12', }
_static_140168026384848 = {u'id': u'sampleheader-standard-fields', u'class': u'table-responsive', }
_static_140168208991440 = __compile_zt_expr
_static_140168046999824 = {u'class': u'sampleheader-controls d-flex justify-content-end', }
_static_140168047172560 = {u'class': u'form-row', }
_static_140168046860368 = {u'data-toggle': u'collapse', u'href': u'#', u'class': u'text-decoration-none', u'data-target': u'#sampleheader-standard-fields', }
_static_140168026275792 = {u'class': u'col-auto', }
_static_140168257770128 = {}
_static_140168047813264 = {u'id': u'senaite-sampleheader', }
_static_140168047805520 = {u'data-toggle': u'tooltip', u'class': u'fas fa-sitemap small', u'title': u'Changes will be propagated to partitions', }
_static_140168037656336 = {u'class': u'form-row', }
_static_140168025889040 = {u'data-toggle': u'tooltip', u'title': u'description', }
_static_140168026310032 = {u'id': u'toggle-hide-icon', u'class': u'fas fa-window-minimize', }
_static_140168047807824 = {u'class': u'sampleheader-table-field', }
_static_140168036701840 = {u'style': u'width:200px;max-width:200px;', u'class': u'bg-light text-truncate', }
_static_140168037658320 = {u'class': u'col-auto', }
_static_140168047812112 = {u'class': u'col-auto', }
_static_140168027602576 = {u'type': u'text/javascript', }
_static_140168026311952 = {u'id': u'toggle-show-icon', u'class': u'fas fa-window-maximize d-none', }
_static_140168046861072 = {u'id': u'sampleheader-prominent-fields', u'class': u'table-responsive', }
_static_140168047841424 = {u'data-toggle': u'tooltip', u'title': u'description', }
_static_140168027601936 = {u'src': u"python:portal.absolute_url() + '/senaite_widgets/datetimewidget.js'", u'type': u'text/javascript', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6ab2e290> name=None at 7f7b6ab2e4d0> -> __attrs_140168047816144
            __attrs_140168047816144 = _static_140168047813264
            __backup_senaite_view_140168037641616 = get('senaite_view', __marker)

            # <Value u"python:context.restrictedTraverse('@@senaite_view')" (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"context.restrictedTraverse('@@senaite_view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['senaite_view'] = __value
            __backup_test_140168047815184 = get('test', __marker)

            # <Value u'nocall:senaite_view/test' (3:21)> -> __value
            __token = 135
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('nocall', u'senaite_view/test', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['test'] = __value
            __backup_errors_140168026219280 = get('errors', __marker)

            # <Value u"python:options.get('errors', {}) or {}" (4:22)> -> __value
            __token = 184
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"options.get('errors', {}) or {}", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_config_140168047412496 = get('config', __marker)

            # <Value u'python:view.get_configuration()' (5:21)> -> __value
            __token = 247
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.get_configuration()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['config'] = __value
            __backup_prominent_columns_140168037531280 = get('prominent_columns', __marker)

            # <Value u"python:config.get('prominent_columns')" (6:31)> -> __value
            __token = 314
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"config.get('prominent_columns')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['prominent_columns'] = __value
            __backup_standard_columns_140168037642000 = get('standard_columns', __marker)

            # <Value u"python:config.get('standard_columns')" (7:29)> -> __value
            __token = 387
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"config.get('standard_columns')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['standard_columns'] = __value
            __backup_prominent_fields_140168047412048 = get('prominent_fields', __marker)

            # <Value u"python:config.get('prominent_fields')" (8:28)> -> __value
            __token = 459
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"config.get('prominent_fields')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['prominent_fields'] = __value
            __backup_standard_fields_140168026304848 = get('standard_fields', __marker)

            # <Value u"python:config.get('standard_fields')" (9:26)> -> __value
            __token = 530
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"config.get('standard_fields')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['standard_fields'] = __value
            __backup_render_prominent_fields_140168083137808 = get('render_prominent_fields', __marker)

            # <Value u'python:prominent_columns > 0 and len(prominent_fields) > 0' (10:33)> -> __value
            __token = 608
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'prominent_columns > 0 and len(prominent_fields) > 0', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['render_prominent_fields'] = __value
            __backup_render_standard_fields_140168082037904 = get('render_standard_fields', __marker)

            # <Value u'python:standard_columns > 0 and len(standard_fields) > 0' (11:31)> -> __value
            __token = 707
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'standard_columns > 0 and len(standard_fields) > 0', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['render_standard_fields'] = __value
            __backup_show_standard_fields_140168037641360 = get('show_standard_fields', __marker)

            # <Value u"python:config.get('show_standard_fields')" (12:28)> -> __value
            __token = 802
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"config.get('show_standard_fields')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['show_standard_fields'] = __value
            __backup_toggle_css_140168046862736 = get('toggle_css', __marker)

            # <Value u"python:'collapse show' if show_standard_fields else 'collapse'" (13:17)> -> __value
            __token = 872
            try:
                __zt_tmp = __attrs_140168047816144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"'collapse show' if show_standard_fields else 'collapse'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['toggle_css'] = __value
            __previous_i18n_domain_140168036615440 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="senaite-sampleheader">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a080d90> name=None at 7f7b6a080f10> -> __attrs_140168036616464
            __attrs_140168036616464 = _static_140168036617616

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6a080750> name=None at 7f7b6a0804d0> -> __attrs_140168036617872
            __attrs_140168036617872 = _static_140168036616016

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n\n      <!-- SAMPLE HEADER FORM -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036614736
            __attrs_140168036614736 = _static_140168257770128

            # <Value u'python:False' (20:30)> -> __condition
            __token = 1095
            try:
                __zt_tmp = __attrs_140168036614736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'False', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        <!--\n             Note: the `novalidate` attribute is needed to avoid browser validation\n             when e.g. the "expected sampling date" has passed and another value\n             wants to be changed.\n\n             https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Constraint_validation\n        -->\n      ')
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa69210> name=None at 7f7b6aa69990> -> __attrs_140168047005840
            __attrs_140168047005840 = _static_140168047006224

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form id="senaite-sampleheader-form" name="sampleheader_form" class="senaite-form" method="post" novalidate>\n\n        <!-- Hidden fields -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa69390> name=None at 7f7b6aa69b10> -> __attrs_140168046998416
            __attrs_140168046998416 = _static_140168047006608

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="sampleheader_form_submitted" value="1" />\n\n        <!-- Display Controls -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa67910> name=None at 7f7b6aa67250> -> __attrs_140168047000336
            __attrs_140168047000336 = _static_140168046999824

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="sampleheader-controls d-flex justify-content-end">\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b68d92390> name=None at 7f7b68d92790> -> __attrs_140168016765712
            __attrs_140168016765712 = _static_140168016765840

            # <Value u'python:view.can_manage_sample_fields()' (39:43)> -> __condition
            __token = 1856
            try:
                __zt_tmp = __attrs_140168016765712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.can_manage_sample_fields()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="pr-3">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68d92690> name=None at 7f7b68d92710> -> __attrs_140168016767824
                __attrs_140168016767824 = _static_140168016766608

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="text-decoration-none" target="_blank"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016767888
                __default_140168016767888 = _DEFAULT_MARKER

                # <Substitution u"python:context.absolute_url() + '/manage-sample-fields'" (42:36)> -> __attr_href
                __token = 2008
                try:
                    __zt_tmp = __attrs_140168016767824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u"context.absolute_url() + '/manage-sample-fields'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa45e90> name=None at 7f7b68d92490> -> __attrs_140168046860880
                __attrs_140168046860880 = _static_140168046861968

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-tasks"></i>\n            </a>\n          </div>')
            __append(u'\n          <!-- Toggle standard fields visibility -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046859344
            __attrs_140168046859344 = _static_140168257770128

            # <Value u'python:render_standard_fields' (47:30)> -> __condition
            __token = 2226
            try:
                __zt_tmp = __attrs_140168046859344
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'render_standard_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa45850> name=None at 7f7b6aa456d0> -> __attrs_140168046860240
                __attrs_140168046860240 = _static_140168046860368

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a href="#" class="text-decoration-none" data-toggle="collapse" data-target="#sampleheader-standard-fields">\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037626256
                __attrs_140168037626256 = _static_140168257770128

                # <Value u'python:show_standard_fields' (49:46)> -> __condition
                __token = 2425
                try:
                    __zt_tmp = __attrs_140168037626256
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'show_standard_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ab34210> name=None at 7f7b6ab342d0> -> __attrs_140168026308880
                    __attrs_140168026308880 = _static_140168047837712

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i id="toggle-show-icon" class="fas fa-window-maximize"></i>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b696ac610> name=None at 7f7b696ac650> -> __attrs_140168026312400
                    __attrs_140168026312400 = _static_140168026310160

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i id="toggle-hide-icon" class="fas fa-window-minimize d-none"></i>\n              ')
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026309584
                __attrs_140168026309584 = _static_140168257770128

                # <Value u'python:not show_standard_fields' (53:46)> -> __condition
                __token = 2695
                try:
                    __zt_tmp = __attrs_140168026309584
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'not show_standard_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b696acd10> name=None at 7f7b696ac710> -> __attrs_140168026311440
                    __attrs_140168026311440 = _static_140168026311952

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i id="toggle-show-icon" class="fas fa-window-maximize d-none"></i>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b696ac590> name=None at 7f7b696ac410> -> __attrs_140168047034320
                    __attrs_140168047034320 = _static_140168026310032

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i id="toggle-hide-icon" class="fas fa-window-minimize"></i>\n              ')
                __append(u'\n            </a>\n          </div>')
            __append(u'\n        </div>\n\n        <!-- Prominent fields -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa45b10> name=None at 7f7b6aa458d0> -> __attrs_140168047030736
            __attrs_140168047030736 = _static_140168046861072

            # <Value u'python:render_prominent_fields' (63:28)> -> __condition
            __token = 3108
            try:
                __zt_tmp = __attrs_140168047030736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'render_prominent_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="sampleheader-prominent-fields" class="table-responsive">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa6f350> name=None at 7f7b6aa6f290> -> __attrs_140168026384272
                __attrs_140168026384272 = _static_140168047031120

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table class="sampleheader-table table table-sm table-bordered mb-1">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026384528
                __attrs_140168026384528 = _static_140168257770128
                __backup_group_140168047150608 = get('group', __marker)

                # <Value u'python:view.grouper(prominent_fields, prominent_columns)' (65:34)> -> __iterator
                __token = 3255
                try:
                    __zt_tmp = __attrs_140168026384528
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('python', u'view.grouper(prominent_fields, prominent_columns)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168026383504, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026384720
                    __attrs_140168026384720 = _static_140168257770128
                    __backup_name_140168026367888 = get('name', __marker)

                    # <Value u'python:group' (66:42)> -> __iterator
                    __token = 3356
                    try:
                        __zt_tmp = __attrs_140168026384720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('python', u'group', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047342480, ) = getitem('repeat')(u'name', __iterator)
                    econtext['name'] = None
                    for __item in __iterator:
                        econtext['name'] = __item
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036702416
                        __attrs_140168036702416 = _static_140168257770128
                        __backup_fieldinfo_140168046997904 = get('fieldinfo', __marker)

                        # <Value u'python:view.get_field_info(name)' (67:53)> -> __value
                        __token = 3424
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'view.get_field_info(name)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['fieldinfo'] = __value
                        __backup_mode_140168037495248 = get('mode', __marker)

                        # <Value u"python:fieldinfo.get('mode')" (68:47)> -> __value
                        __token = 3505
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('mode')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['mode'] = __value
                        __backup_html_140168046998224 = get('html', __marker)

                        # <Value u"python:fieldinfo.get('html')" (69:46)> -> __value
                        __token = 3582
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('html')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['html'] = __value
                        __backup_field_140168037644240 = get('field', __marker)

                        # <Value u"python:fieldinfo.get('field')" (70:46)> -> __value
                        __token = 3660
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('field')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['field'] = __value
                        __backup_label_140168047354448 = get('label', __marker)

                        # <Value u"python:fieldinfo.get('label')" (71:45)> -> __value
                        __token = 3739
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('label')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['label'] = __value
                        __backup_description_140168026327056 = get('description', __marker)

                        # <Value u"python:fieldinfo.get('description')" (72:50)> -> __value
                        __token = 3824
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('description')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['description'] = __value
                        __backup_required_140168047355024 = get('required', __marker)

                        # <Value u"python:fieldinfo.get('required')" (73:46)> -> __value
                        __token = 3912
                        try:
                            __zt_tmp = __attrs_140168036702416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('required')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['required'] = __value
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a095690> name=None at 7f7b6a095c10> -> __attrs_140168036703312
                        __attrs_140168036703312 = _static_140168036701840

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="bg-light text-truncate" style="width:200px;max-width:200px;">\n                    <!-- Widget Label -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b69645910> name=None at 7f7b69645f50> -> __attrs_140168025890320
                        __attrs_140168025890320 = _static_140168025889040

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span data-toggle="tooltip"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025887120
                        __default_140168025887120 = _DEFAULT_MARKER

                        # <Substitution u'description' (77:48)> -> __attr_title
                        __token = 4157
                        try:
                            __zt_tmp = __attrs_140168025890320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025888784
                        __default_140168025888784 = _DEFAULT_MARKER

                        # <Value u'label' (79:49)> -> __cache_140168036701328
                        __token = 4267
                        try:
                            __zt_tmp = __attrs_140168025890320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036701328 = _static_140168208991440('path', u'label', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'label' (79:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a095890> -> __condition
                        __expression = __cache_140168036701328

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168036701328
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                    <!-- Display a notification icon if the field is primary bound\n                         (if changes propagate to partitions) -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025888400
                        __attrs_140168025888400 = _static_140168257770128

                        # <Value u"python:mode == 'edit' and view.is_primary_bound(field)" (82:50)> -> __condition
                        __token = 4475
                        try:
                            __zt_tmp = __attrs_140168025888400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u"mode == 'edit' and view.is_primary_bound(field)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b69645d10> name=None at 7f7b69645090> -> __attrs_140168047169680
                            __attrs_140168047169680 = _static_140168025890064

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<i class="fas fa-sitemap small" data-toggle="tooltip"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047171408
                            __default_140168047171408 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<_ast.Str object at 0x7f7b6aa91790> at 7f7b6aa91650> -> __attr_title
                            __attr_title = u'Changes will be propagated to partitions'
                            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'></i>\n                    ')
                        __append(u'\n                    <!-- Display Required Marker -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b69645290> name=None at 7f7b69645b50> -> __attrs_140168047172816
                        __attrs_140168047172816 = _static_140168025887376

                        # <Value u'python:required' (90:41)> -> __condition
                        __token = 4939
                        try:
                            __zt_tmp = __attrs_140168047172816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047170256
                            __default_140168047170256 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b6aa91a90> at 7f7b6aa91250> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'> </span>')
                        __append(u'\n                  </td>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047172048
                        __attrs_140168047172048 = _static_140168257770128

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td>\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa91bd0> name=None at 7f7b6aa917d0> -> __attrs_140168046846288
                        __attrs_140168046846288 = _static_140168047172560

                        # <Value u'python:html' (95:57)> -> __condition
                        __token = 5178
                        try:
                            __zt_tmp = __attrs_140168046846288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="form-row">\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b6aa429d0> name=None at 7f7b6aa42990> -> __attrs_140168046846224
                            __attrs_140168046846224 = _static_140168046848464

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="col-auto">\n                        <!-- Render widget HTML -->\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046848848
                            __attrs_140168046848848 = _static_140168257770128

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046846352
                            __default_140168046846352 = _DEFAULT_MARKER

                            # <Value u'html' (98:52)> -> __cache_140168046847504
                            __token = 5341
                            try:
                                __zt_tmp = __attrs_140168046848848
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140168046847504 = _static_140168208991440('path', u'html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                            # <BinOp left=<Value u'html' (98:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa42510> -> __condition
                            __expression = __cache_140168046847504

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140168046847504
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                      </div>\n                    </div>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa42ed0> name=None at 7f7b6aa42cd0> -> __attrs_140168047810896
                        __attrs_140168047810896 = _static_140168046849744

                        # <Value u'python:not html' (101:57)> -> __condition
                        __token = 5462
                        try:
                            __zt_tmp = __attrs_140168047810896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'not html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="form-row">\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b6ab2de10> name=None at 7f7b6ab2d310> -> __attrs_140168047810448
                            __attrs_140168047810448 = _static_140168047812112

                            # <Value u"python:mode in ['view', 'edit']" (102:59)> -> __condition
                            __token = 5539
                            try:
                                __zt_tmp = __attrs_140168047810448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140168208991440('python', u"mode in ['view', 'edit']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="col-auto">\n                        <!-- Render widget macro -->\n                        ')

                                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047809808
                                __attrs_140168047809808 = _static_140168257770128
                                __backup_macroname_140168055408192 = get('macroname', __marker)

                                # <Static value=<_ast.Str object at 0x7f7b6ab2db50> name=None at 7f7b6ab2d250> -> __value
                                __value = _static_140168047811408
                                econtext['macroname'] = __value

                                # <Value u'python:view.render_widget(field, mode=mode)' (104:48)> -> __macro
                                __token = 5674
                                try:
                                    __zt_tmp = __attrs_140168047809808
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __macro = _static_140168208991440('python', u'view.render_widget(field, mode=mode)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                __token = 5674
                                __m = __macro.include
                                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                                econtext.update(rcontext)
                                if (__backup_macroname_140168055408192 is __marker):
                                    del econtext['macroname']
                                else:
                                    econtext['macroname'] = __backup_macroname_140168055408192
                                __append(u'\n                      </div>')
                            __append(u'\n                    </div>')
                        __append(u'\n                  </td>\n                ')
                        if (__backup_required_140168047355024 is __marker):
                            del econtext['required']
                        else:
                            econtext['required'] = __backup_required_140168047355024
                        if (__backup_description_140168026327056 is __marker):
                            del econtext['description']
                        else:
                            econtext['description'] = __backup_description_140168026327056
                        if (__backup_label_140168047354448 is __marker):
                            del econtext['label']
                        else:
                            econtext['label'] = __backup_label_140168047354448
                        if (__backup_field_140168037644240 is __marker):
                            del econtext['field']
                        else:
                            econtext['field'] = __backup_field_140168037644240
                        if (__backup_html_140168046998224 is __marker):
                            del econtext['html']
                        else:
                            econtext['html'] = __backup_html_140168046998224
                        if (__backup_mode_140168037495248 is __marker):
                            del econtext['mode']
                        else:
                            econtext['mode'] = __backup_mode_140168037495248
                        if (__backup_fieldinfo_140168046997904 is __marker):
                            del econtext['fieldinfo']
                        else:
                            econtext['fieldinfo'] = __backup_fieldinfo_140168046997904
                        __append(u'\n              ')
                        ____index_140168047342480 -= 1
                        if (____index_140168047342480 > 0):
                            __append('')
                    if (__backup_name_140168026367888 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140168026367888
                    __append(u'\n            </tr>')
                    ____index_140168026383504 -= 1
                    if (____index_140168026383504 > 0):
                        __append('\n            ')
                if (__backup_group_140168047150608 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140168047150608
                __append(u'\n          </table>\n      </div>')
            __append(u'\n\n        <!-- Standard fields -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b696be9d0> name=None at 7f7b696be350> -> __attrs_140168046846736
            __attrs_140168046846736 = _static_140168026384848

            # <Value u'python:render_standard_fields' (116:28)> -> __condition
            __token = 6045
            try:
                __zt_tmp = __attrs_140168046846736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'render_standard_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="sampleheader-standard-fields"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036703056
                __default_140168036703056 = _DEFAULT_MARKER

                # <Substitution u'string:table-responsive ${toggle_css}' (117:35)> -> __attr_class
                __token = 6111
                try:
                    __zt_tmp = __attrs_140168046846736
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140168208991440('string', u'table-responsive ${toggle_css}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'table-responsive', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab2d090> name=None at 7f7b6ab2d9d0> -> __attrs_140168047351312
                __attrs_140168047351312 = _static_140168047808656

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table class="sampleheader-table table table-sm table-bordered">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047351696
                __attrs_140168047351696 = _static_140168257770128
                __backup_group_140168026368976 = get('group', __marker)

                # <Value u'python:view.grouper(standard_fields, standard_columns)' (119:34)> -> __iterator
                __token = 6260
                try:
                    __zt_tmp = __attrs_140168047351696
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('python', u'view.grouper(standard_fields, standard_columns)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168047352336, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047352208
                    __attrs_140168047352208 = _static_140168257770128
                    __backup_name_140168047001104 = get('name', __marker)

                    # <Value u'python:group' (120:42)> -> __iterator
                    __token = 6359
                    try:
                        __zt_tmp = __attrs_140168047352208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('python', u'group', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047350032, ) = getitem('repeat')(u'name', __iterator)
                    econtext['name'] = None
                    for __item in __iterator:
                        econtext['name'] = __item
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037618384
                        __attrs_140168037618384 = _static_140168257770128
                        __backup_fieldinfo_140168046974544 = get('fieldinfo', __marker)

                        # <Value u'python:view.get_field_info(name)' (121:53)> -> __value
                        __token = 6427
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'view.get_field_info(name)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['fieldinfo'] = __value
                        __backup_mode_140168046973392 = get('mode', __marker)

                        # <Value u"python:fieldinfo.get('mode')" (122:47)> -> __value
                        __token = 6508
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('mode')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['mode'] = __value
                        __backup_html_140168047805904 = get('html', __marker)

                        # <Value u"python:fieldinfo.get('html')" (123:46)> -> __value
                        __token = 6585
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('html')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['html'] = __value
                        __backup_field_140168047805008 = get('field', __marker)

                        # <Value u"python:fieldinfo.get('field')" (124:46)> -> __value
                        __token = 6663
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('field')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['field'] = __value
                        __backup_label_140168025889936 = get('label', __marker)

                        # <Value u"python:fieldinfo.get('label')" (125:45)> -> __value
                        __token = 6742
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('label')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['label'] = __value
                        __backup_description_140168047289616 = get('description', __marker)

                        # <Value u"python:fieldinfo.get('description')" (126:50)> -> __value
                        __token = 6827
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('description')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['description'] = __value
                        __backup_required_140168046848272 = get('required', __marker)

                        # <Value u"python:fieldinfo.get('required')" (127:46)> -> __value
                        __token = 6915
                        try:
                            __zt_tmp = __attrs_140168037618384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"fieldinfo.get('required')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['required'] = __value
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab22d10> name=None at 7f7b6ab22c50> -> __attrs_140168047841808
                        __attrs_140168047841808 = _static_140168047766800

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="sampleheader-table-label bg-light text-truncate" style="width:200px;max-width:200px;">\n                    <!-- Widget Label -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab35090> name=None at 7f7b6ab35950> -> __attrs_140168047844432
                        __attrs_140168047844432 = _static_140168047841424

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span data-toggle="tooltip"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047844496
                        __default_140168047844496 = _DEFAULT_MARKER

                        # <Substitution u'description' (131:48)> -> __attr_title
                        __token = 7185
                        try:
                            __zt_tmp = __attrs_140168047844432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047842832
                        __default_140168047842832 = _DEFAULT_MARKER

                        # <Value u'label' (133:49)> -> __cache_140168047843600
                        __token = 7295
                        try:
                            __zt_tmp = __attrs_140168047844432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047843600 = _static_140168208991440('path', u'label', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'label' (133:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab35a90> -> __condition
                        __expression = __cache_140168047843600

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047843600
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                    <!-- Display a notification icon if the field is primary bound\n                         (if changes propagate to partitions) -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047807056
                        __attrs_140168047807056 = _static_140168257770128

                        # <Value u"python:mode == 'edit' and view.is_primary_bound(field)" (136:50)> -> __condition
                        __token = 7503
                        try:
                            __zt_tmp = __attrs_140168047807056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u"mode == 'edit' and view.is_primary_bound(field)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b6ab2c450> name=None at 7f7b6ab2c190> -> __attrs_140168047807440
                            __attrs_140168047807440 = _static_140168047805520

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<i class="fas fa-sitemap small" data-toggle="tooltip"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047807696
                            __default_140168047807696 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<_ast.Str object at 0x7f7b6ab2cb90> at 7f7b6ab2cf50> -> __attr_title
                            __attr_title = u'Changes will be propagated to partitions'
                            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'></i>\n                    ')
                        __append(u'\n                    <!-- Display Required Marker -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab2cfd0> name=None at 7f7b6ab2c590> -> __attrs_140168037657040
                        __attrs_140168037657040 = _static_140168047808464

                        # <Value u'python:required' (144:41)> -> __condition
                        __token = 7967
                        try:
                            __zt_tmp = __attrs_140168037657040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026219536
                            __default_140168026219536 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b69696c50> at 7f7b69696e90> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'> </span>')
                        __append(u'\n                  </td>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab2cd50> name=None at 7f7b6ab2c710> -> __attrs_140168037656528
                        __attrs_140168037656528 = _static_140168047807824

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="sampleheader-table-field">\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a17e710> name=None at 7f7b6a17e610> -> __attrs_140168037657744
                        __attrs_140168037657744 = _static_140168037656336

                        # <Value u'python:html' (149:57)> -> __condition
                        __token = 8239
                        try:
                            __zt_tmp = __attrs_140168037657744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="form-row">\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b6a17eed0> name=None at 7f7b6a17edd0> -> __attrs_140168037655696
                            __attrs_140168037655696 = _static_140168037658320

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="col-auto">\n                        <!-- Render widget HTML -->\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026362192
                            __attrs_140168026362192 = _static_140168257770128

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047742672
                            __default_140168047742672 = _DEFAULT_MARKER

                            # <Value u'html' (152:52)> -> __cache_140168047532880
                            __token = 8402
                            try:
                                __zt_tmp = __attrs_140168026362192
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140168047532880 = _static_140168208991440('path', u'html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                            # <BinOp left=<Value u'html' (152:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aae9690> -> __condition
                            __expression = __cache_140168047532880

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140168047532880
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                      </div>\n                    </div>')
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a17e990> name=None at 7f7b6a17e850> -> __attrs_140168026271888
                        __attrs_140168026271888 = _static_140168037656976

                        # <Value u'python:not html' (155:57)> -> __condition
                        __token = 8523
                        try:
                            __zt_tmp = __attrs_140168026271888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('python', u'not html', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="form-row">\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f7b696a3fd0> name=None at 7f7b696a3bd0> -> __attrs_140168026273744
                            __attrs_140168026273744 = _static_140168026275792

                            # <Value u"python:mode in ['view', 'edit']" (156:59)> -> __condition
                            __token = 8600
                            try:
                                __zt_tmp = __attrs_140168026273744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140168208991440('python', u"mode in ['view', 'edit']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="col-auto">\n                        <!-- Render widget macro -->\n                        ')

                                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026273872
                                __attrs_140168026273872 = _static_140168257770128
                                __backup_macroname_140168054995536 = get('macroname', __marker)

                                # <Static value=<_ast.Str object at 0x7f7b696a3dd0> name=None at 7f7b696a3190> -> __value
                                __value = _static_140168026275280
                                econtext['macroname'] = __value

                                # <Value u'python:view.render_widget(field, mode=mode)' (158:48)> -> __macro
                                __token = 8735
                                try:
                                    __zt_tmp = __attrs_140168026273872
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __macro = _static_140168208991440('python', u'view.render_widget(field, mode=mode)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                __token = 8735
                                __m = __macro.include
                                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                                econtext.update(rcontext)
                                if (__backup_macroname_140168054995536 is __marker):
                                    del econtext['macroname']
                                else:
                                    econtext['macroname'] = __backup_macroname_140168054995536
                                __append(u'\n                      </div>')
                            __append(u'\n                    </div>')
                        __append(u'\n                  </td>\n                ')
                        if (__backup_required_140168046848272 is __marker):
                            del econtext['required']
                        else:
                            econtext['required'] = __backup_required_140168046848272
                        if (__backup_description_140168047289616 is __marker):
                            del econtext['description']
                        else:
                            econtext['description'] = __backup_description_140168047289616
                        if (__backup_label_140168025889936 is __marker):
                            del econtext['label']
                        else:
                            econtext['label'] = __backup_label_140168025889936
                        if (__backup_field_140168047805008 is __marker):
                            del econtext['field']
                        else:
                            econtext['field'] = __backup_field_140168047805008
                        if (__backup_html_140168047805904 is __marker):
                            del econtext['html']
                        else:
                            econtext['html'] = __backup_html_140168047805904
                        if (__backup_mode_140168046973392 is __marker):
                            del econtext['mode']
                        else:
                            econtext['mode'] = __backup_mode_140168046973392
                        if (__backup_fieldinfo_140168046974544 is __marker):
                            del econtext['fieldinfo']
                        else:
                            econtext['fieldinfo'] = __backup_fieldinfo_140168046974544
                        __append(u'\n              ')
                        ____index_140168047350032 -= 1
                        if (____index_140168047350032 > 0):
                            __append('')
                    if (__backup_name_140168047001104 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140168047001104
                    __append(u'\n            </tr>')
                    ____index_140168047352336 -= 1
                    if (____index_140168047352336 > 0):
                        __append('\n            ')
                if (__backup_group_140168026368976 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140168026368976
                __append(u'\n          </table>\n        </div>')
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047349904
            __attrs_140168047349904 = _static_140168257770128

            # <Value u'python:render_prominent_fields and render_standard_fields' (168:33)> -> __condition
            __token = 9008
            try:
                __zt_tmp = __attrs_140168047349904
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'render_prominent_fields and render_standard_fields', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          <!-- Save Button -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab22cd0> name=None at 7f7b6ab2c6d0> -> __attrs_140168027601680
                __attrs_140168027601680 = _static_140168047766736

                # <Value u'python:view.is_edit_allowed()' (170:32)> -> __condition
                __token = 9131
                try:
                    __zt_tmp = __attrs_140168027601680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'view.is_edit_allowed()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="btn btn-sm btn-primary mt-2" type="submit" name="sampleheader_form_save"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027602192
                    __default_140168027602192 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_save' node=<_ast.Str object at 0x7f7b6cb0f550> at 7f7b6cb0ffd0> -> __attr_value
                    __attr_value = u'Save'
                    __attr_value = translate(u'label_save', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>')
                __append(u'\n        ')
            __append(u'\n      </form>\n\n\n    </div>\n  </div>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047006800
            __attrs_140168047006800 = _static_140168257770128
            __backup_portal_140168026331792 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (183:29)> -> __value
            __token = 9468
            try:
                __zt_tmp = __attrs_140168047006800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __append(u'\n    <!-- needed for datetime fields -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b697e7c10> name=None at 7f7b697e7910> -> __attrs_140168027600208
            __attrs_140168027600208 = _static_140168027601936

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027602000
            __default_140168027602000 = _DEFAULT_MARKER

            # <Substitution u"python:portal.absolute_url() + '/senaite_widgets/datetimewidget.js'" (186:28)> -> __attr_src
            __token = 9610
            try:
                __zt_tmp = __attrs_140168027600208
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140168208991440('python', u"portal.absolute_url() + '/senaite_widgets/datetimewidget.js'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b697e7e90> name=None at 7f7b697e7ed0> -> __attrs_140168027599760
            __attrs_140168027599760 = _static_140168027602576

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript">\n     document.addEventListener("DOMContentLoaded", function(event) {\n       let show_icon = document.getElementById("toggle-show-icon");\n       let hide_icon = document.getElementById("toggle-hide-icon");\n       // Event handler when the standard fields are hidden\n       $("#sampleheader-standard-fields").on("hide.bs.collapse", function () {\n         console.log("Hide standard fields");\n         $(show_icon).toggleClass("d-none", true);\n         $(hide_icon).toggleClass("d-none", false)\n       });\n       // Event handler when the standard fields are shown\n       $("#sampleheader-standard-fields").on("show.bs.collapse", function () {\n         console.log("Show standard fields");\n         $(show_icon).toggleClass("d-none", false);\n         $(hide_icon).toggleClass("d-none", true)\n       });\n\n     });\n    </script>\n  ')
            if (__backup_portal_140168026331792 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168026331792
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168027599632
            __attrs_140168027599632 = _static_140168257770128
            __backup_portal_140168037562384 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (208:30)> -> __value
            __token = 10592
            try:
                __zt_tmp = __attrs_140168027599632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b697e7d50> name=None at 7f7b697e73d0> -> __attrs_140168027214672
            __attrs_140168027214672 = _static_140168027602256

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u'<style type="text/css" media="screen">\n     /* TODO: Check why this margin is defined in the loader.scss => reduce gap */\n     article#content header { margin-bottom: 0; }\n     form[name="sampleheader_form"] div.field { margin-bottom: 0; }\n     /* Increase fields for better editing experience */\n    </style>\n  ')
            if (__backup_portal_140168037562384 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168037562384
            __append(u'\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140168036615440
            if (__backup_toggle_css_140168046862736 is __marker):
                del econtext['toggle_css']
            else:
                econtext['toggle_css'] = __backup_toggle_css_140168046862736
            if (__backup_show_standard_fields_140168037641360 is __marker):
                del econtext['show_standard_fields']
            else:
                econtext['show_standard_fields'] = __backup_show_standard_fields_140168037641360
            if (__backup_render_standard_fields_140168082037904 is __marker):
                del econtext['render_standard_fields']
            else:
                econtext['render_standard_fields'] = __backup_render_standard_fields_140168082037904
            if (__backup_render_prominent_fields_140168083137808 is __marker):
                del econtext['render_prominent_fields']
            else:
                econtext['render_prominent_fields'] = __backup_render_prominent_fields_140168083137808
            if (__backup_standard_fields_140168026304848 is __marker):
                del econtext['standard_fields']
            else:
                econtext['standard_fields'] = __backup_standard_fields_140168026304848
            if (__backup_prominent_fields_140168047412048 is __marker):
                del econtext['prominent_fields']
            else:
                econtext['prominent_fields'] = __backup_prominent_fields_140168047412048
            if (__backup_standard_columns_140168037642000 is __marker):
                del econtext['standard_columns']
            else:
                econtext['standard_columns'] = __backup_standard_columns_140168037642000
            if (__backup_prominent_columns_140168037531280 is __marker):
                del econtext['prominent_columns']
            else:
                econtext['prominent_columns'] = __backup_prominent_columns_140168037531280
            if (__backup_config_140168047412496 is __marker):
                del econtext['config']
            else:
                econtext['config'] = __backup_config_140168047412496
            if (__backup_errors_140168026219280 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140168026219280
            if (__backup_test_140168047815184 is __marker):
                del econtext['test']
            else:
                econtext['test'] = __backup_test_140168047815184
            if (__backup_senaite_view_140168037641616 is __marker):
                del econtext['senaite_view']
            else:
                econtext['senaite_view'] = __backup_senaite_view_140168037641616
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }