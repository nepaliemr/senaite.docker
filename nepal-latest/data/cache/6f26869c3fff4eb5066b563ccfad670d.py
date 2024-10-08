# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/skins/bika/bika_widgets/remarkswidget.pt'

__tokens = {3733: (u'context/widgets/remarkswidget/macros/remarks_edit', 82, 32), 3733: (u'context/widgets/remarkswidget/macros/remarks_edit', 82, 32), 3622: (u'context/widgets/field/macros/edit', 80, 26), 3622: (u'context/widgets/field/macros/edit', 80, 26), 2582: (u'python:field.get_history(context)', 56, 33), 2665: (u'record/id', 57, 47), 2730: (u'record/user_id', 58, 52), 2798: (u'record/user_id', 59, 51), 2871: (u'record/user_name', 60, 55), 2942: (u'record/created_ulocalized', 61, 51), 3064: (u'record/html_content', 64, 38), 3352: (u'context/bika_widgets/remarkswidget/macros/remarks_history', 73, 32), 3352: (u'context/bika_widgets/remarkswidget/macros/remarks_history', 73, 32), 3445: (u'context/bika_widgets/remarkswidget/macros/remarks_edit', 74, 32), 3445: (u'context/bika_widgets/remarkswidget/macros/remarks_edit', 74, 32), 3227: (u'field_macro | context/widgets/field/macros/edit', 71, 26), 3227: (u'field_macro | context/widgets/field/macros/edit', 71, 26), 1668: (u'string:${portal/absolute_url}/bika_widgets', 37, 36), 1784: (u'string:${static_path}/remarkswidget.js', 39, 34), 1932: (u'string:${static_path}/remarkswidget.css', 41, 33), 2049: (u'fieldName', 43, 56), 2062: (u' fieldNam', 43, 69), 2111: (u"python: 'portal_factory' not in context.absolute_url()", 44, 24), 361: (u'context/UID|nothing', 9, 26), 416: (u' context/@@plone_portal_stat', 10, 34), 474: (u'l portal_state/port', 11, 27), 524: (u'ry acces', 12, 27), 562: (u'history', 13, 25), 600: (u'string:parent-fieldname-$fieldName-$uid', 14, 29), 714: (u'string:${portal/absolute_url}/bika_widgets', 16, 38), 861: (u'string:${static_path}/remarkswidget.css', 18, 35), 995: (u'history', 21, 35), 1054: (u'record/id', 22, 49), 1121: (u'record/user_id', 23, 54), 1191: (u'record/user_id', 24, 53), 1266: (u'record/user_name', 25, 57), 1339: (u'record/created_ulocalized', 26, 53), 1466: (u'record/html_content', 29, 39)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140168069635920 = {u'class': u'record-date', }
_static_140168081258832 = {u'class': u'remarks_history', }
_static_140168046892560 = u'edit'
_static_140168081241552 = {u'class': u'record-header', }
_static_140168079754320 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140168062242192 = {u'src': u'string:${static_path}/remarkswidget.js', u'type': u'text/javascript', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168046851408 = u'remarks_history'
_static_140168081258704 = {u'media': u'all', u'href': u'', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140168046896016 = {u'class': u'record-username', }
_static_140168047239248 = {u'class': u'record-header', }
_static_140168068630096 = {u'id': u'fieldName', u'class': u'form-control', u'name': u'fieldName', }
_static_140168046897168 = {u'class': u'record-date', }
_static_140168046896272 = {u'class': u'record-content', }
_static_140168046850128 = u'edit'
_static_140168046851856 = u'remarks_edit'
_static_140168046850448 = u'remarks_edit'
_static_140168307496144 = {u'media': u'all', u'href': u'', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140168097134672 = {u'class': u'record-username', }
_static_140168257770128 = {}
_static_140168047242064 = {u'class': u'record-user', }
_static_140168089850896 = {u'class': u'record-user', }
_static_140168208991440 = __compile_zt_expr
_static_140168046892816 = {u'class': u'record', u'id': u'record/id', }
_static_140168082677648 = {u'class': u'remarks_history', u'id': u'string:parent-fieldname-$fieldName-$uid', }
_static_140168046894096 = {u'class': u'remarks_history', }
_static_140168082916240 = {u'class': u'record-content', }
_static_140168047301520 = {u'disabled': u'disabled', u'type': u'submit', u'class': u'saveRemarks allowMultiSubmit btn btn-primary btn-sm input-sm', u'value': u'Add remarks', }
_static_140168084386704 = {u'class': u'record', u'id': u'record/id', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046892176
            __attrs_140168046892176 = _static_140168257770128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046853840
            __attrs_140168046853840 = _static_140168257770128
            __backup_macroname_140168057710224 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa43050> name=None at 7f7b6aa437d0> -> __value
            __value = _static_140168046850128
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046851088
                __attrs_140168046851088 = _static_140168257770128
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046883152
                __attrs_140168046883152 = _static_140168257770128
                __backup_macroname_140168054319616 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa43190> name=None at 7f7b6aa4b810> -> __value
                __value = _static_140168046850448
                econtext['macroname'] = __value

                # <Value u'context/widgets/remarkswidget/macros/remarks_edit' (82:32)> -> __macro
                __token = 3733
                try:
                    __zt_tmp = __attrs_140168046883152
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/widgets/remarkswidget/macros/remarks_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 3733
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168054319616 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168054319616
                __append(u'\n      ')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'context/widgets/field/macros/edit' (80:26)> -> __macro
            __token = 3622
            try:
                __zt_tmp = __attrs_140168046853840
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 3622
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057710224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057710224
            __append(u'\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_remarks_history(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047304272
            __attrs_140168047304272 = _static_140168257770128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa4dc10> name=None at 7f7b6aa4d450> -> __attrs_140168046892432
            __attrs_140168046892432 = _static_140168046894096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="remarks_history">\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046892944
            __attrs_140168046892944 = _static_140168257770128
            __backup_record_140168081259216 = get('record', __marker)

            # <Value u'python:field.get_history(context)' (56:33)> -> __iterator
            __token = 2582
            try:
                __zt_tmp = __attrs_140168046892944
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('python', u'field.get_history(context)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168046891920, ) = getitem('repeat')(u'record', __iterator)
            econtext['record'] = None
            for __item in __iterator:
                econtext['record'] = __item
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa4d710> name=None at 7f7b6aa4de90> -> __attrs_140168046893968
                __attrs_140168046893968 = _static_140168046892816

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="record"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046891536
                __default_140168046891536 = _DEFAULT_MARKER

                # <Substitution u'record/id' (57:47)> -> __attr_id
                __token = 2665
                try:
                    __zt_tmp = __attrs_140168046893968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('path', u'record/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaa2050> name=None at 7f7b6aaa2150> -> __attrs_140168047242768
                __attrs_140168047242768 = _static_140168047239248

                # <Value u'record/user_id' (58:52)> -> __condition
                __token = 2730
                try:
                    __zt_tmp = __attrs_140168047242768
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'record/user_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="record-header">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aaa2b50> name=None at 7f7b6aaa2c50> -> __attrs_140168047240528
                    __attrs_140168047240528 = _static_140168047242064

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="record-user">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047241680
                    __default_140168047241680 = _DEFAULT_MARKER

                    # <Value u'record/user_id' (59:51)> -> __cache_140168047241104
                    __token = 2798
                    try:
                        __zt_tmp = __attrs_140168047240528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047241104 = _static_140168208991440('path', u'record/user_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'record/user_id' (59:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aaa2250> -> __condition
                    __expression = __cache_140168047241104

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168047241104
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa4e390> name=None at 7f7b6aa4ec10> -> __attrs_140168046895440
                    __attrs_140168046895440 = _static_140168046896016

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="record-username">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047240720
                    __default_140168047240720 = _DEFAULT_MARKER

                    # <Value u'record/user_name' (60:55)> -> __cache_140168047240784
                    __token = 2871
                    try:
                        __zt_tmp = __attrs_140168046895440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047240784 = _static_140168208991440('path', u'record/user_name', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'record/user_name' (60:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aaa2810> -> __condition
                    __expression = __cache_140168047240784

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168047240784
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa4e810> name=None at 7f7b6aa4e4d0> -> __attrs_140168046897680
                    __attrs_140168046897680 = _static_140168046897168

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="record-date">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046897616
                    __default_140168046897616 = _DEFAULT_MARKER

                    # <Value u'record/created_ulocalized' (61:51)> -> __cache_140168046898768
                    __token = 2942
                    try:
                        __zt_tmp = __attrs_140168046897680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168046898768 = _static_140168208991440('path', u'record/created_ulocalized', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'record/created_ulocalized' (61:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4e950> -> __condition
                    __expression = __cache_140168046898768

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168046898768
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n          </div>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa4e490> name=None at 7f7b6aa4e8d0> -> __attrs_140168046896464
                __attrs_140168046896464 = _static_140168046896272

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="record-content">')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046896592
                __default_140168046896592 = _DEFAULT_MARKER

                # <Value u'record/html_content' (64:38)> -> __cache_140168046896400
                __token = 3064
                try:
                    __zt_tmp = __attrs_140168046896464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046896400 = _static_140168208991440('path', u'record/html_content', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'record/html_content' (64:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4e890> -> __condition
                __expression = __cache_140168046896400

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168046896400
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n        </div>\n      ')
                ____index_140168046891920 -= 1
                if (____index_140168046891920 > 0):
                    __append('')
            if (__backup_record_140168081259216 is __marker):
                del econtext['record']
            else:
                econtext['record'] = __backup_record_140168081259216
            __append(u'\n    </div>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046894416
            __attrs_140168046894416 = _static_140168257770128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046896976
            __attrs_140168046896976 = _static_140168257770128
            __backup_macroname_140168054907680 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6aa4d610> name=None at 7f7b6aaa2950> -> __value
            __value = _static_140168046892560
            econtext['macroname'] = __value

            def __fill_widget_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046851664
                __attrs_140168046851664 = _static_140168257770128
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046853904
                __attrs_140168046853904 = _static_140168257770128
                __backup_macroname_140168054318256 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa43550> name=None at 7f7b6aa43850> -> __value
                __value = _static_140168046851408
                econtext['macroname'] = __value

                # <Value u'context/bika_widgets/remarkswidget/macros/remarks_history' (73:32)> -> __macro
                __token = 3352
                try:
                    __zt_tmp = __attrs_140168046853904
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/bika_widgets/remarkswidget/macros/remarks_history', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 3352
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168054318256 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168054318256
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046851152
                __attrs_140168046851152 = _static_140168257770128
                __backup_macroname_140168054317776 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aa43710> name=None at 7f7b6aa43990> -> __value
                __value = _static_140168046851856
                econtext['macroname'] = __value

                # <Value u'context/bika_widgets/remarkswidget/macros/remarks_edit' (74:32)> -> __macro
                __token = 3445
                try:
                    __zt_tmp = __attrs_140168046851152
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('path', u'context/bika_widgets/remarkswidget/macros/remarks_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 3445
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168054317776 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168054317776
                __append(u'\n      ')
            _slots = econtext[u'__slot_widget_body'] = _deque((__fill_widget_body, ))

            # <Value u'field_macro | context/widgets/field/macros/edit' (71:26)> -> __macro
            __token = 3227
            try:
                __zt_tmp = __attrs_140168046896976
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'field_macro | context/widgets/field/macros/edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 3227
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168054907680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168054907680
            __append(u'\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_remarks_edit(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168081257296
            __attrs_140168081257296 = _static_140168257770128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168082565392
            __attrs_140168082565392 = _static_140168257770128
            __backup_static_path_140168068765200 = get('static_path', __marker)

            # <Value u'string:${portal/absolute_url}/bika_widgets' (37:36)> -> __value
            __token = 1668
            try:
                __zt_tmp = __attrs_140168082565392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'${portal/absolute_url}/bika_widgets', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['static_path'] = __value
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6b8f0d90> name=None at 7f7b6b8f0f90> -> __attrs_140168307496272
            __attrs_140168307496272 = _static_140168062242192

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168318328912
            __default_140168318328912 = _DEFAULT_MARKER

            # <Substitution u'string:${static_path}/remarkswidget.js' (39:34)> -> __attr_src
            __token = 1784
            try:
                __zt_tmp = __attrs_140168307496272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140168208991440('string', u'${static_path}/remarkswidget.js', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b7a2d54d0> name=None at 7f7b7a2d5bd0> -> __attrs_140168038017488
            __attrs_140168038017488 = _static_140168307496144

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="stylesheet" type="text/css" media="all"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047083216
            __default_140168047083216 = _DEFAULT_MARKER

            # <Substitution u'string:${static_path}/remarkswidget.css' (41:33)> -> __attr_href
            __token = 1932
            try:
                __zt_tmp = __attrs_140168038017488
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('string', u'${static_path}/remarkswidget.css', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'/>\n    ')
            if (__backup_static_path_140168068765200 is __marker):
                del econtext['static_path']
            else:
                econtext['static_path'] = __backup_static_path_140168068765200
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6bf08650> name=None at 7f7b6a1d6510> -> __attrs_140168047285584
            __attrs_140168047285584 = _static_140168068630096

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append(u'<textarea class="form-control"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047285840
            __default_140168047285840 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (43:56)> -> __attr_name
            __token = 2049
            try:
                __zt_tmp = __attrs_140168047285584
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047288016
            __default_140168047288016 = _DEFAULT_MARKER

            # <Substitution u'fieldName' (43:69)> -> __attr_id
            __token = 2062
            try:
                __zt_tmp = __attrs_140168047285584
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140168208991440('path', u'fieldName', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'></textarea>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047285968
            __attrs_140168047285968 = _static_140168257770128

            # <Value u"python: 'portal_factory' not in context.absolute_url()" (44:24)> -> __condition
            __token = 2111
            try:
                __zt_tmp = __attrs_140168047285968
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u" 'portal_factory' not in context.absolute_url()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aab1390> name=None at 7f7b6aab15d0> -> __attrs_140168166252688
                __attrs_140168166252688 = _static_140168047301520
                __previous_i18n_domain_140168166255248 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="saveRemarks allowMultiSubmit btn btn-primary btn-sm input-sm" type="submit"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168166254672
                __default_140168166254672 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f7b71c22910> at 7f7b71c22410> -> __attr_value
                __attr_value = u'Add remarks'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u' disabled="disabled"/>')
                __i18n_domain = __previous_i18n_domain_140168166255248
                __append(u'\n    </div>')
            __append(u'\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_textarea_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f7b6cc6df90> name=None at 7f7b6cc6db10> -> __attrs_140168068354832
            __attrs_140168068354832 = _static_140168082677648
            __backup_uid_140168068331024 = get('uid', __marker)

            # <Value u'context/UID|nothing' (9:26)> -> __value
            __token = 361
            try:
                __zt_tmp = __attrs_140168068354832
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/UID|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['uid'] = __value
            __backup_portal_state_140168081532560 = get('portal_state', __marker)

            # <Value u'context/@@plone_portal_state' (10:34)> -> __value
            __token = 416
            try:
                __zt_tmp = __attrs_140168068354832
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_portal_140168081227472 = get('portal', __marker)

            # <Value u'portal_state/portal' (11:27)> -> __value
            __token = 474
            try:
                __zt_tmp = __attrs_140168068354832
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_history_140168082676176 = get('history', __marker)

            # <Value u'accessor' (12:27)> -> __value
            __token = 524
            try:
                __zt_tmp = __attrs_140168068354832
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'accessor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['history'] = __value

            # <Value u'history' (13:25)> -> __condition
            __token = 562
            try:
                __zt_tmp = __attrs_140168068354832
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'history', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="remarks_history"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168082675600
                __default_140168082675600 = _DEFAULT_MARKER

                # <Substitution u'string:parent-fieldname-$fieldName-$uid' (14:29)> -> __attr_id
                __token = 600
                try:
                    __zt_tmp = __attrs_140168068354832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('string', u'parent-fieldname-$fieldName-$uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168081260496
                __attrs_140168081260496 = _static_140168257770128
                __backup_static_path_140168068354576 = get('static_path', __marker)

                # <Value u'string:${portal/absolute_url}/bika_widgets' (16:38)> -> __value
                __token = 714
                try:
                    __zt_tmp = __attrs_140168081260496
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('string', u'${portal/absolute_url}/bika_widgets', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['static_path'] = __value
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6cb138d0> name=None at 7f7b6cb13b10> -> __attrs_140168068565968
                __attrs_140168068565968 = _static_140168081258704

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link rel="stylesheet" type="text/css" media="all"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168068788048
                __default_140168068788048 = _DEFAULT_MARKER

                # <Substitution u'string:${static_path}/remarkswidget.css' (18:35)> -> __attr_href
                __token = 861
                try:
                    __zt_tmp = __attrs_140168068565968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('string', u'${static_path}/remarkswidget.css', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'/>\n      ')
                if (__backup_static_path_140168068354576 is __marker):
                    del econtext['static_path']
                else:
                    econtext['static_path'] = __backup_static_path_140168068354576
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6cb13950> name=None at 7f7b6cb134d0> -> __attrs_140168160146192
                __attrs_140168160146192 = _static_140168081258832

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="remarks_history">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168068629264
                __attrs_140168068629264 = _static_140168257770128
                __backup_record_140168081258448 = get('record', __marker)

                # <Value u'history' (21:35)> -> __iterator
                __token = 995
                try:
                    __zt_tmp = __attrs_140168068629264
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'history', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168080726288, ) = getitem('repeat')(u'record', __iterator)
                econtext['record'] = None
                for __item in __iterator:
                    econtext['record'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ce0f390> name=None at 7f7b79008ad0> -> __attrs_140168084568464
                    __attrs_140168084568464 = _static_140168084386704

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="record"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168084569872
                    __default_140168084569872 = _DEFAULT_MARKER

                    # <Substitution u'record/id' (22:49)> -> __attr_id
                    __token = 1054
                    try:
                        __zt_tmp = __attrs_140168084568464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('path', u'record/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6cb0f5d0> name=None at 7f7b6cb0f290> -> __attrs_140168094339664
                    __attrs_140168094339664 = _static_140168081241552

                    # <Value u'record/user_id' (23:54)> -> __condition
                    __token = 1121
                    try:
                        __zt_tmp = __attrs_140168094339664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'record/user_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="record-header">\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b6d345410> name=None at 7f7b6d5a3bd0> -> __attrs_140168067364496
                        __attrs_140168067364496 = _static_140168089850896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="record-user">')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168092335184
                        __default_140168092335184 = _DEFAULT_MARKER

                        # <Value u'record/user_id' (24:53)> -> __cache_140168092335568
                        __token = 1191
                        try:
                            __zt_tmp = __attrs_140168067364496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168092335568 = _static_140168208991440('path', u'record/user_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'record/user_id' (24:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6d5a3d10> -> __condition
                        __expression = __cache_140168092335568

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168092335568
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b6da37850> name=None at 7f7b6da37250> -> __attrs_140168066338512
                        __attrs_140168066338512 = _static_140168097134672

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="record-username">')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168097133648
                        __default_140168097133648 = _DEFAULT_MARKER

                        # <Value u'record/user_name' (25:57)> -> __cache_140168162603600
                        __token = 1266
                        try:
                            __zt_tmp = __attrs_140168066338512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168162603600 = _static_140168208991440('path', u'record/user_name', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'record/user_name' (25:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6da37990> -> __condition
                        __expression = __cache_140168162603600

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168162603600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b6bffdf50> name=None at 7f7b6bffde90> -> __attrs_140168078818192
                        __attrs_140168078818192 = _static_140168069635920

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="record-date">')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168069633424
                        __default_140168069633424 = _DEFAULT_MARKER

                        # <Value u'record/created_ulocalized' (26:53)> -> __cache_140168066336272
                        __token = 1339
                        try:
                            __zt_tmp = __attrs_140168078818192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168066336272 = _static_140168208991440('path', u'record/created_ulocalized', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'record/created_ulocalized' (26:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6d15c110> -> __condition
                        __expression = __cache_140168066336272

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168066336272
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n            </div>')
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6cca8390> name=None at 7f7b6cca8a90> -> __attrs_140168066350288
                    __attrs_140168066350288 = _static_140168082916240

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="record-content">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168078677904
                    __default_140168078677904 = _DEFAULT_MARKER

                    # <Value u'record/html_content' (29:39)> -> __cache_140168081241424
                    __token = 1466
                    try:
                        __zt_tmp = __attrs_140168066350288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168081241424 = _static_140168208991440('path', u'record/html_content', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'record/html_content' (29:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6c8bf9d0> -> __condition
                    __expression = __cache_140168081241424

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168081241424
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n          </div>\n        ')
                    ____index_140168080726288 -= 1
                    if (____index_140168080726288 > 0):
                        __append('')
                if (__backup_record_140168081258448 is __marker):
                    del econtext['record']
                else:
                    econtext['record'] = __backup_record_140168081258448
                __append(u'\n      </div>\n    </span>')
            if (__backup_history_140168082676176 is __marker):
                del econtext['history']
            else:
                econtext['history'] = __backup_history_140168082676176
            if (__backup_portal_140168081227472 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168081227472
            if (__backup_portal_state_140168081532560 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140168081532560
            if (__backup_uid_140168068331024 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140168068331024
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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168068330704
            __attrs_140168068330704 = _static_140168257770128
            __append(u'\n    ')
            __token = None
            render_textarea_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n  ')
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

            # <Static value=<_ast.Dict object at 0x7f7b6c9a4450> name=None at 7f7b6c9a4310> -> __attrs_140168068332880
            __attrs_140168068332880 = _static_140168079754320
            __previous_i18n_domain_140168068332624 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n\n  ')
            __token = None
            render_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  ')
            __token = None
            render_remarks_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  ')
            __token = None
            render_remarks_history(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  ')
            __token = None
            render_edit(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  ')
            __token = None
            render_search(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140168068332624
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_search': render_search, u'render_remarks_history': render_remarks_history, u'render_edit': render_edit, u'render_remarks_edit': render_remarks_edit, u'render_textarea_field_view': render_textarea_field_view, u'render_view': render_view, 'render': render, }