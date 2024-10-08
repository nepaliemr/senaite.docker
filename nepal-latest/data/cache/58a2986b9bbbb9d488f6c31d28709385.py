# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/worksheet/views/../templates/results.pt'

__tokens = {441: (u'view/icon | nothing', 16, 28), 502: (u'view/icon', 17, 40), 571: (u'context/title_or_id', 18, 56), 1320: (u'view/is_assignment_allowed', 39, 39), 1595: (u'view/get_analysts', 43, 46), 1665: (u'alist', 44, 50), 1727: (u'python:option', 45, 54), 1798: (u" python: context.getAnalyst() == option and 'selected' or '", 46, 56), 1906: (u'python:alist.getValue(option)', 47, 45), 2122: (u'not: view/is_assignment_allowed', 52, 39), 2246: (u'python:view.get_analysts().getValue(context.getAnalyst())', 54, 39), 2517: (u'python:context.getInstrument()', 61, 41), 2887: (u'view/is_assignment_allowed', 68, 39), 3169: (u'view/getInstruments', 72, 50), 3241: (u'instrlist', 73, 50), 3307: (u'python:option', 74, 54), 3378: (u" python: instrument and instrument.UID() == option and 'selected' or '", 75, 56), 3497: (u'python:instrlist.getValue(option)', 76, 45), 3718: (u'not: view/is_assignment_allowed', 82, 39), 3844: (u'python:instrument', 84, 41), 3902: (u'python:view.getInstruments().getValue(instrument.UID())', 85, 39), 4059: (u'python:not instrument', 87, 41), 5131: (u'python:view.layout_displaylist.items()', 112, 55), 5228: (u'python: option[0] == context.getResultsLayout()', 113, 56), 5331: (u'python:option[0]', 114, 54), 5394: (u'python:option[1]', 115, 45), 5494: (u'python: option[0] != context.getResultsLayout()', 117, 47), 5597: (u'python:option[0]', 118, 54), 5660: (u'python:option[1]', 119, 45), 6609: (u"python:context.absolute_url()+'/print'", 140, 44), 7087: (u'view/get_wide_interims', 156, 49), 7151: (u'python:wideinterims', 157, 39), 7219: (u'python:wideinterims.keys()[0]', 158, 46), 7300: (u" python:wideinterims[wideanselected]['interims'].keys()[0", 159, 50), 7849: (u'python:wideinterims.keys()', 169, 50), 7932: (u'python:option', 170, 54), 8003: (u' python:option==wideanselecte', 171, 56), 8081: (u"python:wideinterims[option]['analysis']", 172, 45), 8243: (u'python:wideinterims.keys()', 175, 51), 8327: (u"python:wideinterims[an]['interims'].values()", 176, 55), 8468: (u"python:'wideinterim_%s_%s' % (an, inter['keyword'])", 178, 49), 8571: (u" python:inter['title'", 179, 50), 8645: (u"e python:inter['value", 180, 50), 8721: (u"rd python:inter['keywor", 181, 51), 9033: (u"python:wideinterims[wideanselected]['interims'].keys()", 189, 43), 9389: (u'interims', 194, 51), 9454: (u'python:interim', 195, 54), 9526: (u' python:interim==wideinterimselecte', 196, 56), 9610: (u"python:wideinterims[wideanselected]['interims'][interim]['title']", 197, 45), 10270: (u"python:wideinterims[wideanselected]['interims'][wideinterimselected]['value']", 212, 48), 11067: (u'view/Analyses/contents_table', 232, 41), 11391: (u'nocall: context/portal_membership/checkPermission', 242, 41), 11463: (u" python:'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view", 243, 21), 11577: (u"d python:context.Schema()['Remarks", 244, 21), 11636: (u'rs python', 245, 21), 11812: (u"python:context.widget('Remarks', mode=mode)", 250, 35), 11812: (u"python:context.widget('Remarks', mode=mode)", 250, 35), 12063: (u"python:context.getWorksheetTemplate().getEnableMultipleUseOfInstrument() if context.getWorksheetTemplate() else 'True'", 258, 35), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168047469648 = {u'id': u'wideinterims_analyses', u'class': u'form-control form-control-sm', }
_static_140168047507280 = {u'class': u'form-group form-inline', }
_static_140168047502992 = {u'required': '', u'class': u'mr-2', }
_static_140168047422608 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168047388816 = {u'class': u'input-group-text', }
_static_140168047502672 = {u'class': u'row', }
_static_140168047365392 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168047429392 = {u'class': u'input-group-text', }
_static_140168047437328 = {u'class': u'text-center', }
_static_140168047448592 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168047430352 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'id': u'resultslayout', u'name': u'resultslayout', u'class': u'selectpicker', }
_static_140168047414352 = {u'class': u'input-group-text', }
_static_140168047457488 = {u'href': u"python:context.absolute_url()+'/print'", u'class': u'btn btn-outline-secondary btn-sm print_button', }
_static_140168047533392 = {u'id': u'remarks-widget', u'class': u'col-sm-12 remarks-widget', }
_static_140168047428048 = {u'class': u'input-group-prepend', }
_static_140168047501712 = {u'class': u'required', }
_static_140168047485712 = {u'keyword': u"python:inter['keyword']", u'type': u'hidden', u'id': u"python:'wideinterim_%s_%s' % (an, inter['keyword'])", u'value': u"python:inter['value']", u'name': u"python:inter['title']", }
_static_140168047502608 = {u'id': u'wideinterims_interims', u'class': u'form-control form-control-sm', }
_static_140168047362832 = {u'class': u'row', }
_static_140168047381584 = {u'class': u'input-group-append', }
_static_140168047405968 = {u'class': u'input-group-append', }
_static_140168047420112 = {u'method': u'post', u'class': u'form-inline', u'enctype': u'multipart/form-data', u'id': u'resultslayout_form', u'name': u'resultslayout_form', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047875280 = {u'class': u'row', }
_static_140168047382224 = {u'selected': u"python: context.getAnalyst() == option and 'selected' or ''", u'value': u'python:option', }
_static_140168047536080 = u"python:context.widget('Remarks', mode=mode)"
_static_140168047470992 = {u'class': u'mr-2', }
_static_140168047876496 = {u'class': u'col-sm-12', }
_static_140168047514448 = {u'size': u'6', u'type': u'text', u'id': u'wideinterims_value', u'value': u"python:wideinterims[wideanselected]['interims'][wideinterimselected]['value']", u'class': u'form-control form-control-sm mr-2', }
_static_140168047406608 = {u'selected': u"python: instrument and instrument.UID() == option and 'selected' or ''", u'value': u'python:option', }
_static_140168047521872 = {u'checked': '', u'type': u'checkbox', u'id': u'wideinterims_empty', }
_static_140168047465232 = {u'class': u'wideinterims_bar bg-light table table-borderless table-sm', }
_static_140168047370960 = {u'class': u'input-group-prepend', }
_static_140168047413200 = {u'class': u'input-group-text', }
_static_140168047372432 = {u'class': u'input-group-text', }
_static_140168047468752 = {u'class': u'form-group form-inline', }
_static_140168047398864 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'data-live-search': u'true', u'class': u'instrument selectpicker', }
_static_140168047397136 = {u'class': u'input-group-text', }
_static_140168047390352 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto', }
_static_140168047485520 = {u'class': u'form-group form-inline', }
_static_140168047451216 = {u'class': u'input-group-text', }
_static_140168047374224 = {u'data-style': u'dropdown-toggle btn-sm btn-light border rounded-0', u'data-live-search': u'true', u'class': u'analyst selectpicker', }
_static_140168047483088 = {u'selected': u'python:option==wideanselected', u'value': u'python:option', }
_static_140168047438032 = {u'selected': '', u'value': u'python:option[0]', }
_static_140168047395792 = {u'class': u'input-group-prepend', }
_static_140168047873552 = {u'class': u'documentFirstHeading', }
_static_140168257770128 = {}
_static_140168047523728 = {u'class': u'mx-2', }
_static_140168047531728 = {u'class': u'row', }
_static_140168047514896 = {u'class': u'mr-2', }
_static_140168047449872 = {u'class': u'input-group-prepend', }
_static_140168047507216 = {u'selected': u'python:interim==wideinterimselected', u'value': u'python:interim', }
_static_140168047524752 = {u'id': u'wideinterims_apply', u'class': u'btn btn-outline-secondary btn-sm', }
_static_140168208991440 = __compile_zt_expr
_static_140168047436432 = {u'class': u'input-group input-group-append', }
_static_140168047449488 = {u'class': u'input-group input-group-append', }
_static_140168047872464 = {u'src': u'', }
_static_140168047542416 = {u'type': u'hidden', u'id': u'instrument_multiple_use', u'value': u"python:context.getWorksheetTemplate().getEnableMultipleUseOfInstrument() if context.getWorksheetTemplate() else 'True'", }
_static_140168047444304 = {u'value': u'python:option[0]', }
_static_140168047458768 = {u'class': u'col-sm-12', }
_static_140168047536528 = {u'class': u'fas fa-comment', }
_static_140168047847120 = u'master'
_static_140168047446096 = {u'type': u'submit', u'class': u'btn btn-sm btn-outline-secondary', u'value': u'Apply', u'id': u'resultslayout_button', }
_static_140168047877712 = {u'class': u'table table-sm table-borderless manage_results_header', }
_static_140168047530640 = {u'class': u'col-sm-12', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047847312
            __attrs_140168047847312 = _static_140168257770128
            __previous_i18n_domain_140168047847440 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140168057693600 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b6ab366d0> name=None at 7f7b6cbf3bd0> -> __value
            __value = _static_140168047847120
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047870672
                __attrs_140168047870672 = _static_140168257770128
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047871568
                __attrs_140168047871568 = _static_140168257770128

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab3c9d0> name=None at 7f7b6cbe6490> -> __attrs_140168047872784
                __attrs_140168047872784 = _static_140168047872464

                # <Value u'view/icon | nothing' (16:28)> -> __condition
                __token = 441
                try:
                    __zt_tmp = __attrs_140168047872784
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'view/icon | nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168081540688
                    __default_140168081540688 = _DEFAULT_MARKER

                    # <Substitution u'view/icon' (17:40)> -> __attr_src
                    __token = 502
                    try:
                        __zt_tmp = __attrs_140168047872784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_140168208991440('path', u'view/icon', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((u' src="%s"' % __attr_src))
                    __append(u'/>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab3ce10> name=None at 7f7b6ab3cdd0> -> __attrs_140168047874256
                __attrs_140168047874256 = _static_140168047873552

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="documentFirstHeading">')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047873360
                __default_140168047873360 = _DEFAULT_MARKER

                # <Value u'context/title_or_id' (18:56)> -> __cache_140168047873104
                __token = 571
                try:
                    __zt_tmp = __attrs_140168047874256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047873104 = _static_140168208991440('path', u'context/title_or_id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/title_or_id' (18:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b71c22090> -> __condition
                __expression = __cache_140168047873104

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047873104
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n      </h1>\n    ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047870160
                __attrs_140168047870160 = _static_140168257770128
                __append(u'\n    ')
            _slots = econtext[u'__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047874576
                __attrs_140168047874576 = _static_140168257770128
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab3d4d0> name=None at 7f7b6ab3d490> -> __attrs_140168047875856
                __attrs_140168047875856 = _static_140168047875280

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab3d990> name=None at 7f7b6ab3d910> -> __attrs_140168047877072
                __attrs_140168047877072 = _static_140168047876496

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab3de50> name=None at 7f7b6ab3de10> -> __attrs_140168047362320
                __attrs_140168047362320 = _static_140168047877712

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table class="table table-sm table-borderless manage_results_header">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047363344
                __attrs_140168047363344 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n              <!-- Analyst -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047364624
                __attrs_140168047364624 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac0d10> name=None at 7f7b6aac0cd0> -> __attrs_140168047366032
                __attrs_140168047366032 = _static_140168047365392

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac22d0> name=None at 7f7b6aac2290> -> __attrs_140168047371600
                __attrs_140168047371600 = _static_140168047370960

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac2890> name=None at 7f7b6aac2850> -> __attrs_140168047373072
                __attrs_140168047373072 = _static_140168047372432

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group-text">')
                __stream_140168047372304 = []
                __append_140168047372304 = __stream_140168047372304.append
                __append_140168047372304(u'\n                      Analyst\n                    ')
                __msgid_140168047372304 = __re_whitespace(''.join(__stream_140168047372304)).strip()
                if __msgid_140168047372304:
                    __append(translate(__msgid_140168047372304, mapping=None, default=__msgid_140168047372304, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                  </div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047373456
                __attrs_140168047373456 = _static_140168257770128

                # <Value u'view/is_assignment_allowed' (39:39)> -> __condition
                __token = 1320
                try:
                    __zt_tmp = __attrs_140168047373456
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'view/is_assignment_allowed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aac2f90> name=None at 7f7b6aac2f50> -> __attrs_140168047379664
                    __attrs_140168047379664 = _static_140168047374224
                    __backup_alist_140168047370832 = get('alist', __marker)

                    # <Value u'view/get_analysts' (43:46)> -> __value
                    __token = 1595
                    try:
                        __zt_tmp = __attrs_140168047379664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('path', u'view/get_analysts', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['alist'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select class="analyst selectpicker" data-style="dropdown-toggle btn-sm btn-light border rounded-0" data-live-search="true">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047380816
                    __attrs_140168047380816 = _static_140168257770128
                    __backup_option_140168047365264 = get('option', __marker)

                    # <Value u'alist' (44:50)> -> __iterator
                    __token = 1665
                    try:
                        __zt_tmp = __attrs_140168047380816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'alist', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047380880, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aac4ed0> name=None at 7f7b6aac4e50> -> __attrs_140168047387600
                        __attrs_140168047387600 = _static_140168047382224

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047387024
                        __default_140168047387024 = _DEFAULT_MARKER

                        # <Substitution u'python:option' (45:54)> -> __attr_value
                        __token = 1727
                        try:
                            __zt_tmp = __attrs_140168047387600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'option', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047387280
                        __default_140168047387280 = _DEFAULT_MARKER

                        # <Boolean u"python: context.getAnalyst() == option and 'selected' or ''" (46:56)> -> __attr_selected
                        __token = 1798
                        try:
                            __zt_tmp = __attrs_140168047387600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_140168208991440('python', u" context.getAnalyst() == option and 'selected' or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
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

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047381968
                        __default_140168047381968 = _DEFAULT_MARKER

                        # <Value u'python:alist.getValue(option)' (47:45)> -> __cache_140168047381648
                        __token = 1906
                        try:
                            __zt_tmp = __attrs_140168047387600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047381648 = _static_140168208991440('python', u'alist.getValue(option)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:alist.getValue(option)' (47:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aac4d10> -> __condition
                        __expression = __cache_140168047381648

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047381648
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                      ')
                        ____index_140168047380880 -= 1
                        if (____index_140168047380880 > 0):
                            __append('')
                    if (__backup_option_140168047365264 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140168047365264
                    __append(u'\n                    </select>')
                    if (__backup_alist_140168047370832 is __marker):
                        del econtext['alist']
                    else:
                        econtext['alist'] = __backup_alist_140168047370832
                    __append(u'\n                  </span>')
                __append(u'\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac4c50> name=None at 7f7b6aac2f10> -> __attrs_140168047380176
                __attrs_140168047380176 = _static_140168047381584

                # <Value u'not: view/is_assignment_allowed' (52:39)> -> __condition
                __token = 2122
                try:
                    __zt_tmp = __attrs_140168047380176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('not', u' view/is_assignment_allowed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-append">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aac6890> name=None at 7f7b6aac6850> -> __attrs_140168047389456
                    __attrs_140168047389456 = _static_140168047388816

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-text">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047388624
                    __default_140168047388624 = _DEFAULT_MARKER

                    # <Value u'python:view.get_analysts().getValue(context.getAnalyst())' (54:39)> -> __cache_140168047388304
                    __token = 2246
                    try:
                        __zt_tmp = __attrs_140168047389456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047388304 = _static_140168208991440('python', u'view.get_analysts().getValue(context.getAnalyst())', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:view.get_analysts().getValue(context.getAnalyst())' (54:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aac6710> -> __condition
                    __expression = __cache_140168047388304

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                      Selected Analyst\n                    ')
                    else:
                        __content = __cache_140168047388304
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                  </span>')
                __append(u'\n                </div>\n              </td>\n              <!-- Instrument -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047388048
                __attrs_140168047388048 = _static_140168257770128
                __backup_instrument_140168047362640 = get('instrument', __marker)

                # <Value u'python:context.getInstrument()' (61:41)> -> __value
                __token = 2517
                try:
                    __zt_tmp = __attrs_140168047388048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'context.getInstrument()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['instrument'] = __value

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac6e90> name=None at 7f7b6aac6e50> -> __attrs_140168047395152
                __attrs_140168047395152 = _static_140168047390352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac83d0> name=None at 7f7b6aac8390> -> __attrs_140168047396432
                __attrs_140168047396432 = _static_140168047395792

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac8910> name=None at 7f7b6aac88d0> -> __attrs_140168047397776
                __attrs_140168047397776 = _static_140168047397136

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group-text">')
                __stream_140168047397008 = []
                __append_140168047397008 = __stream_140168047397008.append
                __append_140168047397008(u'\n                      Instrument\n                    ')
                __msgid_140168047397008 = __re_whitespace(''.join(__stream_140168047397008)).strip()
                if __msgid_140168047397008:
                    __append(translate(__msgid_140168047397008, mapping=None, default=__msgid_140168047397008, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                  </div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047398096
                __attrs_140168047398096 = _static_140168257770128

                # <Value u'view/is_assignment_allowed' (68:39)> -> __condition
                __token = 2887
                try:
                    __zt_tmp = __attrs_140168047398096
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'view/is_assignment_allowed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aac8fd0> name=None at 7f7b6aac8f90> -> __attrs_140168047404304
                    __attrs_140168047404304 = _static_140168047398864
                    __backup_instrlist_140168047364880 = get('instrlist', __marker)

                    # <Value u'view/getInstruments' (72:50)> -> __value
                    __token = 3169
                    try:
                        __zt_tmp = __attrs_140168047404304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('path', u'view/getInstruments', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['instrlist'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select class="instrument selectpicker" data-style="dropdown-toggle btn-sm btn-light border rounded-0" data-live-search="true">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047405200
                    __attrs_140168047405200 = _static_140168257770128
                    __backup_option_140168047371856 = get('option', __marker)

                    # <Value u'instrlist' (73:50)> -> __iterator
                    __token = 3241
                    try:
                        __zt_tmp = __attrs_140168047405200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'instrlist', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047405520, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aacae10> name=None at 7f7b6aacadd0> -> __attrs_140168047411984
                        __attrs_140168047411984 = _static_140168047406608

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047411408
                        __default_140168047411408 = _DEFAULT_MARKER

                        # <Substitution u'python:option' (74:54)> -> __attr_value
                        __token = 3307
                        try:
                            __zt_tmp = __attrs_140168047411984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'option', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047411664
                        __default_140168047411664 = _DEFAULT_MARKER

                        # <Boolean u"python: instrument and instrument.UID() == option and 'selected' or ''" (75:56)> -> __attr_selected
                        __token = 3378
                        try:
                            __zt_tmp = __attrs_140168047411984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_140168208991440('python', u" instrument and instrument.UID() == option and 'selected' or ''", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
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

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047406352
                        __default_140168047406352 = _DEFAULT_MARKER

                        # <Value u'python:instrlist.getValue(option)' (76:45)> -> __cache_140168047406032
                        __token = 3497
                        try:
                            __zt_tmp = __attrs_140168047411984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047406032 = _static_140168208991440('python', u'instrlist.getValue(option)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:instrlist.getValue(option)' (76:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aacac50> -> __condition
                        __expression = __cache_140168047406032

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047406032
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                      ')
                        ____index_140168047405520 -= 1
                        if (____index_140168047405520 > 0):
                            __append('')
                    if (__backup_option_140168047371856 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140168047371856
                    __append(u'\n                    </select>')
                    if (__backup_instrlist_140168047364880 is __marker):
                        del econtext['instrlist']
                    else:
                        econtext['instrlist'] = __backup_instrlist_140168047364880
                    __append(u'\n                  </span>')
                __append(u'\n\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aacab90> name=None at 7f7b6aac8f50> -> __attrs_140168047404688
                __attrs_140168047404688 = _static_140168047405968

                # <Value u'not: view/is_assignment_allowed' (82:39)> -> __condition
                __token = 3718
                try:
                    __zt_tmp = __attrs_140168047404688
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('not', u' view/is_assignment_allowed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-append">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aacc7d0> name=None at 7f7b6aacc790> -> __attrs_140168047413840
                    __attrs_140168047413840 = _static_140168047413200

                    # <Value u'python:instrument' (84:41)> -> __condition
                    __token = 3844
                    try:
                        __zt_tmp = __attrs_140168047413840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'instrument', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="input-group-text">')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047413008
                        __default_140168047413008 = _DEFAULT_MARKER

                        # <Value u'python:view.getInstruments().getValue(instrument.UID())' (85:39)> -> __cache_140168047412688
                        __token = 3902
                        try:
                            __zt_tmp = __attrs_140168047413840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047412688 = _static_140168208991440('python', u'view.getInstruments().getValue(instrument.UID())', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:view.getInstruments().getValue(instrument.UID())' (85:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aacc650> -> __condition
                        __expression = __cache_140168047412688

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047412688
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aaccc50> name=None at 7f7b6aaccc10> -> __attrs_140168047414992
                    __attrs_140168047414992 = _static_140168047414352

                    # <Value u'python:not instrument' (87:41)> -> __condition
                    __token = 4059
                    try:
                        __zt_tmp = __attrs_140168047414992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u'not instrument', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="input-group-text">')
                        __stream_140168047414160 = []
                        __append_140168047414160 = __stream_140168047414160.append
                        __append_140168047414160(u'\n                      Not defined\n                    ')
                        __msgid_140168047414160 = __re_whitespace(''.join(__stream_140168047414160)).strip()
                        if __msgid_140168047414160:
                            __append(translate(__msgid_140168047414160, mapping=None, default=__msgid_140168047414160, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>')
                    __append(u'\n                  </span>')
                __append(u'\n\n                </div>\n              </td>')
                if (__backup_instrument_140168047362640 is __marker):
                    del econtext['instrument']
                else:
                    econtext['instrument'] = __backup_instrument_140168047362640
                __append(u'\n              <!-- Layout -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047412368
                __attrs_140168047412368 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aace2d0> name=None at 7f7b6aace310> -> __attrs_140168047421968
                __attrs_140168047421968 = _static_140168047420112

                # <form ... (0:0)
                # --------------------------------------------------------
                __append(u'<form id="resultslayout_form" name="resultslayout_form" class="form-inline" enctype="multipart/form-data" method="post">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aacec90> name=None at 7f7b6aacec50> -> __attrs_140168047423248
                __attrs_140168047423248 = _static_140168047422608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad01d0> name=None at 7f7b6aad0190> -> __attrs_140168047428688
                __attrs_140168047428688 = _static_140168047428048

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad0710> name=None at 7f7b6aad06d0> -> __attrs_140168047430032
                __attrs_140168047430032 = _static_140168047429392

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group-text">')
                __stream_140168047429264 = []
                __append_140168047429264 = __stream_140168047429264.append
                __append_140168047429264(u'\n                        Layout\n                      ')
                __msgid_140168047429264 = __re_whitespace(''.join(__stream_140168047429264)).strip()
                if __msgid_140168047429264:
                    __append(translate(__msgid_140168047429264, mapping=None, default=__msgid_140168047429264, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad0ad0> name=None at 7f7b6aad0490> -> __attrs_140168047436112
                __attrs_140168047436112 = _static_140168047430352

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select id="resultslayout" data-style="dropdown-toggle btn-sm btn-light border rounded-0" class="selectpicker" name="resultslayout">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047436880
                __attrs_140168047436880 = _static_140168257770128
                __backup_option_140168047405328 = get('option', __marker)

                # <Value u'python:view.layout_displaylist.items()' (112:55)> -> __iterator
                __token = 5131
                try:
                    __zt_tmp = __attrs_140168047436880
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('python', u'view.layout_displaylist.items()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168047437072, ) = getitem('repeat')(u'option', __iterator)
                econtext['option'] = None
                for __item in __iterator:
                    econtext['option'] = __item
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aad28d0> name=None at 7f7b6aad2890> -> __attrs_140168047439056
                    __attrs_140168047439056 = _static_140168047438032

                    # <Value u'python: option[0] == context.getResultsLayout()' (113:56)> -> __condition
                    __token = 5228
                    try:
                        __zt_tmp = __attrs_140168047439056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u' option[0] == context.getResultsLayout()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option selected')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047438736
                        __default_140168047438736 = _DEFAULT_MARKER

                        # <Substitution u'python:option[0]' (114:54)> -> __attr_value
                        __token = 5331
                        try:
                            __zt_tmp = __attrs_140168047439056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'option[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047437840
                        __default_140168047437840 = _DEFAULT_MARKER

                        # <Value u'python:option[1]' (115:45)> -> __cache_140168047437456
                        __token = 5394
                        try:
                            __zt_tmp = __attrs_140168047439056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047437456 = _static_140168208991440('python', u'option[1]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:option[1]' (115:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aad2750> -> __condition
                        __expression = __cache_140168047437456

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                        ')
                        else:
                            __content = __cache_140168047437456
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>')
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aad4150> name=None at 7f7b6aad4110> -> __attrs_140168047445008
                    __attrs_140168047445008 = _static_140168047444304

                    # <Value u'python: option[0] != context.getResultsLayout()' (117:47)> -> __condition
                    __token = 5494
                    try:
                        __zt_tmp = __attrs_140168047445008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('python', u' option[0] != context.getResultsLayout()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047444688
                        __default_140168047444688 = _DEFAULT_MARKER

                        # <Substitution u'python:option[0]' (118:54)> -> __attr_value
                        __token = 5597
                        try:
                            __zt_tmp = __attrs_140168047445008
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'option[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047444112
                        __default_140168047444112 = _DEFAULT_MARKER

                        # <Value u'python:option[1]' (119:45)> -> __cache_140168047439568
                        __token = 5660
                        try:
                            __zt_tmp = __attrs_140168047445008
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047439568 = _static_140168208991440('python', u'option[1]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:option[1]' (119:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aad2f90> -> __condition
                        __expression = __cache_140168047439568

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047439568
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>')
                    __append(u'\n                      ')
                    ____index_140168047437072 -= 1
                    if (____index_140168047437072 > 0):
                        __append('')
                if (__backup_option_140168047405328 is __marker):
                    del econtext['option']
                else:
                    econtext['option'] = __backup_option_140168047405328
                __append(u'\n                    </select>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad2290> name=None at 7f7b6aad2190> -> __attrs_140168047445456
                __attrs_140168047445456 = _static_140168047436432

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-append">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad4850> name=None at 7f7b6aad4890> -> __attrs_140168047447632
                __attrs_140168047447632 = _static_140168047446096

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="btn btn-sm btn-outline-secondary" type="submit" id="resultslayout_button" value="Apply"/>\n                    </div>\n                  </div>\n                </form>\n              </td>\n              <!-- Print -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad2610> name=None at 7f7b6aacef50> -> __attrs_140168047447888
                __attrs_140168047447888 = _static_140168047437328

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="text-center">\n                ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad5210> name=None at 7f7b6aad51d0> -> __attrs_140168047449232
                __attrs_140168047449232 = _static_140168047448592

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad5710> name=None at 7f7b6aad56d0> -> __attrs_140168047450512
                __attrs_140168047450512 = _static_140168047449872

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad5c50> name=None at 7f7b6aad5c10> -> __attrs_140168047451856
                __attrs_140168047451856 = _static_140168047451216

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="input-group-text">')
                __stream_140168047451088 = []
                __append_140168047451088 = __stream_140168047451088.append
                __append_140168047451088(u'\n                      Print Worksheet\n                    ')
                __msgid_140168047451088 = __re_whitespace(''.join(__stream_140168047451088)).strip()
                if __msgid_140168047451088:
                    __append(translate(__msgid_140168047451088, mapping=None, default=__msgid_140168047451088, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                  </div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad5590> name=None at 7f7b6aad59d0> -> __attrs_140168047456784
                __attrs_140168047456784 = _static_140168047449488

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-append">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad74d0> name=None at 7f7b6aad7490> -> __attrs_140168047458512
                __attrs_140168047458512 = _static_140168047457488

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="btn btn-outline-secondary btn-sm print_button"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047458192
                __default_140168047458192 = _DEFAULT_MARKER

                # <Substitution u"python:context.absolute_url()+'/print'" (140:44)> -> __attr_href
                __token = 6609
                try:
                    __zt_tmp = __attrs_140168047458512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u"context.absolute_url()+'/print'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')
                __stream_140168047457360 = []
                __append_140168047457360 = __stream_140168047457360.append
                __append_140168047457360(u'\n                      Print\n                    ')
                __msgid_140168047457360 = __re_whitespace(''.join(__stream_140168047457360)).strip()
                if __msgid_140168047457360:
                    __append(translate(__msgid_140168047457360, mapping=None, default=__msgid_140168047457360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n                  </div>\n                </div>\n              </td>\n            </tr>\n          </table>\n        </div>\n      </div>\n\n      <!-- Wide Interim -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aac0310> name=None at 7f7b6ab3d810> -> __attrs_140168047449296
                __attrs_140168047449296 = _static_140168047362832

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad79d0> name=None at 7f7b6aad7350> -> __attrs_140168047459344
                __attrs_140168047459344 = _static_140168047458768

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047460048
                __attrs_140168047460048 = _static_140168257770128
                __backup_wideinterims_140168047871824 = get('wideinterims', __marker)

                # <Value u'view/get_wide_interims' (156:49)> -> __value
                __token = 7087
                try:
                    __zt_tmp = __attrs_140168047460048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/get_wide_interims', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['wideinterims'] = __value

                # <Value u'python:wideinterims' (157:39)> -> __condition
                __token = 7151
                try:
                    __zt_tmp = __attrs_140168047460048
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'wideinterims', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aad9310> name=None at 7f7b6aad92d0> -> __attrs_140168047465872
                    __attrs_140168047465872 = _static_140168047465232
                    __backup_wideanselected_140168047364304 = get('wideanselected', __marker)

                    # <Value u'python:wideinterims.keys()[0]' (158:46)> -> __value
                    __token = 7219
                    try:
                        __zt_tmp = __attrs_140168047465872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u'wideinterims.keys()[0]', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['wideanselected'] = __value
                    __backup_wideinterimselected_140168047877584 = get('wideinterimselected', __marker)

                    # <Value u"python:wideinterims[wideanselected]['interims'].keys()[0]" (159:50)> -> __value
                    __token = 7300
                    try:
                        __zt_tmp = __attrs_140168047465872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u"wideinterims[wideanselected]['interims'].keys()[0]", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['wideinterimselected'] = __value

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<table class="wideinterims_bar bg-light table table-borderless table-sm">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047467088
                    __attrs_140168047467088 = _static_140168257770128

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n                <!-- Autofill -->\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047468048
                    __attrs_140168047468048 = _static_140168257770128

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aada0d0> name=None at 7f7b6aada090> -> __attrs_140168047469392
                    __attrs_140168047469392 = _static_140168047468752

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="form-group form-inline">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047470224
                    __attrs_140168047470224 = _static_140168257770128

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label>\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aada990> name=None at 7f7b6aada950> -> __attrs_140168047471568
                    __attrs_140168047471568 = _static_140168047470992

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="mr-2">')
                    __stream_140168047470800 = []
                    __append_140168047470800 = __stream_140168047470800.append
                    __append_140168047470800(u'Autofill')
                    __msgid_140168047470800 = __re_whitespace(''.join(__stream_140168047470800)).strip()
                    if __msgid_140168047470800:
                        __append(translate(__msgid_140168047470800, mapping=None, default=__msgid_140168047470800, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n                    </label>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aada450> name=None at 7f7b6aada6d0> -> __attrs_140168047480976
                    __attrs_140168047480976 = _static_140168047469648

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select id="wideinterims_analyses" class="form-control form-control-sm">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047481744
                    __attrs_140168047481744 = _static_140168257770128
                    __backup_option_140168047439184 = get('option', __marker)

                    # <Value u'python:wideinterims.keys()' (169:50)> -> __iterator
                    __token = 7849
                    try:
                        __zt_tmp = __attrs_140168047481744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('python', u'wideinterims.keys()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047482000, ) = getitem('repeat')(u'option', __iterator)
                    econtext['option'] = None
                    for __item in __iterator:
                        econtext['option'] = __item
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aadd8d0> name=None at 7f7b6aadd890> -> __attrs_140168047484304
                        __attrs_140168047484304 = _static_140168047483088

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047483728
                        __default_140168047483728 = _DEFAULT_MARKER

                        # <Substitution u'python:option' (170:54)> -> __attr_value
                        __token = 7932
                        try:
                            __zt_tmp = __attrs_140168047484304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'option', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047483984
                        __default_140168047483984 = _DEFAULT_MARKER

                        # <Boolean u'python:option==wideanselected' (171:56)> -> __attr_selected
                        __token = 8003
                        try:
                            __zt_tmp = __attrs_140168047484304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_140168208991440('python', u'option==wideanselected', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
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

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047482832
                        __default_140168047482832 = _DEFAULT_MARKER

                        # <Value u"python:wideinterims[option]['analysis']" (172:45)> -> __cache_140168047482512
                        __token = 8081
                        try:
                            __zt_tmp = __attrs_140168047484304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047482512 = _static_140168208991440('python', u"wideinterims[option]['analysis']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:wideinterims[option]['analysis']" (172:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aadd710> -> __condition
                        __expression = __cache_140168047482512

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047482512
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                      ')
                        ____index_140168047482000 -= 1
                        if (____index_140168047482000 > 0):
                            __append('')
                    if (__backup_option_140168047439184 is __marker):
                        del econtext['option']
                    else:
                        econtext['option'] = __backup_option_140168047439184
                    __append(u'\n                    </select>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047481616
                    __attrs_140168047481616 = _static_140168257770128
                    __backup_an_140168047381520 = get('an', __marker)

                    # <Value u'python:wideinterims.keys()' (175:51)> -> __iterator
                    __token = 8243
                    try:
                        __zt_tmp = __attrs_140168047481616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('python', u'wideinterims.keys()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047482256, ) = getitem('repeat')(u'an', __iterator)
                    econtext['an'] = None
                    for __item in __iterator:
                        econtext['an'] = __item
                        __append(u'\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047484880
                        __attrs_140168047484880 = _static_140168257770128
                        __backup_inter_140168047471824 = get('inter', __marker)

                        # <Value u"python:wideinterims[an]['interims'].values()" (176:55)> -> __iterator
                        __token = 8327
                        try:
                            __zt_tmp = __attrs_140168047484880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140168208991440('python', u"wideinterims[an]['interims'].values()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        (__iterator, ____index_140168047485200, ) = getitem('repeat')(u'inter', __iterator)
                        econtext['inter'] = None
                        for __item in __iterator:
                            econtext['inter'] = __item
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f7b6aade310> name=None at 7f7b6aade350> -> __attrs_140168047487888
                            __attrs_140168047487888 = _static_140168047485712

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047486864
                            __default_140168047486864 = _DEFAULT_MARKER

                            # <Substitution u"python:'wideinterim_%s_%s' % (an, inter['keyword'])" (178:49)> -> __attr_id
                            __token = 8468
                            try:
                                __zt_tmp = __attrs_140168047487888
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140168208991440('python', u"'wideinterim_%s_%s' % (an, inter['keyword'])", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047487120
                            __default_140168047487120 = _DEFAULT_MARKER

                            # <Substitution u"python:inter['title']" (179:50)> -> __attr_name
                            __token = 8571
                            try:
                                __zt_tmp = __attrs_140168047487888
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_name = _static_140168208991440('python', u"inter['title']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_name is not None):
                                __append((u' name="%s"' % __attr_name))

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047487376
                            __default_140168047487376 = _DEFAULT_MARKER

                            # <Substitution u"python:inter['value']" (180:50)> -> __attr_value
                            __token = 8645
                            try:
                                __zt_tmp = __attrs_140168047487888
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140168208991440('python', u"inter['value']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047487632
                            __default_140168047487632 = _DEFAULT_MARKER

                            # <Substitution u"python:inter['keyword']" (181:51)> -> __attr_keyword
                            __token = 8721
                            try:
                                __zt_tmp = __attrs_140168047487888
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_keyword = _static_140168208991440('python', u"inter['keyword']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            __attr_keyword = __quote(__attr_keyword, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_keyword is not None):
                                __append((u' keyword="%s"' % __attr_keyword))
                            __append(u'/>\n                      ')
                            ____index_140168047485200 -= 1
                            if (____index_140168047485200 > 0):
                                __append('')
                        if (__backup_inter_140168047471824 is __marker):
                            del econtext['inter']
                        else:
                            econtext['inter'] = __backup_inter_140168047471824
                        __append(u'\n                    ')
                        ____index_140168047482256 -= 1
                        if (____index_140168047482256 > 0):
                            __append('')
                    if (__backup_an_140168047381520 is __marker):
                        del econtext['an']
                    else:
                        econtext['an'] = __backup_an_140168047381520
                    __append(u'\n                  </div>\n                </td>\n                <!-- Field -->\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047481040
                    __attrs_140168047481040 = _static_140168257770128

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aade250> name=None at 7f7b6aade1d0> -> __attrs_140168047488528
                    __attrs_140168047488528 = _static_140168047485520
                    __backup_interims_140168047380112 = get('interims', __marker)

                    # <Value u"python:wideinterims[wideanselected]['interims'].keys()" (189:43)> -> __value
                    __token = 9033
                    try:
                        __zt_tmp = __attrs_140168047488528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u"wideinterims[wideanselected]['interims'].keys()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['interims'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="form-group form-inline">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae2190> name=None at 7f7b6aae2150> -> __attrs_140168047502288
                    __attrs_140168047502288 = _static_140168047501712

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label class="required">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae2690> name=None at 7f7b6aae26d0> -> __attrs_140168047503952
                    __attrs_140168047503952 = _static_140168047502992

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="mr-2" required>')
                    __stream_140168047502864 = []
                    __append_140168047502864 = __stream_140168047502864.append
                    __append_140168047502864(u'Field')
                    __msgid_140168047502864 = __re_whitespace(''.join(__stream_140168047502864)).strip()
                    if __msgid_140168047502864:
                        __append(translate(__msgid_140168047502864, mapping=None, default=__msgid_140168047502864, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n                    </label>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae2510> name=None at 7f7b6aae2410> -> __attrs_140168047505040
                    __attrs_140168047505040 = _static_140168047502608

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select id="wideinterims_interims" class="form-control form-control-sm">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047505872
                    __attrs_140168047505872 = _static_140168257770128
                    __backup_interim_140168047439504 = get('interim', __marker)

                    # <Value u'interims' (194:51)> -> __iterator
                    __token = 9389
                    try:
                        __zt_tmp = __attrs_140168047505872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'interims', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168047506128, ) = getitem('repeat')(u'interim', __iterator)
                    econtext['interim'] = None
                    for __item in __iterator:
                        econtext['interim'] = __item
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aae3710> name=None at 7f7b6aae3690> -> __attrs_140168047508432
                        __attrs_140168047508432 = _static_140168047507216

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047507856
                        __default_140168047507856 = _DEFAULT_MARKER

                        # <Substitution u'python:interim' (195:54)> -> __attr_value
                        __token = 9454
                        try:
                            __zt_tmp = __attrs_140168047508432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('python', u'interim', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047508112
                        __default_140168047508112 = _DEFAULT_MARKER

                        # <Boolean u'python:interim==wideinterimselected' (196:56)> -> __attr_selected
                        __token = 9526
                        try:
                            __zt_tmp = __attrs_140168047508432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_140168208991440('python', u'interim==wideinterimselected', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
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

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047506960
                        __default_140168047506960 = _DEFAULT_MARKER

                        # <Value u"python:wideinterims[wideanselected]['interims'][interim]['title']" (197:45)> -> __cache_140168047506640
                        __token = 9610
                        try:
                            __zt_tmp = __attrs_140168047508432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047506640 = _static_140168208991440('python', u"wideinterims[wideanselected]['interims'][interim]['title']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:wideinterims[wideanselected]['interims'][interim]['title']" (197:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aae3550> -> __condition
                        __expression = __cache_140168047506640

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047506640
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n                      ')
                        ____index_140168047506128 -= 1
                        if (____index_140168047506128 > 0):
                            __append('')
                    if (__backup_interim_140168047439504 is __marker):
                        del econtext['interim']
                    else:
                        econtext['interim'] = __backup_interim_140168047439504
                    __append(u'\n                    </select>\n                  </div>')
                    if (__backup_interims_140168047380112 is __marker):
                        del econtext['interims']
                    else:
                        econtext['interims'] = __backup_interims_140168047380112
                    __append(u'\n                </td>\n                <!-- Field -->\n                ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047484816
                    __attrs_140168047484816 = _static_140168257770128

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae3750> name=None at 7f7b6aae33d0> -> __attrs_140168047509136
                    __attrs_140168047509136 = _static_140168047507280

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="form-group form-inline">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047514128
                    __attrs_140168047514128 = _static_140168257770128

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label>\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae5510> name=None at 7f7b6aae54d0> -> __attrs_140168047515472
                    __attrs_140168047515472 = _static_140168047514896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="mr-2">')
                    __stream_140168047514704 = []
                    __append_140168047514704 = __stream_140168047514704.append
                    __append_140168047514704(u'Value')
                    __msgid_140168047514704 = __re_whitespace(''.join(__stream_140168047514704)).strip()
                    if __msgid_140168047514704:
                        __append(translate(__msgid_140168047514704, mapping=None, default=__msgid_140168047514704, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n                    </label>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae5350> name=None at 7f7b6aae5790> -> __attrs_140168047517520
                    __attrs_140168047517520 = _static_140168047514448

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input id="wideinterims_value" class="form-control form-control-sm mr-2" type="text" size="6"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047517264
                    __default_140168047517264 = _DEFAULT_MARKER

                    # <Substitution u"python:wideinterims[wideanselected]['interims'][wideinterimselected]['value']" (212:48)> -> __attr_value
                    __token = 10270
                    try:
                        __zt_tmp = __attrs_140168047517520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('python', u"wideinterims[wideanselected]['interims'][wideinterimselected]['value']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae7050> name=None at 7f7b6aae7110> -> __attrs_140168047523216
                    __attrs_140168047523216 = _static_140168047521872

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<input type='checkbox' id='wideinterims_empty' checked>\n                    ")

                    # <Static value=<_ast.Dict object at 0x7f7b6aae7790> name=None at 7f7b6aae7750> -> __attrs_140168047524304
                    __attrs_140168047524304 = _static_140168047523728

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="mx-2">')
                    __stream_140168047523472 = []
                    __append_140168047523472 = __stream_140168047523472.append
                    __append_140168047523472(u'Only to empty or zero fields')
                    __msgid_140168047523472 = __re_whitespace(''.join(__stream_140168047523472)).strip()
                    if __msgid_140168047523472:
                        __append(translate(__msgid_140168047523472, mapping=None, default=__msgid_140168047523472, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aae7b90> name=None at 7f7b6aae7b50> -> __attrs_140168047525712
                    __attrs_140168047525712 = _static_140168047524752

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<button id="wideinterims_apply" class="btn btn-outline-secondary btn-sm">')
                    __stream_140168047524560 = []
                    __append_140168047524560 = __stream_140168047524560.append
                    __append_140168047524560(u'Apply')
                    __msgid_140168047524560 = __re_whitespace(''.join(__stream_140168047524560)).strip()
                    if __msgid_140168047524560:
                        __append(translate(__msgid_140168047524560, mapping=None, default=__msgid_140168047524560, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</button>\n                  </div>\n                </td>\n              </tr>\n            </table>')
                    if (__backup_wideinterimselected_140168047877584 is __marker):
                        del econtext['wideinterimselected']
                    else:
                        econtext['wideinterimselected'] = __backup_wideinterimselected_140168047877584
                    if (__backup_wideanselected_140168047364304 is __marker):
                        del econtext['wideanselected']
                    else:
                        econtext['wideanselected'] = __backup_wideanselected_140168047364304
                    __append(u'\n          ')
                if (__backup_wideinterims_140168047871824 is __marker):
                    del econtext['wideinterims']
                else:
                    econtext['wideinterims'] = __backup_wideinterims_140168047871824
                __append(u'\n        </div>\n      </div>\n\n      <!-- Analyses Listing Table -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047468368
                __attrs_140168047468368 = _static_140168257770128
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aae2550> name=None at 7f7b6aae2050> -> __attrs_140168047523280
                __attrs_140168047523280 = _static_140168047502672

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6aae9290> name=None at 7f7b6aae9210> -> __attrs_140168047531216
                __attrs_140168047531216 = _static_140168047530640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047532496
                __attrs_140168047532496 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047532368
                __default_140168047532368 = _DEFAULT_MARKER

                # <Value u'view/Analyses/contents_table' (232:41)> -> __cache_140168047532048
                __token = 11067
                try:
                    __zt_tmp = __attrs_140168047532496
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047532048 = _static_140168208991440('path', u'view/Analyses/contents_table', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/Analyses/contents_table' (232:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aae9890> -> __condition
                __expression = __cache_140168047532048

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168047532048
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n          </div>\n        </div>\n      \n\n      <!-- Remarks Widget\n           https://github.com/senaite/senaite.core/pull/920 -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aae96d0> name=None at 7f7b6aae7f90> -> __attrs_140168047532752
                __attrs_140168047532752 = _static_140168047531728

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aae9d50> name=None at 7f7b6aae9d10> -> __attrs_140168047534416
                __attrs_140168047534416 = _static_140168047533392
                __backup_checkPermission_140168047871248 = get('checkPermission', __marker)

                # <Value u'nocall: context/portal_membership/checkPermission' (242:41)> -> __value
                __token = 11391
                try:
                    __zt_tmp = __attrs_140168047534416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('nocall', u' context/portal_membership/checkPermission', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['checkPermission'] = __value
                __backup_mode_140168047872208 = get('mode', __marker)

                # <Value u"python:'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view'" (243:21)> -> __value
                __token = 11463
                try:
                    __zt_tmp = __attrs_140168047534416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"'edit' if checkPermission('senaite.core: Field: Edit Remarks', context) else 'view'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['mode'] = __value
                __backup_field_140168047363664 = get('field', __marker)

                # <Value u"python:context.Schema()['Remarks']" (244:21)> -> __value
                __token = 11577
                try:
                    __zt_tmp = __attrs_140168047534416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u"context.Schema()['Remarks']", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['field'] = __value
                __backup_errors_140168047379792 = get('errors', __marker)

                # <Value u'python:{}' (245:21)> -> __value
                __token = 11636
                try:
                    __zt_tmp = __attrs_140168047534416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('python', u'{}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['errors'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="remarks-widget" class="col-sm-12 remarks-widget">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047535760
                __attrs_140168047535760 = _static_140168257770128

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h3>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaea990> name=None at 7f7b6aaea910> -> __attrs_140168047537168
                __attrs_140168047537168 = _static_140168047536528

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-comment"></i>\n            ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047537808
                __attrs_140168047537808 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168047537488 = []
                __append_140168047537488 = __stream_140168047537488.append
                __append_140168047537488(u'Remarks')
                __msgid_140168047537488 = __re_whitespace(''.join(__stream_140168047537488)).strip()
                if __msgid_140168047537488:
                    __append(translate(__msgid_140168047537488, mapping=None, default=__msgid_140168047537488, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n          </h3>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047542352
                __attrs_140168047542352 = _static_140168257770128
                __backup_macroname_140168056383440 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b6aaea7d0> name=None at 7f7b6aaeaed0> -> __value
                __value = _static_140168047536080
                econtext['macroname'] = __value

                # <Value u"python:context.widget('Remarks', mode=mode)" (250:35)> -> __macro
                __token = 11812
                try:
                    __zt_tmp = __attrs_140168047542352
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140168208991440('python', u"context.widget('Remarks', mode=mode)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __token = 11812
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140168056383440 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140168056383440
                __append(u'\n        </div>')
                if (__backup_errors_140168047379792 is __marker):
                    del econtext['errors']
                else:
                    econtext['errors'] = __backup_errors_140168047379792
                if (__backup_field_140168047363664 is __marker):
                    del econtext['field']
                else:
                    econtext['field'] = __backup_field_140168047363664
                if (__backup_mode_140168047872208 is __marker):
                    del econtext['mode']
                else:
                    econtext['mode'] = __backup_mode_140168047872208
                if (__backup_checkPermission_140168047871248 is __marker):
                    del econtext['checkPermission']
                else:
                    econtext['checkPermission'] = __backup_checkPermission_140168047871248
                __append(u'\n      </div>\n      <!-- /Remarks Widget -->\n\n      <!-- XXX: Where is this used? -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aaec090> name=None at 7f7b6aaec110> -> __attrs_140168047543824
                __attrs_140168047543824 = _static_140168047542416

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" id="instrument_multiple_use"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047543568
                __default_140168047543568 = _DEFAULT_MARKER

                # <Substitution u"python:context.getWorksheetTemplate().getEnableMultipleUseOfInstrument() if context.getWorksheetTemplate() else 'True'" (258:35)> -> __attr_value
                __token = 12063
                try:
                    __zt_tmp = __attrs_140168047543824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140168208991440('python', u"context.getWorksheetTemplate().getEnableMultipleUseOfInstrument() if context.getWorksheetTemplate() else 'True'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'/>\n\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140168047847312
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168057693600 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168057693600
            __i18n_domain = __previous_i18n_domain_140168047847440
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }