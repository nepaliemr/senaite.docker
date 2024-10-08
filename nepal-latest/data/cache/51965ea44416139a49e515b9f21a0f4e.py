# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/favicon.pt'

__tokens = {32: (u'view/site_url', 1, 32), 119: (u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico', 2, 71), 244: (u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico', 3, 54)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574257238672 = {u'href': u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico', u'rel': u'apple-touch-icon', }
_static_140574257242320 = {u'href': u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico', u'type': u'image/x-icon', u'rel': u'shortcut icon', }
_static_140574442558096 = {}

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275597008
            __attrs_140574275597008 = _static_140574442558096
            __backup_portal_url_140574257225040 = get('portal_url', __marker)

            # <Value u'view/site_url' (1:32)> -> __value
            __token = 32
            try:
                __zt_tmp = __attrs_140574275597008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/site_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feaae0d0> name=None at 7fd9feaae1d0> -> __attrs_140574257242192
            __attrs_140574257242192 = _static_140574257242320

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="shortcut icon" type="image/x-icon"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257242384
            __default_140574257242384 = _DEFAULT_MARKER

            # <Substitution u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico' (2:71)> -> __attr_href
            __token = 119
            try:
                __zt_tmp = __attrs_140574257242192
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'$portal_url/++plone++senaite.core.static/images/favicon.ico', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' />\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feaad290> name=None at 7fd9feaad490> -> __attrs_140574257176080
            __attrs_140574257176080 = _static_140574257238672

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="apple-touch-icon"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257241872
            __default_140574257241872 = _DEFAULT_MARKER

            # <Substitution u'string:$portal_url/++plone++senaite.core.static/images/favicon.ico' (3:54)> -> __attr_href
            __token = 244
            try:
                __zt_tmp = __attrs_140574257176080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'$portal_url/++plone++senaite.core.static/images/favicon.ico', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' />\n')
            if (__backup_portal_url_140574257225040 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140574257225040
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }