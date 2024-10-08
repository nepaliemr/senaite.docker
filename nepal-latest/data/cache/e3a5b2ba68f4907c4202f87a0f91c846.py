# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/browser/viewlets/templates/setupbutton.pt'

__tokens = {43: (u'python:view.is_manager()', 1, 43), 151: (u'string:${view/portal/absolute_url}/impress-controlpanel', 4, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574267288144 = {u'class': u'd-inline-block', }
_static_140574266210448 = {u'class': u'fas fa-cogs', }
_static_140574397981968 = __compile_zt_expr
_static_140574267285968 = {u'title': u'Impress Controlpanel', u'href': u'#', u'class': u'btn btn-outline-dark btn-sm', u'target': u'_blank', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff442a50> name=None at 7fd9ff442250> -> __attrs_140574267286416
            __attrs_140574267286416 = _static_140574267288144

            # <Value u'python:view.is_manager()' (1:43)> -> __condition
            __token = 43
            try:
                __zt_tmp = __attrs_140574267286416
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'view.is_manager()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="d-inline-block">\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4421d0> name=None at 7fd9ff442710> -> __attrs_140574134355664
                __attrs_140574134355664 = _static_140574267285968

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267879952
                __default_140574267879952 = _DEFAULT_MARKER

                # <Substitution u'string:${view/portal/absolute_url}/impress-controlpanel' (4:26)> -> __attr_href
                __token = 151
                try:
                    __zt_tmp = __attrs_140574134355664
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('string', u'${view/portal/absolute_url}/impress-controlpanel', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u' class="btn btn-outline-dark btn-sm" target="_blank"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574254552208
                __default_140574254552208 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7fd9fe81dc10> at 7fd9fe81d250> -> __attr_title
                __attr_title = u'Impress Controlpanel'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff33b890> name=None at 7fd9ff444290> -> __attrs_140574267431568
                __attrs_140574267431568 = _static_140574266210448

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-cogs"></i>\n  </a>\n</div>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }