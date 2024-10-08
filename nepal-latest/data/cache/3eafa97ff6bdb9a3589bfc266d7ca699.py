# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/duration/input.pt'

__tokens = {150: (u'python:view.name', 5, 30), 197: (u' python:view.valu', 6, 29), 245: (u"  python:value.get('days', ", 7, 28), 303: (u"   python:value.get('hours',", 8, 27), 362: (u"    python:value.get('minutes'", 9, 26), 423: (u"s    python:value.get('seconds", 10, 25), 484: (u'      python:view', 11, 24), 532: (u"_klass python:'{}-input'.format", 12, 23), 594: (u"ss      python:' '.join([klass, mode", 13, 22), 670: (u'klass', 14, 29), 732: (u'string:${name}.days:record:int', 17, 26), 797: (u"python:'col-auto' if view.show_days else 'd-none'", 18, 33), 943: (u'id', 20, 35), 1032: (u'id', 22, 34), 1071: (u' i', 23, 35), 1111: (u'e da', 24, 35), 1189: (u'string:${name}.hours:record:int', 27, 26), 1255: (u"python:'col-auto' if view.show_hours else 'd-none'", 28, 33), 1403: (u'id', 30, 35), 1493: (u'id', 32, 34), 1532: (u' i', 33, 35), 1572: (u'e hou', 34, 35), 1650: (u'string:${name}.minutes:record:int', 37, 26), 1718: (u"python:'col-auto' if view.show_minutes else 'd-none'", 38, 33), 1870: (u'id', 40, 35), 1962: (u'id', 42, 34), 2001: (u' i', 43, 35), 2041: (u'e minut', 44, 35), 2121: (u'string:${name}.seconds:record:int', 47, 26), 2189: (u"python:'col-auto' if view.show_seconds else 'd-none'", 48, 33), 2341: (u'id', 50, 35), 2433: (u'id', 52, 34), 2472: (u' i', 53, 35), 2512: (u'e secon', 54, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240606107856 = {u'for': u'id', }
_static_140240604790416 = {u'class': u"python:'col-auto' if view.show_days else 'd-none'", }
_static_140241087907024 = __compile_zt_expr
_static_140240604882320 = {u'for': u'id', }
_static_140240752406352 = {u'for': u'id', }
_static_140240606444560 = {u'for': u'id', }
_static_140240606106320 = {u'class': u'col-auto', }
_static_140240793572304 = {u'value': u'seconds', u'type': u'number', u'id': u'id', u'name': u'id', u'size': u'5', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240752404816 = {u'class': u'col-auto', }
_static_140240604789136 = {u'class': u'form-row', }
_static_140240604883408 = {u'value': u'days', u'type': u'number', u'id': u'id', u'name': u'id', u'size': u'5', }
_static_140240612231376 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240606108944 = {u'value': u'hours', u'type': u'number', u'id': u'id', u'name': u'id', u'size': u'5', }
_static_140240606443024 = {u'class': u'col-auto', }
_static_140240752402576 = {u'value': u'minutes', u'type': u'number', u'id': u'id', u'name': u'id', u'size': u'5', }
_static_140240612232528 = {u'class': u'klass', }

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

            # <Static value=<_ast.Dict object at 0x7f8c4fe008d0> name=None at 7f8c4fe00890> -> __attrs_140240610144784
            __attrs_140240610144784 = _static_140240612231376
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4fe00d50> name=None at 7f8c4fe00d10> -> __attrs_140240604787216
            __attrs_140240604787216 = _static_140240612232528
            __backup_name_140240612230288 = get('name', __marker)

            # <Value u'python:view.name' (5:30)> -> __value
            __token = 150
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['name'] = __value
            __backup_value_140240612230800 = get('value', __marker)

            # <Value u'python:view.value' (6:29)> -> __value
            __token = 197
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_days_140240612230416 = get('days', __marker)

            # <Value u"python:value.get('days', 0)" (7:28)> -> __value
            __token = 245
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('days', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['days'] = __value
            __backup_hours_140240604786768 = get('hours', __marker)

            # <Value u"python:value.get('hours', 0)" (8:27)> -> __value
            __token = 303
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('hours', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['hours'] = __value
            __backup_minutes_140240604786832 = get('minutes', __marker)

            # <Value u"python:value.get('minutes', 0)" (9:26)> -> __value
            __token = 362
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('minutes', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['minutes'] = __value
            __backup_seconds_140240604786896 = get('seconds', __marker)

            # <Value u"python:value.get('seconds', 0)" (10:25)> -> __value
            __token = 423
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('seconds', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['seconds'] = __value
            __backup_klass_140240604786960 = get('klass', __marker)

            # <Value u'python:view.klass' (11:24)> -> __value
            __token = 484
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['klass'] = __value
            __backup_mode_klass_140240604787024 = get('mode_klass', __marker)

            # <Value u"python:'{}-input'.format(klass)" (12:23)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"'{}-input'.format(klass)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['mode_klass'] = __value
            __backup_klass_140240604787088 = get('klass', __marker)

            # <Value u"python:' '.join([klass, mode_klass])" (13:22)> -> __value
            __token = 594
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"' '.join([klass, mode_klass])", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['klass'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612232848
            __default_140240612232848 = _DEFAULT_MARKER

            # <Substitution u'klass' (14:29)> -> __attr_class
            __token = 670
            try:
                __zt_tmp = __attrs_140240604787216
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7990> name=None at 7f8c4f6e7950> -> __attrs_140240604789712
            __attrs_140240604789712 = _static_140240604789136

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-row">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7e90> name=None at 7f8c4f6e7e50> -> __attrs_140240604881296
            __attrs_140240604881296 = _static_140240604790416
            __backup_id_140240604788624 = get('id', __marker)

            # <Value u'string:${name}.days:record:int' (17:26)> -> __value
            __token = 732
            try:
                __zt_tmp = __attrs_140240604881296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('string', u'${name}.days:record:int', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['id'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604880976
            __default_140240604880976 = _DEFAULT_MARKER

            # <Substitution u"python:'col-auto' if view.show_days else 'd-none'" (18:33)> -> __attr_class
            __token = 797
            try:
                __zt_tmp = __attrs_140240604881296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('python', u"'col-auto' if view.show_days else 'd-none'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6fe590> name=None at 7f8c4f6fe550> -> __attrs_140240604882960
            __attrs_140240604882960 = _static_140240604882320

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604882640
            __default_140240604882640 = _DEFAULT_MARKER

            # <Substitution u'id' (20:35)> -> __attr_for
            __token = 943
            try:
                __zt_tmp = __attrs_140240604882960
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_for = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_for is not None):
                __append((u' for="%s"' % __attr_for))
            __append(u'>')
            __stream_140240604882128 = []
            __append_140240604882128 = __stream_140240604882128.append
            __append_140240604882128(u'Days')
            __msgid_140240604882128 = __re_whitespace(''.join(__stream_140240604882128)).strip()
            if u'duration_widget_label_days':
                __append(translate(u'duration_widget_label_days', mapping=None, default=__msgid_140240604882128, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6fe9d0> name=None at 7f8c4f6fead0> -> __attrs_140240606106128
            __attrs_140240606106128 = _static_140240604883408

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="number" size="5"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604884688
            __default_140240604884688 = _DEFAULT_MARKER

            # <Substitution u'id' (22:34)> -> __attr_id
            __token = 1032
            try:
                __zt_tmp = __attrs_140240606106128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604884944
            __default_140240604884944 = _DEFAULT_MARKER

            # <Substitution u'id' (23:35)> -> __attr_name
            __token = 1071
            try:
                __zt_tmp = __attrs_140240606106128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606105872
            __default_140240606105872 = _DEFAULT_MARKER

            # <Substitution u'days' (24:35)> -> __attr_value
            __token = 1111
            try:
                __zt_tmp = __attrs_140240606106128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'days', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      </div>')
            if (__backup_id_140240604788624 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140240604788624
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c4f8292d0> name=None at 7f8c4f6fe390> -> __attrs_140240606107024
            __attrs_140240606107024 = _static_140240606106320
            __backup_id_140240604788944 = get('id', __marker)

            # <Value u'string:${name}.hours:record:int' (27:26)> -> __value
            __token = 1189
            try:
                __zt_tmp = __attrs_140240606107024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('string', u'${name}.hours:record:int', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['id'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606106704
            __default_140240606106704 = _DEFAULT_MARKER

            # <Substitution u"python:'col-auto' if view.show_hours else 'd-none'" (28:33)> -> __attr_class
            __token = 1255
            try:
                __zt_tmp = __attrs_140240606107024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('python', u"'col-auto' if view.show_hours else 'd-none'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'col-auto', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c4f8298d0> name=None at 7f8c4f829890> -> __attrs_140240606108496
            __attrs_140240606108496 = _static_140240606107856

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606108176
            __default_140240606108176 = _DEFAULT_MARKER

            # <Substitution u'id' (30:35)> -> __attr_for
            __token = 1403
            try:
                __zt_tmp = __attrs_140240606108496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_for = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_for is not None):
                __append((u' for="%s"' % __attr_for))
            __append(u'>')
            __stream_140240606107664 = []
            __append_140240606107664 = __stream_140240606107664.append
            __append_140240606107664(u'Hours')
            __msgid_140240606107664 = __re_whitespace(''.join(__stream_140240606107664)).strip()
            if u'duration_widget_label_hours':
                __append(translate(u'duration_widget_label_hours', mapping=None, default=__msgid_140240606107664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c4f829d10> name=None at 7f8c4f829e10> -> __attrs_140240606442832
            __attrs_140240606442832 = _static_140240606108944

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="number" size="5"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606442064
            __default_140240606442064 = _DEFAULT_MARKER

            # <Substitution u'id' (32:34)> -> __attr_id
            __token = 1493
            try:
                __zt_tmp = __attrs_140240606442832
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606442320
            __default_140240606442320 = _DEFAULT_MARKER

            # <Substitution u'id' (33:35)> -> __attr_name
            __token = 1532
            try:
                __zt_tmp = __attrs_140240606442832
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606442576
            __default_140240606442576 = _DEFAULT_MARKER

            # <Substitution u'hours' (34:35)> -> __attr_value
            __token = 1572
            try:
                __zt_tmp = __attrs_140240606442832
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'hours', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      </div>')
            if (__backup_id_140240604788944 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140240604788944
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c4f87b610> name=None at 7f8c4f829710> -> __attrs_140240606443728
            __attrs_140240606443728 = _static_140240606443024
            __backup_id_140240604790288 = get('id', __marker)

            # <Value u'string:${name}.minutes:record:int' (37:26)> -> __value
            __token = 1650
            try:
                __zt_tmp = __attrs_140240606443728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('string', u'${name}.minutes:record:int', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['id'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606443408
            __default_140240606443408 = _DEFAULT_MARKER

            # <Substitution u"python:'col-auto' if view.show_minutes else 'd-none'" (38:33)> -> __attr_class
            __token = 1718
            try:
                __zt_tmp = __attrs_140240606443728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('python', u"'col-auto' if view.show_minutes else 'd-none'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'col-auto', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c4f87bc10> name=None at 7f8c4f87bbd0> -> __attrs_140240606445200
            __attrs_140240606445200 = _static_140240606444560

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606444880
            __default_140240606444880 = _DEFAULT_MARKER

            # <Substitution u'id' (40:35)> -> __attr_for
            __token = 1870
            try:
                __zt_tmp = __attrs_140240606445200
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_for = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_for is not None):
                __append((u' for="%s"' % __attr_for))
            __append(u'>')
            __stream_140240606444368 = []
            __append_140240606444368 = __stream_140240606444368.append
            __append_140240606444368(u'Minutes')
            __msgid_140240606444368 = __re_whitespace(''.join(__stream_140240606444368)).strip()
            if u'duration_widget_label_minutes':
                __append(translate(u'duration_widget_label_minutes', mapping=None, default=__msgid_140240606444368, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c583ae090> name=None at 7f8c583ae050> -> __attrs_140240752404624
            __attrs_140240752404624 = _static_140240752402576

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="number" size="5"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240752403856
            __default_140240752403856 = _DEFAULT_MARKER

            # <Substitution u'id' (42:34)> -> __attr_id
            __token = 1962
            try:
                __zt_tmp = __attrs_140240752404624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240752404112
            __default_140240752404112 = _DEFAULT_MARKER

            # <Substitution u'id' (43:35)> -> __attr_name
            __token = 2001
            try:
                __zt_tmp = __attrs_140240752404624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240752404368
            __default_140240752404368 = _DEFAULT_MARKER

            # <Substitution u'minutes' (44:35)> -> __attr_value
            __token = 2041
            try:
                __zt_tmp = __attrs_140240752404624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'minutes', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      </div>')
            if (__backup_id_140240604790288 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140240604790288
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c583ae950> name=None at 7f8c4f87ba50> -> __attrs_140240752405520
            __attrs_140240752405520 = _static_140240752404816
            __backup_id_140240604881424 = get('id', __marker)

            # <Value u'string:${name}.seconds:record:int' (47:26)> -> __value
            __token = 2121
            try:
                __zt_tmp = __attrs_140240752405520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('string', u'${name}.seconds:record:int', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['id'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240752405200
            __default_140240752405200 = _DEFAULT_MARKER

            # <Substitution u"python:'col-auto' if view.show_seconds else 'd-none'" (48:33)> -> __attr_class
            __token = 2189
            try:
                __zt_tmp = __attrs_140240752405520
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('python', u"'col-auto' if view.show_seconds else 'd-none'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'col-auto', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c583aef50> name=None at 7f8c583aef10> -> __attrs_140240793571856
            __attrs_140240793571856 = _static_140240752406352

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793571536
            __default_140240793571536 = _DEFAULT_MARKER

            # <Substitution u'id' (50:35)> -> __attr_for
            __token = 2341
            try:
                __zt_tmp = __attrs_140240793571856
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_for = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_for is not None):
                __append((u' for="%s"' % __attr_for))
            __append(u'>')
            __stream_140240752406160 = []
            __append_140240752406160 = __stream_140240752406160.append
            __append_140240752406160(u'Seconds')
            __msgid_140240752406160 = __re_whitespace(''.join(__stream_140240752406160)).strip()
            if u'duration_widget_label_seconds':
                __append(translate(u'duration_widget_label_seconds', mapping=None, default=__msgid_140240752406160, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c5aaf13d0> name=None at 7f8c5aaf14d0> -> __attrs_140240793574352
            __attrs_140240793574352 = _static_140240793572304

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="number" size="5"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793573584
            __default_140240793573584 = _DEFAULT_MARKER

            # <Substitution u'id' (52:34)> -> __attr_id
            __token = 2433
            try:
                __zt_tmp = __attrs_140240793574352
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793573840
            __default_140240793573840 = _DEFAULT_MARKER

            # <Substitution u'id' (53:35)> -> __attr_name
            __token = 2472
            try:
                __zt_tmp = __attrs_140240793574352
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('path', u'id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793574096
            __default_140240793574096 = _DEFAULT_MARKER

            # <Substitution u'seconds' (54:35)> -> __attr_value
            __token = 2512
            try:
                __zt_tmp = __attrs_140240793574352
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'seconds', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n      </div>')
            if (__backup_id_140240604881424 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140240604881424
            __append(u'\n\n    </div>\n  </div>')
            if (__backup_klass_140240604787088 is __marker):
                del econtext['klass']
            else:
                econtext['klass'] = __backup_klass_140240604787088
            if (__backup_mode_klass_140240604787024 is __marker):
                del econtext['mode_klass']
            else:
                econtext['mode_klass'] = __backup_mode_klass_140240604787024
            if (__backup_klass_140240604786960 is __marker):
                del econtext['klass']
            else:
                econtext['klass'] = __backup_klass_140240604786960
            if (__backup_seconds_140240604786896 is __marker):
                del econtext['seconds']
            else:
                econtext['seconds'] = __backup_seconds_140240604786896
            if (__backup_minutes_140240604786832 is __marker):
                del econtext['minutes']
            else:
                econtext['minutes'] = __backup_minutes_140240604786832
            if (__backup_hours_140240604786768 is __marker):
                del econtext['hours']
            else:
                econtext['hours'] = __backup_hours_140240604786768
            if (__backup_days_140240612230416 is __marker):
                del econtext['days']
            else:
                econtext['days'] = __backup_days_140240612230416
            if (__backup_value_140240612230800 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140240612230800
            if (__backup_name_140240612230288 is __marker):
                del econtext['name']
            else:
                econtext['name'] = __backup_name_140240612230288
            __append(u'\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }