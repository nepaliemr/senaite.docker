# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.listing/src/senaite/app/listing/browser/viewlets/../static/resources.pt'

__tokens = {28: (u'string:${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.js', 1, 28), 182: (u'string:${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.css', 1, 182)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574257171216 = {u'src': u'string:${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.js', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574257170000 = {u'href': u'#', u'rel': u'stylesheet', }

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

            # <Static value=<_ast.Dict object at 0x7fd9fea9cb10> name=None at 7fd9fea9c790> -> __attrs_140574257171088
            __attrs_140574257171088 = _static_140574257171216

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257171984
            __default_140574257171984 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.js' (1:28)> -> __attr_src
            __token = 28
            try:
                __zt_tmp = __attrs_140574257171088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9fea9c650> name=None at 7fd9fea9c690> -> __attrs_140574257245136
            __attrs_140574257245136 = _static_140574257170000

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257170768
            __default_140574257170768 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.css' (1:182)> -> __attr_href
            __token = 182
            try:
                __zt_tmp = __attrs_140574257245136
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.app.listing.static/bundles/senaite.app.listing.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }