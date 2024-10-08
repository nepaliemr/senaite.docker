# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/main_template/templates/main_template.pt'

__tokens = {5367: (u'provider:plone.abovecontenttitle', 121, 87), 5527: (u'context/@@title', 123, 55), 5675: (u'provider:plone.belowcontenttitle', 125, 87), 5847: (u'context/@@description', 128, 54), 6039: (u'provider:plone.abovecontentbody', 132, 84), 6201: (u'nothing', 134, 78), 6409: (u'provider:plone.belowcontentbody', 138, 84), 73: (u'string:&lt;!DOCTYPE ht', 2, 38), 357: (u"python:context.restrictedTraverse('@@senaite_theme')", 8, 34), 443: (u" python:context.restrictedTraverse('@@senaite_view'", 9, 32), 520: (u't nocall:senaite_view/te', 10, 23), 578: (u"te python:context.restrictedTraverse('@@plone_portal_stat", 11, 30), 670: (u"ate python:context.restrictedTraverse('@@plone_context_sta", 12, 30), 760: (u"view python:context.restrictedTraverse('@@pl", 13, 26), 838: (u"ayout python:context.restrictedTraverse('@@plone_la", 14, 27), 924: (u"apview python:context.restrictedTraverse('@@bootstra", 15, 27), 1002: (u'   lang python:portal_state.la', 16, 17), 1058: (u'    view nocall:view | nocall: p', 17, 16), 1117: (u'    dummy python: plone_layout.mark_', 18, 16), 1185: (u'portal_url python:portal_state.p', 19, 20), 1254: (u"kPermission python:context.restrictedTraverse('portal_membership').che", 20, 24), 1361: (u"e_properties python:context.restrictedTraverse('portal_properties').si", 21, 23), 1470: (u"_include_head python:request.get('ajax_include", 22, 24), 1547: (u'     ajax_lo', 23, 15), 1634: (u'lang', 25, 29), 1683: (u'provider:plone.httpheaders', 27, 40), 1753: (u'provider:plone.htmlhead', 29, 38), 1810: (u'nothing', 31, 28), 2570: (u'bootstrapview/get_viewport_values', 49, 39), 2641: (u'viewportvalues', 50, 36), 2805: (u'portal_state/is_rtl', 54, 28), 2850: (u" python:plone_layout.have_portlets('plone.leftcolumn', view", 55, 24), 2935: (u"r python:plone_layout.have_portlets('plone.rightcolumn', vie", 56, 23), 3029: (u'ss python:plone_layout.bodyClass(template, vi', 57, 30), 3101: (u'cls python:bootstrapview.get_columns_classes(v', 58, 22), 3307: (u'  python:bootstrapview.get_data_settings', 61, 24), 3185: (u'string:${body_class} senaite-body', 59, 32), 3249: (u" python:isRTL and 'rtl' or 'ltr", 60, 29), 3560: (u'provider:plone.toolbar', 69, 36), 3691: (u'provider:senaite.sidebar', 75, 36), 3952: (u'provider:plone.portaltop', 83, 44), 4175: (u'provider:plone.mainnavigation', 90, 69), 4465: (u'provider:plone.globalstatusmessage', 99, 52), 4782: (u'provider:plone.abovecontent', 108, 69), 4981: (u'cls/content', 114, 70), 6697: (u'provider:plone.belowcontent', 148, 71), 6938: (u'sl', 155, 34), 6983: (u'cls/one', 156, 41), 7102: (u'provider:plone.leftcolumn', 158, 46), 7347: (u'sr', 165, 34), 7392: (u'cls/two', 166, 41), 7511: (u'provider:plone.rightcolumn', 168, 46), 7720: (u'provider:plone.portalfooter', 175, 40)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574257250832 = {u'id': u'viewlet-below-content-title', }
_static_140574257265168 = {u'class': u'row', }
_static_140574275598224 = {u'id': u'loader', u'i18n-translate': u'', }
_static_140574257291344 = {u'id': u'portal-footer-wrapper', }
_static_140574253165200 = {u'class': u'col-sm-12', }
_static_140574257183440 = {u'class': u'row', }
_static_140574257192592 = {u'id': u'viewlet-above-content', }
_static_140574397981968 = __compile_zt_expr
_static_140574257182736 = {u'class': u'row', }
_static_140574257168784 = {u'class': u'col-sm-12', }
_static_140574257182864 = {u'class': u'col-sm-12', }
_static_140574257292816 = {u'id': u'portal-column-two', u'class': u'cls/two', }
_static_140574257288208 = {u'id': u'viewlet-above-content-body', }
_static_140574253157712 = {u'id': u'viewlet-below-content', }
_static_140574257245520 = {u'id': u'portal-column-one', u'class': u'cls/one', }
_static_140574442558096 = {}
_static_140574275642576 = {u'content': u'width=device-width, initial-scale=0.6666, maximum-scale=1.0, minimum-scale=0.6666', u'name': u'viewport', }
_static_140574257223632 = {u'id': u'content', }
_static_140574257145488 = {u'content': u'SENAITE - https://www.senaite.com', u'name': u'generator', }
_static_140574284352720 = set([])
_static_140574397982672 = __C2ZContextWrapper
_static_140574257188944 = {u'class': u'row', }
_static_140574257171536 = {u'id': u'portal-mainnavigation', }
_static_140574257174096 = {u'id': u'portal-column-content', u'class': u'cls/content', }
_static_140574275642768 = {u'id': u'visual-portal-wrapper', u'dir': u"python:isRTL and 'rtl' or 'ltr'", u'class': u'string:${body_class} senaite-body', }
_static_140574257221072 = {u'id': u'viewlet-above-content-title', }
_static_140574257262992 = {u'id': u'global_statusmessage', }
_static_140574254646160 = {u'class': u'mb-2', }
_static_140574257140368 = {u'class': u'wrapper', }
_static_140574257242640 = {u'id': u'viewlet-below-content-body', }
_static_140574257287440 = {u'id': u'content-core', }
_static_140574257169424 = {u'class': u'row', }
_static_140574275652432 = {u'lang': u'lang', u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140574257184592 = {u'id': u'portal-top', }
_static_140574257140112 = {u'class': u'container-fluid', }
_static_140574257191184 = {u'class': u'col-sm-12', }

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

    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_content_description = econtext[u'__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_main = econtext[u'__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_body = econtext[u'__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_core = econtext[u'__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_content_title = econtext[u'__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257223184
            __attrs_140574257223184 = _static_140574442558096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n                  ')
            if (__slot_body is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257224720
                __attrs_140574257224720 = _static_140574442558096
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7fd9feaa97d0> name=None at 7fd9feaa9a90> -> __attrs_140574257222736
                __attrs_140574257222736 = _static_140574257223632

                # <article ... (0:0)
                # --------------------------------------------------------
                __append(u'<article id="content">\n                      ')
                if (__slot_main is None):

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574253155856
                    __attrs_140574253155856 = _static_140574442558096
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257217872
                    __attrs_140574257217872 = _static_140574442558096

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header>\n                          ')

                    # <Static value=<_ast.Dict object at 0x7fd9feaa8dd0> name=None at 7fd9feaa8d90> -> __attrs_140574257219280
                    __attrs_140574257219280 = _static_140574257221072

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257221136
                    __default_140574257221136 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontenttitle' (121:87)> -> __cache_140574257220560
                    __token = 5367
                    try:
                        __zt_tmp = __attrs_140574257219280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574257220560 = _static_140574397981968('provider', u'plone.abovecontenttitle', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontenttitle' (121:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa8f10> -> __condition
                    __expression = __cache_140574257220560

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574257220560
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n                          ')
                    if (__slot_content_title is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257220944
                        __attrs_140574257220944 = _static_140574442558096
                        __append(u'\n                            ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257250384
                        __attrs_140574257250384 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257253904
                        __default_140574257253904 = _DEFAULT_MARKER

                        # <Value u'context/@@title' (123:55)> -> __cache_140574257254288
                        __token = 5527
                        try:
                            __zt_tmp = __attrs_140574257250384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574257254288 = _static_140574397981968('path', u'context/@@title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@title' (123:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab0810> -> __condition
                        __expression = __cache_140574257254288

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<h1 />')
                        else:
                            __content = __cache_140574257254288
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                          ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append(u'\n                          ')

                    # <Static value=<_ast.Dict object at 0x7fd9feab0210> name=None at 7fd9feab0850> -> __attrs_140574257251280
                    __attrs_140574257251280 = _static_140574257250832

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257252048
                    __default_140574257252048 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontenttitle' (125:87)> -> __cache_140574257220112
                    __token = 5675
                    try:
                        __zt_tmp = __attrs_140574257251280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574257220112 = _static_140574397981968('provider', u'plone.belowcontenttitle', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontenttitle' (125:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa88d0> -> __condition
                    __expression = __cache_140574257220112

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574257220112
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n\n                          ')
                    if (__slot_content_description is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257251088
                        __attrs_140574257251088 = _static_140574442558096
                        __append(u'\n                            ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257288144
                        __attrs_140574257288144 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257288656
                        __default_140574257288656 = _DEFAULT_MARKER

                        # <Value u'context/@@description' (128:54)> -> __cache_140574257254352
                        __token = 5847
                        try:
                            __zt_tmp = __attrs_140574257288144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574257254352 = _static_140574397981968('path', u'context/@@description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@description' (128:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab0bd0> -> __condition
                        __expression = __cache_140574257254352

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<p />')
                        else:
                            __content = __cache_140574257254352
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                          ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append(u'\n                        </header>\n\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fd9feab9410> name=None at 7fd9feaa8850> -> __attrs_140574257289296
                    __attrs_140574257289296 = _static_140574257288208

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257220048
                    __default_140574257220048 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontentbody' (132:84)> -> __cache_140574257253456
                    __token = 6039
                    try:
                        __zt_tmp = __attrs_140574257289296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574257253456 = _static_140574397981968('provider', u'plone.abovecontentbody', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontentbody' (132:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa8210> -> __condition
                    __expression = __cache_140574257253456

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574257253456
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fd9feab9110> name=None at 7fd9feab9050> -> __attrs_140574257288912
                    __attrs_140574257288912 = _static_140574257287440

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n                          ')
                    if (__slot_content_core is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257291088
                        __attrs_140574257291088 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257290000
                        __default_140574257290000 = _DEFAULT_MARKER

                        # <Value u'nothing' (134:78)> -> __cache_140574257290320
                        __token = 6201
                        try:
                            __zt_tmp = __attrs_140574257291088
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574257290320 = _static_140574397981968('path', u'nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'nothing' (134:78)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab9cd0> -> __condition
                        __expression = __cache_140574257290320

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                            Page body text\n                          ')
                        else:
                            __content = __cache_140574257290320
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append(u'\n                        </div>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7fd9feaae210> name=None at 7fd9feaae6d0> -> __attrs_140574257242384
                    __attrs_140574257242384 = _static_140574257242640

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257291024
                    __default_140574257291024 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontentbody' (138:84)> -> __cache_140574257288976
                    __token = 6409
                    try:
                        __zt_tmp = __attrs_140574257242384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574257288976 = _static_140574397981968('provider', u'plone.belowcontentbody', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontentbody' (138:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab99d0> -> __condition
                    __expression = __cache_140574257288976

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140574257288976
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n\n                      ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append(u'\n                    </article>\n\n                  ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append(u'\n                </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_senaite_legacy_js = econtext[u'__slot_senaite_legacy_js'].pop()
        except:
            __slot_senaite_legacy_js = None

        try:
            __slot_senaite_legacy_resources = econtext[u'__slot_senaite_legacy_resources'].pop()
        except:
            __slot_senaite_legacy_resources = None

        try:
            __slot_head_slot = econtext[u'__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_column_two_slot = econtext[u'__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_column_one_slot = econtext[u'__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_global_statusmessage = econtext[u'__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_senaite_legacy_css = econtext[u'__slot_senaite_legacy_css'].pop()
        except:
            __slot_senaite_legacy_css = None

        try:
            __slot_top_slot = econtext[u'__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_portlets_one_slot = econtext[u'__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_portlets_two_slot = econtext[u'__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_content = econtext[u'__slot_content'].pop()
        except:
            __slot_content = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275636112
            __attrs_140574275636112 = _static_140574442558096
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275634576
            __attrs_140574275634576 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275636176
            __default_140574275636176 = _DEFAULT_MARKER

            # <Value u'string:<!DOCTYPE html>' (2:38)> -> __cache_140574275636688
            __token = 73
            try:
                __zt_tmp = __attrs_140574275634576
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574275636688 = _static_140574397981968('string', u'<!DOCTYPE html>', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'string:<!DOCTYPE html>' (2:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc38cd0> -> __condition
            __expression = __cache_140574275636688

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574275636688
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc3cb50> name=None at 7fda00b5e810> -> __attrs_140574275651984
            __attrs_140574275651984 = _static_140574275652432
            __backup_senaite_theme_140574275635472 = get('senaite_theme', __marker)

            # <Value u"python:context.restrictedTraverse('@@senaite_theme')" (8:34)> -> __value
            __token = 357
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@senaite_theme')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['senaite_theme'] = __value
            __backup_senaite_view_140574275635600 = get('senaite_view', __marker)

            # <Value u"python:context.restrictedTraverse('@@senaite_view')" (9:32)> -> __value
            __token = 443
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@senaite_view')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['senaite_view'] = __value
            __backup_test_140574275634384 = get('test', __marker)

            # <Value u'nocall:senaite_view/test' (10:23)> -> __value
            __token = 520
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('nocall', u'senaite_view/test', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['test'] = __value
            __backup_portal_state_140574275636816 = get('portal_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_portal_state')" (11:30)> -> __value
            __token = 578
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_140574275650960 = get('context_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_context_state')" (12:30)> -> __value
            __token = 670
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_140574275649744 = get('plone_view', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone')" (13:26)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@plone')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_140574275650320 = get('plone_layout', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_layout')" (14:27)> -> __value
            __token = 838
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_bootstrapview_140574275652496 = get('bootstrapview', __marker)

            # <Value u"python:context.restrictedTraverse('@@bootstrapview')" (15:27)> -> __value
            __token = 924
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('@@bootstrapview')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['bootstrapview'] = __value
            __backup_lang_140574275652112 = get('lang', __marker)

            # <Value u'python:portal_state.language()' (16:17)> -> __value
            __token = 1002
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'portal_state.language()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_140574275649680 = get('view', __marker)

            # <Value u'nocall:view | nocall: plone_view' (17:16)> -> __value
            __token = 1058
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('nocall', u'view | nocall: plone_view', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_140574275651088 = get('dummy', __marker)

            # <Value u'python: plone_layout.mark_view(view)' (18:16)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u' plone_layout.mark_view(view)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_140574275651152 = get('portal_url', __marker)

            # <Value u'python:portal_state.portal_url()' (19:20)> -> __value
            __token = 1185
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'portal_state.portal_url()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_140574275651280 = get('checkPermission', __marker)

            # <Value u"python:context.restrictedTraverse('portal_membership').checkPermission" (20:24)> -> __value
            __token = 1254
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_140574275651472 = get('site_properties', __marker)

            # <Value u"python:context.restrictedTraverse('portal_properties').site_properties" (21:23)> -> __value
            __token = 1361
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_140574275651600 = get('ajax_include_head', __marker)

            # <Value u"python:request.get('ajax_include_head', False)" (22:24)> -> __value
            __token = 1470
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"request.get('ajax_include_head', False)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_140574275651344 = get('ajax_load', __marker)

            # <Value u'python:False' (23:15)> -> __value
            __token = 1547
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'False', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_140574275649488 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275650704
            __default_140574275650704 = _DEFAULT_MARKER

            # <Substitution u'lang' (25:29)> -> __attr_lang
            __token = 1634
            try:
                __zt_tmp = __attrs_140574275651984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140574397981968('path', u'lang', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275647888
            __attrs_140574275647888 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275647760
            __default_140574275647760 = _DEFAULT_MARKER

            # <Value u'provider:plone.httpheaders' (27:40)> -> __cache_140574275648848
            __token = 1683
            try:
                __zt_tmp = __attrs_140574275647888
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574275648848 = _static_140574397981968('provider', u'plone.httpheaders', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.httpheaders' (27:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc3bc10> -> __condition
            __expression = __cache_140574275648848

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574275648848
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574275648272
            __attrs_140574275648272 = _static_140574442558096

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257144528
            __attrs_140574257144528 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257144080
            __default_140574257144080 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead' (29:38)> -> __cache_140574275647312
            __token = 1753
            try:
                __zt_tmp = __attrs_140574257144528
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574275647312 = _static_140574397981968('provider', u'plone.htmlhead', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead' (29:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ffc3b3d0> -> __condition
            __expression = __cache_140574275647312

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574275647312
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257144784
            __attrs_140574257144784 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257145296
            __default_140574257145296 = _DEFAULT_MARKER

            # <Value u'nothing' (31:28)> -> __cache_140574257143952
            __token = 1810
            try:
                __zt_tmp = __attrs_140574257144784
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257143952 = _static_140574397981968('path', u'nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'nothing' (31:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fea966d0> -> __condition
            __expression = __cache_140574257143952

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n        Various slots where you can insert elements in the header from a template.\n      ')
            else:
                __content = __cache_140574257143952
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n      ')
            if (__slot_top_slot is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257144656
                __attrs_140574257144656 = _static_140574442558096
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n      ')
            if (__slot_head_slot is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257147024
                __attrs_140574257147024 = _static_140574442558096
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n      <!-- Disable all Plone JS/CSS -->\n      <!-- <div tal:replace="structure provider:plone.scripts" /> -->\n      <!-- <metal:javascriptslot define-slot="javascript_head_slot" /> -->\n      <!-- <link tal:replace="structure provider:plone.htmlhead.links" /> -->\n      <!-- <metal:styleslot define-slot="style_slot" /> -->\n\n      <!-- NOTE: All Legacy JS/CSS are rendered at the bottom of the page! -->\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9fea96690> name=None at 7fd9fea96890> -> __attrs_140574275641616
            __attrs_140574275641616 = _static_140574257145488

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="generator" content="SENAITE - https://www.senaite.com" />\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc3a4d0> name=None at 7fd9ffc3a790> -> __attrs_140574275643472
            __attrs_140574275643472 = _static_140574275642576
            __backup_viewportvalues_140574275649232 = get('viewportvalues', __marker)

            # <Value u'bootstrapview/get_viewport_values' (49:39)> -> __value
            __token = 2570
            try:
                __zt_tmp = __attrs_140574275643472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'bootstrapview/get_viewport_values', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['viewportvalues'] = __value

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="viewport"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275642320
            __default_140574275642320 = _DEFAULT_MARKER

            # <Substitution u'viewportvalues' (50:36)> -> __attr_content
            __token = 2641
            try:
                __zt_tmp = __attrs_140574275643472
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_content = _static_140574397981968('path', u'viewportvalues', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_content = __quote(__attr_content, '"', '&quot;', u'width=device-width, initial-scale=0.6666, maximum-scale=1.0, minimum-scale=0.6666', _DEFAULT_MARKER)
            if (__attr_content is not None):
                __append((u' content="%s"' % __attr_content))
            __append(u' />')
            if (__backup_viewportvalues_140574275649232 is __marker):
                del econtext['viewportvalues']
            else:
                econtext['viewportvalues'] = __backup_viewportvalues_140574275649232
            __append(u'\n    </head>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc3a590> name=None at 7fd9ffc3a0d0> -> __attrs_140574275597968
            __attrs_140574275597968 = _static_140574275642768
            __backup_isRTL_140574275649424 = get('isRTL', __marker)

            # <Value u'portal_state/is_rtl' (54:28)> -> __value
            __token = 2805
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'portal_state/is_rtl', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_140574275648976 = get('sl', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.leftcolumn', view)" (55:24)> -> __value
            __token = 2850
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_140574275646608 = get('sr', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.rightcolumn', view)" (56:23)> -> __value
            __token = 2935
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_140574275646800 = get('body_class', __marker)

            # <Value u'python:plone_layout.bodyClass(template, view)' (57:30)> -> __value
            __token = 3029
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['body_class'] = __value
            __backup_cls_140574257145744 = get('cls', __marker)

            # <Value u'python:bootstrapview.get_columns_classes(view)' (58:22)> -> __value
            __token = 3101
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'bootstrapview.get_columns_classes(view)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['cls'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body')

            # <Value u'python:bootstrapview.get_data_settings()' (61:24)> -> __cache_140574275645008
            __token = 3307
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574275645008 = _static_140574397981968('python', u'bootstrapview.get_data_settings()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if (u'id' not in __chain(__cache_140574275645008)):
                __append(u' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275643856
            __default_140574275643856 = _DEFAULT_MARKER

            # <Substitution u'string:${body_class} senaite-body' (59:32)> -> __attr_class
            __token = 3185
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140574397981968('string', u'${body_class} senaite-body', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and (u'class' not in __chain(__cache_140574275645008))):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275643344
            __default_140574275643344 = _DEFAULT_MARKER

            # <Substitution u"python:isRTL and 'rtl' or 'ltr'" (60:29)> -> __attr_dir
            __token = 3249
            try:
                __zt_tmp = __attrs_140574275597968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_140574397981968('python', u"isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and (u'dir' not in __chain(__cache_140574275645008))):
                __append((u' dir="%s"' % __attr_dir))
            __attr_140574275645072 = __cache_140574275645008
            for (name, value, ) in __attr_140574275645072.items():
                if ((name not in _static_140574284352720) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'>\n\n      <!-- Ajax Loader -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc2f790> name=None at 7fd9ffc2f9d0> -> __attrs_140574275598288
            __attrs_140574275598288 = _static_140574275598224

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="loader" i18n-translate="">Loading...</div>\n\n      <!-- Toolbar -->\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9fe834390> name=None at 7fd9fe8345d0> -> __attrs_140574254109520
            __attrs_140574254109520 = _static_140574254646160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="mb-2">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257141904
            __attrs_140574257141904 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257140240
            __default_140574257140240 = _DEFAULT_MARKER

            # <Value u'provider:plone.toolbar' (69:36)> -> __cache_140574347742736
            __token = 3560
            try:
                __zt_tmp = __attrs_140574257141904
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574347742736 = _static_140574397981968('provider', u'plone.toolbar', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.toolbar' (69:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fea96ad0> -> __condition
            __expression = __cache_140574347742736

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574347742736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n      </div>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9fea95290> name=None at 7fd9ffc24fd0> -> __attrs_140574257141264
            __attrs_140574257141264 = _static_140574257140368

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="wrapper">\n\n        <!-- Sidebar -->\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257142608
            __attrs_140574257142608 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257141840
            __default_140574257141840 = _DEFAULT_MARKER

            # <Value u'provider:senaite.sidebar' (75:36)> -> __cache_140574257143440
            __token = 3691
            try:
                __zt_tmp = __attrs_140574257142608
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257143440 = _static_140574397981968('provider', u'senaite.sidebar', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:senaite.sidebar' (75:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fea95f50> -> __condition
            __expression = __cache_140574257143440

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574257143440
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n        <!-- Content -->\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9fea95190> name=None at 7fd9fea952d0> -> __attrs_140574257142736
            __attrs_140574257142736 = _static_140574257140112

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="container-fluid">\n\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9fad0> name=None at 7fda00b4c250> -> __attrs_140574257181072
            __attrs_140574257181072 = _static_140574257183440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9f890> name=None at 7fd9fea9f3d0> -> __attrs_140574257182672
            __attrs_140574257182672 = _static_140574257182864

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9ff50> name=None at 7fd9fea9fa90> -> __attrs_140574257183056
            __attrs_140574257183056 = _static_140574257184592
            __previous_i18n_domain_140574257183248 = __i18n_domain
            __i18n_domain = u'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header id="portal-top">\n                ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574253210512
            __attrs_140574253210512 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574253207952
            __default_140574253207952 = _DEFAULT_MARKER

            # <Value u'provider:plone.portaltop' (83:44)> -> __cache_140574253246992
            __token = 3952
            try:
                __zt_tmp = __attrs_140574253210512
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574253246992 = _static_140574397981968('provider', u'plone.portaltop', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portaltop' (83:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fe6d5950> -> __condition
            __expression = __cache_140574253246992

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574253246992
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n              </header>')
            __i18n_domain = __previous_i18n_domain_140574257183248
            __append(u'\n            </div>\n          </div>\n\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9f810> name=None at 7fd9fea9f510> -> __attrs_140574281803792
            __attrs_140574281803792 = _static_140574257182736

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9c190> name=None at 7fd9fea9c150> -> __attrs_140574257169680
            __attrs_140574257169680 = _static_140574257168784

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9cc50> name=None at 7fd9fea9c8d0> -> __attrs_140574257171024
            __attrs_140574257171024 = _static_140574257171536

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257168912
            __default_140574257168912 = _DEFAULT_MARKER

            # <Value u'provider:plone.mainnavigation' (90:69)> -> __cache_140574257170192
            __token = 4175
            try:
                __zt_tmp = __attrs_140574257171024
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257170192 = _static_140574397981968('provider', u'plone.mainnavigation', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.mainnavigation' (90:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9fea9c0d0> -> __condition
            __expression = __cache_140574257170192

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n                The main navigation\n              ')
            else:
                __content = __cache_140574257170192
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n            </div>\n          </div>\n\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9c410> name=None at 7fd9fea9c310> -> __attrs_140574257171088
            __attrs_140574257171088 = _static_140574257169424

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9fe6caa90> name=None at 7fd9fe6cae90> -> __attrs_140574257264912
            __attrs_140574257264912 = _static_140574253165200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9feab3190> name=None at 7fd9feab3210> -> __attrs_140574257264656
            __attrs_140574257264656 = _static_140574257262992

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside id="global_statusmessage">\n                ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257265616
            __attrs_140574257265616 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257265808
            __default_140574257265808 = _DEFAULT_MARKER

            # <Value u'provider:plone.globalstatusmessage' (99:52)> -> __cache_140574257263888
            __token = 4465
            try:
                __zt_tmp = __attrs_140574257265616
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257263888 = _static_140574397981968('provider', u'plone.globalstatusmessage', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.globalstatusmessage' (99:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feab3d90> -> __condition
            __expression = __cache_140574257263888

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574257263888
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                ')
            if (__slot_global_statusmessage is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257266512
                __attrs_140574257266512 = _static_140574442558096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n                </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append(u'\n              </aside>\n            </div>\n          </div>\n\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9feab3a10> name=None at 7fd9feab3b50> -> __attrs_140574257189520
            __attrs_140574257189520 = _static_140574257265168

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa1910> name=None at 7fd9feaa1a10> -> __attrs_140574257192016
            __attrs_140574257192016 = _static_140574257191184

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n              ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa1e90> name=None at 7fd9feaa1390> -> __attrs_140574257189712
            __attrs_140574257189712 = _static_140574257192592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257189008
            __default_140574257189008 = _DEFAULT_MARKER

            # <Value u'provider:plone.abovecontent' (108:69)> -> __cache_140574257192336
            __token = 4782
            try:
                __zt_tmp = __attrs_140574257189712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257192336 = _static_140574397981968('provider', u'plone.abovecontent', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.abovecontent' (108:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa1790> -> __condition
            __expression = __cache_140574257192336

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574257192336
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n            </div>\n          </div>\n\n          <!-- Main content -->\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9feaa1050> name=None at 7fd9feaa1590> -> __attrs_140574257176336
            __attrs_140574257176336 = _static_140574257188944

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9fea9d650> name=None at 7fd9fea9d710> -> __attrs_140574257174736
            __attrs_140574257174736 = _static_140574257174096

            # <article ... (0:0)
            # --------------------------------------------------------
            __append(u'<article id="portal-column-content"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257176208
            __default_140574257176208 = _DEFAULT_MARKER

            # <Substitution u'cls/content' (114:70)> -> __attr_class
            __token = 4981
            try:
                __zt_tmp = __attrs_140574257174736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140574397981968('path', u'cls/content', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n              ')
            if (__slot_content is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257222096
                __attrs_140574257222096 = _static_140574442558096
                __append(u'\n                ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n\n              ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append(u'\n              ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257224144
            __attrs_140574257224144 = _static_140574442558096

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer>\n                ')

            # <Static value=<_ast.Dict object at 0x7fd9fe6c8d50> name=None at 7fd9fe6c81d0> -> __attrs_140574257244560
            __attrs_140574257244560 = _static_140574253157712

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-below-content">')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574253156432
            __default_140574253156432 = _DEFAULT_MARKER

            # <Value u'provider:plone.belowcontent' (148:71)> -> __cache_140574257223888
            __token = 6697
            try:
                __zt_tmp = __attrs_140574257244560
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257223888 = _static_140574397981968('provider', u'plone.belowcontent', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.belowcontent' (148:71)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa9590> -> __condition
            __expression = __cache_140574257223888

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574257223888
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n              </footer>\n            </article>\n\n            <!-- Column 1 -->\n            ')
            if (__slot_column_one_slot is None):

                # <Static value=<_ast.Dict object at 0x7fd9feaaed50> name=None at 7fd9fea9d850> -> __attrs_140574257244304
                __attrs_140574257244304 = _static_140574257245520

                # <Value u'sl' (155:34)> -> __condition
                __token = 6938
                try:
                    __zt_tmp = __attrs_140574257244304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'sl', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-one"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257245072
                    __default_140574257245072 = _DEFAULT_MARKER

                    # <Substitution u'cls/one' (156:41)> -> __attr_class
                    __token = 6983
                    try:
                        __zt_tmp = __attrs_140574257244304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('path', u'cls/one', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n              ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257294864
                        __attrs_140574257294864 = _static_140574442558096
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257292624
                        __attrs_140574257292624 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257294032
                        __default_140574257294032 = _DEFAULT_MARKER

                        # <Value u'provider:plone.leftcolumn' (158:46)> -> __cache_140574257293712
                        __token = 7102
                        try:
                            __zt_tmp = __attrs_140574257292624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574257293712 = _static_140574397981968('provider', u'plone.leftcolumn', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.leftcolumn' (158:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feabaa90> -> __condition
                        __expression = __cache_140574257293712

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574257293712
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n              ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append(u'\n            </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n            <!-- Column 2 -->\n            ')
            if (__slot_column_two_slot is None):

                # <Static value=<_ast.Dict object at 0x7fd9feaba610> name=None at 7fd9feaba590> -> __attrs_140574257293328
                __attrs_140574257293328 = _static_140574257292816

                # <Value u'sr' (165:34)> -> __condition
                __token = 7347
                try:
                    __zt_tmp = __attrs_140574257293328
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'sr', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-two"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257292048
                    __default_140574257292048 = _DEFAULT_MARKER

                    # <Substitution u'cls/two' (166:41)> -> __attr_class
                    __token = 7392
                    try:
                        __zt_tmp = __attrs_140574257293328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('path', u'cls/two', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n              ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574279892688
                        __attrs_140574279892688 = _static_140574442558096
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257196240
                        __attrs_140574257196240 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257193872
                        __default_140574257193872 = _DEFAULT_MARKER

                        # <Value u'provider:plone.rightcolumn' (168:46)> -> __cache_140574257193552
                        __token = 7511
                        try:
                            __zt_tmp = __attrs_140574257196240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574257193552 = _static_140574397981968('provider', u'plone.rightcolumn', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.rightcolumn' (168:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa2150> -> __condition
                        __expression = __cache_140574257193552

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574257193552
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n              ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append(u'\n            </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n          </div>\n\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9feaba050> name=None at 7fd9feabac90> -> __attrs_140574257196304
            __attrs_140574257196304 = _static_140574257291344
            __previous_i18n_domain_140574257195408 = __i18n_domain
            __i18n_domain = u'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer id="portal-footer-wrapper">\n            ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257196624
            __attrs_140574257196624 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257196944
            __default_140574257196944 = _DEFAULT_MARKER

            # <Value u'provider:plone.portalfooter' (175:40)> -> __cache_140574257196752
            __token = 7720
            try:
                __zt_tmp = __attrs_140574257196624
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574257196752 = _static_140574397981968('provider', u'plone.portalfooter', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portalfooter' (175:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9feaa2f10> -> __condition
            __expression = __cache_140574257196752

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574257196752
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n          </footer>')
            __i18n_domain = __previous_i18n_domain_140574257195408
            __append(u'\n\n        </div>\n\n      </div>\n\n      <!-- NOTE:\n           We define all legacy resource slots at the bottom to ensure these are\n           loaded *after* the JS/CSS from the resources viewlet (rendered in the\n           IHtmlHead viewlet manager) and the HTML is completely loaded.\n      -->\n\n      <!-- SENAITE legacy resouces -->\n      ')
            if (__slot_senaite_legacy_resources is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257195664
                __attrs_140574257195664 = _static_140574442558096
            else:
                __slot_senaite_legacy_resources(__stream, econtext.copy(), rcontext)
            __append(u'\n      <!-- SENAITE legacy JS -->\n      ')
            if (__slot_senaite_legacy_js is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257194320
                __attrs_140574257194320 = _static_140574442558096
            else:
                __slot_senaite_legacy_js(__stream, econtext.copy(), rcontext)
            __append(u'\n      <!-- SENAITE legacy CSS -->\n      ')
            if (__slot_senaite_legacy_css is None):

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574257195024
                __attrs_140574257195024 = _static_140574442558096
            else:
                __slot_senaite_legacy_css(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    </body>')
            if (__backup_cls_140574257145744 is __marker):
                del econtext['cls']
            else:
                econtext['cls'] = __backup_cls_140574257145744
            if (__backup_body_class_140574275646800 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_140574275646800
            if (__backup_sr_140574275646608 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_140574275646608
            if (__backup_sl_140574275648976 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_140574275648976
            if (__backup_isRTL_140574275649424 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_140574275649424
            __append(u'\n  </html>')
            __i18n_domain = __previous_i18n_domain_140574275649488
            if (__backup_ajax_load_140574275651344 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_140574275651344
            if (__backup_ajax_include_head_140574275651600 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_140574275651600
            if (__backup_site_properties_140574275651472 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_140574275651472
            if (__backup_checkPermission_140574275651280 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_140574275651280
            if (__backup_portal_url_140574275651152 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140574275651152
            if (__backup_dummy_140574275651088 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_140574275651088
            if (__backup_view_140574275649680 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_140574275649680
            if (__backup_lang_140574275652112 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_140574275652112
            if (__backup_bootstrapview_140574275652496 is __marker):
                del econtext['bootstrapview']
            else:
                econtext['bootstrapview'] = __backup_bootstrapview_140574275652496
            if (__backup_plone_layout_140574275650320 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_140574275650320
            if (__backup_plone_view_140574275649744 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140574275649744
            if (__backup_context_state_140574275650960 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140574275650960
            if (__backup_portal_state_140574275636816 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140574275636816
            if (__backup_test_140574275634384 is __marker):
                del econtext['test']
            else:
                econtext['test'] = __backup_test_140574275634384
            if (__backup_senaite_view_140574275635600 is __marker):
                del econtext['senaite_view']
            else:
                econtext['senaite_view'] = __backup_senaite_view_140574275635600
            if (__backup_senaite_theme_140574275635472 is __marker):
                del econtext['senaite_theme']
            else:
                econtext['senaite_theme'] = __backup_senaite_theme_140574275635472
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_content': render_content, u'render_master': render_master, 'render': render, }