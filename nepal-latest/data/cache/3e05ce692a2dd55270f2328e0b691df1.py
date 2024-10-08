# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/dexterity/templates/widget.pt'

__tokens = {90: (u'nocall:context', 3, 24), 129: (u" python:widget.mode == 'hidden", 4, 23), 183: (u'r widget/err', 5, 21), 225: (u"ss python:error and ' error' or", 6, 26), 287: (u"ues python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ", 7, 26), 383: (u"lass python: (widget.value in empty_values) and ' empty' ", 8, 24), 477: (u'lass  widget/wrapper_css_class|n', 9, 30), 543: (u'_class string:kssattr-fieldname-${widge', 10, 26), 619: (u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', 11, 27), 757: (u' widget/nam', 12, 35), 793: (u'd string:formfield-${widget/i', 13, 22), 952: (u'python: not hidden and widget.label', 18, 24), 917: (u'widget/id', 17, 29), 1031: (u'widget/label', 19, 41), 1139: (u"python:widget.required and widget.mode == 'input'", 22, 25), 1323: (u'error/render|nothing', 27, 30), 1449: (u"python: getattr(widget, 'description', widget.field.description)", 32, 32), 1608: (u'python:description and not hidden', 35, 23), 1572: (u'description', 34, 31), 1808: (u'python:view.get_prepend_text()', 42, 26), 1867: (u' python:view.get_append_text(', 43, 27), 1921: (u'python:view.is_input_mode()', 44, 22), 1975: (u'python:prefix', 45, 24), 2079: (u'python:prefix', 46, 60), 2164: (u'widget/render', 49, 34), 2244: (u'python:appendix', 51, 24), 2349: (u'python:appendix', 52, 60), 2443: (u'python:view.get_prepend_text()', 57, 26), 2502: (u' python:view.get_append_text(', 58, 27), 2556: (u'python:view.is_view_mode()', 59, 22), 2644: (u'python:prefix', 61, 33), 2745: (u'widget/render', 63, 34), 2862: (u'python:appendix', 66, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240906756368 = {u'class': u'input-group-prepend', }
_static_140240897199888 = {u'class': u'formHelp text-secondary text-muted', }
_static_140240906780112 = {u'class': u'field-prefix', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906829200 = {u'type': u'text', }
_static_140240906760080 = {u'class': u'input-group-text', }
_static_140241133802128 = {}
_static_140240917095056 = {u'data-fieldname': u'widget/name', u'class': u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', u'id': u'string:formfield-${widget/id}', }
_static_140240897196112 = {u'class': u'fieldErrorBox', }
_static_140240906828176 = {u'class': u'field-prefix', }
_static_140240906753552 = {u'class': u'horizontal font-weight-bold', u'for': u'', }
_static_140240906820368 = {u'class': u'input-group-text', }
_static_140240906769360 = {u'class': u'required horizontal', u'title': u'Required', }
_static_140240906757584 = {u'type': u'text', }
_static_140240897198288 = {u'style': u'width:auto', u'class': u'input-group input-group-sm d-flex', }
_static_140240906818704 = {u'class': u'input-group-append', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext[u'__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8c620be290> name=None at 7f8c620be1d0> -> __attrs_140240906752656
            __attrs_140240906752656 = _static_140240917095056
            __backup_widget_140240916730064 = get('widget', __marker)

            # <Value u'nocall:context' (3:24)> -> __value
            __token = 90
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('nocall', u'context', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_hidden_140240916715280 = get('hidden', __marker)

            # <Value u"python:widget.mode == 'hidden'" (4:23)> -> __value
            __token = 129
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"widget.mode == 'hidden'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['hidden'] = __value
            __backup_error_140240917100560 = get('error', __marker)

            # <Value u'widget/error' (5:21)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'widget/error', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_140240917101776 = get('error_class', __marker)

            # <Value u"python:error and ' error' or ''" (6:26)> -> __value
            __token = 225
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"error and ' error' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_140240916649936 = get('empty_values', __marker)

            # <Value u"python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (7:26)> -> __value
            __token = 287
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u" (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_140240917361488 = get('empty_class', __marker)

            # <Value u"python: (widget.value in empty_values) and ' empty' or ''" (8:24)> -> __value
            __token = 383
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u" (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __backup_wrapper_css_class_140240907729488 = get('wrapper_css_class', __marker)

            # <Value u'widget/wrapper_css_class|nothing' (9:30)> -> __value
            __token = 477
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'widget/wrapper_css_class|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['wrapper_css_class'] = __value
            __backup_fieldname_class_140240916648656 = get('fieldname_class', __marker)

            # <Value u'string:kssattr-fieldname-${widget/name}' (10:26)> -> __value
            __token = 543
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('string', u'kssattr-fieldname-${widget/name}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['fieldname_class'] = __value
            __previous_i18n_domain_140240906754384 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906752592
            __default_140240906752592 = _DEFAULT_MARKER

            # <Substitution u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}' (11:27)> -> __attr_class
            __token = 619
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('string', u'field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906755664
            __default_140240906755664 = _DEFAULT_MARKER

            # <Substitution u'widget/name' (12:35)> -> __attr_data_fieldname
            __token = 757
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140241087907024('path', u'widget/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_fieldname is not None):
                __append((u' data-fieldname="%s"' % __attr_data_fieldname))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906752144
            __default_140240906752144 = _DEFAULT_MARKER

            # <Substitution u'string:formfield-${widget/id}' (13:22)> -> __attr_id
            __token = 793
            try:
                __zt_tmp = __attrs_140240906752656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('string', u'formfield-${widget/id}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c616e1610> name=None at 7f8c616e15d0> -> __attrs_140240906772240
            __attrs_140240906772240 = _static_140240906753552

            # <Value u'python: not hidden and widget.label' (18:24)> -> __condition
            __token = 952
            try:
                __zt_tmp = __attrs_140240906772240
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' not hidden and widget.label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906752912
                __default_140240906752912 = _DEFAULT_MARKER

                # <Substitution u'widget/id' (17:29)> -> __attr_for
                __token = 917
                try:
                    __zt_tmp = __attrs_140240906772240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140241087907024('path', u'widget/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u' class="horizontal font-weight-bold">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906770576
                __attrs_140240906770576 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906770256
                __default_140240906770256 = _DEFAULT_MARKER

                # <Value u'widget/label' (19:41)> -> __cache_140240906770512
                __token = 1031
                try:
                    __zt_tmp = __attrs_140240906770576
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906770512 = _static_140241087907024('path', u'widget/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/label' (19:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e5810> -> __condition
                __expression = __cache_140240906770512

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>label</span>')
                else:
                    __content = __cache_140240906770512
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c616e53d0> name=None at 7f8c616e5410> -> __attrs_140240906770960
                __attrs_140240906770960 = _static_140240906769360

                # <Value u"python:widget.required and widget.mode == 'input'" (22:25)> -> __condition
                __token = 1139
                try:
                    __zt_tmp = __attrs_140240906770960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u"widget.required and widget.mode == 'input'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="required horizontal"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906771984
                    __default_140240906771984 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f8c616e5050> at 7f8c616e5090> -> __attr_title
                    __attr_title = u'Required'
                    __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>&nbsp;</span>')
                __append(u'\n  </div>')
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc4050> name=None at 7f8c616e5f50> -> __attrs_140240897197008
            __attrs_140240897197008 = _static_140240897196112

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="fieldErrorBox">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906771856
            __default_140240906771856 = _DEFAULT_MARKER

            # <Value u'error/render|nothing' (27:30)> -> __cache_140240906769488
            __token = 1323
            try:
                __zt_tmp = __attrs_140240897197008
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240906769488 = _static_140241087907024('path', u'error/render|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'error/render|nothing' (27:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e5d50> -> __condition
            __expression = __cache_140240906769488

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n    Error\n  ')
            else:
                __content = __cache_140240906769488
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc4f10> name=None at 7f8c60dc4ed0> -> __attrs_140240897199056
            __attrs_140240897199056 = _static_140240897199888
            __backup_description_140240906694416 = get('description', __marker)

            # <Value u"python: getattr(widget, 'description', widget.field.description)" (32:32)> -> __value
            __token = 1449
            try:
                __zt_tmp = __attrs_140240897199056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u" getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value u'python:description and not hidden' (35:23)> -> __condition
            __token = 1608
            try:
                __zt_tmp = __attrs_140240897199056
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'description and not hidden', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="formHelp text-secondary text-muted">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897199632
                __default_140240897199632 = _DEFAULT_MARKER

                # <Value u'description' (34:31)> -> __cache_140240897198352
                __token = 1572
                try:
                    __zt_tmp = __attrs_140240897199056
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240897198352 = _static_140241087907024('path', u'description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'description' (34:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60dc4c50> -> __condition
                __expression = __cache_140240897198352

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n    field description\n  ')
                else:
                    __content = __cache_140240897198352
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>')
            if (__backup_description_140240906694416 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140240906694416
            __append(u'\n\n  <!-- widget insert mode -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc48d0> name=None at 7f8c60dc4890> -> __attrs_140240906758800
            __attrs_140240906758800 = _static_140240897198288
            __backup_prefix_140240917099920 = get('prefix', __marker)

            # <Value u'python:view.get_prepend_text()' (42:26)> -> __value
            __token = 1808
            try:
                __zt_tmp = __attrs_140240906758800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.get_prepend_text()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['prefix'] = __value
            __backup_appendix_140240916649232 = get('appendix', __marker)

            # <Value u'python:view.get_append_text()' (43:27)> -> __value
            __token = 1867
            try:
                __zt_tmp = __attrs_140240906758800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.get_append_text()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['appendix'] = __value

            # <Value u'python:view.is_input_mode()' (44:22)> -> __condition
            __token = 1921
            try:
                __zt_tmp = __attrs_140240906758800
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'view.is_input_mode()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm d-flex" style="width:auto">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c616e2110> name=None at 7f8c616e20d0> -> __attrs_140240906757008
                __attrs_140240906757008 = _static_140240906756368

                # <Value u'python:prefix' (45:24)> -> __condition
                __token = 1975
                try:
                    __zt_tmp = __attrs_140240906757008
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend">\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8c616e2f90> name=None at 7f8c616e2590> -> __attrs_140240906759632
                    __attrs_140240906759632 = _static_140240906760080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-text">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906760144
                    __default_140240906760144 = _DEFAULT_MARKER

                    # <Value u'python:prefix' (46:60)> -> __cache_140240906759248
                    __token = 2079
                    try:
                        __zt_tmp = __attrs_140240906759632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906759248 = _static_140241087907024('python', u'prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:prefix' (46:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e28d0> -> __condition
                    __expression = __cache_140240906759248

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240906759248
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n    </div>')
                __append(u'\n    ')
                if (__slot_widget is None):

                    # <Static value=<_ast.Dict object at 0x7f8c616e25d0> name=None at 7f8c616e27d0> -> __attrs_140240906817616
                    __attrs_140240906817616 = _static_140240906757584

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906818256
                    __default_140240906818256 = _DEFAULT_MARKER

                    # <Value u'widget/render' (49:34)> -> __cache_140240906820112
                    __token = 2164
                    try:
                        __zt_tmp = __attrs_140240906817616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906820112 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/render' (49:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616f10d0> -> __condition
                    __expression = __cache_140240906820112

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="text" />')
                    else:
                        __content = __cache_140240906820112
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_widget(__stream, econtext.copy(), rcontext)
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c616f1490> name=None at 7f8c616f1450> -> __attrs_140240906820816
                __attrs_140240906820816 = _static_140240906818704

                # <Value u'python:appendix' (51:24)> -> __condition
                __token = 2244
                try:
                    __zt_tmp = __attrs_140240906820816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'appendix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-append">\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8c616f1b10> name=None at 7f8c616f1690> -> __attrs_140240906820304
                    __attrs_140240906820304 = _static_140240906820368

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-text">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906819792
                    __default_140240906819792 = _DEFAULT_MARKER

                    # <Value u'python:appendix' (52:60)> -> __cache_140240906820560
                    __token = 2349
                    try:
                        __zt_tmp = __attrs_140240906820304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906820560 = _static_140241087907024('python', u'appendix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:appendix' (52:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616f1fd0> -> __condition
                    __expression = __cache_140240906820560

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240906820560
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n    </div>')
                __append(u'\n  </div>')
            if (__backup_appendix_140240916649232 is __marker):
                del econtext['appendix']
            else:
                econtext['appendix'] = __backup_appendix_140240916649232
            if (__backup_prefix_140240917099920 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_140240917099920
            __append(u'\n\n  <!-- widget view mode -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906826192
            __attrs_140240906826192 = _static_140241133802128
            __backup_prefix_140240916641552 = get('prefix', __marker)

            # <Value u'python:view.get_prepend_text()' (57:26)> -> __value
            __token = 2443
            try:
                __zt_tmp = __attrs_140240906826192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.get_prepend_text()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['prefix'] = __value
            __backup_appendix_140240917096400 = get('appendix', __marker)

            # <Value u'python:view.get_append_text()' (58:27)> -> __value
            __token = 2502
            try:
                __zt_tmp = __attrs_140240906826192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.get_append_text()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['appendix'] = __value

            # <Value u'python:view.is_view_mode()' (59:22)> -> __condition
            __token = 2556
            try:
                __zt_tmp = __attrs_140240906826192
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'view.is_view_mode()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n    <!-- field prefix -->\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c616f3990> name=None at 7f8c616f3910> -> __attrs_140240906828624
                __attrs_140240906828624 = _static_140240906828176

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="field-prefix">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906827024
                __default_140240906827024 = _DEFAULT_MARKER

                # <Value u'python:prefix' (61:33)> -> __cache_140240906827856
                __token = 2644
                try:
                    __zt_tmp = __attrs_140240906828624
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906827856 = _static_140241087907024('python', u'prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:prefix' (61:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616f3710> -> __condition
                __expression = __cache_140240906827856

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240906827856
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n    ')
                if (__slot_widget is None):

                    # <Static value=<_ast.Dict object at 0x7f8c616f3d90> name=None at 7f8c616f35d0> -> __attrs_140240906778000
                    __attrs_140240906778000 = _static_140240906829200

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906827152
                    __default_140240906827152 = _DEFAULT_MARKER

                    # <Value u'widget/render' (63:34)> -> __cache_140240906827344
                    __token = 2745
                    try:
                        __zt_tmp = __attrs_140240906778000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906827344 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/render' (63:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616f3e10> -> __condition
                    __expression = __cache_140240906827344

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="text" />')
                    else:
                        __content = __cache_140240906827344
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_widget(__stream, econtext.copy(), rcontext)
                __append(u'\n    <!-- field appendix -->\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c616e7dd0> name=None at 7f8c616e7d10> -> __attrs_140240906779664
                __attrs_140240906779664 = _static_140240906780112

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="field-prefix">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906777104
                __default_140240906777104 = _DEFAULT_MARKER

                # <Value u'python:appendix' (66:33)> -> __cache_140240906776912
                __token = 2862
                try:
                    __zt_tmp = __attrs_140240906779664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906776912 = _static_140241087907024('python', u'appendix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:appendix' (66:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616e70d0> -> __condition
                __expression = __cache_140240906776912

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240906776912
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n  </div>')
            if (__backup_appendix_140240917096400 is __marker):
                del econtext['appendix']
            else:
                econtext['appendix'] = __backup_appendix_140240917096400
            if (__backup_prefix_140240916641552 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_140240916641552
            __append(u'\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140240906754384
            if (__backup_fieldname_class_140240916648656 is __marker):
                del econtext['fieldname_class']
            else:
                econtext['fieldname_class'] = __backup_fieldname_class_140240916648656
            if (__backup_wrapper_css_class_140240907729488 is __marker):
                del econtext['wrapper_css_class']
            else:
                econtext['wrapper_css_class'] = __backup_wrapper_css_class_140240907729488
            if (__backup_empty_class_140240917361488 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_140240917361488
            if (__backup_empty_values_140240916649936 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_140240916649936
            if (__backup_error_class_140240917101776 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_140240917101776
            if (__backup_error_140240917100560 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_140240917100560
            if (__backup_hidden_140240916715280 is __marker):
                del econtext['hidden']
            else:
                econtext['hidden'] = __backup_hidden_140240916715280
            if (__backup_widget_140240916730064 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240916730064
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
            __token = None
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_wrapper': render_widget_wrapper, 'render': render, }