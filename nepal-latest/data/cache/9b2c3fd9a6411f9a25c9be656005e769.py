# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/attachments.pt'

__tokens = {508: (u'python:view.get_attachments_view()', 15, 36), 416: (u'string:card p-2 mb-3 bg-light ${view/toggle_css_class}', 14, 29), 1072: (u'attachments_view/can_add_attachments', 40, 29), 1139: (u' attachments_view/can_edit_attachment', 41, 29), 1209: (u'e attachments_view/can_delete_attachmen', 42, 30), 1282: (u'ts attachments_view/get_sorted_attachme', 43, 30), 1360: (u'pes attachments_view/get_attachment_t', 44, 34), 1802: (u'attachments', 53, 29), 1715: (u'string:${context/absolute_url}/@@attachments_view/update', 52, 37), 1993: (u'context/@@authenticator/authenticator', 58, 39), 2821: (u'can_delete', 72, 66), 2947: (u'attachments', 76, 41), 3224: (u'string:${attachment/absolute_url}/at_download/AttachmentFile', 82, 43), 3321: (u'attachment/name', 83, 35), 3450: (u'string:attachments.UID:records', 86, 60), 3542: (u' string:${attachment/UID', 87, 60), 3665: (u'string:order:list', 90, 60), 3744: (u' string:${attachment/UID', 91, 60), 4020: (u'can_edit', 98, 41), 4077: (u'string:attachments.AttachmentType:records', 99, 47), 4181: (u' string:${attachment/UID', 100, 61), 4257: (u'attachment_types', 101, 47), 4327: (u'item/UID', 102, 52), 4391: (u" python:item.UID==attachment['type_uid'", 103, 54), 4476: (u'item/Title', 104, 43), 4557: (u'not:can_edit', 106, 39), 4608: (u'attachment/type', 107, 37), 4792: (u'attachment/size', 112, 54), 4985: (u'attachment/analysis', 117, 54), 5260: (u'can_edit', 124, 40), 5316: (u'string:attachments.AttachmentKeys:records', 125, 46), 5405: (u' attachment/keyword', 126, 46), 5469: (u'not:can_edit', 127, 39), 5520: (u'attachment/keywords', 128, 37), 5683: (u"python:attachment.get('render_in_report', False)", 132, 49), 5821: (u'string:attachments.RenderInReport:records:boolean', 134, 46), 5920: (u' python:render_in_repor', 135, 48), 6034: (u'string:attachments.RenderInReport:records:boolean:default', 137, 46), 6139: (u' python:Fals', 138, 46), 6238: (u'not:can_edit', 140, 39), 6289: (u"python:'Yes' if attachment.get('can_edit') else 'No'", 141, 37), 6429: (u'can_delete', 144, 61), 6666: (u'attachment/can_edit', 149, 41), 6734: (u'string:attachments.delete:records:boolean', 150, 47), 6824: (u' python:Tru', 151, 47), 6925: (u'string:attachments.delete:records:boolean:default', 153, 45), 7021: (u' python:Fals', 154, 45), 7221: (u'can_edit', 161, 56), 7890: (u'can_edit', 177, 32), 8093: (u'can_add', 186, 26), 8332: (u'string:${context/absolute_url}/@@attachments_view/add', 193, 37), 8516: (u'context/@@authenticator/authenticator', 197, 39), 9590: (u'attachment_types', 221, 45), 9658: (u'item/UID', 222, 50), 9710: (u'item/Title', 223, 41), 9961: (u'attachments_view/get_analyses', 230, 43), 10036: (u" python:[a for a in analyses if a.portal_type == 'Analysis'", 231, 44), 10133: (u"c python:[a for a in analyses if a.portal_type == 'ReferenceAnalysis", 232, 35), 10247: (u'es python:[a for a in bc if a.aq_parent.getBlank', 233, 42), 10341: (u'ses python:[a for a in bc if not a.aq_parent.getBlan', 234, 41), 10439: (u"yses python:[a for a in analyses if a.portal_type == 'DuplicateAnaly", 235, 40), 10598: (u'analyses', 236, 82), 10832: (u'python:None', 240, 54), 10892: (u'python:True', 241, 46), 11061: (u'a_analyses', 244, 48), 11130: (u'item/UID', 245, 56), 11188: (u'item/Title', 246, 47), 11283: (u'b_analyses', 248, 48), 11352: (u'item/UID', 249, 56), 11411: (u'item/Title', 250, 47), 11644: (u'c_analyses', 255, 48), 11713: (u'item/UID', 256, 56), 11772: (u'item/Title', 257, 47), 12007: (u'd_analyses', 262, 48), 12076: (u'item/UID', 263, 56), 12135: (u'item/Title', 264, 47), 12793: (u'python:True', 280, 47), 12958: (u'python:False', 283, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168047766736 = {u'id': u'ar-attachments', u'class': u'attachments', }
_static_140168026274192 = {u'type': u'text/css', }
_static_140168047337744 = {u'value': u'item/UID', }
_static_140168046998736 = {u'class': u'attachment-keywords', }
_static_140168047009488 = {u'class': u'formHelp discreet', }
_static_140168026327440 = {u'class': u'pr-3', }
_static_140168047618832 = {u'class': u'pr-3', }
_static_140168047022992 = {u'class': u'filesize', }
_static_140168037645136 = {u'class': u'pr-3', }
_static_140168016906704 = {u'onchange': u"string:document.getElementById('addARButton').disabled=false", u'type': u'file', u'id': u'AttachmentFile_file', u'name': u'AttachmentFile_file', }
_static_140168037443728 = {u'type': u'hidden', u'name': u'string:order:list', u'value': u'string:${attachment/UID}', }
_static_140168016934736 = {u'class': u'pr-3', }
_static_140168026337488 = {u'class': u'attachment-link', }
_static_140168047808464 = {u'value': u'item/UID', }
_static_140168046997776 = {u'class': u'analysis', }
_static_140168047171472 = {u'value': u'Update Attachments', u'type': u'submit', u'class': u'btn btn-secondary context', u'name': u'updateARAttachment', u'id': u'updateButton', }
_static_140168026273232 = {u'type': u'text/javascript', }
_static_140168026366352 = {u'class': u'panel-body', }
_static_140168037591824 = {u'selected': u"python:item.UID==attachment['type_uid']", u'value': u'item/UID', }
_static_140168026309584 = {u'class': u'pr-3', }
_static_140168025889232 = {u'value': u'item/UID', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168037650832 = {u'class': u'pr-3', }
_static_140168025889744 = {u'value': u'item/UID', }
_static_140168047009424 = {u'checked': u'python:render_in_report', u'type': u'checkbox', u'name': u'string:attachments.RenderInReport:records:boolean', }
_static_140168047842320 = {u'class': u'form-control', u'name': u'AttachmentKeys', }
_static_140168026325904 = {u'class': u'pr-3', }
_static_140168016933008 = {u'class': u'pr-3', }
_static_140168037496016 = {u'class': u'attachment-field-size', }
_static_140168047288848 = {u'class': u'text-center', }
_static_140168047340432 = {u'class': u'formHelp discreet', }
_static_140168016765712 = {u'type': u'checkbox', u'name': u'string:attachments.delete:records:boolean', u'value': u'python:True', }
_static_140168047357904 = {u'name': u'Analysis', u'class': u'form-control', }
_static_140168047120528 = {u'id': u'attachments_update_table', }
_static_140168026384272 = {u'data-toggle': u'collapse', u'type': u'button', u'class': u'btn btn-light dropdown-toggle mb-3', u'data-target': u'#ar-attachments-panel', }
_static_140168047811920 = {u'id': u'attachments_add', u'class': u'ar_attachments_list', }
_static_140168036614288 = {u'class': u'attachment-delete', }
_static_140168026329936 = {u'class': u'pr-3', }
_static_140168046976720 = {u'disabled': u'disabled', u'selected': u'selected', u'value': u'python:None', }
_static_140168047619216 = {u'class': u'pr-3', }
_static_140168036700496 = {u'name': u'AttachmentType', u'class': u'form-control', }
_static_140168016765072 = {u'type': u'hidden', u'name': u'string:attachments.delete:records:boolean:default', u'value': u'python:False', }
_static_140168047839504 = {u'action': u'attachments_view', u'method': u'POST', u'name': u'attachments_add_form', u'enctype': u'multipart/form-data', }
_static_140168257770128 = {}
_static_140168026309264 = {u'id': u'attachments_add_table', }
_static_140168047030544 = {u'href': u'string:${attachment/absolute_url}/at_download/AttachmentFile', u'title': u'Click to download', }
_static_140168047409488 = {u'type': u'hidden', u'name': u'RenderInReport:boolean:default', u'value': u'python:False', }
_static_140168037564112 = {u'class': u'fas fa-paperclip', u'aria-hidden': u'true', }
_static_140168047410704 = {u'type': u'checkbox', u'name': u'RenderInReport:boolean', u'value': u'python:True', }
_static_140168208991440 = __compile_zt_expr
_static_140168037561424 = {u'id': u'ar-attachments-panel', u'class': u'string:card p-2 mb-3 bg-light ${view/toggle_css_class}', }
_static_140168047024912 = {u'class': u'attachment-analysis', }
_static_140168016946384 = {u'id': u'attachments_update', u'class': u'ar_attachments_list', }
_static_140168046859728 = {u'name': u'AttachmentKeys', u'value': u'attachment/keywords', u'class': u'form-control', }
_static_140168036615056 = {u'type': u'hidden', u'name': u'string:attachments.RenderInReport:records:boolean:default', u'value': u'python:False', }
_static_140168026340624 = {u'class': u'fa fa-paperclip', u'aria-hidden': u'true', }
_static_140168037444176 = {u'class': u'attachment-type', }
_static_140168047351952 = {u'name': u'addARAttachment', u'value': u'Add Attachment', u'id': u'addARButton', u'disabled': '', u'type': u'submit', u'class': u'context btn btn-secondary', }
_static_140168046846800 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140168016946448 = {u'action': u'attachments_view/update', u'method': u'POST', u'name': u'attachments_update_form', u'enctype': u'multipart/form-data', }
_static_140168037626960 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140168047292304 = {u'value': u'item/UID', }
_static_140168046858512 = {u'class': u'attachment-render-in-report text-center', }
_static_140168016907024 = {u'class': u'pr-3', }
_static_140168047815056 = {u'type': u'hidden', u'name': u'string:attachments.UID:records', u'value': u'string:${attachment/UID}', }
_static_140168016934992 = {u'class': u'pr-3', }
_static_140168037525008 = {u'data-attachment-uid': u'string:${attachment/UID}', u'name': u'AttachmentType', u'class': u'form-control', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6ab22cd0> name=None at 7f7b6ab22fd0> -> __attrs_140168037619920
            __attrs_140168037619920 = _static_140168047766736
            __previous_i18n_domain_140168037620368 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="ar-attachments" class="attachments">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b696be790> name=None at 7f7b696be250> -> __attrs_140168026384208
            __attrs_140168026384208 = _static_140168026384272

            # <button ... (0:0)
            # --------------------------------------------------------
            __append(u'<button type="button" class="btn btn-light dropdown-toggle mb-3" data-toggle="collapse" data-target="#ar-attachments-panel">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b6a167ed0> name=None at 7f7b6a167510> -> __attrs_140168037562512
            __attrs_140168037562512 = _static_140168037564112

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-paperclip" aria-hidden="true"/>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037563088
            __attrs_140168037563088 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168037563280 = []
            __append_140168037563280 = __stream_140168037563280.append
            __append_140168037563280(u'Attachments')
            __msgid_140168037563280 = __re_whitespace(''.join(__stream_140168037563280)).strip()
            if __msgid_140168037563280:
                __append(translate(__msgid_140168037563280, mapping=None, default=__msgid_140168037563280, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n  </button>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a167450> name=None at 7f7b6a167790> -> __attrs_140168026274000
            __attrs_140168026274000 = _static_140168037561424
            __backup_attachments_view_140168047413584 = get('attachments_view', __marker)

            # <Value u'python:view.get_attachments_view()' (15:36)> -> __value
            __token = 508
            try:
                __zt_tmp = __attrs_140168026274000
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.get_attachments_view()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['attachments_view'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="ar-attachments-panel"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026262544
            __default_140168026262544 = _DEFAULT_MARKER

            # <Substitution u'string:card p-2 mb-3 bg-light ${view/toggle_css_class}' (14:29)> -> __attr_class
            __token = 416
            try:
                __zt_tmp = __attrs_140168026274000
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140168208991440('string', u'card p-2 mb-3 bg-light ${view/toggle_css_class}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b696a35d0> name=None at 7f7b696a3450> -> __attrs_140168026272976
            __attrs_140168026272976 = _static_140168026273232

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript">\n    jQuery(document).ready(function($) {\n        $("#attachments_update_table tbody").sortable();\n    });\n    </script>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b696a3990> name=None at 7f7b696a37d0> -> __attrs_140168026274320
            __attrs_140168026274320 = _static_140168026274192

            # <style ... (0:0)
            # --------------------------------------------------------
            __append(u'<style type="text/css">\n    #attachments_update {\n        margin-bottom: 2em;\n    }\n    .formHelp {\n        margin-bottom: 1em;\n    }\n    #attachments_update_table tr {\n        cursor: ns-resize;\n    }\n    .attachment-delete {\n        text-align: center;\n    }\n    </style>\n\n    <!-- Attachments Viewlet -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b696ba190> name=None at 7f7b696baf10> -> __attrs_140168026369424
            __attrs_140168026369424 = _static_140168026366352
            __backup_can_add_140168046866320 = get('can_add', __marker)

            # <Value u'attachments_view/can_add_attachments' (40:29)> -> __value
            __token = 1072
            try:
                __zt_tmp = __attrs_140168026369424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/can_add_attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['can_add'] = __value
            __backup_can_edit_140168047768528 = get('can_edit', __marker)

            # <Value u'attachments_view/can_edit_attachments' (41:29)> -> __value
            __token = 1139
            try:
                __zt_tmp = __attrs_140168026369424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/can_edit_attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['can_edit'] = __value
            __backup_can_delete_140168046892880 = get('can_delete', __marker)

            # <Value u'attachments_view/can_delete_attachments' (42:30)> -> __value
            __token = 1209
            try:
                __zt_tmp = __attrs_140168026369424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/can_delete_attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['can_delete'] = __value
            __backup_attachments_140168026272912 = get('attachments', __marker)

            # <Value u'attachments_view/get_sorted_attachments' (43:30)> -> __value
            __token = 1282
            try:
                __zt_tmp = __attrs_140168026369424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/get_sorted_attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['attachments'] = __value
            __backup_attachment_types_140168026368528 = get('attachment_types', __marker)

            # <Value u'attachments_view/get_attachment_types' (44:34)> -> __value
            __token = 1360
            try:
                __zt_tmp = __attrs_140168026369424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'attachments_view/get_attachment_types', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['attachment_types'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="panel-body">\n      <!-- Attachments List -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b68dbe4d0> name=None at 7f7b68dbea50> -> __attrs_140168016948944
            __attrs_140168016948944 = _static_140168016946384

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="attachments_update" class="ar_attachments_list">\n\n        <!-- Update Attachment Form -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b68dbe510> name=None at 7f7b68dbe590> -> __attrs_140168047149200
            __attrs_140168047149200 = _static_140168016946448

            # <Value u'attachments' (53:29)> -> __condition
            __token = 1802
            try:
                __zt_tmp = __attrs_140168047149200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <form ... (0:0)
                # --------------------------------------------------------
                __append(u'<form')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016947984
                __default_140168016947984 = _DEFAULT_MARKER

                # <Substitution u'string:${context/absolute_url}/@@attachments_view/update' (52:37)> -> __attr_action
                __token = 1715
                try:
                    __zt_tmp = __attrs_140168047149200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140168208991440('string', u'${context/absolute_url}/@@attachments_view/update', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', u'attachments_view/update', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((u' action="%s"' % __attr_action))
                __append(u' name="attachments_update_form" enctype="multipart/form-data" method="POST">\n\n          <!-- POST marker and Authenticator -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6a177450> name=None at 7f7b6a177b10> -> __attrs_140168047122576
                __attrs_140168047122576 = _static_140168037626960

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" name="submitted" value="1"/>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047122704
                __attrs_140168047122704 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047123280
                __default_140168047123280 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (58:39)> -> __cache_140168047124304
                __token = 1993
                try:
                    __zt_tmp = __attrs_140168047122704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047124304 = _static_140168208991440('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (58:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa85cd0> -> __condition
                __expression = __cache_140168047124304

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168047124304
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa85090> name=None at 7f7b6aa85f90> -> __attrs_140168047121232
                __attrs_140168047121232 = _static_140168047120528

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table id="attachments_update_table">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026329616
                __attrs_140168026329616 = _static_140168257770128

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append(u'<thead>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026331664
                __attrs_140168026331664 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b696b1350> name=None at 7f7b696b1f10> -> __attrs_140168026325776
                __attrs_140168026325776 = _static_140168026329936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168026329232 = []
                __append_140168026329232 = __stream_140168026329232.append
                __append_140168026329232(u'Name')
                __msgid_140168026329232 = __re_whitespace(''.join(__stream_140168026329232)).strip()
                if __msgid_140168026329232:
                    __append(translate(__msgid_140168026329232, mapping=None, default=__msgid_140168026329232, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b696b0390> name=None at 7f7b696b0a10> -> __attrs_140168026325712
                __attrs_140168026325712 = _static_140168026325904

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168026326352 = []
                __append_140168026326352 = __stream_140168026326352.append
                __append_140168026326352(u'Type')
                __msgid_140168026326352 = __re_whitespace(''.join(__stream_140168026326352)).strip()
                if __msgid_140168026326352:
                    __append(translate(__msgid_140168026326352, mapping=None, default=__msgid_140168026326352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b696b0990> name=None at 7f7b696b0450> -> __attrs_140168037651792
                __attrs_140168037651792 = _static_140168026327440

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168026327824 = []
                __append_140168026327824 = __stream_140168026327824.append
                __append_140168026327824(u'Size')
                __msgid_140168026327824 = __re_whitespace(''.join(__stream_140168026327824)).strip()
                if __msgid_140168026327824:
                    __append(translate(__msgid_140168026327824, mapping=None, default=__msgid_140168026327824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6a17d190> name=None at 7f7b6a17d950> -> __attrs_140168047388688
                __attrs_140168047388688 = _static_140168037650832

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168037651472 = []
                __append_140168037651472 = __stream_140168037651472.append
                __append_140168037651472(u'Analysis')
                __msgid_140168037651472 = __re_whitespace(''.join(__stream_140168037651472)).strip()
                if __msgid_140168037651472:
                    __append(translate(__msgid_140168037651472, mapping=None, default=__msgid_140168037651472, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aafec90> name=None at 7f7b6aafed50> -> __attrs_140168047618576
                __attrs_140168047618576 = _static_140168047619216

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168047617872 = []
                __append_140168047617872 = __stream_140168047617872.append
                __append_140168047617872(u'Keywords')
                __msgid_140168047617872 = __re_whitespace(''.join(__stream_140168047617872)).strip()
                if __msgid_140168047617872:
                    __append(translate(__msgid_140168047617872, mapping=None, default=__msgid_140168047617872, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aafeb10> name=None at 7f7b6aafeb50> -> __attrs_140168047618704
                __attrs_140168047618704 = _static_140168047618832

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168047616592 = []
                __append_140168047616592 = __stream_140168047616592.append
                __append_140168047616592(u'Render in Report')
                __msgid_140168047616592 = __re_whitespace(''.join(__stream_140168047616592)).strip()
                if __msgid_140168047616592:
                    __append(translate(__msgid_140168047616592, mapping=None, default=__msgid_140168047616592, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                <!-- Please do not move this column to be the first, because the\n                      :records converter will somehow offset the True/False value of\n                      the checkbox by -1 (the record before will be deleted) -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6a17bb50> name=None at 7f7b6a17bf10> -> __attrs_140168037643920
                __attrs_140168037643920 = _static_140168037645136

                # <Value u'can_delete' (72:66)> -> __condition
                __token = 2821
                try:
                    __zt_tmp = __attrs_140168037643920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'can_delete', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th class="pr-3">')
                    __stream_140168047618960 = []
                    __append_140168047618960 = __stream_140168047618960.append
                    __append_140168047618960(u'Remove')
                    __msgid_140168047618960 = __re_whitespace(''.join(__stream_140168047618960)).strip()
                    if __msgid_140168047618960:
                        __append(translate(__msgid_140168047618960, mapping=None, default=__msgid_140168047618960, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</th>')
                __append(u'\n              </tr>\n            </thead>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037644944
                __attrs_140168037644944 = _static_140168257770128

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append(u'<tbody>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026352272
                __attrs_140168026352272 = _static_140168257770128
                __backup_attachment_140168026332752 = get('attachment', __marker)

                # <Value u'attachments' (76:41)> -> __iterator
                __token = 2947
                try:
                    __zt_tmp = __attrs_140168026352272
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'attachments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168026339280, ) = getitem('repeat')(u'attachment', __iterator)
                econtext['attachment'] = None
                for __item in __iterator:
                    econtext['attachment'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b696b30d0> name=None at 7f7b696b3d90> -> __attrs_140168026337552
                    __attrs_140168026337552 = _static_140168026337488

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-link">\n                  <!-- Icon and Attachment download link -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b696b3d10> name=None at 7f7b696b3d50> -> __attrs_140168047031888
                    __attrs_140168047031888 = _static_140168026340624

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-paperclip" aria-hidden="true"/>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa6f110> name=None at 7f7b6aa6f0d0> -> __attrs_140168047813968
                    __attrs_140168047813968 = _static_140168047030544

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a title="Click to download"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047815952
                    __default_140168047815952 = _DEFAULT_MARKER

                    # <Substitution u'string:${attachment/absolute_url}/at_download/AttachmentFile' (82:43)> -> __attr_href
                    __token = 3224
                    try:
                        __zt_tmp = __attrs_140168047813968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('string', u'${attachment/absolute_url}/at_download/AttachmentFile', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047032464
                    __default_140168047032464 = _DEFAULT_MARKER

                    # <Value u'attachment/name' (83:35)> -> __cache_140168047030608
                    __token = 3321
                    try:
                        __zt_tmp = __attrs_140168047813968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047030608 = _static_140168208991440('path', u'attachment/name', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'attachment/name' (83:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa6f910> -> __condition
                    __expression = __cache_140168047030608

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'name')
                    else:
                        __content = __cache_140168047030608
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n\n                  <!-- Attachment UID -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ab2e990> name=None at 7f7b6ab2ef90> -> __attrs_140168047813392
                    __attrs_140168047813392 = _static_140168047815056

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047814608
                    __default_140168047814608 = _DEFAULT_MARKER

                    # <Substitution u'string:attachments.UID:records' (86:60)> -> __attr_name
                    __token = 3450
                    try:
                        __zt_tmp = __attrs_140168047813392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'attachments.UID:records', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047814096
                    __default_140168047814096 = _DEFAULT_MARKER

                    # <Substitution u'string:${attachment/UID}' (87:60)> -> __attr_value
                    __token = 3542
                    try:
                        __zt_tmp = __attrs_140168047813392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('string', u'${attachment/UID}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>\n\n                  <!-- Order -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a14a890> name=None at 7f7b6a14a210> -> __attrs_140168037441936
                    __attrs_140168037441936 = _static_140168037443728

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037445008
                    __default_140168037445008 = _DEFAULT_MARKER

                    # <Substitution u'string:order:list' (90:60)> -> __attr_name
                    __token = 3665
                    try:
                        __zt_tmp = __attrs_140168037441936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'order:list', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037442896
                    __default_140168037442896 = _DEFAULT_MARKER

                    # <Substitution u'string:${attachment/UID}' (91:60)> -> __attr_value
                    __token = 3744
                    try:
                        __zt_tmp = __attrs_140168037441936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('string', u'${attachment/UID}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>\n                </td>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a14aa50> name=None at 7f7b6a14ad10> -> __attrs_140168037527504
                    __attrs_140168037527504 = _static_140168037444176

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-type">\n                  <!-- Attachment Type -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a15e610> name=None at 7f7b6a15e550> -> __attrs_140168037524624
                    __attrs_140168037524624 = _static_140168037525008

                    # <Value u'can_edit' (98:41)> -> __condition
                    __token = 4020
                    try:
                        __zt_tmp = __attrs_140168037524624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<select')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037525328
                        __default_140168037525328 = _DEFAULT_MARKER

                        # <Substitution u'string:attachments.AttachmentType:records' (99:47)> -> __attr_name
                        __token = 4077
                        try:
                            __zt_tmp = __attrs_140168037524624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('string', u'attachments.AttachmentType:records', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', u'AttachmentType', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))
                        __append(u' class="form-control"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037524048
                        __default_140168037524048 = _DEFAULT_MARKER

                        # <Substitution u'string:${attachment/UID}' (100:61)> -> __attr_data_attachment_uid
                        __token = 4181
                        try:
                            __zt_tmp = __attrs_140168037524624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_data_attachment_uid = _static_140168208991440('string', u'${attachment/UID}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_data_attachment_uid = __quote(__attr_data_attachment_uid, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_data_attachment_uid is not None):
                            __append((u' data-attachment-uid="%s"' % __attr_data_attachment_uid))
                        __append(u'>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a16eb10> name=None at 7f7b6a16ee10> -> __attrs_140168037498768
                        __attrs_140168037498768 = _static_140168037591824
                        __backup_item_140168037590544 = get('item', __marker)

                        # <Value u'attachment_types' (101:47)> -> __iterator
                        __token = 4257
                        try:
                            __zt_tmp = __attrs_140168037498768
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140168208991440('path', u'attachment_types', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        (__iterator, ____index_140168037495312, ) = getitem('repeat')(u'item', __iterator)
                        econtext['item'] = None
                        for __item in __iterator:
                            econtext['item'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<option')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037589200
                            __default_140168037589200 = _DEFAULT_MARKER

                            # <Substitution u'item/UID' (102:52)> -> __attr_value
                            __token = 4327
                            try:
                                __zt_tmp = __attrs_140168037498768
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037592784
                            __default_140168037592784 = _DEFAULT_MARKER

                            # <Boolean u"python:item.UID==attachment['type_uid']" (103:54)> -> __attr_selected
                            __token = 4391
                            try:
                                __zt_tmp = __attrs_140168037498768
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_selected = _static_140168208991440('python', u"item.UID==attachment['type_uid']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            if (__attr_selected is _DEFAULT_MARKER):
                                __attr_selected = None
                            else:
                                if __attr_selected:
                                    __attr_selected = u'selected'
                                else:
                                    __attr_selected = None
                            if (__attr_selected is not None):
                                __append((u' selected="%s"' % __attr_selected))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037592400
                            __default_140168037592400 = _DEFAULT_MARKER

                            # <Value u'item/Title' (104:43)> -> __cache_140168037592464
                            __token = 4476
                            try:
                                __zt_tmp = __attrs_140168037498768
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140168037592464 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                            # <BinOp left=<Value u'item/Title' (104:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a16e050> -> __condition
                            __expression = __cache_140168037592464

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140168037592464
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</option>')
                            ____index_140168037495312 -= 1
                            if (____index_140168037495312 > 0):
                                __append('\n                      ')
                        if (__backup_item_140168037590544 is __marker):
                            del econtext['item']
                        else:
                            econtext['item'] = __backup_item_140168037590544
                        __append(u'\n                  </select>')
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037498576
                    __attrs_140168037498576 = _static_140168257770128

                    # <Value u'not:can_edit' (106:39)> -> __condition
                    __token = 4557
                    try:
                        __zt_tmp = __attrs_140168037498576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037496400
                        __default_140168037496400 = _DEFAULT_MARKER

                        # <Value u'attachment/type' (107:37)> -> __cache_140168037495440
                        __token = 4608
                        try:
                            __zt_tmp = __attrs_140168037498576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168037495440 = _static_140168208991440('path', u'attachment/type', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'attachment/type' (107:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a157910> -> __condition
                        __expression = __cache_140168037495440

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168037495440
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n                </td>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a1574d0> name=None at 7f7b6a16e6d0> -> __attrs_140168047023248
                    __attrs_140168047023248 = _static_140168037496016

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-field-size">\n                  <!-- File Size -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa6d390> name=None at 7f7b6aa6d250> -> __attrs_140168047023312
                    __attrs_140168047023312 = _static_140168047022992

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="filesize">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047024208
                    __default_140168047024208 = _DEFAULT_MARKER

                    # <Value u'attachment/size' (112:54)> -> __cache_140168047022416
                    __token = 4792
                    try:
                        __zt_tmp = __attrs_140168047023312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047022416 = _static_140168208991440('path', u'attachment/size', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'attachment/size' (112:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa6da90> -> __condition
                    __expression = __cache_140168047022416

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168047022416
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                </td>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa6db10> name=None at 7f7b6aa6d2d0> -> __attrs_140168046999312
                    __attrs_140168046999312 = _static_140168047024912

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-analysis">\n                  <!-- Attached to Analysis -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa67110> name=None at 7f7b6aa67950> -> __attrs_140168047000016
                    __attrs_140168047000016 = _static_140168046997776

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="analysis">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046997584
                    __default_140168046997584 = _DEFAULT_MARKER

                    # <Value u'attachment/analysis' (117:54)> -> __cache_140168046997968
                    __token = 4985
                    try:
                        __zt_tmp = __attrs_140168047000016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168046997968 = _static_140168208991440('path', u'attachment/analysis', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'attachment/analysis' (117:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa67910> -> __condition
                    __expression = __cache_140168046997968

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168046997968
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                </td>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa674d0> name=None at 7f7b6aa67290> -> __attrs_140168046858576
                    __attrs_140168046858576 = _static_140168046998736

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-keywords">\n                  <!-- Attachment Keywords -->\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa455d0> name=None at 7f7b6aa45cd0> -> __attrs_140168046861584
                    __attrs_140168046861584 = _static_140168046859728

                    # <Value u'can_edit' (124:40)> -> __condition
                    __token = 5260
                    try:
                        __zt_tmp = __attrs_140168046861584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046861072
                        __default_140168046861072 = _DEFAULT_MARKER

                        # <Substitution u'string:attachments.AttachmentKeys:records' (125:46)> -> __attr_name
                        __token = 5316
                        try:
                            __zt_tmp = __attrs_140168046861584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('string', u'attachments.AttachmentKeys:records', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', u'AttachmentKeys', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))
                        __append(u' class="form-control"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046860560
                        __default_140168046860560 = _DEFAULT_MARKER

                        # <Substitution u'attachment/keywords' (126:46)> -> __attr_value
                        __token = 5405
                        try:
                            __zt_tmp = __attrs_140168046861584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'attachment/keywords', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'/>')
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047007184
                    __attrs_140168047007184 = _static_140168257770128

                    # <Value u'not:can_edit' (127:39)> -> __condition
                    __token = 5469
                    try:
                        __zt_tmp = __attrs_140168047007184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046861712
                        __default_140168046861712 = _DEFAULT_MARKER

                        # <Value u'attachment/keywords' (128:37)> -> __cache_140168046861264
                        __token = 5520
                        try:
                            __zt_tmp = __attrs_140168047007184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168046861264 = _static_140168208991440('path', u'attachment/keywords', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'attachment/keywords' (128:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa45a10> -> __condition
                        __expression = __cache_140168046861264

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168046861264
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n                </td>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa45110> name=None at 7f7b6aa45890> -> __attrs_140168047007632
                    __attrs_140168047007632 = _static_140168046858512
                    __backup_render_in_report_140168026330384 = get('render_in_report', __marker)

                    # <Value u"python:attachment.get('render_in_report', False)" (132:49)> -> __value
                    __token = 5683
                    try:
                        __zt_tmp = __attrs_140168047007632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u"attachment.get('render_in_report', False)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['render_in_report'] = __value

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="attachment-render-in-report text-center">\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa69e90> name=None at 7f7b6aa69810> -> __attrs_140168047009232
                    __attrs_140168047009232 = _static_140168047009424

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="checkbox"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047006480
                    __default_140168047006480 = _DEFAULT_MARKER

                    # <Substitution u'string:attachments.RenderInReport:records:boolean' (134:46)> -> __attr_name
                    __token = 5821
                    try:
                        __zt_tmp = __attrs_140168047009232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'attachments.RenderInReport:records:boolean', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047009104
                    __default_140168047009104 = _DEFAULT_MARKER

                    # <Boolean u'python:render_in_report' (135:48)> -> __attr_checked
                    __token = 5920
                    try:
                        __zt_tmp = __attrs_140168047009232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140168208991440('python', u'render_in_report', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = u'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((u' checked="%s"' % __attr_checked))
                    __append(u'/>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a080390> name=None at 7f7b6a080510> -> __attrs_140168036617488
                    __attrs_140168036617488 = _static_140168036615056

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036615120
                    __default_140168036615120 = _DEFAULT_MARKER

                    # <Substitution u'string:attachments.RenderInReport:records:boolean:default' (137:46)> -> __attr_name
                    __token = 6034
                    try:
                        __zt_tmp = __attrs_140168036617488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'attachments.RenderInReport:records:boolean:default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036618192
                    __default_140168036618192 = _DEFAULT_MARKER

                    # <Substitution u'python:False' (138:46)> -> __attr_value
                    __token = 6139
                    try:
                        __zt_tmp = __attrs_140168036617488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('python', u'False', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036616912
                    __attrs_140168036616912 = _static_140168257770128

                    # <Value u'not:can_edit' (140:39)> -> __condition
                    __token = 6238
                    try:
                        __zt_tmp = __attrs_140168036616912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('not', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036616784
                        __default_140168036616784 = _DEFAULT_MARKER

                        # <Value u"python:'Yes' if attachment.get('can_edit') else 'No'" (141:37)> -> __cache_140168036617232
                        __token = 6289
                        try:
                            __zt_tmp = __attrs_140168036616912
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168036617232 = _static_140168208991440('python', u"'Yes' if attachment.get('can_edit') else 'No'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:'Yes' if attachment.get('can_edit') else 'No'" (141:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a080850> -> __condition
                        __expression = __cache_140168036617232

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168036617232
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n                </td>')
                    if (__backup_render_in_report_140168026330384 is __marker):
                        del econtext['render_in_report']
                    else:
                        econtext['render_in_report'] = __backup_render_in_report_140168026330384
                    __append(u'\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a080090> name=None at 7f7b6a0807d0> -> __attrs_140168036617680
                    __attrs_140168036617680 = _static_140168036614288

                    # <Value u'can_delete' (144:61)> -> __condition
                    __token = 6429
                    try:
                        __zt_tmp = __attrs_140168036617680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'can_delete', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="attachment-delete">\n                  <!-- Delete Attachment\n                  Note that for deletion we rely on "can_edit" from attachment\n                  -->\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b68d92310> name=None at 7f7b68d926d0> -> __attrs_140168016767952
                        __attrs_140168016767952 = _static_140168016765712

                        # <Value u'attachment/can_edit' (149:41)> -> __condition
                        __token = 6666
                        try:
                            __zt_tmp = __attrs_140168016767952
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('path', u'attachment/can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="checkbox"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016765520
                            __default_140168016765520 = _DEFAULT_MARKER

                            # <Substitution u'string:attachments.delete:records:boolean' (150:47)> -> __attr_name
                            __token = 6734
                            try:
                                __zt_tmp = __attrs_140168016767952
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_name = _static_140168208991440('string', u'attachments.delete:records:boolean', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_name is not None):
                                __append((u' name="%s"' % __attr_name))

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016765392
                            __default_140168016765392 = _DEFAULT_MARKER

                            # <Substitution u'python:True' (151:47)> -> __attr_value
                            __token = 6824
                            try:
                                __zt_tmp = __attrs_140168016767952
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140168208991440('python', u'True', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u'/>')
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f7b68d92090> name=None at 7f7b68d92050> -> __attrs_140168047170576
                        __attrs_140168047170576 = _static_140168016765072

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016767632
                        __default_140168016767632 = _DEFAULT_MARKER

                        # <Substitution u'string:attachments.delete:records:boolean:default' (153:45)> -> __attr_name
                        __token = 6925
                        try:
                            __zt_tmp = __attrs_140168047170576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('string', u'attachments.delete:records:boolean:default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016768528
                        __default_140168016768528 = _DEFAULT_MARKER

                        # <Substitution u'python:False' (154:45)> -> __attr_value
                        __token = 7021
                        try:
                            __zt_tmp = __attrs_140168047170576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'False', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'/>\n                </td>')
                    __append(u'\n              </tr>')
                    ____index_140168026339280 -= 1
                    if (____index_140168026339280 > 0):
                        __append('\n              ')
                if (__backup_attachment_140168026332752 is __marker):
                    del econtext['attachment']
                else:
                    econtext['attachment'] = __backup_attachment_140168026332752
                __append(u'\n            </tbody>\n          </table>\n\n          <!-- short usage description -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa69ed0> name=None at 7f7b6aa69890> -> __attrs_140168047169808
                __attrs_140168047169808 = _static_140168047009488

                # <Value u'can_edit' (161:56)> -> __condition
                __token = 7221
                try:
                    __zt_tmp = __attrs_140168047169808
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="formHelp discreet">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047171344
                    __attrs_140168047171344 = _static_140168257770128

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')
                    __stream_140168047172240 = []
                    __append_140168047172240 = __stream_140168047172240.append
                    __append_140168047172240(u'\n              Please click the update button after your changes.\n            ')
                    __msgid_140168047172240 = __re_whitespace(''.join(__stream_140168047172240)).strip()
                    if __msgid_140168047172240:
                        __append(translate(__msgid_140168047172240, mapping=None, default=__msgid_140168047172240, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047171664
                    __attrs_140168047171664 = _static_140168257770128

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')
                    __stream_140168047170448 = []
                    __append_140168047170448 = __stream_140168047170448.append
                    __append_140168047170448(u'\n              Note: You can also drag and drop the attachment rows to change the order they appear in the report.\n            ')
                    __msgid_140168047170448 = __re_whitespace(''.join(__stream_140168047170448)).strip()
                    if __msgid_140168047170448:
                        __append(translate(__msgid_140168047170448, mapping=None, default=__msgid_140168047170448, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n          </div>')
                __append(u'\n\n          <!-- Update attachments button.\n               This will send the values to the `attachments_view` endpoint. -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa91790> name=None at 7f7b6aa91b50> -> __attrs_140168047809616
                __attrs_140168047809616 = _static_140168047171472

                # <Value u'can_edit' (177:32)> -> __condition
                __token = 7890
                try:
                    __zt_tmp = __attrs_140168047809616
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'can_edit', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="btn btn-secondary context" id="updateButton" type="submit" name="updateARAttachment"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047812176
                    __default_140168047812176 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f7b6ab2de10> at 7f7b6ab2d310> -> __attr_value
                    __attr_value = u'Update Attachments'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>')
                __append(u'\n\n        </form>')
            __append(u'\n        <!-- /Update Form -->\n      </div>\n\n      <!-- Add Attachments -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6ab2dd50> name=None at 7f7b6ab2d3d0> -> __attrs_140168047810448
            __attrs_140168047810448 = _static_140168047811920

            # <Value u'can_add' (186:26)> -> __condition
            __token = 8093
            try:
                __zt_tmp = __attrs_140168047810448
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('path', u'can_add', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="attachments_add" class="ar_attachments_list">\n\n        <!-- Add Form -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab34910> name=None at 7f7b6ab34b50> -> __attrs_140168046846928
                __attrs_140168046846928 = _static_140168047839504

                # <form ... (0:0)
                # --------------------------------------------------------
                __append(u'<form')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047839248
                __default_140168047839248 = _DEFAULT_MARKER

                # <Substitution u'string:${context/absolute_url}/@@attachments_view/add' (193:37)> -> __attr_action
                __token = 8332
                try:
                    __zt_tmp = __attrs_140168046846928
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140168208991440('string', u'${context/absolute_url}/@@attachments_view/add', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', u'attachments_view', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((u' action="%s"' % __attr_action))
                __append(u' name="attachments_add_form" enctype="multipart/form-data" method="POST">\n\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa42350> name=None at 7f7b6aa42c90> -> __attrs_140168046847248
                __attrs_140168046847248 = _static_140168046846800

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" name="submitted" value="1"/>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046846352
                __attrs_140168046846352 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046849616
                __default_140168046849616 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (197:39)> -> __cache_140168046847888
                __token = 8516
                try:
                    __zt_tmp = __attrs_140168046846352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046847888 = _static_140168208991440('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (197:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa428d0> -> __condition
                __expression = __cache_140168046847888

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168046847888
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b696ac290> name=None at 7f7b696aca10> -> __attrs_140168026311440
                __attrs_140168026311440 = _static_140168026309264

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table id="attachments_add_table">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026310992
                __attrs_140168026310992 = _static_140168257770128

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append(u'<thead>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026312336
                __attrs_140168026312336 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b696ac3d0> name=None at 7f7b696aced0> -> __attrs_140168016934800
                __attrs_140168016934800 = _static_140168026309584

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168026310096 = []
                __append_140168026310096 = __stream_140168026310096.append
                __append_140168026310096(u'Add new Attachment')
                __msgid_140168026310096 = __re_whitespace(''.join(__stream_140168026310096)).strip()
                if __msgid_140168026310096:
                    __append(translate(__msgid_140168026310096, mapping=None, default=__msgid_140168026310096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b68dbb750> name=None at 7f7b68dbb590> -> __attrs_140168016933264
                __attrs_140168016933264 = _static_140168016934736

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168016936272 = []
                __append_140168016936272 = __stream_140168016936272.append
                __append_140168016936272(u'Type')
                __msgid_140168016936272 = __re_whitespace(''.join(__stream_140168016936272)).strip()
                if __msgid_140168016936272:
                    __append(translate(__msgid_140168016936272, mapping=None, default=__msgid_140168016936272, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b68dbb090> name=None at 7f7b68dbb410> -> __attrs_140168016935824
                __attrs_140168016935824 = _static_140168016933008

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168016934480 = []
                __append_140168016934480 = __stream_140168016934480.append
                __append_140168016934480(u'Analysis')
                __msgid_140168016934480 = __re_whitespace(''.join(__stream_140168016934480)).strip()
                if __msgid_140168016934480:
                    __append(translate(__msgid_140168016934480, mapping=None, default=__msgid_140168016934480, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b68dbb850> name=None at 7f7b68dbb310> -> __attrs_140168016906320
                __attrs_140168016906320 = _static_140168016934992

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168016934928 = []
                __append_140168016934928 = __stream_140168016934928.append
                __append_140168016934928(u'Keywords')
                __msgid_140168016934928 = __re_whitespace(''.join(__stream_140168016934928)).strip()
                if __msgid_140168016934928:
                    __append(translate(__msgid_140168016934928, mapping=None, default=__msgid_140168016934928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b68db4b10> name=None at 7f7b68db4590> -> __attrs_140168016906640
                __attrs_140168016906640 = _static_140168016907024

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="pr-3">')
                __stream_140168016904784 = []
                __append_140168016904784 = __stream_140168016904784.append
                __append_140168016904784(u'Render in Report')
                __msgid_140168016904784 = __re_whitespace(''.join(__stream_140168016904784)).strip()
                if __msgid_140168016904784:
                    __append(translate(__msgid_140168016904784, mapping=None, default=__msgid_140168016904784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n              </tr>\n            </thead>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037618384
                __attrs_140168037618384 = _static_140168257770128

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append(u'<tbody>\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016905744
                __attrs_140168016905744 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016904592
                __attrs_140168016904592 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                  <!-- Attachment File Upload -->\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b68db49d0> name=None at 7f7b68db4f50> -> __attrs_140168036701968
                __attrs_140168036701968 = _static_140168016906704

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="file" id="AttachmentFile_file" name="AttachmentFile_file" onchange="string:document.getElementById(\'addARButton\').disabled=false"/>\n                </td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036704208
                __attrs_140168036704208 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                  <!-- Attachment type selection dropdown -->\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6a095150> name=None at 7f7b6a095f90> -> __attrs_140168036701776
                __attrs_140168036701776 = _static_140168036700496

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select name="AttachmentType" class="form-control">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaba110> name=None at 7f7b6aabaf10> -> __attrs_140168047341392
                __attrs_140168047341392 = _static_140168047337744
                __backup_item_140168083081552 = get('item', __marker)

                # <Value u'attachment_types' (221:45)> -> __iterator
                __token = 9590
                try:
                    __zt_tmp = __attrs_140168047341392
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'attachment_types', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168047341072, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047341264
                    __default_140168047341264 = _DEFAULT_MARKER

                    # <Substitution u'item/UID' (222:50)> -> __attr_value
                    __token = 9658
                    try:
                        __zt_tmp = __attrs_140168047341392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036703440
                    __default_140168036703440 = _DEFAULT_MARKER

                    # <Value u'item/Title' (223:41)> -> __cache_140168036702928
                    __token = 9710
                    try:
                        __zt_tmp = __attrs_140168047341392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168036702928 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/Title' (223:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a095410> -> __condition
                    __expression = __cache_140168036702928

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168036702928
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option>')
                    ____index_140168047341072 -= 1
                    if (____index_140168047341072 > 0):
                        __append('\n                    ')
                if (__backup_item_140168083081552 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140168083081552
                __append(u'\n                  </select>\n                </td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036703376
                __attrs_140168036703376 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                  <!-- Analysis selection dropdown -->\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047339920
                __attrs_140168047339920 = _static_140168257770128
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047357008
                __attrs_140168047357008 = _static_140168257770128
                __backup_analyses_140168047388048 = get('analyses', __marker)

                # <Value u'attachments_view/get_analyses' (230:43)> -> __value
                __token = 9961
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'attachments_view/get_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['analyses'] = __value
                __backup_a_analyses_140168026339152 = get('a_analyses', __marker)

                # <Value u"python:[a for a in analyses if a.portal_type == 'Analysis']" (231:44)> -> __value
                __token = 10036
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"[a for a in analyses if a.portal_type == 'Analysis']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['a_analyses'] = __value
                __backup_bc_140168047815184 = get('bc', __marker)

                # <Value u"python:[a for a in analyses if a.portal_type == 'ReferenceAnalysis']" (232:35)> -> __value
                __token = 10133
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"[a for a in analyses if a.portal_type == 'ReferenceAnalysis']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['bc'] = __value
                __backup_b_analyses_140168047815312 = get('b_analyses', __marker)

                # <Value u'python:[a for a in bc if a.aq_parent.getBlank()]' (233:42)> -> __value
                __token = 10247
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'[a for a in bc if a.aq_parent.getBlank()]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['b_analyses'] = __value
                __backup_c_analyses_140168037590864 = get('c_analyses', __marker)

                # <Value u'python:[a for a in bc if not a.aq_parent.getBlank()]' (234:41)> -> __value
                __token = 10341
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'[a for a in bc if not a.aq_parent.getBlank()]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['c_analyses'] = __value
                __backup_d_analyses_140168026331536 = get('d_analyses', __marker)

                # <Value u"python:[a for a in analyses if a.portal_type == 'DuplicateAnalysis']" (235:40)> -> __value
                __token = 10439
                try:
                    __zt_tmp = __attrs_140168047357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"[a for a in analyses if a.portal_type == 'DuplicateAnalysis']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['d_analyses'] = __value
                __append(u'\n                      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aabefd0> name=None at 7f7b6aabed90> -> __attrs_140168046975056
                __attrs_140168046975056 = _static_140168047357904

                # <Value u'analyses' (236:82)> -> __condition
                __token = 10598
                try:
                    __zt_tmp = __attrs_140168046975056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select name="Analysis" class="form-control">\n                        <!-- Empty option attaches to the AR -->\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa61ed0> name=None at 7f7b6aa61ad0> -> __attrs_140168046975760
                    __attrs_140168046975760 = _static_140168046976720

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option selected="selected" disabled="disabled"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046974800
                    __default_140168046974800 = _DEFAULT_MARKER

                    # <Substitution u'python:None' (240:54)> -> __attr_value
                    __token = 10832
                    try:
                        __zt_tmp = __attrs_140168046975760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('python', u'None', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>\n                          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025888912
                    __attrs_140168025888912 = _static_140168257770128

                    # <Negate value=<Value u'python:True' (241:46)> at 7f7b696452d0> -> __cache_140168025887440

                    # <Value u'python:True' (241:46)> -> __cache_140168025887440
                    __token = 10892
                    try:
                        __zt_tmp = __attrs_140168025888912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168025887440 = _static_140168208991440('python', u'True', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __cache_140168025887440 = not __cache_140168025887440
                    __condition = __cache_140168025887440
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                    __stream_140168046973584 = []
                    __append_140168046973584 = __stream_140168046973584.append
                    __append_140168046973584(u'Attach to Sample')
                    __msgid_140168046973584 = __re_whitespace(''.join(__stream_140168046973584)).strip()
                    if __msgid_140168046973584:
                        __append(translate(__msgid_140168046973584, mapping=None, default=__msgid_140168046973584, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __condition = __cache_140168025887440
                    if __condition:
                        __append(u'</span>')
                    __append(u'\n                        </option>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025889552
                    __attrs_140168025889552 = _static_140168257770128
                    __backup_item_140168046973904 = get('item', __marker)

                    # <Value u'a_analyses' (244:48)> -> __iterator
                    __token = 11061
                    try:
                        __zt_tmp = __attrs_140168025889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'a_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168025889808, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append(u'\n                          ')

                        # <Static value=<_ast.Dict object at 0x7f7b69645bd0> name=None at 7f7b69645fd0> -> __attrs_140168025887824
                        __attrs_140168025887824 = _static_140168025889744

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025890512
                        __default_140168025890512 = _DEFAULT_MARKER

                        # <Substitution u'item/UID' (245:56)> -> __attr_value
                        __token = 11130
                        try:
                            __zt_tmp = __attrs_140168025887824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168025888656
                        __default_140168025888656 = _DEFAULT_MARKER

                        # <Value u'item/Title' (246:47)> -> __cache_140168025890384
                        __token = 11188
                        try:
                            __zt_tmp = __attrs_140168025887824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168025890384 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item/Title' (246:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b69645490> -> __condition
                        __expression = __cache_140168025890384

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168025890384
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                        ')
                        ____index_140168025889808 -= 1
                        if (____index_140168025889808 > 0):
                            __append('')
                    if (__backup_item_140168046973904 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168046973904
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025890064
                    __attrs_140168025890064 = _static_140168257770128
                    __backup_item_140168037495504 = get('item', __marker)

                    # <Value u'b_analyses' (248:48)> -> __iterator
                    __token = 11283
                    try:
                        __zt_tmp = __attrs_140168025890064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'b_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168025886864, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append(u'\n                          ')

                        # <Static value=<_ast.Dict object at 0x7f7b696459d0> name=None at 7f7b69645810> -> __attrs_140168047806032
                        __attrs_140168047806032 = _static_140168025889232

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047806608
                        __default_140168047806608 = _DEFAULT_MARKER

                        # <Substitution u'item/UID' (249:56)> -> __attr_value
                        __token = 11352
                        try:
                            __zt_tmp = __attrs_140168047806032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047804816
                        __attrs_140168047804816 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047807312
                        __default_140168047807312 = _DEFAULT_MARKER

                        # <Value u'item/Title' (250:47)> -> __cache_140168047805072
                        __token = 11411
                        try:
                            __zt_tmp = __attrs_140168047804816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047805072 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item/Title' (250:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab2c410> -> __condition
                        __expression = __cache_140168047805072

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047805072
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                            &nbsp;\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047806416
                        __attrs_140168047806416 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140168047807696 = []
                        __append_140168047807696 = __stream_140168047807696.append
                        __append_140168047807696(u'(Blank)')
                        __msgid_140168047807696 = __re_whitespace(''.join(__stream_140168047807696)).strip()
                        if __msgid_140168047807696:
                            __append(translate(__msgid_140168047807696, mapping=None, default=__msgid_140168047807696, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n                          </option>\n                        ')
                        ____index_140168025886864 -= 1
                        if (____index_140168025886864 > 0):
                            __append('')
                    if (__backup_item_140168037495504 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168037495504
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047807440
                    __attrs_140168047807440 = _static_140168257770128
                    __backup_item_140168046973840 = get('item', __marker)

                    # <Value u'c_analyses' (255:48)> -> __iterator
                    __token = 11644
                    try:
                        __zt_tmp = __attrs_140168047807440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'c_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047805840, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append(u'\n                          ')

                        # <Static value=<_ast.Dict object at 0x7f7b6ab2cfd0> name=None at 7f7b6ab2c1d0> -> __attrs_140168047841360
                        __attrs_140168047841360 = _static_140168047808464

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047845136
                        __default_140168047845136 = _DEFAULT_MARKER

                        # <Substitution u'item/UID' (256:56)> -> __attr_value
                        __token = 11713
                        try:
                            __zt_tmp = __attrs_140168047841360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047844048
                        __attrs_140168047844048 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047842832
                        __default_140168047842832 = _DEFAULT_MARKER

                        # <Value u'item/Title' (257:47)> -> __cache_140168047843280
                        __token = 11772
                        try:
                            __zt_tmp = __attrs_140168047844048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047843280 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item/Title' (257:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab35a10> -> __condition
                        __expression = __cache_140168047843280

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047843280
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                            &nbsp;\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047844240
                        __attrs_140168047844240 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140168047842512 = []
                        __append_140168047842512 = __stream_140168047842512.append
                        __append_140168047842512(u'(Control)')
                        __msgid_140168047842512 = __re_whitespace(''.join(__stream_140168047842512)).strip()
                        if __msgid_140168047842512:
                            __append(translate(__msgid_140168047842512, mapping=None, default=__msgid_140168047842512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n                          </option>\n                        ')
                        ____index_140168047805840 -= 1
                        if (____index_140168047805840 > 0):
                            __append('')
                    if (__backup_item_140168046973840 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168046973840
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047841680
                    __attrs_140168047841680 = _static_140168257770128
                    __backup_item_140168046974608 = get('item', __marker)

                    # <Value u'd_analyses' (262:48)> -> __iterator
                    __token = 12007
                    try:
                        __zt_tmp = __attrs_140168047841680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'd_analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047844944, ) = getitem('repeat')(u'item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append(u'\n                          ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aaaef90> name=None at 7f7b6ab35790> -> __attrs_140168047289808
                        __attrs_140168047289808 = _static_140168047292304

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047289040
                        __default_140168047289040 = _DEFAULT_MARKER

                        # <Substitution u'item/UID' (263:56)> -> __attr_value
                        __token = 12076
                        try:
                            __zt_tmp = __attrs_140168047289808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'item/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047289168
                        __attrs_140168047289168 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047291920
                        __default_140168047291920 = _DEFAULT_MARKER

                        # <Value u'item/Title' (264:47)> -> __cache_140168047291600
                        __token = 12135
                        try:
                            __zt_tmp = __attrs_140168047289168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047291600 = _static_140168208991440('path', u'item/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item/Title' (264:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aaae490> -> __condition
                        __expression = __cache_140168047291600

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047291600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                            &nbsp;\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047292240
                        __attrs_140168047292240 = _static_140168257770128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140168047290576 = []
                        __append_140168047290576 = __stream_140168047290576.append
                        __append_140168047290576(u'(Duplicate)')
                        __msgid_140168047290576 = __re_whitespace(''.join(__stream_140168047290576)).strip()
                        if __msgid_140168047290576:
                            __append(translate(__msgid_140168047290576, mapping=None, default=__msgid_140168047290576, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n                          </option>\n                        ')
                        ____index_140168047844944 -= 1
                        if (____index_140168047844944 > 0):
                            __append('')
                    if (__backup_item_140168046974608 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_140168046974608
                    __append(u'\n                      </select>')
                __append(u'\n                    ')
                if (__backup_d_analyses_140168026331536 is __marker):
                    del econtext['d_analyses']
                else:
                    econtext['d_analyses'] = __backup_d_analyses_140168026331536
                if (__backup_c_analyses_140168037590864 is __marker):
                    del econtext['c_analyses']
                else:
                    econtext['c_analyses'] = __backup_c_analyses_140168037590864
                if (__backup_b_analyses_140168047815312 is __marker):
                    del econtext['b_analyses']
                else:
                    econtext['b_analyses'] = __backup_b_analyses_140168047815312
                if (__backup_bc_140168047815184 is __marker):
                    del econtext['bc']
                else:
                    econtext['bc'] = __backup_bc_140168047815184
                if (__backup_a_analyses_140168026339152 is __marker):
                    del econtext['a_analyses']
                else:
                    econtext['a_analyses'] = __backup_a_analyses_140168026339152
                if (__backup_analyses_140168047388048 is __marker):
                    del econtext['analyses']
                else:
                    econtext['analyses'] = __backup_analyses_140168047388048
                __append(u'\n                  \n                </td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047338576
                __attrs_140168047338576 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                  <!-- Attachment Keywords -->\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab35410> name=None at 7f7b6ab2c550> -> __attrs_140168047290512
                __attrs_140168047290512 = _static_140168047842320

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="form-control" name="AttachmentKeys"/>\n                </td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaae210> name=None at 7f7b6aabef50> -> __attrs_140168047292176
                __attrs_140168047292176 = _static_140168047288848

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="text-center">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aacbe10> name=None at 7f7b6aacb490> -> __attrs_140168047408144
                __attrs_140168047408144 = _static_140168047410704

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="checkbox" name="RenderInReport:boolean"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047408400
                __default_140168047408400 = _DEFAULT_MARKER

                # <Substitution u'python:True' (280:47)> -> __attr_value
                __token = 12793
                try:
                    __zt_tmp = __attrs_140168047408144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u'True', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aacb950> name=None at 7f7b6aacb5d0> -> __attrs_140168047350608
                __attrs_140168047350608 = _static_140168047409488

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" name="RenderInReport:boolean:default"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047409552
                __default_140168047409552 = _DEFAULT_MARKER

                # <Substitution u'python:False' (283:47)> -> __attr_value
                __token = 12958
                try:
                    __zt_tmp = __attrs_140168047350608
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u'False', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n                </td>\n              </tr>\n            </tbody>\n          </table>\n\n          <!-- short help desrciption -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aabab90> name=None at 7f7b68db4c90> -> __attrs_140168047350224
                __attrs_140168047350224 = _static_140168047340432

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="formHelp discreet">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047350544
                __attrs_140168047350544 = _static_140168257770128

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p>')
                __stream_140168047352720 = []
                __append_140168047352720 = __stream_140168047352720.append
                __append_140168047352720(u'\n              You can use the browse button to select and upload a new attachment.\n            ')
                __msgid_140168047352720 = __re_whitespace(''.join(__stream_140168047352720)).strip()
                if __msgid_140168047352720:
                    __append(translate(__msgid_140168047352720, mapping=None, default=__msgid_140168047352720, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n          </div>\n\n          <!-- Add Button.\n                This will send the new attachment record to the `analysis_view` endpoint -->\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aabd890> name=None at 7f7b6aabd8d0> -> __attrs_140168047244176
                __attrs_140168047244176 = _static_140168047351952

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input disabled class="context btn btn-secondary" id="addARButton" type="submit" name="addARAttachment"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047246352
                __default_140168047246352 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f7b6aaa3b10> at 7f7b6aaa3850> -> __attr_value
                __attr_value = u'Add Attachment'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n\n        </form> <!-- /Add Attachment Form -->\n      </div>')
            __append(u'\n    </div>')
            if (__backup_attachment_types_140168026368528 is __marker):
                del econtext['attachment_types']
            else:
                econtext['attachment_types'] = __backup_attachment_types_140168026368528
            if (__backup_attachments_140168026272912 is __marker):
                del econtext['attachments']
            else:
                econtext['attachments'] = __backup_attachments_140168026272912
            if (__backup_can_delete_140168046892880 is __marker):
                del econtext['can_delete']
            else:
                econtext['can_delete'] = __backup_can_delete_140168046892880
            if (__backup_can_edit_140168047768528 is __marker):
                del econtext['can_edit']
            else:
                econtext['can_edit'] = __backup_can_edit_140168047768528
            if (__backup_can_add_140168046866320 is __marker):
                del econtext['can_add']
            else:
                econtext['can_add'] = __backup_can_add_140168046866320
            __append(u'\n  </div>')
            if (__backup_attachments_view_140168047413584 is __marker):
                del econtext['attachments_view']
            else:
                econtext['attachments_view'] = __backup_attachments_view_140168047413584
            __append(u' <!-- Collapsible content -->\n</div>')
            __i18n_domain = __previous_i18n_domain_140168037620368
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }