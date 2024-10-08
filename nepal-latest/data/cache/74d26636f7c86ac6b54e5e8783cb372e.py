# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.Archetypes-1.16.6-py2.7.egg/Products/Archetypes/skins/archetypes/widgets/boolean.pt'

__tokens = {1428: (u"python:test(not not value and value not in ('0', 'False'), 1, 0)", 32, 36), 1621: (u'string:${fieldName}:boolean', 37, 36), 1683: (u' fieldNam', 38, 33), 1732: (u"d python:test(value, 'checked', Non", 39, 37), 1879: (u'string:${fieldName}:boolean:default', 43, 36), 1287: (u'field_macro | context/widgets/field/macros/edit', 30, 28), 1287: (u'field_macro | context/widgets/field/macros/edit', 30, 28), 603: (u"python:getKssClasses(fieldName,\n                              templateId='widgets/boolean', macro='boolean-field-view')", 16, 34), 757: (u' context/UID|nothin', 18, 33), 814: (u'kss_class', 19, 34), 855: (u' string:parent-fieldname-$fieldName-$ui', 20, 30), 977: (u'field/Vocabulary', 22, 34), 998: (u' accesso', 22, 55), 1043: (u'e python:voc and voc.getValue(str(key)) or k', 23, 34), 1122: (u'value', 24, 31), 2100: (u"python:test(not not value and value not in ('0', 'False'), 1, 0)", 51, 31), 2243: (u'fieldName', 54, 34), 2288: (u" python:value or '", 55, 34), 2406: (u'context/widgets/boolean/macros/edit', 59, 28), 2406: (u'context/widgets/boolean/macros/edit', 59, 28), 388: (u'context/@@kss_field_decorator_view', 13, 39), 461: (u' nocall:kssClassesView/getKssClassesInlineEditabl', 14, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168036761680 = u'edit'
_static_140168037225168 = {u'type': u'hidden', u'name': u'string:${fieldName}:boolean:default', u'value': u'', }
_static_140168037226704 = {u'type': u'hidden', u'name': u'', u'value': u'', }
_static_140168046938576 = {u'class': u'kss_class', u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168036615312 = u'edit'
_static_140168257770128 = {}
_static_140168026308560 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168037224656 = {u'checked': u"python:test(value, 'checked', None)", u'name': u'string:${fieldName}:boolean', u'value': u'on', u'class': u'noborder', u'type': u'checkbox', u'id': u'fieldName', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036763024
            __attrs_140168036763024 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036764048
            __attrs_140168036764048 = _static_140168257770128
            __backup_macroname_140168054158752 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a0a4050> name=None at 7f7b6a0a42d0> -> __value
            __value = _static_140168036761680
            econtext['macroname'] = __value

            def __fill_widget_body_label_prefix(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037227792
                __attrs_140168037227792 = _static_140168257770128
                __backup_value_140168026325456 = get('value', __marker)

                # <Value u"python:test(not not value and value not in ('0', 'False'), 1, 0)" (32:36)> -> __value
                __token = 1428
                try:
                    __zt_tmp = __attrs_140168037227792
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"test(not not value and value not in ('0', 'False'), 1, 0)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1150d0> name=None at 7f7b6a115710> -> __attrs_140168037225936
                __attrs_140168037225936 = _static_140168037224656

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="noborder" type="checkbox" value="on"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037226448
                __default_140168037226448 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}:boolean' (37:36)> -> __attr_name
                __token = 1621
                try:
                    __zt_tmp = __attrs_140168037225936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}:boolean', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037225424
                __default_140168037225424 = _DEFAULT_MARKER

                # <Substitution u'fieldName' (38:33)> -> __attr_id
                __token = 1683
                try:
                    __zt_tmp = __attrs_140168037225936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037226832
                __default_140168037226832 = _DEFAULT_MARKER

                # <Boolean u"python:test(value, 'checked', None)" (39:37)> -> __attr_checked
                __token = 1732
                try:
                    __zt_tmp = __attrs_140168037225936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_140168208991440('python', u"test(value, 'checked', None)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = u'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((u' checked="%s"' % __attr_checked))
                __append(u' />\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1152d0> name=None at 7f7b6a115e90> -> __attrs_140168047245392
                __attrs_140168047245392 = _static_140168037225168

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" value=""')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047247312
                __default_140168047247312 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}:boolean:default' (43:36)> -> __attr_name
                __token = 1879
                try:
                    __zt_tmp = __attrs_140168047245392
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}:boolean:default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))
                __append(u' />\n      ')
                if (__backup_value_140168026325456 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168026325456
            _slots = econtext[u'__slot_widget_body_label_prefix'] = _deque((__fill_widget_body_label_prefix, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (30:28)> -> __macro
            __token = 1287
            try:
                __zt_tmp = __attrs_140168036764048
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1287
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168054158752 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168054158752
            __append(u'\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_boolean_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b6aa589d0> name=None at 7f7b6aa58210> -> __attrs_140168162603600
            __attrs_140168162603600 = _static_140168046938576
            __backup_kss_class_140168025873040 = get('kss_class', __marker)

            # <Value u"python:getKssClasses(fieldName,\n                              templateId='widgets/boolean', macro='boolean-field-view')" (16:34)> -> __value
            __token = 603
            try:
                __zt_tmp = __attrs_140168162603600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"getKssClasses(fieldName,\n                              templateId='widgets/boolean', macro='boolean-field-view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kss_class'] = __value
            __backup_uid_140168046936848 = get('uid', __marker)

            # <Value u'context/UID|nothing' (18:33)> -> __value
            __token = 757
            try:
                __zt_tmp = __attrs_140168162603600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046939344
            __default_140168046939344 = _DEFAULT_MARKER

            # <Substitution u'kss_class' (19:34)> -> __attr_class
            __token = 814
            try:
                __zt_tmp = __attrs_140168162603600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('path', u'kss_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046937232
            __default_140168046937232 = _DEFAULT_MARKER

            # <Substitution u'string:parent-fieldname-$fieldName-$uid' (20:30)> -> __attr_id
            __token = 855
            try:
                __zt_tmp = __attrs_140168162603600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n            ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036763536
                __attrs_140168036763536 = _static_140168257770128
                __backup_voc_140168036762512 = get('voc', __marker)

                # <Value u'field/Vocabulary' (22:34)> -> __value
                __token = 977
                try:
                    __zt_tmp = __attrs_140168036763536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'field/Vocabulary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['voc'] = __value
                __backup_key_140168036763920 = get('key', __marker)

                # <Value u'accessor' (22:55)> -> __value
                __token = 998
                try:
                    __zt_tmp = __attrs_140168036763536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['key'] = __value
                __backup_value_140168036765328 = get('value', __marker)

                # <Value u'python:voc and voc.getValue(str(key)) or key' (23:34)> -> __value
                __token = 1043
                try:
                    __zt_tmp = __attrs_140168036763536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'voc and voc.getValue(str(key)) or key', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036762576
                __default_140168036762576 = _DEFAULT_MARKER

                # <Value u'value' (24:31)> -> __cache_140168036764112
                __token = 1122
                try:
                    __zt_tmp = __attrs_140168036763536
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168036764112 = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'value' (24:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a0a4110> -> __condition
                __expression = __cache_140168036764112

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>Yes No</span>')
                else:
                    __content = __cache_140168036764112
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_value_140168036765328 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168036765328
                if (__backup_key_140168036763920 is __marker):
                    del econtext['key']
                else:
                    econtext['key'] = __backup_key_140168036763920
                if (__backup_voc_140168036762512 is __marker):
                    del econtext['voc']
                else:
                    econtext['voc'] = __backup_voc_140168036762512
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n        </span>')
            if (__backup_uid_140168046936848 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168046936848
            if (__backup_kss_class_140168025873040 is __marker):
                del econtext['kss_class']
            else:
                econtext['kss_class'] = __backup_kss_class_140168025873040
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036762960
            __attrs_140168036762960 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1158d0> name=None at 7f7b6a115c90> -> __attrs_140168047246864
            __attrs_140168047246864 = _static_140168037226704
            __backup_value_140168046937104 = get('value', __marker)

            # <Value u"python:test(not not value and value not in ('0', 'False'), 1, 0)" (51:31)> -> __value
            __token = 2100
            try:
                __zt_tmp = __attrs_140168047246864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"test(not not value and value not in ('0', 'False'), 1, 0)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['value'] = __value

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047246992
            __default_140168047246992 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (54:34)> -> __attr_name
            __token = 2243
            try:
                __zt_tmp = __attrs_140168047246864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047247056
            __default_140168047247056 = _DEFAULT_MARKER

            # <Substitution u"python:value or ''" (55:34)> -> __attr_value
            __token = 2288
            try:
                __zt_tmp = __attrs_140168047246864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140168208991440('python', u"value or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />')
            if (__backup_value_140168046937104 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140168046937104
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047245520
            __attrs_140168047245520 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036617040
            __attrs_140168036617040 = _static_140168257770128
            __backup_macroname_140168056407776 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6a080490> name=None at 7f7b6a080810> -> __value
            __value = _static_140168036615312
            econtext['macroname'] = __value

            # <Value u'context/widgets/boolean/macros/edit' (59:28)> -> __macro
            __token = 2406
            try:
                __zt_tmp = __attrs_140168036617040
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/boolean/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 2406
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168056407776 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168056407776
            __append(u'\n    </div>')
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025872720
            __attrs_140168025872720 = _static_140168257770128
            __backup_kssClassesView_140168047532752 = get('kssClassesView', __marker)

            # <Value u'context/@@kss_field_decorator_view' (13:39)> -> __value
            __token = 388
            try:
                __zt_tmp = __attrs_140168025872720
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@kss_field_decorator_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kssClassesView'] = __value
            __backup_getKssClasses_140168081542288 = get('getKssClasses', __marker)

            # <Value u'nocall:kssClassesView/getKssClassesInlineEditable' (14:37)> -> __value
            __token = 461
            try:
                __zt_tmp = __attrs_140168025872720
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('nocall', u'kssClassesView/getKssClassesInlineEditable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['getKssClasses'] = __value
            __append(u'\n        ')
            __token = None
            render_boolean_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    ')
            if (__backup_getKssClasses_140168081542288 is __marker):
                del econtext['getKssClasses']
            else:
                econtext['getKssClasses'] = __backup_getKssClasses_140168081542288
            if (__backup_kssClassesView_140168047532752 is __marker):
                del econtext['kssClassesView']
            else:
                econtext['kssClassesView'] = __backup_kssClassesView_140168047532752
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

            # <Static value=<_ast.Dict object at 0x7f7b696abfd0> name=None at 7f7b6ccdfe10> -> __attrs_140168026653584
            __attrs_140168026653584 = _static_140168026308560
            __previous_i18n_domain_140168026653200 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046847568
            __attrs_140168046847568 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047034192
            __attrs_140168047034192 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title></head>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168068785872
            __attrs_140168068785872 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- Boolean Widgets -->\n\n    ')
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
            __append(u'\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168026653200
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_boolean_field_view': render_boolean_field_view, u'render_hidden': render_hidden, u'render_search': render_search, u'render_view': render_view, 'render': render, }