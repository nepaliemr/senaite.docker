# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/css.pt'

__tokens = {30: (u"python:options.get('report_options', {})", 1, 30), 106: (u" python:int(report_options.get('attachments_per_row', 2)", 2, 34), 198: (u'w python:attachments_per_row<1 and 1 or attachments_per_r', 3, 33), 282: (u'th options/page_width|noth', 4, 23), 336: (u'ght options/page_height|not', 5, 23), 393: (u'idth options/content_width|no', 6, 24), 453: (u'eight options/content_height|n', 7, 24), 2082: (u'python:content_width and content_height', 50, 25), 2222: (u'python:float(content_width)', 52, 28), 2278: (u' python:float(content_height', 53, 27), 2149: (u'python:all([content_width, content_height])', 51, 25), 2437: (u"python:'{:.2f}mm'.format(cw / attachments_per_row)", 56, 32), 2525: (u"python:'{:.2f}mm'.format(ch * 0.75)", 57, 33), 2650: (u"python:'{:.2f}mm'.format(cw)", 60, 32), 2716: (u"python:'{:.2f}mm'.format(ch * 0.75)", 61, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574123165520 = {u'type': u'text/css', }
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255218576
            __attrs_140574255218576 = _static_140574442558096
            __backup_report_options_140574122823632 = get('report_options', __marker)

            # <Value u"python:options.get('report_options', {})" (1:30)> -> __value
            __token = 30
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"options.get('report_options', {})", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['report_options'] = __value
            __backup_attachments_per_row_140574122820944 = get('attachments_per_row', __marker)

            # <Value u"python:int(report_options.get('attachments_per_row', 2))" (2:34)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"int(report_options.get('attachments_per_row', 2))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __backup_attachments_per_row_140574123135568 = get('attachments_per_row', __marker)

            # <Value u'python:attachments_per_row<1 and 1 or attachments_per_row' (3:33)> -> __value
            __token = 198
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'attachments_per_row<1 and 1 or attachments_per_row', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __backup_page_width_140574122823376 = get('page_width', __marker)

            # <Value u'options/page_width|nothing' (4:23)> -> __value
            __token = 282
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/page_width|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['page_width'] = __value
            __backup_page_height_140574254002256 = get('page_height', __marker)

            # <Value u'options/page_height|nothing' (5:23)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/page_height|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['page_height'] = __value
            __backup_content_width_140574123135440 = get('content_width', __marker)

            # <Value u'options/content_width|nothing' (6:24)> -> __value
            __token = 393
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/content_width|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['content_width'] = __value
            __backup_content_height_140574123135632 = get('content_height', __marker)

            # <Value u'options/content_height|nothing' (7:24)> -> __value
            __token = 453
            try:
                __zt_tmp = __attrs_140574255218576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/content_height|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['content_height'] = __value
            __previous_i18n_domain_140574123163984 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad0750> name=None at 7fd9f6ad0810> -> __attrs_140574123166096
            __attrs_140574123166096 = _static_140574123165520

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u'<style type="text/css">\n   .report * { font: 9pt; }\n   .report h1 { font-size: 140%; }\n   .report h2 { font-size: 120%; }\n   .report h3 { font-size: 110%; }\n   .report .font-size-140 { font-size: 140%; }\n   .report .font-size-120 { font-size: 120%; }\n   .report .font-size-100 { font-size: 100%; }\n   .report .colon-after:after { content: ":"; }\n   .report address { margin: 0.5rem 0; }\n   .report table.noborder td, .report table.noborder th { border: none; }\n   .report table.nopadding td { padding: 0; }\n   .report table td.label { padding-right: 0.3rem; font-weight: bold; }\n   .report table { border-color: black; }\n   .report table td, .report table th { border: 1px solid black; }\n   .report table th { border-bottom: 1px solid black; }\n   .report table.range-table td { padding: 0 0.3rem 0 0; border: none; }\n   .report .section-header h1 { font-size: 175%; }\n   .report .section-header img.logo { height: 30px; margin: 20px 0; }\n   .report .barcode-hri { margin-top: -0.25em; font-size: 8pt; }\n   .report .section-results .methodtitle { font-size: 85%; }\n   .report .section-results .results_interims { font-size: 85%; }\n   .report .section-footer table td { border: none; }\n   .report .section-footer {\n     position: fixed;\n     left: -20mm;\n     bottom: -20mm;\n     margin-left: 20mm;\n     margin-top: 10mm;\n     height: 20mm;\n     width: 100%;\n     text-align: left;\n     font-size: 9pt;\n   }\n   .report .section-footer #footer-line {\n     width: 100%;\n     height: 2mm;\n     border-top: 1px solid black;\n   }\n\n   ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123164880
            __attrs_140574123164880 = _static_140574442558096

            # <Value u'python:content_width and content_height' (50:25)> -> __condition
            __token = 2082
            try:
                __zt_tmp = __attrs_140574123164880
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'content_width and content_height', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                pass
            __append(u'\n   ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123164304
            __attrs_140574123164304 = _static_140574442558096
            __backup_cw_140574123721360 = get('cw', __marker)

            # <Value u'python:float(content_width)' (52:28)> -> __value
            __token = 2222
            try:
                __zt_tmp = __attrs_140574123164304
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'float(content_width)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['cw'] = __value
            __backup_ch_140574123135312 = get('ch', __marker)

            # <Value u'python:float(content_height)' (53:27)> -> __value
            __token = 2278
            try:
                __zt_tmp = __attrs_140574123164304
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'float(content_height)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ch'] = __value

            # <Value u'python:all([content_width, content_height])' (51:25)> -> __condition
            __token = 2149
            try:
                __zt_tmp = __attrs_140574123164304
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'all([content_width, content_height])', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n   /* Ensure that the images stay within the borders */\n   .report .section-attachments img {\n     max-width: ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123155536
                __attrs_140574123155536 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123155728
                __default_140574123155728 = _DEFAULT_MARKER

                # <Value u"python:'{:.2f}mm'.format(cw / attachments_per_row)" (56:32)> -> __cache_140574123167184
                __token = 2437
                try:
                    __zt_tmp = __attrs_140574123155536
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123167184 = _static_140574397981968('python', u"'{:.2f}mm'.format(cw / attachments_per_row)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:'{:.2f}mm'.format(cw / attachments_per_row)" (56:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ad0f10> -> __condition
                __expression = __cache_140574123167184

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574123167184
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u';\n     max-height: ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123157712
                __attrs_140574123157712 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123157648
                __default_140574123157648 = _DEFAULT_MARKER

                # <Value u"python:'{:.2f}mm'.format(ch * 0.75)" (57:33)> -> __cache_140574123156560
                __token = 2525
                try:
                    __zt_tmp = __attrs_140574123157712
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123156560 = _static_140574397981968('python', u"'{:.2f}mm'.format(ch * 0.75)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:'{:.2f}mm'.format(ch * 0.75)" (57:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ace550> -> __condition
                __expression = __cache_140574123156560

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574123156560
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u';\n   }\n   .report .section-resultsinterpretation img {\n     max-width: ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123158352
                __attrs_140574123158352 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123157840
                __default_140574123157840 = _DEFAULT_MARKER

                # <Value u"python:'{:.2f}mm'.format(cw)" (60:32)> -> __cache_140574123157456
                __token = 2650
                try:
                    __zt_tmp = __attrs_140574123158352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123157456 = _static_140574397981968('python', u"'{:.2f}mm'.format(cw)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:'{:.2f}mm'.format(cw)" (60:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ace710> -> __condition
                __expression = __cache_140574123157456

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574123157456
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u';\n     max-height: ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123158288
                __attrs_140574123158288 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123159184
                __default_140574123159184 = _DEFAULT_MARKER

                # <Value u"python:'{:.2f}mm'.format(ch * 0.75)" (61:33)> -> __cache_140574123157584
                __token = 2716
                try:
                    __zt_tmp = __attrs_140574123158288
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123157584 = _static_140574397981968('python', u"'{:.2f}mm'.format(ch * 0.75)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:'{:.2f}mm'.format(ch * 0.75)" (61:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6aced10> -> __condition
                __expression = __cache_140574123157584

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574123157584
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u';\n   }\n   ')
            if (__backup_ch_140574123135312 is __marker):
                del econtext['ch']
            else:
                econtext['ch'] = __backup_ch_140574123135312
            if (__backup_cw_140574123721360 is __marker):
                del econtext['cw']
            else:
                econtext['cw'] = __backup_cw_140574123721360
            __append(u'\n   @page {\n     @bottom-right {\n       vertical-align: top;\n       margin-top: 2mm;\n       font-size: 9pt;\n       content: "')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123157776
            __attrs_140574123157776 = _static_140574442558096
            __stream_140574123167696 = []
            __append_140574123167696 = __stream_140574123167696.append
            __append_140574123167696(u'Page')
            __msgid_140574123167696 = __re_whitespace(''.join(__stream_140574123167696)).strip()
            if __msgid_140574123167696:
                __append(translate(__msgid_140574123167696, mapping=None, default=__msgid_140574123167696, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u' " counter(page) " ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123159440
            __attrs_140574123159440 = _static_140574442558096
            __stream_140574123158928 = []
            __append_140574123158928 = __stream_140574123158928.append
            __append_140574123158928(u'of')
            __msgid_140574123158928 = __re_whitespace(''.join(__stream_140574123158928)).strip()
            if __msgid_140574123158928:
                __append(translate(__msgid_140574123158928, mapping=None, default=__msgid_140574123158928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u' " counter(pages);\n     }\n   }\n  </style>\n\n')
            __i18n_domain = __previous_i18n_domain_140574123163984
            if (__backup_content_height_140574123135632 is __marker):
                del econtext['content_height']
            else:
                econtext['content_height'] = __backup_content_height_140574123135632
            if (__backup_content_width_140574123135440 is __marker):
                del econtext['content_width']
            else:
                econtext['content_width'] = __backup_content_width_140574123135440
            if (__backup_page_height_140574254002256 is __marker):
                del econtext['page_height']
            else:
                econtext['page_height'] = __backup_page_height_140574254002256
            if (__backup_page_width_140574122823376 is __marker):
                del econtext['page_width']
            else:
                econtext['page_width'] = __backup_page_width_140574122823376
            if (__backup_attachments_per_row_140574123135568 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574123135568
            if (__backup_attachments_per_row_140574122820944 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574122820944
            if (__backup_report_options_140574122823632 is __marker):
                del econtext['report_options']
            else:
                econtext['report_options'] = __backup_report_options_140574122823632
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }