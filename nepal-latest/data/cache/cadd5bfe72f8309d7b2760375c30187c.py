# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.listing/src/senaite/app/listing/templates/contents_table.pt'

__tokens = {37: (u'context/@@plone_portal_state/portal', 2, 17), 284: (u'view/form_adapter_name|nothing', 9, 38), 351: (u" python:'senaite-ajax-form' if form_adapter_name else '", 10, 35), 449: (u's python:view.additional_form_cla', 11, 40), 230: (u'view/omit_form', 8, 22), 562: (u' python:view.get_form_name(', 13, 28), 620: (u's string:form form-inline ${ajax_form_class} ${additional_form_clas', 14, 28), 513: (u'python:view.form_id', 12, 27), 719: (u'on python:view.getPOSTActio', 15, 28), 782: (u'not:view/omit_form', 17, 29), 839: (u'context/@@authenticator/authenticator', 18, 36), 966: (u'form_adapter_name', 22, 28), 1081: (u'form_adapter_name', 24, 35), 1211: (u'python:view.additional_hidden_fields', 29, 32), 1273: (u'python:input_attrs', 30, 24), 1437: (u'python:view.form_id', 36, 38), 1506: (u' python:view.listing_identifie', 37, 48), 1591: (u's python:view.ajax_transitions_enabled', 38, 52), 1684: (u'ns python:view.ajax_transitions_lis', 39, 51), 1759: (u'ize python:view.page', 40, 35), 1818: (u'_url python:view.get_api_', 41, 33), 1882: (u'lumns python:view.ajax_col', 42, 32), 1959: (u'oggles python:view.ajax_show_column_to', 43, 43), 2049: (u'w_state python:view.default_revi', 44, 43), 2126: (u'w_states python:view.ajax_review', 45, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574270217360 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140574268943696 = set([])
_static_140574284496464 = {u'id': u'python:view.form_id', u'method': u'post', u'name': u'listing_form', u'action': u'python:view.getPOSTAction()', u'class': u'listing_form form form-inline', }
_static_140574270357712 = {u'data-enable_ajax_transitions': u'python:view.ajax_transitions_enabled()', u'data-pagesize': u'python:view.pagesize', u'data-listing_identifier': u'python:view.listing_identifier', u'data-show_column_toggles': u'python:view.ajax_show_column_toggles()', u'data-default_review_state': u'python:view.default_review_state', u'data-form_id': u'python:view.form_id', u'class': u'ajax-contents-table w-100', u'data-api_url': u'python:view.get_api_url()', u'data-columns': u'python:view.ajax_columns()', u'data-review_states': u'python:view.ajax_review_states()', u'data-active_ajax_transitions': u'python:view.ajax_transitions_list()', }
_static_140574442558096 = {}
_static_140574397981968 = __compile_zt_expr
_static_140574267881872 = {u'type': u'hidden', u'name': u'form_adapter_name', u'value': u'', }
_static_140574266168848 = {u'type': u'hidden', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284494160
            __attrs_140574284494160 = _static_140574442558096
            __backup_portal_140574266167760 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (2:17)> -> __value
            __token = 37
            try:
                __zt_tmp = __attrs_140574284494160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['portal'] = __value
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fda004abe50> name=None at 7fda004ab350> -> __attrs_140574267905424
            __attrs_140574267905424 = _static_140574284496464
            __backup_form_adapter_name_140574257287824 = get('form_adapter_name', __marker)

            # <Value u'view/form_adapter_name|nothing' (9:38)> -> __value
            __token = 284
            try:
                __zt_tmp = __attrs_140574267905424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/form_adapter_name|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['form_adapter_name'] = __value
            __backup_ajax_form_class_140574267903504 = get('ajax_form_class', __marker)

            # <Value u"python:'senaite-ajax-form' if form_adapter_name else ''" (10:35)> -> __value
            __token = 351
            try:
                __zt_tmp = __attrs_140574267905424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"'senaite-ajax-form' if form_adapter_name else ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['ajax_form_class'] = __value
            __backup_additional_form_class_140574267902544 = get('additional_form_class', __marker)

            # <Value u'python:view.additional_form_class' (11:40)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_140574267905424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.additional_form_class', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['additional_form_class'] = __value
            __previous_i18n_domain_140574284358928 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <Negate value=<Value u'view/omit_form' (8:22)> at 7fd9ff4d9250> -> __cache_140574267904592

            # <Value u'view/omit_form' (8:22)> -> __cache_140574267904592
            __token = 230
            try:
                __zt_tmp = __attrs_140574267905424
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574267904592 = _static_140574397981968('path', u'view/omit_form', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __cache_140574267904592 = not __cache_140574267904592
            __condition = __cache_140574267904592
            if __condition:

                # <form ... (0:0)
                # --------------------------------------------------------
                __append(u'<form')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284496528
                __default_140574284496528 = _DEFAULT_MARKER

                # <Substitution u'python:view.get_form_name()' (13:28)> -> __attr_name
                __token = 562
                try:
                    __zt_tmp = __attrs_140574267905424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140574397981968('python', u'view.get_form_name()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', u'listing_form', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267907408
                __default_140574267907408 = _DEFAULT_MARKER

                # <Substitution u'string:form form-inline ${ajax_form_class} ${additional_form_class}' (14:28)> -> __attr_class
                __token = 620
                try:
                    __zt_tmp = __attrs_140574267905424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140574397981968('string', u'form form-inline ${ajax_form_class} ${additional_form_class}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'listing_form form form-inline', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u' method="post"')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267904720
                __default_140574267904720 = _DEFAULT_MARKER

                # <Substitution u'python:view.form_id' (12:27)> -> __attr_id
                __token = 513
                try:
                    __zt_tmp = __attrs_140574267905424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140574397981968('python', u'view.form_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267907792
                __default_140574267907792 = _DEFAULT_MARKER

                # <Substitution u'python:view.getPOSTAction()' (15:28)> -> __attr_action
                __token = 719
                try:
                    __zt_tmp = __attrs_140574267905424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140574397981968('python', u'view.getPOSTAction()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((u' action="%s"' % __attr_action))
                __append(u'>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284359568
            __attrs_140574284359568 = _static_140574442558096

            # <Value u'not:view/omit_form' (17:29)> -> __condition
            __token = 782
            try:
                __zt_tmp = __attrs_140574284359568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('not', u'view/omit_form', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270214992
                __attrs_140574270214992 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270214672
                __default_140574270214672 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (18:36)> -> __cache_140574284360400
                __token = 839
                try:
                    __zt_tmp = __attrs_140574270214992
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574284360400 = _static_140574397981968('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (18:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff70da10> -> __condition
                __expression = __cache_140574284360400

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input/>')
                else:
                    __content = __cache_140574284360400
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff70dc90> name=None at 7fd9ff70db50> -> __attrs_140574267880208
                __attrs_140574267880208 = _static_140574270217360

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" name="submitted" value="1"/>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4d3990> name=None at 7fd9ff4d3d50> -> __attrs_140574266167824
                __attrs_140574266167824 = _static_140574267881872

                # <Value u'form_adapter_name' (22:28)> -> __condition
                __token = 966
                try:
                    __zt_tmp = __attrs_140574266167824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'form_adapter_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="form_adapter_name"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266167696
                    __default_140574266167696 = _DEFAULT_MARKER

                    # <Substitution u'form_adapter_name' (24:35)> -> __attr_value
                    __token = 1081
                    try:
                        __zt_tmp = __attrs_140574266167824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140574397981968('path', u'form_adapter_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />')
                __append(u'\n\n      <!-- additional hidden fields -->\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff331610> name=None at 7fd9ff3316d0> -> __attrs_140574270359888
                __attrs_140574270359888 = _static_140574266168848
                __backup_input_attrs_140574267905744 = get('input_attrs', __marker)

                # <Value u'python:view.additional_hidden_fields' (29:32)> -> __iterator
                __token = 1211
                try:
                    __zt_tmp = __attrs_140574270359888
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('python', u'view.additional_hidden_fields', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574270361296, ) = getitem('repeat')(u'input_attrs', __iterator)
                econtext['input_attrs'] = None
                for __item in __iterator:
                    econtext['input_attrs'] = __item

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input')

                    # <Value u'python:input_attrs' (30:24)> -> __cache_140574270359632
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_140574270359888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574270359632 = _static_140574397981968('python', u'input_attrs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if (u'type' not in __chain(__cache_140574270359632)):
                        __append(u' type="hidden"')
                    __attr_140574270359376 = __cache_140574270359632
                    for (name, value, ) in __attr_140574270359376.items():
                        if ((name not in _static_140574268943696) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(u'/>')
                    ____index_140574270361296 -= 1
                    if (____index_140574270361296 > 0):
                        __append('\n      ')
                if (__backup_input_attrs_140574267905744 is __marker):
                    del econtext['input_attrs']
                else:
                    econtext['input_attrs'] = __backup_input_attrs_140574267905744
                __append(u'\n\n    ')
            __append(u'\n\n    <!-- ReactJS managed component -->\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff7300d0> name=None at 7fd9ff7309d0> -> __attrs_140574257197008
            __attrs_140574257197008 = _static_140574270357712

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="ajax-contents-table w-100"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267903440
            __default_140574267903440 = _DEFAULT_MARKER

            # <Substitution u'python:view.form_id' (36:38)> -> __attr_data_form_id
            __token = 1437
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_form_id = _static_140574397981968('python', u'view.form_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_form_id = __quote(__attr_data_form_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_form_id is not None):
                __append((u' data-form_id="%s"' % __attr_data_form_id))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267901200
            __default_140574267901200 = _DEFAULT_MARKER

            # <Substitution u'python:view.listing_identifier' (37:48)> -> __attr_data_listing_identifier
            __token = 1506
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_listing_identifier = _static_140574397981968('python', u'view.listing_identifier', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_listing_identifier = __quote(__attr_data_listing_identifier, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_listing_identifier is not None):
                __append((u' data-listing_identifier="%s"' % __attr_data_listing_identifier))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267901008
            __default_140574267901008 = _DEFAULT_MARKER

            # <Substitution u'python:view.ajax_transitions_enabled()' (38:52)> -> __attr_data_enable_ajax_transitions
            __token = 1591
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_enable_ajax_transitions = _static_140574397981968('python', u'view.ajax_transitions_enabled()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_enable_ajax_transitions = __quote(__attr_data_enable_ajax_transitions, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_enable_ajax_transitions is not None):
                __append((u' data-enable_ajax_transitions="%s"' % __attr_data_enable_ajax_transitions))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267900176
            __default_140574267900176 = _DEFAULT_MARKER

            # <Substitution u'python:view.ajax_transitions_list()' (39:51)> -> __attr_data_active_ajax_transitions
            __token = 1684
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_active_ajax_transitions = _static_140574397981968('python', u'view.ajax_transitions_list()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_active_ajax_transitions = __quote(__attr_data_active_ajax_transitions, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_active_ajax_transitions is not None):
                __append((u' data-active_ajax_transitions="%s"' % __attr_data_active_ajax_transitions))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257194256
            __default_140574257194256 = _DEFAULT_MARKER

            # <Substitution u'python:view.pagesize' (40:35)> -> __attr_data_pagesize
            __token = 1759
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pagesize = _static_140574397981968('python', u'view.pagesize', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_pagesize = __quote(__attr_data_pagesize, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pagesize is not None):
                __append((u' data-pagesize="%s"' % __attr_data_pagesize))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257196752
            __default_140574257196752 = _DEFAULT_MARKER

            # <Substitution u'python:view.get_api_url()' (41:33)> -> __attr_data_api_url
            __token = 1818
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_api_url = _static_140574397981968('python', u'view.get_api_url()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_api_url = __quote(__attr_data_api_url, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_api_url is not None):
                __append((u' data-api_url="%s"' % __attr_data_api_url))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257196112
            __default_140574257196112 = _DEFAULT_MARKER

            # <Substitution u'python:view.ajax_columns()' (42:32)> -> __attr_data_columns
            __token = 1882
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_columns = _static_140574397981968('python', u'view.ajax_columns()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_columns = __quote(__attr_data_columns, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_columns is not None):
                __append((u' data-columns="%s"' % __attr_data_columns))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257195024
            __default_140574257195024 = _DEFAULT_MARKER

            # <Substitution u'python:view.ajax_show_column_toggles()' (43:43)> -> __attr_data_show_column_toggles
            __token = 1959
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_show_column_toggles = _static_140574397981968('python', u'view.ajax_show_column_toggles()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_show_column_toggles = __quote(__attr_data_show_column_toggles, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_show_column_toggles is not None):
                __append((u' data-show_column_toggles="%s"' % __attr_data_show_column_toggles))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257193360
            __default_140574257193360 = _DEFAULT_MARKER

            # <Substitution u'python:view.default_review_state' (44:43)> -> __attr_data_default_review_state
            __token = 2049
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_default_review_state = _static_140574397981968('python', u'view.default_review_state', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_default_review_state = __quote(__attr_data_default_review_state, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_default_review_state is not None):
                __append((u' data-default_review_state="%s"' % __attr_data_default_review_state))

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257195280
            __default_140574257195280 = _DEFAULT_MARKER

            # <Substitution u'python:view.ajax_review_states()' (45:35)> -> __attr_data_review_states
            __token = 2126
            try:
                __zt_tmp = __attrs_140574257197008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_review_states = _static_140574397981968('python', u'view.ajax_review_states()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_data_review_states = __quote(__attr_data_review_states, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_review_states is not None):
                __append((u' data-review_states="%s"' % __attr_data_review_states))
            __append(u'>\n    </div>\n  ')
            __condition = __cache_140574267904592
            if __condition:
                __append(u'</form>')
            __i18n_domain = __previous_i18n_domain_140574284358928
            if (__backup_additional_form_class_140574267902544 is __marker):
                del econtext['additional_form_class']
            else:
                econtext['additional_form_class'] = __backup_additional_form_class_140574267902544
            if (__backup_ajax_form_class_140574267903504 is __marker):
                del econtext['ajax_form_class']
            else:
                econtext['ajax_form_class'] = __backup_ajax_form_class_140574267903504
            if (__backup_form_adapter_name_140574257287824 is __marker):
                del econtext['form_adapter_name']
            else:
                econtext['form_adapter_name'] = __backup_form_adapter_name_140574257287824
            __append(u'\n\n')
            if (__backup_portal_140574266167760 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140574266167760
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }