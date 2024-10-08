# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/retest_ar_viewlet.pt'

__tokens = {46: (u'python:view.context.getInvalidated()', 2, 25), 104: (u'python:invalid', 3, 20), 657: (u'python:invalid.absolute_url()', 16, 32), 712: (u'python:invalid.getId()', 17, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168037448016 = {u'id': u'portal-alert', }
_static_140168047008016 = {u'class': u'title', }
_static_140168047009488 = {u'href': u'python:invalid.absolute_url()', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168037400720 = {u'class': u'visualClear', }
_static_140168026220176 = {u'class': u'portlet-alert-item alert alert-info alert-dismissible', }
_static_140168257770128 = {}
_static_140168047358096 = {u'aria-hidden': u'true', }
_static_140168026330896 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026337680
            __attrs_140168026337680 = _static_140168257770128
            __backup_invalid_140168026339408 = get('invalid', __marker)

            # <Value u'python:view.context.getInvalidated()' (2:25)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140168026337680
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.context.getInvalidated()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['invalid'] = __value

            # <Value u'python:invalid' (3:20)> -> __condition
            __token = 104
            try:
                __zt_tmp = __attrs_140168026337680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'invalid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168026340304 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6a140090> name=None at 7f7b6a1408d0> -> __attrs_140168047342608
                __attrs_140168047342608 = _static_140168037400720

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b950> name=None at 7f7b6a14bd90> -> __attrs_140168026285392
                __attrs_140168026285392 = _static_140168037448016

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b69696690> name=None at 7f7b69696310> -> __attrs_140168026332496
                __attrs_140168026332496 = _static_140168026220176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-info alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696b1710> name=None at 7f7b696b1f50> -> __attrs_140168047358288
                __attrs_140168047358288 = _static_140168026330896

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aabf090> name=None at 7f7b6aabfa50> -> __attrs_140168047361232
                __attrs_140168047361232 = _static_140168047358096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047361040
                __attrs_140168047361040 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168047359568 = []
                __append_140168047359568 = __stream_140168047359568.append
                __append_140168047359568(u'Info')
                __msgid_140168047359568 = __re_whitespace(''.join(__stream_140168047359568)).strip()
                if __msgid_140168047359568:
                    __append(translate(__msgid_140168047359568, mapping=None, default=__msgid_140168047359568, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa69910> name=None at 7f7b6aa69310> -> __attrs_140168047009232
                __attrs_140168047009232 = _static_140168047008016

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047008784
                __attrs_140168047008784 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168047007120 = []
                __append_140168047007120 = __stream_140168047007120.append
                __append_140168047007120(u'This Sample has been generated automatically due to the retraction of the Sample ')
                __msgid_140168047007120 = __re_whitespace(''.join(__stream_140168047007120)).strip()
                if __msgid_140168047007120:
                    __append(translate(__msgid_140168047007120, mapping=None, default=__msgid_140168047007120, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa69ed0> name=None at 7f7b6aa69610> -> __attrs_140168046859280
                __attrs_140168046859280 = _static_140168047009488

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046859088
                __default_140168046859088 = _DEFAULT_MARKER

                # <Substitution u'python:invalid.absolute_url()' (16:32)> -> __attr_href
                __token = 657
                try:
                    __zt_tmp = __attrs_140168046859280
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u'invalid.absolute_url()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047008144
                __default_140168047008144 = _DEFAULT_MARKER

                # <Value u'python:invalid.getId()' (17:24)> -> __cache_140168047006800
                __token = 712
                try:
                    __zt_tmp = __attrs_140168046859280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047006800 = _static_140168208991440('python', u'invalid.getId()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:invalid.getId()' (17:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa69810> -> __condition
                __expression = __cache_140168047006800

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047006800
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>\n      </p>\n    </div>\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140168026340304
            if (__backup_invalid_140168026339408 is __marker):
                del econtext['invalid']
            else:
                econtext['invalid'] = __backup_invalid_140168026339408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }