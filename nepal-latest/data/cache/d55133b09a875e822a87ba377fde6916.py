# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/info_nepal.pt'

__tokens = {21: (u'python:view.model', 1, 21), 61: (u' model/Clien', 2, 21), 97: (u't model/Conta', 3, 21), 137: (u'ry python:view.laborat', 4, 23), 861: (u'string:++plone++senaite.core.static/images/nepal.png', 19, 60), 1253: (u'laboratory/Subtitle|nothing', 27, 45), 1399: (u'laboratory/Ministry|nothing', 30, 45), 1554: (u'laboratory/title|nothing', 33, 47), 2083: (u'model/getPatientFullName|nothing', 43, 45), 2334: (u'python:model.get_gender(model.Sex)', 48, 79), 2555: (u'model/Age/years|nothing', 52, 76), 2764: (u'model/PatientAddress|nothing', 56, 80), 2996: (u'model/MedicalRecordNumber/value|nothing', 60, 90), 3282: (u'python:view.to_localized_time(model.DateReceived)', 65, 43), 3620: (u'python:view.to_localized_time(view.timestamp)', 71, 41), 3927: (u'model/LabNumber|nothing', 77, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240884559696 = {u'style': u'font-size: 14px;', }
_static_140241087907024 = __compile_zt_expr
_static_140240884363152 = {u'style': u'vertical-align: middle;', u'class': u'', }
_static_140241133802128 = {}
_static_140240884557776 = {u'class': u'lab-title', }
_static_140240884349136 = {u'style': u'width: 40%', }
_static_140240897219216 = {u'style': u'padding-left:10px;', }
_static_140240884572240 = {u'src': u'string:++plone++senaite.core.static/images/nepal.png', u'class': u'logo', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240896713232 = {u'style': u'font-size: 14px;', }
_static_140240907122320 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140240897181392 = {u'class': u'row section-info no-gutters', }
_static_140240884350096 = {u'style': u'vertical-align: middle;', u'class': u'', }
_static_140240896145296 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140240884361616 = {u'class': u'laboratory-address', }
_static_140240897218640 = {u'class': u'client-name', }
_static_140240884573392 = {u'class': u'red flex flex-column', }
_static_140240896715664 = {u'class': u'client-city', }
_static_140240896978064 = {u'class': u'mt-0', }
_static_140240884574544 = {u'style': u'border-left: 2px solid #f0f0f0; vertical-align: middle;', u'class': u'', }
_static_140240896979984 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140240884575888 = {u'class': u'laboratory-address', }
_static_140240884350672 = {u'class': u'clearfix', }
_static_140240884350416 = {u'style': u'width: 50%', }
_static_140240884557136 = {u'style': u'margin-bottom:20px', u'class': u'lab-title', }
_static_140240897218960 = {u'class': u'client-gender', }
_static_140240897103056 = {u'style': u'width: 10%', }
_static_140240884360336 = {u'class': u'client-name font-weight-bold', }
_static_140240884349840 = {u'class': u'', }
_static_140240896771920 = {u'style': u'color: #333;', }
_static_140240897180624 = {u'class': u'w-100', }
_static_140240897220368 = {u'style': u'font-size: 14px;', u'class': u'font-weight-bold', }
_static_140240897103504 = {u'style': u'background-color: rgba(255, 255, 255, 0.8); border-radius: 8px;', u'class': u'table nepal-info table-sm table-condensed noborder', }
_static_140240896714128 = {u'style': u'font-size: 14px;', }
_static_140240907124624 = {u'style': u'margin-bottom:20px', u'class': u'lab-title', }
_static_140240896587024 = {u'class': u'client-age', }
_static_140240896772176 = {u'class': u'laboratory-address', }
_static_140240896999696 = {u'class': u'contact-phone', }
_static_140240896975248 = {u'class': u'mt-0', }
_static_140240897001232 = {u'style': u'font-size: 14px;', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907191184
            __attrs_140240907191184 = _static_140241133802128
            __backup_model_140240907193104 = get('model', __marker)

            # <Value u'python:view.model' (1:21)> -> __value
            __token = 21
            try:
                __zt_tmp = __attrs_140240907191184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.model', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['model'] = __value
            __backup_client_140240897029392 = get('client', __marker)

            # <Value u'model/Client' (2:21)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140240907191184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'model/Client', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['client'] = __value
            __backup_contact_140240907192144 = get('contact', __marker)

            # <Value u'model/Contact' (3:21)> -> __value
            __token = 97
            try:
                __zt_tmp = __attrs_140240907191184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'model/Contact', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['contact'] = __value
            __backup_laboratory_140240907193872 = get('laboratory', __marker)

            # <Value u'python:view.laboratory' (4:23)> -> __value
            __token = 137
            try:
                __zt_tmp = __attrs_140240907191184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.laboratory', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['laboratory'] = __value
            __previous_i18n_domain_140240897179728 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc06d0> name=None at 7f8c60dc0490> -> __attrs_140240897181584
            __attrs_140240897181584 = _static_140240897181392

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row section-info no-gutters">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc03d0> name=None at 7f8c60dc0ad0> -> __attrs_140240897181520
            __attrs_140240897181520 = _static_140240897180624

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="w-100">\n      <!-- Client Info -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c60dad690> name=None at 7f8c60dad990> -> __attrs_140240897104592
            __attrs_140240897104592 = _static_140240897103504

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table nepal-info table-sm table-condensed noborder" style="background-color: rgba(255, 255, 255, 0.8); border-radius: 8px;">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240897102352
            __attrs_140240897102352 = _static_140241133802128

            # <colgroup ... (0:0)
            # --------------------------------------------------------
            __append(u'<colgroup>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c60dad4d0> name=None at 7f8c60dadc10> -> __attrs_140240897103184
            __attrs_140240897103184 = _static_140240897103056

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 10%">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c601838d0> name=None at 7f8c60183190> -> __attrs_140240884348496
            __attrs_140240884348496 = _static_140240884349136

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 40%">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c60183dd0> name=None at 7f8c60183d50> -> __attrs_140240884349712
            __attrs_140240884349712 = _static_140240884350416

            # <col ... (0:0)
            # --------------------------------------------------------
            __append(u'<col style="width: 50%">\n              </colgroup>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c60183b90> name=None at 7f8c60183550> -> __attrs_140240884350544
            __attrs_140240884350544 = _static_140240884349840

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr class="">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c60183c90> name=None at 7f8c60183890> -> __attrs_140240884359248
            __attrs_140240884359248 = _static_140240884350096

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c60186990> name=None at 7f8c60186ed0> -> __attrs_140240884359376
            __attrs_140240884359376 = _static_140240884361616

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60186490> name=None at 7f8c60186f50> -> __attrs_140240884360656
            __attrs_140240884360656 = _static_140240884360336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-name font-weight-bold">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c601ba050> name=None at 7f8c601bac90> -> __attrs_140240884573456
            __attrs_140240884573456 = _static_140240884572240

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img class="logo"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884574288
            __default_140240884574288 = _DEFAULT_MARKER

            # <Substitution u'string:++plone++senaite.core.static/images/nepal.png' (19:60)> -> __attr_src
            __token = 861
            try:
                __zt_tmp = __attrs_140240884573456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140241087907024('string', u'++plone++senaite.core.static/images/nepal.png', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'/>\n                    </div>\n                  </address>\n                </td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c60186f90> name=None at 7f8c60186dd0> -> __attrs_140240884573584
            __attrs_140240884573584 = _static_140240884363152

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c601bae90> name=None at 7f8c601bae50> -> __attrs_140240884573072
            __attrs_140240884573072 = _static_140240884575888

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c601ba4d0> name=None at 7f8c601ba490> -> __attrs_140240896977616
            __attrs_140240896977616 = _static_140240884573392

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="red flex flex-column">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c60d8e190> name=None at 7f8c60d8ec10> -> __attrs_140240896976528
            __attrs_140240896976528 = _static_140240896975248

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mt-0">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896974992
            __attrs_140240896974992 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896978256
            __default_140240896978256 = _DEFAULT_MARKER

            # <Value u'laboratory/Subtitle|nothing' (27:45)> -> __cache_140240896978576
            __token = 1253
            try:
                __zt_tmp = __attrs_140240896974992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896978576 = _static_140241087907024('path', u'laboratory/Subtitle|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/Subtitle|nothing' (27:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d8e050> -> __condition
            __expression = __cache_140240896978576

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896978576
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c60d8ec90> name=None at 7f8c60d8ef10> -> __attrs_140240896976080
            __attrs_140240896976080 = _static_140240896978064

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mt-0">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896773776
            __attrs_140240896773776 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896773584
            __default_140240896773584 = _DEFAULT_MARKER

            # <Value u'laboratory/Ministry|nothing' (30:45)> -> __cache_140240896772944
            __token = 1399
            try:
                __zt_tmp = __attrs_140240896773776
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896772944 = _static_140241087907024('path', u'laboratory/Ministry|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/Ministry|nothing' (30:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d5cb10> -> __condition
            __expression = __cache_140240896772944

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896772944
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c60d5c750> name=None at 7f8c60d5c990> -> __attrs_140240896773264
            __attrs_140240896773264 = _static_140240896771920

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h2 style="color: #333;">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896772368
            __attrs_140240896772368 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896770512
            __default_140240896770512 = _DEFAULT_MARKER

            # <Value u'laboratory/title|nothing' (33:47)> -> __cache_140240896771024
            __token = 1554
            try:
                __zt_tmp = __attrs_140240896772368
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896771024 = _static_140241087907024('path', u'laboratory/title|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/title|nothing' (33:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d5cd50> -> __condition
            __expression = __cache_140240896771024

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896771024
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </h2>\n                    </div>\n                  </address>\n                </td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c601ba950> name=None at 7f8c601ba450> -> __attrs_140240896772304
            __attrs_140240896772304 = _static_140240884574544

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="" style="border-left: 2px solid #f0f0f0; vertical-align: middle;">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c60d5c850> name=None at 7f8c60d5c5d0> -> __attrs_140240897216784
            __attrs_140240897216784 = _static_140240896772176

            # <address ... (0:0)
            # --------------------------------------------------------
            __append(u'<address class="laboratory-address">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc9a90> name=None at 7f8c60dc9bd0> -> __attrs_140240897219088
            __attrs_140240897219088 = _static_140240897219216

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div style="padding-left:10px;">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc9850> name=None at 7f8c60dc95d0> -> __attrs_140240897218768
            __attrs_140240897218768 = _static_140240897218640

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-name">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240897216720
            __attrs_140240897216720 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Patient Name: ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc9f10> name=None at 7f8c60dc99d0> -> __attrs_140240896586640
            __attrs_140240896586640 = _static_140240897220368

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896588432
            __attrs_140240896588432 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896586000
            __default_140240896586000 = _DEFAULT_MARKER

            # <Value u'model/getPatientFullName|nothing' (43:45)> -> __cache_140240896585936
            __token = 2083
            try:
                __zt_tmp = __attrs_140240896588432
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896585936 = _static_140241087907024('path', u'model/getPatientFullName|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/getPatientFullName|nothing' (43:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d2f350> -> __condition
            __expression = __cache_140240896585936

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            else:
                __content = __cache_140240896585936
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                        </span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60dc9990> name=None at 7f8c60dc9450> -> __attrs_140240896589776
            __attrs_140240896589776 = _static_140240897218960

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-gender">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896587984
            __attrs_140240896587984 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Gender: ')

            # <Static value=<_ast.Dict object at 0x7f8c60d4e210> name=None at 7f8c60d4e1d0> -> __attrs_140240896714576
            __attrs_140240896714576 = _static_140240896713232

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span style="font-size: 14px;">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896713104
            __default_140240896713104 = _DEFAULT_MARKER

            # <Value u'python:model.get_gender(model.Sex)' (48:79)> -> __cache_140240896588944
            __token = 2334
            try:
                __zt_tmp = __attrs_140240896714576
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896588944 = _static_140241087907024('python', u'model.get_gender(model.Sex)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:model.get_gender(model.Sex)' (48:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d4e150> -> __condition
            __expression = __cache_140240896588944

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896588944
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60d2f510> name=None at 7f8c60d2f7d0> -> __attrs_140240896716304
            __attrs_140240896716304 = _static_140240896587024

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-age">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896715600
            __attrs_140240896715600 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Age: ')

            # <Static value=<_ast.Dict object at 0x7f8c60d4e590> name=None at 7f8c60d4e7d0> -> __attrs_140240897000720
            __attrs_140240897000720 = _static_140240896714128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897000656
            __default_140240897000656 = _DEFAULT_MARKER

            # <Value u'model/Age/years|nothing' (52:76)> -> __cache_140240896716048
            __token = 2555
            try:
                __zt_tmp = __attrs_140240897000720
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896716048 = _static_140241087907024('path', u'model/Age/years|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/Age/years|nothing' (52:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d4e450> -> __condition
            __expression = __cache_140240896716048

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span style="font-size: 14px;"/>')
            else:
                __content = __cache_140240896716048
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60d4eb90> name=None at 7f8c60d4ef50> -> __attrs_140240897000080
            __attrs_140240897000080 = _static_140240896715664

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="client-city">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240897002896
            __attrs_140240897002896 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Address: ')

            # <Static value=<_ast.Dict object at 0x7f8c60d94710> name=None at 7f8c60d94cd0> -> __attrs_140240897003472
            __attrs_140240897003472 = _static_140240897001232

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897003280
            __default_140240897003280 = _DEFAULT_MARKER

            # <Value u'model/PatientAddress|nothing' (56:80)> -> __cache_140240897002384
            __token = 2764
            try:
                __zt_tmp = __attrs_140240897003472
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240897002384 = _static_140241087907024('path', u'model/PatientAddress|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/PatientAddress|nothing' (56:80)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d940d0> -> __condition
            __expression = __cache_140240897002384

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span style="font-size: 14px;"></span>')
            else:
                __content = __cache_140240897002384
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c60d94110> name=None at 7f8c60d94dd0> -> __attrs_140240897000336
            __attrs_140240897000336 = _static_140240896999696

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="contact-phone">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884558288
            __attrs_140240884558288 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Medical Record No: ')

            # <Static value=<_ast.Dict object at 0x7f8c601b6f50> name=None at 7f8c601b6f10> -> __attrs_140240884558928
            __attrs_140240884558928 = _static_140240884559696

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span style="font-size: 14px;">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884559312
            __default_140240884559312 = _DEFAULT_MARKER

            # <Value u'model/MedicalRecordNumber/value|nothing' (60:90)> -> __cache_140240884558672
            __token = 2996
            try:
                __zt_tmp = __attrs_140240884558928
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240884558672 = _static_140241087907024('path', u'model/MedicalRecordNumber/value|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/MedicalRecordNumber/value|nothing' (60:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c601b6bd0> -> __condition
            __expression = __cache_140240884558672

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240884558672
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </div>\n                    </div>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c601b67d0> name=None at 7f8c601b6450> -> __attrs_140240884559248
            __attrs_140240884559248 = _static_140240884557776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="lab-title">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884559440
            __attrs_140240884559440 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Received: ')

            # <Static value=<_ast.Dict object at 0x7f8c60d8f410> name=None at 7f8c60d8f450> -> __attrs_140240896981200
            __attrs_140240896981200 = _static_140240896979984

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896982672
            __attrs_140240896982672 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896980688
            __default_140240896980688 = _DEFAULT_MARKER

            # <Value u'python:view.to_localized_time(model.DateReceived)' (65:43)> -> __cache_140240896982096
            __token = 3282
            try:
                __zt_tmp = __attrs_140240896982672
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896982096 = _static_140241087907024('python', u'view.to_localized_time(model.DateReceived)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.to_localized_time(model.DateReceived)' (65:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60d8f610> -> __condition
            __expression = __cache_140240896982096

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896982096
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                      </span>\n                    </div>\n                  </div>\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c601b6550> name=None at 7f8c601b68d0> -> __attrs_140240896982736
            __attrs_140240896982736 = _static_140240884557136

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="lab-title" style="margin-bottom:20px">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907122128
            __attrs_140240907122128 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Published: ')

            # <Static value=<_ast.Dict object at 0x7f8c6173b690> name=None at 7f8c6173b6d0> -> __attrs_140240907121552
            __attrs_140240907121552 = _static_140240907122320

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907123344
            __attrs_140240907123344 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907124688
            __default_140240907124688 = _DEFAULT_MARKER

            # <Value u'python:view.to_localized_time(view.timestamp)' (71:41)> -> __cache_140240907123600
            __token = 3620
            try:
                __zt_tmp = __attrs_140240907123344
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240907123600 = _static_140241087907024('python', u'view.to_localized_time(view.timestamp)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'python:view.to_localized_time(view.timestamp)' (71:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6173bc50> -> __condition
            __expression = __cache_140240907123600

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240907123600
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                    </span>\n                  </div>\n\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6173bf90> name=None at 7f8c6173b610> -> __attrs_140240896145168
            __attrs_140240896145168 = _static_140240907124624

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="lab-title" style="margin-bottom:20px">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896143760
            __attrs_140240896143760 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>Lab Number: ')

            # <Static value=<_ast.Dict object at 0x7f8c60cc3790> name=None at 7f8c60cc3950> -> __attrs_140240896147024
            __attrs_140240896147024 = _static_140240896145296

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold" style="font-size: 14px;">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240896144976
            __attrs_140240896144976 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896145232
            __default_140240896145232 = _DEFAULT_MARKER

            # <Value u'model/LabNumber|nothing' (77:41)> -> __cache_140240896147088
            __token = 3927
            try:
                __zt_tmp = __attrs_140240896144976
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240896147088 = _static_140241087907024('path', u'model/LabNumber|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'model/LabNumber|nothing' (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60cc3850> -> __condition
            __expression = __cache_140240896147088

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240896147088
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n                    </span>\n                  </div>\n                </div>\n              </div>\n            </address>\n          </td>\n        </tr>\n\n      </table>\n    </div>\n    <!-- Clear Floats -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c60183ed0> name=None at 7f8c60183610> -> __attrs_140240884558224
            __attrs_140240884558224 = _static_140240884350672

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="clearfix"></div>\n  </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140240897179728
            if (__backup_laboratory_140240907193872 is __marker):
                del econtext['laboratory']
            else:
                econtext['laboratory'] = __backup_laboratory_140240907193872
            if (__backup_contact_140240907192144 is __marker):
                del econtext['contact']
            else:
                econtext['contact'] = __backup_contact_140240907192144
            if (__backup_client_140240897029392 is __marker):
                del econtext['client']
            else:
                econtext['client'] = __backup_client_140240897029392
            if (__backup_model_140240907193104 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140240907193104
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }