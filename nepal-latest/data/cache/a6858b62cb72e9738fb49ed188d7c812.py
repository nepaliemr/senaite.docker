# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/remarks.pt'

__tokens = {48: (u'python:view.available()', 2, 20), 156: (u'view/icon_name|nothing', 6, 23), 203: (u' view/title|nothin', 7, 23), 247: (u'l context/@@plone_portal_state/port', 8, 23), 307: (u'title', 9, 21), 339: (u'icon|nothing', 10, 24), 382: (u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', 11, 29), 483: (u'title', 12, 41), 536: (u'nocall: context/portal_membership/checkPermission', 15, 35), 610: (u" python:'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view", 16, 23), 733: (u"w python:context.restrictedTraverse('@@senaite_view", 17, 30), 809: (u'st nocall:senaite_view/t', 18, 21), 859: (u"eld python:context.Schema()['Remar", 19, 21), 920: (u'rors pyth', 20, 21), 967: (u"python:context.widget('Remarks', mode=mode)", 21, 29), 967: (u"python:context.widget('Remarks', mode=mode)", 21, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168036706512 = u"python:context.widget('Remarks', mode=mode)"
_static_140168208992144 = __C2ZContextWrapper
_static_140168036704720 = {u'src': u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', }
_static_140168257770128 = {}
_static_140168047220176 = {u'class': u'remarks-widget', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6aa9d5d0> name=None at 7f7b6aa9d090> -> __attrs_140168047222352
            __attrs_140168047222352 = _static_140168047220176

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 48
            try:
                __zt_tmp = __attrs_140168047222352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.available()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047221456 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="remarks-widget">\n\n  <!-- title and icon -->\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168036706960
                __attrs_140168036706960 = _static_140168257770128
                __backup_icon_140168016931728 = get('icon', __marker)

                # <Value u'view/icon_name|nothing' (6:23)> -> __value
                __token = 156
                try:
                    __zt_tmp = __attrs_140168036706960
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/icon_name|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['icon'] = __value
                __backup_title_140168037143504 = get('title', __marker)

                # <Value u'view/title|nothing' (7:23)> -> __value
                __token = 203
                try:
                    __zt_tmp = __attrs_140168036706960
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['title'] = __value
                __backup_portal_140168037234512 = get('portal', __marker)

                # <Value u'context/@@plone_portal_state/portal' (8:23)> -> __value
                __token = 247
                try:
                    __zt_tmp = __attrs_140168036706960
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['portal'] = __value

                # <Value u'title' (9:21)> -> __condition
                __token = 307
                try:
                    __zt_tmp = __attrs_140168036706960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a0961d0> name=None at 7f7b6a096810> -> __attrs_140168036705744
                    __attrs_140168036705744 = _static_140168036704720

                    # <Value u'icon|nothing' (10:24)> -> __condition
                    __token = 339
                    try:
                        __zt_tmp = __attrs_140168036705744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'icon|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036705360
                        __default_140168036705360 = _DEFAULT_MARKER

                        # <Substitution u'string:${portal/absolute_url}/senaite_theme/icon/${icon}' (11:29)> -> __attr_src
                        __token = 382
                        try:
                            __zt_tmp = __attrs_140168036705744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140168208991440('string', u'${portal/absolute_url}/senaite_theme/icon/${icon}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))
                        __append(u'/>')
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015870736
                    __attrs_140168015870736 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168036705104
                    __default_140168036705104 = _DEFAULT_MARKER

                    # <Value u'title' (12:41)> -> __cache_140168036705424
                    __token = 483
                    try:
                        __zt_tmp = __attrs_140168015870736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168036705424 = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'title' (12:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a096b10> -> __condition
                    __expression = __cache_140168036705424

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168036705424
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n  </h3>')
                if (__backup_portal_140168037234512 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_140168037234512
                if (__backup_title_140168037143504 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140168037143504
                if (__backup_icon_140168016931728 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140168016931728
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037142160
                __attrs_140168037142160 = _static_140168257770128
                __backup_checkPermission_140168026367632 = get('checkPermission', __marker)

                # <Value u'nocall: context/portal_membership/checkPermission' (15:35)> -> __value
                __token = 536
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('nocall', u' context/portal_membership/checkPermission', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['checkPermission'] = __value
                __backup_mode_140168037228880 = get('mode', __marker)

                # <Value u"python:'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view'" (16:23)> -> __value
                __token = 610
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['mode'] = __value
                __backup_senaite_view_140168015753296 = get('senaite_view', __marker)

                # <Value u"python:context.restrictedTraverse('@@senaite_view')" (17:30)> -> __value
                __token = 733
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"context.restrictedTraverse('@@senaite_view')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['senaite_view'] = __value
                __backup_test_140168046974544 = get('test', __marker)

                # <Value u'nocall:senaite_view/test' (18:21)> -> __value
                __token = 809
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('nocall', u'senaite_view/test', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['test'] = __value
                __backup_field_140168047768528 = get('field', __marker)

                # <Value u"python:context.Schema()['Remarks']" (19:21)> -> __value
                __token = 859
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"context.Schema()['Remarks']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['field'] = __value
                __backup_errors_140168015755856 = get('errors', __marker)

                # <Value u'python:{}' (20:21)> -> __value
                __token = 920
                try:
                    __zt_tmp = __attrs_140168037142160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'{}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['errors'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016890576
                __attrs_140168016890576 = _static_140168257770128
                __backup_macroname_140168056779312 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6a0968d0> name=None at 7f7b6a096bd0> -> __value
                __value = _static_140168036706512
                econtext['macroname'] = __value

                # <Value u"python:context.widget('Remarks', mode=mode)" (21:29)> -> __macro
                __token = 967
                try:
                    __zt_tmp = __attrs_140168016890576
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('python', u"context.widget('Remarks', mode=mode)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 967
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168056779312 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168056779312
                __append(u'\n  </div>')
                if (__backup_errors_140168015755856 is __marker):
                    del econtext['errors']
                else:
                    econtext['errors'] = __backup_errors_140168015755856
                if (__backup_field_140168047768528 is __marker):
                    del econtext['field']
                else:
                    econtext['field'] = __backup_field_140168047768528
                if (__backup_test_140168046974544 is __marker):
                    del econtext['test']
                else:
                    econtext['test'] = __backup_test_140168046974544
                if (__backup_senaite_view_140168015753296 is __marker):
                    del econtext['senaite_view']
                else:
                    econtext['senaite_view'] = __backup_senaite_view_140168015753296
                if (__backup_mode_140168037228880 is __marker):
                    del econtext['mode']
                else:
                    econtext['mode'] = __backup_mode_140168037228880
                if (__backup_checkPermission_140168026367632 is __marker):
                    del econtext['checkPermission']
                else:
                    econtext['checkPermission'] = __backup_checkPermission_140168026367632
                __append(u'\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140168047221456
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }