# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/worksheet_attachments.pt'

__tokens = {470: (u'python:view.get_attachments_view()', 15, 36), 607: (u'attachments_view/get_attachment_types', 19, 38), 675: (u' view/get_service', 20, 29), 723: (u's view/get_analys', 21, 28), 1007: (u'string:${context/absolute_url}/@@attachments_view/add_to_ws', 30, 37), 1197: (u'context/@@authenticator/authenticator', 34, 39), 2136: (u'attachment_types', 55, 45), 2204: (u'item/UID', 56, 50), 2256: (u'item/Title', 57, 41), 2606: (u'analyses', 66, 51), 2668: (u'analysis/uid', 67, 52), 2726: (u'analysis/title', 68, 43), 3074: (u'services', 77, 48), 3134: (u'service/uid', 78, 50), 3189: (u'service/title', 79, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168047846800 = {u'name': u'addWSAttachment', u'value': u'Add', u'id': u'addARButton', u'disabled': '', u'type': u'submit', u'class': u'context btn btn-secondary', }
_static_140168047874384 = {u'id': u'ws-attachments-panel', u'class': u'collapse card p-2 mb-3 bg-light', }
_static_140168047370896 = {u'id': u'ws-attachments', u'class': u'attachments', }
_static_140168047872144 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140168037966096 = {u'class': u'pr-3', }
_static_140168038015376 = {u'onchange': u"string:document.getElementById('addARButton').disabled=false", u'type': u'file', u'name': u'AttachmentFile_file', }
_static_140168047659600 = {u'value': u'', }
_static_140168047082448 = {u'class': u'form-control', u'name': u'AttachmentType', }
_static_140168083190416 = {u'value': u'service/uid', }
_static_140168038070544 = {u'class': u'form-group', }
_static_140168047872848 = {u'action': u'attachments_view', u'method': u'POST', u'name': u'attachments_add_form', u'enctype': u'multipart/form-data', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047051408 = {u'class': u'pr-3', }
_static_140168047849424 = {u'id': u'Service', u'class': u'form-control', u'name': u'Service', }
_static_140168037966672 = {u'class': u'form-group', }
_static_140168047874448 = {u'class': u'ws_attachments_add', }
_static_140168047845840 = {u'class': u'form-group', }
_static_140168047530960 = {u'data-toggle': u'collapse', u'type': u'button', u'class': u'btn btn-light dropdown-toggle mb-3', u'data-target': u'#ws-attachments-panel', }
_static_140168047741520 = {u'class': u'form-control', u'name': u'AttachmentKeys', }
_static_140168047739344 = {u'class': u'form-group', }
_static_140168257770128 = {}
_static_140168083172624 = {u'value': u'analysis/uid', }
_static_140168038068944 = {u'id': u'Analysis', u'class': u'form-control', u'name': u'Analysis', }
_static_140168208991440 = __compile_zt_expr
_static_140168047053776 = {u'class': u'pr-3', }
_static_140168047533840 = {u'class': u'fas fa-paperclip', u'aria-hidden': u'true', }
_static_140168038015760 = {u'class': u'form-group', }
_static_140168047080912 = {u'value': u'item/UID', }
_static_140168047051216 = {u'class': u'pr-3', }
_static_140168047876880 = {u'class': u'panel-body', }
_static_140168083143632 = {u'value': u'', }
_static_140168047051536 = {u'class': u'pr-3', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6aac2290> name=None at 7f7b6aac2550> -> __attrs_140168047531216
            __attrs_140168047531216 = _static_140168047370896
            __previous_i18n_domain_140168047530640 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="ws-attachments" class="attachments">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6aae93d0> name=None at 7f7b6aae9390> -> __attrs_140168047533392
            __attrs_140168047533392 = _static_140168047530960

            # <button ... (0:0)
            # --------------------------------------------------------
            __append(u'<button type="button" class="btn btn-light dropdown-toggle mb-3" data-toggle="collapse" data-target="#ws-attachments-panel">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6aae9f10> name=None at 7f7b6aae9ed0> -> __attrs_140168097160400
            __attrs_140168097160400 = _static_140168047533840

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-paperclip" aria-hidden="true"/>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047875024
            __attrs_140168047875024 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168067778256 = []
            __append_140168067778256 = __stream_140168067778256.append
            __append_140168067778256(u'Attachments')
            __msgid_140168067778256 = __re_whitespace(''.join(__stream_140168067778256)).strip()
            if __msgid_140168067778256:
                __append(translate(__msgid_140168067778256, mapping=None, default=__msgid_140168067778256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n  </button>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab3d150> name=None at 7f7b6aae9d90> -> __attrs_140168047875664
            __attrs_140168047875664 = _static_140168047874384
            __backup_attachments_view_140168047872912 = get('attachments_view', __marker)

            # <Value u'python:view.get_attachments_view()' (15:36)> -> __value
            __token = 470
            try:
                __zt_tmp = __attrs_140168047875664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.get_attachments_view()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['attachments_view'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="ws-attachments-panel" class="collapse card p-2 mb-3 bg-light">\n\n    <!-- Attachments Viewlet -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab3db10> name=None at 7f7b6ab3db90> -> __attrs_140168047877840
            __attrs_140168047877840 = _static_140168047876880
            __backup_attachment_types_140168047372240 = get('attachment_types', __marker)

            # <Value u'attachments_view/get_attachment_types' (19:38)> -> __value
            __token = 607
            try:
                __zt_tmp = __attrs_140168047877840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/get_attachment_types', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['attachment_types'] = __value
            __backup_services_140168047870864 = get('services', __marker)

            # <Value u'view/get_services' (20:29)> -> __value
            __token = 675
            try:
                __zt_tmp = __attrs_140168047877840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'view/get_services', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['services'] = __value
            __backup_analyses_140168047373328 = get('analyses', __marker)

            # <Value u'view/get_analyses' (21:28)> -> __value
            __token = 723
            try:
                __zt_tmp = __attrs_140168047877840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'view/get_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['analyses'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="panel-body">\n\n      <!-- Add Attachments -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab3d190> name=None at 7f7b6ab3d350> -> __attrs_140168047871568
            __attrs_140168047871568 = _static_140168047874448

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="ws_attachments_add">\n\n        <!-- Add Form -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab3cb50> name=None at 7f7b6ab3cbd0> -> __attrs_140168047870160
            __attrs_140168047870160 = _static_140168047872848

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047873744
            __default_140168047873744 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/@@attachments_view/add_to_ws' (30:37)> -> __attr_action
            __token = 1007
            try:
                __zt_tmp = __attrs_140168047870160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140168208991440('string', u'${context/absolute_url}/@@attachments_view/add_to_ws', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'attachments_view', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' name="attachments_add_form" enctype="multipart/form-data" method="POST">\n\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab3c890> name=None at 7f7b6bf184d0> -> __attrs_140168047378960
            __attrs_140168047378960 = _static_140168047872144

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="submitted" value="1"/>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047380368
            __attrs_140168047380368 = _static_140168257770128

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047380880
            __default_140168047380880 = _DEFAULT_MARKER

            # <Value u'context/@@authenticator/authenticator' (34:39)> -> __cache_140168047379280
            __token = 1197
            try:
                __zt_tmp = __attrs_140168047380368
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168047379280 = _static_140168208991440('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/@@authenticator/authenticator' (34:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aac4a50> -> __condition
            __expression = __cache_140168047379280

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            else:
                __content = __cache_140168047379280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047381968
            __attrs_140168047381968 = _static_140168257770128

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047380304
            __attrs_140168047380304 = _static_140168257770128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa741d0> name=None at 7f7b6aa74710> -> __attrs_140168047054672
            __attrs_140168047054672 = _static_140168047051216

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th class="pr-3">')
            __stream_140168087967440 = []
            __append_140168087967440 = __stream_140168087967440.append
            __append_140168087967440(u'Add new Attachment')
            __msgid_140168087967440 = __re_whitespace(''.join(__stream_140168087967440)).strip()
            if __msgid_140168087967440:
                __append(translate(__msgid_140168087967440, mapping=None, default=__msgid_140168087967440, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa74bd0> name=None at 7f7b6aa74e90> -> __attrs_140168047052752
            __attrs_140168047052752 = _static_140168047053776

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th class="pr-3">')
            __stream_140168047051920 = []
            __append_140168047051920 = __stream_140168047051920.append
            __append_140168047051920(u'Type')
            __msgid_140168047051920 = __re_whitespace(''.join(__stream_140168047051920)).strip()
            if __msgid_140168047051920:
                __append(translate(__msgid_140168047051920, mapping=None, default=__msgid_140168047051920, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa74310> name=None at 7f7b6aa74850> -> __attrs_140168047052688
            __attrs_140168047052688 = _static_140168047051536

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th class="pr-3">')
            __stream_140168047053712 = []
            __append_140168047053712 = __stream_140168047053712.append
            __append_140168047053712(u'Analysis')
            __msgid_140168047053712 = __re_whitespace(''.join(__stream_140168047053712)).strip()
            if __msgid_140168047053712:
                __append(translate(__msgid_140168047053712, mapping=None, default=__msgid_140168047053712, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa74290> name=None at 7f7b6aa74a10> -> __attrs_140168037968208
            __attrs_140168037968208 = _static_140168047051408

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th class="pr-3">')
            __stream_140168047052432 = []
            __append_140168047052432 = __stream_140168047052432.append
            __append_140168047052432(u'All Analyses of Service')
            __msgid_140168047052432 = __re_whitespace(''.join(__stream_140168047052432)).strip()
            if __msgid_140168047052432:
                __append(translate(__msgid_140168047052432, mapping=None, default=__msgid_140168047052432, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1ca110> name=None at 7f7b6a1ca890> -> __attrs_140168037968912
            __attrs_140168037968912 = _static_140168037966096

            # <th ... (0:0)
            # --------------------------------------------------------
            __append(u'<th class="pr-3">')
            __stream_140168037966864 = []
            __append_140168037966864 = __stream_140168037966864.append
            __append_140168037966864(u'Keywords')
            __msgid_140168037966864 = __re_whitespace(''.join(__stream_140168037966864)).strip()
            if __msgid_140168037966864:
                __append(translate(__msgid_140168037966864, mapping=None, default=__msgid_140168037966864, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</th>\n            </tr>\n            ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037968720
            __attrs_140168037968720 = _static_140168257770128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037969424
            __attrs_140168037969424 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1ca350> name=None at 7f7b6a1ca590> -> __attrs_140168038017360
            __attrs_140168038017360 = _static_140168037966672

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n                  <!-- Attachment File Upload -->\n                  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1d6190> name=None at 7f7b6a1d6110> -> __attrs_140168038016720
            __attrs_140168038016720 = _static_140168038015376

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="file" name="AttachmentFile_file" onchange="string:document.getElementById(\'addARButton\').disabled=false"/>\n                </div>\n              </td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168038018896
            __attrs_140168038018896 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1d6310> name=None at 7f7b6a1d6c50> -> __attrs_140168080348816
            __attrs_140168080348816 = _static_140168038015760

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa7bbd0> name=None at 7f7b6aa7b890> -> __attrs_140168047080592
            __attrs_140168047080592 = _static_140168047082448

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select class="form-control" name="AttachmentType">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f7b6aa7b5d0> name=None at 7f7b6aa7bdd0> -> __attrs_140168047082256
            __attrs_140168047082256 = _static_140168047080912
            __backup_item_140168047080848 = get('item', __marker)

            # <Value u'attachment_types' (55:45)> -> __iterator
            __token = 2136
            try:
                __zt_tmp = __attrs_140168047082256
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('path', u'attachment_types', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168047080976, ) = getitem('repeat')(u'item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047080336
                __default_140168047080336 = _DEFAULT_MARKER

                # <Substitution u'item/UID' (56:50)> -> __attr_value
                __token = 2204
                try:
                    __zt_tmp = __attrs_140168047082256
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047082768
                __default_140168047082768 = _DEFAULT_MARKER

                # <Value u'item/Title' (57:41)> -> __cache_140168047081296
                __token = 2256
                try:
                    __zt_tmp = __attrs_140168047082256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047081296 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'item/Title' (57:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa7be50> -> __condition
                __expression = __cache_140168047081296

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047081296
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</option>')
                ____index_140168047080976 -= 1
                if (____index_140168047080976 > 0):
                    __append('\n                    ')
            if (__backup_item_140168047080848 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140168047080848
            __append(u'\n                  </select>\n                </div>\n              </td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047083472
            __attrs_140168047083472 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168038069776
            __attrs_140168038069776 = _static_140168257770128
            __append(u'\n                  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1e3910> name=None at 7f7b6a1e3f10> -> __attrs_140168038070928
            __attrs_140168038070928 = _static_140168038070544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1e32d0> name=None at 7f7b6a1e3810> -> __attrs_140168038069200
            __attrs_140168038069200 = _static_140168038068944

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select class="form-control" name="Analysis" id="Analysis">\n                      ')

            # <Static value=<_ast.Dict object at 0x7f7b6ccdfbd0> name=None at 7f7b6ccdf6d0> -> __attrs_140168047737296
            __attrs_140168047737296 = _static_140168083143632

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value=""/>\n                      ')

            # <Static value=<_ast.Dict object at 0x7f7b6cce6d10> name=None at 7f7b6cce6c90> -> __attrs_140168082150480
            __attrs_140168082150480 = _static_140168083172624
            __backup_analysis_140168047082704 = get('analysis', __marker)

            # <Value u'analyses' (66:51)> -> __iterator
            __token = 2606
            try:
                __zt_tmp = __attrs_140168082150480
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('path', u'analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168047847504, ) = getitem('repeat')(u'analysis', __iterator)
            econtext['analysis'] = None
            for __item in __iterator:
                econtext['analysis'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168068330192
                __default_140168068330192 = _DEFAULT_MARKER

                # <Substitution u'analysis/uid' (67:52)> -> __attr_value
                __token = 2668
                try:
                    __zt_tmp = __attrs_140168082150480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'analysis/uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168083081424
                __default_140168083081424 = _DEFAULT_MARKER

                # <Value u'analysis/title' (68:43)> -> __cache_140168047736336
                __token = 2726
                try:
                    __zt_tmp = __attrs_140168082150480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047736336 = _static_140168208991440('path', u'analysis/title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'analysis/title' (68:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6d36ead0> -> __condition
                __expression = __cache_140168047736336

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047736336
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</option>')
                ____index_140168047847504 -= 1
                if (____index_140168047847504 > 0):
                    __append('\n                      ')
            if (__backup_analysis_140168047082704 is __marker):
                del econtext['analysis']
            else:
                econtext['analysis'] = __backup_analysis_140168047082704
            __append(u'\n                    </select>\n                  </div>\n                \n              </td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168038071568
            __attrs_140168038071568 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab361d0> name=None at 7f7b6a1e3950> -> __attrs_140168047846928
            __attrs_140168047846928 = _static_140168047845840

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab36fd0> name=None at 7f7b6ab36c50> -> __attrs_140168047845456
            __attrs_140168047845456 = _static_140168047849424

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select class="form-control" name="Service" id="Service">\n                    ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab08a50> name=None at 7f7b6ab08e50> -> __attrs_140168047660880
            __attrs_140168047660880 = _static_140168047659600

            # <option ... (0:0)
            # --------------------------------------------------------
            __append(u'<option value=""/>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f7b6cceb290> name=None at 7f7b6cb565d0> -> __attrs_140168047739088
            __attrs_140168047739088 = _static_140168083190416
            __backup_service_140168047083344 = get('service', __marker)

            # <Value u'services' (77:48)> -> __iterator
            __token = 3074
            try:
                __zt_tmp = __attrs_140168047739088
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('path', u'services', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168047739152, ) = getitem('repeat')(u'service', __iterator)
            econtext['service'] = None
            for __item in __iterator:
                econtext['service'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168081586128
                __default_140168081586128 = _DEFAULT_MARKER

                # <Substitution u'service/uid' (78:50)> -> __attr_value
                __token = 3134
                try:
                    __zt_tmp = __attrs_140168047739088
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('path', u'service/uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168081539856
                __default_140168081539856 = _DEFAULT_MARKER

                # <Value u'service/title' (79:41)> -> __cache_140168047658320
                __token = 3189
                try:
                    __zt_tmp = __attrs_140168047739088
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047658320 = _static_140168208991440('path', u'service/title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'service/title' (79:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6bf08610> -> __condition
                __expression = __cache_140168047658320

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047658320
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</option>')
                ____index_140168047739152 -= 1
                if (____index_140168047739152 > 0):
                    __append('\n                    ')
            if (__backup_service_140168047083344 is __marker):
                del econtext['service']
            else:
                econtext['service'] = __backup_service_140168047083344
            __append(u'\n                  </select>\n                </div>\n              </td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047847568
            __attrs_140168047847568 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n                ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab1c1d0> name=None at 7f7b6ab1c890> -> __attrs_140168047741840
            __attrs_140168047741840 = _static_140168047739344

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-group">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab1ca50> name=None at 7f7b6ab1cc90> -> __attrs_140168047742928
            __attrs_140168047742928 = _static_140168047741520

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input class="form-control" name="AttachmentKeys"/>\n                </div>\n              </td>\n            </tr>\n          </table>\n          <!-- Add Attachment Button -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab36590> name=None at 7f7b6ab36b50> -> __attrs_140168166155984
            __attrs_140168166155984 = _static_140168047846800

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input disabled class="context btn btn-secondary" id="addARButton" type="submit" name="addWSAttachment"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168166157712
            __default_140168166157712 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7f7b71c0a710> at 7f7b71c0afd0> -> __attr_value
            __attr_value = u'Add'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'/>\n        </form> <!-- /Add Attachment Form -->\n      </div>\n    </div>')
            if (__backup_analyses_140168047373328 is __marker):
                del econtext['analyses']
            else:
                econtext['analyses'] = __backup_analyses_140168047373328
            if (__backup_services_140168047870864 is __marker):
                del econtext['services']
            else:
                econtext['services'] = __backup_services_140168047870864
            if (__backup_attachment_types_140168047372240 is __marker):
                del econtext['attachment_types']
            else:
                econtext['attachment_types'] = __backup_attachment_types_140168047372240
            __append(u'\n  </div>')
            if (__backup_attachments_view_140168047872912 is __marker):
                del econtext['attachments_view']
            else:
                econtext['attachments_view'] = __backup_attachments_view_140168047872912
            __append(u' <!-- Collapsible content -->\n</div>')
            __i18n_domain = __previous_i18n_domain_140168047530640
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }