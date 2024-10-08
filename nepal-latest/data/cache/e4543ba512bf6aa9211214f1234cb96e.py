# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/worksheet/views/../templates/print.pt'

__tokens = {36: (u'string:&lt;!DOCTYPE ht', 1, 36), 452: (u'context/@@plone_portal_state', 9, 31), 510: (u' portal_state/portal_ur', 10, 28), 563: (u'w context/@@plo', 11, 27), 604: (u'al portal_state/por', 12, 22), 304: (u'default_language|default', 6, 27), 360: (u' default_language|defaul', 7, 30), 671: (u'provider:plone.htmlhead', 14, 32), 3451: (u'python:view.getWSTemplates()', 121, 48), 3526: (u"python:template['id']", 122, 44), 3584: (u"python:template['title']", 123, 35), 4530: (u'python:view.getCSS()', 145, 54), 4631: (u'python:view.getWorksheets()', 147, 33), 4696: (u'python:ws.id', 148, 35), 4744: (u' python:ws.UID(', 149, 34), 4801: (u'python:view.renderWSTemplate()', 150, 38)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168047838608 = {u'type': u'button', u'id': u'cancel_button', u'value': u'Cancel', }
_static_140168037563024 = {u'for': u'template', }
_static_140168026276560 = {u'value': u'9', }
_static_140168026266896 = {u'id': u'worksheet-printview', }
_static_140168037524368 = {u'value': u'1', }
_static_140168037626448 = {u'id': u'numcols', u'name': u'numcols', }
_static_140168026362576 = {u'value': u'5', }
_static_140168037653328 = {u'lang': u'default_language|default', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'default_language|default', }
_static_140168026317456 = {u'uid': u'python:ws.UID()', u'class': u'worksheet', u'id': u'python:ws.id', }
_static_140168026264272 = {u'id': u'report-style', }
_static_140168037641104 = {u'id': u'worksheet-printview-options', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168069635984 = {u'selected': '', u'value': u'3', }
_static_140168047840272 = {u'id': u'buttons', }
_static_140168037496912 = {u'id': u'template', u'name': u'template', }
_static_140168026276496 = {u'value': u'8', }
_static_140168037590096 = {u'id': u'worksheet-printview-head', }
_static_140168037525712 = {u'value': u'2', }
_static_140168257770128 = {}
_static_140168026265360 = {u'type': u'button', u'id': u'print_button', u'value': u'Print', }
_static_140168208991440 = __compile_zt_expr
_static_140168026276304 = {u'value': u'6', }
_static_140168026279760 = {u'value': u'7', }
_static_140168037567312 = {u'for': u'numcols', }
_static_140168026362384 = {u'value': u'4', }
_static_140168047840592 = {u'value': u'10', }
_static_140168037629776 = {u'value': u"python:template['id']", }
_static_140168037589904 = {u'id': u'worksheet-printview-wrapper', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037652560
            __attrs_140168037652560 = _static_140168257770128

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037650704
            __default_140168037650704 = _DEFAULT_MARKER

            # <Value u'string:<!DOCTYPE html>' (1:36)> -> __cache_140168037653712
            __token = 36
            try:
                __zt_tmp = __attrs_140168037652560
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037653712 = _static_140168208991440('string', u'<!DOCTYPE html>', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'string:<!DOCTYPE html>' (1:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a17d4d0> -> __condition
            __expression = __cache_140168037653712

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037653712
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f7b6a17db50> name=None at 7f7b6a17d5d0> -> __attrs_140168037654416
            __attrs_140168037654416 = _static_140168037653328
            __backup_portal_state_140168046864144 = get('portal_state', __marker)

            # <Value u'context/@@plone_portal_state' (9:31)> -> __value
            __token = 452
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_portal_url_140168037444688 = get('portal_url', __marker)

            # <Value u'portal_state/portal_url' (10:28)> -> __value
            __token = 510
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'portal_state/portal_url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_plone_view_140168046864016 = get('plone_view', __marker)

            # <Value u'context/@@plone' (11:27)> -> __value
            __token = 563
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_portal_140168046863248 = get('portal', __marker)

            # <Value u'portal_state/portal' (12:22)> -> __value
            __token = 604
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __previous_i18n_domain_140168026349264 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037651024
            __default_140168037651024 = _DEFAULT_MARKER

            # <Substitution u'default_language|default' (6:27)> -> __attr_lang
            __token = 304
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140168208991440('path', u'default_language|default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037650768
            __default_140168037650768 = _DEFAULT_MARKER

            # <Substitution u'default_language|default' (7:30)> -> __attr_xml_lang
            __token = 360
            try:
                __zt_tmp = __attrs_140168037654416
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_xml_lang = _static_140168208991440('path', u'default_language|default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_xml_lang = __quote(__attr_xml_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_xml_lang is not None):
                __append((u' xml:lang="%s"' % __attr_xml_lang))
            __append(u'>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168307498960
            __attrs_140168307498960 = _static_140168257770128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037442960
            __attrs_140168037442960 = _static_140168257770128

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037445520
            __default_140168037445520 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead' (14:32)> -> __cache_140168037444240
            __token = 671
            try:
                __zt_tmp = __attrs_140168037442960
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037444240 = _static_140168208991440('provider', u'plone.htmlhead', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead' (14:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a14a690> -> __condition
            __expression = __cache_140168037444240

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140168037444240
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037443920
            __attrs_140168037443920 = _static_140168257770128

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u'<style>\n     html {\n       background-color:#cdcdcd;\n     }\n     html, body {\n       margin: 0;\n       padding: 0;\n     }\n     body {\n       width: 210mm;\n       padding: 10px 10px 0px 20px;\n       margin: 10px auto;\n       background-color:#fff;\n     }\n     #worksheet-printview-head {\n       margin:-10px -10px 60px -20px;\n       padding:10px 20px 20px 10px;\n       background-color: #dcdcdc;\n       border-bottom: 20px solid #CDCDCD;\n     }\n     #worksheet-printview-head #worksheet-printview-options label {\n       padding:5px 10px 5px 10px;\n     }\n     #worksheet-printview-head #buttons {\n       text-align:right;\n       padding-left:10px;\n       padding-top:10px;\n     }\n     #worksheet-printview-head #buttons input {\n       padding:4px 15px;\n       border:none;\n       color:#fff;\n       cursor:pointer;\n     }\n     #worksheet-printview-head #buttons input:hover {\n       opacity:0.8;\n       moz-opacity:0.8;\n       filter:alpha(opacity=80);\n       -webkit-transition: opacity 250ms ease-in-out;\n       -moz-transition: opacity 250ms ease-in-out;\n       -o-transition: opacity 250ms ease-in-out;\n       -ms-transition: opacity 250ms ease-in-out;\n       transition: opacity 250ms ease-in-out;\n     }\n     #worksheet-printview-head #buttons #print_button {\n       background-color:#0B486B;\n     }\n     #worksheet-printview-head #buttons #cancel_button {\n       background-color:#666;\n     }\n     .page-break {\n       background-color: #CDCDCD;\n       margin: 60px -10px 30px -20px;\n       padding-bottom: 20px;\n       padding-top: 20px;\n     }\n     .error-report {\n       margin:0 -20px;\n       padding:20px;\n       font-weight:bold;\n       color:#d40000;\n       border-bottom: 60px solid #CDCDCD;\n     }\n     .error-report pre {\n       font-family: monospace;\n       width:205mm;\n       overflow:auto;\n       background-color:#fff;\n       color:#000;\n       font-weight:normal;\n     }\n     @media print {\n       html {\n         background-color:#fff;\n       }\n       body {\n         font: serif;\n         font-size:10pt;\n         max-width:7.6in;\n         margin:0;\n       }\n       .page-break  {\n         display: block;\n         page-break-before: always;\n         margin:none;\n         border:none;\n       }\n       #worksheet-printview-head {\n         display:none;\n         visibility:hidden;\n       }\n       @page {\n         size: auto;\n         margin: 0.7in 0.1in 1in 0.1in;\n       }\n\n     }\n    </style>\n  </head>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037445072
            __attrs_140168037445072 = _static_140168257770128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6a16e390> name=None at 7f7b6a16ef90> -> __attrs_140168037591696
            __attrs_140168037591696 = _static_140168037589904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div id='worksheet-printview-wrapper'>\n      ")

            # <Static value=<_ast.Dict object at 0x7f7b6a16e450> name=None at 7f7b6a16ef50> -> __attrs_140168037638672
            __attrs_140168037638672 = _static_140168037590096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div id='worksheet-printview-head'>\n        ")

            # <Static value=<_ast.Dict object at 0x7f7b6a17ab90> name=None at 7f7b6a17a550> -> __attrs_140168037560528
            __attrs_140168037560528 = _static_140168037641104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div id='worksheet-printview-options'>\n          ")

            # <Static value=<_ast.Dict object at 0x7f7b6a167a90> name=None at 7f7b6a167690> -> __attrs_140168037494928
            __attrs_140168037494928 = _static_140168037563024

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="template">')
            __stream_140168037561360 = []
            __append_140168037561360 = __stream_140168037561360.append
            __append_140168037561360(u'Available templates')
            __msgid_140168037561360 = __re_whitespace(''.join(__stream_140168037561360)).strip()
            if __msgid_140168037561360:
                __append(translate(__msgid_140168037561360, mapping=None, default=__msgid_140168037561360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a157850> name=None at 7f7b6a157e10> -> __attrs_140168037497168
            __attrs_140168037497168 = _static_140168037496912

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select id="template" name ="template">\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037566544
            __attrs_140168037566544 = _static_140168257770128
            __backup_template_140168037640144 = get('template', __marker)

            # <Value u'python:view.getWSTemplates()' (121:48)> -> __iterator
            __token = 3451
            try:
                __zt_tmp = __attrs_140168037566544
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('python', u'view.getWSTemplates()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168037567056, ) = getitem('repeat')(u'template', __iterator)
            econtext['template'] = None
            for __item in __iterator:
                econtext['template'] = __item
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6a177f50> name=None at 7f7b6a177490> -> __attrs_140168037627088
                __attrs_140168037627088 = _static_140168037629776

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037627152
                __default_140168037627152 = _DEFAULT_MARKER

                # <Substitution u"python:template['id']" (122:44)> -> __attr_value
                __token = 3526
                try:
                    __zt_tmp = __attrs_140168037627088
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u"template['id']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037626128
                __default_140168037626128 = _DEFAULT_MARKER

                # <Value u"python:template['title']" (123:35)> -> __cache_140168037568144
                __token = 3584
                try:
                    __zt_tmp = __attrs_140168037627088
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037568144 = _static_140168208991440('python', u"template['title']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:template['title']" (123:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a177b90> -> __condition
                __expression = __cache_140168037568144

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168037568144
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</option>\n            ')
                ____index_140168037567056 -= 1
                if (____index_140168037567056 > 0):
                    __append('')
            if (__backup_template_140168037640144 is __marker):
                del econtext['template']
            else:
                econtext['template'] = __backup_template_140168037640144
            __append(u'\n          </select>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a168b50> name=None at 7f7b6a168890> -> __attrs_140168037626704
            __attrs_140168037626704 = _static_140168037567312

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="numcols">')
            __stream_140168037565456 = []
            __append_140168037565456 = __stream_140168037565456.append
            __append_140168037565456(u'Num columns')
            __msgid_140168037565456 = __re_whitespace(''.join(__stream_140168037565456)).strip()
            if __msgid_140168037565456:
                __append(translate(__msgid_140168037565456, mapping=None, default=__msgid_140168037565456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6a177250> name=None at 7f7b6a177a10> -> __attrs_140168037526864
            __attrs_140168037526864 = _static_140168037626448

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select id="numcols" name="numcols">\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b6a15e390> name=None at 7f7b6a15e490> -> __attrs_140168037523920
            __attrs_140168037523920 = _static_140168037524368

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="1">1</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b6a15e8d0> name=None at 7f7b6a15e210> -> __attrs_140168037524432
            __attrs_140168037524432 = _static_140168037525712

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="2">2</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b6bffdf90> name=None at 7f7b6a15e450> -> __attrs_140168026363984
            __attrs_140168026363984 = _static_140168069635984

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="3" selected>3</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696b9210> name=None at 7f7b696b9cd0> -> __attrs_140168026363728
            __attrs_140168026363728 = _static_140168026362384

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="4">4</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696b92d0> name=None at 7f7b696b9fd0> -> __attrs_140168026365648
            __attrs_140168026365648 = _static_140168026362576

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="5">5</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696a41d0> name=None at 7f7b696b9490> -> __attrs_140168026276944
            __attrs_140168026276944 = _static_140168026276304

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="6">6</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696a4f50> name=None at 7f7b696a4d50> -> __attrs_140168026278800
            __attrs_140168026278800 = _static_140168026279760

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="7">7</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696a4290> name=None at 7f7b696a4f90> -> __attrs_140168026278352
            __attrs_140168026278352 = _static_140168026276496

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="8">8</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b696a42d0> name=None at 7f7b696a4a50> -> __attrs_140168047838864
            __attrs_140168047838864 = _static_140168026276560

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="9">9</option>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab34d50> name=None at 7f7b6ab34b50> -> __attrs_140168047837904
            __attrs_140168047837904 = _static_140168047840592

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value="10">10</option>\n          </select>\n        </div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab34c10> name=None at 7f7b6a15e190> -> __attrs_140168047840528
            __attrs_140168047840528 = _static_140168047840272

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div id='buttons'>\n          ")

            # <Static value=<_ast.Dict object at 0x7f7b6ab34590> name=None at 7f7b6ab34710> -> __attrs_140168037644688
            __attrs_140168037644688 = _static_140168047838608

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="button" id=\'cancel_button\'')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037645840
            __default_140168037645840 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7f7b6a17b310> at 7f7b6a17b2d0> -> __attr_value
            __attr_value = u'Cancel'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b696a1710> name=None at 7f7b696a1fd0> -> __attrs_140168026267536
            __attrs_140168026267536 = _static_140168026265360

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="button" id=\'print_button\'')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026267088
            __default_140168026267088 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7f7b696a19d0> at 7f7b696a1850> -> __attr_value
            __attr_value = u'Print'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n        </div>\n      </div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b696a12d0> name=None at 7f7b696a1d50> -> __attrs_140168026265744
            __attrs_140168026265744 = _static_140168026264272

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u"<style id='report-style'>")

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026265296
            __default_140168026265296 = _DEFAULT_MARKER

            # <Value u'python:view.getCSS()' (145:54)> -> __cache_140168037641424
            __token = 4530
            try:
                __zt_tmp = __attrs_140168026265744
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037641424 = _static_140168208991440('python', u'view.getCSS()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.getCSS()' (145:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab34410> -> __condition
            __expression = __cache_140168037641424

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037641424
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</style>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b696a1d10> name=None at 7f7b696a1290> -> __attrs_140168037619344
            __attrs_140168037619344 = _static_140168026266896

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div id='worksheet-printview'>\n        ")

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037621200
            __attrs_140168037621200 = _static_140168257770128
            __backup_ws_140168026346832 = get('ws', __marker)

            # <Value u'python:view.getWorksheets()' (147:33)> -> __iterator
            __token = 4631
            try:
                __zt_tmp = __attrs_140168037621200
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('python', u'view.getWorksheets()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168037619728, ) = getitem('repeat')(u'ws', __iterator)
            econtext['ws'] = None
            for __item in __iterator:
                econtext['ws'] = __item
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b696ae290> name=None at 7f7b696ae210> -> __attrs_140168026318352
                __attrs_140168026318352 = _static_140168026317456

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="worksheet"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026317968
                __default_140168026317968 = _DEFAULT_MARKER

                # <Substitution u'python:ws.id' (148:35)> -> __attr_id
                __token = 4696
                try:
                    __zt_tmp = __attrs_140168026318352
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('python', u'ws.id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026320592
                __default_140168026320592 = _DEFAULT_MARKER

                # <Substitution u'python:ws.UID()' (149:34)> -> __attr_uid
                __token = 4744
                try:
                    __zt_tmp = __attrs_140168026318352
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_uid = _static_140168208991440('python', u'ws.UID()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_uid = __quote(__attr_uid, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_uid is not None):
                    __append((u' uid="%s"' % __attr_uid))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026318480
                __default_140168026318480 = _DEFAULT_MARKER

                # <Value u'python:view.renderWSTemplate()' (150:38)> -> __cache_140168037618320
                __token = 4801
                try:
                    __zt_tmp = __attrs_140168026318352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037618320 = _static_140168208991440('python', u'view.renderWSTemplate()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:view.renderWSTemplate()' (150:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696ae350> -> __condition
                __expression = __cache_140168037618320

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168037618320
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n        ')
                ____index_140168037619728 -= 1
                if (____index_140168037619728 > 0):
                    __append('')
            if (__backup_ws_140168026346832 is __marker):
                del econtext['ws']
            else:
                econtext['ws'] = __backup_ws_140168026346832
            __append(u'\n      </div>\n    </div>\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140168026349264
            if (__backup_portal_140168046863248 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168046863248
            if (__backup_plone_view_140168046864016 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140168046864016
            if (__backup_portal_url_140168037444688 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140168037444688
            if (__backup_portal_state_140168046864144 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140168046864144
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }