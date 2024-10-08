# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Zope-4.8.10-py2.7.egg/Products/Five/utilities/browser/edit_markers.pt'

__tokens = {803: (u'request/ACTUAL_URL', 22, 33), 991: (u'view/getInterfaceNames', 27, 34), 1141: (u'interface/name', 30, 27), 1226: (u'view/getDirectlyProvidedNames', 33, 34), 1416: (u'interface/name', 36, 38), 1472: (u' interface/nam', 37, 40), 1570: (u'interface/name', 40, 27), 1648: (u'view/getDirectlyProvidedNames', 43, 27), 2151: (u'view/getAvailableInterfaceNames', 57, 34), 2340: (u'interface/name', 60, 38), 2396: (u' interface/nam', 61, 40), 2494: (u'interface/name', 64, 27), 2629: (u'view/getAvailableInterfaceNames', 67, 70), 23: (u'context/@@standard_macros/page', 1, 23), 23: (u'context/@@standard_macros/page', 1, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240907051088 = {u'class': u'form-help formHelp', }
_static_140240608386832 = {u'class': u'zmi-controls form-group form-inline', }
_static_140240801798288 = {u'class': u'table table-striped table-hover table-sm', }
_static_140241087907024 = __compile_zt_expr
_static_140240792007184 = {u'class': u'zmi-object-id', }
_static_140240603791696 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Add', u'name': u'SAVE', }
_static_140240601736848 = {u'class': u'table table-striped table-hover table-sm', }
_static_140240801991568 = {u'class': u'zmi-object-check text-right', }
_static_140240801988944 = {u'class': u'zmi-object-id', }
_static_140241133802128 = {}
_static_140240608383440 = {u'class': u'zmi-object-check text-right', }
_static_140240608719888 = {u'class': u'zmi-object-id', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240802346896 = u'page'
_static_140240792009040 = {u'class': u'zmi-object-check text-right', }
_static_140240801796368 = {u'action': u'.', u'method': u'post', }
_static_140240786651792 = {u'type': u'checkbox', u'id': u'INTERFACE', u'value': u'interface/name', u'name': u'remove:list', }
_static_140240603845328 = {u'class': u'zmi-controls', }
_static_140240603848400 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Remove', u'name': u'SAVE', }
_static_140240608384592 = {u'type': u'checkbox', u'id': u'INTERFACE', u'value': u'interface/name', u'name': u'add:list', }
_static_140240786649296 = {u'class': u'zmi-object-check text-right', }

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240802348880
            __attrs_140240802348880 = _static_140241133802128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6172a050> name=None at 7f8c5893e710> -> __attrs_140240958870288
            __attrs_140240958870288 = _static_140240907051088

            # <p ... (0:0)
            # --------------------------------------------------------
            __append(u'<p class="form-help formHelp">')
            __stream_140240758238928 = []
            __append_140240758238928 = __stream_140240758238928.append
            __append_140240758238928(u'\n      Change the behavior of this object by adding or removing marker\n      interfaces. You can choose one or more interfaces to be added to the\n      list of provided interfaces for this object.\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240801796816
            __attrs_140240801796816 = _static_140241133802128

            # <br ... (0:0)
            # --------------------------------------------------------
            __append_140240758238928(u'<br />\n      A marker interface is used to identify an instance of a piece of\n      content. This allows you to enable and disable views based on marker\n      interfaces for example.\n    ')
            __msgid_140240758238928 = __re_whitespace(''.join(__stream_140240758238928)).strip()
            if __msgid_140240758238928:
                __append(translate(__msgid_140240758238928, mapping=None, default=__msgid_140240758238928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</p>\n    \n    ')

            # <Static value=<_ast.Dict object at 0x7f8c5b2c9110> name=None at 7f8c5b2c9ad0> -> __attrs_140240801796688
            __attrs_140240801796688 = _static_140240801796368

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240801799632
            __default_140240801799632 = _DEFAULT_MARKER

            # <Substitution u'request/ACTUAL_URL' (22:33)> -> __attr_action
            __token = 803
            try:
                __zt_tmp = __attrs_140240801796688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140241087907024('path', u'request/ACTUAL_URL', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' method="post">\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240801799248
            __attrs_140240801799248 = _static_140241133802128

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h3>')
            __stream_140240801797968 = []
            __append_140240801797968 = __stream_140240801797968.append
            __append_140240801797968(u'Provided interfaces')
            __msgid_140240801797968 = __re_whitespace(''.join(__stream_140240801797968)).strip()
            if u'legend_provided':
                __append(translate(u'legend_provided', mapping=None, default=__msgid_140240801797968, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h3>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c5b2c9890> name=None at 7f8c5b2c9d50> -> __attrs_140240801799120
            __attrs_140240801799120 = _static_140240801798288

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792007568
            __attrs_140240792007568 = _static_140241133802128
            __backup_interface_140240792912080 = get('interface', __marker)

            # <Value u'view/getInterfaceNames' (27:34)> -> __iterator
            __token = 991
            try:
                __zt_tmp = __attrs_140240792007568
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/getInterfaceNames', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240792008016, ) = getitem('repeat')(u'interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5a973950> name=None at 7f8c5a973b90> -> __attrs_140240792009424
                __attrs_140240792009424 = _static_140240792009040

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5a973210> name=None at 7f8c5a973710> -> __attrs_140240792009808
                __attrs_140240792009808 = _static_140240792007184

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240792010704
                __default_140240792010704 = _DEFAULT_MARKER

                # <Value u'interface/name' (30:27)> -> __cache_140240792010384
                __token = 1141
                try:
                    __zt_tmp = __attrs_140240792009808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240792010384 = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'interface/name' (30:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a973510> -> __condition
                __expression = __cache_140240792010384

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Interface Name')
                else:
                    __content = __cache_140240792010384
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</td>\n        </tr>')
                ____index_140240792008016 -= 1
                if (____index_140240792008016 > 0):
                    __append('\n        ')
            if (__backup_interface_140240792912080 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140240792912080
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792010640
            __attrs_140240792010640 = _static_140241133802128
            __backup_interface_140240762918608 = get('interface', __marker)

            # <Value u'view/getDirectlyProvidedNames' (33:34)> -> __iterator
            __token = 1226
            try:
                __zt_tmp = __attrs_140240792010640
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/getDirectlyProvidedNames', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240609140880, ) = getitem('repeat')(u'interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5a4570d0> name=None at 7f8c5a457050> -> __attrs_140240786650768
                __attrs_140240786650768 = _static_140240786649296

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-check text-right">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c5a457a90> name=None at 7f8c5a457990> -> __attrs_140240801992592
                __attrs_140240801992592 = _static_140240786651792

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240786649488
                __default_140240786649488 = _DEFAULT_MARKER

                # <Substitution u'interface/name' (36:38)> -> __attr_id
                __token = 1416
                try:
                    __zt_tmp = __attrs_140240801992592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', u'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u' name="remove:list"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240786653136
                __default_140240786653136 = _DEFAULT_MARKER

                # <Substitution u'interface/name' (37:40)> -> __attr_value
                __token = 1472
                try:
                    __zt_tmp = __attrs_140240801992592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n          </td>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5b2f8150> name=None at 7f8c5b2f8550> -> __attrs_140240801992272
                __attrs_140240801992272 = _static_140240801988944

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240801992144
                __default_140240801992144 = _DEFAULT_MARKER

                # <Value u'interface/name' (40:27)> -> __cache_140240786650704
                __token = 1570
                try:
                    __zt_tmp = __attrs_140240801992272
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240786650704 = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'interface/name' (40:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5b2f8090> -> __condition
                __expression = __cache_140240786650704

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Interface Name')
                else:
                    __content = __cache_140240786650704
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</td>\n        </tr>')
                ____index_140240609140880 -= 1
                if (____index_140240609140880 > 0):
                    __append('\n        ')
            if (__backup_interface_140240762918608 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140240762918608
            __append(u'\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240801991952
            __attrs_140240801991952 = _static_140241133802128

            # <Value u'view/getDirectlyProvidedNames' (43:27)> -> __condition
            __token = 1648
            try:
                __zt_tmp = __attrs_140240801991952
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/getDirectlyProvidedNames', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5b2f8b90> name=None at 7f8c5b2f8a10> -> __attrs_140240801991696
                __attrs_140240801991696 = _static_140240801991568

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c4f6012d0> name=None at 7f8c4f601890> -> __attrs_140240603847888
                __attrs_140240603847888 = _static_140240603845328

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-controls">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c4f601ed0> name=None at 7f8c4f601610> -> __attrs_140240801926416
                __attrs_140240801926416 = _static_140240603848400

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240603845584
                __default_140240603845584 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c4f601710> at 7f8c4f601fd0> -> __attr_value
                __attr_value = u'Remove'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n          </td>\n        </tr>')
            __append(u'\n      </table>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240801992208
            __attrs_140240801992208 = _static_140241133802128

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h3>')
            __stream_140240603846352 = []
            __append_140240603846352 = __stream_140240603846352.append
            __append_140240603846352(u'\n        Available Marker Interfaces\n      ')
            __msgid_140240603846352 = __re_whitespace(''.join(__stream_140240603846352)).strip()
            if u'legend_available_marker':
                __append(translate(u'legend_available_marker', mapping=None, default=__msgid_140240603846352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h3>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c4f3fe690> name=None at 7f8c5b2e81d0> -> __attrs_140240608384464
            __attrs_140240608384464 = _static_140240601736848

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240608385360
            __attrs_140240608385360 = _static_140241133802128
            __backup_interface_140240927127184 = get('interface', __marker)

            # <Value u'view/getAvailableInterfaceNames' (57:34)> -> __iterator
            __token = 2151
            try:
                __zt_tmp = __attrs_140240608385360
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/getAvailableInterfaceNames', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240608386576, ) = getitem('repeat')(u'interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c4fa551d0> name=None at 7f8c4fa55190> -> __attrs_140240608386256
                __attrs_140240608386256 = _static_140240608383440

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-check text-right">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c4fa55650> name=None at 7f8c4fa55a10> -> __attrs_140240608720976
                __attrs_140240608720976 = _static_140240608384592

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240608719376
                __default_140240608719376 = _DEFAULT_MARKER

                # <Substitution u'interface/name' (60:38)> -> __attr_id
                __token = 2340
                try:
                    __zt_tmp = __attrs_140240608720976
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', u'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u' name="add:list"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240608722320
                __default_140240608722320 = _DEFAULT_MARKER

                # <Substitution u'interface/name' (61:40)> -> __attr_value
                __token = 2396
                try:
                    __zt_tmp = __attrs_140240608720976
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n          </td>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c4faa7410> name=None at 7f8c4faa7190> -> __attrs_140240608720528
                __attrs_140240608720528 = _static_140240608719888

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240608721808
                __default_140240608721808 = _DEFAULT_MARKER

                # <Value u'interface/name' (64:27)> -> __cache_140240608386704
                __token = 2494
                try:
                    __zt_tmp = __attrs_140240608720528
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240608386704 = _static_140241087907024('path', u'interface/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'interface/name' (64:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4faa7350> -> __condition
                __expression = __cache_140240608386704

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Interface Name')
                else:
                    __content = __cache_140240608386704
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</td>\n        </tr>')
                ____index_140240608386576 -= 1
                if (____index_140240608386576 > 0):
                    __append('\n        ')
            if (__backup_interface_140240927127184 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140240927127184
            __append(u'\n      </table>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c4fa55f10> name=None at 7f8c4fa55bd0> -> __attrs_140240608721168
            __attrs_140240608721168 = _static_140240608386832

            # <Value u'view/getAvailableInterfaceNames' (67:70)> -> __condition
            __token = 2629
            try:
                __zt_tmp = __attrs_140240608721168
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/getAvailableInterfaceNames', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="zmi-controls form-group form-inline">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c4f5f4150> name=None at 7f8c4f5f4790> -> __attrs_140240603794576
                __attrs_140240603794576 = _static_140240603791696

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240603794640
                __default_140240603794640 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c4f5f4890> at 7f8c4f5f4f10> -> __attr_value
                __attr_value = u'Add'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n      </div>')
            __append(u'\n    </form>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_heading(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240802347344
            __attrs_140240802347344 = _static_140241133802128
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240790297168
            __attrs_140240790297168 = _static_140241133802128

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>')
            __stream_140240897190352 = []
            __append_140240897190352 = __stream_140240897190352.append
            __append_140240897190352(u'Assign Marker Interfaces')
            __msgid_140240897190352 = __re_whitespace(''.join(__stream_140240897190352)).strip()
            if u'heading_edit_marker':
                __append(translate(u'heading_edit_marker', mapping=None, default=__msgid_140240897190352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h1>\n  ')
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240802348176
            __attrs_140240802348176 = _static_140241133802128
            __backup_macroname_140240610588064 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c5b34f790> name=None at 7f8c5b34f490> -> __value
            __value = _static_140240802346896
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240802347664
                __attrs_140240802347664 = _static_140241133802128
                __append(u'\n\n  ')
                __token = None
                render_heading(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n  \n  ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n')
            _slots = econtext[u'__slot_body'] = _deque((__fill_body, ))

            # <Value u'context/@@standard_macros/page' (1:23)> -> __macro
            __token = 23
            try:
                __zt_tmp = __attrs_140240802348176
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'context/@@standard_macros/page', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 23
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240610588064 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240610588064
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_main': render_main, u'render_heading': render_heading, 'render': render, }