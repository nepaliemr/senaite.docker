# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/rejected_ar_viewlet.pt'

__tokens = {47: (u'python:view.context.getRejectionReasons()', 2, 26), 110: (u'python:rejected', 3, 20), 240: (u'python:view.context', 8, 44), 721: (u'python:sample.getSelectedRejectionReasons()', 17, 30), 781: (u'reasons', 17, 90), 822: (u'reasons', 18, 31), 844: (u'reason', 18, 53), 905: (u'python:sample.getOtherRejectionReasons()', 20, 35), 971: (u'other_reasons', 21, 24), 1079: (u'other_reasons', 23, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168026325968 = {u'id': u'portal-alert', }
_static_140168026328976 = {u'class': u'visualClear', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168037445712 = {u'aria-hidden': u'true', }
_static_140168257770128 = {}
_static_140168037447056 = {u'class': u'title', }
_static_140168037447376 = {u'class': u'bigger', }
_static_140168046999504 = {u'class': u'portlet-alert-item alert alert-warning alert-dismissible', }
_static_140168046997840 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026326224
            __attrs_140168026326224 = _static_140168257770128
            __backup_rejected_140168047764240 = get('rejected', __marker)

            # <Value u'python:view.context.getRejectionReasons()' (2:26)> -> __value
            __token = 47
            try:
                __zt_tmp = __attrs_140168026326224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.context.getRejectionReasons()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['rejected'] = __value

            # <Value u'python:rejected' (3:20)> -> __condition
            __token = 110
            try:
                __zt_tmp = __attrs_140168026326224
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'rejected', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168026325392 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b696b0f90> name=None at 7f7b696b0150> -> __attrs_140168026327696
                __attrs_140168026327696 = _static_140168026328976

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b696b03d0> name=None at 7f7b696b0c90> -> __attrs_140168046999312
                __attrs_140168046999312 = _static_140168026325968
                __backup_sample_140168026328528 = get('sample', __marker)

                # <Value u'python:view.context' (8:44)> -> __value
                __token = 240
                try:
                    __zt_tmp = __attrs_140168046999312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.context', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['sample'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa677d0> name=None at 7f7b6aa67490> -> __attrs_140168046998352
                __attrs_140168046998352 = _static_140168046999504

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-warning alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa67150> name=None at 7f7b6aa67b50> -> __attrs_140168078456144
                __attrs_140168078456144 = _static_140168046997840

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b050> name=None at 7f7b6a14b9d0> -> __attrs_140168037445776
                __attrs_140168037445776 = _static_140168037445712

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b6d0> name=None at 7f7b6a14be50> -> __attrs_140168037447248
                __attrs_140168037447248 = _static_140168037447376

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong class="bigger">')
                __stream_140168037449424 = []
                __append_140168037449424 = __stream_140168037449424.append
                __append_140168037449424(u'Rejected sample')
                __msgid_140168037449424 = __re_whitespace(''.join(__stream_140168037449424)).strip()
                if __msgid_140168037449424:
                    __append(translate(__msgid_140168037449424, mapping=None, default=__msgid_140168037449424, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b590> name=None at 7f7b6a14b290> -> __attrs_140168037446416
                __attrs_140168037446416 = _static_140168037447056

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168082123792
                __attrs_140168082123792 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168082124560 = []
                __append_140168082124560 = __stream_140168082124560.append
                __append_140168082124560(u'This Sample has been rejected due to the following reasons: ')
                __msgid_140168082124560 = __re_whitespace(''.join(__stream_140168082124560)).strip()
                if __msgid_140168082124560:
                    __append(translate(__msgid_140168082124560, mapping=None, default=__msgid_140168082124560, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n      </p>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047492432
                __attrs_140168047492432 = _static_140168257770128
                __backup_reasons_140168047354704 = get('reasons', __marker)

                # <Value u'python:sample.getSelectedRejectionReasons()' (17:30)> -> __value
                __token = 721
                try:
                    __zt_tmp = __attrs_140168047492432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'sample.getSelectedRejectionReasons()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['reasons'] = __value

                # <Value u'reasons' (17:90)> -> __condition
                __token = 781
                try:
                    __zt_tmp = __attrs_140168047492432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'reasons', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047491216
                    __attrs_140168047491216 = _static_140168257770128
                    __backup_reason_140168046997712 = get('reason', __marker)

                    # <Value u'reasons' (18:31)> -> __iterator
                    __token = 822
                    try:
                        __zt_tmp = __attrs_140168047491216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'reasons', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047492240, ) = getitem('repeat')(u'reason', __iterator)
                    econtext['reason'] = None
                    for __item in __iterator:
                        econtext['reason'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047490064
                        __default_140168047490064 = _DEFAULT_MARKER

                        # <Value u'reason' (18:53)> -> __cache_140168047490832
                        __token = 844
                        try:
                            __zt_tmp = __attrs_140168047491216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047490832 = _static_140168208991440('path', u'reason', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'reason' (18:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aadf750> -> __condition
                        __expression = __cache_140168047490832

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047490832
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</li>')
                        ____index_140168047492240 -= 1
                        if (____index_140168047492240 > 0):
                            __append('\n        ')
                    if (__backup_reason_140168046997712 is __marker):
                        del econtext['reason']
                    else:
                        econtext['reason'] = __backup_reason_140168046997712
                    __append(u'\n      </ul>')
                if (__backup_reasons_140168047354704 is __marker):
                    del econtext['reasons']
                else:
                    econtext['reasons'] = __backup_reasons_140168047354704
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047492304
                __attrs_140168047492304 = _static_140168257770128
                __backup_other_reasons_140168026287312 = get('other_reasons', __marker)

                # <Value u'python:sample.getOtherRejectionReasons()' (20:35)> -> __value
                __token = 905
                try:
                    __zt_tmp = __attrs_140168047492304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'sample.getOtherRejectionReasons()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['other_reasons'] = __value

                # <Value u'other_reasons' (21:24)> -> __condition
                __token = 971
                try:
                    __zt_tmp = __attrs_140168047492304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'other_reasons', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047490704
                    __attrs_140168047490704 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140168047489808 = []
                    __append_140168047489808 = __stream_140168047489808.append
                    __append_140168047489808(u'Other reasons: ')
                    __msgid_140168047489808 = __re_whitespace(''.join(__stream_140168047489808)).strip()
                    if __msgid_140168047489808:
                        __append(translate(__msgid_140168047489808, mapping=None, default=__msgid_140168047489808, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047837264
                    __attrs_140168047837264 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046894480
                    __default_140168046894480 = _DEFAULT_MARKER

                    # <Value u'other_reasons' (23:37)> -> __cache_140168046893712
                    __token = 1079
                    try:
                        __zt_tmp = __attrs_140168047837264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168046893712 = _static_140168208991440('path', u'other_reasons', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'other_reasons' (23:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4d990> -> __condition
                    __expression = __cache_140168046893712

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168046893712
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n      </p>')
                if (__backup_other_reasons_140168026287312 is __marker):
                    del econtext['other_reasons']
                else:
                    econtext['other_reasons'] = __backup_other_reasons_140168026287312
                __append(u'\n    </div>\n  </div>')
                if (__backup_sample_140168026328528 is __marker):
                    del econtext['sample']
                else:
                    econtext['sample'] = __backup_sample_140168026328528
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140168026325392
            if (__backup_rejected_140168047764240 is __marker):
                del econtext['rejected']
            else:
                econtext['rejected'] = __backup_rejected_140168047764240
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }