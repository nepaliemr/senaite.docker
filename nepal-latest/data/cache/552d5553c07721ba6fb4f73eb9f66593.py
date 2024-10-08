# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/toolbar.pt'

__tokens = {105: (u'view/context_state', 3, 31), 154: (u' view/portal_stat', 4, 29), 205: (u's python:view.get_global_sections', 5, 31), 274: (u'or python:view.get_language_selecto', 6, 32), 340: (u'bar python:view.get_personal_b', 7, 26), 495: (u'portal_state/portal_url', 11, 56), 550: (u'python:view.get_toolbar_logo()', 12, 29), 586: (u' python:view.get_toolbar_styles(', 12, 65), 1141: (u'view/base_render', 26, 34), 1306: (u'personal_bar/user_name', 33, 42), 1367: (u'global_sections/render', 34, 36), 1508: (u'language_selector/template', 39, 36), 1628: (u'personal_bar/user_name', 43, 42), 1816: (u'string:${portal_state/portal_url}/spotlight', 47, 32), 1996: (u'view/is_manager', 53, 42), 2074: (u'view/get_lims_setup_url', 55, 32), 2300: (u'personal_bar/user_name', 63, 51), 2580: (u'personal_bar/homelink_url', 71, 32), 2637: (u'personal_bar/user_name', 72, 29), 2804: (u'view/context_state/current_page_url', 76, 28), 2906: (u'personal_bar/user_actions', 78, 33), 2993: (u"python:action['href'] == url", 80, 36), 3054: (u'action', 81, 31), 3067: (u" python:selected and 'active nav-link' or 'nav-link", 81, 44), 3158: (u"python:action['id'] == 'personaltools-site-setup'", 82, 36), 3328: (u"python:action['id'] == 'personaltools-my-organization'", 85, 45), 3508: (u"python:action['id'] == 'personaltools-logout'", 88, 39), 3682: (u"python:action['id'] == 'personaltools-user-profile'", 91, 44), 3862: (u'action/title', 94, 43), 4070: (u'not:personal_bar/user_name', 103, 42), 4155: (u'personal_bar/user_actions', 104, 56), 4126: (u'python:1', 104, 27), 4225: (u'action/href', 105, 42), 4243: (u' string:nav-lin', 105, 60), 4303: (u'action/title', 106, 41), 4412: (u"python:action['id'] == 'personaltools-logout'", 109, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574267983440 = {u'class': u'nav-item', }
_static_140574257222864 = {u'class': u'nav navbar-nav mr-auto content-views', }
_static_140574267979472 = {u'class': u'fas fa-wrench', }
_static_140574266104848 = {u'class': u'nav-item', }
_static_140574267985872 = {u'href': u'string:${portal_state/portal_url}/spotlight', u'class': u'nav-link', u'title': u'Press Ctrl+Space to trigger the Spotlight search', }
_static_140574257218192 = {u'class': u'fas fa-bars', }
_static_140574267938960 = {u'class': u'fas fa-cog', }
_static_140574397981968 = __compile_zt_expr
_static_140574267995088 = {u'class': u'nav-item', }
_static_140574267912784 = {u'href': u'#', u'class': u'navbar-brand', }
_static_140574267914320 = {u'src': u'python:view.get_toolbar_logo()', u'style': u'python:view.get_toolbar_styles()', }
_static_140574442558096 = {}
_static_140574267893200 = {u'href': u'', u'class': u'string:nav-link', }
_static_140574257140432 = {u'aria-label': u'Toggle navigation', u'aria-controls': u'toolbarContent', u'data-target': u'#toolbarContent', u'aria-expanded': u'false', u'data-toggle': u'collapse', u'type': u'button', u'class': u'navbar-toggler btn btn-outline-light', }
_static_140574267997456 = {u'class': u'nav-item', }
_static_140574267991376 = {u'class': u'fas fa-sign-out-alt', }
_static_140574257218064 = {u'class': u'collapse navbar-collapse', u'id': u'toolbarContent', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574267901136 = {u'class': u'nav-item', }
_static_140574266105360 = {u'class': u'dropdown-menu dropdown-menu-right', }
_static_140574267992976 = {u'class': u'fas fa-user-cog', }
_static_140574267901520 = {u'href': u'', u'class': u"python:selected and 'active nav-link' or 'nav-link'", }
_static_140574275633808 = {u'class': u'fas fa-search', }
_static_140574267889168 = {u'id': u'senaite-toolbar', u'class': u'navbar static-top navbar-expand-md', }
_static_140574267936208 = {u'class': u'icon-logout', }
_static_140574267987344 = {u'href': u'view/get_lims_setup_url', u'class': u'nav-link', }
_static_140574284443792 = set([u'class', ])
_static_140574267939600 = {u'aria-haspopup': u'true', u'aria-expanded': u'false', u'id': u'navbarUserDropdown', u'href': u'#', u'role': u'button', u'data-toggle': u'dropdown', u'class': u'nav-link dropdown-toggle', }
_static_140574275633232 = {u'class': u'nav-item', }
_static_140574257251216 = {u'class': u'navbar-nav ml-auto', }
_static_140574267989456 = {u'class': u'nav-item dropdown', }
_static_140574267979216 = {u'class': u'fas fa-building', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff4d5610> name=None at 7fd9ff4d5a10> -> __attrs_140574275646160
            __attrs_140574275646160 = _static_140574267889168
            __backup_context_state_140574284482128 = get('context_state', __marker)

            # <Value u'view/context_state' (3:31)> -> __value
            __token = 105
            try:
                __zt_tmp = __attrs_140574275646160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/context_state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_portal_state_140574257170512 = get('portal_state', __marker)

            # <Value u'view/portal_state' (4:29)> -> __value
            __token = 154
            try:
                __zt_tmp = __attrs_140574275646160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/portal_state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_global_sections_140574267890576 = get('global_sections', __marker)

            # <Value u'python:view.get_global_sections()' (5:31)> -> __value
            __token = 205
            try:
                __zt_tmp = __attrs_140574275646160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.get_global_sections()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['global_sections'] = __value
            __backup_language_selector_140574267891280 = get('language_selector', __marker)

            # <Value u'python:view.get_language_selector()' (6:32)> -> __value
            __token = 274
            try:
                __zt_tmp = __attrs_140574275646160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.get_language_selector()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['language_selector'] = __value
            __backup_personal_bar_140574267889680 = get('personal_bar', __marker)

            # <Value u'python:view.get_personal_bar()' (7:26)> -> __value
            __token = 340
            try:
                __zt_tmp = __attrs_140574275646160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.get_personal_bar()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __previous_i18n_domain_140574275647504 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append(u'<nav id="senaite-toolbar" class="navbar static-top navbar-expand-md">\n\n  <!-- Navbar Brand Icon -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4db250> name=None at 7fd9ff4dbf90> -> __attrs_140574267914896
            __attrs_140574267914896 = _static_140574267912784

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="navbar-brand"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267914128
            __default_140574267914128 = _DEFAULT_MARKER

            # <Substitution u'portal_state/portal_url' (11:56)> -> __attr_href
            __token = 495
            try:
                __zt_tmp = __attrs_140574267914896
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('path', u'portal_state/portal_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4db850> name=None at 7fd9ff4db890> -> __attrs_140574257142480
            __attrs_140574257142480 = _static_140574267914320

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267913808
            __default_140574267913808 = _DEFAULT_MARKER

            # <Substitution u'python:view.get_toolbar_logo()' (12:29)> -> __attr_src
            __token = 550
            try:
                __zt_tmp = __attrs_140574257142480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('python', u'view.get_toolbar_logo()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267915280
            __default_140574267915280 = _DEFAULT_MARKER

            # <Substitution u'python:view.get_toolbar_styles()' (12:65)> -> __attr_style
            __token = 586
            try:
                __zt_tmp = __attrs_140574257142480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140574397981968('python', u'view.get_toolbar_styles()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((u' style="%s"' % __attr_style))
            __append(u' />\n  </a>\n\n  <!-- Navbar Toggle Button -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9fea952d0> name=None at 7fd9fea95dd0> -> __attrs_140574257218512
            __attrs_140574257218512 = _static_140574257140432

            # <button ... (0:0)
            # --------------------------------------------------------
            __append(u'<button class="navbar-toggler btn btn-outline-light" type="button" data-toggle="collapse" data-target="#toolbarContent" aria-controls="toolbarContent" aria-expanded="false" aria-label="Toggle navigation">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa8290> name=None at 7fd9feaa8710> -> __attrs_140574257217808
            __attrs_140574257217808 = _static_140574257218192

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-bars"></i>\n  </button>\n\n  <!-- Navbar Menu Items -->\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa8210> name=None at 7fd9feaa8350> -> __attrs_140574257222928
            __attrs_140574257222928 = _static_140574257218064

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="collapse navbar-collapse" id="toolbarContent">\n\n    <!-- left -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa94d0> name=None at 7fd9feaa9390> -> __attrs_140574257223184
            __attrs_140574257223184 = _static_140574257222864

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="nav navbar-nav mr-auto content-views">\n      <!-- contentviews -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257251088
            __attrs_140574257251088 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257250704
            __default_140574257250704 = _DEFAULT_MARKER

            # <Value u'view/base_render' (26:34)> -> __cache_140574257252816
            __token = 1141
            try:
                __zt_tmp = __attrs_140574257251088
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257252816 = _static_140574397981968('path', u'view/base_render', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/base_render' (26:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab0750> -> __condition
            __expression = __cache_140574257252816

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div></div>')
            else:
                __content = __cache_140574257252816
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </ul>\n\n    <!-- right -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9feab0390> name=None at 7fd9feab0810> -> __attrs_140574257253136
            __attrs_140574257253136 = _static_140574257251216

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="navbar-nav ml-auto">\n\n      <!-- Global Sections -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4ef3d0> name=None at 7fd9ff4ef1d0> -> __attrs_140574267996368
            __attrs_140574267996368 = _static_140574267995088

            # <Value u'personal_bar/user_name' (33:42)> -> __condition
            __token = 1306
            try:
                __zt_tmp = __attrs_140574267996368
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'personal_bar/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item">\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267996048
                __attrs_140574267996048 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267996880
                __default_140574267996880 = _DEFAULT_MARKER

                # <Value u'global_sections/render' (34:36)> -> __cache_140574267995344
                __token = 1367
                try:
                    __zt_tmp = __attrs_140574267996048
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267995344 = _static_140574397981968('path', u'global_sections/render', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'global_sections/render' (34:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4efc50> -> __condition
                __expression = __cache_140574267995344

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140574267995344
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n      </li>')
            __append(u'\n\n      <!-- Language Selector -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4efd10> name=None at 7fd9ff4ef9d0> -> __attrs_140574267982800
            __attrs_140574267982800 = _static_140574267997456

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li class="nav-item">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267985232
            __attrs_140574267985232 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267984912
            __default_140574267984912 = _DEFAULT_MARKER

            # <Value u'language_selector/template' (39:36)> -> __cache_140574267984208
            __token = 1508
            try:
                __zt_tmp = __attrs_140574267985232
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574267984208 = _static_140574397981968('path', u'language_selector/template', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'language_selector/template' (39:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ec710> -> __condition
            __expression = __cache_140574267984208

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div></div>')
            else:
                __content = __cache_140574267984208
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n      </li>\n\n      <!-- Search trigger -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4ec650> name=None at 7fd9ff4ecc90> -> __attrs_140574267982864
            __attrs_140574267982864 = _static_140574267983440

            # <Value u'personal_bar/user_name' (43:42)> -> __condition
            __token = 1628
            try:
                __zt_tmp = __attrs_140574267982864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'personal_bar/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item">\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4ecfd0> name=None at 7fd9ff4ec2d0> -> __attrs_140574275636432
                __attrs_140574275636432 = _static_140574267985872

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="nav-link"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275633616
                __default_140574275633616 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff4ec090> at 7fd9ff4ec610> -> __attr_title
                __attr_title = u'Press Ctrl+Space to trigger the Spotlight search'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275635920
                __default_140574275635920 = _DEFAULT_MARKER

                # <Substitution u'string:${portal_state/portal_url}/spotlight' (47:32)> -> __attr_href
                __token = 1816
                try:
                    __zt_tmp = __attrs_140574275636432
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('string', u'${portal_state/portal_url}/spotlight', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7fd9ffc38290> name=None at 7fd9ffc38150> -> __attrs_140574275634448
                __attrs_140574275634448 = _static_140574275633808

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-search"></i>\n        </a>\n      </li>')
            __append(u'\n\n      <!-- LIMS Setup -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc38050> name=None at 7fd9ffc382d0> -> __attrs_140574267989712
            __attrs_140574267989712 = _static_140574275633232

            # <Value u'view/is_manager' (53:42)> -> __condition
            __token = 1996
            try:
                __zt_tmp = __attrs_140574267989712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'view/is_manager', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item">\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4ed590> name=None at 7fd9ff4eda90> -> __attrs_140574267988240
                __attrs_140574267988240 = _static_140574267987344

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="nav-link"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267987856
                __default_140574267987856 = _DEFAULT_MARKER

                # <Substitution u'view/get_lims_setup_url' (55:32)> -> __attr_href
                __token = 2074
                try:
                    __zt_tmp = __attrs_140574267988240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('path', u'view/get_lims_setup_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267989008
                __attrs_140574267989008 = _static_140574442558096
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4e1890> name=None at 7fd9ff4e1250> -> __attrs_140574267940304
                __attrs_140574267940304 = _static_140574267938960

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-cog"></i>\n          \n        </a>\n      </li>')
            __append(u'\n\n      <!-- Personal Bar Menu -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4eddd0> name=None at 7fd9ff4ed4d0> -> __attrs_140574267937488
            __attrs_140574267937488 = _static_140574267989456

            # <Value u'personal_bar/user_name' (63:51)> -> __condition
            __token = 2300
            try:
                __zt_tmp = __attrs_140574267937488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'personal_bar/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item dropdown">\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4e1b10> name=None at 7fd9ff4e1850> -> __attrs_140574266103696
                __attrs_140574266103696 = _static_140574267939600

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267940624
                __default_140574267940624 = _DEFAULT_MARKER

                # <Substitution u'personal_bar/homelink_url' (71:32)> -> __attr_href
                __token = 2580
                try:
                    __zt_tmp = __attrs_140574266103696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('path', u'personal_bar/homelink_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u' class="nav-link dropdown-toggle" id="navbarUserDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266102736
                __attrs_140574266102736 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266105424
                __default_140574266105424 = _DEFAULT_MARKER

                # <Value u'personal_bar/user_name' (72:29)> -> __cache_140574266105680
                __token = 2637
                try:
                    __zt_tmp = __attrs_140574266102736
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574266105680 = _static_140574397981968('path', u'personal_bar/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'personal_bar/user_name' (72:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff321110> -> __condition
                __expression = __cache_140574266105680

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span />')
                else:
                    __content = __cache_140574266105680
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </a>\n        <!-- Personal Bar Dropdown Items -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff321e10> name=None at 7fd9ff321fd0> -> __attrs_140574266104464
                __attrs_140574266104464 = _static_140574266105360
                __backup_url_140574267998032 = get('url', __marker)

                # <Value u'view/context_state/current_page_url' (76:28)> -> __value
                __token = 2804
                try:
                    __zt_tmp = __attrs_140574266104464
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/context_state/current_page_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['url'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="dropdown-menu dropdown-menu-right">\n          ')

                # <Static value=<_ast.Dict object at 0x7fd9ff321c10> name=None at 7fd9ff321a50> -> __attrs_140574267901840
                __attrs_140574267901840 = _static_140574266104848
                __backup_action_140574257225232 = get('action', __marker)

                # <Value u'personal_bar/user_actions' (78:33)> -> __iterator
                __token = 2906
                try:
                    __zt_tmp = __attrs_140574267901840
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'personal_bar/user_actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574267900624, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="nav-item">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4d8650> name=None at 7fd9ff4d8e10> -> __attrs_140574267903248
                    __attrs_140574267903248 = _static_140574267901520
                    __backup_selected_140574267989392 = get('selected', __marker)

                    # <Value u"python:action['href'] == url" (80:36)> -> __value
                    __token = 2993
                    try:
                        __zt_tmp = __attrs_140574267903248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"action['href'] == url", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Value u'action' (81:31)> -> __cache_140574267900944
                    __token = 3054
                    try:
                        __zt_tmp = __attrs_140574267903248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267900944 = _static_140574397981968('path', u'action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if (u'href' not in __chain(__cache_140574267900944)):
                        __append(u' href=""')
                    __attr_140574267903824 = __cache_140574267900944
                    for (name, value, ) in __attr_140574267903824.items():
                        if ((name not in _static_140574284443792) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267903952
                    __default_140574267903952 = _DEFAULT_MARKER

                    # <Substitution u"python:selected and 'active nav-link' or 'nav-link'" (81:44)> -> __attr_class
                    __token = 3067
                    try:
                        __zt_tmp = __attrs_140574267903248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('python', u"selected and 'active nav-link' or 'nav-link'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267980048
                    __attrs_140574267980048 = _static_140574442558096

                    # <Value u"python:action['id'] == 'personaltools-site-setup'" (82:36)> -> __condition
                    __token = 3158
                    try:
                        __zt_tmp = __attrs_140574267980048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"action['id'] == 'personaltools-site-setup'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4eb6d0> name=None at 7fd9ff4ebc90> -> __attrs_140574267981520
                        __attrs_140574267981520 = _static_140574267979472

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<i class="fas fa-wrench"></i>\n              ')
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267978448
                    __attrs_140574267978448 = _static_140574442558096

                    # <Value u"python:action['id'] == 'personaltools-my-organization'" (85:45)> -> __condition
                    __token = 3328
                    try:
                        __zt_tmp = __attrs_140574267978448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"action['id'] == 'personaltools-my-organization'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4eb5d0> name=None at 7fd9ff4ebb10> -> __attrs_140574267980496
                        __attrs_140574267980496 = _static_140574267979216

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<i class="fas fa-building"></i>\n              ')
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267981264
                    __attrs_140574267981264 = _static_140574442558096

                    # <Value u"python:action['id'] == 'personaltools-logout'" (88:39)> -> __condition
                    __token = 3508
                    try:
                        __zt_tmp = __attrs_140574267981264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"action['id'] == 'personaltools-logout'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4ee550> name=None at 7fd9ff4ee510> -> __attrs_140574267991504
                        __attrs_140574267991504 = _static_140574267991376

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<i class="fas fa-sign-out-alt"></i>\n              ')
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267991568
                    __attrs_140574267991568 = _static_140574442558096

                    # <Value u"python:action['id'] == 'personaltools-user-profile'" (91:44)> -> __condition
                    __token = 3682
                    try:
                        __zt_tmp = __attrs_140574267991568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"action['id'] == 'personaltools-user-profile'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4eeb90> name=None at 7fd9ff4eea90> -> __attrs_140574267990672
                        __attrs_140574267990672 = _static_140574267992976

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<i class="fas fa-user-cog"></i>\n              ')
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267895184
                    __attrs_140574267895184 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267991632
                    __default_140574267991632 = _DEFAULT_MARKER

                    # <Value u'action/title' (94:43)> -> __cache_140574267992016
                    __token = 3862
                    try:
                        __zt_tmp = __attrs_140574267895184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267992016 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/title' (94:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ee450> -> __condition
                    __expression = __cache_140574267992016

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                action title\n              ')
                    else:
                        __content = __cache_140574267992016
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n            </a>')
                    if (__backup_selected_140574267989392 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140574267989392
                    __append(u'\n          </li>')
                    ____index_140574267900624 -= 1
                    if (____index_140574267900624 > 0):
                        __append('\n          ')
                if (__backup_action_140574257225232 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140574257225232
                __append(u'\n        </ul>')
                if (__backup_url_140574267998032 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_140574267998032
                __append(u'\n      </li>')
            __append(u'\n\n      <!-- Login/Register -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4d84d0> name=None at 7fd9ff321390> -> __attrs_140574267895632
            __attrs_140574267895632 = _static_140574267901136

            # <Value u'not:personal_bar/user_name' (103:42)> -> __condition
            __token = 4070
            try:
                __zt_tmp = __attrs_140574267895632
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('not', u'personal_bar/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item">\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267894160
                __attrs_140574267894160 = _static_140574442558096
                __backup_action_140574275649296 = get('action', __marker)

                # <Value u'personal_bar/user_actions' (104:56)> -> __iterator
                __token = 4155
                try:
                    __zt_tmp = __attrs_140574267894160
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'personal_bar/user_actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574267894992, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <Negate value=<Value u'python:1' (104:27)> at 7fd9ff4d68d0> -> __cache_140574267893968

                    # <Value u'python:1' (104:27)> -> __cache_140574267893968
                    __token = 4126
                    try:
                        __zt_tmp = __attrs_140574267894160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267893968 = _static_140574397981968('python', u'1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __cache_140574267893968 = not __cache_140574267893968
                    __condition = __cache_140574267893968
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4d65d0> name=None at 7fd9ff4d6a10> -> __attrs_140574268060304
                    __attrs_140574268060304 = _static_140574267893200

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267894864
                    __default_140574267894864 = _DEFAULT_MARKER

                    # <Substitution u'action/href' (105:42)> -> __attr_href
                    __token = 4225
                    try:
                        __zt_tmp = __attrs_140574268060304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'action/href', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267892112
                    __default_140574267892112 = _DEFAULT_MARKER

                    # <Substitution u'string:nav-link' (105:60)> -> __attr_class
                    __token = 4243
                    try:
                        __zt_tmp = __attrs_140574268060304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('string', u'nav-link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268059984
                    __attrs_140574268059984 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268063248
                    __default_140574268063248 = _DEFAULT_MARKER

                    # <Value u'action/title' (106:41)> -> __cache_140574268059728
                    __token = 4303
                    try:
                        __zt_tmp = __attrs_140574268059984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574268059728 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/title' (106:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4ff190> -> __condition
                    __expression = __cache_140574268059728

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              action title\n            ')
                    else:
                        __content = __cache_140574268059728
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268062544
                    __attrs_140574268062544 = _static_140574442558096

                    # <Value u"python:action['id'] == 'personaltools-logout'" (109:37)> -> __condition
                    __token = 4412
                    try:
                        __zt_tmp = __attrs_140574268062544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u"action['id'] == 'personaltools-logout'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4e0dd0> name=None at 7fd9feaa1ad0> -> __attrs_140574257314128
                        __attrs_140574257314128 = _static_140574267936208

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="icon-logout"></span>\n            ')
                    __append(u'\n          </a>\n        ')
                    __condition = __cache_140574267893968
                    if __condition:
                        __append(u'</div>')
                    ____index_140574267894992 -= 1
                    if (____index_140574267894992 > 0):
                        __append('\n        ')
                if (__backup_action_140574275649296 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140574275649296
                __append(u'\n      </li>')
            __append(u'\n\n    </ul>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_140574275647504
            if (__backup_personal_bar_140574267889680 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_140574267889680
            if (__backup_language_selector_140574267891280 is __marker):
                del econtext['language_selector']
            else:
                econtext['language_selector'] = __backup_language_selector_140574267891280
            if (__backup_global_sections_140574267890576 is __marker):
                del econtext['global_sections']
            else:
                econtext['global_sections'] = __backup_global_sections_140574267890576
            if (__backup_portal_state_140574257170512 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140574257170512
            if (__backup_context_state_140574284482128 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140574284482128
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }