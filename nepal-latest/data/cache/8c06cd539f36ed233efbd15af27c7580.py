# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/dexterity/templates/macros.pt'

__tokens = {6859: (u'view/widgets/values', 146, 48), 367: (u'view/label | nothing', 11, 27), 402: (u'view/label', 11, 62), 6465: (u'show_default_label|nothing', 137, 45), 6529: (u' has_groups|nothin', 138, 36), 7381: (u'has_groups', 157, 64), 7362: (u'groups', 157, 45), 7524: (u'nocall:context/@@plone/normalizeString', 160, 51), 7613: (u' group/labe', 161, 49), 7674: (u"e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 162, 47), 7824: (u'me python:normalizeString(fieldset_na', 163, 46), 7909: (u'string:${fieldset_name}', 164, 42), 7986: (u' fieldset_nam', 165, 52), 8097: (u'group/description|nothing', 168, 52), 8161: (u'group_description', 169, 37), 8225: (u'group_description', 170, 45), 8390: (u'group/widgets/errors', 175, 50), 8458: (u'python:False', 176, 46), 8521: (u'errors', 177, 49), 8633: (u'not:nocall:error/widget', 179, 42), 8708: (u'error/render', 180, 50), 8838: (u'nocall:group', 184, 44), 8900: (u'context/@@ploneform-macros/widget_rendering', 185, 46), 8900: (u'context/@@ploneform-macros/widget_rendering', 185, 46), 9329: (u'view/actions/values|nothing', 199, 55), 9401: (u'view/actions/values', 200, 42), 9485: (u'action/render', 201, 62), 7062: (u'widget/@@ploneform-render-widget', 149, 61), 562: (u'view/status', 17, 35), 612: (u" python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None", 18, 37), 706: (u'status', 18, 131), 778: (u'has_error', 19, 63), 925: (u'status', 23, 29), 1008: (u'not:has_error', 25, 56), 1159: (u'status', 29, 29), 1282: (u'view/widgets/errors', 34, 35), 1314: (u'errors', 34, 67), 1358: (u'errors', 35, 35), 1456: (u'not:nocall:error/widget', 37, 32), 1521: (u'error/render', 38, 40), 1696: (u'view/groups|nothing', 45, 35), 1748: (u'python:bool(groups)', 46, 31), 1803: (u'groups', 47, 34), 1852: (u'group/widgets/errors', 48, 40), 1909: (u'errors', 49, 35), 1955: (u'errors', 50, 38), 2052: (u'not:nocall:error/widget', 52, 31), 2116: (u'error/render', 53, 39), 2348: (u'view/description | nothing', 60, 37), 2404: (u'description', 61, 28), 2453: (u'description|default', 62, 36), 2787: (u'view/groups | nothing', 70, 33), 2845: (u' view/form_name | nothin', 71, 35), 2907: (u's view/css_class | strin', 72, 35), 2981: (u'el view/default_fieldset_label | form_n', 73, 46), 3067: (u'ing view/enable_form_tabbing | python:', 74, 42), 3157: (u'tion view/enable_unload_protection|python', 75, 46), 3243: (u"ction python:enable_unload_protection and 'pat-formunload", 76, 38), 3338: (u'groups python:bool(', 77, 30), 3397: (u"tabbing python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autoto", 78, 31), 3528: (u'lt_label python:has_groups and default_fieldset_label and len(view', 79, 36), 3640: (u'_name_raw python:view.__name__ or request.getURL().spli', 80, 35), 3737: (u"_view_name python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('", 81, 30), 4013: (u"s python:'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_nam", 85, 34), 3899: (u'view/action|request/getURL', 83, 37), 4233: (u'hod view/method|string:', 87, 33), 3964: (u' view/enctyp', 84, 37), 4188: (u'id view', 86, 30), 4427: (u'python: has_groups and enable_form_tabbing', 93, 29), 4598: (u'view/widgets/errors', 97, 39), 4713: (u"python:has_errors and 'nav-link active text-danger' or 'nav-link active'", 99, 39), 4650: (u'default_fieldset_label', 98, 30), 5048: (u'groups', 109, 34), 5139: (u'nocall:context/@@plone/normalizeString', 110, 45), 5222: (u' group/labe', 111, 43), 5277: (u"e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 112, 41), 5421: (u'me python:normalizeString(fieldset_na', 113, 40), 5499: (u'ors group/widgets/errors|not', 114, 36), 5569: (u'string:${fieldset_name}-tab', 115, 36), 5635: (u' string:#${fieldset_name', 116, 37), 5699: (u"s python:has_errors and 'nav-link text-danger' or 'nav-lin", 117, 37), 5791: (u'fieldset_label', 118, 30), 6115: (u'request/fieldset | python:None', 130, 48), 6181: (u'python:has_groups and enable_form_tabbing and current_fieldset is not None', 131, 34), 6298: (u'current_fieldset', 132, 41), 9650: (u'view/enableCSRFProtection|nothing', 207, 36), 9729: (u'context/@@authenticator/authenticator', 208, 44)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140240907633936 = {u'class': u'form', }
_static_140240907587536 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140241133802128 = {}
_static_140240907367952 = {u'role': u'tablist', u'class': u'nav nav-tabs', }
_static_140240907381392 = {u'data-toggle': u'tab', u'href': u'string:#${fieldset_name}', u'role': u'tab', u'id': u'string:${fieldset_name}-tab', u'class': u"python:has_errors and 'nav-link text-danger' or 'nav-link'", }
_static_140241087907024 = __compile_zt_expr
_static_140241087907728 = __C2ZContextWrapper
_static_140240907392848 = {u'class': u'tab-content', }
_static_140240907612880 = {u'class': u'field error alert alert-warning', }
_static_140240907598352 = {u'name': u'edit_form', u'id': u'view/id', u'data-pat-autotoc': u'levels: legend; section: fieldset; className: autotabs', u'method': u'post', u'action': u'.', u'class': u'rowlike enableUnloadProtection', u'enctype': u'view/enctype', }
_static_140240907596304 = {u'class': u'field error alert alert-warning', }
_static_140240906894928 = {u'type': u'submit', }
_static_140240907401616 = {u'type': u'hidden', u'name': u'fieldset', u'value': u'current_fieldset', }
_static_140240907369872 = {u'role': u'presentation', u'class': u'nav-item', }
_static_140240906885968 = {u'class': u'field error fieldErrorBox', }
_static_140240906892688 = {u'class': u'formControls', }
_static_140240907394192 = {u'role': u'tabpanel', u'class': u'tab-pane active', u'id': u'default', }
_static_140240906891920 = u'widget_rendering'
_static_140240906918352 = {u'data-fieldset': u'fieldset_name', u'role': u'tabpanel', u'class': u'tab-pane', u'id': u'string:${fieldset_name}', }
_static_140240907650768 = {u'role': u'alert', u'class': u'portalMessage alert error', }
_static_140240907621008 = {u'role': u'status', u'class': u'portalMessage info', }
_static_140240907599184 = {u'class': u'discreet text-secondary', }
_static_140240907319056 = {u'data-toggle': u'tab', u'href': u'#default', u'role': u'tab', u'id': u'default-tab', u'class': u"python:has_errors and 'nav-link active text-danger' or 'nav-link active'", }
_static_140240907378896 = {u'role': u'presentation', u'class': u'nav-item', }

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

    def render_widget_rendering(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_field = econtext[u'__slot_field'].pop()
        except:
            __slot_field = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906917136
            __attrs_140240906917136 = _static_140241133802128
            __append(u'\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906917968
            __attrs_140240906917968 = _static_140241133802128
            __backup_widget_140240916619920 = get('widget', __marker)

            # <Value u'view/widgets/values' (146:48)> -> __iterator
            __token = 6859
            try:
                __zt_tmp = __attrs_140240906917968
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/widgets/values', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240906918160, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n                      ')
                if (__slot_field is None):

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906918800
                    __attrs_140240906918800 = _static_140241133802128
                    __append(u'\n                        ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append(u'\n                      ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append(u'\n                    ')
                ____index_140240906918160 -= 1
                if (____index_140240906918160 > 0):
                    __append('')
            if (__backup_widget_140240916619920 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240916619920
            __append(u'\n                  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_title = econtext[u'__slot_title'].pop()
        except:
            __slot_title = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8c617b8510> name=None at 7f8c617b82d0> -> __attrs_140240907634064
            __attrs_140240907634064 = _static_140240907633936

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form">\n\n      ')
            if (__slot_title is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907634640
                __attrs_140240907634640 = _static_140241133802128
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907636560
                __attrs_140240907636560 = _static_140241133802128

                # <Value u'view/label | nothing' (11:27)> -> __condition
                __token = 367
                try:
                    __zt_tmp = __attrs_140240907636560
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'view/label | nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907636240
                    __default_140240907636240 = _DEFAULT_MARKER

                    # <Value u'view/label' (11:62)> -> __cache_140240907635152
                    __token = 402
                    try:
                        __zt_tmp = __attrs_140240907636560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907635152 = _static_140241087907024('path', u'view/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/label' (11:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617b8a10> -> __condition
                    __expression = __cache_140240907635152

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240907635152
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</h3>')
                __append(u'\n      ')
            else:
                __slot_title(__stream, econtext.copy(), rcontext)
            __append(u'\n\n      ')
            __token = None
            render_titlelessform(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_fields(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907391632
            __attrs_140240907391632 = _static_140241133802128
            __backup_show_default_label_140240916732048 = get('show_default_label', __marker)

            # <Value u'show_default_label|nothing' (137:45)> -> __value
            __token = 6465
            try:
                __zt_tmp = __attrs_140240907391632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'show_default_label|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_has_groups_140240907728272 = get('has_groups', __marker)

            # <Value u'has_groups|nothing' (138:36)> -> __value
            __token = 6529
            try:
                __zt_tmp = __attrs_140240907391632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'has_groups|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __append(u'\n\n              <!-- tab content -->\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6177d750> name=None at 7f8c6177d6d0> -> __attrs_140240907393424
            __attrs_140240907393424 = _static_140240907392848

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-content">\n\n                <!-- Primary fieldsets -->\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c6177dc90> name=None at 7f8c6177dc50> -> __attrs_140240906916368
            __attrs_140240906916368 = _static_140240907394192

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-pane active" id="default" role="tabpanel">\n                  ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n                </div>\n\n                <!-- Secondary fieldsets -->\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906916624
            __attrs_140240906916624 = _static_140241133802128

            # <Value u'has_groups' (157:64)> -> __condition
            __token = 7381
            try:
                __zt_tmp = __attrs_140240906916624
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'has_groups', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __backup_group_140240916638416 = get('group', __marker)

                # <Value u'groups' (157:45)> -> __iterator
                __token = 7362
                try:
                    __zt_tmp = __attrs_140240906916624
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'groups', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240906917904, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8c617099d0> name=None at 7f8c61709e50> -> __attrs_140240906889552
                    __attrs_140240906889552 = _static_140240906918352
                    __backup_normalizeString_140240916621392 = get('normalizeString', __marker)

                    # <Value u'nocall:context/@@plone/normalizeString' (160:51)> -> __value
                    __token = 7524
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('nocall', u'context/@@plone/normalizeString', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_140240917792464 = get('fieldset_label', __marker)

                    # <Value u'group/label' (161:49)> -> __value
                    __token = 7613
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_140240917016976 = get('fieldset_name', __marker)

                    # <Value u"python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (162:47)> -> __value
                    __token = 7674
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('python', u"getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_140240916622416 = get('fieldset_name', __marker)

                    # <Value u'python:normalizeString(fieldset_name)' (163:46)> -> __value
                    __token = 7824
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('python', u'normalizeString(fieldset_name)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="tab-pane" role="tabpanel"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906888912
                    __default_140240906888912 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldset_name}' (164:42)> -> __attr_id
                    __token = 7909
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('string', u'${fieldset_name}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906889232
                    __default_140240906889232 = _DEFAULT_MARKER

                    # <Substitution u'fieldset_name' (165:52)> -> __attr_data_fieldset
                    __token = 7986
                    try:
                        __zt_tmp = __attrs_140240906889552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldset = _static_140241087907024('path', u'fieldset_name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_data_fieldset = __quote(__attr_data_fieldset, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldset is not None):
                        __append((u' data-fieldset="%s"' % __attr_data_fieldset))
                    __append(u'>\n\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906883472
                    __attrs_140240906883472 = _static_140241133802128
                    __backup_group_description_140240916621840 = get('group_description', __marker)

                    # <Value u'group/description|nothing' (168:52)> -> __value
                    __token = 8097
                    try:
                        __zt_tmp = __attrs_140240906883472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/description|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['group_description'] = __value

                    # <Value u'group_description' (169:37)> -> __condition
                    __token = 8161
                    try:
                        __zt_tmp = __attrs_140240906883472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'group_description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906891216
                        __default_140240906891216 = _DEFAULT_MARKER

                        # <Value u'group_description' (170:45)> -> __cache_140240906890896
                        __token = 8225
                        try:
                            __zt_tmp = __attrs_140240906883472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240906890896 = _static_140241087907024('path', u'group_description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'group_description' (170:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61702f10> -> __condition
                        __expression = __cache_140240906890896

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                      Description\n                    ')
                        else:
                            __content = __cache_140240906890896
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</p>')
                    if (__backup_group_description_140240916621840 is __marker):
                        del econtext['group_description']
                    else:
                        econtext['group_description'] = __backup_group_description_140240916621840
                    __append(u'\n\n                    <!-- Error -->\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906884496
                    __attrs_140240906884496 = _static_140241133802128
                    __backup_errors_140240917017296 = get('errors', __marker)

                    # <Value u'group/widgets/errors' (175:50)> -> __value
                    __token = 8390
                    try:
                        __zt_tmp = __attrs_140240906884496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/widgets/errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value u'python:False' (176:46)> -> __condition
                    __token = 8458
                    try:
                        __zt_tmp = __attrs_140240906884496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u'False', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140240917019856 = get('error', __marker)

                        # <Value u'errors' (177:49)> -> __iterator
                        __token = 8521
                        try:
                            __zt_tmp = __attrs_140240906884496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140241087907024('path', u'errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        (__iterator, ____index_140240906884688, ) = getitem('repeat')(u'error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append(u'\n                      ')

                            # <Static value=<_ast.Dict object at 0x7f8c61701b50> name=None at 7f8c61701b10> -> __attrs_140240906886608
                            __attrs_140240906886608 = _static_140240906885968

                            # <Value u'not:nocall:error/widget' (179:42)> -> __condition
                            __token = 8633
                            try:
                                __zt_tmp = __attrs_140240906886608
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140241087907024('not', u'nocall:error/widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="field error fieldErrorBox">')

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906885776
                                __default_140240906885776 = _DEFAULT_MARKER

                                # <Value u'error/render' (180:50)> -> __cache_140240906885328
                                __token = 8708
                                try:
                                    __zt_tmp = __attrs_140240906886608
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140240906885328 = _static_140241087907024('path', u'error/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                                # <BinOp left=<Value u'error/render' (180:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617019d0> -> __condition
                                __expression = __cache_140240906885328

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140240906885328
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</div>')
                            __append(u'\n                    ')
                            ____index_140240906884688 -= 1
                            if (____index_140240906884688 > 0):
                                __append('')
                        if (__backup_error_140240917019856 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140240917019856
                    if (__backup_errors_140240917017296 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140240917017296
                    __append(u'\n\n                    <!-- Widget -->\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906886928
                    __attrs_140240906886928 = _static_140241133802128
                    __backup_view_140240916961680 = get('view', __marker)

                    # <Value u'nocall:group' (184:44)> -> __value
                    __token = 8838
                    try:
                        __zt_tmp = __attrs_140240906886928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('nocall', u'group', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['view'] = __value
                    __append(u'\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906892176
                    __attrs_140240906892176 = _static_140241133802128
                    __backup_macroname_140240933512368 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f8c61703290> name=None at 7f8c617032d0> -> __value
                    __value = _static_140240906891920
                    econtext['macroname'] = __value

                    # <Value u'context/@@ploneform-macros/widget_rendering' (185:46)> -> __macro
                    __token = 8900
                    try:
                        __zt_tmp = __attrs_140240906892176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140241087907024('path', u'context/@@ploneform-macros/widget_rendering', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __token = 8900
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140240933512368 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140240933512368
                    __append(u'\n                    ')
                    if (__backup_view_140240916961680 is __marker):
                        del econtext['view']
                    else:
                        econtext['view'] = __backup_view_140240916961680
                    __append(u'\n\n                  </div>')
                    if (__backup_fieldset_name_140240916622416 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140240916622416
                    if (__backup_fieldset_name_140240917016976 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140240917016976
                    if (__backup_fieldset_label_140240917792464 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_140240917792464
                    if (__backup_normalizeString_140240916621392 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140240916621392
                    __append(u'\n                ')
                    ____index_140240906917904 -= 1
                    if (____index_140240906917904 > 0):
                        __append('')
                if (__backup_group_140240916638416 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140240916638416
            __append(u'\n              </div>\n\n            ')
            if (__backup_has_groups_140240907728272 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140240907728272
            if (__backup_show_default_label_140240916732048 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140240916732048
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_actions(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906883728
            __attrs_140240906883728 = _static_140241133802128
            __append(u'\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c61703590> name=None at 7f8c61703550> -> __attrs_140240906893264
            __attrs_140240906893264 = _static_140240906892688

            # <Value u'view/actions/values|nothing' (199:55)> -> __condition
            __token = 9329
            try:
                __zt_tmp = __attrs_140240906893264
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/actions/values|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="formControls">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906894160
                __attrs_140240906894160 = _static_140241133802128
                __backup_action_140240916622032 = get('action', __marker)

                # <Value u'view/actions/values' (200:42)> -> __iterator
                __token = 9401
                try:
                    __zt_tmp = __attrs_140240906894160
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/actions/values', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240906894352, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8c61703e50> name=None at 7f8c61703e10> -> __attrs_140240906904208
                    __attrs_140240906904208 = _static_140240906894928

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906904080
                    __default_140240906904080 = _DEFAULT_MARKER

                    # <Value u'action/render' (201:62)> -> __cache_140240906903696
                    __token = 9485
                    try:
                        __zt_tmp = __attrs_140240906904208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906903696 = _static_140241087907024('path', u'action/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/render' (201:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61706150> -> __condition
                    __expression = __cache_140240906903696

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="submit" />')
                    else:
                        __content = __cache_140240906903696
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                ')
                    ____index_140240906894352 -= 1
                    if (____index_140240906894352 > 0):
                        __append('')
                if (__backup_action_140240916622032 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140240916622032
                __append(u'\n              </div>')
            __append(u'\n            ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_field(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906919632
            __attrs_140240906919632 = _static_140241133802128
            __append(u'\n                          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906888144
            __attrs_140240906888144 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906888016
            __default_140240906888016 = _DEFAULT_MARKER

            # <Value u'widget/@@ploneform-render-widget' (149:61)> -> __cache_140240906887696
            __token = 7062
            try:
                __zt_tmp = __attrs_140240906888144
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240906887696 = _static_140241087907024('path', u'widget/@@ploneform-render-widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'widget/@@ploneform-render-widget' (149:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61702290> -> __condition
            __expression = __cache_140240906887696

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240906887696
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                        ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_titlelessform(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_formtop = econtext[u'__slot_formtop'].pop()
        except:
            __slot_formtop = None

        try:
            __slot_fields = econtext[u'__slot_fields'].pop()
        except:
            __slot_fields = None

        try:
            __slot_belowfields = econtext[u'__slot_belowfields'].pop()
        except:
            __slot_belowfields = None

        try:
            __slot_description = econtext[u'__slot_description'].pop()
        except:
            __slot_description = None

        try:
            __slot_actions = econtext[u'__slot_actions'].pop()
        except:
            __slot_actions = None

        try:
            __slot_formbottom = econtext[u'__slot_formbottom'].pop()
        except:
            __slot_formbottom = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907636432
            __attrs_140240907636432 = _static_140241133802128
            __append(u'\n\n        <!-- Status Message -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907652944
            __attrs_140240907652944 = _static_140241133802128
            __backup_status_140240916733648 = get('status', __marker)

            # <Value u'view/status' (17:35)> -> __value
            __token = 562
            try:
                __zt_tmp = __attrs_140240907652944
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/status', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['status'] = __value
            __backup_has_error_140240916730256 = get('has_error', __marker)

            # <Value u"python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)" (18:37)> -> __value
            __token = 612
            try:
                __zt_tmp = __attrs_140240907652944
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['has_error'] = __value

            # <Value u'status' (18:131)> -> __condition
            __token = 706
            try:
                __zt_tmp = __attrs_140240907652944
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'status', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c617bc6d0> name=None at 7f8c617bc710> -> __attrs_140240907651728
                __attrs_140240907651728 = _static_140240907650768

                # <Value u'has_error' (19:63)> -> __condition
                __token = 778
                try:
                    __zt_tmp = __attrs_140240907651728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'has_error', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <dl ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dl class="portalMessage alert error" role="alert">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907621072
                    __attrs_140240907621072 = _static_140241133802128
                    __previous_i18n_domain_140240907620944 = __i18n_domain
                    __i18n_domain = u'plone'

                    # <dt ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dt>')
                    __stream_140240907620624 = []
                    __append_140240907620624 = __stream_140240907620624.append
                    __append_140240907620624(u'\n              Error\n            ')
                    __msgid_140240907620624 = __re_whitespace(''.join(__stream_140240907620624)).strip()
                    if __msgid_140240907620624:
                        __append(translate(__msgid_140240907620624, mapping=None, default=__msgid_140240907620624, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</dt>')
                    __i18n_domain = __previous_i18n_domain_140240907620944
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907624272
                    __attrs_140240907624272 = _static_140241133802128

                    # <dd ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dd>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907622288
                    __default_140240907622288 = _DEFAULT_MARKER

                    # <Value u'status' (23:29)> -> __cache_140240907621712
                    __token = 925
                    try:
                        __zt_tmp = __attrs_140240907624272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907621712 = _static_140241087907024('path', u'status', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'status' (23:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617b5450> -> __condition
                    __expression = __cache_140240907621712

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240907621712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</dd>\n          </dl>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c617b5290> name=None at 7f8c617b5d50> -> __attrs_140240907624208
                __attrs_140240907624208 = _static_140240907621008

                # <Value u'not:has_error' (25:56)> -> __condition
                __token = 1008
                try:
                    __zt_tmp = __attrs_140240907624208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('not', u'has_error', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <dl ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dl class="portalMessage info" role="status">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907657104
                    __attrs_140240907657104 = _static_140241133802128
                    __previous_i18n_domain_140240907655888 = __i18n_domain
                    __i18n_domain = u'plone'

                    # <dt ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dt>')
                    __stream_140240907656528 = []
                    __append_140240907656528 = __stream_140240907656528.append
                    __append_140240907656528(u'\n              Info\n            ')
                    __msgid_140240907656528 = __re_whitespace(''.join(__stream_140240907656528)).strip()
                    if __msgid_140240907656528:
                        __append(translate(__msgid_140240907656528, mapping=None, default=__msgid_140240907656528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</dt>')
                    __i18n_domain = __previous_i18n_domain_140240907655888
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907655056
                    __attrs_140240907655056 = _static_140241133802128

                    # <dd ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dd>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907655312
                    __default_140240907655312 = _DEFAULT_MARKER

                    # <Value u'status' (29:29)> -> __cache_140240907656080
                    __token = 1159
                    try:
                        __zt_tmp = __attrs_140240907655056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907656080 = _static_140241087907024('path', u'status', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'status' (29:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617bd910> -> __condition
                    __expression = __cache_140240907656080

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240907656080
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</dd>\n          </dl>')
                __append(u'\n        ')
            if (__backup_has_error_140240916730256 is __marker):
                del econtext['has_error']
            else:
                econtext['has_error'] = __backup_has_error_140240916730256
            if (__backup_status_140240916733648 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_140240916733648
            __append(u'\n\n        <!-- Primary Field Errors -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907656272
            __attrs_140240907656272 = _static_140241133802128
            __backup_errors_140240916732560 = get('errors', __marker)

            # <Value u'view/widgets/errors' (34:35)> -> __value
            __token = 1282
            try:
                __zt_tmp = __attrs_140240907656272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/widgets/errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['errors'] = __value

            # <Value u'errors' (34:67)> -> __condition
            __token = 1314
            try:
                __zt_tmp = __attrs_140240907656272
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907653328
                __attrs_140240907653328 = _static_140241133802128
                __backup_error_140240916730000 = get('error', __marker)

                # <Value u'errors' (35:35)> -> __iterator
                __token = 1358
                try:
                    __zt_tmp = __attrs_140240907653328
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907654928, ) = getitem('repeat')(u'error', __iterator)
                econtext['error'] = None
                for __item in __iterator:
                    econtext['error'] = __item
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c617b32d0> name=None at 7f8c617b3290> -> __attrs_140240907613520
                    __attrs_140240907613520 = _static_140240907612880

                    # <Value u'not:nocall:error/widget' (37:32)> -> __condition
                    __token = 1456
                    try:
                        __zt_tmp = __attrs_140240907613520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('not', u'nocall:error/widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="field error alert alert-warning">')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907612432
                        __default_140240907612432 = _DEFAULT_MARKER

                        # <Value u'error/render' (38:40)> -> __cache_140240907615120
                        __token = 1521
                        try:
                            __zt_tmp = __attrs_140240907613520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240907615120 = _static_140241087907024('path', u'error/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'error/render' (38:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617b3050> -> __condition
                        __expression = __cache_140240907615120

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              Error\n            ')
                        else:
                            __content = __cache_140240907615120
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</div>')
                    __append(u'\n          ')
                    ____index_140240907654928 -= 1
                    if (____index_140240907654928 > 0):
                        __append('')
                if (__backup_error_140240916730000 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_140240916730000
                __append(u'\n        ')
            if (__backup_errors_140240916732560 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140240916732560
            __append(u'\n\n        <!-- Secondary Field Errors -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907654352
            __attrs_140240907654352 = _static_140241133802128
            __backup_groups_140240916732176 = get('groups', __marker)

            # <Value u'view/groups|nothing' (45:35)> -> __value
            __token = 1696
            try:
                __zt_tmp = __attrs_140240907654352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/groups|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['groups'] = __value

            # <Value u'python:bool(groups)' (46:31)> -> __condition
            __token = 1748
            try:
                __zt_tmp = __attrs_140240907654352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'bool(groups)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __backup_group_140240916732368 = get('group', __marker)

                # <Value u'groups' (47:34)> -> __iterator
                __token = 1803
                try:
                    __zt_tmp = __attrs_140240907654352
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'groups', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907613200, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907613968
                    __attrs_140240907613968 = _static_140241133802128
                    __backup_errors_140240916731792 = get('errors', __marker)

                    # <Value u'group/widgets/errors' (48:40)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_140240907613968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/widgets/errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value u'errors' (49:35)> -> __condition
                    __token = 1909
                    try:
                        __zt_tmp = __attrs_140240907613968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140240916733776 = get('error', __marker)

                        # <Value u'errors' (50:38)> -> __iterator
                        __token = 1955
                        try:
                            __zt_tmp = __attrs_140240907613968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140241087907024('path', u'errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        (__iterator, ____index_140240907614160, ) = getitem('repeat')(u'error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append(u'\n            ')

                            # <Static value=<_ast.Dict object at 0x7f8c617af210> name=None at 7f8c617af250> -> __attrs_140240907596048
                            __attrs_140240907596048 = _static_140240907596304

                            # <Value u'not:nocall:error/widget' (52:31)> -> __condition
                            __token = 2052
                            try:
                                __zt_tmp = __attrs_140240907596048
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140241087907024('not', u'nocall:error/widget', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="field error alert alert-warning">')

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907596560
                                __default_140240907596560 = _DEFAULT_MARKER

                                # <Value u'error/render' (53:39)> -> __cache_140240907614928
                                __token = 2116
                                try:
                                    __zt_tmp = __attrs_140240907596048
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140240907614928 = _static_140241087907024('path', u'error/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                                # <BinOp left=<Value u'error/render' (53:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617b3e50> -> __condition
                                __expression = __cache_140240907614928

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140240907614928
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</div>')
                            __append(u'\n          ')
                            ____index_140240907614160 -= 1
                            if (____index_140240907614160 > 0):
                                __append('')
                        if (__backup_error_140240916733776 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140240916733776
                    if (__backup_errors_140240916731792 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140240916731792
                    __append(u'\n        ')
                    ____index_140240907613200 -= 1
                    if (____index_140240907613200 > 0):
                        __append('')
                if (__backup_group_140240916732368 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140240916732368
            if (__backup_groups_140240916732176 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140240916732176
            __append(u'\n\n        <!-- Description -->\n        ')
            if (__slot_description is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907613904
                __attrs_140240907613904 = _static_140241133802128
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c617afd50> name=None at 7f8c617aff50> -> __attrs_140240907598800
                __attrs_140240907598800 = _static_140240907599184
                __backup_description_140240916733520 = get('description', __marker)

                # <Value u'view/description | nothing' (60:37)> -> __value
                __token = 2348
                try:
                    __zt_tmp = __attrs_140240907598800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('path', u'view/description | nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['description'] = __value

                # <Value u'description' (61:28)> -> __condition
                __token = 2404
                try:
                    __zt_tmp = __attrs_140240907598800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet text-secondary">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907599568
                    __default_140240907599568 = _DEFAULT_MARKER

                    # <Value u'description|default' (62:36)> -> __cache_140240907597904
                    __token = 2453
                    try:
                        __zt_tmp = __attrs_140240907598800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907597904 = _static_140241087907024('path', u'description|default', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'description|default' (62:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617afe90> -> __condition
                    __expression = __cache_140240907597904

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n            Description\n          ')
                    else:
                        __content = __cache_140240907597904
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>')
                if (__backup_description_140240916733520 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_140240916733520
                __append(u'\n        ')
            else:
                __slot_description(__stream, econtext.copy(), rcontext)
            __append(u'\n\n        <!-- Form -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c617afa10> name=None at 7f8c617afa90> -> __attrs_140240907147920
            __attrs_140240907147920 = _static_140240907598352
            __backup_groups_140240916730064 = get('groups', __marker)

            # <Value u'view/groups | nothing' (70:33)> -> __value
            __token = 2787
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/groups | nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_form_name_140240916731984 = get('form_name', __marker)

            # <Value u'view/form_name | nothing' (71:35)> -> __value
            __token = 2845
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/form_name | nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['form_name'] = __value
            __backup_form_class_140240916730128 = get('form_class', __marker)

            # <Value u'view/css_class | string:' (72:35)> -> __value
            __token = 2907
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/css_class | string:', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['form_class'] = __value
            __backup_default_fieldset_label_140240916732112 = get('default_fieldset_label', __marker)

            # <Value u'view/default_fieldset_label | form_name' (73:46)> -> __value
            __token = 2981
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/default_fieldset_label | form_name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['default_fieldset_label'] = __value
            __backup_enable_form_tabbing_140240916731920 = get('enable_form_tabbing', __marker)

            # <Value u'view/enable_form_tabbing | python:True' (74:42)> -> __value
            __token = 3067
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/enable_form_tabbing | python:True', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['enable_form_tabbing'] = __value
            __backup_enable_unload_protection_140240916733264 = get('enable_unload_protection', __marker)

            # <Value u'view/enable_unload_protection|python:True' (75:46)> -> __value
            __token = 3157
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/enable_unload_protection|python:True', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['enable_unload_protection'] = __value
            __backup_unload_protection_140240916730576 = get('unload_protection', __marker)

            # <Value u"python:enable_unload_protection and 'pat-formunloadalert'" (76:38)> -> __value
            __token = 3243
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"enable_unload_protection and 'pat-formunloadalert'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['unload_protection'] = __value
            __backup_has_groups_140240916732240 = get('has_groups', __marker)

            # <Value u'python:bool(groups)' (77:30)> -> __value
            __token = 3338
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'bool(groups)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __backup_form_tabbing_140240916733008 = get('form_tabbing', __marker)

            # <Value u"python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''" (78:31)> -> __value
            __token = 3397
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['form_tabbing'] = __value
            __backup_show_default_label_140240916732816 = get('show_default_label', __marker)

            # <Value u'python:has_groups and default_fieldset_label and len(view.widgets)' (79:36)> -> __value
            __token = 3528
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'has_groups and default_fieldset_label and len(view.widgets)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_form_view_name_raw_140240916733136 = get('form_view_name_raw', __marker)

            # <Value u"python:view.__name__ or request.getURL().split('/')[-1]" (80:35)> -> __value
            __token = 3640
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"view.__name__ or request.getURL().split('/')[-1]", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['form_view_name_raw'] = __value
            __backup_form_view_name_140240916733072 = get('form_view_name', __marker)

            # <Value u"python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])" (81:30)> -> __value
            __token = 3737
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['form_view_name'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form data-pat-autotoc="levels: legend; section: fieldset; className: autotabs"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907145616
            __default_140240907145616 = _DEFAULT_MARKER

            # <Substitution u"python:'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_name)" (85:34)> -> __attr_class
            __token = 4013
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140241087907024('python', u"'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_name)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'rowlike enableUnloadProtection', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907145552
            __default_140240907145552 = _DEFAULT_MARKER

            # <Substitution u'view/action|request/getURL' (83:37)> -> __attr_action
            __token = 3899
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140241087907024('path', u'view/action|request/getURL', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907146896
            __default_140240907146896 = _DEFAULT_MARKER

            # <Substitution u'view/method|string:post' (87:33)> -> __attr_method
            __token = 4233
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_method = _static_140241087907024('path', u'view/method|string:post', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_method = __quote(__attr_method, '"', '&quot;', u'post', _DEFAULT_MARKER)
            if (__attr_method is not None):
                __append((u' method="%s"' % __attr_method))
            __append(u' name="edit_form"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907147408
            __default_140240907147408 = _DEFAULT_MARKER

            # <Substitution u'view/enctype' (84:37)> -> __attr_enctype
            __token = 3964
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_140241087907024('path', u'view/enctype', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((u' enctype="%s"' % __attr_enctype))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907147536
            __default_140240907147536 = _DEFAULT_MARKER

            # <Substitution u'view/id' (86:30)> -> __attr_id
            __token = 4188
            try:
                __zt_tmp = __attrs_140240907147920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n\n          ')
            if (__slot_formtop is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907367440
                __attrs_140240907367440 = _static_140241133802128
            else:
                __slot_formtop(__stream, econtext.copy(), rcontext)
            __append(u'\n\n          <!-- navigation tabs -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c61777610> name=None at 7f8c61777590> -> __attrs_140240907368912
            __attrs_140240907368912 = _static_140240907367952

            # <Value u'python: has_groups and enable_form_tabbing' (93:29)> -> __condition
            __token = 4427
            try:
                __zt_tmp = __attrs_140240907368912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u' has_groups and enable_form_tabbing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="nav nav-tabs" role="tablist">\n\n            <!-- primary tab -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c61777d90> name=None at 7f8c61777dd0> -> __attrs_140240907317776
                __attrs_140240907317776 = _static_140240907369872
                __backup_has_errors_140240916636176 = get('has_errors', __marker)

                # <Value u'view/widgets/errors' (97:39)> -> __value
                __token = 4598
                try:
                    __zt_tmp = __attrs_140240907317776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('path', u'view/widgets/errors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['has_errors'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="nav-item" role="presentation">\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c6176b710> name=None at 7f8c6176b790> -> __attrs_140240907321040
                __attrs_140240907321040 = _static_140240907319056

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a id="default-tab" href="#default" data-toggle="tab" role="tab"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907320720
                __default_140240907320720 = _DEFAULT_MARKER

                # <Substitution u"python:has_errors and 'nav-link active text-danger' or 'nav-link active'" (99:39)> -> __attr_class
                __token = 4713
                try:
                    __zt_tmp = __attrs_140240907321040
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140241087907024('python', u"has_errors and 'nav-link active text-danger' or 'nav-link active'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907318864
                __default_140240907318864 = _DEFAULT_MARKER

                # <Value u'default_fieldset_label' (98:30)> -> __cache_140240907318544
                __token = 4650
                try:
                    __zt_tmp = __attrs_140240907321040
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240907318544 = _static_140241087907024('path', u'default_fieldset_label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'default_fieldset_label' (98:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6176b590> -> __condition
                __expression = __cache_140240907318544

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n                Label\n              ')
                else:
                    __content = __cache_140240907318544
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>\n            </li>')
                if (__backup_has_errors_140240916636176 is __marker):
                    del econtext['has_errors']
                else:
                    econtext['has_errors'] = __backup_has_errors_140240916636176
                __append(u'\n\n            <!-- secondary tabs -->\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c6177a0d0> name=None at 7f8c6177a110> -> __attrs_140240907379984
                __attrs_140240907379984 = _static_140240907378896
                __backup_group_140240916621648 = get('group', __marker)

                # <Value u'groups' (109:34)> -> __iterator
                __token = 5048
                try:
                    __zt_tmp = __attrs_140240907379984
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'groups', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907380112, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="nav-item" role="presentation">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c6177aa90> name=None at 7f8c6213c2d0> -> __attrs_140240907399760
                    __attrs_140240907399760 = _static_140240907381392
                    __backup_normalizeString_140240907729616 = get('normalizeString', __marker)

                    # <Value u'nocall:context/@@plone/normalizeString' (110:45)> -> __value
                    __token = 5139
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('nocall', u'context/@@plone/normalizeString', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_140240916833808 = get('fieldset_label', __marker)

                    # <Value u'group/label' (111:43)> -> __value
                    __token = 5222
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_140240916833872 = get('fieldset_name', __marker)

                    # <Value u"python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (112:41)> -> __value
                    __token = 5277
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('python', u"getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_140240907728528 = get('fieldset_name', __marker)

                    # <Value u'python:normalizeString(fieldset_name)' (113:40)> -> __value
                    __token = 5421
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('python', u'normalizeString(fieldset_name)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_has_errors_140240907727824 = get('has_errors', __marker)

                    # <Value u'group/widgets/errors|nothing' (114:36)> -> __value
                    __token = 5499
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'group/widgets/errors|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['has_errors'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a data-toggle="tab" role="tab"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907382480
                    __default_140240907382480 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldset_name}-tab' (115:36)> -> __attr_id
                    __token = 5569
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140241087907024('string', u'${fieldset_name}-tab', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907382736
                    __default_140240907382736 = _DEFAULT_MARKER

                    # <Substitution u'string:#${fieldset_name}' (116:37)> -> __attr_href
                    __token = 5635
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('string', u'#${fieldset_name}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907399440
                    __default_140240907399440 = _DEFAULT_MARKER

                    # <Substitution u"python:has_errors and 'nav-link text-danger' or 'nav-link'" (117:37)> -> __attr_class
                    __token = 5699
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"has_errors and 'nav-link text-danger' or 'nav-link'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907381200
                    __default_140240907381200 = _DEFAULT_MARKER

                    # <Value u'fieldset_label' (118:30)> -> __cache_140240907380816
                    __token = 5791
                    try:
                        __zt_tmp = __attrs_140240907399760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907380816 = _static_140241087907024('path', u'fieldset_label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'fieldset_label' (118:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6177a910> -> __condition
                    __expression = __cache_140240907380816

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                Label\n              ')
                    else:
                        __content = __cache_140240907380816
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>')
                    if (__backup_has_errors_140240907727824 is __marker):
                        del econtext['has_errors']
                    else:
                        econtext['has_errors'] = __backup_has_errors_140240907727824
                    if (__backup_fieldset_name_140240907728528 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140240907728528
                    if (__backup_fieldset_name_140240916833872 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140240916833872
                    if (__backup_fieldset_label_140240916833808 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_140240916833808
                    if (__backup_normalizeString_140240907729616 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140240907729616
                    __append(u'\n            </li>')
                    ____index_140240907380112 -= 1
                    if (____index_140240907380112 > 0):
                        __append('\n            ')
                if (__backup_group_140240916621648 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140240916621648
                __append(u'\n          </ul>')
            __append(u'\n\n          ')
            if (__slot_fields is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907400720
                __attrs_140240907400720 = _static_140241133802128
                __append(u'\n\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c6177f990> name=None at 7f8c6177f9d0> -> __attrs_140240907402896
                __attrs_140240907402896 = _static_140240907401616
                __backup_current_fieldset_140240916731536 = get('current_fieldset', __marker)

                # <Value u'request/fieldset | python:None' (130:48)> -> __value
                __token = 6115
                try:
                    __zt_tmp = __attrs_140240907402896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('path', u'request/fieldset | python:None', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['current_fieldset'] = __value

                # <Value u'python:has_groups and enable_form_tabbing and current_fieldset is not None' (131:34)> -> __condition
                __token = 6181
                try:
                    __zt_tmp = __attrs_140240907402896
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'has_groups and enable_form_tabbing and current_fieldset is not None', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="fieldset"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907402640
                    __default_140240907402640 = _DEFAULT_MARKER

                    # <Substitution u'current_fieldset' (132:41)> -> __attr_value
                    __token = 6298
                    try:
                        __zt_tmp = __attrs_140240907402896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'current_fieldset', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />')
                if (__backup_current_fieldset_140240916731536 is __marker):
                    del econtext['current_fieldset']
                else:
                    econtext['current_fieldset'] = __backup_current_fieldset_140240916731536
                __append(u'\n\n            <!-- Default fieldset -->\n            ')
                __token = None
                render_fields(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n          ')
            else:
                __slot_fields(__stream, econtext.copy(), rcontext)
            __append(u'\n\n          ')
            if (__slot_belowfields is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907391568
                __attrs_140240907391568 = _static_140241133802128
            else:
                __slot_belowfields(__stream, econtext.copy(), rcontext)
            __append(u'\n\n          ')
            if (__slot_actions is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907393488
                __attrs_140240907393488 = _static_140241133802128
                __append(u'\n            ')
                __token = None
                render_actions(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n          ')
            else:
                __slot_actions(__stream, econtext.copy(), rcontext)
            __append(u'\n\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906891600
            __attrs_140240906891600 = _static_140241133802128

            # <Value u'view/enableCSRFProtection|nothing' (207:36)> -> __condition
            __token = 9650
            try:
                __zt_tmp = __attrs_140240906891600
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/enableCSRFProtection|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906894544
                __default_140240906894544 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (208:44)> -> __cache_140240906916432
                __token = 9729
                try:
                    __zt_tmp = __attrs_140240906891600
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906916432 = _static_140241087907024('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (208:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61709a90> -> __condition
                __expression = __cache_140240906916432

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240906916432
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append(u'\n          ')
            if (__slot_formbottom is None):

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906893968
                __attrs_140240906893968 = _static_140241133802128
            else:
                __slot_formbottom(__stream, econtext.copy(), rcontext)
            __append(u'\n\n        </form>')
            if (__backup_form_view_name_140240916733072 is __marker):
                del econtext['form_view_name']
            else:
                econtext['form_view_name'] = __backup_form_view_name_140240916733072
            if (__backup_form_view_name_raw_140240916733136 is __marker):
                del econtext['form_view_name_raw']
            else:
                econtext['form_view_name_raw'] = __backup_form_view_name_raw_140240916733136
            if (__backup_show_default_label_140240916732816 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140240916732816
            if (__backup_form_tabbing_140240916733008 is __marker):
                del econtext['form_tabbing']
            else:
                econtext['form_tabbing'] = __backup_form_tabbing_140240916733008
            if (__backup_has_groups_140240916732240 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140240916732240
            if (__backup_unload_protection_140240916730576 is __marker):
                del econtext['unload_protection']
            else:
                econtext['unload_protection'] = __backup_unload_protection_140240916730576
            if (__backup_enable_unload_protection_140240916733264 is __marker):
                del econtext['enable_unload_protection']
            else:
                econtext['enable_unload_protection'] = __backup_enable_unload_protection_140240916733264
            if (__backup_enable_form_tabbing_140240916731920 is __marker):
                del econtext['enable_form_tabbing']
            else:
                econtext['enable_form_tabbing'] = __backup_enable_form_tabbing_140240916731920
            if (__backup_default_fieldset_label_140240916732112 is __marker):
                del econtext['default_fieldset_label']
            else:
                econtext['default_fieldset_label'] = __backup_default_fieldset_label_140240916732112
            if (__backup_form_class_140240916730128 is __marker):
                del econtext['form_class']
            else:
                econtext['form_class'] = __backup_form_class_140240916730128
            if (__backup_form_name_140240916731984 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_140240916731984
            if (__backup_groups_140240916730064 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140240916730064
            __append(u'\n      ')
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

            # <Static value=<_ast.Dict object at 0x7f8c617acfd0> name=None at 7f8c617acf90> -> __attrs_140240907585104
            __attrs_140240907585104 = _static_140240907587536
            __previous_i18n_domain_140240907586896 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907635088
            __attrs_140240907635088 = _static_140241133802128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n    ')
            __token = None
            render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140240907586896
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_rendering': render_widget_rendering, u'render_form': render_form, u'render_fields': render_fields, u'render_actions': render_actions, u'render_field': render_field, u'render_titlelessform': render_titlelessform, 'render': render, }