# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/resultsinterpretation.pt'

__tokens = {102: (u'python:view.get_panels', 3, 24), 53: (u'python:view.available()', 2, 20), 209: (u'view/icon_name|nothing', 7, 23), 256: (u' view/title|nothin', 8, 23), 300: (u'l context/@@plone_portal_state/port', 9, 23), 360: (u'title', 10, 21), 392: (u'icon|nothing', 11, 24), 426: (u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', 11, 58), 527: (u'title', 12, 41), 635: (u'string:ResultsInterpretationDepts', 17, 26), 689: (u'python:not view.is_edit_allowed()', 18, 19), 912: (u"python:view.get_text(None, 'raw')", 25, 32), 1080: (u'python:text or default', 30, 39), 1192: (u'panels', 35, 31), 1279: (u"python:view.get_text(panel, 'raw')", 37, 32), 1360: (u'panel/Title', 39, 29), 1445: (u'python:text or default', 42, 39), 1641: (u'string:ResultsInterpretationDepts', 53, 26), 1695: (u'python:view.is_edit_allowed()', 54, 19), 1851: (u'here/absolute_url', 59, 33), 2028: (u'context/@@authenticator/authenticator', 64, 36), 2637: (u'view/get_interpretation_templates', 77, 43), 2715: (u'template/uid', 78, 42), 2762: (u'template/title', 79, 33), 3589: (u'string:#${fieldName}-general', 103, 36), 3649: (u' string:${fieldName}-genera', 104, 30), 3777: (u'panels', 107, 36), 4020: (u' string:#${fieldName}-${panel/UID', 114, 28), 3979: (u'panel/Title', 113, 36), 4087: (u"d python:fieldName+'-'+panel.UID", 115, 31), 4154: (u'panel/Title', 116, 30), 4482: (u'string:${fieldName}-general', 125, 34), 4586: (u'string:${fieldName}.uid:records:ignore_empty', 127, 40), 4659: (u' string:${fieldName}-uid-', 128, 27), 4716: (u'e string:gener', 129, 29), 4828: (u'string:${fieldName}.richtext:records:ignore_empty', 131, 43), 4910: (u' string:${fieldName}-richtext-', 132, 31), 4979: (u"python: view.get_text(None, 'raw')", 133, 35), 5093: (u'panels', 137, 35), 5207: (u'panel/UID', 140, 33), 5254: (u'string:${fieldName}-${uid}', 141, 36), 5361: (u'string:${fieldName}.uid:records:ignore_empty', 143, 42), 5436: (u' string:${fieldName}-uid-${repeat/panel/number', 144, 29), 5516: (u'e string:${ui', 145, 31), 5631: (u'string:${fieldName}.richtext:records:ignore_empty', 147, 45), 5715: (u' string:${fieldName}-richtext-${repeat/panel/number', 148, 33), 5807: (u"python:view.get_text(panel, 'raw')", 149, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168027390352 = {u'class': u'custom-select', u'id': u'interpretationtemplate', u'name': u'interpretationtemplate', }
_static_140168004208848 = {u'type': u'hidden', u'name': u'submitted', u'value': u'1', }
_static_140168027394000 = {u'value': u'', }
_static_140168027478288 = {u'type': u'submit', u'class': u'btn btn-primary btn-sm', }
_static_140168037362128 = {u'class': u'resultsinterpretations', }
_static_140168004136336 = {u'action': u'.', u'method': u'POST', u'enctype': u'multipart/form-data', u'class': u'form', u'name': u'arresultsinterpretation_form', }
_static_140168004274896 = {u'id': u'results-interpretation', }
_static_140168027477840 = {u'role': u'tabpanel', u'class': u'tab-pane fade show active', u'id': u'string:${fieldName}-general', }
_static_140168037336336 = {u'id': u'general', u'href': u'#', u'role': u'tab', u'data-uid': u'string:${fieldName}-general', u'data-toggle': u'tab', u'class': u'nav-link active', }
_static_140168004140496 = {u'value': u'template/uid', }
_static_140168027391376 = {u'class': u'arresultsinterpretation-container mb-2', }
_static_140168027393552 = {u'class': u'input-group-text', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168046937552 = {u'type': u'hidden', u'name': u'string:${fieldName}.uid:records:ignore_empty', u'value': u'string:${uid}', u'id': u'string:${fieldName}-uid-${repeat/panel/number}', }
_static_140168004138128 = {u'class': u'btn btn-outline-primary btn-sm', u'type': u'submit', u'id': u'interpretationtemplate-insert', u'name': u'interpretationtemplate-insert', }
_static_140168003987088 = {u'id': u'string:${fieldName}-richtext-0', u'class': u'my-2 mce_editable', u'name': u'string:${fieldName}.richtext:records:ignore_empty', }
_static_140168036944592 = {u'id': u'panel/Title', u'href': u'#', u'role': u'tab', u'data-uid': u"python:fieldName+'-'+panel.UID()", u'data-toggle': u'tab', u'class': u'nav-link', }
_static_140168026598864 = {u'class': u'table-borderless w-100', }
_static_140168037335888 = {u'class': u'nav-item', }
_static_140168016889424 = {u'class': u'tab-content p-2 border-left border-bottom border-right', }
_static_140168257770128 = {}
_static_140168027432080 = {u'id': u'string:${fieldName}-richtext-${repeat/panel/number}', u'class': u'my-2 mce_editable', u'name': u'string:${fieldName}.richtext:records:ignore_empty', }
_static_140168208991440 = __compile_zt_expr
_static_140168016891408 = {u'class': u'nav-item', }
_static_140168027479952 = {u'type': u'hidden', u'name': u'string:${fieldName}.uid:records:ignore_empty', u'value': u'string:general', u'id': u'string:${fieldName}-uid-0', }
_static_140168046865424 = {u'src': u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', }
_static_140168015745552 = {u'class': u'nav nav-tabs', u'roles': u'tablist', }
_static_140168004209424 = {u'class': u'input-group input-group-sm flex-nowrap d-inline-flex w-auto mb-3 arinterpretationtemplates-selector', }
_static_140168006675152 = {u'class': u'input-group-prepend', }
_static_140168037250576 = {u'class': u'table-borderless w-100', }
_static_140168015860304 = {u'role': u'tabpanel', u'class': u'tab-pane fade', u'id': u'string:${fieldName}-${uid}', }
_static_140168004137872 = {u'class': u'input-group-append', }

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

            # <Static value=<_ast.Dict object at 0x7f7b681a8ad0> name=None at 7f7b681a86d0> -> __attrs_140168004275344
            __attrs_140168004275344 = _static_140168004274896
            __backup_panels_140168004275792 = get('panels', __marker)

            # <Value u'python:view.get_panels' (3:24)> -> __value
            __token = 102
            try:
                __zt_tmp = __attrs_140168004275344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.get_panels', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['panels'] = __value

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_140168004275344
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.available()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168037628496 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="results-interpretation">\n\n  <!-- title and icon -->\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047842640
                __attrs_140168047842640 = _static_140168257770128
                __backup_icon_140168047762576 = get('icon', __marker)

                # <Value u'view/icon_name|nothing' (7:23)> -> __value
                __token = 209
                try:
                    __zt_tmp = __attrs_140168047842640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/icon_name|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['icon'] = __value
                __backup_title_140168037629584 = get('title', __marker)

                # <Value u'view/title|nothing' (8:23)> -> __value
                __token = 256
                try:
                    __zt_tmp = __attrs_140168047842640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['title'] = __value
                __backup_portal_140168047842960 = get('portal', __marker)

                # <Value u'context/@@plone_portal_state/portal' (9:23)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_140168047842640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['portal'] = __value

                # <Value u'title' (10:21)> -> __condition
                __token = 360
                try:
                    __zt_tmp = __attrs_140168047842640
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa46c10> name=None at 7f7b6aa46690> -> __attrs_140168037361936
                    __attrs_140168037361936 = _static_140168046865424

                    # <Value u'icon|nothing' (11:24)> -> __condition
                    __token = 392
                    try:
                        __zt_tmp = __attrs_140168037361936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'icon|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037363024
                        __default_140168037363024 = _DEFAULT_MARKER

                        # <Substitution u'string:${portal/absolute_url}/senaite_theme/icon/${icon}' (11:58)> -> __attr_src
                        __token = 426
                        try:
                            __zt_tmp = __attrs_140168037361936
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140168208991440('string', u'${portal/absolute_url}/senaite_theme/icon/${icon}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))
                        __append(u'/>')
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037360528
                    __attrs_140168037360528 = _static_140168257770128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037363536
                    __default_140168037363536 = _DEFAULT_MARKER

                    # <Value u'title' (12:41)> -> __cache_140168037361296
                    __token = 527
                    try:
                        __zt_tmp = __attrs_140168037360528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037361296 = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'title' (12:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a136dd0> -> __condition
                    __expression = __cache_140168037361296

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168037361296
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n  </h3>')
                if (__backup_portal_140168047842960 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_140168047842960
                if (__backup_title_140168037629584 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140168037629584
                if (__backup_icon_140168047762576 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140168047762576
                __append(u'\n\n  <!-- Readonly Resultsinterpretation Field -->\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037360912
                __attrs_140168037360912 = _static_140168257770128
                __backup_fieldName_140168037629712 = get('fieldName', __marker)

                # <Value u'string:ResultsInterpretationDepts' (17:26)> -> __value
                __token = 635
                try:
                    __zt_tmp = __attrs_140168037360912
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('string', u'ResultsInterpretationDepts', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['fieldName'] = __value

                # <Value u'python:not view.is_edit_allowed()' (18:19)> -> __condition
                __token = 689
                try:
                    __zt_tmp = __attrs_140168037360912
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'not view.is_edit_allowed()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a1369d0> name=None at 7f7b6a136790> -> __attrs_140168037249104
                    __attrs_140168037249104 = _static_140168037362128

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="resultsinterpretations">\n\n      <!-- General Results Interpretation -->\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037249488
                    __attrs_140168037249488 = _static_140168257770128
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a11b610> name=None at 7f7b6a11b590> -> __attrs_140168037250000
                    __attrs_140168037250000 = _static_140168037250576
                    __backup_text_140168037250384 = get('text', __marker)

                    # <Value u"python:view.get_text(None, 'raw')" (25:32)> -> __value
                    __token = 912
                    try:
                        __zt_tmp = __attrs_140168037250000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140168208991440('python', u"view.get_text(None, 'raw')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    econtext['text'] = __value

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<table class="table-borderless w-100">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015803408
                    __attrs_140168015803408 = _static_140168257770128

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015804304
                    __attrs_140168015804304 = _static_140168257770128

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th>')
                    __stream_140168015803984 = []
                    __append_140168015803984 = __stream_140168015803984.append
                    __append_140168015803984(u'General')
                    __msgid_140168015803984 = __re_whitespace(''.join(__stream_140168015803984)).strip()
                    if __msgid_140168015803984:
                        __append(translate(__msgid_140168015803984, mapping=None, default=__msgid_140168015803984, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</th>\n          </tr>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015805968
                    __attrs_140168015805968 = _static_140168257770128

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026597392
                    __attrs_140168026597392 = _static_140168257770128

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168015803216
                    __default_140168015803216 = _DEFAULT_MARKER

                    # <Value u'python:text or default' (30:39)> -> __cache_140168015805008
                    __token = 1080
                    try:
                        __zt_tmp = __attrs_140168026597392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168015805008 = _static_140168208991440('python', u'text or default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:text or default' (30:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68ca7090> -> __condition
                    __expression = __cache_140168015805008

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168015805008
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</td>\n          </tr>\n        </table>')
                    if (__backup_text_140168037250384 is __marker):
                        del econtext['text']
                    else:
                        econtext['text'] = __backup_text_140168037250384
                    __append(u'\n      \n\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037251152
                    __attrs_140168037251152 = _static_140168257770128
                    __backup_panel_140168047842320 = get('panel', __marker)

                    # <Value u'panels' (35:31)> -> __iterator
                    __token = 1192
                    try:
                        __zt_tmp = __attrs_140168037251152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'panels', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168037251984, ) = getitem('repeat')(u'panel', __iterator)
                    econtext['panel'] = None
                    for __item in __iterator:
                        econtext['panel'] = __item
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7f7b696f2dd0> name=None at 7f7b696f28d0> -> __attrs_140168026599056
                        __attrs_140168026599056 = _static_140168026598864
                        __backup_text_140168037250064 = get('text', __marker)

                        # <Value u"python:view.get_text(panel, 'raw')" (37:32)> -> __value
                        __token = 1279
                        try:
                            __zt_tmp = __attrs_140168026599056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u"view.get_text(panel, 'raw')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['text'] = __value

                        # <table ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<table class="table-borderless w-100">\n          ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026596496
                        __attrs_140168026596496 = _static_140168257770128

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tr>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026595664
                        __attrs_140168026595664 = _static_140168257770128

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<th>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026597712
                        __default_140168026597712 = _DEFAULT_MARKER

                        # <Value u'panel/Title' (39:29)> -> __cache_140168026596560
                        __token = 1360
                        try:
                            __zt_tmp = __attrs_140168026595664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168026596560 = _static_140168208991440('path', u'panel/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'panel/Title' (39:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696f2910> -> __condition
                        __expression = __cache_140168026596560

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168026596560
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</th>\n          </tr>\n          ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026599120
                        __attrs_140168026599120 = _static_140168257770128

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tr>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168004136848
                        __attrs_140168004136848 = _static_140168257770128

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168004133584
                        __default_140168004133584 = _DEFAULT_MARKER

                        # <Value u'python:text or default' (42:39)> -> __cache_140168004136720
                        __token = 1445
                        try:
                            __zt_tmp = __attrs_140168004136848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168004136720 = _static_140168208991440('python', u'text or default', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:text or default' (42:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68186d10> -> __condition
                        __expression = __cache_140168004136720

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168004136720
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</td>\n          </tr>\n        </table>')
                        if (__backup_text_140168037250064 is __marker):
                            del econtext['text']
                        else:
                            econtext['text'] = __backup_text_140168037250064
                        __append(u'\n      ')
                        ____index_140168037251984 -= 1
                        if (____index_140168037251984 > 0):
                            __append('')
                    if (__backup_panel_140168047842320 is __marker):
                        del econtext['panel']
                    else:
                        econtext['panel'] = __backup_panel_140168047842320
                    __append(u'\n\n    </div>\n  ')
                if (__backup_fieldName_140168037629712 is __marker):
                    del econtext['fieldName']
                else:
                    econtext['fieldName'] = __backup_fieldName_140168037629712
                __append(u'\n\n\n  <!-- Editable Resultsinterpretation Field -->\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037250768
                __attrs_140168037250768 = _static_140168257770128
                __backup_fieldName_140168047844176 = get('fieldName', __marker)

                # <Value u'string:ResultsInterpretationDepts' (53:26)> -> __value
                __token = 1641
                try:
                    __zt_tmp = __attrs_140168037250768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('string', u'ResultsInterpretationDepts', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['fieldName'] = __value

                # <Value u'python:view.is_edit_allowed()' (54:19)> -> __condition
                __token = 1695
                try:
                    __zt_tmp = __attrs_140168037250768
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'view.is_edit_allowed()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n\n    ')

                    # <Static value=<_ast.Dict object at 0x7f7b68186d90> name=None at 7f7b681868d0> -> __attrs_140168004134928
                    __attrs_140168004134928 = _static_140168004136336

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form class="form" name="arresultsinterpretation_form"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168004134480
                    __default_140168004134480 = _DEFAULT_MARKER

                    # <Substitution u'here/absolute_url' (59:33)> -> __attr_action
                    __token = 1851
                    try:
                        __zt_tmp = __attrs_140168004134928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140168208991440('path', u'here/absolute_url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', u'.', _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u' enctype="multipart/form-data" method="POST">\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b681988d0> name=None at 7f7b68186150> -> __attrs_140168004207760
                    __attrs_140168004207760 = _static_140168004208848

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="submitted" value="1"/>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168004208016
                    __attrs_140168004208016 = _static_140168257770128

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168004208144
                    __default_140168004208144 = _DEFAULT_MARKER

                    # <Value u'context/@@authenticator/authenticator' (64:36)> -> __cache_140168004208208
                    __token = 2028
                    try:
                        __zt_tmp = __attrs_140168004208016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168004208208 = _static_140168208991440('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'context/@@authenticator/authenticator' (64:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68198ed0> -> __condition
                    __expression = __cache_140168004208208

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input/>')
                    else:
                        __content = __cache_140168004208208
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n      <!-- Interpretation templates selector -->\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b68198b10> name=None at 7f7b68198890> -> __attrs_140168004209232
                    __attrs_140168004209232 = _static_140168004209424

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group input-group-sm flex-nowrap d-inline-flex w-auto mb-3 arinterpretationtemplates-selector">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b683f2ad0> name=None at 7f7b683f20d0> -> __attrs_140168036804176
                    __attrs_140168036804176 = _static_140168006675152

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-prepend">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b697b4e10> name=None at 7f7b697b4090> -> __attrs_140168027391504
                    __attrs_140168027391504 = _static_140168027393552

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="input-group-text">')
                    __stream_140168036804752 = []
                    __append_140168036804752 = __stream_140168036804752.append
                    __append_140168036804752(u'\n            Template\n          ')
                    __msgid_140168036804752 = __re_whitespace(''.join(__stream_140168036804752)).strip()
                    if __msgid_140168036804752:
                        __append(translate(__msgid_140168036804752, mapping=None, default=__msgid_140168036804752, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        </div>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b697b4190> name=None at 7f7b697b42d0> -> __attrs_140168027392720
                    __attrs_140168027392720 = _static_140168027390352

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select id="interpretationtemplate" name="interpretationtemplate" class="custom-select">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b697b4fd0> name=None at 7f7b697b4f90> -> __attrs_140168027390160
                    __attrs_140168027390160 = _static_140168027394000

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option value="">')
                    __stream_140168027391312 = []
                    __append_140168027391312 = __stream_140168027391312.append
                    __append_140168027391312(u'Select template')
                    __msgid_140168027391312 = __re_whitespace(''.join(__stream_140168027391312)).strip()
                    if __msgid_140168027391312:
                        __append(translate(__msgid_140168027391312, mapping=None, default=__msgid_140168027391312, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</option>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168004138256
                    __attrs_140168004138256 = _static_140168257770128
                    __backup_template_140168015803728 = get('template', __marker)

                    # <Value u'view/get_interpretation_templates' (77:43)> -> __iterator
                    __token = 2637
                    try:
                        __zt_tmp = __attrs_140168004138256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'view/get_interpretation_templates', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168004139024, ) = getitem('repeat')(u'template', __iterator)
                    econtext['template'] = None
                    for __item in __iterator:
                        econtext['template'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b68187dd0> name=None at 7f7b68187710> -> __attrs_140168004137104
                        __attrs_140168004137104 = _static_140168004140496

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168004139792
                        __default_140168004139792 = _DEFAULT_MARKER

                        # <Substitution u'template/uid' (78:42)> -> __attr_value
                        __token = 2715
                        try:
                            __zt_tmp = __attrs_140168004137104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('path', u'template/uid', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168004140432
                        __default_140168004140432 = _DEFAULT_MARKER

                        # <Value u'template/title' (79:33)> -> __cache_140168004138064
                        __token = 2762
                        try:
                            __zt_tmp = __attrs_140168004137104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168004138064 = _static_140168208991440('path', u'template/title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'template/title' (79:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68187590> -> __condition
                        __expression = __cache_140168004138064

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168004138064
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>\n          ')
                        ____index_140168004139024 -= 1
                        if (____index_140168004139024 > 0):
                            __append('')
                    if (__backup_template_140168015803728 is __marker):
                        del econtext['template']
                    else:
                        econtext['template'] = __backup_template_140168015803728
                    __append(u'\n        </select>\n        <!-- Template insert button -->\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b68187390> name=None at 7f7b68187290> -> __attrs_140168004141008
                    __attrs_140168004141008 = _static_140168004137872

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="input-group-append">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b68187490> name=None at 7f7b68187e50> -> __attrs_140168036706192
                    __attrs_140168036706192 = _static_140168004138128

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<button id="interpretationtemplate-insert" name="interpretationtemplate-insert" type="submit" class="btn btn-outline-primary btn-sm">')
                    __stream_140168004137360 = []
                    __append_140168004137360 = __stream_140168004137360.append
                    __append_140168004137360(u'\n            Use Template\n          ')
                    __msgid_140168004137360 = __re_whitespace(''.join(__stream_140168004137360)).strip()
                    if __msgid_140168004137360:
                        __append(translate(__msgid_140168004137360, mapping=None, default=__msgid_140168004137360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</button>\n        </div>\n      </div>\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b697b4590> name=None at 7f7b68187c90> -> __attrs_140168015747664
                    __attrs_140168015747664 = _static_140168027391376

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="arresultsinterpretation-container mb-2">\n        <!-- Tabs for panels (departments) -->\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b68c99210> name=None at 7f7b68c99e10> -> __attrs_140168015746320
                    __attrs_140168015746320 = _static_140168015745552

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="nav nav-tabs" roles="tablist">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a130350> name=None at 7f7b6a130e50> -> __attrs_140168037338448
                    __attrs_140168037338448 = _static_140168037335888

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="nav-item">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a130510> name=None at 7f7b6a1303d0> -> __attrs_140168016888592
                    __attrs_140168016888592 = _static_140168037336336

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a class="nav-link active" data-toggle="tab"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037336400
                    __default_140168037336400 = _DEFAULT_MARKER

                    # <Substitution u'string:#${fieldName}-general' (103:36)> -> __attr_href
                    __token = 3589
                    try:
                        __zt_tmp = __attrs_140168016888592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('string', u'#${fieldName}-general', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u' role="tab" id="general"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016890576
                    __default_140168016890576 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}-general' (104:30)> -> __attr_data_uid
                    __token = 3649
                    try:
                        __zt_tmp = __attrs_140168016888592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_uid = _static_140168208991440('string', u'${fieldName}-general', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_data_uid = __quote(__attr_data_uid, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_uid is not None):
                        __append((u' data-uid="%s"' % __attr_data_uid))
                    __append(u'>')
                    __stream_140168037335760 = []
                    __append_140168037335760 = __stream_140168037335760.append
                    __append_140168037335760(u'General')
                    __msgid_140168037335760 = __re_whitespace(''.join(__stream_140168037335760)).strip()
                    if __msgid_140168037335760:
                        __append(translate(__msgid_140168037335760, mapping=None, default=__msgid_140168037335760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</a>\n          </li>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016890000
                    __attrs_140168016890000 = _static_140168257770128
                    __backup_panel_140168015805392 = get('panel', __marker)

                    # <Value u'panels' (107:36)> -> __iterator
                    __token = 3777
                    try:
                        __zt_tmp = __attrs_140168016890000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'panels', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168016891344, ) = getitem('repeat')(u'panel', __iterator)
                    econtext['panel'] = None
                    for __item in __iterator:
                        econtext['panel'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b68db0e10> name=None at 7f7b68db0d50> -> __attrs_140168016891664
                        __attrs_140168016891664 = _static_140168016891408

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="nav-item">\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b6a0d0ad0> name=None at 7f7b68db01d0> -> __attrs_140168027478992
                        __attrs_140168027478992 = _static_140168036944592

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a class="nav-link" data-toggle="tab"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047361424
                        __default_140168047361424 = _DEFAULT_MARKER

                        # <Substitution u'string:#${fieldName}-${panel/UID}' (114:28)> -> __attr_href
                        __token = 4020
                        try:
                            __zt_tmp = __attrs_140168027478992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140168208991440('string', u'#${fieldName}-${panel/UID}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u' role="tab"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047359312
                        __default_140168047359312 = _DEFAULT_MARKER

                        # <Substitution u'panel/Title' (113:36)> -> __attr_id
                        __token = 3979
                        try:
                            __zt_tmp = __attrs_140168027478992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('path', u'panel/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027479760
                        __default_140168027479760 = _DEFAULT_MARKER

                        # <Substitution u"python:fieldName+'-'+panel.UID()" (115:31)> -> __attr_data_uid
                        __token = 4087
                        try:
                            __zt_tmp = __attrs_140168027478992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_data_uid = _static_140168208991440('python', u"fieldName+'-'+panel.UID()", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_data_uid = __quote(__attr_data_uid, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_data_uid is not None):
                            __append((u' data-uid="%s"' % __attr_data_uid))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168016891728
                        __default_140168016891728 = _DEFAULT_MARKER

                        # <Value u'panel/Title' (116:30)> -> __cache_140168016888784
                        __token = 4154
                        try:
                            __zt_tmp = __attrs_140168027478992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168016888784 = _static_140168208991440('path', u'panel/Title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'panel/Title' (116:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b68db05d0> -> __condition
                        __expression = __cache_140168016888784

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168016888784
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</a>\n            </li>\n          ')
                        ____index_140168016891344 -= 1
                        if (____index_140168016891344 > 0):
                            __append('')
                    if (__backup_panel_140168015805392 is __marker):
                        del econtext['panel']
                    else:
                        econtext['panel'] = __backup_panel_140168015805392
                    __append(u'\n        </ul>\n\n        <!-- TextAreas (RichText) for results interpretation -->\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b68db0650> name=None at 7f7b68db0390> -> __attrs_140168027478480
                    __attrs_140168027478480 = _static_140168016889424

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="tab-content p-2 border-left border-bottom border-right">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b697c9750> name=None at 7f7b697c9b10> -> __attrs_140168027477904
                    __attrs_140168027477904 = _static_140168027477840

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="tab-pane fade show active" role="tabpanel"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027476752
                    __default_140168027476752 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}-general' (125:34)> -> __attr_id
                    __token = 4482
                    try:
                        __zt_tmp = __attrs_140168027477904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('string', u'${fieldName}-general', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b697c9f90> name=None at 7f7b697c9890> -> __attrs_140168003989136
                    __attrs_140168003989136 = _static_140168027479952

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003988240
                    __default_140168003988240 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}.uid:records:ignore_empty' (127:40)> -> __attr_name
                    __token = 4586
                    try:
                        __zt_tmp = __attrs_140168003989136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'${fieldName}.uid:records:ignore_empty', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003986576
                    __default_140168003986576 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}-uid-0' (128:27)> -> __attr_id
                    __token = 4659
                    try:
                        __zt_tmp = __attrs_140168003989136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('string', u'${fieldName}-uid-0', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003986640
                    __default_140168003986640 = _DEFAULT_MARKER

                    # <Substitution u'string:general' (129:29)> -> __attr_value
                    __token = 4716
                    try:
                        __zt_tmp = __attrs_140168003989136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140168208991440('string', u'general', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'/>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b68162690> name=None at 7f7b68162950> -> __attrs_140168003988368
                    __attrs_140168003988368 = _static_140168003987088

                    # <textarea ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<textarea class="my-2 mce_editable"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003987152
                    __default_140168003987152 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}.richtext:records:ignore_empty' (131:43)> -> __attr_name
                    __token = 4828
                    try:
                        __zt_tmp = __attrs_140168003988368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140168208991440('string', u'${fieldName}.richtext:records:ignore_empty', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((u' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003987664
                    __default_140168003987664 = _DEFAULT_MARKER

                    # <Substitution u'string:${fieldName}-richtext-0' (132:31)> -> __attr_id
                    __token = 4910
                    try:
                        __zt_tmp = __attrs_140168003988368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140168208991440('string', u'${fieldName}-richtext-0', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168003987600
                    __default_140168003987600 = _DEFAULT_MARKER

                    # <Value u"python: view.get_text(None, 'raw')" (133:35)> -> __cache_140168003987472
                    __token = 4979
                    try:
                        __zt_tmp = __attrs_140168003988368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168003987472 = _static_140168208991440('python', u" view.get_text(None, 'raw')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python: view.get_text(None, 'raw')" (133:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b681629d0> -> __condition
                    __expression = __cache_140168003987472

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n            ')
                    else:
                        __content = __cache_140168003987472
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</textarea>\n          </div>\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168015862032
                    __attrs_140168015862032 = _static_140168257770128
                    __backup_panel_140168004138960 = get('panel', __marker)

                    # <Value u'panels' (137:35)> -> __iterator
                    __token = 5093
                    try:
                        __zt_tmp = __attrs_140168015862032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'panels', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168015862928, ) = getitem('repeat')(u'panel', __iterator)
                    econtext['panel'] = None
                    for __item in __iterator:
                        econtext['panel'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b68cb5250> name=None at 7f7b68cb5d90> -> __attrs_140168046937232
                        __attrs_140168046937232 = _static_140168015860304
                        __backup_uid_140168015805840 = get('uid', __marker)

                        # <Value u'panel/UID' (140:33)> -> __value
                        __token = 5207
                        try:
                            __zt_tmp = __attrs_140168046937232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('path', u'panel/UID', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['uid'] = __value

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="tab-pane fade" role="tabpanel"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037644240
                        __default_140168037644240 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}-${uid}' (141:36)> -> __attr_id
                        __token = 5254
                        try:
                            __zt_tmp = __attrs_140168046937232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}-${uid}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b6aa585d0> name=None at 7f7b6aa58f10> -> __attrs_140168027434576
                        __attrs_140168027434576 = _static_140168046937552

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046936400
                        __default_140168046936400 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}.uid:records:ignore_empty' (143:42)> -> __attr_name
                        __token = 5361
                        try:
                            __zt_tmp = __attrs_140168027434576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('string', u'${fieldName}.uid:records:ignore_empty', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046939856
                        __default_140168046939856 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}-uid-${repeat/panel/number}' (144:29)> -> __attr_id
                        __token = 5436
                        try:
                            __zt_tmp = __attrs_140168027434576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}-uid-${repeat/panel/number}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027434832
                        __default_140168027434832 = _DEFAULT_MARKER

                        # <Substitution u'string:${uid}' (145:31)> -> __attr_value
                        __token = 5516
                        try:
                            __zt_tmp = __attrs_140168027434576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140168208991440('string', u'${uid}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u'/>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b697be490> name=None at 7f7b697be790> -> __attrs_140168027434000
                        __attrs_140168027434000 = _static_140168027432080

                        # <textarea ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<textarea class="my-2 mce_editable"')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027431760
                        __default_140168027431760 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}.richtext:records:ignore_empty' (147:45)> -> __attr_name
                        __token = 5631
                        try:
                            __zt_tmp = __attrs_140168027434000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140168208991440('string', u'${fieldName}.richtext:records:ignore_empty', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((u' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027433232
                        __default_140168027433232 = _DEFAULT_MARKER

                        # <Substitution u'string:${fieldName}-richtext-${repeat/panel/number}' (148:33)> -> __attr_id
                        __token = 5715
                        try:
                            __zt_tmp = __attrs_140168027434000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140168208991440('string', u'${fieldName}-richtext-${repeat/panel/number}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027433488
                        __default_140168027433488 = _DEFAULT_MARKER

                        # <Value u"python:view.get_text(panel, 'raw')" (149:37)> -> __cache_140168027434128
                        __token = 5807
                        try:
                            __zt_tmp = __attrs_140168027434000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168027434128 = _static_140168208991440('python', u"view.get_text(panel, 'raw')", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:view.get_text(panel, 'raw')" (149:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b697be710> -> __condition
                        __expression = __cache_140168027434128

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              ')
                        else:
                            __content = __cache_140168027434128
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</textarea>\n            </div>')
                        if (__backup_uid_140168015805840 is __marker):
                            del econtext['uid']
                        else:
                            econtext['uid'] = __backup_uid_140168015805840
                        __append(u'\n          ')
                        ____index_140168015862928 -= 1
                        if (____index_140168015862928 > 0):
                            __append('')
                    if (__backup_panel_140168004138960 is __marker):
                        del econtext['panel']
                    else:
                        econtext['panel'] = __backup_panel_140168004138960
                    __append(u'\n        </div>\n      </div>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f7b697c9910> name=None at 7f7b697c9b90> -> __attrs_140168027434768
                    __attrs_140168027434768 = _static_140168027478288

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<button type="submit" class="btn btn-primary btn-sm">')
                    __stream_140168027478608 = []
                    __append_140168027478608 = __stream_140168027478608.append
                    __append_140168027478608(u'Save')
                    __msgid_140168027478608 = __re_whitespace(''.join(__stream_140168027478608)).strip()
                    if __msgid_140168027478608:
                        __append(translate(__msgid_140168027478608, mapping=None, default=__msgid_140168027478608, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</button>\n    </form>\n  ')
                if (__backup_fieldName_140168047844176 is __marker):
                    del econtext['fieldName']
                else:
                    econtext['fieldName'] = __backup_fieldName_140168047844176
                __append(u'\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140168037628496
            if (__backup_panels_140168004275792 is __marker):
                del econtext['panels']
            else:
                econtext['panels'] = __backup_panels_140168004275792
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }