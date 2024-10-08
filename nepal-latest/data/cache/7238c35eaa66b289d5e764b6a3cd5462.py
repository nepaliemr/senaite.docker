# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.CMFPlone-5.2.14-py2.7.egg/Products/CMFPlone/browser/templates/error_message.pt'

__tokens = {390: (u'options/error_type|nothing', 11, 26), 441: (u' options/error_tb|nothin', 12, 23), 494: (u'd options/error_log_id|nothi', 13, 26), 567: (u"python:err_type == 'NotFound'", 15, 39), 651: (u'nocall:view/@@plone_redirector_view', 17, 51), 1690: (u'string:${context/portal_url}/contact-info', 35, 48), 2046: (u'redirection_view/find_first_parent', 43, 58), 2140: (u' redirection_view/search_for_simila', 44, 58), 2232: (u'w context/@@plo', 45, 54), 2302: (u'ry context/portal_regis', 46, 51), 2387: (u"ion python:registry['plone.types_use_view_action_in_listin", 47, 57), 2503: (u"ngth python:registry['plone.search_results_description_len", 48, 52), 2623: (u'tring nocall:plone_view/normalize', 49, 55), 2713: (u'python:first_parent is not None or similar_items', 50, 48), 3022: (u'first_parent/absolute_url | nothing', 56, 52), 3115: (u'first_parent/absolute_url', 57, 55), 3197: (u" python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId(", 58, 55), 3328: (u"l python:result_url + '/view' if result_type in use_view_action else result_u", 59, 46), 3457: (u'result_type', 60, 47), 3587: (u"python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", 62, 67), 3512: (u'${url}', 61, 41), 3514: (u'url', 61, 43), 3734: (u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 63, 57), 3810: (u'${first_parent/Title}', 63, 133), 3812: (u'first_parent/Title', 63, 135), 3887: (u'python:plone_view.cropText(first_parent.Description(), desc_length)', 64, 51), 4125: (u'similar_items', 68, 53), 4196: (u'similar/getURL', 69, 55), 4267: (u' similar/portal_typ', 70, 55), 4335: (u"l python:result_url + '/view' if result_type in use_view_action else result_u", 71, 46), 4534: (u'string: state-${similar/review_state}', 73, 67), 4459: (u'${url}', 72, 41), 4461: (u'url', 72, 43), 4631: (u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 74, 57), 4707: (u'${similar/pretty_title_or_id}', 74, 133), 4709: (u'similar/pretty_title_or_id', 74, 135), 4792: (u"python:plone_view.cropText(similar.Description or '', desc_length)", 75, 51), 5260: (u'view/is_manager', 89, 35), 5193: (u"python: err_type != 'NotFound'", 88, 41), 5548: (u'isManager', 97, 36), 5747: (u'err_tb', 102, 37), 5821: (u'not:isManager', 105, 40), 6222: (u'string:${context/portal_url}/contact-info', 111, 44), 261: (u'context/@@main_template/macros/master', 6, 23), 261: (u'context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140656773075600 = {}
_static_140656452234704 = {u'href': u'#', }
_static_140656555704208 = {u'class': u'documentFirstHeading', }
_static_140656452211920 = {u'class': u'discreet', }
_static_140656556408592 = {u'href': u'#', }
_static_140656555948176 = {u'href': u'${url}', u'class': u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_140656727177104 = __C2ZContextWrapper
_static_140656452247696 = {u'id': u'content-core', }
_static_140656453449744 = {u'class': u'documentFirstHeading', }
_static_140656556507920 = {u'class': u'discreet', }
_static_140656455697808 = {u'href': u'${url}', u'class': u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_140656452179920 = u'master'
_static_140656556546384 = {u'id': u'content-core', }
_static_140656452442192 = {u'class': u'description', }
_static_140656727176400 = __compile_zt_expr
_static_140656555949328 = {u'class': u'discreet', }
_static_140656452195856 = {u'id': u'page-not-found-list', }

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

            # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452078416
            __attrs_140656452078416 = _static_140656773075600
            __previous_i18n_domain_140656453510032 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140656568023392 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fed21de17d0> name=None at 7fed21de1690> -> __value
            __value = _static_140656452179920
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656451752784
                __attrs_140656451752784 = _static_140656773075600
                __backup_err_type_140656453622096 = get('err_type', __marker)

                # <Value u'options/error_type|nothing' (11:26)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_140656451752784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140656727176400('path', u'options/error_type|nothing', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                econtext['err_type'] = __value
                __backup_err_tb_140656452988112 = get('err_tb', __marker)

                # <Value u'options/error_tb|nothing' (12:23)> -> __value
                __token = 441
                try:
                    __zt_tmp = __attrs_140656451752784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140656727176400('path', u'options/error_tb|nothing', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                econtext['err_tb'] = __value
                __backup_err_log_id_140656453681104 = get('err_log_id', __marker)

                # <Value u'options/error_log_id|nothing' (13:26)> -> __value
                __token = 494
                try:
                    __zt_tmp = __attrs_140656451752784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140656727176400('path', u'options/error_log_id|nothing', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                econtext['err_log_id'] = __value
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452114192
                __attrs_140656452114192 = _static_140656773075600

                # <Value u"python:err_type == 'NotFound'" (15:39)> -> __condition
                __token = 567
                try:
                    __zt_tmp = __attrs_140656452114192
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140656727176400('python', u"err_type == 'NotFound'", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656453450576
                    __attrs_140656453450576 = _static_140656773075600
                    __backup_redirection_view_140656453623120 = get('redirection_view', __marker)

                    # <Value u'nocall:view/@@plone_redirector_view' (17:51)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_140656453450576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('nocall', u'view/@@plone_redirector_view', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['redirection_view'] = __value
                    __append(u'\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fed21f17810> name=None at 7fed21f17890> -> __attrs_140656453451280
                    __attrs_140656453451280 = _static_140656453449744

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h1 class="documentFirstHeading">')
                    __stream_140656453447760 = []
                    __append_140656453447760 = __stream_140656453447760.append
                    __append_140656453447760(u'\n                    This page does not seem to exist&hellip;\n                ')
                    __msgid_140656453447760 = __re_whitespace(''.join(__stream_140656453447760)).strip()
                    if u'heading_site_there_seems_to_be_an_error':
                        __append(translate(u'heading_site_there_seems_to_be_an_error', mapping=None, default=__msgid_140656453447760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h1>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fed21df2090> name=None at 7fed21df2450> -> __attrs_140656452248080
                    __attrs_140656452248080 = _static_140656452247696

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fed21e21850> name=None at 7fed21df2590> -> __attrs_140656452214160
                    __attrs_140656452214160 = _static_140656452442192

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="description">')
                    __stream_140656452251408 = []
                    __append_140656452251408 = __stream_140656452251408.append
                    __append_140656452251408(u'\n \t                    We apologize for the inconvenience, but the page you were trying to access is not at this address.\n                        You can use the links below to help you find what you are looking for.\n                     ')
                    __msgid_140656452251408 = __re_whitespace(''.join(__stream_140656452251408)).strip()
                    if u'description_site_error':
                        __append(translate(u'description_site_error', mapping=None, default=__msgid_140656452251408, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fed21de94d0> name=None at 7fed21de9650> -> __attrs_140656452212816
                    __attrs_140656452212816 = _static_140656452211920

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140656456184848_site_admin = ''
                    __stream_140656452212048 = []
                    __append_140656452212048 = __stream_140656452212048.append
                    __append_140656452212048(u'\n                        If you are certain you have the correct web address but are encountering an error, please\n                        contact the ')
                    __stream_140656456184848_site_admin = []
                    __append_140656456184848_site_admin = __stream_140656456184848_site_admin.append

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452232784
                    __attrs_140656452232784 = _static_140656773075600

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140656456184848_site_admin(u'<span>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fed21deedd0> name=None at 7fed21deefd0> -> __attrs_140656453145360
                    __attrs_140656453145360 = _static_140656452234704

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140656456184848_site_admin(u'<a')

                    # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656452232656
                    __default_140656452232656 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/portal_url}/contact-info' (35:48)> -> __attr_href
                    __token = 1690
                    try:
                        __zt_tmp = __attrs_140656453145360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140656727176400('string', u'${context/portal_url}/contact-info', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140656456184848_site_admin((u' href="%s"' % __attr_href))
                    __append_140656456184848_site_admin(u'>')
                    __stream_140656452233552 = []
                    __append_140656452233552 = __stream_140656452233552.append
                    __append_140656452233552(u'site administration')
                    __msgid_140656452233552 = __re_whitespace(''.join(__stream_140656452233552)).strip()
                    if u'label_site_admin':
                        __append_140656456184848_site_admin(translate(u'label_site_admin', mapping=None, default=__msgid_140656452233552, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140656456184848_site_admin(u'</a></span>')
                    __append_140656452212048(u'${site_admin}')
                    __stream_140656456184848_site_admin = ''.join(__stream_140656456184848_site_admin)
                    __append_140656452212048(u'.\n                    ')
                    __msgid_140656452212048 = __re_whitespace(''.join(__stream_140656452212048)).strip()
                    if u'description_site_error_mail_site_admin':
                        __append(translate(u'description_site_error_mail_site_admin', mapping={u'site_admin': __stream_140656456184848_site_admin, }, default=__msgid_140656452212048, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452213072
                    __attrs_140656452213072 = _static_140656773075600

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')
                    __stream_140656452233680 = []
                    __append_140656452233680 = __stream_140656452233680.append
                    __append_140656452233680(u'\n                    Thank you.\n                    ')
                    __msgid_140656452233680 = __re_whitespace(''.join(__stream_140656452233680)).strip()
                    if u'description_site_error_thank_you':
                        __append(translate(u'description_site_error_thank_you', mapping=None, default=__msgid_140656452233680, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>\n\n                    <!-- Offer search results for suggestions -->\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656453147280
                    __attrs_140656453147280 = _static_140656773075600
                    __backup_first_parent_140656454063120 = get('first_parent', __marker)

                    # <Value u'redirection_view/find_first_parent' (43:58)> -> __value
                    __token = 2046
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('path', u'redirection_view/find_first_parent', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['first_parent'] = __value
                    __backup_similar_items_140656454065872 = get('similar_items', __marker)

                    # <Value u'redirection_view/search_for_similar' (44:58)> -> __value
                    __token = 2140
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('path', u'redirection_view/search_for_similar', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['similar_items'] = __value
                    __backup_plone_view_140656454052368 = get('plone_view', __marker)

                    # <Value u'context/@@plone' (45:54)> -> __value
                    __token = 2232
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('path', u'context/@@plone', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['plone_view'] = __value
                    __backup_registry_140656454065744 = get('registry', __marker)

                    # <Value u'context/portal_registry' (46:51)> -> __value
                    __token = 2302
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('path', u'context/portal_registry', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['registry'] = __value
                    __backup_use_view_action_140656454063696 = get('use_view_action', __marker)

                    # <Value u"python:registry['plone.types_use_view_action_in_listings']" (47:57)> -> __value
                    __token = 2387
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('python', u"registry['plone.types_use_view_action_in_listings']", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['use_view_action'] = __value
                    __backup_desc_length_140656454053328 = get('desc_length', __marker)

                    # <Value u"python:registry['plone.search_results_description_length']" (48:52)> -> __value
                    __token = 2503
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('python', u"registry['plone.search_results_description_length']", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['desc_length'] = __value
                    __backup_normalizeString_140656454051344 = get('normalizeString', __marker)

                    # <Value u'nocall:plone_view/normalizeString' (49:55)> -> __value
                    __token = 2623
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140656727176400('nocall', u'plone_view/normalizeString', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value

                    # <Value u'python:first_parent is not None or similar_items' (50:48)> -> __condition
                    __token = 2713
                    try:
                        __zt_tmp = __attrs_140656453147280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140656727176400('python', u'first_parent is not None or similar_items', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656454032400
                        __attrs_140656454032400 = _static_140656773075600

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h2>')
                        __stream_140656454032976 = []
                        __append_140656454032976 = __stream_140656454032976.append
                        __append_140656454032976(u'You might have been looking for&hellip;')
                        __msgid_140656454032976 = __re_whitespace(''.join(__stream_140656454032976)).strip()
                        if u'heading_not_found_suggestions':
                            __append(translate(u'heading_not_found_suggestions', mapping=None, default=__msgid_140656454032976, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</h2>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452198160
                        __attrs_140656452198160 = _static_140656773075600

                        # <nav ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<nav>\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fed21de5610> name=None at 7fed21de5890> -> __attrs_140656452197968
                        __attrs_140656452197968 = _static_140656452195856

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul id="page-not-found-list">\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656452198288
                        __attrs_140656452198288 = _static_140656773075600

                        # <Value u'first_parent/absolute_url | nothing' (56:52)> -> __condition
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_140656452198288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140656727176400('path', u'first_parent/absolute_url | nothing', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656555701840
                            __attrs_140656555701840 = _static_140656773075600
                            __backup_result_url_140656454065552 = get('result_url', __marker)

                            # <Value u'first_parent/absolute_url' (57:55)> -> __value
                            __token = 3115
                            try:
                                __zt_tmp = __attrs_140656555701840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('path', u'first_parent/absolute_url', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140656454064848 = get('result_type', __marker)

                            # <Value u"python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()" (58:55)> -> __value
                            __token = 3197
                            try:
                                __zt_tmp = __attrs_140656555701840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('python', u"hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140656454063504 = get('url', __marker)

                            # <Value u"python:result_url + '/view' if result_type in use_view_action else result_url" (59:46)> -> __value
                            __token = 3328
                            try:
                                __zt_tmp = __attrs_140656555701840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('python', u"result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <Value u'result_type' (60:47)> -> __condition
                            __token = 3457
                            try:
                                __zt_tmp = __attrs_140656555701840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140656727176400('path', u'result_type', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<li>\n                                ')

                                # <Static value=<_ast.Dict object at 0x7fed2213c590> name=None at 7fed2809b410> -> __attrs_140656486443024
                                __attrs_140656486443024 = _static_140656455697808
                                __backup_item_wf_state_class_140656454077008 = get('item_wf_state_class', __marker)

                                # <Value u"python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')" (62:67)> -> __value
                                __token = 3587
                                try:
                                    __zt_tmp = __attrs_140656486443024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140656727176400('python', u"' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                                econtext['item_wf_state_class'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656455699792
                                __default_140656455699792 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution u'${url}' (61:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fed2213cf90> -> __attr_href
                                __token = 3512
                                __token = 3514
                                try:
                                    __zt_tmp = __attrs_140656486443024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140656727176400('path', u'url', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_href = __attr_href
                                if (__attr_href is None):
                                    pass
                                else:
                                    if (__attr_href is _DEFAULT_MARKER):
                                        __attr_href = None
                                    else:
                                        __tt = type(__attr_href)
                                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                                            __attr_href = unicode(__attr_href)
                                        else:
                                            if (__tt is str):
                                                __attr_href = decode(__attr_href)
                                            else:
                                                if (__tt is not unicode):
                                                    try:
                                                        __attr_href = __attr_href.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_href)
                                                        __attr_href = (unicode(__attr_href) if (__attr_href is __converted) else __converted)
                                                    else:
                                                        __attr_href = __attr_href()
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656584658896
                                __default_140656584658896 = _DEFAULT_MARKER

                                # <Substitution u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (63:57)> -> __attr_class
                                __token = 3734
                                try:
                                    __zt_tmp = __attrs_140656486443024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140656727176400('python', u"'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>')

                                # <Interpolation value=<Substitution u'${first_parent/Title}' (63:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fed28160e90> -> __content_140656833983712
                                __token = 3810
                                __token = 3812
                                try:
                                    __zt_tmp = __attrs_140656486443024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140656833983712 = _static_140656727176400('path', u'first_parent/Title', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                                __content_140656833983712 = __quote(__content_140656833983712, '\x00', '&#0;', None, None)
                                __content_140656833983712 = __content_140656833983712
                                if (__content_140656833983712 is None):
                                    pass
                                else:
                                    if (__content_140656833983712 is None):
                                        __content_140656833983712 = None
                                    else:
                                        __tt = type(__content_140656833983712)
                                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                                            __content_140656833983712 = unicode(__content_140656833983712)
                                        else:
                                            if (__tt is str):
                                                __content_140656833983712 = decode(__content_140656833983712)
                                            else:
                                                if (__tt is not unicode):
                                                    try:
                                                        __content_140656833983712 = __content_140656833983712.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140656833983712)
                                                        __content_140656833983712 = (unicode(__content_140656833983712) if (__content_140656833983712 is __converted) else __converted)
                                                    else:
                                                        __content_140656833983712 = __content_140656833983712()
                                if (__content_140656833983712 is not None):
                                    __append(__content_140656833983712)
                                __append(u'</a>')
                                if (__backup_item_wf_state_class_140656454077008 is __marker):
                                    del econtext['item_wf_state_class']
                                else:
                                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_140656454077008
                                __append(u'\n                                ')

                                # <Static value=<_ast.Dict object at 0x7fed28160310> name=None at 7fed28160810> -> __attrs_140656556507792
                                __attrs_140656556507792 = _static_140656556507920

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="discreet">')

                                # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656556507408
                                __default_140656556507408 = _DEFAULT_MARKER

                                # <Value u'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> -> __cache_140656556508688
                                __token = 3887
                                try:
                                    __zt_tmp = __attrs_140656556507792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140656556508688 = _static_140656727176400('python', u'plone_view.cropText(first_parent.Description(), desc_length)', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))

                                # <BinOp left=<Value u'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fed34fe93d0> at 7fed2b6d99d0> -> __condition
                                __expression = __cache_140656556508688

                                # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u' Description ')
                                else:
                                    __content = __cache_140656556508688
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n                            </li>')
                            if (__backup_url_140656454063504 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140656454063504
                            if (__backup_result_type_140656454064848 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140656454064848
                            if (__backup_result_url_140656454065552 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140656454065552
                            __append(u'\n                        ')
                        __append(u'\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656555700752
                        __attrs_140656555700752 = _static_140656773075600
                        __backup_similar_140656454066000 = get('similar', __marker)

                        # <Value u'similar_items' (68:53)> -> __iterator
                        __token = 4125
                        try:
                            __zt_tmp = __attrs_140656555700752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140656727176400('path', u'similar_items', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                        (__iterator, ____index_140656556509520, ) = getitem('repeat')(u'similar', __iterator)
                        econtext['similar'] = None
                        for __item in __iterator:
                            econtext['similar'] = __item
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556507984
                            __attrs_140656556507984 = _static_140656773075600
                            __backup_result_url_140656454064016 = get('result_url', __marker)

                            # <Value u'similar/getURL' (69:55)> -> __value
                            __token = 4196
                            try:
                                __zt_tmp = __attrs_140656556507984
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('path', u'similar/getURL', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140656454062800 = get('result_type', __marker)

                            # <Value u'similar/portal_type' (70:55)> -> __value
                            __token = 4267
                            try:
                                __zt_tmp = __attrs_140656556507984
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('path', u'similar/portal_type', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140656454065808 = get('url', __marker)

                            # <Value u"python:result_url + '/view' if result_type in use_view_action else result_url" (71:46)> -> __value
                            __token = 4335
                            try:
                                __zt_tmp = __attrs_140656556507984
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('python', u"result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fed280d7890> name=None at 7fed280d7410> -> __attrs_140656555946640
                            __attrs_140656555946640 = _static_140656555948176
                            __backup_item_wf_state_class_140656454076944 = get('item_wf_state_class', __marker)

                            # <Value u'string: state-${similar/review_state}' (73:67)> -> __value
                            __token = 4534
                            try:
                                __zt_tmp = __attrs_140656555946640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140656727176400('string', u' state-${similar/review_state}', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            econtext['item_wf_state_class'] = __value

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a')

                            # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656555947280
                            __default_140656555947280 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution u'${url}' (72:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fed280d7b50> -> __attr_href
                            __token = 4459
                            __token = 4461
                            try:
                                __zt_tmp = __attrs_140656555946640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140656727176400('path', u'url', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = __attr_href
                            if (__attr_href is None):
                                pass
                            else:
                                if (__attr_href is _DEFAULT_MARKER):
                                    __attr_href = None
                                else:
                                    __tt = type(__attr_href)
                                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                                        __attr_href = unicode(__attr_href)
                                    else:
                                        if (__tt is str):
                                            __attr_href = decode(__attr_href)
                                        else:
                                            if (__tt is not unicode):
                                                try:
                                                    __attr_href = __attr_href.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_href)
                                                    __attr_href = (unicode(__attr_href) if (__attr_href is __converted) else __converted)
                                                else:
                                                    __attr_href = __attr_href()
                            if (__attr_href is not None):
                                __append((u' href="%s"' % __attr_href))

                            # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656555947856
                            __default_140656555947856 = _DEFAULT_MARKER

                            # <Substitution u"python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (74:57)> -> __attr_class
                            __token = 4631
                            try:
                                __zt_tmp = __attrs_140656555946640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140656727176400('python', u"'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Interpolation value=<Substitution u'${similar/pretty_title_or_id}' (74:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fed280d7e10> -> __content_140656833983712
                            __token = 4707
                            __token = 4709
                            try:
                                __zt_tmp = __attrs_140656555946640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140656833983712 = _static_140656727176400('path', u'similar/pretty_title_or_id', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                            __content_140656833983712 = __quote(__content_140656833983712, '\x00', '&#0;', None, None)
                            __content_140656833983712 = __content_140656833983712
                            if (__content_140656833983712 is None):
                                pass
                            else:
                                if (__content_140656833983712 is None):
                                    __content_140656833983712 = None
                                else:
                                    __tt = type(__content_140656833983712)
                                    if ((__tt is int) or (__tt is float) or (__tt is long)):
                                        __content_140656833983712 = unicode(__content_140656833983712)
                                    else:
                                        if (__tt is str):
                                            __content_140656833983712 = decode(__content_140656833983712)
                                        else:
                                            if (__tt is not unicode):
                                                try:
                                                    __content_140656833983712 = __content_140656833983712.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_140656833983712)
                                                    __content_140656833983712 = (unicode(__content_140656833983712) if (__content_140656833983712 is __converted) else __converted)
                                                else:
                                                    __content_140656833983712 = __content_140656833983712()
                            if (__content_140656833983712 is not None):
                                __append(__content_140656833983712)
                            __append(u'</a>')
                            if (__backup_item_wf_state_class_140656454076944 is __marker):
                                del econtext['item_wf_state_class']
                            else:
                                econtext['item_wf_state_class'] = __backup_item_wf_state_class_140656454076944
                            __append(u'\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fed280d7d10> name=None at 7fed280d7490> -> __attrs_140656556546256
                            __attrs_140656556546256 = _static_140656555949328

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="discreet">')

                            # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656555946768
                            __default_140656555946768 = _DEFAULT_MARKER

                            # <Value u"python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> -> __cache_140656555948112
                            __token = 4792
                            try:
                                __zt_tmp = __attrs_140656556546256
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140656555948112 = _static_140656727176400('python', u"plone_view.cropText(similar.Description or '', desc_length)", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))

                            # <BinOp left=<Value u"python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fed34fe93d0> at 7fed280d7fd0> -> __condition
                            __expression = __cache_140656555948112

                            # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u' Description ')
                            else:
                                __content = __cache_140656555948112
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                            </li>')
                            if (__backup_url_140656454065808 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140656454065808
                            if (__backup_result_type_140656454062800 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140656454062800
                            if (__backup_result_url_140656454064016 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140656454064016
                            __append(u'\n                        ')
                            ____index_140656556509520 -= 1
                            if (____index_140656556509520 > 0):
                                __append('')
                        if (__backup_similar_140656454066000 is __marker):
                            del econtext['similar']
                        else:
                            econtext['similar'] = __backup_similar_140656454066000
                        __append(u'\n\n                        </ul>\n                        </nav>\n\n                    ')
                    if (__backup_normalizeString_140656454051344 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140656454051344
                    if (__backup_desc_length_140656454053328 is __marker):
                        del econtext['desc_length']
                    else:
                        econtext['desc_length'] = __backup_desc_length_140656454053328
                    if (__backup_use_view_action_140656454063696 is __marker):
                        del econtext['use_view_action']
                    else:
                        econtext['use_view_action'] = __backup_use_view_action_140656454063696
                    if (__backup_registry_140656454065744 is __marker):
                        del econtext['registry']
                    else:
                        econtext['registry'] = __backup_registry_140656454065744
                    if (__backup_plone_view_140656454052368 is __marker):
                        del econtext['plone_view']
                    else:
                        econtext['plone_view'] = __backup_plone_view_140656454052368
                    if (__backup_similar_items_140656454065872 is __marker):
                        del econtext['similar_items']
                    else:
                        econtext['similar_items'] = __backup_similar_items_140656454065872
                    if (__backup_first_parent_140656454063120 is __marker):
                        del econtext['first_parent']
                    else:
                        econtext['first_parent'] = __backup_first_parent_140656454063120
                    __append(u'\n                </div>\n            ')
                    if (__backup_redirection_view_140656453623120 is __marker):
                        del econtext['redirection_view']
                    else:
                        econtext['redirection_view'] = __backup_redirection_view_140656453623120
                    __append(u'\n\n        ')
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656453451152
                __attrs_140656453451152 = _static_140656773075600
                __backup_isManager_140656587784656 = get('isManager', __marker)

                # <Value u'view/is_manager' (89:35)> -> __value
                __token = 5260
                try:
                    __zt_tmp = __attrs_140656453451152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140656727176400('path', u'view/is_manager', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                econtext['isManager'] = __value

                # <Value u"python: err_type != 'NotFound'" (88:41)> -> __condition
                __token = 5193
                try:
                    __zt_tmp = __attrs_140656453451152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140656727176400('python', u" err_type != 'NotFound'", econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fed2809bf90> name=None at 7fed21fa58d0> -> __attrs_140656452195216
                    __attrs_140656452195216 = _static_140656555704208

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h1 class="documentFirstHeading">')
                    __stream_140656454029968 = []
                    __append_140656454029968 = __stream_140656454029968.append
                    __append_140656454029968(u'\n                We&#8217;re sorry, but there seems to be an error&hellip;\n            ')
                    __msgid_140656454029968 = __re_whitespace(''.join(__stream_140656454029968)).strip()
                    if u'heading_site_error_sorry':
                        __append(translate(u'heading_site_error_sorry', mapping=None, default=__msgid_140656454029968, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h1>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fed28169950> name=None at 7fed28160b50> -> __attrs_140656556544656
                    __attrs_140656556544656 = _static_140656556546384

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n                ')

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556546448
                    __attrs_140656556546448 = _static_140656773075600

                    # <Value u'isManager' (97:36)> -> __condition
                    __token = 5548
                    try:
                        __zt_tmp = __attrs_140656556546448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140656727176400('path', u'isManager', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556434512
                        __attrs_140656556434512 = _static_140656773075600

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __stream_140656556434192 = []
                        __append_140656556434192 = __stream_140656556434192.append
                        __append_140656556434192(u'\n                   Here is the full error message:\n                   ')
                        __msgid_140656556434192 = __re_whitespace(''.join(__stream_140656556434192)).strip()
                        if u'description_site_admin_full_error':
                            __append(translate(u'description_site_admin_full_error', mapping=None, default=__msgid_140656556434192, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</p>\n\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556435920
                        __attrs_140656556435920 = _static_140656773075600

                        # <pre ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<pre>')

                        # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656556436304
                        __default_140656556436304 = _DEFAULT_MARKER

                        # <Value u'err_tb' (102:37)> -> __cache_140656556433744
                        __token = 5747
                        try:
                            __zt_tmp = __attrs_140656556435920
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140656556433744 = _static_140656727176400('path', u'err_tb', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))

                        # <BinOp left=<Value u'err_tb' (102:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fed34fe93d0> at 7fed2814e5d0> -> __condition
                        __expression = __cache_140656556433744

                        # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140656556433744
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</pre>\n                </div>')
                    __append(u'\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556434064
                    __attrs_140656556434064 = _static_140656773075600

                    # <Value u'not:isManager' (105:40)> -> __condition
                    __token = 5821
                    try:
                        __zt_tmp = __attrs_140656556434064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140656727176400('not', u'isManager', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556404944
                        __attrs_140656556404944 = _static_140656773075600

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')
                        __stream_140656456184848_site_admin = ''
                        __stream_140656556408528 = []
                        __append_140656556408528 = __stream_140656556408528.append
                        __append_140656556408528(u'\n                    If you are certain you have the correct web address but are encountering an error, please\n                    contact the ')
                        __stream_140656456184848_site_admin = []
                        __append_140656456184848_site_admin = __stream_140656456184848_site_admin.append

                        # <Static value=<_ast.Dict object at 0x7fed34fe9290> name=None at 7fed34fe9190> -> __attrs_140656556407184
                        __attrs_140656556407184 = _static_140656773075600

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140656456184848_site_admin(u'<span>\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fed28147f10> name=None at 7fed281471d0> -> __attrs_140656556372368
                        __attrs_140656556372368 = _static_140656556408592

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140656456184848_site_admin(u'<a')

                        # <Symbol value=<DEFAULT> at 7fed34fe93d0> -> __default_140656556408080
                        __default_140656556408080 = _DEFAULT_MARKER

                        # <Substitution u'string:${context/portal_url}/contact-info' (111:44)> -> __attr_href
                        __token = 6222
                        try:
                            __zt_tmp = __attrs_140656556372368
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140656727176400('string', u'${context/portal_url}/contact-info', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140656456184848_site_admin((u' href="%s"' % __attr_href))
                        __append_140656456184848_site_admin(u'>')
                        __stream_140656556405456 = []
                        __append_140656556405456 = __stream_140656556405456.append
                        __append_140656556405456(u'site administration')
                        __msgid_140656556405456 = __re_whitespace(''.join(__stream_140656556405456)).strip()
                        if u'label_site_admin':
                            __append_140656456184848_site_admin(translate(u'label_site_admin', mapping=None, default=__msgid_140656556405456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append_140656456184848_site_admin(u'</a></span>')
                        __append_140656556408528(u'${site_admin}')
                        __stream_140656456184848_site_admin = ''.join(__stream_140656456184848_site_admin)
                        __append_140656556408528(u'.\n                    ')
                        __msgid_140656556408528 = __re_whitespace(''.join(__stream_140656556408528)).strip()
                        if u'description_site_error_mail_site_admin':
                            __append(translate(u'description_site_error_mail_site_admin', mapping={u'site_admin': __stream_140656456184848_site_admin, }, default=__msgid_140656556408528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</p>\n                ')
                    __append(u'\n            </div>\n\n        ')
                if (__backup_isManager_140656587784656 is __marker):
                    del econtext['isManager']
                else:
                    econtext['isManager'] = __backup_isManager_140656587784656
                __append(u'\n\n')
                if (__backup_err_log_id_140656453681104 is __marker):
                    del econtext['err_log_id']
                else:
                    econtext['err_log_id'] = __backup_err_log_id_140656453681104
                if (__backup_err_tb_140656452988112 is __marker):
                    del econtext['err_tb']
                else:
                    econtext['err_tb'] = __backup_err_tb_140656452988112
                if (__backup_err_type_140656453622096 is __marker):
                    del econtext['err_type']
                else:
                    econtext['err_type'] = __backup_err_type_140656453622096
            _slots = econtext[u'__slot_main'] = _deque((__fill_main, ))

            # <Value u'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140656452078416
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140656727176400('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140656727177104(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140656568023392 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140656568023392
            __i18n_domain = __previous_i18n_domain_140656453510032
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }