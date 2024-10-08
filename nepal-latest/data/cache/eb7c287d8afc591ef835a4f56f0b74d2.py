# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/resultsranges_out_of_date_viewlet.pt'

__tokens = {41: (u'python:view.available()', 2, 20), 151: (u'python:view.context', 6, 26), 199: (u' python:view.is_specification_editable(', 7, 27), 270: (u"s python: editable and 'alert-warning' or 'alert-inf", 8, 29), 354: (u"ss python: 'portlet-alert-item alert {} alert-dismissible'.format(alert_cla", 9, 28), 461: (u'ate python:view.is_results_ranges_out_of_da', 10, 27), 532: (u'out_of_date', 11, 22), 578: (u'python: alert_class', 13, 31), 963: (u'python: editable', 23, 29), 1370: (u'python: sample.getSpecification()', 31, 28), 1437: (u'python:spec.absolute_url()', 32, 32), 1489: (u'python:spec.Title()', 33, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047410000 = {u'aria-hidden': u'true', }
_static_140168047837712 = {u'href': u'python:spec.absolute_url()', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047489424 = {u'class': u'python: alert_class', }
_static_140168257770128 = {}
_static_140168046976080 = {u'tal': '', u'condition': u'python: editable', }
_static_140168047410896 = {u'class': u'title', }
_static_140168047491216 = {u'id': u'portal-alert', }
_static_140168047410128 = {u'class': u'description', }
_static_140168047160400 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047490896
            __attrs_140168047490896 = _static_140168257770128

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 41
            try:
                __zt_tmp = __attrs_140168047490896
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.available()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047491536 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aadf890> name=None at 7f7b6aadf1d0> -> __attrs_140168047491024
                __attrs_140168047491024 = _static_140168047491216
                __backup_sample_140168037402064 = get('sample', __marker)

                # <Value u'python:view.context' (6:26)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.context', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['sample'] = __value
                __backup_editable_140168026343952 = get('editable', __marker)

                # <Value u'python:view.is_specification_editable()' (7:27)> -> __value
                __token = 199
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.is_specification_editable()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['editable'] = __value
                __backup_alert_class_140168026339408 = get('alert_class', __marker)

                # <Value u"python: editable and 'alert-warning' or 'alert-info'" (8:29)> -> __value
                __token = 270
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" editable and 'alert-warning' or 'alert-info'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['alert_class'] = __value
                __backup_alert_class_140168037403216 = get('alert_class', __marker)

                # <Value u"python: 'portlet-alert-item alert {} alert-dismissible'.format(alert_class)" (9:28)> -> __value
                __token = 354
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u" 'portlet-alert-item alert {} alert-dismissible'.format(alert_class)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['alert_class'] = __value
                __backup_out_of_date_140168047001360 = get('out_of_date', __marker)

                # <Value u'python:view.is_results_ranges_out_of_date()' (10:27)> -> __value
                __token = 461
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'view.is_results_ranges_out_of_date()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['out_of_date'] = __value

                # <Value u'out_of_date' (11:22)> -> __condition
                __token = 532
                try:
                    __zt_tmp = __attrs_140168047491024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'out_of_date', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="portal-alert">\n\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aadf190> name=None at 7f7b6aadfe10> -> __attrs_140168047158864
                    __attrs_140168047158864 = _static_140168047489424

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037498064
                    __default_140168037498064 = _DEFAULT_MARKER

                    # <Substitution u'python: alert_class' (13:31)> -> __attr_class
                    __token = 578
                    try:
                        __zt_tmp = __attrs_140168047158864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140168208991440('python', u' alert_class', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa8ec50> name=None at 7f7b6aa8eed0> -> __attrs_140168047157328
                    __attrs_140168047157328 = _static_140168047160400

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aacbb50> name=None at 7f7b6aacb410> -> __attrs_140168047411152
                    __attrs_140168047411152 = _static_140168047410000

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aacbed0> name=None at 7f7b6aacb790> -> __attrs_140168047410064
                    __attrs_140168047410064 = _static_140168047410896

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="title">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047409744
                    __attrs_140168047409744 = _static_140168257770128

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140168047408784 = []
                    __append_140168047408784 = __stream_140168047408784.append
                    __append_140168047408784(u'\n          Specification ranges have changed since they were assigned\n        ')
                    __msgid_140168047408784 = __re_whitespace(''.join(__stream_140168047408784)).strip()
                    if __msgid_140168047408784:
                        __append(translate(__msgid_140168047408784, mapping=None, default=__msgid_140168047408784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n      </p>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aacbbd0> name=None at 7f7b6aacb550> -> __attrs_140168025871312
                    __attrs_140168025871312 = _static_140168047410128

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="description">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046975504
                    __attrs_140168046975504 = _static_140168257770128

                    # <Value u'python: editable' (23:29)> -> __condition
                    __token = 963
                    try:
                        __zt_tmp = __attrs_140168046975504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u' editable', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140168046973392 = []
                        __append_140168046973392 = __stream_140168046973392.append
                        __append_140168046973392(u"\n          New ranges won't be applied to neither new nor current analyses.\n          Re-assign the Specification if you want to apply latest changes.\n        ")
                        __msgid_140168046973392 = __re_whitespace(''.join(__stream_140168046973392)).strip()
                        if __msgid_140168046973392:
                            __append(translate(__msgid_140168046973392, mapping=None, default=__msgid_140168046973392, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa61c50> name=None at 7f7b6aa61bd0> -> __attrs_140168046976336
                    __attrs_140168046976336 = _static_140168046976080

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<br tal condition="python: editable"/>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046973648
                    __attrs_140168046973648 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140168046975312 = []
                    __append_140168046975312 = __stream_140168046975312.append
                    __append_140168046975312(u"\n          Visit the Specification's changes history for additional information:\n        ")
                    __msgid_140168046975312 = __re_whitespace(''.join(__stream_140168046975312)).strip()
                    if __msgid_140168046975312:
                        __append(translate(__msgid_140168046975312, mapping=None, default=__msgid_140168046975312, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ab34210> name=None at 7f7b6ab34350> -> __attrs_140168046892048
                    __attrs_140168046892048 = _static_140168047837712
                    __backup_spec_140168037439248 = get('spec', __marker)

                    # <Value u'python: sample.getSpecification()' (31:28)> -> __value
                    __token = 1370
                    try:
                        __zt_tmp = __attrs_140168046892048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u' sample.getSpecification()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['spec'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047837904
                    __default_140168047837904 = _DEFAULT_MARKER

                    # <Substitution u'python:spec.absolute_url()' (32:32)> -> __attr_href
                    __token = 1437
                    try:
                        __zt_tmp = __attrs_140168046892048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('python', u'spec.absolute_url()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047837264
                    __default_140168047837264 = _DEFAULT_MARKER

                    # <Value u'python:spec.Title()' (33:24)> -> __cache_140168046974736
                    __token = 1489
                    try:
                        __zt_tmp = __attrs_140168046892048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168046974736 = _static_140168208991440('python', u'spec.Title()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:spec.Title()' (33:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa61f10> -> __condition
                    __expression = __cache_140168046974736

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168046974736
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>')
                    if (__backup_spec_140168037439248 is __marker):
                        del econtext['spec']
                    else:
                        econtext['spec'] = __backup_spec_140168037439248
                    __append(u'\n      </p>\n    </div>\n  </div>')
                if (__backup_out_of_date_140168047001360 is __marker):
                    del econtext['out_of_date']
                else:
                    econtext['out_of_date'] = __backup_out_of_date_140168047001360
                if (__backup_alert_class_140168037403216 is __marker):
                    del econtext['alert_class']
                else:
                    econtext['alert_class'] = __backup_alert_class_140168037403216
                if (__backup_alert_class_140168026339408 is __marker):
                    del econtext['alert_class']
                else:
                    econtext['alert_class'] = __backup_alert_class_140168026339408
                if (__backup_editable_140168026343952 is __marker):
                    del econtext['editable']
                else:
                    econtext['editable'] = __backup_editable_140168026343952
                if (__backup_sample_140168037402064 is __marker):
                    del econtext['sample']
                else:
                    econtext['sample'] = __backup_sample_140168037402064
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140168047491536
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }