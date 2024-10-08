# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/custom_css.pt'

__tokens = {30: (u"python:options.get('report_options', {})", 1, 30), 106: (u" python:int(report_options.get('attachments_per_row', 2)", 2, 34), 198: (u'w python:attachments_per_row<1 and 1 or attachments_per_r', 3, 33), 282: (u'th options/page_width|noth', 4, 23), 336: (u'ght options/page_height|not', 5, 23), 393: (u'idth options/content_width|no', 6, 24), 453: (u'eight options/content_height|n', 7, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574122270544 = {u'type': u'text/css', }
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267399632
            __attrs_140574267399632 = _static_140574442558096
            __backup_report_options_140574123135312 = get('report_options', __marker)

            # <Value u"python:options.get('report_options', {})" (1:30)> -> __value
            __token = 30
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"options.get('report_options', {})", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['report_options'] = __value
            __backup_attachments_per_row_140574123135120 = get('attachments_per_row', __marker)

            # <Value u"python:int(report_options.get('attachments_per_row', 2))" (2:34)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"int(report_options.get('attachments_per_row', 2))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __backup_attachments_per_row_140574122308752 = get('attachments_per_row', __marker)

            # <Value u'python:attachments_per_row<1 and 1 or attachments_per_row' (3:33)> -> __value
            __token = 198
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'attachments_per_row<1 and 1 or attachments_per_row', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __backup_page_width_140574254002256 = get('page_width', __marker)

            # <Value u'options/page_width|nothing' (4:23)> -> __value
            __token = 282
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/page_width|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['page_width'] = __value
            __backup_page_height_140574123135632 = get('page_height', __marker)

            # <Value u'options/page_height|nothing' (5:23)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/page_height|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['page_height'] = __value
            __backup_content_width_140574122310800 = get('content_width', __marker)

            # <Value u'options/content_width|nothing' (6:24)> -> __value
            __token = 393
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/content_width|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['content_width'] = __value
            __backup_content_height_140574267398352 = get('content_height', __marker)

            # <Value u'options/content_height|nothing' (7:24)> -> __value
            __token = 453
            try:
                __zt_tmp = __attrs_140574267399632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/content_height|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['content_height'] = __value
            __previous_i18n_domain_140574123689872 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f5f50> name=None at 7fd9f69f5b10> -> __attrs_140574122269584
            __attrs_140574122269584 = _static_140574122270544

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u'<style type="text/css">\n\n    .logo {\n        width: 120px;\n    }\n\n    .red {\n        color: red;\n    }\n\n    .text-center {\n        text-align: center;\n    }\n    .flex {\n        display: flex;\n    }\n   \n    .align-item-center {\n        align-items: center;\n    }\n\n    .justify-content-center {\n        justify-content: center;\n    }\n\n    .justify-between {\n        justify-content: space-between;\n    }\n    .justify-around {\n        justify-content: space-around;\n    }\n\n    .flex-row {\n        flex-direction: row;\n    }\n\n    .flex-column {\n        flex-direction: column;\n    }\n    .gap-2 {\n        gap: 0.5rem;\n    }\n\n    .align-item-top {\n        align-items: top;\n    }\n\n    .align-item-botom {\n        align-items: bottom;\n    }\n    .justify-item-top {\n        justify-items: top;\n    }\n\n    .align-center {\n        align-items: center;\n    }\n    .align-right{\n      align-item: right;\n    }\n    p{\n      margin: 0;\n      padding:0;\n    }\n\n    .nepal-info tr td{\n        padding: 0 !important;\n    }\n    \n    \n    .border-buttom{\n      border-bottom: 1px solid red;\n      margin-bottom: 10px;\n    }\n\n    .border-r-0{\n        border-right: 0 !important;\n    }\n    .border-l-0{\n        border-left: 0 !important;\n    }\n\n    .border-0 tr td{\n        border: 0 !important;\n    }\n    .border-0{\n        border: 0 !important;\n    }\n\n    .border{\n        border: 2px solid black !important;\n    }\n   \n    </style>\n\n')
            __i18n_domain = __previous_i18n_domain_140574123689872
            if (__backup_content_height_140574267398352 is __marker):
                del econtext['content_height']
            else:
                econtext['content_height'] = __backup_content_height_140574267398352
            if (__backup_content_width_140574122310800 is __marker):
                del econtext['content_width']
            else:
                econtext['content_width'] = __backup_content_width_140574122310800
            if (__backup_page_height_140574123135632 is __marker):
                del econtext['page_height']
            else:
                econtext['page_height'] = __backup_page_height_140574123135632
            if (__backup_page_width_140574254002256 is __marker):
                del econtext['page_width']
            else:
                econtext['page_width'] = __backup_page_width_140574254002256
            if (__backup_attachments_per_row_140574122308752 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574122308752
            if (__backup_attachments_per_row_140574123135120 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574123135120
            if (__backup_report_options_140574123135312 is __marker):
                del econtext['report_options']
            else:
                econtext['report_options'] = __backup_report_options_140574123135312
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }