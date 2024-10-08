# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.locking-2.3.0-py2.7.egg/plone/locking/browser/info.pt'

__tokens = {77: (u'view/info/is_locked_for_current_user', 3, 24), 141: (u' view/lock_is_stealabl', 4, 26), 194: (u's view/lock_in', 5, 28), 238: (u'locked', 6, 24), 398: (u'lock_details/author_page', 11, 27), 647: (u'lock_details/author_page', 16, 34), 590: (u'lock_details/fullname', 15, 26), 738: (u'lock_details/time_difference', 18, 29), 858: (u'not:lock_details/author_page', 21, 27), 1060: (u'lock_details/fullname', 25, 29), 1148: (u'lock_details/time_difference', 27, 29), 1245: (u'stealable', 29, 29), 1293: (u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 30, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574267348624 = {u'type': u'submit', u'value': u'Unlock', }
_static_140574267459856 = {u'class': u'portalMessage info', }
_static_140574442558096 = {}
_static_140574268019152 = {u'action': u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', u'method': u'POST', }
_static_140574255063568 = {u'id': u'plone-lock-status', }
_static_140574397981968 = __compile_zt_expr
_static_140574268021456 = {u'href': u'lock_details/author_page', }

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

            # <Static value=<_ast.Dict object at 0x7fd9fe89a210> name=None at 7fd9fe89a550> -> __attrs_140574267435088
            __attrs_140574267435088 = _static_140574255063568
            __backup_locked_140574255076944 = get('locked', __marker)

            # <Value u'view/info/is_locked_for_current_user' (3:24)> -> __value
            __token = 77
            try:
                __zt_tmp = __attrs_140574267435088
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/info/is_locked_for_current_user', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_140574272095440 = get('stealable', __marker)

            # <Value u'view/lock_is_stealable' (4:26)> -> __value
            __token = 141
            try:
                __zt_tmp = __attrs_140574267435088
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/lock_is_stealable', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_140574255077136 = get('lock_details', __marker)

            # <Value u'view/lock_info' (5:28)> -> __value
            __token = 194
            try:
                __zt_tmp = __attrs_140574267435088
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/lock_info', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __previous_i18n_domain_140574266210448 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="plone-lock-status">\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257224400
            __attrs_140574257224400 = _static_140574442558096

            # <Value u'locked' (6:24)> -> __condition
            __token = 238
            try:
                __zt_tmp = __attrs_140574257224400
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'locked', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff46c910> name=None at 7fd9ff46c710> -> __attrs_140574267460496
                __attrs_140574267460496 = _static_140574267459856

                # <dl ... (0:0)
                # --------------------------------------------------------
                __append(u'<dl class="portalMessage info">\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267459088
                __attrs_140574267459088 = _static_140574442558096

                # <dt ... (0:0)
                # --------------------------------------------------------
                __append(u'<dt>')
                __stream_140574267458896 = []
                __append_140574267458896 = __stream_140574267458896.append
                __append_140574267458896(u'Locked')
                __msgid_140574267458896 = __re_whitespace(''.join(__stream_140574267458896)).strip()
                if u'label_locked':
                    __append(translate(u'label_locked', mapping=None, default=__msgid_140574267458896, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</dt>\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267460048
                __attrs_140574267460048 = _static_140574442558096

                # <dd ... (0:0)
                # --------------------------------------------------------
                __append(u'<dd>\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267458320
                __attrs_140574267458320 = _static_140574442558096

                # <Value u'lock_details/author_page' (11:27)> -> __condition
                __token = 398
                try:
                    __zt_tmp = __attrs_140574267458320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'lock_details/author_page', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:
                    __stream_140574237118784_author = ''
                    __stream_140574237118784_time = ''
                    __stream_140574267458448 = []
                    __append_140574267458448 = __stream_140574267458448.append
                    __append_140574267458448(u'\n          This item was locked by\n          ')
                    __stream_140574237118784_author = []
                    __append_140574237118784_author = __stream_140574237118784_author.append

                    # <Static value=<_ast.Dict object at 0x7fd9ff4f5ad0> name=None at 7fd9ff4f52d0> -> __attrs_140574269062352
                    __attrs_140574269062352 = _static_140574268021456

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140574237118784_author(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270568016
                    __default_140574270568016 = _DEFAULT_MARKER

                    # <Substitution u'lock_details/author_page' (16:34)> -> __attr_href
                    __token = 647
                    try:
                        __zt_tmp = __attrs_140574269062352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'lock_details/author_page', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140574237118784_author((u' href="%s"' % __attr_href))
                    __append_140574237118784_author(u'>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268019024
                    __default_140574268019024 = _DEFAULT_MARKER

                    # <Value u'lock_details/fullname' (15:26)> -> __cache_140574268022160
                    __token = 590
                    try:
                        __zt_tmp = __attrs_140574269062352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574268022160 = _static_140574397981968('path', u'lock_details/fullname', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/fullname' (15:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f5d50> -> __condition
                    __expression = __cache_140574268022160

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574268022160
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140574237118784_author(__content)
                    __append_140574237118784_author(u'</a>')
                    __append_140574267458448(u'${author}')
                    __stream_140574237118784_author = ''.join(__stream_140574237118784_author)
                    __append_140574267458448(u'\n          ')
                    __stream_140574237118784_time = []
                    __append_140574237118784_time = __stream_140574237118784_time.append

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269059664
                    __attrs_140574269059664 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140574237118784_time(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269059984
                    __default_140574269059984 = _DEFAULT_MARKER

                    # <Value u'lock_details/time_difference' (18:29)> -> __cache_140574269060048
                    __token = 738
                    try:
                        __zt_tmp = __attrs_140574269059664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574269060048 = _static_140574397981968('path', u'lock_details/time_difference', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/time_difference' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff5f3ad0> -> __condition
                    __expression = __cache_140574269060048

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574269060048
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140574237118784_time(__content)
                    __append_140574237118784_time(u'</span>')
                    __append_140574267458448(u'${time}')
                    __stream_140574237118784_time = ''.join(__stream_140574237118784_time)
                    __append_140574267458448(u' ago.\n        ')
                    __msgid_140574267458448 = __re_whitespace(''.join(__stream_140574267458448)).strip()
                    if u'description_webdav_locked_by_author_on_time':
                        __append(translate(u'description_webdav_locked_by_author_on_time', mapping={u'time': __stream_140574237118784_time, u'author': __stream_140574237118784_author, }, default=__msgid_140574267458448, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574269061776
                __attrs_140574269061776 = _static_140574442558096

                # <Value u'not:lock_details/author_page' (21:27)> -> __condition
                __token = 858
                try:
                    __zt_tmp = __attrs_140574269061776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('not', u'lock_details/author_page', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:
                    __stream_140574237118784_author = ''
                    __stream_140574237118784_time = ''
                    __stream_140574267459408 = []
                    __append_140574267459408 = __stream_140574267459408.append
                    __append_140574267459408(u'\n          This item was locked by\n          ')
                    __stream_140574237118784_author = []
                    __append_140574237118784_author = __stream_140574237118784_author.append

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284358672
                    __attrs_140574284358672 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140574237118784_author(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268021584
                    __default_140574268021584 = _DEFAULT_MARKER

                    # <Value u'lock_details/fullname' (25:29)> -> __cache_140574268021200
                    __token = 1060
                    try:
                        __zt_tmp = __attrs_140574284358672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574268021200 = _static_140574397981968('path', u'lock_details/fullname', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/fullname' (25:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f5e50> -> __condition
                    __expression = __cache_140574268021200

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574268021200
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140574237118784_author(__content)
                    __append_140574237118784_author(u'</span>')
                    __append_140574267459408(u'${author}')
                    __stream_140574237118784_author = ''.join(__stream_140574237118784_author)
                    __append_140574267459408(u'\n          ')
                    __stream_140574237118784_time = []
                    __append_140574237118784_time = __stream_140574237118784_time.append

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284473488
                    __attrs_140574284473488 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140574237118784_time(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270227408
                    __default_140574270227408 = _DEFAULT_MARKER

                    # <Value u'lock_details/time_difference' (27:29)> -> __cache_140574284361424
                    __token = 1148
                    try:
                        __zt_tmp = __attrs_140574284473488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574284361424 = _static_140574397981968('path', u'lock_details/time_difference', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/time_difference' (27:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff710d50> -> __condition
                    __expression = __cache_140574284361424

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574284361424
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140574237118784_time(__content)
                    __append_140574237118784_time(u'</span>')
                    __append_140574267459408(u'${time}')
                    __stream_140574237118784_time = ''.join(__stream_140574237118784_time)
                    __append_140574267459408(u' ago.\n        ')
                    __msgid_140574267459408 = __re_whitespace(''.join(__stream_140574267459408)).strip()
                    if u'description_webdav_locked_by_author_on_time':
                        __append(translate(u'description_webdav_locked_by_author_on_time', mapping={u'time': __stream_140574237118784_time, u'author': __stream_140574237118784_author, }, default=__msgid_140574267459408, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4f51d0> name=None at 7fd9ff4f5210> -> __attrs_140574270169680
                __attrs_140574270169680 = _static_140574268019152

                # <Value u'stealable' (29:29)> -> __condition
                __token = 1245
                try:
                    __zt_tmp = __attrs_140574270169680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'stealable', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270170128
                    __default_140574270170128 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (30:37)> -> __attr_action
                    __token = 1293
                    try:
                        __zt_tmp = __attrs_140574270169680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140574397981968('string', u'${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267349712
                    __attrs_140574267349712 = _static_140574442558096

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140574270516112_unlock_button = ''
                    __stream_140574267349008 = []
                    __append_140574267349008 = __stream_140574267349008.append
                    __append_140574267349008(u'\n            If you are certain this user has abandoned the object,\n            you may\n            ')
                    __stream_140574270516112_unlock_button = []
                    __append_140574270516112_unlock_button = __stream_140574270516112_unlock_button.append

                    # <Static value=<_ast.Dict object at 0x7fd9ff451690> name=None at 7fd9ff451590> -> __attrs_140574267347280
                    __attrs_140574267347280 = _static_140574267348624

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_140574270516112_unlock_button(u'<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267349200
                    __default_140574267349200 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7fd9ff451d50> at 7fd9ff451050> -> __attr_value
                    __attr_value = u'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append_140574270516112_unlock_button((u' value="%s"' % __attr_value))
                    __append_140574270516112_unlock_button(u' />')
                    __append_140574267349008(u'${unlock_button}')
                    __stream_140574270516112_unlock_button = ''.join(__stream_140574270516112_unlock_button)
                    __append_140574267349008(u'\n            the object. You will then be able to edit it.\n          ')
                    __msgid_140574267349008 = __re_whitespace(''.join(__stream_140574267349008)).strip()
                    if u'description_webdav_locked_steal':
                        __append(translate(u'description_webdav_locked_steal', mapping={u'unlock_button': __stream_140574270516112_unlock_button, }, default=__msgid_140574267349008, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        </form>')
                __append(u'\n      </dd>\n    </dl>\n  ')
            __append(u'\n</div>')
            __i18n_domain = __previous_i18n_domain_140574266210448
            if (__backup_lock_details_140574255077136 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_140574255077136
            if (__backup_stealable_140574272095440 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_140574272095440
            if (__backup_locked_140574255076944 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_140574255076944
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }