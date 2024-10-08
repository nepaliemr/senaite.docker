# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/info_nepal.pt'

__tokens = {21: (u'python:view.model', 1, 21), 61: (u' model/Clien', 2, 21), 97: (u't model/Conta', 3, 21), 137: (u'ry python:view.laborat', 4, 23), 861: (u'string:++plone++senaite.core.static/images/nepal.png', 19, 60), 1253: (u'laboratory/Subtitle|nothing', 27, 45), 1399: (u'laboratory/Ministry|nothing', 30, 45), 1554: (u'laboratory/title|nothing', 33, 47), 2083: (u'model/getPatientFullName|nothing', 43, 45), 2334: (u'python:model.get_gender(model.Sex)', 48, 79), 2555: (u'model/Age/years|nothing', 52, 76), 2764: (u'model/PatientAddress|nothing', 56, 80), 2996: (u'model/MedicalRecordNumber/value|nothing', 60, 90), 3282: (u'python:view.to_localized_time(model.DateReceived)', 65, 43), 3620: (u'python:view.to_localized_time(view.timestamp)', 71, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574123138128 = {u'class': u'row section-info no-gutters', }
_static_140574123265744 = {u'class': u'laboratory-address', }
_static_140574123208528 = {u'class': u'client-city', }
_static_140574123138256 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140574123215056 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140574123231888 = {u'style': u'font-size: 14px;', }
_static_140574123211536 = {u'class': u'', }
_static_140574123262160 = {u'style': u'vertical-align: middle;', u'class': u'', }
_static_140574122266896 = {u'class': u'client-name', }
_static_140574397981968 = __compile_zt_expr
_static_140574123189392 = {u'class': u'client-age', }
_static_140574123209808 = {u'style': u'width: 50%', }
_static_140574123225296 = {u'class': u'mt-0', }
_static_140574123215696 = {u'style': u'margin-bottom:20px', u'class': u'lab-title', }
_static_140574123208592 = {u'style': u'font-size: 14px;', }
_static_140574442558096 = {}
_static_140574123148816 = {u'class': u'client-gender', }
_static_140574123164240 = {u'class': u'mt-0', }
_static_140574123189264 = {u'style': u'font-size: 14px;', }
_static_140574123164048 = {u'class': u'laboratory-address', }
_static_140574123228240 = {u'style': u'color: #333;', }
_static_140574123145168 = {u'style': u'background-color: rgba(255, 255, 255, 0.8); border-radius: 8px;', u'class': u'table nepal-info table-sm table-condensed noborder', }
_static_140574123181072 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140574123205520 = {u'style': u'font-size: 14px;', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574123227792 = {u'style': u'border-left: 2px solid #f0f0f0; vertical-align: middle;', u'class': u'', }
_static_140574123206032 = {u'class': u'contact-phone', }
_static_140574123232336 = {u'class': u'lab-title', }
_static_140574122231184 = {u'style': u'width: 10%', }
_static_140574123163792 = {u'class': u'red flex flex-column', }
_static_140574122326544 = {u'class': u'w-100', }
_static_140574123265424 = {u'style': u'vertical-align: middle;', u'class': u'', }
_static_140574122269328 = {u'style': u'padding-left:10px;', }
_static_140574123235152 = {u'src': u'string:++plone++senaite.core.static/images/nepal.png', u'class': u'logo', }
_static_140574123177104 = {u'class': u'laboratory-address', }
_static_140574123263376 = {u'class': u'client-name font-weight-bold', }
_static_140574122231056 = {u'style': u'width: 40%', }
_static_140574123210512 = {u'class': u'clearfix', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123199696
            __attrs_140574123199696 = _static_140574442558096
            __backup_model_140574123199056 = get('model', __marker)

            # <Value u'python:view.model' (1:21)> -> __value
            __token = 21
            try:
                __zt_tmp = __attrs_140574123199696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.model', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['model'] = __value
            __backup_client_140574123135312 = get('client', __marker)

            # <Value u'model/Client' (2:21)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140574123199696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'model/Client', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['client'] = __value
            __backup_contact_140574123200272 = get('contact', __marker)

            # <Value u'model/Contact' (3:21)> -> __value
            __token = 97
            try:
                __zt_tmp = __attrs_140574123199696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'model/Contact', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['contact'] = __value
            __backup_laboratory_140574123198992 = get('laboratory', __marker)

            # <Value u'python:view.laboratory' (4:23)> -> __value
            __token = 137
            try:
                __zt_tmp = __attrs_140574123199696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.laboratory', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['laboratory'] = __value
            __previous_i18n_domain_140574123762768 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ac9c50> name=None at 7fd9f6ac9c10> -> __attrs_140574123139024
            __attrs_140574123139024 = _static_140574123138128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row section-info no-gutters">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6a03a10> name=None at 7fd9f6a03d90> -> __attrs_140574122327632
            __attrs_140574122327632 = _static_140574122326544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="w-100">\n      <!-- Client Info -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6acb7d0> name=None at 7fd9f6b4e4d0> -> __attrs_140574122233424
            __attrs_140574122233424 = _static_140574123145168

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table nepal-info table-sm table-condensed noborder" style="background-color: rgba(255, 255, 255, 0.8); border-radius: 8px;">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122231504
            __attrs_140574122231504 = _static_140574442558096

            # <colgroup ... (0:0)
            # --------------------------------------------------------
            __append(u'<colgroup>\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9f69ec590> name=None at 7fd9f69ecf50> -> __attrs_140574122229904
            __attrs_140574122229904 = _static_140574122231184

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 10%">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9f69ec510> name=None at 7fd9f69ec250> -> __attrs_140574123305232
            __attrs_140574123305232 = _static_140574122231056

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 40%">\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adb450> name=None at 7fd9f6adbe50> -> __attrs_140574123212496
            __attrs_140574123212496 = _static_140574123209808

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 50%">\n              </colgroup>\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adbb10> name=None at 7fd9f6adbd90> -> __attrs_140574123211856
            __attrs_140574123211856 = _static_140574123211536

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr class="">\n                ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae8d90> name=None at 7fd9f6ae8990> -> __attrs_140574123264976
            __attrs_140574123264976 = _static_140574123265424

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae8ed0> name=None at 7fd9f6ae8f10> -> __attrs_140574123262416
            __attrs_140574123262416 = _static_140574123265744

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae8590> name=None at 7fd9f6ae8310> -> __attrs_140574123236304
            __attrs_140574123236304 = _static_140574123263376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-name font-weight-bold">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae1750> name=None at 7fd9f6ae1a50> -> __attrs_140574123235600
            __attrs_140574123235600 = _static_140574123235152

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img class="logo"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123235472
            __default_140574123235472 = _DEFAULT_MARKER

            # <Substitution u'string:++plone++senaite.core.static/images/nepal.png' (19:60)> -> __attr_src
            __token = 861
            try:
                __zt_tmp = __attrs_140574123235600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'++plone++senaite.core.static/images/nepal.png', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'/>\n                    </div>\n                  </address>\n                </td>\n                ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae80d0> name=None at 7fd9f6ae8a10> -> __attrs_140574123235728
            __attrs_140574123235728 = _static_140574123262160

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad0190> name=None at 7fd9f6ae1b90> -> __attrs_140574123165776
            __attrs_140574123165776 = _static_140574123164048

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad0090> name=None at 7fd9f6ad0450> -> __attrs_140574123166608
            __attrs_140574123166608 = _static_140574123163792

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="red flex flex-column">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad0250> name=None at 7fd9f6ad0690> -> __attrs_140574123167568
            __attrs_140574123167568 = _static_140574123164240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mt-0">\n                        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123229008
            __attrs_140574123229008 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123226512
            __default_140574123226512 = _DEFAULT_MARKER

            # <Value u'laboratory/Subtitle|nothing' (27:45)> -> __cache_140574123225360
            __token = 1253
            try:
                __zt_tmp = __attrs_140574123229008
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123225360 = _static_140574397981968('path', u'laboratory/Subtitle|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/Subtitle|nothing' (27:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6adf9d0> -> __condition
            __expression = __cache_140574123225360

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123225360
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adf0d0> name=None at 7fd9f6adfa10> -> __attrs_140574123226192
            __attrs_140574123226192 = _static_140574123225296

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mt-0">\n                        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123227984
            __attrs_140574123227984 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123228752
            __default_140574123228752 = _DEFAULT_MARKER

            # <Value u'laboratory/Ministry|nothing' (30:45)> -> __cache_140574123225232
            __token = 1399
            try:
                __zt_tmp = __attrs_140574123227984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123225232 = _static_140574397981968('path', u'laboratory/Ministry|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/Ministry|nothing' (30:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6adfed0> -> __condition
            __expression = __cache_140574123225232

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123225232
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adfc50> name=None at 7fd9f6adfb90> -> __attrs_140574123225680
            __attrs_140574123225680 = _static_140574123228240

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h2 style="color: #333;">\n                        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123177744
            __attrs_140574123177744 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123178064
            __default_140574123178064 = _DEFAULT_MARKER

            # <Value u'laboratory/title|nothing' (33:47)> -> __cache_140574123198480
            __token = 1554
            try:
                __zt_tmp = __attrs_140574123177744
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123198480 = _static_140574397981968('path', u'laboratory/title|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/title|nothing' (33:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ad37d0> -> __condition
            __expression = __cache_140574123198480

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123198480
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </h2>\n                    </div>\n                  </address>\n                </td>\n                ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adfa90> name=None at 7fd9f6ae1310> -> __attrs_140574123178832
            __attrs_140574123178832 = _static_140574123227792

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="border-left: 2px solid #f0f0f0; vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad3490> name=None at 7fd9f6ad3150> -> __attrs_140574123179728
            __attrs_140574123179728 = _static_140574123177104

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f5a90> name=None at 7fd9f69f5090> -> __attrs_140574122270480
            __attrs_140574122270480 = _static_140574122269328

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div style="padding-left:10px;">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f5110> name=None at 7fd9f69f5350> -> __attrs_140574122266704
            __attrs_140574122266704 = _static_140574122266896

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-name">\n                        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123147984
            __attrs_140574123147984 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Patient Name: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ac9cd0> name=None at 7fd9f6ad0f90> -> __attrs_140574123151120
            __attrs_140574123151120 = _static_140574123138256

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123147856
            __attrs_140574123147856 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123149968
            __default_140574123149968 = _DEFAULT_MARKER

            # <Value u'model/getPatientFullName|nothing' (43:45)> -> __cache_140574123149904
            __token = 2083
            try:
                __zt_tmp = __attrs_140574123147856
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123149904 = _static_140574397981968('path', u'model/getPatientFullName|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/getPatientFullName|nothing' (43:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acce90> -> __condition
            __expression = __cache_140574123149904

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            else:
                __content = __cache_140574123149904
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                        </span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6acc610> name=None at 7fd9f6acc910> -> __attrs_140574123191120
            __attrs_140574123191120 = _static_140574123148816

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-gender">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123189072
            __attrs_140574123189072 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Gender: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad6410> name=None at 7fd9f6ad60d0> -> __attrs_140574123190160
            __attrs_140574123190160 = _static_140574123189264

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span style="font-size: 14px;">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123188688
            __default_140574123188688 = _DEFAULT_MARKER

            # <Value u'python:model.get_gender(model.Sex)' (48:79)> -> __cache_140574123188368
            __token = 2334
            try:
                __zt_tmp = __attrs_140574123190160
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123188368 = _static_140574397981968('python', u'model.get_gender(model.Sex)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:model.get_gender(model.Sex)' (48:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ad6a90> -> __condition
            __expression = __cache_140574123188368

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123188368
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad6490> name=None at 7fd9f6ad63d0> -> __attrs_140574122199952
            __attrs_140574122199952 = _static_140574123189392

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-age">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122198032
            __attrs_140574122198032 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Age: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ada390> name=None at 7fd9f6ada350> -> __attrs_140574123206096
            __attrs_140574123206096 = _static_140574123205520

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123205328
            __default_140574123205328 = _DEFAULT_MARKER

            # <Value u'model/Age/years|nothing' (52:76)> -> __cache_140574123206864
            __token = 2555
            try:
                __zt_tmp = __attrs_140574123206096
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123206864 = _static_140574397981968('path', u'model/Age/years|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/Age/years|nothing' (52:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ada110> -> __condition
            __expression = __cache_140574123206864

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span style="font-size: 14px;"/>')
            else:
                __content = __cache_140574123206864
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adaf50> name=None at 7fd9f69e44d0> -> __attrs_140574123205200
            __attrs_140574123205200 = _static_140574123208528

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-city">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123207952
            __attrs_140574123207952 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Address: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adaf90> name=None at 7fd9f6adacd0> -> __attrs_140574123635024
            __attrs_140574123635024 = _static_140574123208592

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123732368
            __default_140574123732368 = _DEFAULT_MARKER

            # <Value u'model/PatientAddress|nothing' (56:80)> -> __cache_140574123732112
            __token = 2764
            try:
                __zt_tmp = __attrs_140574123635024
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123732112 = _static_140574397981968('path', u'model/PatientAddress|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/PatientAddress|nothing' (56:80)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b5a750> -> __condition
            __expression = __cache_140574123732112

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span style="font-size: 14px;"></span>')
            else:
                __content = __cache_140574123732112
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ada590> name=None at 7fd9f6adaa90> -> __attrs_140574123230672
            __attrs_140574123230672 = _static_140574123206032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="contact-phone">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123232144
            __attrs_140574123232144 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Medical Record No: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae0a90> name=None at 7fd9f6ae0550> -> __attrs_140574123231440
            __attrs_140574123231440 = _static_140574123231888

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span style="font-size: 14px;">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123230480
            __default_140574123230480 = _DEFAULT_MARKER

            # <Value u'model/MedicalRecordNumber/value|nothing' (60:90)> -> __cache_140574123231056
            __token = 2996
            try:
                __zt_tmp = __attrs_140574123231440
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123231056 = _static_140574397981968('path', u'model/MedicalRecordNumber/value|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/MedicalRecordNumber/value|nothing' (60:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae0e90> -> __condition
            __expression = __cache_140574123231056

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123231056
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ae0c50> name=None at 7fd9f6ae0d90> -> __attrs_140574123229328
            __attrs_140574123229328 = _static_140574123232336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="lab-title">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123213904
            __attrs_140574123213904 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Received: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adc8d0> name=None at 7fd9f6adc090> -> __attrs_140574123216080
            __attrs_140574123216080 = _static_140574123215056

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123181968
            __attrs_140574123181968 = _static_140574442558096

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123213968
            __default_140574123213968 = _DEFAULT_MARKER

            # <Value u'python:view.to_localized_time(model.DateReceived)' (65:43)> -> __cache_140574123214032
            __token = 3282
            try:
                __zt_tmp = __attrs_140574123181968
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123214032 = _static_140574397981968('python', u'view.to_localized_time(model.DateReceived)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.to_localized_time(model.DateReceived)' (65:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6adc0d0> -> __condition
            __expression = __cache_140574123214032

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123214032
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </span>\n                    </div>\n                  </div>\n                  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adcb50> name=None at 7fd9f6adcbd0> -> __attrs_140574123183440
            __attrs_140574123183440 = _static_140574123215696

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="lab-title" style="margin-bottom:20px">\n                    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123181200
            __attrs_140574123181200 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Published: ')

            # <Static value=<_ast.Dict object at 0x7fd9f6ad4410> name=None at 7fd9f6ad42d0> -> __attrs_140574123183504
            __attrs_140574123183504 = _static_140574123181072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123267408
            __attrs_140574123267408 = _static_140574442558096

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123269584
            __default_140574123269584 = _DEFAULT_MARKER

            # <Value u'python:view.to_localized_time(view.timestamp)' (71:41)> -> __cache_140574123182032
            __token = 3620
            try:
                __zt_tmp = __attrs_140574123267408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574123182032 = _static_140574397981968('python', u'view.to_localized_time(view.timestamp)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.to_localized_time(view.timestamp)' (71:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae9c50> -> __condition
            __expression = __cache_140574123182032

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574123182032
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                    </span>\n                  </div>\n                </div>\n              </div>\n            </address>\n          </td>\n        </tr>\n\n      </table>\n    </div>\n    <!-- Clear Floats -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9f6adb710> name=None at 7fd9f6adbf90> -> __attrs_140574123177808
            __attrs_140574123177808 = _static_140574123210512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="clearfix"></div>\n  </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140574123762768
            if (__backup_laboratory_140574123198992 is __marker):
                del econtext['laboratory']
            else:
                econtext['laboratory'] = __backup_laboratory_140574123198992
            if (__backup_contact_140574123200272 is __marker):
                del econtext['contact']
            else:
                econtext['contact'] = __backup_contact_140574123200272
            if (__backup_client_140574123135312 is __marker):
                del econtext['client']
            else:
                econtext['client'] = __backup_client_140574123135312
            if (__backup_model_140574123199056 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140574123199056
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }