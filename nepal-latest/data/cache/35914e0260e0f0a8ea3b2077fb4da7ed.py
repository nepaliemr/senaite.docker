# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/sample/templates/not_sampled.pt'

__tokens = {24: (u'python: view.is_visible()', 1, 24)}

from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140168208991440 = __compile_zt_expr
_static_140168026286928 = {u'class': u'visualClear', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168306006608 = {u'class': u'description', }
_static_140168037606288 = {u'class': u'portlet-alert-item alert alert-warning', }
_static_140168257770128 = {}
_static_140168083083024 = {u'id': u'portal-alert', }
_static_140168037636816 = {u'class': u'title font-weight-bold', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168082566864
            __attrs_140168082566864 = _static_140168257770128

            # <Value u'python: view.is_visible()' (1:24)> -> __condition
            __token = 24
            try:
                __zt_tmp = __attrs_140168082566864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u' view.is_visible()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168026347856 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b696a6b50> name=None at 7f7b696a61d0> -> __attrs_140168026362192
                __attrs_140168026362192 = _static_140168026286928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6ccd0f10> name=None at 7f7b6ccd0a50> -> __attrs_140168067779792
                __attrs_140168067779792 = _static_140168083083024

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6a172390> name=None at 7f7b6a1726d0> -> __attrs_140168166247632
                __attrs_140168166247632 = _static_140168037606288

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-warning">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a179ad0> name=None at 7f7b6a179a10> -> __attrs_140168083139280
                __attrs_140168083139280 = _static_140168037636816

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title font-weight-bold">')
                __stream_140168037634320 = []
                __append_140168037634320 = __stream_140168037634320.append
                __msgid_140168037634320 = __re_whitespace(''.join(__stream_140168037634320)).strip()
                if __msgid_140168037634320:
                    __append(translate(__msgid_140168037634320, mapping=None, default=__msgid_140168037634320, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n        The sample cannot be received\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168083136656
                __attrs_140168083136656 = _static_140168257770128

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b7a169a50> name=None at 7f7b6aadd950> -> __attrs_140168046981776
                __attrs_140168046981776 = _static_140168306006608

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="description">')
                __stream_140168047484112 = []
                __append_140168047484112 = __stream_140168047484112.append
                __append_140168047484112(u'\n        Please check that the sample has been physically collected and the\n        value for "Sampled Date" field has been set in accordance.\n      ')
                __msgid_140168047484112 = __re_whitespace(''.join(__stream_140168047484112)).strip()
                if __msgid_140168047484112:
                    __append(translate(__msgid_140168047484112, mapping=None, default=__msgid_140168047484112, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n    </div>\n  </div>\n\n')
                __i18n_domain = __previous_i18n_domain_140168026347856
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }