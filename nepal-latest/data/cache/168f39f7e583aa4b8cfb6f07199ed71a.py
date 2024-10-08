# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/specification_non_compliant_viewlet.pt'

__tokens = {41: (u'python:view.available()', 2, 20), 151: (u'python:view.context', 6, 26), 204: (u' python:view.get_non_compliant_analyses(', 7, 32), 273: (u'e python:view.is_specification_editable', 8, 26), 344: (u"ss python: editable and 'alert-warning' or 'alert-in", 9, 28), 428: (u"ass python: 'portlet-alert-item alert {} alert-dismissible'.format(alert_cl", 10, 27), 531: (u'non_compliant', 11, 22), 579: (u'python: alert_class', 13, 31), 1170: (u"python: ', '.join(non_compliant)", 27, 27), 1283: (u'python: editable', 29, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047122256 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140168047816528 = {u'aria-hidden': u'true', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168026312656 = {u'class': u'description', }
_static_140168026261328 = {u'tal': '', u'condition': u'python: editable', }
_static_140168257770128 = {}
_static_140168026312016 = {u'id': u'portal-alert', }
_static_140168026261008 = {u'class': u'title', }
_static_140168047123792 = {u'class': u'python: alert_class', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047359120
            __attrs_140168047359120 = _static_140168257770128

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 41
            try:
                __zt_tmp = __attrs_140168047359120
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.available()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168026311376 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b696acd50> name=None at 7f7b696acf90> -> __attrs_140168026311696
                __attrs_140168026311696 = _static_140168026312016
                __backup_sample_140168047345232 = get('sample', __marker)

                # <Value u'python:view.context' (6:26)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.context', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['sample'] = __value
                __backup_non_compliant_140168047358800 = get('non_compliant', __marker)

                # <Value u'python:view.get_non_compliant_analyses()' (7:32)> -> __value
                __token = 204
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.get_non_compliant_analyses()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['non_compliant'] = __value
                __backup_editable_140168016770448 = get('editable', __marker)

                # <Value u'python:view.is_specification_editable()' (8:26)> -> __value
                __token = 273
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.is_specification_editable()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['editable'] = __value
                __backup_alert_class_140168037403216 = get('alert_class', __marker)

                # <Value u"python: editable and 'alert-warning' or 'alert-info'" (9:28)> -> __value
                __token = 344
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" editable and 'alert-warning' or 'alert-info'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['alert_class'] = __value
                __backup_alert_class_140168037439312 = get('alert_class', __marker)

                # <Value u"python: 'portlet-alert-item alert {} alert-dismissible'.format(alert_class)" (10:27)> -> __value
                __token = 428
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" 'portlet-alert-item alert {} alert-dismissible'.format(alert_class)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['alert_class'] = __value

                # <Value u'non_compliant' (11:22)> -> __condition
                __token = 531
                try:
                    __zt_tmp = __attrs_140168026311696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'non_compliant', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="portal-alert">\n\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa85d50> name=None at 7f7b6aa85510> -> __attrs_140168047122000
                    __attrs_140168047122000 = _static_140168047123792

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047123152
                    __default_140168047123152 = _DEFAULT_MARKER

                    # <Substitution u'python: alert_class' (13:31)> -> __attr_class
                    __token = 579
                    try:
                        __zt_tmp = __attrs_140168047122000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140168208991440('python', u' alert_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa85750> name=None at 7f7b6aa85d10> -> __attrs_140168047813840
                    __attrs_140168047813840 = _static_140168047122256

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ab2ef50> name=None at 7f7b6ab2eed0> -> __attrs_140168047814544
                    __attrs_140168047814544 = _static_140168047816528

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b696a0610> name=None at 7f7b6aa85550> -> __attrs_140168026259984
                    __attrs_140168026259984 = _static_140168026261008

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="title">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026312336
                    __attrs_140168026312336 = _static_140168257770128

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140168026259920 = []
                    __append_140168026259920 = __stream_140168026259920.append
                    __append_140168026259920(u'\n          Ranges for some analyses are different from the Specification\n        ')
                    __msgid_140168026259920 = __re_whitespace(''.join(__stream_140168026259920)).strip()
                    if __msgid_140168026259920:
                        __append(translate(__msgid_140168026259920, mapping=None, default=__msgid_140168026259920, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n      </p>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b696acfd0> name=None at 7f7b696acd90> -> __attrs_140168026309712
                    __attrs_140168026309712 = _static_140168026312656

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="description">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026259728
                    __attrs_140168026259728 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140168026259664 = []
                    __append_140168026259664 = __stream_140168026259664.append
                    __append_140168026259664(u'\n          The ranges for the following analyses have been manually changed and\n          they are no longer compliant with the ranges of the Specification:\n        ')
                    __msgid_140168026259664 = __re_whitespace(''.join(__stream_140168026259664)).strip()
                    if __msgid_140168026259664:
                        __append(translate(__msgid_140168026259664, mapping=None, default=__msgid_140168026259664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026260176
                    __attrs_140168026260176 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026260816
                    __default_140168026260816 = _DEFAULT_MARKER

                    # <Value u"python: ', '.join(non_compliant)" (27:27)> -> __cache_140168026260240
                    __token = 1170
                    try:
                        __zt_tmp = __attrs_140168026260176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168026260240 = _static_140168208991440('python', u" ', '.join(non_compliant)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python: ', '.join(non_compliant)" (27:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696a0d50> -> __condition
                    __expression = __cache_140168026260240

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168026260240
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b696a0750> name=None at 7f7b696a0790> -> __attrs_140168046904144
                    __attrs_140168046904144 = _static_140168026261328

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<br tal condition="python: editable"/>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046904272
                    __attrs_140168046904272 = _static_140168257770128

                    # <Value u'python: editable' (29:29)> -> __condition
                    __token = 1283
                    try:
                        __zt_tmp = __attrs_140168046904272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u' editable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140168046906832 = []
                        __append_140168046906832 = __stream_140168046906832.append
                        __append_140168046906832(u'\n          Re-assign the Specification if you want to restore analysis ranges.\n        ')
                        __msgid_140168046906832 = __re_whitespace(''.join(__stream_140168046906832)).strip()
                        if __msgid_140168046906832:
                            __append(translate(__msgid_140168046906832, mapping=None, default=__msgid_140168046906832, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>')
                    __append(u'\n      </p>\n    </div>\n  </div>')
                if (__backup_alert_class_140168037439312 is __marker):
                    del econtext['alert_class']
                else:
                    econtext['alert_class'] = __backup_alert_class_140168037439312
                if (__backup_alert_class_140168037403216 is __marker):
                    del econtext['alert_class']
                else:
                    econtext['alert_class'] = __backup_alert_class_140168037403216
                if (__backup_editable_140168016770448 is __marker):
                    del econtext['editable']
                else:
                    econtext['editable'] = __backup_editable_140168016770448
                if (__backup_non_compliant_140168047358800 is __marker):
                    del econtext['non_compliant']
                else:
                    econtext['non_compliant'] = __backup_non_compliant_140168047358800
                if (__backup_sample_140168047345232 is __marker):
                    del econtext['sample']
                else:
                    econtext['sample'] = __backup_sample_140168047345232
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140168026311376
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }