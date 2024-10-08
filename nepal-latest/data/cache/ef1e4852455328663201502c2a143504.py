# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/uidreference/input.pt'

__tokens = {143: (u'python:view.get_input_widget_attributes()', 5, 23), 214: (u' view/klas', 6, 28), 254: (u'e view/sty', 7, 27), 294: (u'le view/ti', 8, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907024 = __compile_zt_expr
_static_140240755172496 = {u'style': u'view/style', u'class': u'view/klass', u'title': u'view/title', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240755173840 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240780918224 = set([u'style', u'class', u'title', ])

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

            # <Static value=<_ast.Dict object at 0x7f8c586529d0> name=None at 7f8c58652610> -> __attrs_140240755174416
            __attrs_140240755174416 = _static_140240755173840
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c58652490> name=None at 7f8c58652750> -> __attrs_140240766771280
            __attrs_140240766771280 = _static_140240755172496

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div')

            # <Value u'python:view.get_input_widget_attributes()' (5:23)> -> __cache_140240762494288
            __token = 143
            try:
                __zt_tmp = __attrs_140240766771280
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240762494288 = _static_140241087907024('python', u'view.get_input_widget_attributes()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_140240766774928 = __cache_140240762494288
            for (name, value, ) in __attr_140240766774928.items():
                if ((name not in _static_140240780918224) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766775120
            __default_140240766775120 = _DEFAULT_MARKER

            # <Substitution u'view/klass' (6:28)> -> __attr_class
            __token = 214
            try:
                __zt_tmp = __attrs_140240766771280
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('path', u'view/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766771344
            __default_140240766771344 = _DEFAULT_MARKER

            # <Substitution u'view/style' (7:27)> -> __attr_style
            __token = 254
            try:
                __zt_tmp = __attrs_140240766771280
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140241087907024('path', u'view/style', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766772432
            __default_140240766772432 = _DEFAULT_MARKER

            # <Substitution u'view/title' (8:26)> -> __attr_title
            __token = 294
            try:
                __zt_tmp = __attrs_140240766771280
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140241087907024('path', u'view/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>\n    <!-- ReactJS controlled component -->\n  </div>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }