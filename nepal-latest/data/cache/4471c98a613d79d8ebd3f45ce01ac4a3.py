# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/invalid_ar_viewlet.pt'

__tokens = {45: (u'python:view.context.getRetest()', 2, 24), 98: (u'python:retest', 3, 20), 694: (u'python:retest.absolute_url()', 16, 32), 748: (u'python:retest.getId()', 17, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168046860304 = {u'class': u'portlet-alert-item alert alert-warning alert-dismissible', }
_static_140168047007120 = {u'id': u'portal-alert', }
_static_140168026259664 = {u'class': u'title', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047505488 = {u'href': u'python:retest.absolute_url()', }
_static_140168257770128 = {}
_static_140168047008528 = {u'class': u'visualClear', }
_static_140168046862032 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140168026261008 = {u'aria-hidden': u'true', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047345104
            __attrs_140168047345104 = _static_140168257770128
            __backup_retest_140168026339408 = get('retest', __marker)

            # <Value u'python:view.context.getRetest()' (2:24)> -> __value
            __token = 45
            try:
                __zt_tmp = __attrs_140168047345104
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.context.getRetest()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['retest'] = __value

            # <Value u'python:retest' (3:20)> -> __condition
            __token = 98
            try:
                __zt_tmp = __attrs_140168047345104
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'retest', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047158672 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa69b10> name=None at 7f7b6aa69910> -> __attrs_140168047009296
                __attrs_140168047009296 = _static_140168047008528

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa69590> name=None at 7f7b6aa69d90> -> __attrs_140168047007696
                __attrs_140168047007696 = _static_140168047007120

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa45810> name=None at 7f7b6aa45f10> -> __attrs_140168046861072
                __attrs_140168046861072 = _static_140168046860304

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-warning alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa45ed0> name=None at 7f7b6aa451d0> -> __attrs_140168046893712
                __attrs_140168046893712 = _static_140168046862032

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b696a0610> name=None at 7f7b696a0ad0> -> __attrs_140168026260944
                __attrs_140168026260944 = _static_140168026261008

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026263440
                __attrs_140168026263440 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168046860368 = []
                __append_140168046860368 = __stream_140168046860368.append
                __append_140168046860368(u'Warning')
                __msgid_140168046860368 = __re_whitespace(''.join(__stream_140168046860368)).strip()
                if __msgid_140168046860368:
                    __append(translate(__msgid_140168046860368, mapping=None, default=__msgid_140168046860368, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696a00d0> name=None at 7f7b696a0cd0> -> __attrs_140168026260688
                __attrs_140168026260688 = _static_140168026259664

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026262160
                __attrs_140168026262160 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168026261712 = []
                __append_140168026261712 = __stream_140168026261712.append
                __append_140168026261712(u'These results have been withdrawn and are listed here for trace-ability purposes. Please follow the link to the retest ')
                __msgid_140168026261712 = __re_whitespace(''.join(__stream_140168026261712)).strip()
                if __msgid_140168026261712:
                    __append(translate(__msgid_140168026261712, mapping=None, default=__msgid_140168026261712, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aae3050> name=None at 7f7b6aae3610> -> __attrs_140168047509072
                __attrs_140168047509072 = _static_140168047505488

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047505808
                __default_140168047505808 = _DEFAULT_MARKER

                # <Substitution u'python:retest.absolute_url()' (16:32)> -> __attr_href
                __token = 694
                try:
                    __zt_tmp = __attrs_140168047509072
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u'retest.absolute_url()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047506896
                __default_140168047506896 = _DEFAULT_MARKER

                # <Value u'python:retest.getId()' (17:24)> -> __cache_140168047509200
                __token = 748
                try:
                    __zt_tmp = __attrs_140168047509072
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047509200 = _static_140168208991440('python', u'retest.getId()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:retest.getId()' (17:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aae3990> -> __condition
                __expression = __cache_140168047509200

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047509200
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>\n      </p>\n    </div>\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140168047158672
            if (__backup_retest_140168026339408 is __marker):
                del econtext['retest']
            else:
                econtext['retest'] = __backup_retest_140168026339408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }