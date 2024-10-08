# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/duration/display.pt'

__tokens = {150: (u'python:view.name', 5, 30), 197: (u' python:view.valu', 6, 29), 245: (u"  python:value.get('days', ", 7, 28), 303: (u"   python:value.get('hours',", 8, 27), 362: (u"    python:value.get('minutes'", 9, 26), 423: (u"s    python:value.get('seconds", 10, 25), 484: (u'      python:view', 11, 24), 532: (u"_klass python:'{}-display'.format", 12, 23), 596: (u"ss      python:' '.join([klass, mode", 13, 22), 670: (u'klass', 14, 27), 759: (u'python: view.show_days and days > 0', 17, 25), 839: (u'days', 18, 42), 951: (u'python: view.show_hours and hours > 0', 22, 25), 1034: (u'hours', 23, 43), 1150: (u'python: view.show_minutes and minutes > 0', 27, 25), 1239: (u'minutes', 28, 45), 1359: (u'python: view.show_seconds and seconds > 0', 32, 25), 1448: (u'seconds', 33, 45)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240604537040 = {u'class': u'klass', }
_static_140241087907024 = __compile_zt_expr
_static_140241087907728 = __C2ZContextWrapper
_static_140240604787664 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140241133802128 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8c4f6e73d0> name=None at 7f8c4f6e77d0> -> __attrs_140240604788304
            __attrs_140240604788304 = _static_140240604787664
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6aa0d0> name=None at 7f8c4f6aaf10> -> __attrs_140240604540624
            __attrs_140240604540624 = _static_140240604537040
            __backup_name_140240781386960 = get('name', __marker)

            # <Value u'python:view.name' (5:30)> -> __value
            __token = 150
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['name'] = __value
            __backup_value_140240779875280 = get('value', __marker)

            # <Value u'python:view.value' (6:29)> -> __value
            __token = 197
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_days_140240781280016 = get('days', __marker)

            # <Value u"python:value.get('days', 0)" (7:28)> -> __value
            __token = 245
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('days', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['days'] = __value
            __backup_hours_140240780917008 = get('hours', __marker)

            # <Value u"python:value.get('hours', 0)" (8:27)> -> __value
            __token = 303
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('hours', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['hours'] = __value
            __backup_minutes_140240748636496 = get('minutes', __marker)

            # <Value u"python:value.get('minutes', 0)" (9:26)> -> __value
            __token = 362
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('minutes', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['minutes'] = __value
            __backup_seconds_140240604787088 = get('seconds', __marker)

            # <Value u"python:value.get('seconds', 0)" (10:25)> -> __value
            __token = 423
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"value.get('seconds', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['seconds'] = __value
            __backup_klass_140240605379152 = get('klass', __marker)

            # <Value u'python:view.klass' (11:24)> -> __value
            __token = 484
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['klass'] = __value
            __backup_mode_klass_140240779871504 = get('mode_klass', __marker)

            # <Value u"python:'{}-display'.format(klass)" (12:23)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"'{}-display'.format(klass)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['mode_klass'] = __value
            __backup_klass_140240779876560 = get('klass', __marker)

            # <Value u"python:' '.join([klass, mode_klass])" (13:22)> -> __value
            __token = 596
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"' '.join([klass, mode_klass])", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['klass'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604538960
            __default_140240604538960 = _DEFAULT_MARKER

            # <Substitution u'klass' (14:27)> -> __attr_class
            __token = 670
            try:
                __zt_tmp = __attrs_140240604540624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240604538576
            __attrs_140240604538576 = _static_140241133802128

            # <Value u'python: view.show_days and days > 0' (17:25)> -> __condition
            __token = 759
            try:
                __zt_tmp = __attrs_140240604538576
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' view.show_days and days > 0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240756865216_days = ''
                __stream_140240604539856 = []
                __append_140240604539856 = __stream_140240604539856.append
                __append_140240604539856(u'\n      ')
                __stream_140240756865216_days = []
                __append_140240756865216_days = __stream_140240756865216_days.append

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606441680
                __attrs_140240606441680 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606441744
                __default_140240606441744 = _DEFAULT_MARKER

                # <Value u'days' (18:42)> -> __cache_140240606442576
                __token = 839
                try:
                    __zt_tmp = __attrs_140240606441680
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240606442576 = _static_140241087907024('path', u'days', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'days' (18:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4f87b190> -> __condition
                __expression = __cache_140240606442576

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140240756865216_days(u'<span/>')
                else:
                    __content = __cache_140240606442576
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140240756865216_days(__content)
                __append_140240604539856(u'${days}')
                __stream_140240756865216_days = ''.join(__stream_140240756865216_days)
                __append_140240604539856(u'\n      days\n    ')
                __msgid_140240604539856 = __re_whitespace(''.join(__stream_140240604539856)).strip()
                if u'duration_widget_days_number':
                    __append(translate(u'duration_widget_days_number', mapping={u'days': __stream_140240756865216_days, }, default=__msgid_140240604539856, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606442320
            __attrs_140240606442320 = _static_140241133802128

            # <Value u'python: view.show_hours and hours > 0' (22:25)> -> __condition
            __token = 951
            try:
                __zt_tmp = __attrs_140240606442320
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' view.show_hours and hours > 0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240756865216_hours = ''
                __stream_140240606442000 = []
                __append_140240606442000 = __stream_140240606442000.append
                __append_140240606442000(u'\n      ')
                __stream_140240756865216_hours = []
                __append_140240756865216_hours = __stream_140240756865216_hours.append

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240803779216
                __attrs_140240803779216 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240803781008
                __default_140240803781008 = _DEFAULT_MARKER

                # <Value u'hours' (23:43)> -> __cache_140240803781712
                __token = 1034
                try:
                    __zt_tmp = __attrs_140240803779216
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240803781712 = _static_140241087907024('path', u'hours', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'hours' (23:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5b4ad050> -> __condition
                __expression = __cache_140240803781712

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140240756865216_hours(u'<span/>')
                else:
                    __content = __cache_140240803781712
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140240756865216_hours(__content)
                __append_140240606442000(u'${hours}')
                __stream_140240756865216_hours = ''.join(__stream_140240756865216_hours)
                __append_140240606442000(u'\n      hours\n    ')
                __msgid_140240606442000 = __re_whitespace(''.join(__stream_140240606442000)).strip()
                if u'duration_widget_hours_number':
                    __append(translate(u'duration_widget_hours_number', mapping={u'hours': __stream_140240756865216_hours, }, default=__msgid_140240606442000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606444560
            __attrs_140240606444560 = _static_140241133802128

            # <Value u'python: view.show_minutes and minutes > 0' (27:25)> -> __condition
            __token = 1150
            try:
                __zt_tmp = __attrs_140240606444560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' view.show_minutes and minutes > 0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240756865216_minutes = ''
                __stream_140240604540112 = []
                __append_140240604540112 = __stream_140240604540112.append
                __append_140240604540112(u'\n      ')
                __stream_140240756865216_minutes = []
                __append_140240756865216_minutes = __stream_140240756865216_minutes.append

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606445008
                __attrs_140240606445008 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606443600
                __default_140240606443600 = _DEFAULT_MARKER

                # <Value u'minutes' (28:45)> -> __cache_140240606443152
                __token = 1239
                try:
                    __zt_tmp = __attrs_140240606445008
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240606443152 = _static_140241087907024('path', u'minutes', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'minutes' (28:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4f87bc90> -> __condition
                __expression = __cache_140240606443152

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140240756865216_minutes(u'<span/>')
                else:
                    __content = __cache_140240606443152
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140240756865216_minutes(__content)
                __append_140240604540112(u'${minutes}')
                __stream_140240756865216_minutes = ''.join(__stream_140240756865216_minutes)
                __append_140240604540112(u'\n      minutes\n    ')
                __msgid_140240604540112 = __re_whitespace(''.join(__stream_140240604540112)).strip()
                if u'duration_widget_minutes_number':
                    __append(translate(u'duration_widget_minutes_number', mapping={u'minutes': __stream_140240756865216_minutes, }, default=__msgid_140240604540112, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240756195728
            __attrs_140240756195728 = _static_140241133802128

            # <Value u'python: view.show_seconds and seconds > 0' (32:25)> -> __condition
            __token = 1359
            try:
                __zt_tmp = __attrs_140240756195728
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' view.show_seconds and seconds > 0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240756865216_seconds = ''
                __stream_140240606444240 = []
                __append_140240606444240 = __stream_140240606444240.append
                __append_140240606444240(u'\n      ')
                __stream_140240756865216_seconds = []
                __append_140240756865216_seconds = __stream_140240756865216_seconds.append

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240756197456
                __attrs_140240756197456 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240756197776
                __default_140240756197776 = _DEFAULT_MARKER

                # <Value u'seconds' (33:45)> -> __cache_140240756196560
                __token = 1448
                try:
                    __zt_tmp = __attrs_140240756197456
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240756196560 = _static_140241087907024('path', u'seconds', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'seconds' (33:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5874c310> -> __condition
                __expression = __cache_140240756196560

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140240756865216_seconds(u'<span/>')
                else:
                    __content = __cache_140240756196560
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140240756865216_seconds(__content)
                __append_140240606444240(u'${seconds}')
                __stream_140240756865216_seconds = ''.join(__stream_140240756865216_seconds)
                __append_140240606444240(u'\n      seconds\n    ')
                __msgid_140240606444240 = __re_whitespace(''.join(__stream_140240606444240)).strip()
                if u'duration_widget_seconds_number':
                    __append(translate(u'duration_widget_seconds_number', mapping={u'seconds': __stream_140240756865216_seconds, }, default=__msgid_140240606444240, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')
            __append(u'\n\n  </div>')
            if (__backup_klass_140240779876560 is __marker):
                del econtext['klass']
            else:
                econtext['klass'] = __backup_klass_140240779876560
            if (__backup_mode_klass_140240779871504 is __marker):
                del econtext['mode_klass']
            else:
                econtext['mode_klass'] = __backup_mode_klass_140240779871504
            if (__backup_klass_140240605379152 is __marker):
                del econtext['klass']
            else:
                econtext['klass'] = __backup_klass_140240605379152
            if (__backup_seconds_140240604787088 is __marker):
                del econtext['seconds']
            else:
                econtext['seconds'] = __backup_seconds_140240604787088
            if (__backup_minutes_140240748636496 is __marker):
                del econtext['minutes']
            else:
                econtext['minutes'] = __backup_minutes_140240748636496
            if (__backup_hours_140240780917008 is __marker):
                del econtext['hours']
            else:
                econtext['hours'] = __backup_hours_140240780917008
            if (__backup_days_140240781280016 is __marker):
                del econtext['days']
            else:
                econtext['days'] = __backup_days_140240781280016
            if (__backup_value_140240779875280 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_140240779875280
            if (__backup_name_140240781386960 is __marker):
                del econtext['name']
            else:
                econtext['name'] = __backup_name_140240781386960
            __append(u'\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }