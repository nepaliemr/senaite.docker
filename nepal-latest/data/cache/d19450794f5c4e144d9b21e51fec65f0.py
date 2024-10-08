# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/portlets/templates/navigation.pt'

__tokens = {58: (u'view/navigation_root', 2, 24), 471: (u'view/createNavTree', 14, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574284391568 = {u'title': u'Toggle sidebar visibility', u'type': u'button', u'id': u'sidebarCollapse', u'class': u'btn btn-link', }
_static_140574270175696 = {u'class': u'list-unstyled', }
_static_140574442558096 = {}
_static_140574270174992 = {u'class': u'sidebar-toggle-icon', }
_static_140574284393616 = {u'id': u'sidebar-header', u'class': u'border-bottom active', }
_static_140574397981968 = __compile_zt_expr
_static_140574270188560 = {u'class': u'nav navbar-nav', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267914192
            __attrs_140574267914192 = _static_140574442558096
            __previous_i18n_domain_140574267915024 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574282046864
            __attrs_140574282046864 = _static_140574442558096
            __backup_root_140574282112080 = get('root', __marker)

            # <Value u'view/navigation_root' (2:24)> -> __value
            __token = 58
            try:
                __zt_tmp = __attrs_140574282046864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/navigation_root', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['root'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda00492c90> name=None at 7fda00492890> -> __attrs_140574284390608
            __attrs_140574284390608 = _static_140574284393616

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="sidebar-header" class="border-bottom active">\n      ')

            # <Static value=<_ast.Dict object at 0x7fda00492490> name=None at 7fda00492850> -> __attrs_140574270174864
            __attrs_140574270174864 = _static_140574284391568

            # <button ... (0:0)
            # --------------------------------------------------------
            __append(u'<button type="button" id="sidebarCollapse" class="btn btn-link"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270177232
            __default_140574270177232 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff7036d0> at 7fd9ff7034d0> -> __attr_title
            __attr_title = u'Toggle sidebar visibility'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff703710> name=None at 7fd9ff703ed0> -> __attrs_140574270177104
            __attrs_140574270177104 = _static_140574270174992

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="sidebar-toggle-icon"></i>\n      </button>\n    </div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff7039d0> name=None at 7fd9ff7037d0> -> __attrs_140574270174480
            __attrs_140574270174480 = _static_140574270175696

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="list-unstyled">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff706c10> name=None at 7fd9ff706390> -> __attrs_140574268003216
            __attrs_140574268003216 = _static_140574270188560

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="nav navbar-nav">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268003152
            __attrs_140574268003152 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268003088
            __default_140574268003088 = _DEFAULT_MARKER

            # <Value u'view/createNavTree' (14:35)> -> __cache_140574268002896
            __token = 471
            try:
                __zt_tmp = __attrs_140574268003152
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574268002896 = _static_140574397981968('path', u'view/createNavTree', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/createNavTree' (14:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f1410> -> __condition
            __expression = __cache_140574268002896

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n          SUBTREE\n        </li>')
            else:
                __content = __cache_140574268002896
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n      </ul>\n    </div>\n\n  </div>')
            if (__backup_root_140574282112080 is __marker):
                del econtext['root']
            else:
                econtext['root'] = __backup_root_140574282112080
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140574267915024
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }