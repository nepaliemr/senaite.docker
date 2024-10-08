# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.patient/src/senaite/patient/browser/viewlets/templates/temporary_mrn_viewlet.pt'

__tokens = {41: (u'python: view.is_visible()', 2, 20), 188: (u'nocall:context/portal_url', 7, 48)}

from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140168208991440 = __compile_zt_expr
_static_140168047767248 = {u'id': u'portal-alert', }
_static_140168026350416 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140168160146768 = {u'class': u'visualClear', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168257770128 = {}
_static_140168037447056 = {u'style': u'margin-bottom:0', u'class': u'title', }
_static_140168047766352 = {u'class': u'portlet-alert-item alert alert-warning alert-dismissible', }
_static_140168037446032 = {u'aria-hidden': u'true', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047344912
            __attrs_140168047344912 = _static_140168257770128

            # <Value u'python: view.is_visible()' (2:20)> -> __condition
            __token = 41
            try:
                __zt_tmp = __attrs_140168047344912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u' view.is_visible()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047343568 = __i18n_domain
                __i18n_domain = u'senaite.patient'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b7164f550> name=None at 7f7b7164f610> -> __attrs_140168047764688
                __attrs_140168047764688 = _static_140168160146768

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab22ed0> name=None at 7f7b6ab22950> -> __attrs_140168047767376
                __attrs_140168047767376 = _static_140168047767248
                __backup_portal_url_140168026384912 = get('portal_url', __marker)

                # <Value u'nocall:context/portal_url' (7:48)> -> __value
                __token = 188
                try:
                    __zt_tmp = __attrs_140168047767376
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('nocall', u'context/portal_url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['portal_url'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab22b50> name=None at 7f7b6ab22650> -> __attrs_140168047765264
                __attrs_140168047765264 = _static_140168047766352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-warning alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696b6350> name=None at 7f7b696b6290> -> __attrs_140168037448784
                __attrs_140168037448784 = _static_140168026350416

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b190> name=None at 7f7b6a14bf90> -> __attrs_140168037446544
                __attrs_140168037446544 = _static_140168037446032

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14b590> name=None at 7f7b6a14b290> -> __attrs_140168046998032
                __attrs_140168046998032 = _static_140168037447056

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title" style="margin-bottom:0">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047000464
                __attrs_140168047000464 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168046999760 = []
                __append_140168046999760 = __stream_140168046999760.append
                __append_140168046999760(u'\n          The Medical Record Number (MRN) assigned to this sample is temporary\n        ')
                __msgid_140168046999760 = __re_whitespace(''.join(__stream_140168046999760)).strip()
                if __msgid_140168046999760:
                    __append(translate(__msgid_140168046999760, mapping=None, default=__msgid_140168046999760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>&nbsp;\n      </p>\n    </div>\n  </div>')
                if (__backup_portal_url_140168026384912 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140168026384912
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140168047343568
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }