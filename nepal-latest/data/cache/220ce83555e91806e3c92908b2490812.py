# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/controlpanel/templates/setupview.pt'

__tokens = {438: (u"python:request.set('disable_plone.leftcolumn', 1)", 12, 51), 539: (u" python:request.set('disable_plone.rightcolumn', 1", 13, 50), 679: (u'context/@@plone_portal_state/portal', 16, 36), 835: (u'string:${portal/absolute_url}/++plone++senaite.core.static/js/senaite.core.setupview.js', 19, 34), 1429: (u'python:view.setup', 36, 37), 1630: (u'setup/absolute_url', 39, 36), 1686: (u' setup/Titl', 40, 36), 1860: (u"python:view.get_icon_for(setup, css_class='icon')", 44, 44), 2059: (u'setup/Title', 47, 34), 2284: (u'view/setupitems', 56, 36), 2477: (u'item/absolute_url', 59, 36), 2532: (u' item/Titl', 60, 36), 2739: (u"python:view.get_icon_for(item, css_class='icon')", 65, 44), 2902: (u'item/Title', 68, 35), 3076: (u'python:view.get_count(item)', 73, 37), 3139: (u'python:count>0', 74, 34), 3239: (u'count', 76, 37), 3375: (u'python:count == 1', 79, 37), 3549: (u'python:count > 1', 82, 37), 261: (u'here/prefs_main_template/macros/master', 6, 23), 261: (u'here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240906134800 = {u'id': u'lims-controlpanel', }
_static_140241087907024 = __compile_zt_expr
_static_140241133802128 = {}
_static_140240906931792 = {u'src': u'#', u'class': u'icon', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240906722064 = {u'href': u'setup/absolute_url', u'class': u'tile setup text-capitalized text-decoration-none', u'title': u'setup/Title', }
_static_140240906640080 = {u'class': u'small text-right', }
_static_140240906645584 = {u'class': u'text-secondary', }
_static_140240917782224 = {u'placeholder': u'Type to filter ...', u'autofocus': '', u'type': u'text', u'id': u'searchbox', u'class': u'form-control form-control-lg', }
_static_140240907506000 = {u'id': u'setupview', u'class': u'row', }
_static_140240907429072 = {u'class': u'item text-truncate', }
_static_140240906802832 = {u'class': u'text-secondary', }
_static_140240906425040 = u'master'
_static_140240906648400 = {u'class': u'text-secondary', }
_static_140240906134032 = {u'src': u'senaite.core.setupview.js', u'type': u'text/javascript', }
_static_140240906929168 = {u'class': u'title', }
_static_140240907572944 = {u'class': u'tilewrapper col-xs-12 col-sm-6 col-md-4 col-lg-3', }
_static_140240906672656 = {u'href': u'item/absolute_url', u'class': u'tile text-capitalized text-decoration-none', u'title': u'item/Title', }
_static_140240907729552 = {u'class': u'tilewrapper col-xs-12 col-sm-6 col-md-4 col-lg-3', }
_static_140240907574992 = {u'src': u'#', }
_static_140240907049296 = {u'class': u'item text-truncate', }
_static_140240907509520 = {u'class': u'col-sm-12 mb-4', }
_static_140240907572688 = {u'class': u'title vcenter text-truncate d-inline-block', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240917091600
            __attrs_140240917091600 = _static_140241133802128
            __previous_i18n_domain_140240906739088 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140240933552928 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c616912d0> name=None at 7f8c617cbfd0> -> __value
            __value = _static_140240906425040
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906501584
                __attrs_140240906501584 = _static_140241133802128
                __backup_disable_column_one_140240907112912 = get('disable_column_one', __marker)

                # <Value u"python:request.set('disable_plone.leftcolumn', 1)" (12:51)> -> __value
                __token = 438
                try:
                    __zt_tmp = __attrs_140240906501584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u"request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140240907115088 = get('disable_column_two', __marker)

                # <Value u"python:request.set('disable_plone.rightcolumn', 1)" (13:50)> -> __value
                __token = 539
                try:
                    __zt_tmp = __attrs_140240906501584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u"request.set('disable_plone.rightcolumn', 1)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140240907115088 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140240907115088
                if (__backup_disable_column_one_140240907112912 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140240907112912
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_senaite_legacy_js(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906190416
                __attrs_140240906190416 = _static_140241133802128
                __backup_portal_140241184956048 = get('portal', __marker)

                # <Value u'context/@@plone_portal_state/portal' (16:36)> -> __value
                __token = 679
                try:
                    __zt_tmp = __attrs_140240906190416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['portal'] = __value
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c6164a210> name=None at 7f8c6164a690> -> __attrs_140240917095952
                __attrs_140240917095952 = _static_140240906134032

                # <script ... (0:0)
                # --------------------------------------------------------
                __append(u'<script type="text/javascript"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906548176
                __default_140240906548176 = _DEFAULT_MARKER

                # <Substitution u'string:${portal/absolute_url}/++plone++senaite.core.static/js/senaite.core.setupview.js' (19:34)> -> __attr_src
                __token = 835
                try:
                    __zt_tmp = __attrs_140240917095952
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140241087907024('string', u'${portal/absolute_url}/++plone++senaite.core.static/js/senaite.core.setupview.js', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', u'senaite.core.setupview.js', _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))
                __append(u'></script>\n    ')
                if (__backup_portal_140241184956048 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_140241184956048
            _slots = econtext[u'__slot_senaite_legacy_js'] = _deque((__fill_senaite_legacy_js, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6164a510> name=None at 7f8c6164ad50> -> __attrs_140240917094736
                __attrs_140240917094736 = _static_140240906134800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="lims-controlpanel">\n\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c61799150> name=None at 7f8c61799290> -> __attrs_140240907507536
                __attrs_140240907507536 = _static_140240907506000

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="setupview" class="row">\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c61799f10> name=None at 7f8c61799dd0> -> __attrs_140240907508496
                __attrs_140240907508496 = _static_140240907509520

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12 mb-4">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c62165ed0> name=None at 7f8c62165710> -> __attrs_140240917638224
                __attrs_140240917638224 = _static_140240917782224

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input id="searchbox" autofocus type="text" class="form-control form-control-lg"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240916715600
                __default_140240916715600 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c62061ad0> at 7f8c62061a50> -> __attr_placeholder
                __attr_placeholder = u'Type to filter ...'
                __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_placeholder is not None):
                    __append((u' placeholder="%s"' % __attr_placeholder))
                __append(u'>\n        </div>\n\n        <!-- The setup item -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907418704
                __attrs_140240907418704 = _static_140241133802128
                __backup_setup_140240906136656 = get('setup', __marker)

                # <Value u'python:view.setup' (36:37)> -> __value
                __token = 1429
                try:
                    __zt_tmp = __attrs_140240907418704
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u'view.setup', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['setup'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c617cfa90> name=None at 7f8c617cf7d0> -> __attrs_140240906722000
                __attrs_140240906722000 = _static_140240907729552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="tilewrapper col-xs-12 col-sm-6 col-md-4 col-lg-3">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c616d9b10> name=None at 7f8c616d9050> -> __attrs_140240916748048
                __attrs_140240916748048 = _static_140240906722064

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="tile setup text-capitalized text-decoration-none"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240916745360
                __default_140240916745360 = _DEFAULT_MARKER

                # <Substitution u'setup/absolute_url' (39:36)> -> __attr_href
                __token = 1630
                try:
                    __zt_tmp = __attrs_140240916748048
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140241087907024('path', u'setup/absolute_url', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240918270480
                __default_140240918270480 = _DEFAULT_MARKER

                # <Translate msgid=None node=<Substitution u'setup/Title' (40:36)> at 7f8c621dd310> -> __attr_title

                # <Substitution u'setup/Title' (40:36)> -> __attr_title
                __token = 1686
                try:
                    __zt_tmp = __attrs_140240916748048
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140241087907024('path', u'setup/Title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n              ')

                # <Static value=<_ast.Dict object at 0x7f8c617864d0> name=None at 7f8c61786750> -> __attrs_140240907429456
                __attrs_140240907429456 = _static_140240907429072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="item text-truncate">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c617a9ed0> name=None at 7f8c6588d910> -> __attrs_140240907574352
                __attrs_140240907574352 = _static_140240907574992

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907571344
                __default_140240907571344 = _DEFAULT_MARKER

                # <Value u"python:view.get_icon_for(setup, css_class='icon')" (44:44)> -> __cache_140240907571536
                __token = 1860
                try:
                    __zt_tmp = __attrs_140240907574352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240907571536 = _static_140241087907024('python', u"view.get_icon_for(setup, css_class='icon')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:view.get_icon_for(setup, css_class='icon')" (44:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617a92d0> -> __condition
                __expression = __cache_140240907571536

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img src="#"/>')
                else:
                    __content = __cache_140240907571536
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n                ')

                # <Static value=<_ast.Dict object at 0x7f8c617a95d0> name=None at 7f8c617a94d0> -> __attrs_140240907572880
                __attrs_140240907572880 = _static_140240907572688

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="title vcenter text-truncate d-inline-block">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907572496
                __default_140240907572496 = _DEFAULT_MARKER

                # <Value u'setup/Title' (47:34)> -> __cache_140240907571856
                __token = 2059
                try:
                    __zt_tmp = __attrs_140240907572880
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240907571856 = _static_140241087907024('path', u'setup/Title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'setup/Title' (47:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c617a9250> -> __condition
                __expression = __cache_140240907571856

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n                  Setup Item Title\n                ')
                else:
                    __content = __cache_140240907571856
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n              </div>\n            </a>\n          </div>\n        ')
                if (__backup_setup_140240906136656 is __marker):
                    del econtext['setup']
                else:
                    econtext['setup'] = __backup_setup_140240906136656
                __append(u'\n\n        <!-- The other setup items -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906721168
                __attrs_140240906721168 = _static_140241133802128
                __backup_item_140240916803216 = get('item', __marker)

                # <Value u'view/setupitems' (56:36)> -> __iterator
                __token = 2284
                try:
                    __zt_tmp = __attrs_140240906721168
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/setupitems', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240916749072, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c617a96d0> name=None at 7f8c617a9110> -> __attrs_140240917139792
                    __attrs_140240917139792 = _static_140240907572944

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="tilewrapper col-xs-12 col-sm-6 col-md-4 col-lg-3">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c616cda10> name=None at 7f8c616cdf50> -> __attrs_140240907047120
                    __attrs_140240907047120 = _static_140240906672656

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a class="tile text-capitalized text-decoration-none"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907050960
                    __default_140240907050960 = _DEFAULT_MARKER

                    # <Substitution u'item/absolute_url' (59:36)> -> __attr_href
                    __token = 2477
                    try:
                        __zt_tmp = __attrs_140240907047120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('path', u'item/absolute_url', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907049936
                    __default_140240907049936 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution u'item/Title' (60:36)> at 7f8c61729b90> -> __attr_title

                    # <Substitution u'item/Title' (60:36)> -> __attr_title
                    __token = 2532
                    try:
                        __zt_tmp = __attrs_140240907047120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140241087907024('path', u'item/Title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c61729950> name=None at 7f8c61729c90> -> __attrs_140240907048016
                    __attrs_140240907048016 = _static_140240907049296

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="item text-truncate">\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c6170ce50> name=None at 7f8c6170c510> -> __attrs_140240906930704
                    __attrs_140240906930704 = _static_140240906931792

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906932176
                    __default_140240906932176 = _DEFAULT_MARKER

                    # <Value u"python:view.get_icon_for(item, css_class='icon')" (65:44)> -> __cache_140240906931600
                    __token = 2739
                    try:
                        __zt_tmp = __attrs_140240906930704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906931600 = _static_140241087907024('python', u"view.get_icon_for(item, css_class='icon')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python:view.get_icon_for(item, css_class='icon')" (65:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6170cad0> -> __condition
                    __expression = __cache_140240906931600

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img src="#" class="icon"/>')
                    else:
                        __content = __cache_140240906931600
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c6170c410> name=None at 7f8c6170c910> -> __attrs_140240906638416
                    __attrs_140240906638416 = _static_140240906929168

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="title">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906930512
                    __default_140240906930512 = _DEFAULT_MARKER

                    # <Value u'item/Title' (68:35)> -> __cache_140240906931536
                    __token = 2902
                    try:
                        __zt_tmp = __attrs_140240906638416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240906931536 = _static_140241087907024('path', u'item/Title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/Title' (68:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6170cbd0> -> __condition
                    __expression = __cache_140240906931536

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                  Setup Item Title\n                ')
                    else:
                        __content = __cache_140240906931536
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n              </div>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c616c5ad0> name=None at 7f8c6170cc50> -> __attrs_140240906639440
                    __attrs_140240906639440 = _static_140240906640080
                    __backup_count_140240906722896 = get('count', __marker)

                    # <Value u'python:view.get_count(item)' (73:37)> -> __value
                    __token = 3076
                    try:
                        __zt_tmp = __attrs_140240906639440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('python', u'view.get_count(item)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['count'] = __value

                    # <Value u'python:count>0' (74:34)> -> __condition
                    __token = 3139
                    try:
                        __zt_tmp = __attrs_140240906639440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u'count>0', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="small text-right">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c616c7b50> name=None at 7f8c616c7090> -> __attrs_140240906646416
                        __attrs_140240906646416 = _static_140240906648400

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="text-secondary">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906647056
                        __attrs_140240906647056 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906646160
                        __default_140240906646160 = _DEFAULT_MARKER

                        # <Value u'count' (76:37)> -> __cache_140240906647760
                        __token = 3239
                        try:
                            __zt_tmp = __attrs_140240906647056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240906647760 = _static_140241087907024('path', u'count', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'count' (76:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616c7850> -> __condition
                        __expression = __cache_140240906647760

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240906647760
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                </span>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c616c7050> name=None at 7f8c616c7110> -> __attrs_140240906645712
                        __attrs_140240906645712 = _static_140240906645584

                        # <Value u'python:count == 1' (79:37)> -> __condition
                        __token = 3375
                        try:
                            __zt_tmp = __attrs_140240906645712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('python', u'count == 1', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="text-secondary">')
                            __stream_140240906648912 = []
                            __append_140240906648912 = __stream_140240906648912.append
                            __append_140240906648912(u'Item')
                            __msgid_140240906648912 = __re_whitespace(''.join(__stream_140240906648912)).strip()
                            if u'label_setupview_item':
                                __append(translate(u'label_setupview_item', mapping=None, default=__msgid_140240906648912, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>')
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c616ed690> name=None at 7f8c616ed6d0> -> __attrs_140240906805200
                        __attrs_140240906805200 = _static_140240906802832

                        # <Value u'python:count > 1' (82:37)> -> __condition
                        __token = 3549
                        try:
                            __zt_tmp = __attrs_140240906805200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('python', u'count > 1', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="text-secondary">')
                            __stream_140240906645904 = []
                            __append_140240906645904 = __stream_140240906645904.append
                            __append_140240906645904(u'Items')
                            __msgid_140240906645904 = __re_whitespace(''.join(__stream_140240906645904)).strip()
                            if u'label_setupview_items':
                                __append(translate(u'label_setupview_items', mapping=None, default=__msgid_140240906645904, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>')
                        __append(u'\n              </div>')
                    if (__backup_count_140240906722896 is __marker):
                        del econtext['count']
                    else:
                        econtext['count'] = __backup_count_140240906722896
                    __append(u'\n            </a>\n          </div>\n        ')
                    ____index_140240916749072 -= 1
                    if (____index_140240916749072 > 0):
                        __append('')
                if (__backup_item_140240916803216 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140240916803216
                __append(u'\n      </div>\n\n    </div>')
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140240917091600
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'here/prefs_main_template/macros/master', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240933552928 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240933552928
            __i18n_domain = __previous_i18n_domain_140240906739088
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }