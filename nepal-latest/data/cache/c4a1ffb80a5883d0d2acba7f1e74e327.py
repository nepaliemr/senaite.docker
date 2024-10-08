# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.Archetypes-1.16.6-py2.7.egg/Products/Archetypes/skins/archetypes/widgets/string.pt'

__tokens = {1396: (u'fieldName', 33, 36), 1440: (u' fieldNam', 34, 33), 1487: (u'e val', 35, 35), 1529: (u'ze widget/s', 36, 33), 1584: (u'der widget/placeholder|not', 37, 39), 1652: (u'ngth widget/maxl', 38, 36), 1099: (u'field_macro | context/widgets/field/macros/edit', 25, 28), 1099: (u'field_macro | context/widgets/field/macros/edit', 25, 28), 1800: (u'context/widgets/string/macros/edit', 44, 28), 1800: (u'context/widgets/string/macros/edit', 44, 28), 599: (u"python:getKssClasses(fieldName,\n                              templateId='widgets/string', macro='string-field-view')", 14, 34), 751: (u' context/UID|nothin', 16, 33), 807: (u'kss_class', 17, 34), 848: (u' string:parent-fieldname-$fieldName-$ui', 18, 30), 967: (u'accessor', 20, 31), 385: (u'context/@@kss_field_decorator_view', 11, 39), 458: (u' nocall:kssClassesView/getKssClassesInlineEditabl', 12, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047006992 = u'edit'
_static_140168047768720 = u'edit'
_static_140168046859536 = {u'class': u'kss_class', u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168016766672 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168037620432 = {u'name': u'', u'placeholder': u'widget/placeholder|nothing', u'value': u'', u'class': u'blurrable firstToFocus', u'maxlength': u'widget/maxlength', u'type': u'text', u'id': u'', u'size': u'30', }
_static_140168257770128 = {}

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046862288
            __attrs_140168046862288 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026305488
            __attrs_140168026305488 = _static_140168257770128
            __backup_macroname_140168067743248 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6ab23490> name=None at 7f7b6ab238d0> -> __value
            __value = _static_140168047768720
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b6a175ad0> name=None at 7f7b6a175b90> -> __attrs_140168047007184
                __attrs_140168047007184 = _static_140168037620432

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026386128
                __default_140168026386128 = _DEFAULT_MARKER

                # <Substitution u'fieldName' (33:36)> -> __attr_name
                __token = 1396
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))
                __append(u' class="blurrable firstToFocus"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026386320
                __default_140168026386320 = _DEFAULT_MARKER

                # <Substitution u'fieldName' (34:33)> -> __attr_id
                __token = 1440
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026384528
                __default_140168026384528 = _DEFAULT_MARKER

                # <Substitution u'value' (35:35)> -> __attr_value
                __token = 1487
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026385616
                __default_140168026385616 = _DEFAULT_MARKER

                # <Substitution u'widget/size' (36:33)> -> __attr_size
                __token = 1529
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_size = _static_140168208991440('path', u'widget/size', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_size = __quote(__attr_size, '"', '&quot;', u'30', _DEFAULT_MARKER)
                if (__attr_size is not None):
                    __append((u' size="%s"' % __attr_size))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026383120
                __default_140168026383120 = _DEFAULT_MARKER

                # <Substitution u'widget/placeholder|nothing' (37:39)> -> __attr_placeholder
                __token = 1584
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_placeholder = _static_140168208991440('path', u'widget/placeholder|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_placeholder is not None):
                    __append((u' placeholder="%s"' % __attr_placeholder))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047005776
                __default_140168047005776 = _DEFAULT_MARKER

                # <Substitution u'widget/maxlength' (38:36)> -> __attr_maxlength
                __token = 1652
                try:
                    __zt_tmp = __attrs_140168047007184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_maxlength = _static_140168208991440('path', u'widget/maxlength', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_maxlength is not None):
                    __append((u' maxlength="%s"' % __attr_maxlength))
                __append(u' />')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (25:28)> -> __macro
            __token = 1099
            try:
                __zt_tmp = __attrs_140168026305488
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1099
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168067743248 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168067743248
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026306960
            __attrs_140168026306960 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047009360
            __attrs_140168047009360 = _static_140168257770128
            __backup_macroname_140168056022672 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa69510> name=None at 7f7b6aa698d0> -> __value
            __value = _static_140168047006992
            econtext['macroname'] = __value

            # <Value u'context/widgets/string/macros/edit' (44:28)> -> __macro
            __token = 1800
            try:
                __zt_tmp = __attrs_140168047009360
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1800
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168056022672 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168056022672
            __append(u'\n    </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_string_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b6aa45510> name=None at 7f7b6aa45e10> -> __attrs_140168046860304
            __attrs_140168046860304 = _static_140168046859536
            __backup_kss_class_140168046981392 = get('kss_class', __marker)

            # <Value u"python:getKssClasses(fieldName,\n                              templateId='widgets/string', macro='string-field-view')" (14:34)> -> __value
            __token = 599
            try:
                __zt_tmp = __attrs_140168046860304
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u"getKssClasses(fieldName,\n                              templateId='widgets/string', macro='string-field-view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kss_class'] = __value
            __backup_uid_140168066376592 = get('uid', __marker)

            # <Value u'context/UID|nothing' (16:33)> -> __value
            __token = 751
            try:
                __zt_tmp = __attrs_140168046860304
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046859856
            __default_140168046859856 = _DEFAULT_MARKER

            # <Substitution u'kss_class' (17:34)> -> __attr_class
            __token = 807
            try:
                __zt_tmp = __attrs_140168046860304
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('path', u'kss_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046858576
            __default_140168046858576 = _DEFAULT_MARKER

            # <Substitution u'string:parent-fieldname-$fieldName-$uid' (18:30)> -> __attr_id
            __token = 848
            try:
                __zt_tmp = __attrs_140168046860304
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n            ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046904208
                __attrs_140168046904208 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046903760
                __default_140168046903760 = _DEFAULT_MARKER

                # <Value u'accessor' (20:31)> -> __cache_140168047307984
                __token = 967
                try:
                    __zt_tmp = __attrs_140168046904208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047307984 = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'accessor' (20:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa50750> -> __condition
                __expression = __cache_140168047307984

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>string</span>')
                else:
                    __content = __cache_140168047307984
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n        </span>')
            if (__backup_uid_140168066376592 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168066376592
            if (__backup_kss_class_140168046981392 is __marker):
                del econtext['kss_class']
            else:
                econtext['kss_class'] = __backup_kss_class_140168046981392
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046859920
            __attrs_140168046859920 = _static_140168257770128
            __backup_kssClassesView_140168026329808 = get('kssClassesView', __marker)

            # <Value u'context/@@kss_field_decorator_view' (11:39)> -> __value
            __token = 385
            try:
                __zt_tmp = __attrs_140168046859920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@kss_field_decorator_view', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['kssClassesView'] = __value
            __backup_getKssClasses_140168026383760 = get('getKssClasses', __marker)

            # <Value u'nocall:kssClassesView/getKssClassesInlineEditable' (12:37)> -> __value
            __token = 458
            try:
                __zt_tmp = __attrs_140168046859920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('nocall', u'kssClassesView/getKssClassesInlineEditable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['getKssClasses'] = __value
            __append(u'\n        ')
            __token = None
            render_string_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    ')
            if (__backup_getKssClasses_140168026383760 is __marker):
                del econtext['getKssClasses']
            else:
                econtext['getKssClasses'] = __backup_getKssClasses_140168026383760
            if (__backup_kssClassesView_140168026329808 is __marker):
                del econtext['kssClassesView']
            else:
                econtext['kssClassesView'] = __backup_kssClassesView_140168026329808
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

            # <Static value=<_ast.Dict object at 0x7f7b68d926d0> name=None at 7f7b68d920d0> -> __attrs_140168016767376
            __attrs_140168016767376 = _static_140168016766672
            __previous_i18n_domain_140168016766736 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016768656
            __attrs_140168016768656 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016768144
            __attrs_140168016768144 = _static_140168257770128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title></title></head>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016765968
            __attrs_140168016765968 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    <!-- String Widgets -->\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168016766736
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_string_field_view': render_string_field_view, u'render_view': render_view, 'render': render, }