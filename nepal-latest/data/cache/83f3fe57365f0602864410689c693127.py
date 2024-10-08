# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/sample_dispatched_viewlet.pt'

__tokens = {41: (u'python: view.is_dispatched()', 2, 20), 154: (u'python:view.get_state_info()', 6, 24), 584: (u'info/actor', 13, 82), 647: (u'info/date', 14, 46), 756: (u'info/comments', 18, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047616592 = {u'aria-hidden': u'true', }
_static_140168046982992 = {u'class': u'portlet-alert-item alert alert-secondary alert-dismissible', }
_static_140168047619216 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168257770128 = {}
_static_140168047122064 = {u'class': u'title', }
_static_140168046985168 = {u'id': u'portal-alert', }
_static_140168037566928 = {u'class': u'description', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046984720
            __attrs_140168046984720 = _static_140168257770128

            # <Value u'python: view.is_dispatched()' (2:20)> -> __condition
            __token = 41
            try:
                __zt_tmp = __attrs_140168046984720
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u' view.is_dispatched()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168046985104 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa63fd0> name=None at 7f7b6aa63d10> -> __attrs_140168046982160
                __attrs_140168046982160 = _static_140168046985168
                __backup_info_140168026330576 = get('info', __marker)

                # <Value u'python:view.get_state_info()' (6:24)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_140168046982160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.get_state_info()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['info'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa63750> name=None at 7f7b6aa63310> -> __attrs_140168047361872
                __attrs_140168047361872 = _static_140168046982992

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-secondary alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aafec90> name=None at 7f7b6aafe050> -> __attrs_140168047619728
                __attrs_140168047619728 = _static_140168047619216

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aafe250> name=None at 7f7b6aafed50> -> __attrs_140168047122320
                __attrs_140168047122320 = _static_140168047616592

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa85690> name=None at 7f7b6aabf290> -> __attrs_140168047121232
                __attrs_140168047121232 = _static_140168047122064

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047122704
                __attrs_140168047122704 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168016706448_actor = ''
                __stream_140168016706448_date = ''
                __stream_140168047121040 = []
                __append_140168047121040 = __stream_140168047121040.append
                __append_140168047121040(u'\n          This sample has been dispatched by ')
                __stream_140168016706448_actor = []
                __append_140168016706448_actor = __stream_140168016706448_actor.append

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026332688
                __attrs_140168026332688 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026332240
                __default_140168026332240 = _DEFAULT_MARKER

                # <Value u'info/actor' (13:82)> -> __cache_140168047124368
                __token = 584
                try:
                    __zt_tmp = __attrs_140168026332688
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047124368 = _static_140168208991440('path', u'info/actor', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'info/actor' (13:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b1bd0> -> __condition
                __expression = __cache_140168047124368

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140168016706448_actor(u'<span/>')
                else:
                    __content = __cache_140168047124368
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140168016706448_actor(__content)
                __append_140168047121040(u'${actor}')
                __stream_140168016706448_actor = ''.join(__stream_140168016706448_actor)
                __append_140168047121040(u' on\n          ')
                __stream_140168016706448_date = []
                __append_140168016706448_date = __stream_140168016706448_date.append

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168083151760
                __attrs_140168083151760 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047736912
                __default_140168047736912 = _DEFAULT_MARKER

                # <Value u'info/date' (14:46)> -> __cache_140168026329296
                __token = 647
                try:
                    __zt_tmp = __attrs_140168083151760
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168026329296 = _static_140168208991440('path', u'info/date', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'info/date' (14:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b1410> -> __condition
                __expression = __cache_140168026329296

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140168016706448_date(u'<span/>')
                else:
                    __content = __cache_140168026329296
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140168016706448_date(__content)
                __append_140168047121040(u'${date}')
                __stream_140168016706448_date = ''.join(__stream_140168016706448_date)
                __append_140168047121040(u'\n        ')
                __msgid_140168047121040 = __re_whitespace(''.join(__stream_140168047121040)).strip()
                if u'this_sample_has_been_dispatched_by':
                    __append(translate(u'this_sample_has_been_dispatched_by', mapping={u'date': __stream_140168016706448_date, u'actor': __stream_140168016706448_actor, }, default=__msgid_140168047121040, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      </p>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1689d0> name=None at 7f7b6a168050> -> __attrs_140168037565968
                __attrs_140168037565968 = _static_140168037566928

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="description">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037564624
                __attrs_140168037564624 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037566160
                __default_140168037566160 = _DEFAULT_MARKER

                # <Value u'info/comments' (18:37)> -> __cache_140168037566352
                __token = 756
                try:
                    __zt_tmp = __attrs_140168037564624
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037566352 = _static_140168208991440('path', u'info/comments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'info/comments' (18:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a168c10> -> __condition
                __expression = __cache_140168037566352

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168037566352
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n      </p>\n    </div>\n  </div>')
                if (__backup_info_140168026330576 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140168026330576
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140168046985104
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }