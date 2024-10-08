# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/skins/bika/bika_widgets/decimal.pt'

__tokens = {1682: (u'string:${fieldName}', 36, 36), 1783: (u'e val', 38, 35), 1825: (u'ze widget/s', 39, 33), 1736: (u' fieldNam', 37, 33), 1880: (u'der widget/placeholder|not', 40, 39), 1948: (u'ngth widget/maxlength|no', 41, 36), 2031: (u'widget/unit', 42, 51), 1389: (u'field_macro | context/widgets/field/macros/edit', 28, 28), 1389: (u'field_macro | context/widgets/field/macros/edit', 28, 28), 2169: (u'context/widgets/decimal/macros/edit', 49, 28), 2169: (u'context/widgets/decimal/macros/edit', 49, 28), 388: (u'widget/dollars_and_cents', 13, 41), 450: (u' widget/whole_dollar', 14, 36), 511: (u's widget/thousands_comm', 15, 38), 568: (u'at python:dollars_and_cents or whole_dollars or thousands_com', 16, 30), 660: (u'ult acce', 17, 26), 702: (u'tted python:r', 18, 28), 743: (u'  pps modules/Products/PythonScripts/st', 19, 21), 816: (u'matted python:(dollars_and_cents and pps.dollars_and_cents(formatted)) or fo', 20, 26), 926: (u'rmatted python:(whole_dollars and pps.whole_dollars(formatted)) or f', 21, 25), 1028: (u'ormatted python:(thousands_commas and pps.thousands_commas(formatted)) or ', 22, 24), 1133: (u'   result python:(if_format and formatted)', 23, 20), 1204: (u'      unit ', 24, 17), 1265: (u"python: '%s %s' % (result, unit) if unit else result", 25, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047245456 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168046975056 = u'edit'
_static_140168046975696 = {u'class': u'discreet', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168026653072 = u'edit'
_static_140168257770128 = {}
_static_140168015805840 = {u'name': u'', u'placeholder': u'widget/placeholder|nothing', u'value': u'', u'class': u'blurrable firstToFocus', u'maxlength': u'widget/maxlength|nothing', u'type': u'text', u'id': u'fieldName', u'size': u'30', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046894032
            __attrs_140168046894032 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026654800
            __attrs_140168026654800 = _static_140168257770128
            __backup_macroname_140168106873312 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b69700190> name=None at 7f7b69700b50> -> __value
            __value = _static_140168026653072
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015802576
                __attrs_140168015802576 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b68ca7d90> name=None at 7f7b68ca7910> -> __attrs_140168046976336
                __attrs_140168046976336 = _static_140168015805840

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" class="blurrable firstToFocus"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015804624
                __default_140168015804624 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}' (36:36)> -> __attr_name
                __token = 1682
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015805712
                __default_140168015805712 = _DEFAULT_MARKER

                # <Substitution u'value' (38:35)> -> __attr_value
                __token = 1783
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015802448
                __default_140168015802448 = _DEFAULT_MARKER

                # <Substitution u'widget/size' (39:33)> -> __attr_size
                __token = 1825
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_size = _static_140168208991440('path', u'widget/size', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_size = __quote(__attr_size, '"', '&quot;', u'30', _DEFAULT_MARKER)
                if (__attr_size is not None):
                    __append((u' size="%s"' % __attr_size))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015804880
                __default_140168015804880 = _DEFAULT_MARKER

                # <Substitution u'fieldName' (37:33)> -> __attr_id
                __token = 1736
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015805264
                __default_140168015805264 = _DEFAULT_MARKER

                # <Substitution u'widget/placeholder|nothing' (40:39)> -> __attr_placeholder
                __token = 1880
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_placeholder = _static_140168208991440('path', u'widget/placeholder|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_placeholder is not None):
                    __append((u' placeholder="%s"' % __attr_placeholder))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046976208
                __default_140168046976208 = _DEFAULT_MARKER

                # <Substitution u'widget/maxlength|nothing' (41:36)> -> __attr_maxlength
                __token = 1948
                try:
                    __zt_tmp = __attrs_140168046976336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_maxlength = _static_140168208991440('path', u'widget/maxlength|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_maxlength is not None):
                    __append((u' maxlength="%s"' % __attr_maxlength))
                __append(u' />')

                # <Static value=<_ast.Dict object at 0x7f7b6aa61ad0> name=None at 7f7b6aa615d0> -> __attrs_140168046975312
                __attrs_140168046975312 = _static_140168046975696

                # <em ... (0:0)
                # --------------------------------------------------------
                __append(u"<em class='discreet'>")

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046973264
                __default_140168046973264 = _DEFAULT_MARKER

                # <Value u'widget/unit' (42:51)> -> __cache_140168046976848
                __token = 2031
                try:
                    __zt_tmp = __attrs_140168046975312
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046976848 = _static_140168208991440('path', u'widget/unit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/unit' (42:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa61790> -> __condition
                __expression = __cache_140168046976848

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168046976848
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</em>\n        </span>')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (28:28)> -> __macro
            __token = 1389
            try:
                __zt_tmp = __attrs_140168026654800
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1389
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168106873312 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168106873312
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046893904
            __attrs_140168046893904 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046976720
            __attrs_140168046976720 = _static_140168257770128
            __backup_macroname_140168057718336 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa61850> name=None at 7f7b6aa61610> -> __value
            __value = _static_140168046975056
            econtext['macroname'] = __value

            # <Value u'context/widgets/decimal/macros/edit' (49:28)> -> __macro
            __token = 2169
            try:
                __zt_tmp = __attrs_140168046976720
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/decimal/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 2169
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057718336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057718336
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026329424
            __attrs_140168026329424 = _static_140168257770128
            __backup_dollars_and_cents_140168015847184 = get('dollars_and_cents', __marker)

            # <Value u'widget/dollars_and_cents' (13:41)> -> __value
            __token = 388
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/dollars_and_cents', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['dollars_and_cents'] = __value
            __backup_whole_dollars_140168047306768 = get('whole_dollars', __marker)

            # <Value u'widget/whole_dollars' (14:36)> -> __value
            __token = 450
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/whole_dollars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['whole_dollars'] = __value
            __backup_thousands_commas_140168015847696 = get('thousands_commas', __marker)

            # <Value u'widget/thousands_commas' (15:38)> -> __value
            __token = 511
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/thousands_commas', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['thousands_commas'] = __value
            __backup_if_format_140168092335440 = get('if_format', __marker)

            # <Value u'python:dollars_and_cents or whole_dollars or thousands_commas' (16:30)> -> __value
            __token = 568
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'dollars_and_cents or whole_dollars or thousands_commas', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['if_format'] = __value
            __backup_result_140168037311248 = get('result', __marker)

            # <Value u'accessor' (17:26)> -> __value
            __token = 660
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['result'] = __value
            __backup_formatted_140168037323792 = get('formatted', __marker)

            # <Value u'python:result' (18:28)> -> __value
            __token = 702
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'result', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['formatted'] = __value
            __backup_pps_140168036772304 = get('pps', __marker)

            # <Value u'modules/Products/PythonScripts/standard' (19:21)> -> __value
            __token = 743
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'modules/Products/PythonScripts/standard', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['pps'] = __value
            __backup_formatted_140168036763600 = get('formatted', __marker)

            # <Value u'python:(dollars_and_cents and pps.dollars_and_cents(formatted)) or formatted' (20:26)> -> __value
            __token = 816
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'(dollars_and_cents and pps.dollars_and_cents(formatted)) or formatted', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['formatted'] = __value
            __backup_formatted_140168015845584 = get('formatted', __marker)

            # <Value u'python:(whole_dollars and pps.whole_dollars(formatted)) or formatted' (21:25)> -> __value
            __token = 926
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'(whole_dollars and pps.whole_dollars(formatted)) or formatted', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['formatted'] = __value
            __backup_formatted_140168036939536 = get('formatted', __marker)

            # <Value u'python:(thousands_commas and pps.thousands_commas(formatted)) or formatted' (22:24)> -> __value
            __token = 1028
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'(thousands_commas and pps.thousands_commas(formatted)) or formatted', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['formatted'] = __value
            __backup_result_140168036940816 = get('result', __marker)

            # <Value u'python:(if_format and formatted) or result' (23:20)> -> __value
            __token = 1133
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'(if_format and formatted) or result', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['result'] = __value
            __backup_unit_140168047022672 = get('unit', __marker)

            # <Value u'widget/unit' (24:17)> -> __value
            __token = 1204
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'widget/unit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['unit'] = __value

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026330128
            __default_140168026330128 = _DEFAULT_MARKER

            # <Value u"python: '%s %s' % (result, unit) if unit else result" (25:36)> -> __cache_140168026331920
            __token = 1265
            try:
                __zt_tmp = __attrs_140168026329424
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168026331920 = _static_140168208991440('python', u" '%s %s' % (result, unit) if unit else result", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u"python: '%s %s' % (result, unit) if unit else result" (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b1e10> -> __condition
            __expression = __cache_140168026331920

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168026331920
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            if (__backup_unit_140168047022672 is __marker):
                del econtext['unit']
            else:
                econtext['unit'] = __backup_unit_140168047022672
            if (__backup_result_140168036940816 is __marker):
                del econtext['result']
            else:
                econtext['result'] = __backup_result_140168036940816
            if (__backup_formatted_140168036939536 is __marker):
                del econtext['formatted']
            else:
                econtext['formatted'] = __backup_formatted_140168036939536
            if (__backup_formatted_140168015845584 is __marker):
                del econtext['formatted']
            else:
                econtext['formatted'] = __backup_formatted_140168015845584
            if (__backup_formatted_140168036763600 is __marker):
                del econtext['formatted']
            else:
                econtext['formatted'] = __backup_formatted_140168036763600
            if (__backup_pps_140168036772304 is __marker):
                del econtext['pps']
            else:
                econtext['pps'] = __backup_pps_140168036772304
            if (__backup_formatted_140168037323792 is __marker):
                del econtext['formatted']
            else:
                econtext['formatted'] = __backup_formatted_140168037323792
            if (__backup_result_140168037311248 is __marker):
                del econtext['result']
            else:
                econtext['result'] = __backup_result_140168037311248
            if (__backup_if_format_140168092335440 is __marker):
                del econtext['if_format']
            else:
                econtext['if_format'] = __backup_if_format_140168092335440
            if (__backup_thousands_commas_140168015847696 is __marker):
                del econtext['thousands_commas']
            else:
                econtext['thousands_commas'] = __backup_thousands_commas_140168015847696
            if (__backup_whole_dollars_140168047306768 is __marker):
                del econtext['whole_dollars']
            else:
                econtext['whole_dollars'] = __backup_whole_dollars_140168047306768
            if (__backup_dollars_and_cents_140168015847184 is __marker):
                del econtext['dollars_and_cents']
            else:
                econtext['dollars_and_cents'] = __backup_dollars_and_cents_140168015847184
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

            # <Static value=<_ast.Dict object at 0x7f7b6aaa3890> name=None at 7f7b6aaa36d0> -> __attrs_140168047245584
            __attrs_140168047245584 = _static_140168047245456
            __previous_i18n_domain_140168047246288 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047244176
            __attrs_140168047244176 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047245264
            __attrs_140168047245264 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title></head>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047244048
            __attrs_140168047244048 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- Float Widgets -->\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168047246288
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_view': render_view, 'render': render, }