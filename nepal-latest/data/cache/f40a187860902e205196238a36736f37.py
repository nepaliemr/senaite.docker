# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.contenttypes-2.2.3-py2.7.egg/plone/app/contenttypes/browser/templates/archetypes_warning_viewlet.pt'

__tokens = {26: (u'view/available', 1, 26), 200: (u'not:view/can_migrate', 4, 32), 388: (u'view/can_migrate', 7, 32), 565: (u'string:${context/plone_portal_state/portal_url}/@@atct_migrator', 10, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574266146064 = {u'href': u'#', }
_static_140574255109264 = {u'class': u'portalMessage alert-box secondary warning', }
_static_140574442558096 = {}
_static_140574397981968 = __compile_zt_expr
_static_140574270601232 = {u'type': u'text/css', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255063568
            __attrs_140574255063568 = _static_140574442558096

            # <Value u'view/available' (1:26)> -> __condition
            __token = 26
            try:
                __zt_tmp = __attrs_140574255063568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'view/available', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9fe8a5490> name=None at 7fd9fe8a5710> -> __attrs_140574270401808
                __attrs_140574270401808 = _static_140574255109264
                __previous_i18n_domain_140574270402448 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portalMessage alert-box secondary warning">\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270602064
                __attrs_140574270602064 = _static_140574442558096

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140574270398736 = []
                __append_140574270398736 = __stream_140574270398736.append
                __append_140574270398736(u'Warning')
                __msgid_140574270398736 = __re_whitespace(''.join(__stream_140574270398736)).strip()
                if __msgid_140574270398736:
                    __append(translate(__msgid_140574270398736, mapping=None, default=__msgid_140574270398736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270599696
                __attrs_140574270599696 = _static_140574442558096

                # <Value u'not:view/can_migrate' (4:32)> -> __condition
                __token = 200
                try:
                    __zt_tmp = __attrs_140574270599696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('not', u'view/can_migrate', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270600208
                    __attrs_140574270600208 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140574270601680 = []
                    __append_140574270601680 = __stream_140574270601680.append
                    __append_140574270601680(u"You can't edit this content. Ask your administrator to migrate to Dexterity!")
                    __msgid_140574270601680 = __re_whitespace(''.join(__stream_140574270601680)).strip()
                    if __msgid_140574270601680:
                        __append(translate(__msgid_140574270601680, mapping=None, default=__msgid_140574270601680, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270601360
                __attrs_140574270601360 = _static_140574442558096

                # <Value u'view/can_migrate' (7:32)> -> __condition
                __token = 388
                try:
                    __zt_tmp = __attrs_140574270601360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'view/can_migrate', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266145872
                    __attrs_140574266145872 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140574284320352_migrate = ''
                    __stream_140574270602000 = []
                    __append_140574270602000 = __stream_140574270602000.append
                    __append_140574270602000(u"You can't edit this content unless you\n        ")
                    __stream_140574284320352_migrate = []
                    __append_140574284320352_migrate = __stream_140574284320352_migrate.append

                    # <Static value=<_ast.Dict object at 0x7fd9ff32bd10> name=None at 7fd9ff32bf90> -> __attrs_140574266143888
                    __attrs_140574266143888 = _static_140574266146064

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140574284320352_migrate(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266146448
                    __default_140574266146448 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/plone_portal_state/portal_url}/@@atct_migrator' (10:31)> -> __attr_href
                    __token = 565
                    try:
                        __zt_tmp = __attrs_140574266143888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('string', u'${context/plone_portal_state/portal_url}/@@atct_migrator', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140574284320352_migrate((u' href="%s"' % __attr_href))
                    __append_140574284320352_migrate(u'>')
                    __stream_140574266143504 = []
                    __append_140574266143504 = __stream_140574266143504.append
                    __append_140574266143504(u'\n          migrate the default content-types to Dexterity.\n        ')
                    __msgid_140574266143504 = __re_whitespace(''.join(__stream_140574266143504)).strip()
                    if __msgid_140574266143504:
                        __append_140574284320352_migrate(translate(__msgid_140574266143504, mapping=None, default=__msgid_140574266143504, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140574284320352_migrate(u'</a>')
                    __append_140574270602000(u'${migrate}')
                    __stream_140574284320352_migrate = ''.join(__stream_140574284320352_migrate)
                    __append_140574270602000(u'\n      ')
                    __msgid_140574270602000 = __re_whitespace(''.join(__stream_140574270602000)).strip()
                    if __msgid_140574270602000:
                        __append(translate(__msgid_140574270602000, mapping={u'migrate': __stream_140574284320352_migrate, }, default=__msgid_140574270602000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n    ')
                __append(u'\n  </div>')
                __i18n_domain = __previous_i18n_domain_140574270402448
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff76b810> name=None at 7fd9ff76b610> -> __attrs_140574255624912
                __attrs_140574255624912 = _static_140574270601232

                # <style ... (0:0)
                # --------------------------------------------------------
                __append(u'<style type="text/css">\n    #contentview-edit {display: None;}\n  </style>\n')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }