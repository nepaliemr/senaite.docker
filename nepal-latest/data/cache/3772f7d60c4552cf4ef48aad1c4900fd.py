# -*- coding: utf-8 -*-
__filename = u'/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/templates/reports/MultiDefaultWithoutSignature.pt'

__tokens = {65: (u'python:view.render_css(context, **options)', 4, 28), 170: (u'python:view.render_custom_css(context, **options)', 7, 28), 276: (u'python:view.render_info_nepal(context, **options)', 10, 28), 619: (u'python:view.render_results(context, **options)', 19, 28), 733: (u'python:view.render_interpretations(context, **options)', 22, 28), 962: (u'python:view.render_remarks(context, **options)', 28, 28), 1072: (u'python:view.render_attachments(context, **options)', 31, 28), 1185: (u'python:view.render_publisher(context, **options)', 34, 28), 1296: (u'python:view.render_discreeter(context, **options)', 37, 28), 1404: (u'python:view.render_footer_nepal(context, **options)', 40, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}

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
            __append(u' ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123137616
            __attrs_140574123137616 = _static_140574442558096
            __append(u'\n\n  <!-- REPORT CSS -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123138832
            __attrs_140574123138832 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123138704
            __default_140574123138704 = _DEFAULT_MARKER

            # <Value u'python:view.render_css(context, **options)' (4:28)> -> __cache_140574123138448
            __token = 65
            try:
                __zt_tmp = __attrs_140574123138832
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123138448 = _static_140574397981968('python', u'view.render_css(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_css(context, **options)' (4:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda004ab590> -> __condition
            __expression = __cache_140574123138448

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123138448
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- CUSTOM REPORT CSS -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123143824
            __attrs_140574123143824 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123143696
            __default_140574123143696 = _DEFAULT_MARKER

            # <Value u'python:view.render_custom_css(context, **options)' (7:28)> -> __cache_140574123143376
            __token = 170
            try:
                __zt_tmp = __attrs_140574123143824
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123143376 = _static_140574397981968('python', u'view.render_custom_css(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_custom_css(context, **options)' (7:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acb150> -> __condition
            __expression = __cache_140574123143376

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123143376
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT INFO -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123144656
            __attrs_140574123144656 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123144528
            __default_140574123144528 = _DEFAULT_MARKER

            # <Value u'python:view.render_info_nepal(context, **options)' (10:28)> -> __cache_140574123144208
            __token = 276
            try:
                __zt_tmp = __attrs_140574123144656
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123144208 = _static_140574397981968('python', u'view.render_info_nepal(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_info_nepal(context, **options)' (10:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acb490> -> __condition
            __expression = __cache_140574123144208

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123144208
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- PATIENT  INFO -->\n  <!-- <tal:t replace="structure python:view.render_patient_info(context, **options)" /> -->\n\n  <!-- REPORT SUMMARY -->\n  <!-- <tal:t replace="structure python:view.render_summary(context, **options)" /> -->\n\n  <!-- REPORT RESULTS -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123146000
            __attrs_140574123146000 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123145872
            __default_140574123145872 = _DEFAULT_MARKER

            # <Value u'python:view.render_results(context, **options)' (19:28)> -> __cache_140574123145552
            __token = 619
            try:
                __zt_tmp = __attrs_140574123146000
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123145552 = _static_140574397981968('python', u'view.render_results(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_results(context, **options)' (19:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acb9d0> -> __condition
            __expression = __cache_140574123145552

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123145552
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- RESULTS INTERPRETATION -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123146832
            __attrs_140574123146832 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123146704
            __default_140574123146704 = _DEFAULT_MARKER

            # <Value u'python:view.render_interpretations(context, **options)' (22:28)> -> __cache_140574123146384
            __token = 733
            try:
                __zt_tmp = __attrs_140574123146832
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123146384 = _static_140574397981968('python', u'view.render_interpretations(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_interpretations(context, **options)' (22:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acbd10> -> __condition
            __expression = __cache_140574123146384

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123146384
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT QR CODE -->\n  <!-- <tal:t replace="structure python:view.render_qr_code(context, **options)" /> -->\n\n  <!-- SAMPLE REMARKS -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123147984
            __attrs_140574123147984 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123147856
            __default_140574123147856 = _DEFAULT_MARKER

            # <Value u'python:view.render_remarks(context, **options)' (28:28)> -> __cache_140574123147536
            __token = 962
            try:
                __zt_tmp = __attrs_140574123147984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123147536 = _static_140574397981968('python', u'view.render_remarks(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_remarks(context, **options)' (28:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acc190> -> __condition
            __expression = __cache_140574123147536

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123147536
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT ATTACHMENTS -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123148816
            __attrs_140574123148816 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123148688
            __default_140574123148688 = _DEFAULT_MARKER

            # <Value u'python:view.render_attachments(context, **options)' (31:28)> -> __cache_140574123148368
            __token = 1072
            try:
                __zt_tmp = __attrs_140574123148816
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123148368 = _static_140574397981968('python', u'view.render_attachments(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_attachments(context, **options)' (31:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acc4d0> -> __condition
            __expression = __cache_140574123148368

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123148368
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT SIGNATURES -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123149648
            __attrs_140574123149648 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123149520
            __default_140574123149520 = _DEFAULT_MARKER

            # <Value u'python:view.render_publisher(context, **options)' (34:28)> -> __cache_140574123149200
            __token = 1185
            try:
                __zt_tmp = __attrs_140574123149648
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123149200 = _static_140574397981968('python', u'view.render_publisher(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_publisher(context, **options)' (34:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acc810> -> __condition
            __expression = __cache_140574123149200

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123149200
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT DISCREETER -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123150480
            __attrs_140574123150480 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123150352
            __default_140574123150352 = _DEFAULT_MARKER

            # <Value u'python:view.render_discreeter(context, **options)' (37:28)> -> __cache_140574123150032
            __token = 1296
            try:
                __zt_tmp = __attrs_140574123150480
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123150032 = _static_140574397981968('python', u'view.render_discreeter(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_discreeter(context, **options)' (37:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6accb50> -> __condition
            __expression = __cache_140574123150032

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123150032
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  <!-- REPORT FOOTER -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123151312
            __attrs_140574123151312 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123151184
            __default_140574123151184 = _DEFAULT_MARKER

            # <Value u'python:view.render_footer_nepal(context, **options)' (40:28)> -> __cache_140574123150864
            __token = 1404
            try:
                __zt_tmp = __attrs_140574123151312
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123150864 = _static_140574397981968('python', u'view.render_footer_nepal(context, **options)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.render_footer_nepal(context, **options)' (40:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acce90> -> __condition
            __expression = __cache_140574123150864

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123150864
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n\n\n\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }