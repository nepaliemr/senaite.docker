# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/quickinstaller/templates/quickinstaller.pt'

__tokens = {478: (u'string:$portal_url/@@overview-controlpanel', 15, 30), 958: (u'view/get_upgrades', 32, 38), 1018: (u' python:len(products', 33, 41), 1073: (u'python:num_products>0', 34, 32), 1262: (u'not:products', 37, 34), 1633: (u'products', 43, 57), 1729: (u'products', 45, 49), 1776: (u'product/id', 46, 36), 2028: (u'pid', 50, 49), 2323: (u'string:Upgrade ${pid}', 56, 49), 2437: (u'product/title', 59, 39), 2662: (u'product/description', 64, 45), 2696: (u'product/description', 64, 79), 2829: (u'pid', 65, 64), 2876: (u'product/version', 65, 111), 3059: (u'product/upgrade_info', 68, 70), 3256: (u'not:upgrade_info/hasProfile', 72, 43), 3446: (u'upgrade_info/installedVersion', 74, 81), 3568: (u'upgrade_info/hasProfile', 76, 43), 3779: (u'upgrade_info/installedVersion', 78, 91), 4048: (u'upgrade_info/newVersion', 81, 90), 4200: (u'not:upgrade_info/available', 85, 42), 4740: (u'python:num_products > 1', 96, 33), 4882: (u'products', 98, 53), 5062: (u'product/id', 101, 49), 5734: (u'view/get_available', 119, 38), 5795: (u' python:len(products', 120, 41), 5850: (u'python:num_products>0', 121, 32), 6131: (u'products', 126, 38), 6183: (u'product/id', 127, 41), 6421: (u'pid', 131, 49), 6748: (u'product/title', 140, 39), 6973: (u'product/description', 145, 45), 7085: (u'product/description', 147, 43), 7200: (u'pid', 148, 64), 7247: (u'product/version', 148, 111), 7429: (u'not:product/uninstall_profile', 152, 37), 7829: (u'view/get_installed', 164, 38), 7890: (u' python:len(products', 165, 41), 8173: (u'products', 170, 38), 8225: (u'product/id', 171, 41), 8467: (u'pid', 175, 49), 8700: (u'product/uninstall_profile', 180, 42), 8868: (u'product/title', 184, 39), 9093: (u'product/description', 189, 45), 9205: (u'product/description', 191, 43), 9320: (u'pid', 192, 64), 9367: (u'product/version', 192, 111), 9959: (u'view/get_broken', 208, 38), 10017: (u' python:len(products', 209, 41), 10073: (u'num_products', 210, 32), 10341: (u'products', 215, 38), 10410: (u'product/product_id', 217, 37), 10624: (u'product/type', 222, 37), 10739: (u'product/value', 223, 65), 261: (u'context/prefs_main_template/macros/master', 6, 23), 261: (u'context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140574272095184 = u'master'
_static_140574284438608 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'product', }
_static_140574284434896 = {u'type': u'hidden', u'name': u'install_product', u'value': u'pid', }
_static_140574266143696 = {u'class': u'configlets', }
_static_140574270663120 = {u'class': u'portletContent', }
_static_140574267453904 = {u'class': u'documentDescription', }
_static_140574267404112 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'pid', }
_static_140574284495632 = {u'class': u'configlets', }
_static_140574284377744 = {u'class': u'portletContent', }
_static_140574255002320 = {u'class': u'configletDescription discreet', }
_static_140574397981968 = __compile_zt_expr
_static_140574256080784 = {u'class': u'portletContent', }
_static_140574270466576 = {u'class': u'text-primary', }
_static_140574255040656 = {u'type': u'submit', u'class': u'destructive', u'value': u'Uninstall', u'name': u'form.submitted', }
_static_140574268022544 = {u'class': u'portletHeader', }
_static_140574270568528 = {u'class': u'configlets', }
_static_140574256082064 = {u'role': u'status', u'id': u'up-to-date-message', u'class': u'portalMessage info', }
_static_140574255111184 = {u'class': u'configletDetails p-0 m-0', }
_static_140574442558096 = {}
_static_140574270172688 = {u'class': u'portletHeader', }
_static_140574256082768 = {u'class': u'portletHeader', }
_static_140574267399184 = {u'type': u'submit', u'class': u'standalone', u'value': u'Upgrade ${pid}', u'name': u'form.submitted', }
_static_140574284434576 = {u'type': u'submit', u'class': u'context', u'value': u'Install', u'name': u'form.submitted', }
_static_140574267401360 = {u'action': u'upgrade_products', u'method': u'post', u'class': u'float-right', }
_static_140574255063312 = {u'class': u'discreet', }
_static_140574268006288 = {u'type': u'submit', u'class': u'context', u'value': u'Upgrade them ALL!', u'name': u'form.submitted', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574270571152 = {u'class': u'discreet', }
_static_140574267456784 = {u'id': u'content-core', }
_static_140574266144720 = {u'id': u'activated-products', u'class': u'portlet', }
_static_140574267402448 = {u'class': u'configletDescription discreet', }
_static_140574272096592 = {u'href': u'string:$portal_url/@@overview-controlpanel', u'id': u'setup-link', u'class': u'link-parent', }
_static_140574267429456 = {u'class': u'configlets', }
_static_140574255078224 = {u'class': u'configletDescription discreet', }
_static_140574255003536 = {u'type': u'hidden', u'name': u'uninstall_product', u'value': u'pid', }
_static_140574269036688 = {u'id': u'upgrade-products', u'class': u'portlet', }
_static_140574255174992 = {u'class': u'portletContent', }
_static_140574255011152 = {u'action': u'upgrade_products', u'method': u'post', }
_static_140574270661968 = {u'class': u'portletHeader', }
_static_140574270372816 = {u'action': u'install_products', u'method': u'post', u'class': u'float-right', }
_static_140574268935184 = {u'class': u'discreet', }
_static_140574255001808 = {u'action': u'uninstall_products', u'method': u'post', u'class': u'float-right', }
_static_140574255003408 = {u'id': u'broken-products', u'class': u'portlet', }
_static_140574270600272 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140574257254352 = {u'class': u'portletContent', }
_static_140574267328976 = {u'class': u'configletDescription discreet', }
_static_140574267456144 = {u'class': u'documentFirstHeading', }
_static_140574270603088 = {u'class': u'discreet', }
_static_140574267432016 = {u'id': u'install-products', u'class': u'portlet', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574272097872
            __attrs_140574272097872 = _static_140574442558096
            __backup_macroname_140574270520688 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fd9ff8d83d0> name=None at 7fd9ff8d8a50> -> __value
            __value = _static_140574272095184
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574272096144
                __attrs_140574272096144 = _static_140574442558096
                __previous_i18n_domain_140574272098000 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff8d8950> name=None at 7fd9ff8d8bd0> -> __attrs_140574267454096
                __attrs_140574267454096 = _static_140574272096592

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a id="setup-link" class="link-parent"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267454800
                __default_140574267454800 = _DEFAULT_MARKER

                # <Substitution u'string:$portal_url/@@overview-controlpanel' (15:30)> -> __attr_href
                __token = 478
                try:
                    __zt_tmp = __attrs_140574267454096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140574397981968('string', u'$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')
                __stream_140574272096272 = []
                __append_140574272096272 = __stream_140574272096272.append
                __append_140574272096272(u'\n        Site Setup\n      ')
                __msgid_140574272096272 = __re_whitespace(''.join(__stream_140574272096272)).strip()
                if __msgid_140574272096272:
                    __append(translate(__msgid_140574272096272, mapping=None, default=__msgid_140574272096272, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff46ba90> name=None at 7fd9ff46b790> -> __attrs_140574267453584
                __attrs_140574267453584 = _static_140574267456144

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140574267454736 = []
                __append_140574267454736 = __stream_140574267454736.append
                __append_140574267454736(u'Add-ons')
                __msgid_140574267454736 = __re_whitespace(''.join(__stream_140574267454736)).strip()
                if __msgid_140574267454736:
                    __append(translate(__msgid_140574267454736, mapping=None, default=__msgid_140574267454736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff46b1d0> name=None at 7fd9ff46bad0> -> __attrs_140574267455056
                __attrs_140574267455056 = _static_140574267453904

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentDescription">')
                __stream_140574267456336 = []
                __append_140574267456336 = __stream_140574267456336.append
                __append_140574267456336(u'\n        This is the Add-on configuration section, you can activate and deactivate\n        add-ons in the lists below.\n      ')
                __msgid_140574267456336 = __re_whitespace(''.join(__stream_140574267456336)).strip()
                if __msgid_140574267456336:
                    __append(translate(__msgid_140574267456336, mapping=None, default=__msgid_140574267456336, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff46bd10> name=None at 7fd9ff46b3d0> -> __attrs_140574267455888
                __attrs_140574267455888 = _static_140574267456784

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="content-core">\n\n        <!-- UPGRADES -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff5ed890> name=None at 7fd9ff5ed650> -> __attrs_140574269035280
                __attrs_140574269035280 = _static_140574269036688
                __backup_products_140574272094928 = get('products', __marker)

                # <Value u'view/get_upgrades' (32:38)> -> __value
                __token = 958
                try:
                    __zt_tmp = __attrs_140574269035280
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/get_upgrades', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140574272095632 = get('num_products', __marker)

                # <Value u'python:len(products)' (33:41)> -> __value
                __token = 1018
                try:
                    __zt_tmp = __attrs_140574269035280
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'len(products)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value u'python:num_products>0' (34:32)> -> __condition
                __token = 1073
                try:
                    __zt_tmp = __attrs_140574269035280
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'num_products>0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section id="upgrade-products" class="portlet">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe992f50> name=None at 7fd9fe992650> -> __attrs_140574256079824
                    __attrs_140574256079824 = _static_140574256082768

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header class="portletHeader">')
                    __stream_140574269036496 = []
                    __append_140574269036496 = __stream_140574269036496.append
                    __append_140574269036496(u'Upgrades')
                    __msgid_140574269036496 = __re_whitespace(''.join(__stream_140574269036496)).strip()
                    if __msgid_140574269036496:
                        __append(translate(__msgid_140574269036496, mapping=None, default=__msgid_140574269036496, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</header>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe992790> name=None at 7fd9fe992990> -> __attrs_140574256081232
                    __attrs_140574256081232 = _static_140574256080784

                    # <Value u'not:products' (37:34)> -> __condition
                    __token = 1262
                    try:
                        __zt_tmp = __attrs_140574256081232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('not', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<section class="portletContent">\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9fe992c90> name=None at 7fd9fe992dd0> -> __attrs_140574255174032
                        __attrs_140574255174032 = _static_140574256082064

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div id="up-to-date-message" class="portalMessage info" role="status">\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255177616
                        __attrs_140574255177616 = _static_140574442558096

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<strong>')
                        __stream_140574255174544 = []
                        __append_140574255174544 = __stream_140574255174544.append
                        __append_140574255174544(u'No upgrades in this corner')
                        __msgid_140574255174544 = __re_whitespace(''.join(__stream_140574255174544)).strip()
                        if __msgid_140574255174544:
                            __append(translate(__msgid_140574255174544, mapping=None, default=__msgid_140574255174544, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</strong>\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255175632
                        __attrs_140574255175632 = _static_140574442558096

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140574255176528 = []
                        __append_140574255176528 = __stream_140574255176528.append
                        __append_140574255176528(u'You are up to date. High fives.')
                        __msgid_140574255176528 = __re_whitespace(''.join(__stream_140574255176528)).strip()
                        if __msgid_140574255176528:
                            __append(translate(__msgid_140574255176528, mapping=None, default=__msgid_140574255176528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n            </div>\n          </section>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe8b5550> name=None at 7fd9fe8b5a90> -> __attrs_140574255174288
                    __attrs_140574255174288 = _static_140574255174992

                    # <Value u'products' (43:57)> -> __condition
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_140574255174288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<section class="portletContent">\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff465250> name=None at 7fd9ff4656d0> -> __attrs_140574267431184
                        __attrs_140574267431184 = _static_140574267429456

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul class="configlets">\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267432912
                        __attrs_140574267432912 = _static_140574442558096
                        __backup_product_140574256082320 = get('product', __marker)

                        # <Value u'products' (45:49)> -> __iterator
                        __token = 1729
                        try:
                            __zt_tmp = __attrs_140574267432912
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574267430096, ) = getitem('repeat')(u'product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append(u'\n                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267430416
                            __attrs_140574267430416 = _static_140574442558096
                            __backup_pid_140574255174736 = get('pid', __marker)

                            # <Value u'product/id' (46:36)> -> __value
                            __token = 1776
                            try:
                                __zt_tmp = __attrs_140574267430416
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('path', u'product/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['pid'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff45e490> name=None at 7fd9ff45e090> -> __attrs_140574267403728
                            __attrs_140574267403728 = _static_140574267401360

                            # <form ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<form action="upgrade_products" method="post" class="float-right">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff45ef50> name=None at 7fd9ff45e390> -> __attrs_140574267396752
                            __attrs_140574267396752 = _static_140574267404112

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="hidden" name="prefs_reinstallProducts:list"')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267402192
                            __default_140574267402192 = _DEFAULT_MARKER

                            # <Substitution u'pid' (50:49)> -> __attr_value
                            __token = 2028
                            try:
                                __zt_tmp = __attrs_140574267396752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' />\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff45dc10> name=None at 7fd9ff45dd50> -> __attrs_140574267398672
                            __attrs_140574267398672 = _static_140574267399184

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input class="standalone" type="submit"')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267397648
                            __default_140574267397648 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<Substitution u'string:Upgrade ${pid}' (56:49)> at 7fd9ff45d750> -> __attr_value

                            # <Substitution u'string:Upgrade ${pid}' (56:49)> -> __attr_value
                            __token = 2323
                            try:
                                __zt_tmp = __attrs_140574267398672
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140574397981968('string', u'Upgrade ${pid}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', u'Upgrade ${pid}', _DEFAULT_MARKER)
                            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' name="form.submitted"/>\n                  </form>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267398992
                            __attrs_140574267398992 = _static_140574442558096

                            # <h5 ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<h5>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255064144
                            __attrs_140574255064144 = _static_140574442558096

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255066320
                            __default_140574255066320 = _DEFAULT_MARKER

                            # <Value u'product/title' (59:39)> -> __cache_140574267397776
                            __token = 2437
                            try:
                                __zt_tmp = __attrs_140574255064144
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574267397776 = _static_140574397981968('path', u'product/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'product/title' (59:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe89a910> -> __condition
                            __expression = __cache_140574267397776

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>\n                      Add-on Name\n                    </span>')
                            else:
                                __content = __cache_140574267397776
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'\n                  </h5>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff45e8d0> name=None at 7fd9ff45e410> -> __attrs_140574255063888
                            __attrs_140574255063888 = _static_140574267402448

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<p class="configletDescription discreet">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255066512
                            __attrs_140574255066512 = _static_140574442558096

                            # <Value u'product/description' (64:45)> -> __condition
                            __token = 2662
                            try:
                                __zt_tmp = __attrs_140574255066512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255066704
                                __default_140574255066704 = _DEFAULT_MARKER

                                # <Value u'product/description' (64:79)> -> __cache_140574255063760
                                __token = 2696
                                try:
                                    __zt_tmp = __attrs_140574255066512
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574255063760 = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'product/description' (64:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe89aad0> -> __condition
                                __expression = __cache_140574255063760

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'add-on description')
                                else:
                                    __content = __cache_140574255063760
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9fe89a110> name=None at 7fd9fe89add0> -> __attrs_140574255108176
                            __attrs_140574255108176 = _static_140574255063312

                            # <em ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<em class="discreet"> \u2013 (')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255111696
                            __attrs_140574255111696 = _static_140574442558096

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255109328
                            __default_140574255109328 = _DEFAULT_MARKER

                            # <Value u'pid' (65:64)> -> __cache_140574255110288
                            __token = 2829
                            try:
                                __zt_tmp = __attrs_140574255111696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574255110288 = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'pid' (65:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe8a52d0> -> __condition
                            __expression = __cache_140574255110288

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>plugin.app.name</span>')
                            else:
                                __content = __cache_140574255110288
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u' ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255109776
                            __attrs_140574255109776 = _static_140574442558096

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255109648
                            __default_140574255109648 = _DEFAULT_MARKER

                            # <Value u'product/version' (65:111)> -> __cache_140574255111312
                            __token = 2876
                            try:
                                __zt_tmp = __attrs_140574255109776
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574255111312 = _static_140574397981968('path', u'product/version', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'product/version' (65:111)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe8a5490> -> __condition
                            __expression = __cache_140574255111312

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>1.0</span>')
                            else:
                                __content = __cache_140574255111312
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u')</em>\n                  </p>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9fe8a5c10> name=None at 7fd9fe89a650> -> __attrs_140574255111440
                            __attrs_140574255111440 = _static_140574255111184

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<ul class="configletDetails p-0 m-0">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff74aa10> name=None at 7fd9ff74a810> -> __attrs_140574270465616
                            __attrs_140574270465616 = _static_140574270466576
                            __backup_upgrade_info_140574267404240 = get('upgrade_info', __marker)

                            # <Value u'product/upgrade_info' (68:70)> -> __value
                            __token = 3059
                            try:
                                __zt_tmp = __attrs_140574270465616
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('path', u'product/upgrade_info', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['upgrade_info'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li class="text-primary">\n                      ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270466192
                            __attrs_140574270466192 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574270464336 = []
                            __append_140574270464336 = __stream_140574270464336.append
                            __append_140574270464336(u'\n                        This addon has been upgraded.\n                      ')
                            __msgid_140574270464336 = __re_whitespace(''.join(__stream_140574270464336)).strip()
                            if __msgid_140574270464336:
                                __append(translate(__msgid_140574270464336, mapping=None, default=__msgid_140574270464336, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                      ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257194000
                            __attrs_140574257194000 = _static_140574442558096

                            # <Value u'not:upgrade_info/hasProfile' (72:43)> -> __condition
                            __token = 3256
                            try:
                                __zt_tmp = __attrs_140574257194000
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u'upgrade_info/hasProfile', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')
                                __stream_140574270607920_version = ''
                                __stream_140574257193104 = []
                                __append_140574257193104 = __stream_140574257193104.append
                                __append_140574257193104(u'\n                        Old version was ')
                                __stream_140574270607920_version = []
                                __append_140574270607920_version = __stream_140574270607920_version.append

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267880592
                                __attrs_140574267880592 = _static_140574442558096

                                # <strong ... (0:0)
                                # --------------------------------------------------------
                                __append_140574270607920_version(u'<strong>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267881488
                                __default_140574267881488 = _DEFAULT_MARKER

                                # <Value u'upgrade_info/installedVersion' (74:81)> -> __cache_140574267879888
                                __token = 3446
                                try:
                                    __zt_tmp = __attrs_140574267880592
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574267879888 = _static_140574397981968('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'upgrade_info/installedVersion' (74:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d34d0> -> __condition
                                __expression = __cache_140574267879888

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append_140574270607920_version(u'version')
                                else:
                                    __content = __cache_140574267879888
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append_140574270607920_version(__content)
                                __append_140574270607920_version(u'</strong>')
                                __append_140574257193104(u'${version}')
                                __stream_140574270607920_version = ''.join(__stream_140574270607920_version)
                                __append_140574257193104(u'.\n                      ')
                                __msgid_140574257193104 = __re_whitespace(''.join(__stream_140574257193104)).strip()
                                if u'label_product_upgrade_old_version':
                                    __append(translate(u'label_product_upgrade_old_version', mapping={u'version': __stream_140574270607920_version, }, default=__msgid_140574257193104, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</span>')
                            __append(u'\n                      ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270444304
                            __attrs_140574270444304 = _static_140574442558096

                            # <Value u'upgrade_info/hasProfile' (76:43)> -> __condition
                            __token = 3568
                            try:
                                __zt_tmp = __attrs_140574270444304
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'upgrade_info/hasProfile', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>\n                        ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267489808
                                __attrs_140574267489808 = _static_140574442558096
                                __stream_140574270608160_version = ''
                                __stream_140574267490256 = []
                                __append_140574267490256 = __stream_140574267490256.append
                                __append_140574267490256(u'\n                          Old profile version was ')
                                __stream_140574270608160_version = []
                                __append_140574270608160_version = __stream_140574270608160_version.append

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267489680
                                __attrs_140574267489680 = _static_140574442558096

                                # <strong ... (0:0)
                                # --------------------------------------------------------
                                __append_140574270608160_version(u'<strong>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267487184
                                __default_140574267487184 = _DEFAULT_MARKER

                                # <Value u'upgrade_info/installedVersion' (78:91)> -> __cache_140574267489424
                                __token = 3779
                                try:
                                    __zt_tmp = __attrs_140574267489680
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574267489424 = _static_140574397981968('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'upgrade_info/installedVersion' (78:91)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff473510> -> __condition
                                __expression = __cache_140574267489424

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append_140574270608160_version(u'version')
                                else:
                                    __content = __cache_140574267489424
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append_140574270608160_version(__content)
                                __append_140574270608160_version(u'</strong>')
                                __append_140574267490256(u'${version}')
                                __stream_140574270608160_version = ''.join(__stream_140574270608160_version)
                                __append_140574267490256(u'.\n                        ')
                                __msgid_140574267490256 = __re_whitespace(''.join(__stream_140574267490256)).strip()
                                if u'label_product_upgrade_old_profile_version':
                                    __append(translate(u'label_product_upgrade_old_profile_version', mapping={u'version': __stream_140574270608160_version, }, default=__msgid_140574267490256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'\n                        ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267486800
                                __attrs_140574267486800 = _static_140574442558096
                                __stream_140574270608160_version = ''
                                __stream_140574267488080 = []
                                __append_140574267488080 = __stream_140574267488080.append
                                __append_140574267488080(u'\n                          New profile version is ')
                                __stream_140574270608160_version = []
                                __append_140574270608160_version = __stream_140574270608160_version.append

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270345296
                                __attrs_140574270345296 = _static_140574442558096

                                # <strong ... (0:0)
                                # --------------------------------------------------------
                                __append_140574270608160_version(u'<strong>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270346960
                                __default_140574270346960 = _DEFAULT_MARKER

                                # <Value u'upgrade_info/newVersion' (81:90)> -> __cache_140574270348624
                                __token = 4048
                                try:
                                    __zt_tmp = __attrs_140574270345296
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574270348624 = _static_140574397981968('path', u'upgrade_info/newVersion', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'upgrade_info/newVersion' (81:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff72de50> -> __condition
                                __expression = __cache_140574270348624

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append_140574270608160_version(u'version')
                                else:
                                    __content = __cache_140574270348624
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append_140574270608160_version(__content)
                                __append_140574270608160_version(u'</strong>')
                                __append_140574267488080(u'${version}')
                                __stream_140574270608160_version = ''.join(__stream_140574270608160_version)
                                __append_140574267488080(u'.\n                        ')
                                __msgid_140574267488080 = __re_whitespace(''.join(__stream_140574267488080)).strip()
                                if u'label_product_upgrade_new_profile_version':
                                    __append(translate(u'label_product_upgrade_new_profile_version', mapping={u'version': __stream_140574270608160_version, }, default=__msgid_140574267488080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'\n                      </span>')
                            __append(u'\n\n                      ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267488208
                            __attrs_140574267488208 = _static_140574442558096

                            # <Value u'not:upgrade_info/available' (85:42)> -> __condition
                            __token = 4200
                            try:
                                __zt_tmp = __attrs_140574267488208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u'upgrade_info/available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div>\n                        ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255009872
                                __attrs_140574255009872 = _static_140574442558096

                                # <strong ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<strong>')
                                __stream_140574255010896 = []
                                __append_140574255010896 = __stream_140574255010896.append
                                __append_140574255010896(u'Warning')
                                __msgid_140574255010896 = __re_whitespace(''.join(__stream_140574255010896)).strip()
                                if __msgid_140574255010896:
                                    __append(translate(__msgid_140574255010896, mapping=None, default=__msgid_140574255010896, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</strong>\n                        ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255011664
                                __attrs_140574255011664 = _static_140574442558096

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')
                                __stream_140574255012816 = []
                                __append_140574255012816 = __stream_140574255012816.append
                                __append_140574255012816(u'There is no upgrade procedure defined for this\n                          addon. Please consult the addon documentation\n                          for upgrade information, or contact the addon\n                          author.')
                                __msgid_140574255012816 = __re_whitespace(''.join(__stream_140574255012816)).strip()
                                if __msgid_140574255012816:
                                    __append(translate(__msgid_140574255012816, mapping=None, default=__msgid_140574255012816, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</span>\n                      </div>')
                            __append(u'\n                    </li>')
                            if (__backup_upgrade_info_140574267404240 is __marker):
                                del econtext['upgrade_info']
                            else:
                                econtext['upgrade_info'] = __backup_upgrade_info_140574267404240
                            __append(u'\n                  </ul>\n                </li>')
                            if (__backup_pid_140574255174736 is __marker):
                                del econtext['pid']
                            else:
                                econtext['pid'] = __backup_pid_140574255174736
                            __append(u'\n              ')
                            ____index_140574267430096 -= 1
                            if (____index_140574267430096 > 0):
                                __append('')
                        if (__backup_product_140574256082320 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_140574256082320
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255066192
                        __attrs_140574255066192 = _static_140574442558096

                        # <Value u'python:num_products > 1' (96:33)> -> __condition
                        __token = 4740
                        try:
                            __zt_tmp = __attrs_140574255066192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('python', u'num_products > 1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li>\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9fe88d550> name=None at 7fd9fe88dc50> -> __attrs_140574255013328
                            __attrs_140574255013328 = _static_140574255011152

                            # <form ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<form action="upgrade_products" method="post">\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255010512
                            __attrs_140574255010512 = _static_140574442558096
                            __backup_product_140574267428944 = get('product', __marker)

                            # <Value u'products' (98:53)> -> __iterator
                            __token = 4882
                            try:
                                __zt_tmp = __attrs_140574255010512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            (__iterator, ____index_140574255012176, ) = getitem('repeat')(u'product', __iterator)
                            econtext['product'] = None
                            for __item in __iterator:
                                econtext['product'] = __item
                                __append(u'\n                    ')

                                # <Static value=<_ast.Dict object at 0x7fda0049dc50> name=None at 7fd9fe88dfd0> -> __attrs_140574270401552
                                __attrs_140574270401552 = _static_140574284438608

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input type="hidden"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270401744
                                __default_140574270401744 = _DEFAULT_MARKER

                                # <Substitution u'product/id' (101:49)> -> __attr_value
                                __token = 5062
                                try:
                                    __zt_tmp = __attrs_140574270401552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_value = _static_140574397981968('path', u'product/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_value = __quote(__attr_value, '"', '&quot;', u'product', _DEFAULT_MARKER)
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' name="prefs_reinstallProducts:list" />\n                  ')
                                ____index_140574255012176 -= 1
                                if (____index_140574255012176 > 0):
                                    __append('')
                            if (__backup_product_140574267428944 is __marker):
                                del econtext['product']
                            else:
                                econtext['product'] = __backup_product_140574267428944
                            __append(u'\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270401232
                            __attrs_140574270401232 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270400208
                            __attrs_140574270400208 = _static_140574442558096

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>')
                            __stream_140574270400784 = []
                            __append_140574270400784 = __stream_140574270400784.append
                            __append_140574270400784(u'This can be risky, are you sure you want to do this?')
                            __msgid_140574270400784 = __re_whitespace(''.join(__stream_140574270400784)).strip()
                            if u'label_product_upgrade_all_action':
                                __append(translate(u'label_product_upgrade_all_action', mapping=None, default=__msgid_140574270400784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</div>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff4f1f90> name=None at 7fd9ff4f1ed0> -> __attrs_140574270208784
                            __attrs_140574270208784 = _static_140574268006288

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input class="context" type="submit"')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268004944
                            __default_140574268004944 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff4f1250> at 7fd9ff4f14d0> -> __attr_value
                            __attr_value = u'Upgrade them ALL!'
                            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' name="form.submitted" />\n                  </span>\n                </form>\n              </li>')
                        __append(u'\n            </ul>\n          </section>')
                    __append(u'\n        </section>')
                if (__backup_num_products_140574272095632 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140574272095632
                if (__backup_products_140574272094928 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140574272094928
                __append(u'\n        <!-- /UPGRADES -->\n\n        <!-- INSTALLABLE -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff465c50> name=None at 7fd9ff465c10> -> __attrs_140574255168592
                __attrs_140574255168592 = _static_140574267432016
                __backup_products_140574267455120 = get('products', __marker)

                # <Value u'view/get_available' (119:38)> -> __value
                __token = 5734
                try:
                    __zt_tmp = __attrs_140574255168592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/get_available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140574269034896 = get('num_products', __marker)

                # <Value u'python:len(products)' (120:41)> -> __value
                __token = 5795
                try:
                    __zt_tmp = __attrs_140574255168592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'len(products)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value u'python:num_products>0' (121:32)> -> __condition
                __token = 5850
                try:
                    __zt_tmp = __attrs_140574255168592
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'num_products>0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section id="install-products" class="portlet">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff702e10> name=None at 7fd9ff702f50> -> __attrs_140574284374544
                    __attrs_140574284374544 = _static_140574270172688

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header class="portletHeader">')
                    __stream_140574270172176 = []
                    __append_140574270172176 = __stream_140574270172176.append
                    __append_140574270172176(u'Available add-ons')
                    __msgid_140574270172176 = __re_whitespace(''.join(__stream_140574270172176)).strip()
                    if __msgid_140574270172176:
                        __append(translate(__msgid_140574270172176, mapping=None, default=__msgid_140574270172176, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</header>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda0048ee90> name=None at 7fda0048eb10> -> __attrs_140574266145936
                    __attrs_140574266145936 = _static_140574284377744

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff32b3d0> name=None at 7fd9ff32b4d0> -> __attrs_140574266145872
                    __attrs_140574266145872 = _static_140574266143696

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270373840
                    __attrs_140574270373840 = _static_140574442558096
                    __backup_product_140574255176464 = get('product', __marker)

                    # <Value u'products' (126:38)> -> __iterator
                    __token = 6131
                    try:
                        __zt_tmp = __attrs_140574270373840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574270370320, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270373776
                        __attrs_140574270373776 = _static_140574442558096
                        __backup_pid_140574255177168 = get('pid', __marker)

                        # <Value u'product/id' (127:41)> -> __value
                        __token = 6183
                        try:
                            __zt_tmp = __attrs_140574270373776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('path', u'product/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['pid'] = __value
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff733bd0> name=None at 7fd9ff733b50> -> __attrs_140574284432528
                        __attrs_140574284432528 = _static_140574270372816

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<form action="install_products" method="post" class="float-right">\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fda0049cdd0> name=None at 7fda0049cc50> -> __attrs_140574284433424
                        __attrs_140574284433424 = _static_140574284434896

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden" name="install_product"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284432016
                        __default_140574284432016 = _DEFAULT_MARKER

                        # <Substitution u'pid' (131:49)> -> __attr_value
                        __token = 6421
                        try:
                            __zt_tmp = __attrs_140574284433424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' />\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fda0049cc90> name=None at 7fda0049c390> -> __attrs_140574267328272
                        __attrs_140574267328272 = _static_140574284434576

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="context" type="submit"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267329808
                        __default_140574267329808 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff44cad0> at 7fd9ff44c2d0> -> __attr_value
                        __attr_value = u'Install'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>\n                  </form>\n\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267328080
                        __attrs_140574267328080 = _static_140574442558096

                        # <h5 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h5>\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267326672
                        __attrs_140574267326672 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267330448
                        __default_140574267330448 = _DEFAULT_MARKER

                        # <Value u'product/title' (140:39)> -> __cache_140574267330064
                        __token = 6748
                        try:
                            __zt_tmp = __attrs_140574267326672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574267330064 = _static_140574397981968('path', u'product/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/title' (140:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff44c250> -> __condition
                        __expression = __cache_140574267330064

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                      Add-on Name\n                    </span>')
                        else:
                            __content = __cache_140574267330064
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                  </h5>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff44c9d0> name=None at 7fd9ff44cb10> -> __attrs_140574270602768
                        __attrs_140574270602768 = _static_140574267328976

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270601808
                        __attrs_140574270601808 = _static_140574442558096

                        # <Value u'product/description' (145:45)> -> __condition
                        __token = 6973
                        try:
                            __zt_tmp = __attrs_140574270601808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270599760
                            __default_140574270599760 = _DEFAULT_MARKER

                            # <Value u'product/description' (147:43)> -> __cache_140574270600976
                            __token = 7085
                            try:
                                __zt_tmp = __attrs_140574270601808
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574270600976 = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'product/description' (147:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff76b090> -> __condition
                            __expression = __cache_140574270600976

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'add-on description')
                            else:
                                __content = __cache_140574270600976
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff76bf50> name=None at 7fd9ff76bb50> -> __attrs_140574270602384
                        __attrs_140574270602384 = _static_140574270603088

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> \u2013 (')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270612624
                        __attrs_140574270612624 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270614544
                        __default_140574270614544 = _DEFAULT_MARKER

                        # <Value u'pid' (148:64)> -> __cache_140574270615440
                        __token = 7200
                        try:
                            __zt_tmp = __attrs_140574270612624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270615440 = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'pid' (148:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff76e110> -> __condition
                        __expression = __cache_140574270615440

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>plugin.app.name</span>')
                        else:
                            __content = __cache_140574270615440
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u' ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270615504
                        __attrs_140574270615504 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270614928
                        __default_140574270614928 = _DEFAULT_MARKER

                        # <Value u'product/version' (148:111)> -> __cache_140574270614992
                        __token = 7247
                        try:
                            __zt_tmp = __attrs_140574270615504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270614992 = _static_140574397981968('path', u'product/version', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/version' (148:111)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff76e050> -> __condition
                        __expression = __cache_140574270614992

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>1.0</span>')
                        else:
                            __content = __cache_140574270614992
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u')</em>\n                  </p>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff76b450> name=None at 7fd9ff76b790> -> __attrs_140574270611664
                        __attrs_140574270611664 = _static_140574270600272

                        # <Value u'not:product/uninstall_profile' (152:37)> -> __condition
                        __token = 7429
                        try:
                            __zt_tmp = __attrs_140574270611664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('not', u'product/uninstall_profile', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <dl ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<dl class="portalMessage warning" role="status">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270664080
                            __attrs_140574270664080 = _static_140574442558096

                            # <dt ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<dt>')
                            __stream_140574270662736 = []
                            __append_140574270662736 = __stream_140574270662736.append
                            __append_140574270662736(u'Warning')
                            __msgid_140574270662736 = __re_whitespace(''.join(__stream_140574270662736)).strip()
                            if __msgid_140574270662736:
                                __append(translate(__msgid_140574270662736, mapping=None, default=__msgid_140574270662736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</dt>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270662032
                            __attrs_140574270662032 = _static_140574442558096

                            # <dd ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<dd>')
                            __stream_140574270661072 = []
                            __append_140574270661072 = __stream_140574270661072.append
                            __append_140574270661072(u'This product cannot be uninstalled!')
                            __msgid_140574270661072 = __re_whitespace(''.join(__stream_140574270661072)).strip()
                            if __msgid_140574270661072:
                                __append(translate(__msgid_140574270661072, mapping=None, default=__msgid_140574270661072, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</dd>\n                  </dl>')
                        __append(u'\n                ')
                        if (__backup_pid_140574255177168 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_140574255177168
                        __append(u'\n              </li>')
                        ____index_140574270370320 -= 1
                        if (____index_140574270370320 > 0):
                            __append('\n              ')
                    if (__backup_product_140574255176464 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140574255176464
                    __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140574269034896 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140574269034896
                if (__backup_products_140574267455120 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140574267455120
                __append(u'\n        <!-- /INSTALLABLE  -->\n\n        <!-- INSTALLED -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff32b7d0> name=None at 7fd9ff32b750> -> __attrs_140574270664208
                __attrs_140574270664208 = _static_140574266144720
                __backup_products_140574269036752 = get('products', __marker)

                # <Value u'view/get_installed' (164:38)> -> __value
                __token = 7829
                try:
                    __zt_tmp = __attrs_140574270664208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/get_installed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140574269035472 = get('num_products', __marker)

                # <Value u'python:len(products)' (165:41)> -> __value
                __token = 7890
                try:
                    __zt_tmp = __attrs_140574270664208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'len(products)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="activated-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7fd9ff77a550> name=None at 7fd9ff77a0d0> -> __attrs_140574270661904
                __attrs_140574270661904 = _static_140574270661968

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140574270660752 = []
                __append_140574270660752 = __stream_140574270660752.append
                __append_140574270660752(u'Activated add-ons')
                __msgid_140574270660752 = __re_whitespace(''.join(__stream_140574270660752)).strip()
                if __msgid_140574270660752:
                    __append(translate(__msgid_140574270660752, mapping=None, default=__msgid_140574270660752, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7fd9ff77a9d0> name=None at 7fd9ff77a950> -> __attrs_140574270569872
                __attrs_140574270569872 = _static_140574270663120

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n            ')

                # <Static value=<_ast.Dict object at 0x7fd9ff763850> name=None at 7fd9ff763110> -> __attrs_140574270570000
                __attrs_140574270570000 = _static_140574270568528

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n              ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284482320
                __attrs_140574284482320 = _static_140574442558096
                __backup_product_140574267401552 = get('product', __marker)

                # <Value u'products' (170:38)> -> __iterator
                __token = 8173
                try:
                    __zt_tmp = __attrs_140574284482320
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574284483600, ) = getitem('repeat')(u'product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255004496
                    __attrs_140574255004496 = _static_140574442558096
                    __backup_pid_140574255110480 = get('pid', __marker)

                    # <Value u'product/id' (171:41)> -> __value
                    __token = 8225
                    try:
                        __zt_tmp = __attrs_140574255004496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('path', u'product/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe88b0d0> name=None at 7fd9fe88bd10> -> __attrs_140574255002768
                    __attrs_140574255002768 = _static_140574255001808

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form action="uninstall_products" method="post" class="float-right">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe88b790> name=None at 7fd9fe88b990> -> __attrs_140574255038608
                    __attrs_140574255038608 = _static_140574255003536

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255041680
                    __default_140574255041680 = _DEFAULT_MARKER

                    # <Substitution u'pid' (175:49)> -> __attr_value
                    __token = 8467
                    try:
                        __zt_tmp = __attrs_140574255038608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe894890> name=None at 7fd9fe894690> -> __attrs_140574255038992
                    __attrs_140574255038992 = _static_140574255040656

                    # <Value u'product/uninstall_profile' (180:42)> -> __condition
                    __token = 8700
                    try:
                        __zt_tmp = __attrs_140574255038992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'product/uninstall_profile', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="destructive" type="submit"')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255039760
                        __default_140574255039760 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7fd9fe894a50> at 7fd9fe894750> -> __attr_value
                        __attr_value = u'Uninstall'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>')
                    __append(u'\n                  </form>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255041360
                    __attrs_140574255041360 = _static_140574442558096

                    # <h5 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h5>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270235024
                    __attrs_140574270235024 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270235728
                    __default_140574270235728 = _DEFAULT_MARKER

                    # <Value u'product/title' (184:39)> -> __cache_140574255039440
                    __token = 8868
                    try:
                        __zt_tmp = __attrs_140574270235024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574255039440 = _static_140574397981968('path', u'product/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/title' (184:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff712290> -> __condition
                    __expression = __cache_140574255039440

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                      Add-on Name\n                    </span>')
                    else:
                        __content = __cache_140574255039440
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                  </h5>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fd9fe88b2d0> name=None at 7fd9fe88bdd0> -> __attrs_140574270237328
                    __attrs_140574270237328 = _static_140574255002320

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="configletDescription discreet">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270570576
                    __attrs_140574270570576 = _static_140574442558096

                    # <Value u'product/description' (189:45)> -> __condition
                    __token = 9093
                    try:
                        __zt_tmp = __attrs_140574270570576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270570960
                        __default_140574270570960 = _DEFAULT_MARKER

                        # <Value u'product/description' (191:43)> -> __cache_140574270574160
                        __token = 9205
                        try:
                            __zt_tmp = __attrs_140574270570576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270574160 = _static_140574397981968('path', u'product/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/description' (191:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff764190> -> __condition
                        __expression = __cache_140574270574160

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'add-on description')
                        else:
                            __content = __cache_140574270574160
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff764290> name=None at 7fd9ff764990> -> __attrs_140574270571472
                    __attrs_140574270571472 = _static_140574270571152

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<em class="discreet"> \u2013 (')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270573264
                    __attrs_140574270573264 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270571728
                    __default_140574270571728 = _DEFAULT_MARKER

                    # <Value u'pid' (192:64)> -> __cache_140574270574224
                    __token = 9320
                    try:
                        __zt_tmp = __attrs_140574270573264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574270574224 = _static_140574397981968('path', u'pid', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'pid' (192:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff764b50> -> __condition
                    __expression = __cache_140574270574224

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140574270574224
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u' ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284388048
                    __attrs_140574284388048 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284388688
                    __default_140574284388688 = _DEFAULT_MARKER

                    # <Value u'product/version' (192:111)> -> __cache_140574284386640
                    __token = 9367
                    try:
                        __zt_tmp = __attrs_140574284388048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574284386640 = _static_140574397981968('path', u'product/version', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/version' (192:111)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda00491d10> -> __condition
                    __expression = __cache_140574284386640

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>1.0</span>')
                    else:
                        __content = __cache_140574284386640
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u')</em>\n                  </p>\n                  <!-- <dl class="portalMessage info"\n                       role="status"\n                       tal:condition="not:product/uninstall_profile">\n                       <dt i18n:translate="">Info</dt>\n                       <dd i18n:translate="">This product cannot be uninstalled!</dd>\n                       </dl> -->\n                ')
                    if (__backup_pid_140574255110480 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140574255110480
                    __append(u'\n              </li>')
                    ____index_140574284483600 -= 1
                    if (____index_140574284483600 > 0):
                        __append('\n              ')
                if (__backup_product_140574267401552 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140574267401552
                __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140574269035472 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140574269035472
                if (__backup_products_140574269036752 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140574269036752
                __append(u'\n        <!-- /INSTALLED -->\n\n        <!-- BROKEN -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9fe88b710> name=None at 7fda004a8d90> -> __attrs_140574284388880
                __attrs_140574284388880 = _static_140574255003408
                __backup_products_140574269037712 = get('products', __marker)

                # <Value u'view/get_broken' (208:38)> -> __value
                __token = 9959
                try:
                    __zt_tmp = __attrs_140574284388880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/get_broken', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140574269035152 = get('num_products', __marker)

                # <Value u'python:len(products)' (209:41)> -> __value
                __token = 10017
                try:
                    __zt_tmp = __attrs_140574284388880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'len(products)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value u'num_products' (210:32)> -> __condition
                __token = 10073
                try:
                    __zt_tmp = __attrs_140574284388880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'num_products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section id="broken-products" class="portlet">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4f5f10> name=None at 7fd9ff4f5650> -> __attrs_140574257251024
                    __attrs_140574257251024 = _static_140574268022544

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header class="portletHeader">')
                    __stream_140574268018768 = []
                    __append_140574268018768 = __stream_140574268018768.append
                    __append_140574268018768(u'Broken add-ons')
                    __msgid_140574268018768 = __re_whitespace(''.join(__stream_140574268018768)).strip()
                    if __msgid_140574268018768:
                        __append(translate(__msgid_140574268018768, mapping=None, default=__msgid_140574268018768, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</header>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9feab0fd0> name=None at 7fd9feab0f50> -> __attrs_140574284493648
                    __attrs_140574284493648 = _static_140574257254352

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda004abb10> name=None at 7fda004abc10> -> __attrs_140574255161872
                    __attrs_140574255161872 = _static_140574284495632

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255078800
                    __attrs_140574255078800 = _static_140574442558096
                    __backup_product_140574256079952 = get('product', __marker)

                    # <Value u'products' (215:38)> -> __iterator
                    __token = 10341
                    try:
                        __zt_tmp = __attrs_140574255078800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'products', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574255076368, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255079376
                        __attrs_140574255079376 = _static_140574442558096

                        # <h5 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h5>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255077648
                        __attrs_140574255077648 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255078992
                        __default_140574255078992 = _DEFAULT_MARKER

                        # <Value u'product/product_id' (217:37)> -> __cache_140574255075856
                        __token = 10410
                        try:
                            __zt_tmp = __attrs_140574255077648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574255075856 = _static_140574397981968('path', u'product/product_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/product_id' (217:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe89d050> -> __condition
                        __expression = __cache_140574255075856

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    Add-on Name\n                  </span>')
                        else:
                            __content = __cache_140574255075856
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </h5>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9fe89db50> name=None at 7fd9fe89d850> -> __attrs_140574255076496
                        __attrs_140574255076496 = _static_140574255078224

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268934096
                        __attrs_140574268934096 = _static_140574442558096

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268934352
                        __default_140574268934352 = _DEFAULT_MARKER

                        # <Value u'product/type' (222:37)> -> __cache_140574268935568
                        __token = 10624
                        try:
                            __zt_tmp = __attrs_140574268934096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574268935568 = _static_140574397981968('path', u'product/type', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/type' (222:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff5d4250> -> __condition
                        __expression = __cache_140574268935568

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Type')
                        else:
                            __content = __cache_140574268935568
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff5d4c10> name=None at 7fd9ff5d4ad0> -> __attrs_140574268935952
                        __attrs_140574268935952 = _static_140574268935184

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> - ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269062928
                        __attrs_140574269062928 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269061776
                        __default_140574269061776 = _DEFAULT_MARKER

                        # <Value u'product/value' (223:65)> -> __cache_140574269063120
                        __token = 10739
                        try:
                            __zt_tmp = __attrs_140574269062928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574269063120 = _static_140574397981968('path', u'product/value', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/value' (223:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff5f3250> -> __condition
                        __expression = __cache_140574269063120

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Reason')
                        else:
                            __content = __cache_140574269063120
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</em>\n                </p>\n              </li>')
                        ____index_140574255076368 -= 1
                        if (____index_140574255076368 > 0):
                            __append('\n              ')
                    if (__backup_product_140574256079952 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140574256079952
                    __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140574269035152 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140574269035152
                if (__backup_products_140574269037712 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140574269037712
                __append(u'\n        <!-- /BROKEN -->\n\n      </div>\n    ')
                __i18n_domain = __previous_i18n_domain_140574272098000
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140574272097872
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140574397981968('path', u'context/prefs_main_template/macros/master', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140574270520688 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140574270520688
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }