# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/skins/senaite_templates/senaite_widgets/datetimewidget.pt'

__tokens = {860: (u'context/@@plone_portal_state/portal', 23, 33), 934: (u' string:${portal/absolute_url}/senaite_widget', 24, 37), 1085: (u'string:${static_path}/datetimewidget.css', 26, 35), 1781: (u'python:widget.attrs(context, field)', 39, 39), 2030: (u'   python:widget_at', 44, 17), 1877: (u'fieldName', 41, 27), 1912: (u' string:${fieldName}-dat', 42, 24), 1963: (u'e python:widget.get_date(value) if value else ', 43, 24), 2208: (u'python:widget.show_time', 49, 29), 2291: (u'fieldName', 51, 27), 2326: (u' string:${fieldName}-tim', 52, 24), 2377: (u'e python:widget.get_time(value) if value else ', 53, 24), 2608: (u'string:${fieldName}', 59, 23), 2652: (u" python:widget.to_local_date(value, context=context, request=request) if value else '", 60, 23), 1177: (u'field_macro | context/widgets/field/macros/edit', 28, 28), 1177: (u'field_macro | context/widgets/field/macros/edit', 28, 28), 722: (u'here/widgets/string/macros/edit', 19, 28), 722: (u'here/widgets/string/macros/edit', 19, 28), 263: (u'context/UID|nothing', 9, 28), 315: (u'string:parent-fieldname-$fieldName-$uid', 10, 31), 430: (u'accessor', 12, 32), 471: (u" python: widget.ulocalized_time(value, context=context, request=request) if value else '", 13, 31), 589: (u'value', 14, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168015691856 = u'edit'
_static_140168015663952 = set([])
_static_140168208992144 = __C2ZContextWrapper
_static_140168015745360 = {u'type': u'hidden', u'name': u'string:${fieldName}', u'value': u"python:widget.to_local_date(value, context=context, request=request) if value else ''", }
_static_140168016771792 = {u'value': u"python:widget.get_date(value) if value else ''", u'type': u'date', u'class': u'form-control form-control-sm', u'name': u'string:${fieldName}-date', u'target': u'fieldName', }
_static_140168016769936 = {u'class': u'text-left', }
_static_140168046860496 = u'edit'
_static_140168257770128 = {}
_static_140168046861328 = {u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168047354576 = {u'value': u"python:widget.get_time(value) if value else ''", u'type': u'time', u'class': u'form-control form-control-sm', u'name': u'string:${fieldName}-time', u'target': u'fieldName', }
_static_140168015694032 = {u'media': u'all', u'href': u'', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140168016772048 = {u'class': u'input-group flex-nowrap d-inline-flex w-auto datetimewidget', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036702992
            __attrs_140168036702992 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015692432
            __attrs_140168015692432 = _static_140168257770128
            __backup_portal_140168046846160 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (23:33)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_140168015692432
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_static_path_140168047355024 = get('static_path', __marker)

            # <Value u'string:${portal/absolute_url}/senaite_widgets' (24:37)> -> __value
            __token = 934
            try:
                __zt_tmp = __attrs_140168015692432
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${portal/absolute_url}/senaite_widgets', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['static_path'] = __value
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68c8c8d0> name=None at 7f7b68c8c310> -> __attrs_140168015694288
            __attrs_140168015694288 = _static_140168015694032

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="stylesheet" type="text/css" media="all"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015695376
            __default_140168015695376 = _DEFAULT_MARKER

            # <Substitution u'string:${static_path}/datetimewidget.css' (26:35)> -> __attr_href
            __token = 1085
            try:
                __zt_tmp = __attrs_140168015694288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('string', u'${static_path}/datetimewidget.css', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'/>\n      ')
            if (__backup_static_path_140168047355024 is __marker):
                del econtext['static_path']
            else:
                econtext['static_path'] = __backup_static_path_140168047355024
            if (__backup_portal_140168046846160 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168046846160
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015695440
            __attrs_140168015695440 = _static_140168257770128
            __backup_macroname_140168055864768 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b68c8c050> name=None at 7f7b68c8c510> -> __value
            __value = _static_140168015691856
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b68d93390> name=None at 7f7b68d93fd0> -> __attrs_140168016770576
                __attrs_140168016770576 = _static_140168016769936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="text-left">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b68d93bd0> name=None at 7f7b68d93cd0> -> __attrs_140168016771088
                __attrs_140168016771088 = _static_140168016772048

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group flex-nowrap d-inline-flex w-auto datetimewidget">\n            <!-- date -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b68d93ad0> name=None at 7f7b68d93190> -> __attrs_140168047355152
                __attrs_140168047355152 = _static_140168016771792
                __backup_widget_attrs_140168047342160 = get('widget_attrs', __marker)

                # <Value u'python:widget.attrs(context, field)' (39:39)> -> __value
                __token = 1781
                try:
                    __zt_tmp = __attrs_140168047355152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'widget.attrs(context, field)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['widget_attrs'] = __value

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input')

                # <Value u'python:widget_attrs' (44:17)> -> __cache_140168047354000
                __token = 2030
                try:
                    __zt_tmp = __attrs_140168047355152
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047354000 = _static_140168208991440('python', u'widget_attrs', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if (u'type' not in __chain(__cache_140168047354000)):
                    __append(u' type="date"')
                if (u'class' not in __chain(__cache_140168047354000)):
                    __append(u' class="form-control form-control-sm"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168082099152
                __default_140168082099152 = _DEFAULT_MARKER

                # <Substitution u'fieldName' (41:27)> -> __attr_target
                __token = 1877
                try:
                    __zt_tmp = __attrs_140168047355152
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_target = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                if ((__attr_target is not None) and (u'target' not in __chain(__cache_140168047354000))):
                    __append((u' target="%s"' % __attr_target))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047355216
                __default_140168047355216 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}-date' (42:24)> -> __attr_name
                __token = 1912
                try:
                    __zt_tmp = __attrs_140168047355152
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}-date', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if ((__attr_name is not None) and (u'name' not in __chain(__cache_140168047354000))):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047355280
                __default_140168047355280 = _DEFAULT_MARKER

                # <Substitution u"python:widget.get_date(value) if value else ''" (43:24)> -> __attr_value
                __token = 1963
                try:
                    __zt_tmp = __attrs_140168047355152
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u"widget.get_date(value) if value else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if ((__attr_value is not None) and (u'value' not in __chain(__cache_140168047354000))):
                    __append((u' value="%s"' % __attr_value))
                __attr_140168047357776 = __cache_140168047354000
                for (name, value, ) in __attr_140168047357776.items():
                    if ((name not in _static_140168015663952) and (value is not None)):
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(u'/>')
                if (__backup_widget_attrs_140168047342160 is __marker):
                    del econtext['widget_attrs']
                else:
                    econtext['widget_attrs'] = __backup_widget_attrs_140168047342160
                __append(u'\n            <!-- time -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6aabe2d0> name=None at 7f7b6aabe410> -> __attrs_140168015745744
                __attrs_140168015745744 = _static_140168047354576

                # <Value u'python:widget.show_time' (49:29)> -> __condition
                __token = 2208
                try:
                    __zt_tmp = __attrs_140168015745744
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'widget.show_time', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="time" class="form-control form-control-sm"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015748624
                    __default_140168015748624 = _DEFAULT_MARKER

                    # <Substitution u'fieldName' (51:27)> -> __attr_target
                    __token = 2291
                    try:
                        __zt_tmp = __attrs_140168015745744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((u' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015746832
                    __default_140168015746832 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}-time' (52:24)> -> __attr_name
                    __token = 2326
                    try:
                        __zt_tmp = __attrs_140168015745744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'${fieldName}-time', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015748304
                    __default_140168015748304 = _DEFAULT_MARKER

                    # <Substitution u"python:widget.get_time(value) if value else ''" (53:24)> -> __attr_value
                    __token = 2377
                    try:
                        __zt_tmp = __attrs_140168015745744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('python', u"widget.get_time(value) if value else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>')
                __append(u'\n          </div>\n          <!-- datetime value (outside to avoid style issues) -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b68c99150> name=None at 7f7b68c997d0> -> __attrs_140168015748176
                __attrs_140168015748176 = _static_140168015745360

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015746512
                __default_140168015746512 = _DEFAULT_MARKER

                # <Substitution u'string:${fieldName}' (59:23)> -> __attr_name
                __token = 2608
                try:
                    __zt_tmp = __attrs_140168015748176
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140168208991440('string', u'${fieldName}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015747792
                __default_140168015747792 = _DEFAULT_MARKER

                # <Substitution u"python:widget.to_local_date(value, context=context, request=request) if value else ''" (60:23)> -> __attr_value
                __token = 2652
                try:
                    __zt_tmp = __attrs_140168015748176
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u"widget.to_local_date(value, context=context, request=request) if value else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n        </div>')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (28:28)> -> __macro
            __token = 1177
            try:
                __zt_tmp = __attrs_140168015695440
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 1177
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168055864768 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168055864768
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046860560
            __attrs_140168046860560 = _static_140168257770128
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015694672
            __attrs_140168015694672 = _static_140168257770128
            __backup_macroname_140168054961168 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa458d0> name=None at 7f7b6a140790> -> __value
            __value = _static_140168046860496
            econtext['macroname'] = __value

            # <Value u'here/widgets/string/macros/edit' (19:28)> -> __macro
            __token = 722
            try:
                __zt_tmp = __attrs_140168015694672
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/widgets/string/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 722
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168054961168 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168054961168
            __append(u'\n    ')
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

            # <Static value=<_ast.Dict object at 0x7f7b6aa45c10> name=None at 7f7b6aa455d0> -> __attrs_140168046858896
            __attrs_140168046858896 = _static_140168046861328
            __backup_uid_140168047341712 = get('uid', __marker)

            # <Value u'context/UID|nothing' (9:28)> -> __value
            __token = 263
            try:
                __zt_tmp = __attrs_140168046858896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046859984
            __default_140168046859984 = _DEFAULT_MARKER

            # <Substitution u'string:parent-fieldname-$fieldName-$uid' (10:31)> -> __attr_id
            __token = 315
            try:
                __zt_tmp = __attrs_140168046858896
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n        ')
            if (__slot_inside is None):

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046861136
                __attrs_140168046861136 = _static_140168257770128
                __backup_value_140168047361488 = get('value', __marker)

                # <Value u'accessor' (12:32)> -> __value
                __token = 430
                try:
                    __zt_tmp = __attrs_140168046861136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value
                __backup_value_140168047307600 = get('value', __marker)

                # <Value u"python: widget.ulocalized_time(value, context=context, request=request) if value else ''" (13:31)> -> __value
                __token = 471
                try:
                    __zt_tmp = __attrs_140168046861136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" widget.ulocalized_time(value, context=context, request=request) if value else ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['value'] = __value

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046861776
                __default_140168046861776 = _DEFAULT_MARKER

                # <Value u'value' (14:27)> -> __cache_140168046860752
                __token = 589
                try:
                    __zt_tmp = __attrs_140168046861136
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046860752 = _static_140168208991440('path', u'value', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'value' (14:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa45650> -> __condition
                __expression = __cache_140168046860752

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>Date</span>')
                else:
                    __content = __cache_140168046860752
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_value_140168047307600 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168047307600
                if (__backup_value_140168047361488 is __marker):
                    del econtext['value']
                else:
                    econtext['value'] = __backup_value_140168047361488
            else:
                __slot_inside(__stream, econtext.copy(), rcontext)
            __append(u'\n      </span>')
            if (__backup_uid_140168047341712 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168047341712
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047172688
            __attrs_140168047172688 = _static_140168257770128
            __append(u'\n      ')
            __token = None
            render_string_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015665808
            __attrs_140168015665808 = _static_140168257770128
            __previous_i18n_domain_140168015666896 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015666832
            __attrs_140168015666832 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n    ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n    ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  </body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168015666896
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_edit': render_edit, u'render_search': render_search, u'render_string_field_view': render_string_field_view, u'render_view': render_view, 'render': render, }