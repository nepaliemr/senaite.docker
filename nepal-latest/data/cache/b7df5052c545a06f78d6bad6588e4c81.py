# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/footer_nepal.pt'

__tokens = {22: (u'python:view.get_footer_text()', 1, 22), 106: (u'python:footer', 4, 25), 266: (u'footer', 8, 34), 407: (u'python:view.laboratory', 14, 33), 355: (u'python:not footer', 13, 25), 652: (u'laboratory/Name|nothing', 22, 35), 730: (u'laboratory/PhysicalAddress/address|nothing', 23, 35), 836: (u'laboratory/PhysicalAddress/city|nothing', 24, 33), 1015: (u'laboratory/Phone|nothing', 28, 33), 1114: (u'string:mailto:${laboratory/EmailAddress|nothing}', 29, 49), 1200: (u'laboratory/EmailAddress|nothing', 30, 35), 1318: (u'laboratory/LabURL|nothing', 32, 49), 1381: (u'laboratory/LabURL|nothing', 33, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574123258384 = {u'class': u'row section-footer no-gutters', }
_static_140574122310352 = {u'id': u'footer-line', }
_static_140574123604560 = {u'class': u'row section-footer no-gutters', }
_static_140574123150800 = {u'id': u'footer-line', }
_static_140574121563728 = {u'href': u'#', }
_static_140574122310928 = {u'class': u'w-100', }
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}
_static_140574121564560 = {u'href': u'#', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574277720144
            __attrs_140574277720144 = _static_140574442558096
            __backup_footer_140574122234192 = get('footer', __marker)

            # <Value u'python:view.get_footer_text()' (1:22)> -> __value
            __token = 22
            try:
                __zt_tmp = __attrs_140574277720144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.get_footer_text()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['footer'] = __value
            __append(u'\n\n  <!-- CUSTOM FOOTER -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123209360
            __attrs_140574123209360 = _static_140574442558096

            # <Value u'python:footer' (4:25)> -> __condition
            __token = 106
            try:
                __zt_tmp = __attrs_140574123209360
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'footer', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9f6b3ba50> name=None at 7fd9f6b3b410> -> __attrs_140574123603344
                __attrs_140574123603344 = _static_140574123604560

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row section-footer no-gutters">\n      <!-- Footer Line -->\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9f6accdd0> name=None at 7fd9f6acc5d0> -> __attrs_140574123257936
                __attrs_140574123257936 = _static_140574123150800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="footer-line"></div>\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123260304
                __attrs_140574123260304 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123259728
                __default_140574123259728 = _DEFAULT_MARKER

                # <Value u'footer' (8:34)> -> __cache_140574123261392
                __token = 266
                try:
                    __zt_tmp = __attrs_140574123260304
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123261392 = _static_140574397981968('path', u'footer', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'footer' (8:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae7490> -> __condition
                __expression = __cache_140574123261392

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div/>')
                else:
                    __content = __cache_140574123261392
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n    </div>\n  ')
            __append(u'\n\n  <!-- DEFAULT FOOTER -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123149328
            __attrs_140574123149328 = _static_140574442558096
            __backup_laboratory_140574123789776 = get('laboratory', __marker)

            # <Value u'python:view.laboratory' (14:33)> -> __value
            __token = 407
            try:
                __zt_tmp = __attrs_140574123149328
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.laboratory', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['laboratory'] = __value

            # <Value u'python:not footer' (13:25)> -> __condition
            __token = 355
            try:
                __zt_tmp = __attrs_140574123149328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'not footer', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9f6ae7210> name=None at 7fd9f6ae7590> -> __attrs_140574122310480
                __attrs_140574122310480 = _static_140574123258384

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row section-footer no-gutters">\n      <!-- Footer Line -->\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9f69ffad0> name=None at 7fd9f69ffa10> -> __attrs_140574122310608
                __attrs_140574122310608 = _static_140574122310352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="footer-line"></div>\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9f69ffd10> name=None at 7fd9f69fffd0> -> __attrs_140574121810448
                __attrs_140574121810448 = _static_140574122310928

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table class="w-100">\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808144
                __attrs_140574121808144 = _static_140574442558096

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121810128
                __attrs_140574121810128 = _static_140574442558096

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121810512
                __attrs_140574121810512 = _static_140574442558096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n              ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121490384
                __attrs_140574121490384 = _static_140574442558096

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121492112
                __default_140574121492112 = _DEFAULT_MARKER

                # <Value u'laboratory/Name|nothing' (22:35)> -> __cache_140574121490576
                __token = 652
                try:
                    __zt_tmp = __attrs_140574121490384
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121490576 = _static_140574397981968('path', u'laboratory/Name|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/Name|nothing' (22:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6937a10> -> __condition
                __expression = __cache_140574121490576

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab Name')
                else:
                    __content = __cache_140574121490576
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</strong>\n              \u2022 ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121489808
                __attrs_140574121489808 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121489616
                __default_140574121489616 = _DEFAULT_MARKER

                # <Value u'laboratory/PhysicalAddress/address|nothing' (23:35)> -> __cache_140574121492304
                __token = 730
                try:
                    __zt_tmp = __attrs_140574121489808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121492304 = _static_140574397981968('path', u'laboratory/PhysicalAddress/address|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/PhysicalAddress/address|nothing' (23:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69371d0> -> __condition
                __expression = __cache_140574121492304

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab Street and Number')
                else:
                    __content = __cache_140574121492304
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n              ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121491600
                __attrs_140574121491600 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121491920
                __default_140574121491920 = _DEFAULT_MARKER

                # <Value u'laboratory/PhysicalAddress/city|nothing' (24:33)> -> __cache_140574121492240
                __token = 836
                try:
                    __zt_tmp = __attrs_140574121491600
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121492240 = _static_140574397981968('path', u'laboratory/PhysicalAddress/city|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/PhysicalAddress/city|nothing' (24:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6937fd0> -> __condition
                __expression = __cache_140574121492240

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab City')
                else:
                    __content = __cache_140574121492240
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121491408
                __attrs_140574121491408 = _static_140574442558096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n              ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122236112
                __attrs_140574122236112 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140574122235984 = []
                __append_140574122235984 = __stream_140574122235984.append
                __append_140574122235984(u'Phone')
                __msgid_140574122235984 = __re_whitespace(''.join(__stream_140574122235984)).strip()
                if __msgid_140574122235984:
                    __append(translate(__msgid_140574122235984, mapping=None, default=__msgid_140574122235984, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>:\n              ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121563152
                __attrs_140574121563152 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121563024
                __default_140574121563024 = _DEFAULT_MARKER

                # <Value u'laboratory/Phone|nothing' (28:33)> -> __cache_140574121565648
                __token = 1015
                try:
                    __zt_tmp = __attrs_140574121563152
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121565648 = _static_140574397981968('path', u'laboratory/Phone|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/Phone|nothing' (28:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69493d0> -> __condition
                __expression = __cache_140574121565648

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab Phone Number')
                else:
                    __content = __cache_140574121565648
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n              \u2022 ')

                # <Static value=<_ast.Dict object at 0x7fd9f6949990> name=None at 7fd9f6949790> -> __attrs_140574121565136
                __attrs_140574121565136 = _static_140574121564560

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121562640
                __default_140574121562640 = _DEFAULT_MARKER

                # <Substitution u'string:mailto:${laboratory/EmailAddress|nothing}' (29:49)> -> __attr_href
                __token = 1114
                try:
                    __zt_tmp = __attrs_140574121565136
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('string', u'mailto:${laboratory/EmailAddress|nothing}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n                ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121565776
                __attrs_140574121565776 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121564752
                __default_140574121564752 = _DEFAULT_MARKER

                # <Value u'laboratory/EmailAddress|nothing' (30:35)> -> __cache_140574121563280
                __token = 1200
                try:
                    __zt_tmp = __attrs_140574121565776
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574121563280 = _static_140574397981968('path', u'laboratory/EmailAddress|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/EmailAddress|nothing' (30:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6949b10> -> __condition
                __expression = __cache_140574121563280

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab Email')
                else:
                    __content = __cache_140574121563280
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n              </a>\n              \u2022 ')

                # <Static value=<_ast.Dict object at 0x7fd9f6949650> name=None at 7fd9f6949c50> -> __attrs_140574123233232
                __attrs_140574123233232 = _static_140574121563728

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123232144
                __default_140574123232144 = _DEFAULT_MARKER

                # <Substitution u'laboratory/LabURL|nothing' (32:49)> -> __attr_href
                __token = 1318
                try:
                    __zt_tmp = __attrs_140574123233232
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('path', u'laboratory/LabURL|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n                ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123229776
                __attrs_140574123229776 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123230480
                __default_140574123230480 = _DEFAULT_MARKER

                # <Value u'laboratory/LabURL|nothing' (33:35)> -> __cache_140574123229264
                __token = 1381
                try:
                    __zt_tmp = __attrs_140574123229776
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123229264 = _static_140574397981968('path', u'laboratory/LabURL|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'laboratory/LabURL|nothing' (33:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae01d0> -> __condition
                __expression = __cache_140574123229264

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Lab URL')
                else:
                    __content = __cache_140574123229264
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n              </a>\n            </div>\n          </td>\n        </tr>\n      </table>\n    </div>\n  ')
            if (__backup_laboratory_140574123789776 is __marker):
                del econtext['laboratory']
            else:
                econtext['laboratory'] = __backup_laboratory_140574123789776
            __append(u'\n\n')
            if (__backup_footer_140574122234192 is __marker):
                del econtext['footer']
            else:
                econtext['footer'] = __backup_footer_140574122234192
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }