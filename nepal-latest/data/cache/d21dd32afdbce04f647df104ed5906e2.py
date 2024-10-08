# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.databox/src/senaite/databox/browser/static/resources.pt'

__tokens = {28: (u'string:${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.js', 1, 28), 175: (u'string:${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.css', 1, 175)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240906499728 = {u'src': u'string:${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.js', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240906426512 = {u'href': u'#', u'rel': u'stylesheet', }

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

            # <Static value=<_ast.Dict object at 0x7f8c616a3690> name=None at 7f8c62a4f150> -> __attrs_140240906499856
            __attrs_140240906499856 = _static_140240906499728

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906499216
            __default_140240906499216 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.js' (1:28)> -> __attr_src
            __token = 28
            try:
                __zt_tmp = __attrs_140240906499856
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140241087907024('string', u'${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.js', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7f8c61691890> name=None at 7f8c61691910> -> __attrs_140240907110800
            __attrs_140240907110800 = _static_140240906426512

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907111440
            __default_140240907111440 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.css' (1:175)> -> __attr_href
            __token = 175
            try:
                __zt_tmp = __attrs_140240907110800
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140241087907024('string', u'${view/site_url}//++plone++senaite.databox.static/bundles/senaite.databox.css', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }