# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/globalstatusmessage.pt'

__tokens = {36: (u'view/messages', 1, 36), 86: (u'messages', 2, 35), 155: (u'message/type | nothing', 5, 25), 205: (u" python:{'error': 'danger'", 6, 26), 260: (u'y python:mapping.get(mtype, mtyp', 7, 26), 326: (u'string:alert alert-dismissible alert-${facility}', 8, 29), 564: (u'python:mtype.capitalize()', 14, 43), 666: (u'message/message | nothing', 18, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574270445520 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140574270445264 = {u'aria-hidden': u'true', }
_static_140574442558096 = {}
_static_140574270229776 = {u'class': u'content', }
_static_140574397981968 = __compile_zt_expr
_static_140574270452624 = {u'class': u'alert alert-info', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270453840
            __attrs_140574270453840 = _static_140574442558096
            __backup_messages_140574270566544 = get('messages', __marker)

            # <Value u'view/messages' (1:36)> -> __value
            __token = 36
            try:
                __zt_tmp = __attrs_140574270453840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/messages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['messages'] = __value
            __backup_message_140574267906128 = get('message', __marker)

            # <Value u'messages' (2:35)> -> __iterator
            __token = 86
            try:
                __zt_tmp = __attrs_140574270453840
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'messages', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574270452816, ) = getitem('repeat')(u'message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fd9ff747390> name=None at 7fd9ff747d90> -> __attrs_140574270454992
                __attrs_140574270454992 = _static_140574270452624
                __backup_mtype_140574270566736 = get('mtype', __marker)

                # <Value u'message/type | nothing' (5:25)> -> __value
                __token = 155
                try:
                    __zt_tmp = __attrs_140574270454992
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'message/type | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['mtype'] = __value
                __backup_mapping_140574270302480 = get('mapping', __marker)

                # <Value u"python:{'error': 'danger'}" (6:26)> -> __value
                __token = 205
                try:
                    __zt_tmp = __attrs_140574270454992
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"{'error': 'danger'}", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['mapping'] = __value
                __backup_facility_140574267915920 = get('facility', __marker)

                # <Value u'python:mapping.get(mtype, mtype)' (7:26)> -> __value
                __token = 260
                try:
                    __zt_tmp = __attrs_140574270454992
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'mapping.get(mtype, mtype)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['facility'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270455056
                __default_140574270455056 = _DEFAULT_MARKER

                # <Substitution u'string:alert alert-dismissible alert-${facility}' (8:29)> -> __attr_class
                __token = 326
                try:
                    __zt_tmp = __attrs_140574270454992
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140574397981968('string', u'alert alert-dismissible alert-${facility}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'alert alert-info', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff7457d0> name=None at 7fd9ff745690> -> __attrs_140574270444816
                __attrs_140574270444816 = _static_140574270445520

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff7456d0> name=None at 7fd9ff745dd0> -> __attrs_140574270445584
                __attrs_140574270445584 = _static_140574270445264

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n    </button>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270226704
                __attrs_140574270226704 = _static_140574442558096

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270226768
                __default_140574270226768 = _DEFAULT_MARKER

                # <Value u'python:mtype.capitalize()' (14:43)> -> __cache_140574270446864
                __token = 564
                try:
                    __zt_tmp = __attrs_140574270226704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574270446864 = _static_140574397981968('python', u'mtype.capitalize()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:mtype.capitalize()' (14:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff710790> -> __condition
                __expression = __cache_140574270446864

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n      Info\n    ')
                else:
                    __content = __cache_140574270446864
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</strong>\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff710d10> name=None at 7fd9ff7104d0> -> __attrs_140574270301136
                __attrs_140574270301136 = _static_140574270229776

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270302928
                __default_140574270302928 = _DEFAULT_MARKER

                # <Value u'message/message | nothing' (18:23)> -> __cache_140574267888976
                __token = 666
                try:
                    __zt_tmp = __attrs_140574270301136
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267888976 = _static_140574397981968('path', u'message/message | nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'message/message | nothing' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d5710> -> __condition
                __expression = __cache_140574267888976

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="content">\n      The status message.\n    </span>')
                else:
                    __content = __cache_140574267888976
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  </div>')
                if (__backup_facility_140574267915920 is __marker):
                    del econtext['facility']
                else:
                    econtext['facility'] = __backup_facility_140574267915920
                if (__backup_mapping_140574270302480 is __marker):
                    del econtext['mapping']
                else:
                    econtext['mapping'] = __backup_mapping_140574270302480
                if (__backup_mtype_140574270566736 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_140574270566736
                __append(u'\n\n')
                ____index_140574270452816 -= 1
                if (____index_140574270452816 > 0):
                    __append('')
            if (__backup_message_140574267906128 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_140574267906128
            if (__backup_messages_140574270566544 is __marker):
                del econtext['messages']
            else:
                econtext['messages'] = __backup_messages_140574270566544
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }