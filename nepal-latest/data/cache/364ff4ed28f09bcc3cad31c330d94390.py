# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.Archetypes-1.16.6-py2.7.egg/Products/Archetypes/skins/archetypes/widgets/field.pt'

__tokens = {2968: (u'python:widget.isVisible(here, mode)', 66, 29), 3038: (u' python:field.getEditAccessor(here', 67, 33), 3103: (u'd python:(widget.populate and (edit_accessor or accessor)) or No', 68, 28), 3194: (u'ue python:getMethod and getMetho', 69, 23), 3253: (u'lue python:request.get(fieldName, value) if widget.postback else v', 70, 22), 3347: (u'rtal python:context.portal_url.getPortalObj', 71, 22), 3424: (u'ition python:field.widget.testCondition(context.aq_inner.getParentNode(), portal, co', 72, 27), 3538: (u'ror_id python:errors.get(fie', 73, 22), 3618: (u"python:visState == 'visible' and visCondition", 75, 21), 3733: (u'context/@@kss_field_decorator_view', 77, 40), 3807: (u' nocall:kssClassesView/getKssClasse', 78, 38), 3878: (u's python:getKssClasses(fieldNam', 79, 33), 3942: (u"python:('edit' in widget.modes and 'w' in field.mode and field.checkPermission('w',here))\n                                    or (mode=='search' and field.checkPermission('r',here))", 80, 28), 4160: (u"python: test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + kss_class", 82, 35), 4327: (u" python: 'archetypes-fieldname-' + fieldNam", 83, 31), 4409: (u'd context/UID|nothi', 84, 36), 4473: (u'me fieldN', 85, 41), 4596: (u'nothing', 87, 38), 4926: (u'not: widget/render_own_label | nothing', 92, 38), 5046: (u'python:fieldName', 94, 39), 5100: (u'python:widget.Label(here)', 95, 35), 5247: (u'field/required', 98, 37), 5462: (u'python:widget.Description(here)', 102, 45), 5592: (u'string:${fieldName}_help', 104, 40), 5539: (u'description', 103, 44), 5782: (u'field/workflowable | nothing', 110, 31), 5923: (u'context/portal_workflow', 114, 35), 5978: (u' python:accessor(', 115, 30), 6036: (u"e python:wf_tool.getInfoFor(obj, 'review_state', '", 116, 38), 6126: (u'string:${obj/absolute_url}/content_status_history', 117, 36), 6213: (u" python:test(review_state, review_state, 'private'", 118, 36), 6294: (u'review_state', 119, 28), 6436: (u'error_id', 124, 28), 6612: (u"python: visState == 'hidden'", 129, 32), 6707: (u"python:path('context/%s/macros' % widget.macro)", 131, 37), 6800: (u' context/widgets/field/macros/hidde', 132, 44), 6873: (u'o widget_macro/hidden | default_hidden_mac', 133, 35), 6978: (u'hidden_macro', 135, 32), 6978: (u'hidden_macro', 135, 32), 436: (u'python:context.widget(field.getName(), mode=mode, use_label=1)', 14, 32), 532: (u' context/widgets/field/macro', 15, 32), 593: (u'o view_macros/label | label_macro | field_macros/lab', 16, 30), 677: (u'ro view_macros/data | data_macro | field_macros/d', 17, 28), 756: (u'ate python:widget.isVisible(here, m', 18, 25), 819: (u'rtal python:context.portal_url.getPortalObj', 19, 22), 896: (u'ition python:field.widget.testCondition(context.aq_inner.getParentNode(), portal, co', 20, 27), 1032: (u"python:visState == 'visible' and visCondition", 22, 21), 1124: (u"python:'view' in widget.modes and 'r' in field.mode and field.checkPermission('r',here)", 24, 23), 1253: (u'use_label | nothing', 25, 39), 1315: (u'label_macro', 26, 40), 1315: (u'label_macro', 26, 40), 1398: (u'data_macro|default', 28, 37), 1398: (u'data_macro|default', 28, 37), 1613: (u'python:widget.Label(here)', 34, 71), 1689: (u'field/workflowable | nothing', 35, 27), 1809: (u'context/portal_workflow', 39, 31), 1860: (u' python:accessor(', 40, 26), 1914: (u"e python:wf_tool.getInfoFor(obj, 'review_state', '", 41, 34), 2000: (u'string:${obj/absolute_url}/content_status_history', 42, 32), 2083: (u" python:test(review_state, review_state, 'private'", 43, 32), 2160: (u'review_state', 44, 24), 7220: (u'fieldName', 145, 34), 7265: (u' valu', 146, 34), 2347: (u'widget_view', 53, 30), 2347: (u'widget_view', 53, 30), 2445: (u'fieldName|field/getName', 56, 57), 2530: (u" python:field.getType().split('.')[-1", 57, 60), 2619: (u'd context/UID|nothi', 58, 49), 2672: (u'string:field ArchetypesField-${fieldtypename}', 59, 30), 2745: (u' string:archetypes-fieldname-${fieldName}-${uid', 60, 26), 2838: (u'context/widgets/field/macros/base_view', 61, 42), 2838: (u'context/widgets/field/macros/base_view', 61, 42)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168046850576 = {u'class': u'formQuestion', u'for': u'python:fieldName', }
_static_140168046898128 = {u'class': u'formHelp', u'id': u'string:${fieldName}_help', }
_static_140168047238096 = {u'class': u'string:field ArchetypesField-${fieldtypename}', u'id': u'string:archetypes-fieldname-${fieldName}-${uid}', }
_static_140168047242896 = u'data_macro|default'
_static_140168087909520 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140168046896080 = {u'class': u'required', u'title': u'Required', }
_static_140168047348752 = {u'href': u'#', u'class': u"python:test(review_state, review_state, 'private')", }
_static_140168208992144 = __C2ZContextWrapper
_static_140168046953168 = {u'data-fieldname': u'fieldName', u'data-uid': u'context/UID|nothing', u'class': u'field', u'id': u"python: 'archetypes-fieldname-' + fieldName", }
_static_140168047768848 = u'hidden_macro'
_static_140168047236304 = u'widget_view'
_static_140168047238864 = u'base_view'
_static_140168257770128 = {}
_static_140168047242000 = u'label_macro'
_static_140168047370640 = {u'href': u'#', u'class': u"python:test(review_state, review_state, 'private')", }
_static_140168047285584 = {u'class': u'fieldErrorBox', }
_static_140168047770384 = {u'type': u'hidden', u'name': u'', u'value': u'', }
_static_140168047242256 = {u'class': u'formQuestion', }

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
            __slot_widget_body_label_prefix = econtext[u'__slot_widget_body_label_prefix'].pop()
        except:
            __slot_widget_body_label_prefix = None

        try:
            __slot_widget_body = econtext[u'__slot_widget_body'].pop()
        except:
            __slot_widget_body = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047238288
            __attrs_140168047238288 = _static_140168257770128
            __backup_visState_140168026260112 = get('visState', __marker)

            # <Value u'python:widget.isVisible(here, mode)' (66:29)> -> __value
            __token = 2968
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'widget.isVisible(here, mode)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['visState'] = __value
            __backup_edit_accessor_140168047531408 = get('edit_accessor', __marker)

            # <Value u'python:field.getEditAccessor(here)' (67:33)> -> __value
            __token = 3038
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.getEditAccessor(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['edit_accessor'] = __value
            __backup_getMethod_140168047240144 = get('getMethod', __marker)

            # <Value u'python:(widget.populate and (edit_accessor or accessor)) or None' (68:28)> -> __value
            __token = 3103
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'(widget.populate and (edit_accessor or accessor)) or None', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['getMethod'] = __value
            __backup_value_140168047242576 = get('value', __marker)

            # <Value u'python:getMethod and getMethod()' (69:23)> -> __value
            __token = 3194
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'getMethod and getMethod()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_value_140168047242768 = get('value', __marker)

            # <Value u'python:request.get(fieldName, value) if widget.postback else value' (70:22)> -> __value
            __token = 3253
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'request.get(fieldName, value) if widget.postback else value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_portal_140168047159760 = get('portal', __marker)

            # <Value u'python:context.portal_url.getPortalObject()' (71:22)> -> __value
            __token = 3347
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'context.portal_url.getPortalObject()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_visCondition_140168047241936 = get('visCondition', __marker)

            # <Value u'python:field.widget.testCondition(context.aq_inner.getParentNode(), portal, context)' (72:27)> -> __value
            __token = 3424
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.widget.testCondition(context.aq_inner.getParentNode(), portal, context)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['visCondition'] = __value
            __backup_error_id_140168047240272 = get('error_id', __marker)

            # <Value u'python:errors.get(fieldName)' (73:22)> -> __value
            __token = 3538
            try:
                __zt_tmp = __attrs_140168047238288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'errors.get(fieldName)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['error_id'] = __value
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046953296
            __attrs_140168046953296 = _static_140168257770128

            # <Value u"python:visState == 'visible' and visCondition" (75:21)> -> __condition
            __token = 3618
            try:
                __zt_tmp = __attrs_140168046953296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u"visState == 'visible' and visCondition", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa5c2d0> name=None at 7f7b6aa5ced0> -> __attrs_140168068765648
                __attrs_140168068765648 = _static_140168046953168
                __backup_kssClassesView_140168046952720 = get('kssClassesView', __marker)

                # <Value u'context/@@kss_field_decorator_view' (77:40)> -> __value
                __token = 3733
                try:
                    __zt_tmp = __attrs_140168068765648
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/@@kss_field_decorator_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['kssClassesView'] = __value
                __backup_getKssClasses_140168046955280 = get('getKssClasses', __marker)

                # <Value u'nocall:kssClassesView/getKssClasses' (78:38)> -> __value
                __token = 3807
                try:
                    __zt_tmp = __attrs_140168068765648
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('nocall', u'kssClassesView/getKssClasses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['getKssClasses'] = __value
                __backup_kss_class_140168046953936 = get('kss_class', __marker)

                # <Value u'python:getKssClasses(fieldName)' (79:33)> -> __value
                __token = 3878
                try:
                    __zt_tmp = __attrs_140168068765648
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'getKssClasses(fieldName)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['kss_class'] = __value

                # <Value u"python:('edit' in widget.modes and 'w' in field.mode and field.checkPermission('w',here))\n                                    or (mode=='search' and field.checkPermission('r',here))" (80:28)> -> __condition
                __token = 3942
                try:
                    __zt_tmp = __attrs_140168068765648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u"('edit' in widget.modes and 'w' in field.mode and field.checkPermission('w',here))\n                                    or (mode=='search' and field.checkPermission('r',here))", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046952528
                    __default_140168046952528 = _DEFAULT_MARKER

                    # <Substitution u"python: test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + kss_class" (82:35)> -> __attr_class
                    __token = 4160
                    try:
                        __zt_tmp = __attrs_140168068765648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140168208991440('python', u" test(error_id, 'field error ' + 'Archetypes' + widget.getName(), 'field ' + 'Archetypes' + widget.getName()) + ' ' + kss_class", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'field', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168089829520
                    __default_140168089829520 = _DEFAULT_MARKER

                    # <Substitution u"python: 'archetypes-fieldname-' + fieldName" (83:31)> -> __attr_id
                    __token = 4327
                    try:
                        __zt_tmp = __attrs_140168068765648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('python', u" 'archetypes-fieldname-' + fieldName", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168067786448
                    __default_140168067786448 = _DEFAULT_MARKER

                    # <Substitution u'context/UID|nothing' (84:36)> -> __attr_data_uid
                    __token = 4409
                    try:
                        __zt_tmp = __attrs_140168068765648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_uid = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_data_uid = __quote(__attr_data_uid, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_uid is not None):
                        __append((u' data-uid="%s"' % __attr_data_uid))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168067785424
                    __default_140168067785424 = _DEFAULT_MARKER

                    # <Substitution u'fieldName' (85:41)> -> __attr_data_fieldname
                    __token = 4473
                    try:
                        __zt_tmp = __attrs_140168068765648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldname = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldname is not None):
                        __append((u' data-fieldname="%s"' % __attr_data_fieldname))
                    __append(u'>\n          ')
                    if (__slot_widget_body_label_prefix is None):

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046850896
                        __attrs_140168046850896 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span></span>')
                    else:
                        __slot_widget_body_label_prefix(__stream, econtext.copy(), rcontext)
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046850704
                    __attrs_140168046850704 = _static_140168257770128

                    # <Value u'nothing' (87:38)> -> __condition
                    __token = 4596
                    try:
                        __zt_tmp = __attrs_140168046850704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            Label insertion for the selection and multi-selection widgets is deferred to the widget, as they must\n            consider their format (checkbox, radio, select box ...) to correctly format the label to meet\n            accessibility standards.\n          ')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046852048
                    __attrs_140168046852048 = _static_140168257770128

                    # <Value u'not: widget/render_own_label | nothing' (92:38)> -> __condition
                    __token = 4926
                    try:
                        __zt_tmp = __attrs_140168046852048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u' widget/render_own_label | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa43210> name=None at 7f7b6aa43090> -> __attrs_140168047845776
                        __attrs_140168047845776 = _static_140168046850576

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<label class="formQuestion"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046853584
                        __default_140168046853584 = _DEFAULT_MARKER

                        # <Substitution u'python:fieldName' (94:39)> -> __attr_for
                        __token = 5046
                        try:
                            __zt_tmp = __attrs_140168047845776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_for = _static_140168208991440('python', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_for is not None):
                            __append((u' for="%s"' % __attr_for))
                        __append(u'>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046895696
                        __attrs_140168046895696 = _static_140168257770128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046896720
                        __default_140168046896720 = _DEFAULT_MARKER

                        # <Value u'python:widget.Label(here)' (95:35)> -> __cache_140168046896656
                        __token = 5100
                        try:
                            __zt_tmp = __attrs_140168046895696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168046896656 = _static_140168208991440('python', u'widget.Label(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:widget.Label(here)' (95:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4e410> -> __condition
                        __expression = __cache_140168046896656

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span />')
                        else:
                            __content = __cache_140168046896656
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa4e3d0> name=None at 7f7b6aa4e150> -> __attrs_140168046897936
                        __attrs_140168046897936 = _static_140168046896080

                        # <Value u'field/required' (98:37)> -> __condition
                        __token = 5247
                        try:
                            __zt_tmp = __attrs_140168046897936
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('path', u'field/required', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046895312
                            __default_140168046895312 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f7b6aa4e810> at 7f7b6aa4e790> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'>&nbsp;</span>')
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa4ebd0> name=None at 7f7b6aa4ecd0> -> __attrs_140168047347792
                        __attrs_140168047347792 = _static_140168046898128
                        __backup_description_140168046850320 = get('description', __marker)

                        # <Value u'python:widget.Description(here)' (102:45)> -> __value
                        __token = 5462
                        try:
                            __zt_tmp = __attrs_140168047347792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'widget.Description(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['description'] = __value

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="formHelp"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047348624
                        __default_140168047348624 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}_help' (104:40)> -> __attr_id
                        __token = 5592
                        try:
                            __zt_tmp = __attrs_140168047347792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}_help', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046898896
                        __default_140168046898896 = _DEFAULT_MARKER

                        # <Value u'description' (103:44)> -> __cache_140168046897552
                        __token = 5539
                        try:
                            __zt_tmp = __attrs_140168047347792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168046897552 = _static_140168208991440('path', u'description', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'description' (103:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4ed10> -> __condition
                        __expression = __cache_140168046897552

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                  Help\n                ')
                        else:
                            __content = __cache_140168046897552
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                        if (__backup_description_140168046850320 is __marker):
                            del econtext['description']
                        else:
                            econtext['description'] = __backup_description_140168046850320
                        __append(u'\n            </label>\n          ')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046852688
                    __attrs_140168046852688 = _static_140168257770128

                    # <Value u'field/workflowable | nothing' (110:31)> -> __condition
                    __token = 5782
                    try:
                        __zt_tmp = __attrs_140168046852688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'field/workflowable | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            State:\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aabcc10> name=None at 7f7b6aabc610> -> __attrs_140168047348496
                        __attrs_140168047348496 = _static_140168047348752
                        __backup_wf_tool_140168047227024 = get('wf_tool', __marker)

                        # <Value u'context/portal_workflow' (114:35)> -> __value
                        __token = 5923
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('path', u'context/portal_workflow', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['wf_tool'] = __value
                        __backup_obj_140168083094416 = get('obj', __marker)

                        # <Value u'python:accessor()' (115:30)> -> __value
                        __token = 5978
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'accessor()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['obj'] = __value
                        __backup_review_state_140168046850832 = get('review_state', __marker)

                        # <Value u"python:wf_tool.getInfoFor(obj, 'review_state', '')" (116:38)> -> __value
                        __token = 6036
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"wf_tool.getInfoFor(obj, 'review_state', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['review_state'] = __value

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047347344
                        __default_140168047347344 = _DEFAULT_MARKER

                        # <Substitution u'string:${obj/absolute_url}/content_status_history' (117:36)> -> __attr_href
                        __token = 6126
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140168208991440('string', u'${obj/absolute_url}/content_status_history', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047347664
                        __default_140168047347664 = _DEFAULT_MARKER

                        # <Substitution u"python:test(review_state, review_state, 'private')" (118:36)> -> __attr_class
                        __token = 6213
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140168208991440('python', u"test(review_state, review_state, 'private')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047348432
                        __default_140168047348432 = _DEFAULT_MARKER

                        # <Value u'review_state' (119:28)> -> __cache_140168047346512
                        __token = 6294
                        try:
                            __zt_tmp = __attrs_140168047348496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047346512 = _static_140168208991440('path', u'review_state', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'review_state' (119:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aabcf50> -> __condition
                        __expression = __cache_140168047346512

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              review_state\n            ')
                        else:
                            __content = __cache_140168047346512
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</a>')
                        if (__backup_review_state_140168046850832 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_140168046850832
                        if (__backup_obj_140168083094416 is __marker):
                            del econtext['obj']
                        else:
                            econtext['obj'] = __backup_obj_140168083094416
                        if (__backup_wf_tool_140168047227024 is __marker):
                            del econtext['wf_tool']
                        else:
                            econtext['wf_tool'] = __backup_wf_tool_140168047227024
                        __append(u'\n          ')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aaad550> name=None at 7f7b6aaad9d0> -> __attrs_140168047288016
                    __attrs_140168047288016 = _static_140168047285584

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="fieldErrorBox">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047348688
                    __default_140168047348688 = _DEFAULT_MARKER

                    # <Value u'error_id' (124:28)> -> __cache_140168047845712
                    __token = 6436
                    try:
                        __zt_tmp = __attrs_140168047288016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047845712 = _static_140168208991440('path', u'error_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'error_id' (124:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aabc210> -> __condition
                    __expression = __cache_140168047845712

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Validation Error')
                    else:
                        __content = __cache_140168047845712
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n          ')
                    if (__slot_widget_body is None):

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047284880
                        __attrs_140168047284880 = _static_140168257770128

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div></div>')
                    else:
                        __slot_widget_body(__stream, econtext.copy(), rcontext)
                    __append(u'\n        </div>')
                if (__backup_kss_class_140168046953936 is __marker):
                    del econtext['kss_class']
                else:
                    econtext['kss_class'] = __backup_kss_class_140168046953936
                if (__backup_getKssClasses_140168046955280 is __marker):
                    del econtext['getKssClasses']
                else:
                    econtext['getKssClasses'] = __backup_getKssClasses_140168046955280
                if (__backup_kssClassesView_140168046952720 is __marker):
                    del econtext['kssClassesView']
                else:
                    econtext['kssClassesView'] = __backup_kssClassesView_140168046952720
                __append(u'\n      ')
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168082036368
            __attrs_140168082036368 = _static_140168257770128

            # <Value u"python: visState == 'hidden'" (129:32)> -> __condition
            __token = 6612
            try:
                __zt_tmp = __attrs_140168082036368
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u" visState == 'hidden'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047770512
                __attrs_140168047770512 = _static_140168257770128
                __backup_widget_macro_140168046953424 = get('widget_macro', __marker)

                # <Value u"python:path('context/%s/macros' % widget.macro)" (131:37)> -> __value
                __token = 6707
                try:
                    __zt_tmp = __attrs_140168047770512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"path('context/%s/macros' % widget.macro)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['widget_macro'] = __value
                __backup_default_hidden_macro_140168046956432 = get('default_hidden_macro', __marker)

                # <Value u'context/widgets/field/macros/hidden' (132:44)> -> __value
                __token = 6800
                try:
                    __zt_tmp = __attrs_140168047770512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/widgets/field/macros/hidden', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['default_hidden_macro'] = __value
                __backup_hidden_macro_140168046852112 = get('hidden_macro', __marker)

                # <Value u'widget_macro/hidden | default_hidden_macro' (133:35)> -> __value
                __token = 6873
                try:
                    __zt_tmp = __attrs_140168047770512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'widget_macro/hidden | default_hidden_macro', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['hidden_macro'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047768272
                __attrs_140168047768272 = _static_140168257770128
                __backup_macroname_140168056302960 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6ab23510> name=None at 7f7b6ab23650> -> __value
                __value = _static_140168047768848
                econtext['macroname'] = __value

                # <Value u'hidden_macro' (135:32)> -> __macro
                __token = 6978
                try:
                    __zt_tmp = __attrs_140168047768272
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'hidden_macro', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 6978
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168056302960 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168056302960
                __append(u'\n        ')
                if (__backup_hidden_macro_140168046852112 is __marker):
                    del econtext['hidden_macro']
                else:
                    econtext['hidden_macro'] = __backup_hidden_macro_140168046852112
                if (__backup_default_hidden_macro_140168046956432 is __marker):
                    del econtext['default_hidden_macro']
                else:
                    econtext['default_hidden_macro'] = __backup_default_hidden_macro_140168046956432
                if (__backup_widget_macro_140168046953424 is __marker):
                    del econtext['widget_macro']
                else:
                    econtext['widget_macro'] = __backup_widget_macro_140168046953424
                __append(u'\n      ')
            __append(u'\n\n    ')
            if (__backup_error_id_140168047240272 is __marker):
                del econtext['error_id']
            else:
                econtext['error_id'] = __backup_error_id_140168047240272
            if (__backup_visCondition_140168047241936 is __marker):
                del econtext['visCondition']
            else:
                econtext['visCondition'] = __backup_visCondition_140168047241936
            if (__backup_portal_140168047159760 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168047159760
            if (__backup_value_140168047242768 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168047242768
            if (__backup_value_140168047242576 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168047242576
            if (__backup_getMethod_140168047240144 is __marker):
                del econtext['getMethod']
            else:
                econtext['getMethod'] = __backup_getMethod_140168047240144
            if (__backup_edit_accessor_140168047531408 is __marker):
                del econtext['edit_accessor']
            else:
                econtext['edit_accessor'] = __backup_edit_accessor_140168047531408
            if (__backup_visState_140168026260112 is __marker):
                del econtext['visState']
            else:
                econtext['visState'] = __backup_visState_140168026260112
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_base_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047302352
            __attrs_140168047302352 = _static_140168257770128
            __backup_widget_view_140168082675856 = get('widget_view', __marker)

            # <Value u'python:context.widget(field.getName(), mode=mode, use_label=1)' (14:32)> -> __value
            __token = 436
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'context.widget(field.getName(), mode=mode, use_label=1)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['widget_view'] = __value
            __backup_field_macros_140168047767824 = get('field_macros', __marker)

            # <Value u'context/widgets/field/macros' (15:32)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/widgets/field/macros', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['field_macros'] = __value
            __backup_label_macro_140168046984784 = get('label_macro', __marker)

            # <Value u'view_macros/label | label_macro | field_macros/label' (16:30)> -> __value
            __token = 593
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'view_macros/label | label_macro | field_macros/label', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['label_macro'] = __value
            __backup_data_macro_140168067788176 = get('data_macro', __marker)

            # <Value u'view_macros/data | data_macro | field_macros/data' (17:28)> -> __value
            __token = 677
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'view_macros/data | data_macro | field_macros/data', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['data_macro'] = __value
            __backup_visState_140168046997648 = get('visState', __marker)

            # <Value u'python:widget.isVisible(here, mode)' (18:25)> -> __value
            __token = 756
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'widget.isVisible(here, mode)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['visState'] = __value
            __backup_portal_140168067777360 = get('portal', __marker)

            # <Value u'python:context.portal_url.getPortalObject()' (19:22)> -> __value
            __token = 819
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'context.portal_url.getPortalObject()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_visCondition_140168082660688 = get('visCondition', __marker)

            # <Value u'python:field.widget.testCondition(context.aq_inner.getParentNode(), portal, context)' (20:27)> -> __value
            __token = 896
            try:
                __zt_tmp = __attrs_140168047302352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'field.widget.testCondition(context.aq_inner.getParentNode(), portal, context)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['visCondition'] = __value
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168092335312
            __attrs_140168092335312 = _static_140168257770128

            # <Value u"python:visState == 'visible' and visCondition" (22:21)> -> __condition
            __token = 1032
            try:
                __zt_tmp = __attrs_140168092335312
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u"visState == 'visible' and visCondition", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168092265040
                __attrs_140168092265040 = _static_140168257770128

                # <Value u"python:'view' in widget.modes and 'r' in field.mode and field.checkPermission('r',here)" (24:23)> -> __condition
                __token = 1124
                try:
                    __zt_tmp = __attrs_140168092265040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u"'view' in widget.modes and 'r' in field.mode and field.checkPermission('r',here)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047241552
                    __attrs_140168047241552 = _static_140168257770128

                    # <Value u'use_label | nothing' (25:39)> -> __condition
                    __token = 1253
                    try:
                        __zt_tmp = __attrs_140168047241552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'use_label | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047240208
                        __attrs_140168047240208 = _static_140168257770128
                        __backup_macroname_140168057754880 = get('macroname', __marker)

                        # <Static value=<_ast.Str object at 0x7f7b6aaa2b10> name=None at 7f7b6aaa24d0> -> __value
                        __value = _static_140168047242000
                        econtext['macroname'] = __value

                        # <Value u'label_macro' (26:40)> -> __macro
                        __token = 1315
                        try:
                            __zt_tmp = __attrs_140168047240208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140168208991440('path', u'label_macro', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __token = 1315
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140168057754880 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140168057754880
                        __append(u'\n          ')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047239440
                    __attrs_140168047239440 = _static_140168257770128
                    __backup_macroname_140168057755040 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f7b6aaa2e90> name=None at 7f7b6aaa2150> -> __value
                    __value = _static_140168047242896
                    econtext['macroname'] = __value

                    # <Value u'data_macro|default' (28:37)> -> __macro
                    __token = 1398
                    try:
                        __zt_tmp = __attrs_140168047239440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140168208991440('path', u'data_macro|default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __token = 1398
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140168057755040 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140168057755040
                    __append(u'\n        ')
                __append(u'\n      ')
            __append(u'\n    ')
            if (__backup_visCondition_140168082660688 is __marker):
                del econtext['visCondition']
            else:
                econtext['visCondition'] = __backup_visCondition_140168082660688
            if (__backup_portal_140168067777360 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168067777360
            if (__backup_visState_140168046997648 is __marker):
                del econtext['visState']
            else:
                econtext['visState'] = __backup_visState_140168046997648
            if (__backup_data_macro_140168067788176 is __marker):
                del econtext['data_macro']
            else:
                econtext['data_macro'] = __backup_data_macro_140168067788176
            if (__backup_label_macro_140168046984784 is __marker):
                del econtext['label_macro']
            else:
                econtext['label_macro'] = __backup_label_macro_140168046984784
            if (__backup_field_macros_140168047767824 is __marker):
                del econtext['field_macros']
            else:
                econtext['field_macros'] = __backup_field_macros_140168047767824
            if (__backup_widget_view_140168082675856 is __marker):
                del econtext['widget_view']
            else:
                econtext['widget_view'] = __backup_widget_view_140168082675856
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_label(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168092335184
            __attrs_140168092335184 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6aaa2c10> name=None at 7f7b6aaa26d0> -> __attrs_140168047239568
            __attrs_140168047239568 = _static_140168047242256

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label class="formQuestion">')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168068329616
            __attrs_140168068329616 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168068483600
            __default_140168068483600 = _DEFAULT_MARKER

            # <Value u'python:widget.Label(here)' (34:71)> -> __cache_140168047243024
            __token = 1613
            try:
                __zt_tmp = __attrs_140168068329616
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168047243024 = _static_140168208991440('python', u'widget.Label(here)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:widget.Label(here)' (34:71)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6cb63850> -> __condition
            __expression = __cache_140168047243024

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'Field')
            else:
                __content = __cache_140168047243024
                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>:</label>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168068330640
            __attrs_140168068330640 = _static_140168257770128

            # <Value u'field/workflowable | nothing' (35:27)> -> __condition
            __token = 1689
            try:
                __zt_tmp = __attrs_140168068330640
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'field/workflowable | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        (\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac2190> name=None at 7f7b6aac2610> -> __attrs_140168082099088
                __attrs_140168082099088 = _static_140168047370640
                __backup_wf_tool_140168046984336 = get('wf_tool', __marker)

                # <Value u'context/portal_workflow' (39:31)> -> __value
                __token = 1809
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/portal_workflow', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['wf_tool'] = __value
                __backup_obj_140168082098000 = get('obj', __marker)

                # <Value u'python:accessor()' (40:26)> -> __value
                __token = 1860
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'accessor()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['obj'] = __value
                __backup_review_state_140168047239632 = get('review_state', __marker)

                # <Value u"python:wf_tool.getInfoFor(obj, 'review_state', '')" (41:34)> -> __value
                __token = 1914
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"wf_tool.getInfoFor(obj, 'review_state', '')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['review_state'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047741008
                __default_140168047741008 = _DEFAULT_MARKER

                # <Substitution u'string:${obj/absolute_url}/content_status_history' (42:32)> -> __attr_href
                __token = 2000
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('string', u'${obj/absolute_url}/content_status_history', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168082097872
                __default_140168082097872 = _DEFAULT_MARKER

                # <Substitution u"python:test(review_state, review_state, 'private')" (43:32)> -> __attr_class
                __token = 2083
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140168208991440('python', u"test(review_state, review_state, 'private')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047371280
                __default_140168047371280 = _DEFAULT_MARKER

                # <Value u'review_state' (44:24)> -> __cache_140168047373584
                __token = 2160
                try:
                    __zt_tmp = __attrs_140168082099088
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047373584 = _static_140168208991440('path', u'review_state', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'review_state' (44:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aac27d0> -> __condition
                __expression = __cache_140168047373584

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n          review_state\n        ')
                else:
                    __content = __cache_140168047373584
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>')
                if (__backup_review_state_140168047239632 is __marker):
                    del econtext['review_state']
                else:
                    econtext['review_state'] = __backup_review_state_140168047239632
                if (__backup_obj_140168082098000 is __marker):
                    del econtext['obj']
                else:
                    econtext['obj'] = __backup_obj_140168082098000
                if (__backup_wf_tool_140168046984336 is __marker):
                    del econtext['wf_tool']
                else:
                    econtext['wf_tool'] = __backup_wf_tool_140168046984336
                __append(u'\n        )\n      ')
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168092264912
            __attrs_140168092264912 = _static_140168257770128

            # <br ... (0:0)
            # --------------------------------------------------------
            __append(u'<br />\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_hidden(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046955856
            __attrs_140168046955856 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab23b10> name=None at 7f7b6ab23590> -> __attrs_140168047768336
            __attrs_140168047768336 = _static_140168047770384

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047768784
            __default_140168047768784 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (145:34)> -> __attr_name
            __token = 7220
            try:
                __zt_tmp = __attrs_140168047768336
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047769872
            __default_140168047769872 = _DEFAULT_MARKER

            # <Substitution u'value' (146:34)> -> __attr_value
            __token = 7265
            try:
                __zt_tmp = __attrs_140168047768336
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_data(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047301712
            __attrs_140168047301712 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047238736
            __attrs_140168047238736 = _static_140168257770128
            __backup_macroname_140168054051216 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aaa14d0> name=None at 7f7b6aaa16d0> -> __value
            __value = _static_140168047236304
            econtext['macroname'] = __value

            # <Value u'widget_view' (53:30)> -> __macro
            __token = 2347
            try:
                __zt_tmp = __attrs_140168047238736
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'widget_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 2347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168054051216 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168054051216
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

            # <Static value=<_ast.Dict object at 0x7f7b6aaa1bd0> name=None at 7f7b6aaa1250> -> __attrs_140168047235536
            __attrs_140168047235536 = _static_140168047238096
            __backup_fieldName_140168026363216 = get('fieldName', __marker)

            # <Value u'fieldName|field/getName' (56:57)> -> __value
            __token = 2445
            try:
                __zt_tmp = __attrs_140168047235536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'fieldName|field/getName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fieldName'] = __value
            __backup_fieldtypename_140168026363664 = get('fieldtypename', __marker)

            # <Value u"python:field.getType().split('.')[-1]" (57:60)> -> __value
            __token = 2530
            try:
                __zt_tmp = __attrs_140168047235536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"field.getType().split('.')[-1]", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['fieldtypename'] = __value
            __backup_uid_140168159969168 = get('uid', __marker)

            # <Value u'context/UID|nothing' (58:49)> -> __value
            __token = 2619
            try:
                __zt_tmp = __attrs_140168047235536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047235856
            __default_140168047235856 = _DEFAULT_MARKER

            # <Substitution u'string:field ArchetypesField-${fieldtypename}' (59:30)> -> __attr_class
            __token = 2672
            try:
                __zt_tmp = __attrs_140168047235536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('string', u'field ArchetypesField-${fieldtypename}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047236880
            __default_140168047236880 = _DEFAULT_MARKER

            # <Substitution u'string:archetypes-fieldname-${fieldName}-${uid}' (60:26)> -> __attr_id
            __token = 2745
            try:
                __zt_tmp = __attrs_140168047235536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'archetypes-fieldname-${fieldName}-${uid}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047235792
            __attrs_140168047235792 = _static_140168257770128
            __backup_macroname_140168054052816 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aaa1ed0> name=None at 7f7b6aaa1090> -> __value
            __value = _static_140168047238864
            econtext['macroname'] = __value

            # <Value u'context/widgets/field/macros/base_view' (61:42)> -> __macro
            __token = 2838
            try:
                __zt_tmp = __attrs_140168047235792
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/field/macros/base_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 2838
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168054052816 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168054052816
            __append(u'\n    </div>')
            if (__backup_uid_140168159969168 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168159969168
            if (__backup_fieldtypename_140168026363664 is __marker):
                del econtext['fieldtypename']
            else:
                econtext['fieldtypename'] = __backup_fieldtypename_140168026363664
            if (__backup_fieldName_140168026363216 is __marker):
                del econtext['fieldName']
            else:
                econtext['fieldName'] = __backup_fieldName_140168026363216
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

            # <Static value=<_ast.Dict object at 0x7f7b6d16b490> name=None at 7f7b6d16bc50> -> __attrs_140168062242320
            __attrs_140168062242320 = _static_140168087909520
            __previous_i18n_domain_140168081260368 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168081258192
            __attrs_140168081258192 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168081257296
            __attrs_140168081257296 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title></head>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168160146192
            __attrs_140168160146192 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- Base Field Widgets -->\n    ')
            __token = None
            render_base_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_label(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_data(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_hidden(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140168081260368
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_base_view': render_base_view, u'render_label': render_label, u'render_hidden': render_hidden, u'render_data': render_data, u'render_view': render_view, 'render': render, }