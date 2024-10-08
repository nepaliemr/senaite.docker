# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/sidebar.pt'

__tokens = {46: (u'python:view.render_navigation_portlet()', 2, 28), 109: (u" python:view.is_navbar_toggled() and 'toggled' or 'minimized", 3, 22), 193: (u'python:view.available() and navigation', 4, 20), 260: (u'string:${clazz} bg-light', 5, 27), 380: (u'navigation', 9, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574270225680 = {u'id': u'sidebar', u'class': u'string:${clazz} bg-light', }
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

            # <Static value=<_ast.Dict object at 0x7fd9ff70fd10> name=None at 7fd9ff70f550> -> __attrs_140574270225296
            __attrs_140574270225296 = _static_140574270225680
            __backup_navigation_140574257176400 = get('navigation', __marker)

            # <Value u'python:view.render_navigation_portlet()' (2:28)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140574270225296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.render_navigation_portlet()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['navigation'] = __value
            __backup_clazz_140574284461840 = get('clazz', __marker)

            # <Value u"python:view.is_navbar_toggled() and 'toggled' or 'minimized'" (3:22)> -> __value
            __token = 109
            try:
                __zt_tmp = __attrs_140574270225296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"view.is_navbar_toggled() and 'toggled' or 'minimized'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['clazz'] = __value

            # <Value u'python:view.available() and navigation' (4:20)> -> __condition
            __token = 193
            try:
                __zt_tmp = __attrs_140574270225296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'view.available() and navigation', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270225808 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav id="sidebar"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270222544
                __default_140574270222544 = _DEFAULT_MARKER

                # <Substitution u'string:${clazz} bg-light' (5:27)> -> __attr_class
                __token = 260
                try:
                    __zt_tmp = __attrs_140574270225296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140574397981968('string', u'${clazz} bg-light', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n\n  <!-- Navigation portlet -->\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268006352
                __attrs_140574268006352 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268002704
                __default_140574268002704 = _DEFAULT_MARKER

                # <Value u'navigation' (9:30)> -> __cache_140574268003472
                __token = 380
                try:
                    __zt_tmp = __attrs_140574268006352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574268003472 = _static_140574397981968('path', u'navigation', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'navigation' (9:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f1c50> -> __condition
                __expression = __cache_140574268003472

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div/>')
                else:
                    __content = __cache_140574268003472
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n</nav>')
                __i18n_domain = __previous_i18n_domain_140574270225808
            if (__backup_clazz_140574284461840 is __marker):
                del econtext['clazz']
            else:
                econtext['clazz'] = __backup_clazz_140574284461840
            if (__backup_navigation_140574257176400 is __marker):
                del econtext['navigation']
            else:
                econtext['navigation'] = __backup_navigation_140574257176400
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }