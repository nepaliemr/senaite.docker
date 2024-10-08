# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/controlpanel/templates/overview.pt'

__tokens = {430: (u"python:request.set('disable_plone.leftcolumn',1)", 11, 51), 530: (u" python:request.set('disable_plone.rightcolumn',1", 12, 50), 998: (u'view/upgrade_warning', 25, 26), 1285: (u'string:${context/portal_url}/@@plone-upgrade', 33, 34), 1697: (u'view/mailhost_warning', 45, 26), 2266: (u'string:${portal_url}/@@mail-controlpanel', 56, 36), 2531: (u'view/timezone_warning', 65, 26), 3062: (u'string:${portal_url}/@@dateandtime-controlpanel', 77, 36), 3352: (u'not:view/pil', 86, 26), 3649: (u'view/categories', 95, 41), 3705: (u"python:view.sublists(category.get('id'))", 96, 38), 3837: (u'sublist', 97, 89), 3917: (u'category/title', 98, 70), 4114: (u'sublist', 102, 57), 4181: (u'sublist', 103, 57), 4241: (u'sublist', 104, 50), 4316: (u'action/visible', 105, 65), 4451: (u'action/icon', 108, 42), 4510: (u'action/url', 109, 46), 4575: (u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", 110, 52), 4693: (u'action/title', 111, 48), 5066: (u'not:sublist', 124, 32), 5451: (u'view/version_overview', 137, 43), 5502: (u'version', 138, 27), 5597: (u'view/server_info', 140, 44), 5655: (u' server_info/wsg', 141, 40), 5799: (u'has_wsgi', 144, 51), 5870: (u'not:has_wsgi', 145, 51), 6003: (u'${server_info/server_name}', 149, 18), 6005: (u'server_info/server_name', 149, 20), 6055: (u'${server_info/version}', 150, 18), 6057: (u'server_info/version', 150, 20), 6160: (u'not:view/is_dev_mode', 155, 24), 6777: (u'view/is_dev_mode', 167, 24), 261: (u'here/prefs_main_template/macros/master', 6, 23), 261: (u'here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140574284461776 = {u'class': u'portlet portletNavigationTree portletSiteSetup', }
_static_140574284481808 = {u'class': u'portletHeader text-secondary', }
_static_140574284481296 = {u'class': u'row', }
_static_140574255165008 = u'master'
_static_140574270390928 = {u'class': u'nav nav-pills', }
_static_140574270569872 = {u'class': u'nav-item col-sm-3', }
_static_140574397981968 = __compile_zt_expr
_static_140574269031120 = {u'href': u'#', u'title': u'Go to the upgrade page', }
_static_140574442558096 = {}
_static_140574268003152 = {u'class': u'documentDescription text-secondary', }
_static_140574257251984 = {u'class': u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", }
_static_140574268017104 = {u'href': u'#', u'class': u'nav-link', }
_static_140574268918416 = {u'href': u'', }
_static_140574268919760 = {u'role': u'status', u'class': u'portalMessage warning alert alert-warning', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574284440464 = {u'role': u'status', u'class': u'portalMessage warning alert alert-warning', }
_static_140574270207632 = {u'class': u'discreet text-muted small', }
_static_140574268059472 = {u'class': u'discreet text-muted small', }
_static_140574270166480 = {u'role': u'status', u'class': u'portalMessage warning alert alert-warning', }
_static_140574270570640 = {u'class': u'visualClear', }
_static_140574270170704 = {u'class': u'documentFirstHeading', }
_static_140574268003920 = {u'role': u'status', u'class': u'portalMessage warning alert alert-warning', }
_static_140574284429520 = {u'class': u'discreet', }
_static_140574269062096 = {u'href': u'', }
_static_140574270236240 = {u'class': u'portletContent', }
_static_140574284428880 = {u'class': u'col-sm-12', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268935632
            __attrs_140574268935632 = _static_140574442558096
            __previous_i18n_domain_140574268936080 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140574248837600 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fd9fe8b2e50> name=None at 7fd9ff5d4150> -> __value
            __value = _static_140574255165008
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270172496
                __attrs_140574270172496 = _static_140574442558096
                __backup_disable_column_one_140574268935312 = get('disable_column_one', __marker)

                # <Value u"python:request.set('disable_plone.leftcolumn',1)" (11:51)> -> __value
                __token = 430
                try:
                    __zt_tmp = __attrs_140574270172496
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140574268933072 = get('disable_column_two', __marker)

                # <Value u"python:request.set('disable_plone.rightcolumn',1)" (12:50)> -> __value
                __token = 530
                try:
                    __zt_tmp = __attrs_140574270172496
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140574268933072 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140574268933072
                if (__backup_disable_column_one_140574268935312 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140574268935312
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270171280
                __attrs_140574270171280 = _static_140574442558096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff702650> name=None at 7fd9ff702fd0> -> __attrs_140574268005456
                __attrs_140574268005456 = _static_140574270170704

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140574270171024 = []
                __append_140574270171024 = __stream_140574270171024.append
                __append_140574270171024(u'Site Setup')
                __msgid_140574270171024 = __re_whitespace(''.join(__stream_140574270171024)).strip()
                if __msgid_140574270171024:
                    __append(translate(__msgid_140574270171024, mapping=None, default=__msgid_140574270171024, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f1350> name=None at 7fd9ff4f1250> -> __attrs_140574268004304
                __attrs_140574268004304 = _static_140574268003152

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="documentDescription text-secondary">')
                __stream_140574268004816 = []
                __append_140574268004816 = __stream_140574268004816.append
                __append_140574268004816(u'\n        Configuration area for Plone and add-on Products.\n      ')
                __msgid_140574268004816 = __re_whitespace(''.join(__stream_140574268004816)).strip()
                if u'description_control_panel':
                    __append(translate(u'description_control_panel', mapping=None, default=__msgid_140574268004816, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f1650> name=None at 7fd9ff4f1e10> -> __attrs_140574270167760
                __attrs_140574270167760 = _static_140574268003920

                # <Value u'view/upgrade_warning' (25:26)> -> __condition
                __token = 998
                try:
                    __zt_tmp = __attrs_140574270167760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/upgrade_warning', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning alert alert-warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270168336
                    __attrs_140574270168336 = _static_140574442558096

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140574270168464 = []
                    __append_140574270168464 = __stream_140574270168464.append
                    __append_140574270168464(u'\n          Warning\n        ')
                    __msgid_140574270168464 = __re_whitespace(''.join(__stream_140574270168464)).strip()
                    if __msgid_140574270168464:
                        __append(translate(__msgid_140574270168464, mapping=None, default=__msgid_140574270168464, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270167632
                    __attrs_140574270167632 = _static_140574442558096
                    __stream_140574267302448_link_continue_with_the_upgrade = ''
                    __stream_140574270165392 = []
                    __append_140574270165392 = __stream_140574270165392.append
                    __append_140574270165392(u'\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_140574267302448_link_continue_with_the_upgrade = []
                    __append_140574267302448_link_continue_with_the_upgrade = __stream_140574267302448_link_continue_with_the_upgrade.append

                    # <Static value=<_ast.Dict object at 0x7fd9ff5ec2d0> name=None at 7fd9ff5ec510> -> __attrs_140574269031888
                    __attrs_140574269031888 = _static_140574269031120

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140574267302448_link_continue_with_the_upgrade(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269032336
                    __default_140574269032336 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/portal_url}/@@plone-upgrade' (33:34)> -> __attr_href
                    __token = 1285
                    try:
                        __zt_tmp = __attrs_140574269031888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140574267302448_link_continue_with_the_upgrade((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269031824
                    __default_140574269031824 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff5ecb90> at 7fd9ff5ec050> -> __attr_title
                    __attr_title = u'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append_140574267302448_link_continue_with_the_upgrade((u' title="%s"' % __attr_title))
                    __append_140574267302448_link_continue_with_the_upgrade(u'>')
                    __stream_140574269031632 = []
                    __append_140574269031632 = __stream_140574269031632.append
                    __append_140574269031632(u'\n            continue with the upgrade\n          ')
                    __msgid_140574269031632 = __re_whitespace(''.join(__stream_140574269031632)).strip()
                    if __msgid_140574269031632:
                        __append_140574267302448_link_continue_with_the_upgrade(translate(__msgid_140574269031632, mapping=None, default=__msgid_140574269031632, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140574267302448_link_continue_with_the_upgrade(u'</a>')
                    __append_140574270165392(u'${link_continue_with_the_upgrade}')
                    __stream_140574267302448_link_continue_with_the_upgrade = ''.join(__stream_140574267302448_link_continue_with_the_upgrade)
                    __append_140574270165392(u'.\n        ')
                    __msgid_140574270165392 = __re_whitespace(''.join(__stream_140574270165392)).strip()
                    if __msgid_140574270165392:
                        __append(translate(__msgid_140574270165392, mapping={u'link_continue_with_the_upgrade': __stream_140574267302448_link_continue_with_the_upgrade, }, default=__msgid_140574270165392, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n      </div>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff7015d0> name=None at 7fd9ff701e90> -> __attrs_140574269032528
                __attrs_140574269032528 = _static_140574270166480

                # <Value u'view/mailhost_warning' (45:26)> -> __condition
                __token = 1697
                try:
                    __zt_tmp = __attrs_140574269032528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/mailhost_warning', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning alert alert-warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284442640
                    __attrs_140574284442640 = _static_140574442558096

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140574284442000 = []
                    __append_140574284442000 = __stream_140574284442000.append
                    __append_140574284442000(u'\n          Warning\n        ')
                    __msgid_140574284442000 = __re_whitespace(''.join(__stream_140574284442000)).strip()
                    if __msgid_140574284442000:
                        __append(translate(__msgid_140574284442000, mapping=None, default=__msgid_140574284442000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284440976
                    __attrs_140574284440976 = _static_140574442558096
                    __stream_140574267302448_label_mail_control_panel_link = ''
                    __stream_140574284441424 = []
                    __append_140574284441424 = __stream_140574284441424.append
                    __append_140574284441424(u"\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_140574267302448_label_mail_control_panel_link = []
                    __append_140574267302448_label_mail_control_panel_link = __stream_140574267302448_label_mail_control_panel_link.append

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284440784
                    __attrs_140574284440784 = _static_140574442558096
                    __append_140574267302448_label_mail_control_panel_link(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff5f3bd0> name=None at 7fd9ff5f3f10> -> __attrs_140574269061968
                    __attrs_140574269061968 = _static_140574269062096

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140574267302448_label_mail_control_panel_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269060112
                    __default_140574269060112 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@mail-controlpanel' (56:36)> -> __attr_href
                    __token = 2266
                    try:
                        __zt_tmp = __attrs_140574269061968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140574267302448_label_mail_control_panel_link((u' href="%s"' % __attr_href))
                    __append_140574267302448_label_mail_control_panel_link(u' >')
                    __stream_140574269061712 = []
                    __append_140574269061712 = __stream_140574269061712.append
                    __append_140574269061712(u'Mail control panel')
                    __msgid_140574269061712 = __re_whitespace(''.join(__stream_140574269061712)).strip()
                    if u'text_no_mailhost_configured_control_panel_link':
                        __append_140574267302448_label_mail_control_panel_link(translate(u'text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_140574269061712, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140574267302448_label_mail_control_panel_link(u'</a>\n          ')
                    __append_140574284441424(u'${label_mail_control_panel_link}')
                    __stream_140574267302448_label_mail_control_panel_link = ''.join(__stream_140574267302448_label_mail_control_panel_link)
                    __append_140574284441424(u'\n          to fix this.\n        ')
                    __msgid_140574284441424 = __re_whitespace(''.join(__stream_140574284441424)).strip()
                    if u'text_no_mailhost_configured':
                        __append(translate(u'text_no_mailhost_configured', mapping={u'label_mail_control_panel_link': __stream_140574267302448_label_mail_control_panel_link, }, default=__msgid_140574284441424, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n      </div>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fda0049e390> name=None at 7fda0049e550> -> __attrs_140574269059344
                __attrs_140574269059344 = _static_140574284440464

                # <Value u'view/timezone_warning' (65:26)> -> __condition
                __token = 2531
                try:
                    __zt_tmp = __attrs_140574269059344
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/timezone_warning', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning alert alert-warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268918224
                    __attrs_140574268918224 = _static_140574442558096

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140574269062544 = []
                    __append_140574269062544 = __stream_140574269062544.append
                    __append_140574269062544(u'\n          Warning\n        ')
                    __msgid_140574269062544 = __re_whitespace(''.join(__stream_140574269062544)).strip()
                    if __msgid_140574269062544:
                        __append(translate(__msgid_140574269062544, mapping=None, default=__msgid_140574269062544, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268916944
                    __attrs_140574268916944 = _static_140574442558096
                    __stream_140574267302448_label_mail_event_settings_link = ''
                    __stream_140574268918096 = []
                    __append_140574268918096 = __stream_140574268918096.append
                    __append_140574268918096(u'\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_140574267302448_label_mail_event_settings_link = []
                    __append_140574267302448_label_mail_event_settings_link = __stream_140574267302448_label_mail_event_settings_link.append

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268917840
                    __attrs_140574268917840 = _static_140574442558096
                    __append_140574267302448_label_mail_event_settings_link(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff5d0a90> name=None at 7fd9ff5d0410> -> __attrs_140574268917136
                    __attrs_140574268917136 = _static_140574268918416

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140574267302448_label_mail_event_settings_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268917456
                    __default_140574268917456 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@dateandtime-controlpanel' (77:36)> -> __attr_href
                    __token = 3062
                    try:
                        __zt_tmp = __attrs_140574268917136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140574267302448_label_mail_event_settings_link((u' href="%s"' % __attr_href))
                    __append_140574267302448_label_mail_event_settings_link(u' >')
                    __stream_140574268919504 = []
                    __append_140574268919504 = __stream_140574268919504.append
                    __append_140574268919504(u'Date and Time Settings control panel')
                    __msgid_140574268919504 = __re_whitespace(''.join(__stream_140574268919504)).strip()
                    if u'text_no_timezone_configured_control_panel_link':
                        __append_140574267302448_label_mail_event_settings_link(translate(u'text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_140574268919504, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140574267302448_label_mail_event_settings_link(u'</a>\n          ')
                    __append_140574268918096(u'${label_mail_event_settings_link}')
                    __stream_140574267302448_label_mail_event_settings_link = ''.join(__stream_140574267302448_label_mail_event_settings_link)
                    __append_140574268918096(u'\n          to fix this.\n        ')
                    __msgid_140574268918096 = __re_whitespace(''.join(__stream_140574268918096)).strip()
                    if u'text_no_timezone_configured':
                        __append(translate(u'text_no_timezone_configured', mapping={u'label_mail_event_settings_link': __stream_140574267302448_label_mail_event_settings_link, }, default=__msgid_140574268918096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n      </div>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff5d0fd0> name=None at 7fd9ff5d0450> -> __attrs_140574270572048
                __attrs_140574270572048 = _static_140574268919760

                # <Value u'not:view/pil' (86:26)> -> __condition
                __token = 3352
                try:
                    __zt_tmp = __attrs_140574270572048
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('not', u'view/pil', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning alert alert-warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270574544
                    __attrs_140574270574544 = _static_140574442558096

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140574270574096 = []
                    __append_140574270574096 = __stream_140574270574096.append
                    __append_140574270574096(u'\n          Warning\n        ')
                    __msgid_140574270574096 = __re_whitespace(''.join(__stream_140574270574096)).strip()
                    if __msgid_140574270574096:
                        __append(translate(__msgid_140574270574096, mapping=None, default=__msgid_140574270574096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270572240
                    __attrs_140574270572240 = _static_140574442558096
                    __stream_140574270571088 = []
                    __append_140574270571088 = __stream_140574270571088.append
                    __append_140574270571088(u'\n          PIL is not installed properly, image scaling will not work.\n        ')
                    __msgid_140574270571088 = __re_whitespace(''.join(__stream_140574270571088)).strip()
                    if u'text_no_pil_installed':
                        __append(translate(u'text_no_pil_installed', mapping=None, default=__msgid_140574270571088, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n      </div>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270573840
                __attrs_140574270573840 = _static_140574442558096
                __backup_category_140574270170896 = get('category', __marker)

                # <Value u'view/categories' (95:41)> -> __iterator
                __token = 3649
                try:
                    __zt_tmp = __attrs_140574270573840
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'view/categories', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574270571728, ) = getitem('repeat')(u'category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270572432
                    __attrs_140574270572432 = _static_140574442558096
                    __backup_sublist_140574270172944 = get('sublist', __marker)

                    # <Value u"python:view.sublists(category.get('id'))" (96:38)> -> __value
                    __token = 3705
                    try:
                        __zt_tmp = __attrs_140574270572432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u"view.sublists(category.get('id'))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda004a36d0> name=None at 7fda004a3890> -> __attrs_140574284460944
                    __attrs_140574284460944 = _static_140574284461776

                    # <Value u'sublist' (97:89)> -> __condition
                    __token = 3837
                    try:
                        __zt_tmp = __attrs_140574284460944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'sublist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<section class="portlet portletNavigationTree portletSiteSetup">\n            ')

                        # <Static value=<_ast.Dict object at 0x7fda004a8510> name=None at 7fd9ff70fc90> -> __attrs_140574284483920
                        __attrs_140574284483920 = _static_140574284481808

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<strong class="portletHeader text-secondary">')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270225168
                        __default_140574270225168 = _DEFAULT_MARKER

                        # <Value u'category/title' (98:70)> -> __cache_140574270225360
                        __token = 3917
                        try:
                            __zt_tmp = __attrs_140574284483920
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574270225360 = _static_140574397981968('path', u'category/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'category/title' (98:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff70f950> -> __condition
                        __expression = __cache_140574270225360

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Category')
                        else:
                            __content = __cache_140574270225360
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</strong>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fda004a8310> name=None at 7fda004a8b90> -> __attrs_140574284429008
                        __attrs_140574284429008 = _static_140574284481296

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="row">\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda0049b650> name=None at 7fda0049b190> -> __attrs_140574270236432
                        __attrs_140574270236432 = _static_140574284428880

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="col-sm-12">\n              ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff712650> name=None at 7fd9ff712610> -> __attrs_140574270236304
                        __attrs_140574270236304 = _static_140574270236240

                        # <Value u'sublist' (102:57)> -> __condition
                        __token = 4114
                        try:
                            __zt_tmp = __attrs_140574270236304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'sublist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<nav class="portletContent">\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff738290> name=None at 7fd9ff738210> -> __attrs_140574270392784
                            __attrs_140574270392784 = _static_140574270390928

                            # <Value u'sublist' (103:57)> -> __condition
                            __token = 4181
                            try:
                                __zt_tmp = __attrs_140574270392784
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'sublist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<ul class="nav nav-pills">\n                  ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284427856
                                __attrs_140574284427856 = _static_140574442558096
                                __backup_action_140574270236368 = get('action', __marker)

                                # <Value u'sublist' (104:50)> -> __iterator
                                __token = 4241
                                try:
                                    __zt_tmp = __attrs_140574284427856
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140574397981968('path', u'sublist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                (__iterator, ____index_140574270569296, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append(u'\n                    ')

                                    # <Static value=<_ast.Dict object at 0x7fd9ff763d90> name=None at 7fd9ff763e50> -> __attrs_140574270568144
                                    __attrs_140574270568144 = _static_140574270569872

                                    # <Value u'action/visible' (105:65)> -> __condition
                                    __token = 4316
                                    try:
                                        __zt_tmp = __attrs_140574270568144
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140574397981968('path', u'action/visible', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<li class="nav-item col-sm-3">\n                      ')

                                        # <Static value=<_ast.Dict object at 0x7fd9ff4f49d0> name=None at 7fd9ff4f4e50> -> __attrs_140574257251472
                                        __attrs_140574257251472 = _static_140574268017104
                                        __backup_icon_140574270568656 = get('icon', __marker)

                                        # <Value u'action/icon' (108:42)> -> __value
                                        __token = 4451
                                        try:
                                            __zt_tmp = __attrs_140574257251472
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_140574397981968('path', u'action/icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                        econtext['icon'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<a')

                                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268016208
                                        __default_140574268016208 = _DEFAULT_MARKER

                                        # <Substitution u'action/url' (109:46)> -> __attr_href
                                        __token = 4510
                                        try:
                                            __zt_tmp = __attrs_140574257251472
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_140574397981968('path', u'action/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((u' href="%s"' % __attr_href))
                                        __append(u' class="nav-link">\n                        ')

                                        # <Static value=<_ast.Dict object at 0x7fd9feab0690> name=None at 7fd9feab0b10> -> __attrs_140574268019152
                                        __attrs_140574268019152 = _static_140574257251984

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<span')

                                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268020880
                                        __default_140574268020880 = _DEFAULT_MARKER

                                        # <Substitution u"python:'icon-controlpanel-' + action['id'].replace('.', '_')" (110:52)> -> __attr_class
                                        __token = 4575
                                        try:
                                            __zt_tmp = __attrs_140574268019152
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_140574397981968('python', u"'icon-controlpanel-' + action['id'].replace('.', '_')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_class is not None):
                                            __append((u' class="%s"' % __attr_class))
                                        __append(u'></span>\n                        ')

                                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268021776
                                        __attrs_140574268021776 = _static_140574442558096

                                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268021584
                                        __default_140574268021584 = _DEFAULT_MARKER

                                        # <Value u'action/title' (111:48)> -> __cache_140574268022096
                                        __token = 4693
                                        try:
                                            __zt_tmp = __attrs_140574268021776
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140574268022096 = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                        # <BinOp left=<Value u'action/title' (111:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f5dd0> -> __condition
                                        __expression = __cache_140574268022096

                                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append(u'\n                          Title\n                        ')
                                        else:
                                            __content = __cache_140574268022096
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append(u'\n                      </a>')
                                        if (__backup_icon_140574270568656 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_140574270568656
                                        __append(u'\n                    </li>')
                                    __append(u'\n                  ')
                                    ____index_140574270569296 -= 1
                                    if (____index_140574270569296 > 0):
                                        __append('')
                                if (__backup_action_140574270236368 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140574270236368
                                __append(u'\n                </ul>')
                            __append(u'\n              </nav>')
                        __append(u'\n              </div>\n            </div>\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7fda0049b8d0> name=None at 7fda0049bad0> -> __attrs_140574270569616
                        __attrs_140574270569616 = _static_140574284429520

                        # <Value u'not:sublist' (124:32)> -> __condition
                        __token = 5066
                        try:
                            __zt_tmp = __attrs_140574270569616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('not', u'sublist', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="discreet">')
                            __stream_140574284430416 = []
                            __append_140574284430416 = __stream_140574284430416.append
                            __append_140574284430416(u'\n              No preference panels available.\n            ')
                            __msgid_140574284430416 = __re_whitespace(''.join(__stream_140574284430416)).strip()
                            if u'label_no_prefs_panels_available':
                                __append(translate(u'label_no_prefs_panels_available', mapping=None, default=__msgid_140574284430416, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</div>')
                        __append(u'\n\n          </section>')
                    __append(u'\n        ')
                    if (__backup_sublist_140574270172944 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_140574270172944
                    __append(u'\n      ')
                    ____index_140574270571728 -= 1
                    if (____index_140574270571728 > 0):
                        __append('')
                if (__backup_category_140574270170896 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140574270170896
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff764090> name=None at 7fd9ff7648d0> -> __attrs_140574284483024
                __attrs_140574284483024 = _static_140574270570640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"><!-- --></div>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268019024
                __attrs_140574268019024 = _static_140574442558096

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h2>')
                __stream_140574257254352 = []
                __append_140574257254352 = __stream_140574257254352.append
                __append_140574257254352(u'Version Overview')
                __msgid_140574257254352 = __re_whitespace(''.join(__stream_140574257254352)).strip()
                if u'heading_version_overview':
                    __append(translate(u'heading_version_overview', mapping=None, default=__msgid_140574257254352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h2>\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270302608
                __attrs_140574270302608 = _static_140574442558096

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270300752
                __attrs_140574270300752 = _static_140574442558096
                __backup_version_140574268003344 = get('version', __marker)

                # <Value u'view/version_overview' (137:43)> -> __iterator
                __token = 5451
                try:
                    __zt_tmp = __attrs_140574270300752
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'view/version_overview', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574270302864, ) = getitem('repeat')(u'version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268055696
                    __attrs_140574268055696 = _static_140574442558096

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268055888
                    __default_140574268055888 = _DEFAULT_MARKER

                    # <Value u'version' (138:27)> -> __cache_140574268059408
                    __token = 5502
                    try:
                        __zt_tmp = __attrs_140574268055696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574268059408 = _static_140574397981968('path', u'version', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'version' (138:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4feed0> -> __condition
                    __expression = __cache_140574268059408

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Version')
                    else:
                        __content = __cache_140574268059408
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</li>\n        ')
                    ____index_140574270302864 -= 1
                    if (____index_140574270302864 > 0):
                        __append('')
                if (__backup_version_140574268003344 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_140574268003344
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268056784
                __attrs_140574268056784 = _static_140574442558096
                __backup_server_info_140574270167888 = get('server_info', __marker)

                # <Value u'view/server_info' (140:44)> -> __value
                __token = 5597
                try:
                    __zt_tmp = __attrs_140574268056784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/server_info', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_140574269034192 = get('has_wsgi', __marker)

                # <Value u'server_info/wsgi' (141:40)> -> __value
                __token = 5655
                try:
                    __zt_tmp = __attrs_140574268056784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'server_info/wsgi', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255011152
                __attrs_140574255011152 = _static_140574442558096

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255010768
                __attrs_140574255010768 = _static_140574442558096
                __stream_140574255010064 = []
                __append_140574255010064 = __stream_140574255010064.append
                __append_140574255010064(u'WSGI:')
                __msgid_140574255010064 = __re_whitespace(''.join(__stream_140574255010064)).strip()
                if __msgid_140574255010064:
                    __append(translate(__msgid_140574255010064, mapping=None, default=__msgid_140574255010064, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255012944
                __attrs_140574255012944 = _static_140574442558096

                # <Value u'has_wsgi' (144:51)> -> __condition
                __token = 5799
                try:
                    __zt_tmp = __attrs_140574255012944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'has_wsgi', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140574255010832 = []
                    __append_140574255010832 = __stream_140574255010832.append
                    __append_140574255010832(u'On')
                    __msgid_140574255010832 = __re_whitespace(''.join(__stream_140574255010832)).strip()
                    if __msgid_140574255010832:
                        __append(translate(__msgid_140574255010832, mapping=None, default=__msgid_140574255010832, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255011984
                __attrs_140574255011984 = _static_140574442558096

                # <Value u'not:has_wsgi' (145:51)> -> __condition
                __token = 5870
                try:
                    __zt_tmp = __attrs_140574255011984
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('not', u'has_wsgi', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140574255011088 = []
                    __append_140574255011088 = __stream_140574255011088.append
                    __append_140574255011088(u'Off')
                    __msgid_140574255011088 = __re_whitespace(''.join(__stream_140574255011088)).strip()
                    if __msgid_140574255011088:
                        __append(translate(__msgid_140574255011088, mapping=None, default=__msgid_140574255011088, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n          </li>\n          ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255012496
                __attrs_140574255012496 = _static_140574442558096

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270206736
                __attrs_140574270206736 = _static_140574442558096
                __stream_140574255010512 = []
                __append_140574255010512 = __stream_140574255010512.append
                __append_140574255010512(u'Server:')
                __msgid_140574255010512 = __re_whitespace(''.join(__stream_140574255010512)).strip()
                if __msgid_140574255010512:
                    __append(translate(__msgid_140574255010512, mapping=None, default=__msgid_140574255010512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270208336
                __attrs_140574270208336 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/server_name}' (149:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fd9ff70b650> -> __content_140574503216352
                __token = 6003
                __token = 6005
                try:
                    __zt_tmp = __attrs_140574270208336
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140574503216352 = _static_140574397981968('path', u'server_info/server_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __content_140574503216352 = __quote(__content_140574503216352, '\x00', '&#0;', None, None)
                __content_140574503216352 = __content_140574503216352
                if (__content_140574503216352 is None):
                    pass
                else:
                    if (__content_140574503216352 is None):
                        __content_140574503216352 = None
                    else:
                        __tt = type(__content_140574503216352)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140574503216352 = unicode(__content_140574503216352)
                        else:
                            if (__tt is str):
                                __content_140574503216352 = decode(__content_140574503216352)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140574503216352 = __content_140574503216352.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140574503216352)
                                        __content_140574503216352 = (unicode(__content_140574503216352) if (__content_140574503216352 is __converted) else __converted)
                                    else:
                                        __content_140574503216352 = __content_140574503216352()
                if (__content_140574503216352 is not None):
                    __append(__content_140574503216352)
                __append(u'</span>\n            ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270208592
                __attrs_140574270208592 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/version}' (150:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fd9ff70b9d0> -> __content_140574503216352
                __token = 6055
                __token = 6057
                try:
                    __zt_tmp = __attrs_140574270208592
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140574503216352 = _static_140574397981968('path', u'server_info/version', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __content_140574503216352 = __quote(__content_140574503216352, '\x00', '&#0;', None, None)
                __content_140574503216352 = __content_140574503216352
                if (__content_140574503216352 is None):
                    pass
                else:
                    if (__content_140574503216352 is None):
                        __content_140574503216352 = None
                    else:
                        __tt = type(__content_140574503216352)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140574503216352 = unicode(__content_140574503216352)
                        else:
                            if (__tt is str):
                                __content_140574503216352 = decode(__content_140574503216352)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140574503216352 = __content_140574503216352.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140574503216352)
                                        __content_140574503216352 = (unicode(__content_140574503216352) if (__content_140574503216352 is __converted) else __converted)
                                    else:
                                        __content_140574503216352 = __content_140574503216352()
                if (__content_140574503216352 is not None):
                    __append(__content_140574503216352)
                __append(u'</span>\n          </li>\n        ')
                if (__backup_has_wsgi_140574269034192 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_140574269034192
                if (__backup_server_info_140574270167888 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_140574270167888
                __append(u'\n      </ul>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4fef50> name=None at 7fd9ff7222d0> -> __attrs_140574270206864
                __attrs_140574270206864 = _static_140574268059472

                # <Value u'not:view/is_dev_mode' (155:24)> -> __condition
                __token = 6160
                try:
                    __zt_tmp = __attrs_140574270206864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('not', u'view/is_dev_mode', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet text-muted small">')
                    __stream_140574270300944 = []
                    __append_140574270300944 = __stream_140574270300944.append
                    __append_140574270300944(u'\n        You are running in "production mode". This is the preferred mode of\n        operation for a live Plone site, but means that some\n        configuration changes will not take effect until your server is\n        restarted or a product refreshed. If this is a development instance,\n        and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n        in your buildout.cfg, re-run bin/buildout and then restart the server\n        process.\n      ')
                    __msgid_140574270300944 = __re_whitespace(''.join(__stream_140574270300944)).strip()
                    if u'description_production_mode':
                        __append(translate(u'description_production_mode', mapping=None, default=__msgid_140574270300944, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff70b690> name=None at 7fd9ff70b910> -> __attrs_140574268982160
                __attrs_140574268982160 = _static_140574270207632

                # <Value u'view/is_dev_mode' (167:24)> -> __condition
                __token = 6777
                try:
                    __zt_tmp = __attrs_140574268982160
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/is_dev_mode', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet text-muted small">')
                    __stream_140574270209360 = []
                    __append_140574270209360 = __stream_140574270209360.append
                    __append_140574270209360(u'\n        You are running in "debug mode". This mode is intended for sites that\n        are under development. This allows many configuration changes to be\n        immediately visible, but will make your site run more slowly. To turn\n        off debug mode, stop the server, set \'debug-mode=off\' in your\n        buildout.cfg, re-run bin/buildout and then restart the server\n        process.\n      ')
                    __msgid_140574270209360 = __re_whitespace(''.join(__stream_140574270209360)).strip()
                    if u'description_debug_mode':
                        __append(translate(u'description_debug_mode', mapping=None, default=__msgid_140574270209360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n    </div>')
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140574268935632
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140574397981968('path', u'here/prefs_main_template/macros/master', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140574248837600 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140574248837600
            __i18n_domain = __previous_i18n_domain_140574268936080
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }