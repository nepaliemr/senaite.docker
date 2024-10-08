# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.databox/src/senaite/databox/browser/templates/databox_controls.pt'

__tokens = {380: (u'string:${here/absolute_url}/@@update', 12, 31), 2278: (u'view/get_catalog_sort_indexes', 74, 43), 2358: (u'index', 75, 48), 2373: (u" python:context.sort_on == index and 'selected' or '", 75, 63), 2468: (u'index', 76, 39), 3089: (u'here/limit', 94, 43), 3504: (u'here/sort_reversed', 105, 45), 3731: (u'here/sort_reversed', 110, 36), 4496: (u'view/get_catalog_date_indexes', 130, 43), 4576: (u'index', 131, 48), 4591: (u" python:context.date_index == index and 'selected' or '", 131, 63), 4689: (u'index', 132, 39), 5238: (u'python:view.date_from', 148, 43), 5767: (u'here/date_to', 162, 41), 5824: (u'python:view.date_to', 163, 43), 6438: (u'view/get_advanced_query', 178, 34), 6494: (u'python:sorted(query, reverse=1)', 179, 30), 7035: (u'view/get_catalog_indexes', 191, 47), 7114: (u'index', 192, 52), 7129: (u" python:index == q and 'selected' or '", 192, 67), 7214: (u'index', 193, 43), 7822: (u'python:query[q]', 210, 47), 10496: (u'python:view.columns', 269, 36), 10553: (u'columns', 270, 35), 11180: (u"python:columns[column].get('title')", 284, 48), 11945: (u'view/get_schema_fields', 300, 49), 12024: (u'field', 301, 54), 12039: (u" python:field == columns.get(column).get('column') and 'selected' or '", 301, 69), 12158: (u'field', 302, 45), 12440: (u'python:view.get_reference_columns(column)', 311, 36), 12847: (u'ref/type', 318, 48), 13158: (u'ref/fields', 325, 44), 13225: (u'key', 326, 54), 13238: (u" python:key == ref.get('key') and 'selected' or '", 326, 67), 13336: (u'key', 327, 45), 14717: (u"python:columns[column].get('code')", 362, 48), 15518: (u'view/get_converters', 378, 53), 15589: (u'converter/name', 379, 49), 15616: (u' converter/descriptio', 379, 76), 15694: (u'name', 380, 54), 15753: (u' converter/descriptio', 381, 53), 15832: (u"d python:name == columns[column].get('converter') and 'selected' or ", 382, 55), 15950: (u'name', 383, 45), 16385: (u"python:request.get('debug', False)", 401, 29), 16454: (u'view/widgets', 402, 33), 16560: (u'widget/label', 404, 32), 16673: (u'widget/value', 407, 61), 16970: (u'view/databox/query_type', 416, 51), 17274: (u'view/databox/get_query_catalog', 425, 51), 17642: (u'view/databox/query', 436, 51), 17901: (u'request/tab|string:query', 446, 72), 17964: (u'context/@@authenticator/authenticator', 447, 34), 18102: (u'python:False', 451, 24), 18166: (u'view/settings', 453, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240906802640 = {u'class': u'input-group-text', }
_static_140241087907024 = __compile_zt_expr
_static_140240907586384 = {u'class': u'input-group-prepend', }
_static_140240906681040 = {u'class': u'col-auto', }
_static_140240906464848 = {u'checked': u'here/sort_reversed', u'name': u'senaite.databox.sort_reversed:boolean', u'value': u'selected', u'id': u'field-sort_reversed', u'type': u'checkbox', u'class': u'form-check-input', }
_static_140240884110480 = {u'class': u'ml-1', }
_static_140240884152784 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140240884119184 = {u'class': u'text-nowrap font-weight-bold pr-1', }
_static_140240906675216 = {u'class': u'form-text text-muted', }
_static_140240884084240 = {u'class': u'input-group input-group-sm mb-2', }
_static_140240906766352 = {u'class': u'input-group mb-2', }
_static_140240884157328 = {u'class': u'font-weight-bold text-nowrap align-top mr-2', }
_static_140240906623504 = {u'id': u'columns-list', u'class': u'columns col-auto list-unstyled', }
_static_140240884107792 = {u'style': u'max-width:225px', u'class': u'flex-fill mr-2', }
_static_140240884224080 = {u'type': u'submit', u'class': u'btn btn-sm btn-primary', u'value': u'Update', u'name': u'form.buttons.save', }
_static_140240906930192 = {u'class': u'input-group-text', }
_static_140240906190800 = {u'class': u'tab-content mt-3', }
_static_140240884105680 = {u'class': u'ml-1', }
_static_140240917073744 = {u'role': u'tablist', u'class': u'nav nav-tabs', u'id': u'databox-edit', }
_static_140240884135376 = {u'class': u'input-group-prepend', }
_static_140240906190096 = {u'data-toggle': u'tab', u'href': u'#info', u'role': u'tab', u'class': u'nav-link', u'id': u'info-tab', }
_static_140240907084432 = {u'id': u'advanced-queries', u'class': u'col-auto list-unstyled m-0', }
_static_140240906737744 = {u'class': u'form-control', u'name': u'senaite.databox.advanced_query.index:records', }
_static_140240906453072 = {u'data-toggle': u'tab', u'href': u'#advanced-query', u'role': u'tab', u'class': u'nav-link', u'id': u'advanced-query-tab', }
_static_140240906739664 = {u'class': u'input-group-text', }
_static_140240906119824 = {u'class': u'input-group-text', }
_static_140240906136016 = {u'class': u'form-control', u'name': u'senaite.databox.sort_on', }
_static_140240906206992 = {u'class': u'col-auto', }
_static_140240884177040 = {u'class': u'fas fa-arrow-right', }
_static_140240906947216 = {u'class': u'input-group-prepend', }
_static_140240884099792 = {u'class': u'del_column btn btn-sm btn-outline-danger', u'title': u'Delete column', }
_static_140240884114256 = {u'class': u'input-group-prepend', }
_static_140240884272336 = {u'class': u'flex mr-2', }
_static_140240906946448 = {u'type': u'text', u'class': u'form-control', u'value': u"python:columns[column].get('title')", u'name': u'senaite.databox.columns.title:records', }
_static_140240884136656 = {u'class': u'input-group-text', }
_static_140240906680848 = {u'class': u'input-group mb-2', }
_static_140240906558864 = {u'type': u'checkbox', u'class': u'mr-2', u'value': u'1', u'name': u'senaite.databox.advanced_query.delete:bool:records', }
_static_140240884078480 = {u'class': u'table-borderless mb-4', }
_static_140240906613456 = {u'type': u'date', u'class': u'form-control', u'value': u'python:view.date_from', u'name': u'senaite.databox.date_from', }
_static_140240907005776 = {u'class': u'input-group-append', }
_static_140240884180368 = {u'class': u'text-dark', }
_static_140240907629392 = {u'class': u'ml-1', }
_static_140240884109392 = {u'class': u'fas fa-compress', }
_static_140240906946320 = {u'class': u'input-group-text', }
_static_140240907586256 = {u'class': u'input-group input-group-sm mb-2', }
_static_140240906120784 = {u'class': u'form-control', u'name': u'senaite.databox.columns.refs:list:records', }
_static_140240906455184 = {u'role': u'presentation', u'class': u'nav-item', }
_static_140240907062800 = {u'data-toggle': u'tab', u'href': u'#query', u'role': u'tab', u'class': u'nav-link active', u'id': u'query-tab', }
_static_140241133802128 = {}
_static_140240884134096 = {u'class': u'input-group input-group-sm mb-2', }
_static_140240906463504 = {u'class': u'form-check mb-2', }
_static_140240906675920 = {u'class': u'form-text text-muted mb-2', }
_static_140240884082960 = {u'class': u'flex-fill mr-2', }
_static_140240884153232 = {u'class': u'font-weight-bold text-nowrap align-top mr-2', }
_static_140240906622288 = {u'role': u'tabpanel', u'class': u'tab-pane fade', u'id': u'info', }
_static_140240884182800 = {u'class': u'font-weight-bold text-nowrap align-top mr-2', }
_static_140240906802192 = {u'class': u'input-group-prepend', }
_static_140240884115536 = {u'class': u'input-group-text', }
_static_140240906135440 = {u'class': u'input-group-text', }
_static_140240907016400 = {u'class': u'flex-fill mr-2', }
_static_140240884155792 = {u'class': u'text-dark', }
_static_140240907018704 = {u'class': u'flex-fill mr-2', }
_static_140240906122960 = {u'role': u'presentation', u'class': u'nav-item', }
_static_140240884081360 = {u'class': u'fas fa-minus', }
_static_140240884189264 = {u'class': u'text-dark', }
_static_140240884097232 = {u'class': u'd-flex text-nowrap', }
_static_140240907113296 = {u'class': u'input-group-text', }
_static_140240906680016 = {u'class': u'form-check-label', u'for': u'field-sort_reversed', }
_static_140240906767824 = {u'class': u'input-group-prepend', }
_static_140240907113168 = {u'class': u'input-group-prepend', }
_static_140240906647312 = {u'class': u'form-text text-muted', }
_static_140240906489168 = {u'style': u'width:75px', u'name': u'senaite.databox.limit:int', u'min': u'1', u'value': u'here/limit', u'id': u'field-limit', u'type': u'number', u'class': u'form-control', }
_static_140240906117264 = {u'class': u'input-group input-group-sm mb-2', }
_static_140240907017872 = {u'class': u'input-group mb-2', }
_static_140240907049296 = {u'class': u'form-text text-muted', }
_static_140240907195472 = {u'class': u'ml-1', }
_static_140240907584336 = {u'class': u'flex-fill mr-2', }
_static_140240906621136 = {u'class': u'form-row', }
_static_140240884270608 = {u'selected': u"python:key == ref.get('key') and 'selected' or ''", u'value': u'key', }
_static_140240907019408 = {u'selected': u"python:index == q and 'selected' or ''", u'value': u'index', }
_static_140240906550160 = {u'type': u'hidden', u'name': u'senaite.databox.sort_reversed:boolean', u'value': u'', }
_static_140240884218192 = {u'class': u'databox', }
_static_140240907195216 = {u'class': u'fas fa-tag', }
_static_140240907629200 = {u'class': u'fas fa-database', }
_static_140240896378384 = set([])
_static_140240907086608 = {u'class': u'advanced-query d-flex flex-wrap p-0', }
_static_140240906205840 = {u'class': u'form-text text-muted mb-2', }
_static_140240884137360 = {u'class': u'form-control', u'name': u'senaite.databox.columns.converter:records', }
_static_140240906601936 = {u'class': u'form-row', }
_static_140240907628944 = {u'class': u'form-control', u'name': u'senaite.databox.columns.column:records', }
_static_140240917021840 = {u'selected': u"python:context.date_index == index and 'selected' or ''", u'value': u'index', }
_static_140240906592144 = {u'action': u'string:${here/absolute_url}/@@update', u'method': u'post', u'enctype': u'multipart/form-data', u'name': u'databox-form', u'class': u'form', }
_static_140240906849360 = {u'selected': u"python:context.sort_on == index and 'selected' or ''", u'value': u'index', }
_static_140240907113232 = {u'role': u'tabpanel', u'class': u'tab-pane fade', u'id': u'advanced-query', }
_static_140240906640656 = {u'class': u'form-text text-muted', }
_static_140240907086096 = {u'role': u'tabpanel', u'class': u'tab-pane fade', u'id': u'columns', }
_static_140240917019664 = {u'type': u'date', u'class': u'form-control', u'value': u'python:view.date_to', u'name': u'senaite.databox.date_to', }
_static_140240906136592 = {u'class': u'col-auto', }
_static_140240907237392 = {u'selected': u"python:field == columns.get(column).get('column') and 'selected' or ''", u'value': u'field', }
_static_140240906613264 = {u'class': u'input-group-text', }
_static_140240884116880 = {u'class': u'fas fa-code', }
_static_140240917069200 = {u'class': u'input-group-text', }
_static_140240884099216 = {u'class': u'fas fa-plus', }
_static_140240906118544 = {u'class': u'input-group-prepend', }
_static_140240907016336 = {u'class': u'input-group-prepend', }
_static_140240917102032 = {u'class': u'input-group mb-2', }
_static_140240906433808 = {u'role': u'tabpanel', u'class': u'tab-pane fade show active', u'id': u'query', }
_static_140240907005200 = {u'type': u'text', u'class': u'form-control', u'value': u'python:query[q]', u'name': u'senaite.databox.advanced_query.value:records', }
_static_140240907585744 = {u'class': u'input-group-text', }
_static_140240884190736 = {u'type': u'hidden', u'name': u'tab', u'value': u'query', }
_static_140240906450960 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140240906946576 = {u'class': u'input-group input-group-sm mb-2', }
_static_140240917102224 = {u'class': u'input-group-prepend', }
_static_140240906465040 = {u'class': u'form-row', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240917067600 = {u'class': u'input-group-prepend', }
_static_140240907012880 = {u'class': u'flex-fill mr-2', }
_static_140240884115216 = {u'type': u'text', u'class': u'form-control', u'value': u"python:columns[column].get('code')", u'name': u'senaite.databox.columns.code:records', }
_static_140240906532112 = {u'class': u'form-control', u'name': u'senaite.databox.date_index', }
_static_140240906206544 = {u'class': u'form-row', }
_static_140240884097296 = {u'class': u'add_column btn btn-sm btn-outline-success', u'title': u'add', }
_static_140240906623824 = {u'class': u'column pt-2 pl-2 mb-2 border border-light rounded bg-light', }
_static_140240884076624 = {u'selected': u"python:name == columns[column].get('converter') and 'selected' or ''", u'value': u'name', u'label': u'converter/description', }
_static_140240917069520 = {u'class': u'input-group mb-2', }
_static_140240906464592 = {u'class': u'col-auto', }
_static_140240906187920 = {u'role': u'presentation', u'class': u'nav-item', }
_static_140240906928720 = {u'class': u'input-group mb-2', }
_static_140240906604368 = {u'class': u'form-text text-muted mb-2', }
_static_140240884175760 = {u'class': u'ref-type', }
_static_140240906929552 = {u'class': u'flex-fill mr-2', }
_static_140240907114384 = {u'class': u'input-group mb-2', }
_static_140240907012944 = {u'class': u'd-flex text-nowrap', }
_static_140240884151696 = {u'class': u'text-dark', }
_static_140240906558416 = {u'class': u'input-group-text', }
_static_140240907130000 = {u'data-toggle': u'tab', u'href': u'#columns', u'role': u'tab', u'class': u'nav-link', u'id': u'columns-tab', }
_static_140240906533200 = {u'class': u'col-auto', }
_static_140240906693072 = {u'role': u'presentation', u'class': u'nav-item', }
_static_140240906613200 = {u'class': u'col-auto', }
_static_140240906930576 = {u'class': u'input-group-prepend', }

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

            # <Static value=<_ast.Dict object at 0x7f8c61697810> name=None at 7f8c61697050> -> __attrs_140240906450512
            __attrs_140240906450512 = _static_140240906450960
            __previous_i18n_domain_140240906451408 = __i18n_domain
            __i18n_domain = u'senaite.databox'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n  <!-- DATABOX EDITOR -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c616b9f90> name=None at 7f8c61697a90> -> __attrs_140240906591184
            __attrs_140240906591184 = _static_140240906592144

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form name="databox-form" class="form" method="post" enctype="multipart/form-data"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906590544
            __default_140240906590544 = _DEFAULT_MARKER

            # <Substitution u'string:${here/absolute_url}/@@update' (12:31)> -> __attr_action
            __token = 380
            try:
                __zt_tmp = __attrs_140240906591184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140241087907024('string', u'${here/absolute_url}/@@update', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u'>\n\n    <!-- Edit Tabs -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c620b8f50> name=None at 7f8c620b8110> -> __attrs_140240906691280
            __attrs_140240906691280 = _static_140240917073744

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="nav nav-tabs" id="databox-edit" role="tablist">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c616d29d0> name=None at 7f8c616d2790> -> __attrs_140240906694160
            __attrs_140240906694160 = _static_140240906693072

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li class="nav-item" role="presentation">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6172ce10> name=None at 7f8c6172c410> -> __attrs_140240907062288
            __attrs_140240907062288 = _static_140240907062800

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link active" id="query-tab" data-toggle="tab" href="#query" role="tab">')
            __stream_140240907061328 = []
            __append_140240907061328 = __stream_140240907061328.append
            __append_140240907061328(u'\n          Query\n        ')
            __msgid_140240907061328 = __re_whitespace(''.join(__stream_140240907061328)).strip()
            if __msgid_140240907061328:
                __append(translate(__msgid_140240907061328, mapping=None, default=__msgid_140240907061328, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      </li>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c61698890> name=None at 7f8c616d2550> -> __attrs_140240906455824
            __attrs_140240906455824 = _static_140240906455184

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li class="nav-item" role="presentation">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c61698050> name=None at 7f8c616988d0> -> __attrs_140240906122256
            __attrs_140240906122256 = _static_140240906453072

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" id="advanced-query-tab" data-toggle="tab" href="#advanced-query" role="tab">')
            __stream_140240906456016 = []
            __append_140240906456016 = __stream_140240906456016.append
            __append_140240906456016(u'\n          Advanced Query\n        ')
            __msgid_140240906456016 = __re_whitespace(''.join(__stream_140240906456016)).strip()
            if __msgid_140240906456016:
                __append(translate(__msgid_140240906456016, mapping=None, default=__msgid_140240906456016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      </li>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c616476d0> name=None at 7f8c61647310> -> __attrs_140240906122832
            __attrs_140240906122832 = _static_140240906122960

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li class="nav-item" role="presentation">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6173d490> name=None at 7f8c6173d890> -> __attrs_140240906190352
            __attrs_140240906190352 = _static_140240907130000

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" id="columns-tab" data-toggle="tab" href="#columns" role="tab">')
            __stream_140240907129104 = []
            __append_140240907129104 = __stream_140240907129104.append
            __append_140240907129104(u'\n          Columns\n        ')
            __msgid_140240907129104 = __re_whitespace(''.join(__stream_140240907129104)).strip()
            if __msgid_140240907129104:
                __append(translate(__msgid_140240907129104, mapping=None, default=__msgid_140240907129104, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      </li>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c61657490> name=None at 7f8c616572d0> -> __attrs_140240906189136
            __attrs_140240906189136 = _static_140240906187920

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li class="nav-item" role="presentation">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c61657d10> name=None at 7f8c61657050> -> __attrs_140240906826512
            __attrs_140240906826512 = _static_140240906190096

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" id="info-tab" data-toggle="tab" href="#info" role="tab">')
            __stream_140240906188240 = []
            __append_140240906188240 = __stream_140240906188240.append
            __append_140240906188240(u'\n          Info\n        ')
            __msgid_140240906188240 = __re_whitespace(''.join(__stream_140240906188240)).strip()
            if __msgid_140240906188240:
                __append(translate(__msgid_140240906188240, mapping=None, default=__msgid_140240906188240, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n      </li>\n    </ul>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c61657fd0> name=None at 7f8c61657850> -> __attrs_140240906434448
            __attrs_140240906434448 = _static_140240906190800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-content mt-3">\n      <!-- QUERY CONFIG TAB -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c61693510> name=None at 7f8c616931d0> -> __attrs_140240906435088
            __attrs_140240906435088 = _static_140240906433808

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-pane fade show active" id="query" role="tabpanel">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6165ba90> name=None at 7f8c6165b590> -> __attrs_140240906203216
            __attrs_140240906203216 = _static_140240906205840

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted mb-2">')
            __stream_140240906205328 = []
            __append_140240906205328 = __stream_140240906205328.append
            __append_140240906205328(u'\n          Define basic query options.\n        ')
            __msgid_140240906205328 = __re_whitespace(''.join(__stream_140240906205328)).strip()
            if __msgid_140240906205328:
                __append(translate(__msgid_140240906205328, mapping=None, default=__msgid_140240906205328, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6165bd50> name=None at 7f8c6165b090> -> __attrs_140240906205136
            __attrs_140240906205136 = _static_140240906206544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-row">\n          <!-- sort on -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6165bf10> name=None at 7f8c6165bd90> -> __attrs_140240906768080
            __attrs_140240906768080 = _static_140240906206992

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c616e4810> name=None at 7f8c616e42d0> -> __attrs_140240906764752
            __attrs_140240906764752 = _static_140240906766352

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616e4dd0> name=None at 7f8c616e4950> -> __attrs_140240906765072
            __attrs_140240906765072 = _static_140240906767824

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-prepend">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c6164a790> name=None at 7f8c6164abd0> -> __attrs_140240906134160
            __attrs_140240906134160 = _static_140240906135440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-text">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906135376
            __attrs_140240906135376 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906137552 = []
            __append_140240906137552 = __stream_140240906137552.append
            __append_140240906137552(u'Sort on')
            __msgid_140240906137552 = __re_whitespace(''.join(__stream_140240906137552)).strip()
            if __msgid_140240906137552:
                __append(translate(__msgid_140240906137552, mapping=None, default=__msgid_140240906137552, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n                </div>\n              </div>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6164a9d0> name=None at 7f8c6164a510> -> __attrs_140240906133584
            __attrs_140240906133584 = _static_140240906136016

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select class="form-control" name="senaite.databox.sort_on">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906846800
            __attrs_140240906846800 = _static_140241133802128
            __backup_index_140240906765776 = get('index', __marker)

            # <Value u'view/get_catalog_sort_indexes' (74:43)> -> __iterator
            __token = 2278
            try:
                __zt_tmp = __attrs_140240906846800
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/get_catalog_sort_indexes', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240906848208, ) = getitem('repeat')(u'index', __iterator)
            econtext['index'] = None
            for __item in __iterator:
                econtext['index'] = __item
                __append(u'\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c616f8c50> name=None at 7f8c616f8950> -> __attrs_140240906846288
                __attrs_140240906846288 = _static_140240906849360

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906850128
                __default_140240906850128 = _DEFAULT_MARKER

                # <Substitution u'index' (75:48)> -> __attr_value
                __token = 2358
                try:
                    __zt_tmp = __attrs_140240906846288
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906848336
                __default_140240906848336 = _DEFAULT_MARKER

                # <Boolean u"python:context.sort_on == index and 'selected' or ''" (75:63)> -> __attr_selected
                __token = 2373
                try:
                    __zt_tmp = __attrs_140240906846288
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_140241087907024('python', u"context.sort_on == index and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = u'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((u' selected="%s"' % __attr_selected))
                __append(u'>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906847120
                __attrs_140240906847120 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906847760
                __default_140240906847760 = _DEFAULT_MARKER

                # <Value u'index' (76:39)> -> __cache_140240906848080
                __token = 2468
                try:
                    __zt_tmp = __attrs_140240906847120
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906848080 = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'index' (76:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c620babd0> -> __condition
                __expression = __cache_140240906848080

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140240906848080
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n                  </option>\n                ')
                ____index_140240906848208 -= 1
                if (____index_140240906848208 > 0):
                    __append('')
            if (__backup_index_140240906765776 is __marker):
                del econtext['index']
            else:
                econtext['index'] = __backup_index_140240906765776
            __append(u'\n              </select>\n            </div>\n          </div>\n          <!-- limit -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6164ac10> name=None at 7f8c6164aa10> -> __attrs_140240906849424
            __attrs_140240906849424 = _static_140240906136592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c620b7ed0> name=None at 7f8c620b7d10> -> __attrs_140240917067856
            __attrs_140240917067856 = _static_140240917069520

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c620b7750> name=None at 7f8c620b7a50> -> __attrs_140240917066128
            __attrs_140240917066128 = _static_140240917067600

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-prepend">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c620b7d90> name=None at 7f8c620b79d0> -> __attrs_140240917068496
            __attrs_140240917068496 = _static_140240917069200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-text">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906489808
            __attrs_140240906489808 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906489744 = []
            __append_140240906489744 = __stream_140240906489744.append
            __append_140240906489744(u'Limit')
            __msgid_140240906489744 = __re_whitespace(''.join(__stream_140240906489744)).strip()
            if __msgid_140240906489744:
                __append(translate(__msgid_140240906489744, mapping=None, default=__msgid_140240906489744, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n                </div>\n              </div>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616a0d50> name=None at 7f8c616a0850> -> __attrs_140240906462288
            __attrs_140240906462288 = _static_140240906489168

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="number" style="width:75px" class="form-control" id="field-limit" min="1" name="senaite.databox.limit:int"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906463888
            __default_140240906463888 = _DEFAULT_MARKER

            # <Substitution u'here/limit' (94:43)> -> __attr_value
            __token = 3089
            try:
                __zt_tmp = __attrs_140240906462288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'here/limit', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'>\n            </div>\n          </div>\n          <!-- reversed order -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6169ad50> name=None at 7f8c620b7990> -> __attrs_140240906462416
            __attrs_140240906462416 = _static_140240906464592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6169a910> name=None at 7f8c6169afd0> -> __attrs_140240906462928
            __attrs_140240906462928 = _static_140240906463504

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-check mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6169ae50> name=None at 7f8c6169a250> -> __attrs_140240906548752
            __attrs_140240906548752 = _static_140240906464848

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="checkbox" class="form-check-input" id="field-sort_reversed" value="selected" name="senaite.databox.sort_reversed:boolean"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906548368
            __default_140240906548368 = _DEFAULT_MARKER

            # <Boolean u'here/sort_reversed' (105:45)> -> __attr_checked
            __token = 3504
            try:
                __zt_tmp = __attrs_140240906548752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_140241087907024('path', u'here/sort_reversed', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = u'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((u' checked="%s"' % __attr_checked))
            __append(u'>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616afb90> name=None at 7f8c616af410> -> __attrs_140240906550864
            __attrs_140240906550864 = _static_140240906550160

            # <Value u'here/sort_reversed' (110:36)> -> __condition
            __token = 3731
            try:
                __zt_tmp = __attrs_140240906550864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'here/sort_reversed', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" value="" name="senaite.databox.sort_reversed:boolean" />')
            __append(u'\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616cf6d0> name=None at 7f8c616cf5d0> -> __attrs_140240906681936
            __attrs_140240906681936 = _static_140240906680016

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label class="form-check-label" for="field-sort_reversed">')
            __stream_140240906680400 = []
            __append_140240906680400 = __stream_140240906680400.append
            __append_140240906680400(u'\n                Reversed order\n              ')
            __msgid_140240906680400 = __re_whitespace(''.join(__stream_140240906680400)).strip()
            if __msgid_140240906680400:
                __append(translate(__msgid_140240906680400, mapping=None, default=__msgid_140240906680400, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n            </div>\n          </div>\n        </div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6169af10> name=None at 7f8c616e4510> -> __attrs_140240906681424
            __attrs_140240906681424 = _static_140240906465040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-row">\n          <!-- date index -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c616cfad0> name=None at 7f8c616cfbd0> -> __attrs_140240906678864
            __attrs_140240906678864 = _static_140240906681040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c616cfa10> name=None at 7f8c616cf890> -> __attrs_140240906802064
            __attrs_140240906802064 = _static_140240906680848

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616ed410> name=None at 7f8c616edc10> -> __attrs_140240906802896
            __attrs_140240906802896 = _static_140240906802192

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-prepend">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c616ed5d0> name=None at 7f8c616edc50> -> __attrs_140240906531472
            __attrs_140240906531472 = _static_140240906802640

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-text">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906534672
            __attrs_140240906534672 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906534288 = []
            __append_140240906534288 = __stream_140240906534288.append
            __append_140240906534288(u'Date Index')
            __msgid_140240906534288 = __re_whitespace(''.join(__stream_140240906534288)).strip()
            if __msgid_140240906534288:
                __append(translate(__msgid_140240906534288, mapping=None, default=__msgid_140240906534288, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n                </div>\n              </div>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616ab510> name=None at 7f8c616abdd0> -> __attrs_140240906532944
            __attrs_140240906532944 = _static_140240906532112

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select class="form-control" name="senaite.databox.date_index">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906531280
            __attrs_140240906531280 = _static_140241133802128
            __backup_index_140240906133968 = get('index', __marker)

            # <Value u'view/get_catalog_date_indexes' (130:43)> -> __iterator
            __token = 4496
            try:
                __zt_tmp = __attrs_140240906531280
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/get_catalog_date_indexes', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240906533328, ) = getitem('repeat')(u'index', __iterator)
            econtext['index'] = None
            for __item in __iterator:
                econtext['index'] = __item
                __append(u'\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c620ac490> name=None at 7f8c620ac690> -> __attrs_140240917024656
                __attrs_140240917024656 = _static_140240917021840

                # <option ... (0:0)
                # --------------------------------------------------------
                __append(u'<option')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917021584
                __default_140240917021584 = _DEFAULT_MARKER

                # <Substitution u'index' (131:48)> -> __attr_value
                __token = 4576
                try:
                    __zt_tmp = __attrs_140240917024656
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917024592
                __default_140240917024592 = _DEFAULT_MARKER

                # <Boolean u"python:context.date_index == index and 'selected' or ''" (131:63)> -> __attr_selected
                __token = 4591
                try:
                    __zt_tmp = __attrs_140240917024656
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_140241087907024('python', u"context.date_index == index and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = u'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((u' selected="%s"' % __attr_selected))
                __append(u'>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917023952
                __attrs_140240917023952 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917023504
                __default_140240917023504 = _DEFAULT_MARKER

                # <Value u'index' (132:39)> -> __cache_140240917022608
                __token = 4689
                try:
                    __zt_tmp = __attrs_140240917023952
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240917022608 = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'index' (132:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c620ac290> -> __condition
                __expression = __cache_140240917022608

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140240917022608
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n                  </option>\n                ')
                ____index_140240906533328 -= 1
                if (____index_140240906533328 > 0):
                    __append('')
            if (__backup_index_140240906133968 is __marker):
                del econtext['index']
            else:
                econtext['index'] = __backup_index_140240906133968
            __append(u'\n              </select>\n            </div>\n          </div>\n          <!-- date from -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c616ab950> name=None at 7f8c616ed310> -> __attrs_140240917024464
            __attrs_140240917024464 = _static_140240906533200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c620bfdd0> name=None at 7f8c620bf150> -> __attrs_140240917099152
            __attrs_140240917099152 = _static_140240917102032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c620bfe90> name=None at 7f8c620bf1d0> -> __attrs_140240917099536
            __attrs_140240917099536 = _static_140240917102224

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-prepend">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c616bf210> name=None at 7f8c616bfd90> -> __attrs_140240906616336
            __attrs_140240906616336 = _static_140240906613264

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-text">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906614608
            __attrs_140240906614608 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906615824 = []
            __append_140240906615824 = __stream_140240906615824.append
            __append_140240906615824(u'Date From')
            __msgid_140240906615824 = __re_whitespace(''.join(__stream_140240906615824)).strip()
            if __msgid_140240906615824:
                __append(translate(__msgid_140240906615824, mapping=None, default=__msgid_140240906615824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n                </div>\n              </div>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c616bf2d0> name=None at 7f8c616bfe90> -> __attrs_140240906615760
            __attrs_140240906615760 = _static_140240906613456

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="date" class="form-control" name="senaite.databox.date_from"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906614032
            __default_140240906614032 = _DEFAULT_MARKER

            # <Substitution u'python:view.date_from' (148:43)> -> __attr_value
            __token = 5238
            try:
                __zt_tmp = __attrs_140240906615760
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('python', u'view.date_from', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'>\n            </div>\n          </div>\n          <!-- date to -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c616bf1d0> name=None at 7f8c616bf490> -> __attrs_140240907115600
            __attrs_140240907115600 = _static_140240906613200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-auto">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c61739790> name=None at 7f8c61739690> -> __attrs_140240907116496
            __attrs_140240907116496 = _static_140240907114384

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group mb-2">\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c617392d0> name=None at 7f8c61739190> -> __attrs_140240907113680
            __attrs_140240907113680 = _static_140240907113168

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-prepend">\n                ')

            # <Static value=<_ast.Dict object at 0x7f8c61739350> name=None at 7f8c61739110> -> __attrs_140240917017104
            __attrs_140240917017104 = _static_140240907113296

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="input-group-text">\n                  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917018704
            __attrs_140240917018704 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240917018128 = []
            __append_140240917018128 = __stream_140240917018128.append
            __append_140240917018128(u'Date To')
            __msgid_140240917018128 = __re_whitespace(''.join(__stream_140240917018128)).strip()
            if __msgid_140240917018128:
                __append(translate(__msgid_140240917018128, mapping=None, default=__msgid_140240917018128, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n                </div>\n              </div>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c620abc10> name=None at 7f8c620aba10> -> __attrs_140240906601744
            __attrs_140240906601744 = _static_140240917019664
            __backup_date_to_140240906767888 = get('date_to', __marker)

            # <Value u'here/date_to' (162:41)> -> __value
            __token = 5767
            try:
                __zt_tmp = __attrs_140240906601744
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'here/date_to', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['date_to'] = __value

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="date" class="form-control" name="senaite.databox.date_to"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906601488
            __default_140240906601488 = _DEFAULT_MARKER

            # <Substitution u'python:view.date_to' (163:43)> -> __attr_value
            __token = 5824
            try:
                __zt_tmp = __attrs_140240906601744
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('python', u'view.date_to', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u'>')
            if (__backup_date_to_140240906767888 is __marker):
                del econtext['date_to']
            else:
                econtext['date_to'] = __backup_date_to_140240906767888
            __append(u'\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <!-- ADVANCED QUERY CONFIG TAB -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c61739310> name=None at 7f8c61739550> -> __attrs_140240906600592
            __attrs_140240906600592 = _static_140240907113232

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-pane fade" id="advanced-query" role="tabpanel">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616bcf50> name=None at 7f8c616bcb50> -> __attrs_140240906602576
            __attrs_140240906602576 = _static_140240906604368

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted mb-2">')
            __stream_140240906601168 = []
            __append_140240906601168 = __stream_140240906601168.append
            __append_140240906601168(u'\n          Define one or more explicit values for catalog indexes to refine the query.\n        ')
            __msgid_140240906601168 = __re_whitespace(''.join(__stream_140240906601168)).strip()
            if __msgid_140240906601168:
                __append(translate(__msgid_140240906601168, mapping=None, default=__msgid_140240906601168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616bc5d0> name=None at 7f8c616bc690> -> __attrs_140240918125968
            __attrs_140240918125968 = _static_140240906601936

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-row">\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c61732290> name=None at 7f8c61732f50> -> __attrs_140240907084368
            __attrs_140240907084368 = _static_140240907084432

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul id="advanced-queries" class="col-auto list-unstyled m-0">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c61732b10> name=None at 7f8c61732f10> -> __attrs_140240907084688
            __attrs_140240907084688 = _static_140240907086608
            __backup_query_140240906206800 = get('query', __marker)

            # <Value u'view/get_advanced_query' (178:34)> -> __value
            __token = 6438
            try:
                __zt_tmp = __attrs_140240907084688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'view/get_advanced_query', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['query'] = __value
            __backup_q_140240906766032 = get('q', __marker)

            # <Value u'python:sorted(query, reverse=1)' (179:30)> -> __iterator
            __token = 6494
            try:
                __zt_tmp = __attrs_140240907084688
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('python', u'sorted(query, reverse=1)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240907086224, ) = getitem('repeat')(u'q', __iterator)
            econtext['q'] = None
            for __item in __iterator:
                econtext['q'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="advanced-query d-flex flex-wrap p-0">\n\n              <!-- Index -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c617218d0> name=None at 7f8c61721610> -> __attrs_140240907015952
                __attrs_140240907015952 = _static_140240907016400

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c61721e90> name=None at 7f8c61721d10> -> __attrs_140240907014352
                __attrs_140240907014352 = _static_140240907017872

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group mb-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c61721890> name=None at 7f8c61721d90> -> __attrs_140240907017104
                __attrs_140240907017104 = _static_140240907016336

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c616ddfd0> name=None at 7f8c616dd590> -> __attrs_140240906736912
                __attrs_140240906736912 = _static_140240906739664

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906738128
                __attrs_140240906738128 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240906738896 = []
                __append_140240906738896 = __stream_140240906738896.append
                __append_140240906738896(u'Index')
                __msgid_140240906738896 = __re_whitespace(''.join(__stream_140240906738896)).strip()
                if __msgid_140240906738896:
                    __append(translate(__msgid_140240906738896, mapping=None, default=__msgid_140240906738896, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                    </div>\n                  </div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c616dd850> name=None at 7f8c616dd750> -> __attrs_140240906736848
                __attrs_140240906736848 = _static_140240906737744

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select class="form-control" name="senaite.databox.advanced_query.index:records">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907018768
                __attrs_140240907018768 = _static_140241133802128
                __backup_index_140240907016272 = get('index', __marker)

                # <Value u'view/get_catalog_indexes' (191:47)> -> __iterator
                __token = 7035
                try:
                    __zt_tmp = __attrs_140240907018768
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/get_catalog_indexes', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907022096, ) = getitem('repeat')(u'index', __iterator)
                econtext['index'] = None
                for __item in __iterator:
                    econtext['index'] = __item
                    __append(u'\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8c61722490> name=None at 7f8c61722310> -> __attrs_140240907021264
                    __attrs_140240907021264 = _static_140240907019408

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907019792
                    __default_140240907019792 = _DEFAULT_MARKER

                    # <Substitution u'index' (192:52)> -> __attr_value
                    __token = 7114
                    try:
                        __zt_tmp = __attrs_140240907021264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907021392
                    __default_140240907021392 = _DEFAULT_MARKER

                    # <Boolean u"python:index == q and 'selected' or ''" (192:67)> -> __attr_selected
                    __token = 7129
                    try:
                        __zt_tmp = __attrs_140240907021264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140241087907024('python', u"index == q and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = u'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((u' selected="%s"' % __attr_selected))
                    __append(u'>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907020688
                    __attrs_140240907020688 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907020752
                    __default_140240907020752 = _DEFAULT_MARKER

                    # <Value u'index' (193:43)> -> __cache_140240907022032
                    __token = 7214
                    try:
                        __zt_tmp = __attrs_140240907020688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907022032 = _static_140241087907024('path', u'index', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'index' (193:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61722290> -> __condition
                    __expression = __cache_140240907022032

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span/>')
                    else:
                        __content = __cache_140240907022032
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                      </option>\n                    ')
                    ____index_140240907022096 -= 1
                    if (____index_140240907022096 > 0):
                        __append('')
                if (__backup_index_140240907016272 is __marker):
                    del econtext['index']
                else:
                    econtext['index'] = __backup_index_140240907016272
                __append(u'\n                  </select>\n                </div>\n              </div>\n\n              <!-- Value -->\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c617221d0> name=None at 7f8c616ddad0> -> __attrs_140240907019152
                __attrs_140240907019152 = _static_140240907018704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c6170c250> name=None at 7f8c6170ced0> -> __attrs_140240906930704
                __attrs_140240906930704 = _static_140240906928720

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group mb-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c6170c990> name=None at 7f8c6170cf50> -> __attrs_140240906929744
                __attrs_140240906929744 = _static_140240906930576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6170c810> name=None at 7f8c6170c410> -> __attrs_140240906930512
                __attrs_140240906930512 = _static_140240906930192

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907005008
                __attrs_140240907005008 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240907005840 = []
                __append_140240907005840 = __stream_140240907005840.append
                __append_140240907005840(u'=')
                __msgid_140240907005840 = __re_whitespace(''.join(__stream_140240907005840)).strip()
                if __msgid_140240907005840:
                    __append(translate(__msgid_140240907005840, mapping=None, default=__msgid_140240907005840, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                    </div>\n                  </div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c6171ed10> name=None at 7f8c6170cad0> -> __attrs_140240907002064
                __attrs_140240907002064 = _static_140240907005200

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" class="form-control" name="senaite.databox.advanced_query.value:records"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907002832
                __default_140240907002832 = _DEFAULT_MARKER

                # <Substitution u'python:query[q]' (210:47)> -> __attr_value
                __token = 7822
                try:
                    __zt_tmp = __attrs_140240907002064
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('python', u'query[q]', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c6171ef50> name=None at 7f8c6171e090> -> __attrs_140240907004176
                __attrs_140240907004176 = _static_140240907005776

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-append">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c616b1bd0> name=None at 7f8c6171ec10> -> __attrs_140240906559312
                __attrs_140240906559312 = _static_140240906558416

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c616b1d90> name=None at 7f8c616b1850> -> __attrs_140240906556944
                __attrs_140240906556944 = _static_140240906558864

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input class="mr-2" value="1" name="senaite.databox.advanced_query.delete:bool:records" type="checkbox"/>\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906677200
                __attrs_140240906677200 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240906556624 = []
                __append_140240906556624 = __stream_140240906556624.append
                __append_140240906556624(u'Delete')
                __msgid_140240906556624 = __re_whitespace(''.join(__stream_140240906556624)).strip()
                if __msgid_140240906556624:
                    __append(translate(__msgid_140240906556624, mapping=None, default=__msgid_140240906556624, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                    </div>\n                  </div>\n                </div>\n              </div>\n\n            </li>')
                ____index_140240907086224 -= 1
                if (____index_140240907086224 > 0):
                    __append('\n            ')
            if (__backup_q_140240906766032 is __marker):
                del econtext['q']
            else:
                econtext['q'] = __backup_q_140240906766032
            if (__backup_query_140240906206800 is __marker):
                del econtext['query']
            else:
                econtext['query'] = __backup_query_140240906206800
            __append(u'\n          </ul>\n        </div>\n      </div>\n\n      <!-- COLUMNS CONFIG TAB -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c61732910> name=None at 7f8c61732ed0> -> __attrs_140240906556560
            __attrs_140240906556560 = _static_140240907086096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-pane fade" id="columns" role="tabpanel">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616ce6d0> name=None at 7f8c616cec90> -> __attrs_140240906676112
            __attrs_140240906676112 = _static_140240906675920

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted mb-2">')
            __stream_140240906675792 = []
            __append_140240906675792 = __stream_140240906675792.append
            __append_140240906675792(u'\n          Define display columns for the search results.\n        ')
            __msgid_140240906675792 = __re_whitespace(''.join(__stream_140240906675792)).strip()
            if __msgid_140240906675792:
                __append(translate(__msgid_140240906675792, mapping=None, default=__msgid_140240906675792, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616ce410> name=None at 7f8c616ce750> -> __attrs_140240906676496
            __attrs_140240906676496 = _static_140240906675216

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted">')
            __stream_140240906675728 = []
            __append_140240906675728 = __stream_140240906675728.append
            __append_140240906675728(u'\n          Use the code line below to retrieve a value by a Python expression\n          instead using the field.\n        ')
            __msgid_140240906675728 = __re_whitespace(''.join(__stream_140240906675728)).strip()
            if __msgid_140240906675728:
                __append(translate(__msgid_140240906675728, mapping=None, default=__msgid_140240906675728, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c61729950> name=None at 7f8c616ce7d0> -> __attrs_140240907049680
            __attrs_140240907049680 = _static_140240907049296

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted">\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907047760
            __attrs_140240907047760 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240907050256 = []
            __append_140240907050256 = __stream_140240907050256.append
            __append_140240907050256(u'Available variables are ')
            __msgid_140240907050256 = __re_whitespace(''.join(__stream_140240907050256)).strip()
            if __msgid_140240907050256:
                __append(translate(__msgid_140240907050256, mapping=None, default=__msgid_140240907050256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907049168
            __attrs_140240907049168 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>context</code> ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907049552
            __attrs_140240907049552 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240907050640 = []
            __append_140240907050640 = __stream_140240907050640.append
            __append_140240907050640(u'(the current column context),')
            __msgid_140240907050640 = __re_whitespace(''.join(__stream_140240907050640)).strip()
            if __msgid_140240907050640:
                __append(translate(__msgid_140240907050640, mapping=None, default=__msgid_140240907050640, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907046992
            __attrs_140240907046992 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>model</code> ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240916605968
            __attrs_140240916605968 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240907048528 = []
            __append_140240907048528 = __stream_140240907048528.append
            __append_140240907048528(u'(wrapped senaite.supermodel context),')
            __msgid_140240907048528 = __re_whitespace(''.join(__stream_140240907048528)).strip()
            if __msgid_140240907048528:
                __append(translate(__msgid_140240907048528, mapping=None, default=__msgid_140240907048528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906641104
            __attrs_140240906641104 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>brain</code> ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906637520
            __attrs_140240906637520 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906637392 = []
            __append_140240906637392 = __stream_140240906637392.append
            __append_140240906637392(u'(catalog brain of the databox query type),')
            __msgid_140240906637392 = __re_whitespace(''.join(__stream_140240906637392)).strip()
            if __msgid_140240906637392:
                __append(translate(__msgid_140240906637392, mapping=None, default=__msgid_140240906637392, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906638928
            __attrs_140240906638928 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>obj</code> ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906639376
            __attrs_140240906639376 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906639440 = []
            __append_140240906639440 = __stream_140240906639440.append
            __append_140240906639440(u'(content object of the databox query type),')
            __msgid_140240906639440 = __re_whitespace(''.join(__stream_140240906639440)).strip()
            if __msgid_140240906639440:
                __append(translate(__msgid_140240906639440, mapping=None, default=__msgid_140240906639440, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906640208
            __attrs_140240906640208 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>api</code> ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906639120
            __attrs_140240906639120 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906640592 = []
            __append_140240906640592 = __stream_140240906640592.append
            __append_140240906640592(u'(the senaite API module).')
            __msgid_140240906640592 = __re_whitespace(''.join(__stream_140240906640592)).strip()
            if __msgid_140240906640592:
                __append(translate(__msgid_140240906640592, mapping=None, default=__msgid_140240906640592, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n        </div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616c5d10> name=None at 7f8c616c5910> -> __attrs_140240906648336
            __attrs_140240906648336 = _static_140240906640656

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted">\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906646096
            __attrs_140240906646096 = _static_140241133802128

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append(u'<strong>')
            __stream_140240906646992 = []
            __append_140240906646992 = __stream_140240906646992.append
            __append_140240906646992(u'Examples:')
            __msgid_140240906646992 = __re_whitespace(''.join(__stream_140240906646992)).strip()
            if __msgid_140240906646992:
                __append(translate(__msgid_140240906646992, mapping=None, default=__msgid_140240906646992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</strong>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906647440
            __attrs_140240906647440 = _static_140241133802128

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906649232
            __attrs_140240906649232 = _static_140241133802128

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906649296
            __attrs_140240906649296 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>context.aq_parent.Title()</code>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907051920
            __attrs_140240907051920 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240907051664 = []
            __append_140240907051664 = __stream_140240907051664.append
            __append_140240907051664(u'Retrieve the title of the parent object')
            __msgid_140240907051664 = __re_whitespace(''.join(__stream_140240907051664)).strip()
            if __msgid_140240907051664:
                __append(translate(__msgid_140240907051664, mapping=None, default=__msgid_140240907051664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n            </li>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907052304
            __attrs_140240907052304 = _static_140241133802128

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907054480
            __attrs_140240907054480 = _static_140241133802128

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code>api.get_review_status(context)</code>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907054096
            __attrs_140240907054096 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240907053200 = []
            __append_140240907053200 = __stream_140240907053200.append
            __append_140240907053200(u'Retrieve the review state of the current context')
            __msgid_140240907053200 = __re_whitespace(''.join(__stream_140240907053200)).strip()
            if __msgid_140240907053200:
                __append(translate(__msgid_140240907053200, mapping=None, default=__msgid_140240907053200, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n            </li>\n          </ul>\n        </div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616c7710> name=None at 7f8c616c77d0> -> __attrs_140240907052560
            __attrs_140240907052560 = _static_140240906647312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-text text-muted">\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907051856
            __attrs_140240907051856 = _static_140241133802128

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append(u'<strong>')
            __stream_140240907052624 = []
            __append_140240907052624 = __stream_140240907052624.append
            __append_140240907052624(u'Caution:')
            __msgid_140240907052624 = __re_whitespace(''.join(__stream_140240907052624)).strip()
            if __msgid_140240907052624:
                __append(translate(__msgid_140240907052624, mapping=None, default=__msgid_140240907052624, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</strong>\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906622928
            __attrs_140240906622928 = _static_140241133802128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140240906621456 = []
            __append_140240906621456 = __stream_140240906621456.append
            __append_140240906621456(u'\n            Using the code field executes the Python\n            code without restrictions and can potentially damage data.\n          ')
            __msgid_140240906621456 = __re_whitespace(''.join(__stream_140240906621456)).strip()
            if __msgid_140240906621456:
                __append(translate(__msgid_140240906621456, mapping=None, default=__msgid_140240906621456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n        </div>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c616c10d0> name=None at 7f8c6172a090> -> __attrs_140240906621904
            __attrs_140240906621904 = _static_140240906621136

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form-row">\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c616c1a10> name=None at 7f8c616c19d0> -> __attrs_140240906623120
            __attrs_140240906623120 = _static_140240906623504

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul id="columns-list" class="columns col-auto list-unstyled">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c616c1b50> name=None at 7f8c616c1b90> -> __attrs_140240907010320
            __attrs_140240907010320 = _static_140240906623824
            __backup_columns_140240906133840 = get('columns', __marker)

            # <Value u'python:view.columns' (269:36)> -> __value
            __token = 10496
            try:
                __zt_tmp = __attrs_140240907010320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.columns', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['columns'] = __value
            __backup_column_140240906457040 = get('column', __marker)

            # <Value u'columns' (270:35)> -> __iterator
            __token = 10553
            try:
                __zt_tmp = __attrs_140240907010320
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'columns', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240907010384, ) = getitem('repeat')(u'column', __iterator)
            econtext['column'] = None
            for __item in __iterator:
                econtext['column'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="column pt-2 pl-2 mb-2 border border-light rounded bg-light">\n\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c61720b50> name=None at 7f8c61720950> -> __attrs_140240907012560
                __attrs_140240907012560 = _static_140240907012944

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="d-flex text-nowrap">\n                <!-- column title -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c61720b10> name=None at 7f8c61720cd0> -> __attrs_140240907010256
                __attrs_140240907010256 = _static_140240907012880

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c61710810> name=None at 7f8c61710b90> -> __attrs_140240906946896
                __attrs_140240906946896 = _static_140240906946576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm mb-2">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c61710a90> name=None at 7f8c61710210> -> __attrs_140240906945680
                __attrs_140240906945680 = _static_140240906947216

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c61710710> name=None at 7f8c61710150> -> __attrs_140240906948432
                __attrs_140240906948432 = _static_140240906946320

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c6174d350> name=None at 7f8c6174d210> -> __attrs_140240907198416
                __attrs_140240907198416 = _static_140240907195216

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-tag"></i>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c6174d450> name=None at 7f8c6174d0d0> -> __attrs_140240907195344
                __attrs_140240907195344 = _static_140240907195472

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="ml-1">')
                __stream_140240907197072 = []
                __append_140240907197072 = __stream_140240907197072.append
                __append_140240907197072(u'Label')
                __msgid_140240907197072 = __re_whitespace(''.join(__stream_140240907197072)).strip()
                if __msgid_140240907197072:
                    __append(translate(__msgid_140240907197072, mapping=None, default=__msgid_140240907197072, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                      </div>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c61710790> name=None at 7f8c61710310> -> __attrs_140240907197776
                __attrs_140240907197776 = _static_140240906946448

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" class="form-control" name="senaite.databox.columns.title:records"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907195600
                __default_140240907195600 = _DEFAULT_MARKER

                # <Substitution u"python:columns[column].get('title')" (284:48)> -> __attr_value
                __token = 11180
                try:
                    __zt_tmp = __attrs_140240907197776
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('python', u"columns[column].get('title')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>\n                  </div>\n                </div>\n\n                <!-- column -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c6170c590> name=None at 7f8c617100d0> -> __attrs_140240907585424
                __attrs_140240907585424 = _static_140240906929552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c617acad0> name=None at 7f8c617ac610> -> __attrs_140240907585488
                __attrs_140240907585488 = _static_140240907586256

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm mb-2">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c617acb50> name=None at 7f8c617acdd0> -> __attrs_140240907586512
                __attrs_140240907586512 = _static_140240907586384

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c617ac8d0> name=None at 7f8c617ac710> -> __attrs_140240907632528
                __attrs_140240907632528 = _static_140240907585744

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c617b7290> name=None at 7f8c617b7250> -> __attrs_140240907632272
                __attrs_140240907632272 = _static_140240907629200

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-database"></i>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c617b7350> name=None at 7f8c617b7dd0> -> __attrs_140240907629648
                __attrs_140240907629648 = _static_140240907629392

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="ml-1">')
                __stream_140240907629712 = []
                __append_140240907629712 = __stream_140240907629712.append
                __append_140240907629712(u'Field')
                __msgid_140240907629712 = __re_whitespace(''.join(__stream_140240907629712)).strip()
                if __msgid_140240907629712:
                    __append(translate(__msgid_140240907629712, mapping=None, default=__msgid_140240907629712, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                      </div>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c617b7190> name=None at 7f8c617b79d0> -> __attrs_140240907629456
                __attrs_140240907629456 = _static_140240907628944

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select class="form-control" name="senaite.databox.columns.column:records">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907238544
                __attrs_140240907238544 = _static_140241133802128
                __backup_field_140240907020432 = get('field', __marker)

                # <Value u'view/get_schema_fields' (300:49)> -> __iterator
                __token = 11945
                try:
                    __zt_tmp = __attrs_140240907238544
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/get_schema_fields', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907238224, ) = getitem('repeat')(u'field', __iterator)
                econtext['field'] = None
                for __item in __iterator:
                    econtext['field'] = __item
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8c61757810> name=None at 7f8c61757a90> -> __attrs_140240907236688
                    __attrs_140240907236688 = _static_140240907237392

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907237328
                    __default_140240907237328 = _DEFAULT_MARKER

                    # <Substitution u'field' (301:54)> -> __attr_value
                    __token = 12024
                    try:
                        __zt_tmp = __attrs_140240907236688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'field', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907236432
                    __default_140240907236432 = _DEFAULT_MARKER

                    # <Boolean u"python:field == columns.get(column).get('column') and 'selected' or ''" (301:69)> -> __attr_selected
                    __token = 12039
                    try:
                        __zt_tmp = __attrs_140240907236688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140241087907024('python', u"field == columns.get(column).get('column') and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = u'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((u' selected="%s"' % __attr_selected))
                    __append(u'>\n                          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907238096
                    __attrs_140240907238096 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907239056
                    __default_140240907239056 = _DEFAULT_MARKER

                    # <Value u'field' (302:45)> -> __cache_140240907238480
                    __token = 12158
                    try:
                        __zt_tmp = __attrs_140240907238096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907238480 = _static_140241087907024('path', u'field', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'field' (302:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61757390> -> __condition
                    __expression = __cache_140240907238480

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span/>')
                    else:
                        __content = __cache_140240907238480
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                        </option>\n                      ')
                    ____index_140240907238224 -= 1
                    if (____index_140240907238224 > 0):
                        __append('')
                if (__backup_field_140240907020432 is __marker):
                    del econtext['field']
                else:
                    econtext['field'] = __backup_field_140240907020432
                __append(u'\n                    </select>\n                  </div>\n                </div>\n\n                <!-- reference columns -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c617ac350> name=None at 7f8c617ace10> -> __attrs_140240907238608
                __attrs_140240907238608 = _static_140240907584336
                __backup_ref_140240907017360 = get('ref', __marker)

                # <Value u'python:view.get_reference_columns(column)' (311:36)> -> __iterator
                __token = 12440
                try:
                    __zt_tmp = __attrs_140240907238608
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('python', u'view.get_reference_columns(column)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240907236624, ) = getitem('repeat')(u'ref', __iterator)
                econtext['ref'] = None
                for __item in __iterator:
                    econtext['ref'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="flex-fill mr-2">\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8c61646090> name=None at 7f8c61646050> -> __attrs_140240906117904
                    __attrs_140240906117904 = _static_140240906117264

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-sm mb-2">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8c61646590> name=None at 7f8c61646550> -> __attrs_140240906119184
                    __attrs_140240906119184 = _static_140240906118544

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8c61646a90> name=None at 7f8c61646a50> -> __attrs_140240906120464
                    __attrs_140240906120464 = _static_140240906119824

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-text">\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884174992
                    __attrs_140240884174992 = _static_140241133802128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>\n                          ')

                    # <Static value=<_ast.Dict object at 0x7f8c60159390> name=None at 7f8c60159350> -> __attrs_140240884176336
                    __attrs_140240884176336 = _static_140240884175760

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="ref-type">\n                            ')

                    # <Static value=<_ast.Dict object at 0x7f8c60159890> name=None at 7f8c60159850> -> __attrs_140240884177680
                    __attrs_140240884177680 = _static_140240884177040

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fas fa-arrow-right"></i>\n                            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884178640
                    __attrs_140240884178640 = _static_140241133802128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884178256
                    __default_140240884178256 = _DEFAULT_MARKER

                    # <Value u'ref/type' (318:48)> -> __cache_140240884177936
                    __token = 12847
                    try:
                        __zt_tmp = __attrs_140240884178640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240884177936 = _static_140241087907024('path', u'ref/type', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'ref/type' (318:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60159c90> -> __condition
                    __expression = __cache_140240884177936

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240884177936
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                          </span>\n                        </span>\n                      </div>\n                    </div>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8c61646e50> name=None at 7f8c61646d50> -> __attrs_140240884269200
                    __attrs_140240884269200 = _static_140240906120784

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select class="form-control" name="senaite.databox.columns.refs:list:records">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884270032
                    __attrs_140240884270032 = _static_140241133802128
                    __backup_key_140240907195728 = get('key', __marker)

                    # <Value u'ref/fields' (325:44)> -> __iterator
                    __token = 13158
                    try:
                        __zt_tmp = __attrs_140240884270032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('path', u'ref/fields', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240884270160, ) = getitem('repeat')(u'key', __iterator)
                    econtext['key'] = None
                    for __item in __iterator:
                        econtext['key'] = __item
                        __append(u'\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f8c60170610> name=None at 7f8c60170690> -> __attrs_140240884271824
                        __attrs_140240884271824 = _static_140240884270608

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884271248
                        __default_140240884271248 = _DEFAULT_MARKER

                        # <Substitution u'key' (326:54)> -> __attr_value
                        __token = 13225
                        try:
                            __zt_tmp = __attrs_140240884271824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140241087907024('path', u'key', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884271504
                        __default_140240884271504 = _DEFAULT_MARKER

                        # <Boolean u"python:key == ref.get('key') and 'selected' or ''" (326:67)> -> __attr_selected
                        __token = 13238
                        try:
                            __zt_tmp = __attrs_140240884271824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_140241087907024('python', u"key == ref.get('key') and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if (__attr_selected is _DEFAULT_MARKER):
                            __attr_selected = None
                        else:
                            if __attr_selected:
                                __attr_selected = u'selected'
                            else:
                                __attr_selected = None
                        if (__attr_selected is not None):
                            __append((u' selected="%s"' % __attr_selected))
                        __append(u'>\n                          ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884273040
                        __attrs_140240884273040 = _static_140241133802128

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884272912
                        __default_140240884272912 = _DEFAULT_MARKER

                        # <Value u'key' (327:45)> -> __cache_140240884272592
                        __token = 13336
                        try:
                            __zt_tmp = __attrs_140240884273040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240884272592 = _static_140241087907024('path', u'key', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'key' (327:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60170e50> -> __condition
                        __expression = __cache_140240884272592

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>')
                        else:
                            __content = __cache_140240884272592
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                        </option>\n                      ')
                        ____index_140240884270160 -= 1
                        if (____index_140240884270160 > 0):
                            __append('')
                    if (__backup_key_140240907195728 is __marker):
                        del econtext['key']
                    else:
                        econtext['key'] = __backup_key_140240907195728
                    __append(u'\n                    </select>\n                  </div>\n                </div>')
                    ____index_140240907236624 -= 1
                    if (____index_140240907236624 > 0):
                        __append('\n                ')
                if (__backup_ref_140240907017360 is __marker):
                    del econtext['ref']
                else:
                    econtext['ref'] = __backup_ref_140240907017360
                __append(u'\n\n                <!-- add/del column button -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c60170cd0> name=None at 7f8c61646450> -> __attrs_140240884270480
                __attrs_140240884270480 = _static_140240884272336

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex mr-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c60146110> name=None at 7f8c60146150> -> __attrs_140240884098512
                __attrs_140240884098512 = _static_140240884097296

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884098000
                __default_140240884098000 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c60146310> at 7f8c60146350> -> __attr_title
                __attr_title = u'add'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u' class="add_column btn btn-sm btn-outline-success">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c60146890> name=None at 7f8c60146810> -> __attrs_140240884099728
                __attrs_140240884099728 = _static_140240884099216

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-plus"/>\n                  </button>\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c60146ad0> name=None at 7f8c60146710> -> __attrs_140240884101008
                __attrs_140240884101008 = _static_140240884099792

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884100496
                __default_140240884100496 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c60146cd0> at 7f8c60146d10> -> __attr_title
                __attr_title = u'Delete column'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u' class="del_column btn btn-sm btn-outline-danger">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c601422d0> name=None at 7f8c60142290> -> __attrs_140240884081872
                __attrs_140240884081872 = _static_140240884081360

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-minus"/>\n                  </button>\n                </div>\n              </div>\n\n\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c601460d0> name=None at 7f8c60170190> -> __attrs_140240884082128
                __attrs_140240884082128 = _static_140240884097232

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="d-flex text-nowrap">\n                <!-- Code -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c60142910> name=None at 7f8c60142890> -> __attrs_140240884083600
                __attrs_140240884083600 = _static_140240884082960

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c60142e10> name=None at 7f8c60142dd0> -> __attrs_140240884113616
                __attrs_140240884113616 = _static_140240884084240

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm mb-2">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6014a350> name=None at 7f8c6014a310> -> __attrs_140240884114896
                __attrs_140240884114896 = _static_140240884114256

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6014a850> name=None at 7f8c6014a810> -> __attrs_140240884116176
                __attrs_140240884116176 = _static_140240884115536

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c6014ad90> name=None at 7f8c6014ad10> -> __attrs_140240884117456
                __attrs_140240884117456 = _static_140240884116880

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-code"></i>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c601481d0> name=None at 7f8c60148190> -> __attrs_140240884106256
                __attrs_140240884106256 = _static_140240884105680

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="ml-1">')
                __stream_140240884105424 = []
                __append_140240884105424 = __stream_140240884105424.append
                __append_140240884105424(u'Code')
                __msgid_140240884105424 = __re_whitespace(''.join(__stream_140240884105424)).strip()
                if __msgid_140240884105424:
                    __append(translate(__msgid_140240884105424, mapping=None, default=__msgid_140240884105424, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                      </div>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6014a710> name=None at 7f8c6014a7d0> -> __attrs_140240884107728
                __attrs_140240884107728 = _static_140240884115216

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="text" class="form-control" name="senaite.databox.columns.code:records"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884107472
                __default_140240884107472 = _DEFAULT_MARKER

                # <Substitution u"python:columns[column].get('code')" (362:48)> -> __attr_value
                __token = 14717
                try:
                    __zt_tmp = __attrs_140240884107728
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140241087907024('python', u"columns[column].get('code')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((u' value="%s"' % __attr_value))
                __append(u'>\n                  </div>\n                </div>\n\n                <!-- converter -->\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c60148a10> name=None at 7f8c61710190> -> __attrs_140240884108816
                __attrs_140240884108816 = _static_140240884107792

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="flex-fill mr-2" style="max-width:225px">\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8c6014f0d0> name=None at 7f8c6014f090> -> __attrs_140240884134736
                __attrs_140240884134736 = _static_140240884134096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group input-group-sm mb-2">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6014f5d0> name=None at 7f8c6014f590> -> __attrs_140240884136016
                __attrs_140240884136016 = _static_140240884135376

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-prepend">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6014fad0> name=None at 7f8c6014fa90> -> __attrs_140240884137296
                __attrs_140240884137296 = _static_140240884136656

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="input-group-text">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c60149050> name=None at 7f8c6014ffd0> -> __attrs_140240884110032
                __attrs_140240884110032 = _static_140240884109392

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-compress"></i>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8c60149490> name=None at 7f8c60149450> -> __attrs_140240884111056
                __attrs_140240884111056 = _static_140240884110480

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="ml-1">')
                __stream_140240884110224 = []
                __append_140240884110224 = __stream_140240884110224.append
                __append_140240884110224(u'Converter')
                __msgid_140240884110224 = __re_whitespace(''.join(__stream_140240884110224)).strip()
                if __msgid_140240884110224:
                    __append(translate(__msgid_140240884110224, mapping=None, default=__msgid_140240884110224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n                      </div>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8c6014fd90> name=None at 7f8c6014fa50> -> __attrs_140240884111952
                __attrs_140240884111952 = _static_140240884137360

                # <select ... (0:0)
                # --------------------------------------------------------
                __append(u'<select class="form-control" name="senaite.databox.columns.converter:records">\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884112720
                __attrs_140240884112720 = _static_140241133802128
                __backup_converter_140240906947152 = get('converter', __marker)

                # <Value u'view/get_converters' (378:53)> -> __iterator
                __token = 15518
                try:
                    __zt_tmp = __attrs_140240884112720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/get_converters', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240884112912, ) = getitem('repeat')(u'converter', __iterator)
                econtext['converter'] = None
                for __item in __iterator:
                    econtext['converter'] = __item
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8c60141050> name=None at 7f8c60149f90> -> __attrs_140240884078096
                    __attrs_140240884078096 = _static_140240884076624
                    __backup_name_140240906736400 = get('name', __marker)

                    # <Value u'converter/name' (379:49)> -> __value
                    __token = 15589
                    try:
                        __zt_tmp = __attrs_140240884078096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'converter/name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_description_140240884176592 = get('description', __marker)

                    # <Value u'converter/description' (379:76)> -> __value
                    __token = 15616
                    try:
                        __zt_tmp = __attrs_140240884078096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'converter/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['description'] = __value

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884077264
                    __default_140240884077264 = _DEFAULT_MARKER

                    # <Substitution u'name' (380:54)> -> __attr_value
                    __token = 15694
                    try:
                        __zt_tmp = __attrs_140240884078096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140241087907024('path', u'name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884077520
                    __default_140240884077520 = _DEFAULT_MARKER

                    # <Substitution u'converter/description' (381:53)> -> __attr_label
                    __token = 15753
                    try:
                        __zt_tmp = __attrs_140240884078096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_label = _static_140241087907024('path', u'converter/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_label is not None):
                        __append((u' label="%s"' % __attr_label))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884077776
                    __default_140240884077776 = _DEFAULT_MARKER

                    # <Boolean u"python:name == columns[column].get('converter') and 'selected' or ''" (382:55)> -> __attr_selected
                    __token = 15832
                    try:
                        __zt_tmp = __attrs_140240884078096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140241087907024('python', u"name == columns[column].get('converter') and 'selected' or ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = u'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((u' selected="%s"' % __attr_selected))
                    __append(u'>\n                          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884079760
                    __attrs_140240884079760 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884079632
                    __default_140240884079632 = _DEFAULT_MARKER

                    # <Value u'name' (383:45)> -> __cache_140240884079312
                    __token = 15950
                    try:
                        __zt_tmp = __attrs_140240884079760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240884079312 = _static_140241087907024('path', u'name', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'name' (383:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60141b50> -> __condition
                    __expression = __cache_140240884079312

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span/>')
                    else:
                        __content = __cache_140240884079312
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                        </option>')
                    if (__backup_description_140240884176592 is __marker):
                        del econtext['description']
                    else:
                        econtext['description'] = __backup_description_140240884176592
                    if (__backup_name_140240906736400 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140240906736400
                    __append(u'\n                      ')
                    ____index_140240884112912 -= 1
                    if (____index_140240884112912 > 0):
                        __append('')
                if (__backup_converter_140240906947152 is __marker):
                    del econtext['converter']
                else:
                    econtext['converter'] = __backup_converter_140240906947152
                __append(u'\n                    </select>\n                  </div>\n                </div>\n\n              </div>\n\n            </li>')
                ____index_140240907010384 -= 1
                if (____index_140240907010384 > 0):
                    __append('\n            ')
            if (__backup_column_140240906457040 is __marker):
                del econtext['column']
            else:
                econtext['column'] = __backup_column_140240906457040
            if (__backup_columns_140240906133840 is __marker):
                del econtext['columns']
            else:
                econtext['columns'] = __backup_columns_140240906133840
            __append(u'\n          </ul>\n        </div>\n      </div>\n\n      <!-- Info TAB -->\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c616c1550> name=None at 7f8c616c1bd0> -> __attrs_140240884112656
            __attrs_140240884112656 = _static_140240906622288

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="tab-pane fade" id="info" role="tabpanel">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c60141790> name=None at 7f8c60141890> -> __attrs_140240884080336
            __attrs_140240884080336 = _static_140240884078480

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table-borderless mb-4">\n          <!-- Schema fields -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884118160
            __attrs_140240884118160 = _static_140241133802128

            # <Value u"python:request.get('debug', False)" (401:29)> -> __condition
            __token = 16385
            try:
                __zt_tmp = __attrs_140240884118160
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u"request.get('debug', False)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __backup_widget_140240907061904 = get('widget', __marker)

                # <Value u'view/widgets' (402:33)> -> __iterator
                __token = 16454
                try:
                    __zt_tmp = __attrs_140240884118160
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/widgets', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240884118480, ) = getitem('repeat')(u'widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6014b690> name=None at 7f8c6014b650> -> __attrs_140240884119824
                    __attrs_140240884119824 = _static_140240884119184

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td class="text-nowrap font-weight-bold pr-1">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884121296
                    __attrs_140240884121296 = _static_140241133802128

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884120912
                    __default_140240884120912 = _DEFAULT_MARKER

                    # <Value u'widget/label' (404:32)> -> __cache_140240884120528
                    __token = 16560
                    try:
                        __zt_tmp = __attrs_140240884121296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240884120528 = _static_140241087907024('path', u'widget/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/label' (404:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6014bc90> -> __condition
                    __expression = __cache_140240884120528

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240884120528
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n            </td>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884154512
                    __attrs_140240884154512 = _static_140241133802128

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c60154590> name=None at 7f8c60154510> -> __attrs_140240884156368
                    __attrs_140240884156368 = _static_140240884155792

                    # <code ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<code class="text-dark">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884155536
                    __default_140240884155536 = _DEFAULT_MARKER

                    # <Value u'widget/value' (407:61)> -> __cache_140240884155152
                    __token = 16673
                    try:
                        __zt_tmp = __attrs_140240884156368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240884155152 = _static_140241087907024('path', u'widget/value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/value' (407:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c601543d0> -> __condition
                    __expression = __cache_140240884155152

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240884155152
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</code>\n            </td>\n          </tr>')
                    ____index_140240884118480 -= 1
                    if (____index_140240884118480 > 0):
                        __append('\n          ')
                if (__backup_widget_140240907061904 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_140240907061904
            __append(u'\n          <!-- Primary Type -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884156560
            __attrs_140240884156560 = _static_140241133802128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c60154b90> name=None at 7f8c60154b50> -> __attrs_140240884157968
            __attrs_140240884157968 = _static_140240884157328

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="font-weight-bold text-nowrap align-top mr-2">')
            __stream_140240884157200 = []
            __append_140240884157200 = __stream_140240884157200.append
            __append_140240884157200(u'\n              Portal Type\n            ')
            __msgid_140240884157200 = __re_whitespace(''.join(__stream_140240884157200)).strip()
            if __msgid_140240884157200:
                __append(translate(__msgid_140240884157200, mapping=None, default=__msgid_140240884157200, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</td>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884150480
            __attrs_140240884150480 = _static_140241133802128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c60153590> name=None at 7f8c60153510> -> __attrs_140240884152272
            __attrs_140240884152272 = _static_140240884151696

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code class="text-dark">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884151440
            __default_140240884151440 = _DEFAULT_MARKER

            # <Value u'view/databox/query_type' (416:51)> -> __cache_140240884151120
            __token = 16970
            try:
                __zt_tmp = __attrs_140240884152272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240884151120 = _static_140241087907024('path', u'view/databox/query_type', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/databox/query_type' (416:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c601533d0> -> __condition
            __expression = __cache_140240884151120

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240884151120
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</code>\n            </td>\n          </tr>\n          <!-- Catalog -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884152464
            __attrs_140240884152464 = _static_140241133802128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c60153b90> name=None at 7f8c60153b50> -> __attrs_140240884153872
            __attrs_140240884153872 = _static_140240884153232

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="font-weight-bold text-nowrap align-top mr-2">')
            __stream_140240884153104 = []
            __append_140240884153104 = __stream_140240884153104.append
            __append_140240884153104(u'\n              Catalog\n            ')
            __msgid_140240884153104 = __re_whitespace(''.join(__stream_140240884153104)).strip()
            if __msgid_140240884153104:
                __append(translate(__msgid_140240884153104, mapping=None, default=__msgid_140240884153104, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</td>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884179152
            __attrs_140240884179152 = _static_140241133802128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6015a590> name=None at 7f8c6015a510> -> __attrs_140240884180944
            __attrs_140240884180944 = _static_140240884180368

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code class="text-dark">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884180112
            __default_140240884180112 = _DEFAULT_MARKER

            # <Value u'view/databox/get_query_catalog' (425:51)> -> __cache_140240884179792
            __token = 17274
            try:
                __zt_tmp = __attrs_140240884180944
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240884179792 = _static_140241087907024('path', u'view/databox/get_query_catalog', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/databox/get_query_catalog' (425:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6015a3d0> -> __condition
            __expression = __cache_140240884179792

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240884179792
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</code>\n            </td>\n          </tr>\n          <!-- Catalog Query -->\n          ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884181136
            __attrs_140240884181136 = _static_140241133802128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884182032
            __attrs_140240884182032 = _static_140241133802128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6015af10> name=None at 7f8c6015aed0> -> __attrs_140240884187600
            __attrs_140240884187600 = _static_140240884182800

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="font-weight-bold text-nowrap align-top mr-2">')
            __stream_140240884182672 = []
            __append_140240884182672 = __stream_140240884182672.append
            __append_140240884182672(u'\n                Catalog Query\n              ')
            __msgid_140240884182672 = __re_whitespace(''.join(__stream_140240884182672)).strip()
            if __msgid_140240884182672:
                __append(translate(__msgid_140240884182672, mapping=None, default=__msgid_140240884182672, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n            </td>\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884188048
            __attrs_140240884188048 = _static_140241133802128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6015c850> name=None at 7f8c6015c7d0> -> __attrs_140240884189840
            __attrs_140240884189840 = _static_140240884189264

            # <code ... (0:0)
            # --------------------------------------------------------
            __append(u'<code class="text-dark">')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884189008
            __default_140240884189008 = _DEFAULT_MARKER

            # <Value u'view/databox/query' (436:51)> -> __cache_140240884188688
            __token = 17642
            try:
                __zt_tmp = __attrs_140240884189840
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240884188688 = _static_140241087907024('path', u'view/databox/query', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/databox/query' (436:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6015c690> -> __condition
            __expression = __cache_140240884188688

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240884188688
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</code>\n            </td>\n          </tr>\n        </table>\n      </div>\n\n    </div>\n\n    <!-- hidden fields -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c601539d0> name=None at 7f8c60153e50> -> __attrs_140240884190480
            __attrs_140240884190480 = _static_140240884152784

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="submitted" value="1" />\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6015ce10> name=None at 7f8c6015ced0> -> __attrs_140240884216784
            __attrs_140240884216784 = _static_140240884190736

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="tab"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884216528
            __default_140240884216528 = _DEFAULT_MARKER

            # <Substitution u'request/tab|string:query' (446:72)> -> __attr_value
            __token = 17901
            try:
                __zt_tmp = __attrs_140240884216784
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140241087907024('path', u'request/tab|string:query', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'query', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884217680
            __attrs_140240884217680 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884217552
            __default_140240884217552 = _DEFAULT_MARKER

            # <Value u'context/@@authenticator/authenticator' (447:34)> -> __cache_140240884217232
            __token = 17964
            try:
                __zt_tmp = __attrs_140240884217680
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240884217232 = _static_140241087907024('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/@@authenticator/authenticator' (447:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60163610> -> __condition
            __expression = __cache_140240884217232

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input/>')
            else:
                __content = __cache_140240884217232
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    <!-- !TEMPORARY DEACTIVATED!\n         ReactJS managed component -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c60163950> name=None at 7f8c60163a10> -> __attrs_140240884219216
            __attrs_140240884219216 = _static_140240884218192

            # <Value u'python:False' (451:24)> -> __condition
            __token = 18102
            try:
                __zt_tmp = __attrs_140240884219216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('python', u'False', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Value u'view/settings' (453:25)> -> __cache_140240884218832
                __token = 18166
                try:
                    __zt_tmp = __attrs_140240884219216
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240884218832 = _static_140241087907024('path', u'view/settings', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if (u'class' not in __chain(__cache_140240884218832)):
                    __append(u' class="databox"')
                __attr_140240884218896 = __cache_140240884218832
                for (name, value, ) in __attr_140240884218896.items():
                    if ((name not in _static_140240896378384) and (value is not None)):
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(u'>\n    </div>')
            __append(u'\n    <!-- /ReactJS managed component -->\n\n    <!-- submit button -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c60165050> name=None at 7f8c60163fd0> -> __attrs_140240884225616
            __attrs_140240884225616 = _static_140240884224080

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input class="btn btn-sm btn-primary" type="submit" name="form.buttons.save" value="Update" />\n  </form>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140240906451408
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }