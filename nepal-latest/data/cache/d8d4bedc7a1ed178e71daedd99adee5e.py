# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/templates/publish.pt'

__tokens = {450: (u'provider:senaite.impress.publishhead', 11, 32), 602: (u'provider:senaite.impress.publishcustomhead', 13, 32), 831: (u'view/get_custom_javascripts', 19, 34), 961: (u'script/filecontents', 21, 50), 1280: (u'provider:senaite.impress.publishtop', 32, 40), 1505: (u'provider:senaite.impress.publishcontent', 39, 40)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574267354320 = {u'class': u'row', u'id': u'publish_controller', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574284437392 = {u'type': u'text/javascript', }
_static_140574505898064 = {u'class': u'container', }
_static_140574267354704 = {u'class': u'col-sm-12', }
_static_140574255217744 = {u'content': u'width=device-width, initial-scale=1', u'name': u'viewport', }
_static_140574442558096 = {}
_static_140574255629776 = {u'charset': u'utf-8', }
_static_140574270568208 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140574266102544 = {u'class': u'col-sm-12 text-right', }
_static_140574275649808 = {u'class': u'card my-4 p-4', }
_static_140574267988048 = {u'class': u'row', }
_static_140574397981968 = __compile_zt_expr
_static_140574267354512 = {u'class': u'row', }
_static_140574272012432 = {u'content': u'IE=edge', u'http-equiv': u'X-UA-Compatible', }

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
            __append(u'<!doctype html>\n')

            # <Static value=<_ast.Dict object at 0x7fd9ff763710> name=None at 7fd9ff763a10> -> __attrs_140574255631504
            __attrs_140574255631504 = _static_140574270568208
            __previous_i18n_domain_140574255629136 = __i18n_domain
            __i18n_domain = u'senaite.impress'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255630224
            __attrs_140574255630224 = _static_140574442558096

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9fe9245d0> name=None at 7fd9fe924090> -> __attrs_140574237110224
            __attrs_140574237110224 = _static_140574255629776

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta charset="utf-8">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff8c4090> name=None at 7fd9fd76cd10> -> __attrs_140574272117072
            __attrs_140574272117072 = _static_140574272012432

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta http-equiv="X-UA-Compatible" content="IE=edge">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9fe8bfc50> name=None at 7fd9ff70d5d0> -> __attrs_140574255216656
            __attrs_140574255216656 = _static_140574255217744

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="viewport" content="width=device-width, initial-scale=1">\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574255216720
            __attrs_140574255216720 = _static_140574442558096

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title>')
            __stream_140574255216016 = []
            __append_140574255216016 = __stream_140574255216016.append
            __append_140574255216016(u'SENAITE IMPRESS')
            __msgid_140574255216016 = __re_whitespace(''.join(__stream_140574255216016)).strip()
            if __msgid_140574255216016:
                __append(translate(__msgid_140574255216016, mapping=None, default=__msgid_140574255216016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</title>\n    <!-- SENAITE IMPRESS HTML head -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268016080
            __attrs_140574268016080 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268017744
            __default_140574268017744 = _DEFAULT_MARKER

            # <Value u'provider:senaite.impress.publishhead' (11:32)> -> __cache_140574255166928
            __token = 450
            try:
                __zt_tmp = __attrs_140574268016080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574255166928 = _static_140574397981968('provider', u'senaite.impress.publishhead', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:senaite.impress.publishhead' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f757c6d0> -> __condition
            __expression = __cache_140574255166928

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574255166928
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    <!-- SENANITE IMPRESS Custom HTML head (after impress core resources)  -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270171536
            __attrs_140574270171536 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270304144
            __default_140574270304144 = _DEFAULT_MARKER

            # <Value u'provider:senaite.impress.publishcustomhead' (13:32)> -> __cache_140574270303504
            __token = 602
            try:
                __zt_tmp = __attrs_140574270171536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574270303504 = _static_140574397981968('provider', u'senaite.impress.publishcustomhead', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:senaite.impress.publishcustomhead' (13:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff722850> -> __condition
            __expression = __cache_140574270303504

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574270303504
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    <!-- /END -->\n\n    <!-- CUSTOM JS\n         N.B. we render the JS inline, because traversal seems to not work for plone:static resouces!\n    -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270172560
            __attrs_140574270172560 = _static_140574442558096
            __backup_script_140574255628560 = get('script', __marker)

            # <Value u'view/get_custom_javascripts' (19:34)> -> __iterator
            __token = 831
            try:
                __zt_tmp = __attrs_140574270172560
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'view/get_custom_javascripts', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574268021584, ) = getitem('repeat')(u'script', __iterator)
            econtext['script'] = None
            for __item in __iterator:
                econtext['script'] = __item
                __append(u'\n      <!-- <tal:t replace="script/filename"/> -->\n      ')

                # <Static value=<_ast.Dict object at 0x7fda0049d790> name=None at 7fda0049db10> -> __attrs_140574254648720
                __attrs_140574254648720 = _static_140574284437392

                # <script ... (0:0)
                # --------------------------------------------------------
                __append(u'<script type="text/javascript">')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284436304
                __default_140574284436304 = _DEFAULT_MARKER

                # <Value u'script/filecontents' (21:50)> -> __cache_140574268019216
                __token = 961
                try:
                    __zt_tmp = __attrs_140574254648720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574268019216 = _static_140574397981968('path', u'script/filecontents', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'script/filecontents' (21:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4f5dd0> -> __condition
                __expression = __cache_140574268019216

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574268019216
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</script>\n    ')
                ____index_140574268021584 -= 1
                if (____index_140574268021584 > 0):
                    __append('')
            if (__backup_script_140574255628560 is __marker):
                del econtext['script']
            else:
                econtext['script'] = __backup_script_140574255628560
            __append(u'\n    <!-- /CUSTOM JS -->\n  </head>\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270170832
            __attrs_140574270170832 = _static_140574442558096

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n    ')

            # <Static value=<_ast.Dict object at 0x7fda0d7d1050> name=None at 7fd9ffc2f990> -> __attrs_140574257245072
            __attrs_140574257245072 = _static_140574505898064

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="container">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ffc3c110> name=None at 7fd9ffc3c750> -> __attrs_140574267904592
            __attrs_140574267904592 = _static_140574275649808

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="card my-4 p-4">\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4ed850> name=None at 7fd9ff4ede10> -> __attrs_140574254005072
            __attrs_140574254005072 = _static_140574267988048

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9ff321310> name=None at 7fd9ff3213d0> -> __attrs_140574255163856
            __attrs_140574255163856 = _static_140574266102544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12 text-right">\n            <!-- Viewlet manager: publish top -->\n            ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267354896
            __attrs_140574267354896 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267353168
            __default_140574267353168 = _DEFAULT_MARKER

            # <Value u'provider:senaite.impress.publishtop' (32:40)> -> __cache_140574267352080
            __token = 1280
            try:
                __zt_tmp = __attrs_140574267354896
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574267352080 = _static_140574397981968('provider', u'senaite.impress.publishtop', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:senaite.impress.publishtop' (32:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff452750> -> __condition
            __expression = __cache_140574267352080

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574267352080
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n          </div>\n        </div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff452d90> name=None at 7fda00047e10> -> __attrs_140574267353360
            __attrs_140574267353360 = _static_140574267354512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9ff452e50> name=None at 7fd9ff452510> -> __attrs_140574284375504
            __attrs_140574284375504 = _static_140574267354704

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-sm-12">\n            <!-- Viewlet manager: report header -->\n            ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574256072016
            __attrs_140574256072016 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267316752
            __default_140574267316752 = _DEFAULT_MARKER

            # <Value u'provider:senaite.impress.publishcontent' (39:40)> -> __cache_140574284376208
            __token = 1505
            try:
                __zt_tmp = __attrs_140574256072016
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574284376208 = _static_140574397981968('provider', u'senaite.impress.publishcontent', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:senaite.impress.publishcontent' (39:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda00491150> -> __condition
            __expression = __cache_140574284376208

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140574284376208
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n          </div>\n        </div>\n\n        <!-- ReactJS controlled component -->\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff452cd0> name=None at 7fd9ff452a10> -> __attrs_140574256071760
            __attrs_140574256071760 = _static_140574267354320

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row" id="publish_controller"></div>\n\n      </div> <!-- /card -->\n    </div> <!-- /container -->\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140574255629136
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }