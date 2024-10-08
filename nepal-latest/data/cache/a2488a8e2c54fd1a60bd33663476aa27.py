# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/discreeter.pt'

__tokens = {26: (u'view/collection', 1, 26), 68: (u' python:view.laborator', 2, 25), 124: (u'l string', 3, 31), 166: (u'ol strin', 4, 30), 512: (u'outofrange_symbol', 12, 27), 707: (u'python:all(map(lambda m: m.InvoiceExclude, collection))', 17, 26), 892: (u'laboratory/LaboratoryAccredited', 22, 26), 1076: (u'accredited_symbol', 25, 27), 1218: (u'laboratory/AccreditationBody', 29, 30), 1749: (u'laboratory/title', 41, 28), 1843: (u'laboratory/Confidence', 43, 40), 1892: (u'confidence_level', 44, 26), 1979: (u'confidence_level', 45, 50)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574121833808 = {u'style': u'font-family:Lucida Console, Courier, monospace;', u'class': u'accredited-symbol text-success', }
_static_140574121599184 = {u'class': u'w-100 text-muted font-weight-light small', }
_static_140574121310544 = {u'class': u'discreeter-not-invoiced', }
_static_140574121836240 = {u'class': u'', }
_static_140574121475152 = {u'class': u'discreeter-disclaimer', }
_static_140574442558096 = {}
_static_140574121474576 = {u'class': u'discreeter-copyright', }
_static_140574122250576 = {u'style': u'font-family:Lucida Console, Courier, monospace;', u'class': u'outofrange text-danger', }
_static_140574122251280 = {u'class': u'discreeter-outofrange', }
_static_140574121308496 = {u'class': u'discreeter-methods', }
_static_140574121601808 = {u'class': u'row section-discreeter no-gutters', }
_static_140574397981968 = __compile_zt_expr

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121601296
            __attrs_140574121601296 = _static_140574442558096
            __backup_collection_140574122235408 = get('collection', __marker)

            # <Value u'view/collection' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574121601296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['collection'] = __value
            __backup_laboratory_140574122327696 = get('laboratory', __marker)

            # <Value u'python:view.laboratory' (2:25)> -> __value
            __token = 68
            try:
                __zt_tmp = __attrs_140574121601296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.laboratory', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['laboratory'] = __value
            __backup_accredited_symbol_140574122234192 = get('accredited_symbol', __marker)

            # <Value u'string:\u2605' (3:31)> -> __value
            __token = 124
            try:
                __zt_tmp = __attrs_140574121601296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('string', u'\u2605', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['accredited_symbol'] = __value
            __backup_outofrange_symbol_140574123262160 = get('outofrange_symbol', __marker)

            # <Value u'string:\u26a0' (4:30)> -> __value
            __token = 166
            try:
                __zt_tmp = __attrs_140574121601296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('string', u'\u26a0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['outofrange_symbol'] = __value
            __previous_i18n_domain_140574121600720 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9f6952b10> name=None at 7fd9f69521d0> -> __attrs_140574121601360
            __attrs_140574121601360 = _static_140574121601808

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row section-discreeter no-gutters">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9f69520d0> name=None at 7fd9f6952b50> -> __attrs_140574122250832
            __attrs_140574122250832 = _static_140574121599184

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="w-100 text-muted font-weight-light small">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f1410> name=None at 7fd9f69f1210> -> __attrs_140574122251984
            __attrs_140574122251984 = _static_140574122251280

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="discreeter-outofrange">\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f1150> name=None at 7fd9f69f1b10> -> __attrs_140574122251088
            __attrs_140574122251088 = _static_140574122250576

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="outofrange text-danger" style="font-family:Lucida Console, Courier, monospace;">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122252624
            __default_140574122252624 = _DEFAULT_MARKER

            # <Value u'outofrange_symbol' (12:27)> -> __cache_140574122251216
            __token = 512
            try:
                __zt_tmp = __attrs_140574122251088
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574122251216 = _static_140574397981968('path', u'outofrange_symbol', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'outofrange_symbol' (12:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f1c10> -> __condition
            __expression = __cache_140574122251216

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n        ')
            else:
                __content = __cache_140574122251216
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121308880
            __attrs_140574121308880 = _static_140574442558096

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140574121310224 = []
            __append_140574121310224 = __stream_140574121310224.append
            __append_140574121310224(u'Result out of client specified range.')
            __msgid_140574121310224 = __re_whitespace(''.join(__stream_140574121310224)).strip()
            if __msgid_140574121310224:
                __append(translate(__msgid_140574121310224, mapping=None, default=__msgid_140574121310224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n      </div>\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f690b950> name=None at 7fd9f690bd90> -> __attrs_140574121309328
            __attrs_140574121309328 = _static_140574121310544

            # <Value u'python:all(map(lambda m: m.InvoiceExclude, collection))' (17:26)> -> __condition
            __token = 707
            try:
                __zt_tmp = __attrs_140574121309328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'all(map(lambda m: m.InvoiceExclude, collection))', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="discreeter-not-invoiced">')
                __stream_140574122251728 = []
                __append_140574122251728 = __stream_140574122251728.append
                __append_140574122251728(u'\n        Not invoiced\n      ')
                __msgid_140574122251728 = __re_whitespace(''.join(__stream_140574122251728)).strip()
                if __msgid_140574122251728:
                    __append(translate(__msgid_140574122251728, mapping=None, default=__msgid_140574122251728, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>')
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f690b150> name=None at 7fd9f690ba90> -> __attrs_140574121310608
            __attrs_140574121310608 = _static_140574121308496

            # <Value u'laboratory/LaboratoryAccredited' (22:26)> -> __condition
            __token = 892
            try:
                __zt_tmp = __attrs_140574121310608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'laboratory/LaboratoryAccredited', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="discreeter-methods">\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9f698b550> name=None at 7fd9f698bbd0> -> __attrs_140574121833104
                __attrs_140574121833104 = _static_140574121833808

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="accredited-symbol text-success" style="font-family:Lucida Console, Courier, monospace;">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121835984
                __default_140574121835984 = _DEFAULT_MARKER

                # <Value u'accredited_symbol' (25:27)> -> __cache_140574121835664
                __token = 1076
                try:
                    __zt_tmp = __attrs_140574121833104
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121835664 = _static_140574397981968('path', u'accredited_symbol', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'accredited_symbol' (25:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f698b310> -> __condition
                __expression = __cache_140574121835664

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n        ')
                else:
                    __content = __cache_140574121835664
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9f698bed0> name=None at 7fd9f698be50> -> __attrs_140574121475472
                __attrs_140574121475472 = _static_140574121836240

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="">')
                __stream_140574121120064_accreditation_body = ''
                __stream_140574121833296 = []
                __append_140574121833296 = __stream_140574121833296.append
                __append_140574121833296(u'\n          Methods included in the\n          ')
                __stream_140574121120064_accreditation_body = []
                __append_140574121120064_accreditation_body = __stream_140574121120064_accreditation_body.append

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121473104
                __attrs_140574121473104 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121474512
                __default_140574121474512 = _DEFAULT_MARKER

                # <Value u'laboratory/AccreditationBody' (29:30)> -> __cache_140574121473680
                __token = 1218
                try:
                    __zt_tmp = __attrs_140574121473104
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121473680 = _static_140574397981968('path', u'laboratory/AccreditationBody', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/AccreditationBody' (29:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6933250> -> __condition
                __expression = __cache_140574121473680

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574121473680
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140574121120064_accreditation_body(__content)
                __append_140574121833296(u'${accreditation_body}')
                __stream_140574121120064_accreditation_body = ''.join(__stream_140574121120064_accreditation_body)
                __append_140574121833296(u'\n          schedule of Accreditation for this Laboratory. Analysis remarks are not\n          accredited\n        ')
                __msgid_140574121833296 = __re_whitespace(''.join(__stream_140574121833296)).strip()
                if __msgid_140574121833296:
                    __append(translate(__msgid_140574121833296, mapping={u'accreditation_body': __stream_140574121120064_accreditation_body, }, default=__msgid_140574121833296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n      </div>')
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6933c50> name=None at 7fd9f6933510> -> __attrs_140574121475024
            __attrs_140574121475024 = _static_140574121475152

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="discreeter-disclaimer">')
            __stream_140574121473040 = []
            __append_140574121473040 = __stream_140574121473040.append
            __append_140574121473040(u'\n        Analysis results relate only to the samples tested.\n      ')
            __msgid_140574121473040 = __re_whitespace(''.join(__stream_140574121473040)).strip()
            if __msgid_140574121473040:
                __append(translate(__msgid_140574121473040, mapping=None, default=__msgid_140574121473040, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f6933a10> name=None at 7fd9f6933f10> -> __attrs_140574121472272
            __attrs_140574121472272 = _static_140574121474576

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="discreeter-copyright">')
            __stream_140574120413376_name_lab = ''
            __stream_140574121474000 = []
            __append_140574121474000 = __stream_140574121474000.append
            __append_140574121474000(u'\n        This document shall not be reproduced except in full, without the written approval of\n        ')
            __stream_140574120413376_name_lab = []
            __append_140574120413376_name_lab = __stream_140574120413376_name_lab.append

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121189136
            __attrs_140574121189136 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121188752
            __default_140574121188752 = _DEFAULT_MARKER

            # <Value u'laboratory/title' (41:28)> -> __cache_140574121472912
            __token = 1749
            try:
                __zt_tmp = __attrs_140574121189136
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574121472912 = _static_140574397981968('path', u'laboratory/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'laboratory/title' (41:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f68edd10> -> __condition
            __expression = __cache_140574121472912

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574121472912
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140574120413376_name_lab(__content)
            __append_140574121474000(u'${name_lab}')
            __stream_140574120413376_name_lab = ''.join(__stream_140574120413376_name_lab)
            __append_140574121474000(u'\n      ')
            __msgid_140574121474000 = __re_whitespace(''.join(__stream_140574121474000)).strip()
            if __msgid_140574121474000:
                __append(translate(__msgid_140574121474000, mapping={u'name_lab': __stream_140574120413376_name_lab, }, default=__msgid_140574121474000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121186960
            __attrs_140574121186960 = _static_140574442558096
            __backup_confidence_level_140574122252304 = get('confidence_level', __marker)

            # <Value u'laboratory/Confidence' (43:40)> -> __value
            __token = 1843
            try:
                __zt_tmp = __attrs_140574121186960
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'laboratory/Confidence', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['confidence_level'] = __value

            # <Value u'confidence_level' (44:26)> -> __condition
            __token = 1892
            try:
                __zt_tmp = __attrs_140574121186960
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'confidence_level', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>')
                __stream_140574120413376_lab_confidence = ''
                __stream_140574121475664 = []
                __append_140574121475664 = __stream_140574121475664.append
                __append_140574121475664(u'\n        Test results are at a ')
                __stream_140574120413376_lab_confidence = []
                __append_140574120413376_lab_confidence = __stream_140574120413376_lab_confidence.append

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121187536
                __attrs_140574121187536 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121186576
                __default_140574121186576 = _DEFAULT_MARKER

                # <Value u'confidence_level' (45:50)> -> __cache_140574121189072
                __token = 1979
                try:
                    __zt_tmp = __attrs_140574121187536
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121189072 = _static_140574397981968('path', u'confidence_level', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'confidence_level' (45:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f68ed410> -> __condition
                __expression = __cache_140574121189072

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574121189072
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140574120413376_lab_confidence(__content)
                __append_140574121475664(u'${lab_confidence}')
                __stream_140574120413376_lab_confidence = ''.join(__stream_140574120413376_lab_confidence)
                __append_140574121475664(u'% confidence level\n      ')
                __msgid_140574121475664 = __re_whitespace(''.join(__stream_140574121475664)).strip()
                if __msgid_140574121475664:
                    __append(translate(__msgid_140574121475664, mapping={u'lab_confidence': __stream_140574120413376_lab_confidence, }, default=__msgid_140574121475664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>')
            if (__backup_confidence_level_140574122252304 is __marker):
                del econtext['confidence_level']
            else:
                econtext['confidence_level'] = __backup_confidence_level_140574122252304
            __append(u'\n    </div>\n  </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140574121600720
            if (__backup_outofrange_symbol_140574123262160 is __marker):
                del econtext['outofrange_symbol']
            else:
                econtext['outofrange_symbol'] = __backup_outofrange_symbol_140574123262160
            if (__backup_accredited_symbol_140574122234192 is __marker):
                del econtext['accredited_symbol']
            else:
                econtext['accredited_symbol'] = __backup_accredited_symbol_140574122234192
            if (__backup_laboratory_140574122327696 is __marker):
                del econtext['laboratory']
            else:
                econtext['laboratory'] = __backup_laboratory_140574122327696
            if (__backup_collection_140574122235408 is __marker):
                del econtext['collection']
            else:
                econtext['collection'] = __backup_collection_140574122235408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }