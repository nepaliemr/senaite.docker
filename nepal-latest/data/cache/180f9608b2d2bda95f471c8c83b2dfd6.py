# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/dashboard/templates/dashboard.pt'

__tokens = {281: (u'string:${portal_url}?redirect_to=frontpage', 9, 28), 15257: (u'python:view.get_sections()', 467, 33), 15346: (u'section/id', 468, 60), 15431: (u'section/title', 470, 27), 15530: (u'python:False', 471, 46), 15699: (u'python:view.is_admin_user()', 475, 54), 16084: (u'python:view.get_dashboard_panels_visibility(section_id)', 482, 42), 16354: (u"python: role_value_pair[1] == 'yes'", 487, 43), 16433: (u' python: role_value_pair[0', 488, 42), 16506: (u'd section_', 489, 44), 16561: (u"ed python: role_value_pair[0] in ['LabManager', 'Manage", 490, 41), 16708: (u'python: role_value_pair[0]', 492, 41), 17095: (u'section/id', 502, 43), 17040: (u'section/id', 501, 47), 17181: (u'python: view.get_filter_options()', 504, 32), 17247: (u'options', 505, 31), 17321: (u'python:option', 507, 40), 17378: (u" python: 'selected' if view.is_filter_selected(section_id, option) else '", 508, 42), 17486: (u'python:options.getValue(option)', 509, 31), 17764: (u"python:[p for p in section.get('panels',[]) if p.get('type','')=='bar-chart-panel']", 518, 45), 17998: (u'repeat/panel/number', 520, 37), 17889: (u"python:'dashboard-bargraph-panel-wrapper %s' % panel.get('class', '')", 519, 39), 18079: (u"python:panel.get('data','[]')!='[]'", 521, 58), 18162: (u'python:"bar-chart-%s-%s" % (section["id"],itemnum)', 522, 45), 18376: (u'python:"bar-chart-%s-%s-period" % (section["id"],itemnum)', 525, 63), 18491: (u"python:panel.get('name', '')", 526, 33), 18664: (u'python:plone_view.toLocalizedTime(view.date_from)', 529, 37), 18824: (u'python:plone_view.toLocalizedTime(view.date_to)', 531, 37), 19074: (u"python:'selected' if view.periodicity == 'd' else ''", 535, 44), 19152: (u'string:${view/portal_url}/senaite-dashboard?p=d', 535, 122), 19278: (u"python:'selected' if view.periodicity == 'w' else ''", 536, 44), 19356: (u'string:${view/portal_url}/senaite-dashboard?p=w', 536, 122), 19483: (u"python:'selected' if view.periodicity == 'm' else ''", 537, 44), 19561: (u'string:${view/portal_url}/senaite-dashboard?p=m', 537, 122), 19689: (u"python:'selected' if view.periodicity == 'q' else ''", 538, 44), 19767: (u'string:${view/portal_url}/senaite-dashboard?p=q', 538, 122), 19897: (u"python:'selected' if view.periodicity == 'b' else ''", 539, 44), 19975: (u'string:${view/portal_url}/senaite-dashboard?p=b', 539, 122), 20104: (u"python:'selected' if view.periodicity == 'y' else ''", 540, 44), 20182: (u'string:${view/portal_url}/senaite-dashboard?p=y', 540, 122), 20383: (u'python:"bar-chart-%s-%s" % (section["id"],itemnum)', 544, 38), 20465: (u' panel/dat', 545, 30), 20514: (u's panel/datacolo', 546, 36), 20848: (u"python:[p for p in section.get('panels',[]) if p.get('type','')=='simple-panel']", 554, 43), 21006: (u'panel/number', 556, 33), 21052: (u" python:'' if num==0 else 'highlight", 557, 32), 21131: (u"python:'card my-2 dashboard-info-panel-wrapper %s %s' % (panel.get('class', ''), numclass)", 558, 39), 21263: (u'panel/link', 559, 38), 21486: (u"python:'height: {}%'.format(100 - panel.get('percentage', 0))", 563, 47), 21649: (u"python:'height: {}%'.format(panel.get('percentage', 0))", 565, 47), 21774: (u'panel/number', 567, 36), 21931: (u"python:panel.get('legend','')", 568, 100), 21867: (u'panel/legend', 568, 36), 22005: (u'panel/description', 569, 36), 22284: (u'context/@@authenticator/authenticator', 578, 34), 66: (u'here/main_template/macros/master', 2, 23), 66: (u'here/main_template/macros/master', 2, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140240884918928 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=m', }
_static_140241087907024 = __compile_zt_expr
_static_140240809268304 = {u'style': u'display:none;', u'class': u'bar-chart-period', u'id': u'python:"bar-chart-%s-%s-period" % (section["id"],itemnum)', }
_static_140240906202064 = {u'class': u'clearfix', }
_static_140240907509712 = {u'class': u'dashboard-info-panel', }
_static_140240884233744 = {u'class': u'dashboard-info-panel-vertbar', }
_static_140240885131792 = {u'class': u"python:'selected' if view.periodicity == 'd' else ''", }
_static_140241133802128 = {}
_static_140240907049360 = {u'class': u'checkbox', }
_static_140240884235536 = {u'style': u"python:'height: {}%'.format(100 - panel.get('percentage', 0))", u'class': u'vertbar-remaining', }
_static_140240897377232 = {u'class': u"python:'selected' if view.periodicity == 'y' else ''", }
_static_140240884924688 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=w', }
_static_140240884919632 = {u'class': u"python:'selected' if view.periodicity == 'b' else ''", }
_static_140240809021392 = u'master'
_static_140240897386128 = {u'style': u"python:'height: {}%'.format(panel.get('percentage', 0))", u'class': u'vertbar-done', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240885129744 = {u'class': u"python:'selected' if view.periodicity == 'q' else ''", }
_static_140240907368528 = {u'class': u'dashboard-info-panel-total', }
_static_140240809268816 = {u'target-id': u'python:"bar-chart-%s-%s" % (section["id"],itemnum)', u'href': u'#', }
_static_140240907366800 = {u'class': u'dashboard-info-panel-description', }
_static_140240907003344 = {u'class': u'toggle-barchart', }
_static_140240884918608 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=q', }
_static_140240906205392 = {u'class': u'dashboard_filters', u'section_id': u'section/id', }
_static_140240906577424 = {u'class': u'dashboard-section', }
_static_140240906557456 = {u'selected': u"python: 'selected' if view.is_filter_selected(section_id, option) else ''", u'value': u'python:option', }
_static_140240884889744 = {u'class': u'dashboard-info-panel-number', }
_static_140240884934160 = {u'style': u'display:none', u'data': u'panel/data', u'class': u'bar-chart', u'data-colors': u'panel/datacolors', u'id': u'python:"bar-chart-%s-%s" % (section["id"],itemnum)', }
_static_140240906369616 = {u'class': u'bar-chart-no-data', }
_static_140240884934352 = {u'class': u"python:'selected' if view.periodicity == 'm' else ''", }
_static_140240906200144 = {u'style': u'min-width: 12em;', u'class': u"python:'card my-2 dashboard-info-panel-wrapper %s %s' % (panel.get('class', ''), numclass)", }
_static_140240917091280 = {u'class': u'actions', }
_static_140240906929616 = {u'checked': u"python: role_value_pair[1] == 'yes'", u'section_id': u'section_id', u'value': u'', u'role_id': u'python: role_value_pair[0]', u'disabled': u"python: role_value_pair[0] in ['LabManager', 'Manager']", u'type': u'checkbox', }
_static_140240907428240 = {u'class': u'dashboard-section-head', }
_static_140240907112528 = {u'class': u'fas fa-caret-down', }
_static_140240907004304 = {u'class': u"python:'dashboard-bargraph-panel-wrapper %s' % panel.get('class', '')", }
_static_140240896143952 = {u'href': u'panel/link', }
_static_140240916927056 = {u'class': u'dashboard-panels', }
_static_140240885132048 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=d', }
_static_140240916632976 = {u'class': u'dashboard-section-title', }
_static_140240897376400 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=y', }
_static_140240809583312 = {u'style': u'float:right;', u'href': u'', }
_static_140240808757392 = {u'class': u'h2-legend', }
_static_140240897379920 = {u'href': u'string:${view/portal_url}/senaite-dashboard?p=b', }
_static_140240884896656 = {u'class': u'dashboard-time-selector', }
_static_140240906616784 = {u'href': u'#', u'class': u'dashboard-visibility-link', }
_static_140240809586256 = {u'class': u'documentFirstHeading', }
_static_140240885133008 = {u'class': u"python:'selected' if view.periodicity == 'w' else ''", }
_static_140240907116496 = {u'style': u'display:none', u'class': u'roles-visibility', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240809071184
            __attrs_140240809071184 = _static_140241133802128
            __previous_i18n_domain_140240809072016 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140240928802208 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8c5b9acfd0> name=None at 7f8c5b9acd90> -> __value
            __value = _static_140240809021392
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140241041488144
                __attrs_140241041488144 = _static_140241133802128
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c5ba362d0> name=None at 7f8c5ba36290> -> __attrs_140240809585232
                __attrs_140240809585232 = _static_140240809583312

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240809584016
                __default_140240809584016 = _DEFAULT_MARKER

                # <Substitution u'string:${portal_url}?redirect_to=frontpage' (9:28)> -> __attr_href
                __token = 281
                try:
                    __zt_tmp = __attrs_140240809585232
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140241087907024('string', u'${portal_url}?redirect_to=frontpage', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u' style="float:right;">')
                __stream_140240809074576 = []
                __append_140240809074576 = __stream_140240809074576.append
                __append_140240809074576(u'\n      Switch to frontpage\n    ')
                __msgid_140240809074576 = __re_whitespace(''.join(__stream_140240809074576)).strip()
                if __msgid_140240809074576:
                    __append(translate(__msgid_140240809074576, mapping=None, default=__msgid_140240809074576, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c5ba36e50> name=None at 7f8c5ba36e90> -> __attrs_140240917728016
                __attrs_140240917728016 = _static_140240809586256

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140240809585872 = []
                __append_140240809585872 = __stream_140240809585872.append
                __append_140240809585872(u'System Dashboard')
                __msgid_140240809585872 = __re_whitespace(''.join(__stream_140240809585872)).strip()
                if __msgid_140240809585872:
                    __append(translate(__msgid_140240809585872, mapping=None, default=__msgid_140240809585872, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n  ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240958923856
                __attrs_140240958923856 = _static_140241133802128
                __append(u'\n  ')
            _slots = econtext[u'__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240916803216
                __attrs_140240916803216 = _static_140241133802128
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906694160
                __attrs_140240906694160 = _static_140241133802128

                # <style ... (0:0)
                # --------------------------------------------------------
                __append(u'<style>\n     .dashboard-section {\n       padding: 0 0 20px;\n     }\n     .dashboard-section-head {\n       border-bottom: 1px dotted #dfdfdf;\n       margin: 0 0 10px;\n     }\n     .dashboard-section-head div.actions {\n       float:right;\n       text-align:right;\n     }\n     .dashboard-section-head div.actions select {\n       padding: 0 5px;\n       vertical-align: top;\n     }\n     .dashboard-section-head:after {\n       clear: both;\n       content: " ";\n       display: block;\n       font-size: 0;\n       height: 0;\n       visibility: hidden;\n     }\n     .dashboard-section h2 {\n       float: left;\n       font-size: 1.3em;\n       font-weight: bold;\n       letter-spacing: 0;\n       padding: 5px 0 4px;\n       width: 70%;\n     }\n     .dashboard-section .h2-legend {\n       font-size: 0.9em;\n       padding: 0 0 10px 2px;\n     }\n     .dashboard-panels {\n     }\n     .dashboard-info-panel-wrapper {\n       float: left;\n       margin-right: 1em;\n     }\n     .dashboard-info-panel {\n     }\n     #content .dashboard-info-panel-wrapper a {\n       color:#333;\n       text-decoration:none;\n     }\n     #content .dashboard-info-panel-wrapper a:hover div {\n       opacity:0.8;\n       filter:alpha(opacity=80);\n       -webkit-transition: opacity 250ms ease-in-out;\n       -moz-transition: opacity 250ms ease-in-out;\n       -o-transition: opacity 250ms ease-in-out;\n       -ms-transition: opacity 250ms ease-in-out;\n       transition: opacity 250ms ease-in-out\n     }\n     .dashboard-info-panel-number {\n       float: left;\n       font-size: 2em;\n       font-weight: normal;\n       line-height: 1em;\n       padding: 0px 4px 0 10px;\n       text-align: left;\n       color: #3b8686;\n     }\n     #content .dashboard-info-panel-wrapper {\n       opacity:0.4;\n       filter:alpha(opacity=40);\n     }\n     #content .dashboard-info-panel-wrapper.highlight {\n       opacity:1;\n       filter:alpha(opacity=100);\n     }\n     #content .dashboard-info-panel-wrapper.highlight .dashboard-info-panel-number {\n       color:#ff7f0e;\n       color:#79bd9a;\n     }\n\n     .dashboard-section .period-informative {\n       color: #666;\n       font-size: 0.85em;\n       padding: 10px;\n     }\n     .dashboard-info-panel-description {\n       background-color: #dfdfdf;\n       clear: both;\n       font-size: 0.85em;\n       font-weight: normal;\n       padding: 1em;\n     }\n     .dashboard-info-panel-total {\n       color: #666;\n       float: left;\n       font-size: 0.85em;\n       font-weight: normal;\n       padding: 5px 0 0 10px;\n       text-align: left;\n       vertical-align: bottom;\n     }\n     #content ul.dashboard-time-selector {\n       list-style:none;\n       margin: 10px 0 10px -5px;\n       padding:0;\n     }\n     #content ul.dashboard-time-selector li {\n       display:inline;\n     }\n     #content ul.dashboard-time-selector li a {\n       background-color: #efefef;\n       border-radius: 5px;\n       margin: 0 5px;\n       padding: 4px 10px;\n       color:#333;\n     }\n     #content ul.dashboard-time-selector li.selected a {\n       background-color: #dcdcdc;\n     }\n     .clearfix {\n       clear: both;\n     }\n     .bar-chart {\n       width:100%;\n       min-width:640px;\n     }\n     .bar-chart-period {\n       clear: both;\n       padding: 1px 0 0 15px;\n     }\n     .bar-chart .axis path,\n     .bar-chart .axis line {\n       fill: none;\n       stroke: #aaa;\n       shape-rendering: crispEdges;\n     }\n     .bar-chart .y.axis line {\n       stroke: #ddd;\n     }\n     .bar-chart .axis text {\n       fill:#777;\n     }\n     .bar-chart .bar {\n       fill: steelblue;\n     }\n     .bar-chart g.legend {\n       font-size: 0.8em;\n     }\n     .bar-chart .x.axis {\n       font-size: 0.75em;\n     }\n     .bar-chart .y.axis {\n       font-size: 0.75em;\n     }\n     .bar-chart .graph-text-bar {\n       border:1px solid red;\n       background-color:red;\n     }\n     div.dashboard-period {\n       padding:10px;\n       font-size:1.2em;\n     }\n     .toggle-barchart {\n       text-align: left;\n       padding: 0 0 10px;\n     }\n     .toggle-barchart a {\n       padding: 0;\n     }\n     .bar-chart-no-data {\n       color: #b22222;\n       font-size: 0.9em;\n       padding: 20px;\n     }\n     div.roles-visibility {\n       align-self: right;\n       background-color: #e3e3e3;\n       border: 1px solid #cdcdcd;\n       border-radius: 0 0 5px 5px;\n       padding: 5px;\n       position: absolute;\n       text-align: left;\n       z-index: 10;\n     }\n     div.roles-visibility div.checkbox label {\n       font-weight:normal;\n     }\n     a.dashboard-visibility-link {\n       margin-right:10px;\n     }\n     /* a.dashboard-visibility-link:after {\n        content: " \u25bc";\n        } */\n     .dashboard-info-panel-vertbar {\n       height:2em;\n       float:left;\n     }\n     .vertbar-remaining, .vertbar-done {\n       width:4px;\n     }\n     .vertbar-done {\n       background-color: #A8DBA8;\n     }\n     .vertbar-remaining {\n       background-color:#efefef;\n       border-radius: 2px 2px 0 0;\n     }\n    </style>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906122576
                __attrs_140240906122576 = _static_140241133802128

                # <script ... (0:0)
                # --------------------------------------------------------
                __append(u'<script>\n     document.addEventListener("DOMContentLoaded", () => {\n       loadBarCharts();\n       dashboard_cookie_controller();\n       role_permission_input_controller();\n       load_roles_visibility_links();\n\n       function loadBarCharts() {\n         $(\'.bar-chart\').each(function(e){\n           var id = $(this).attr(\'id\');\n           var vis = bika.lims.SiteView.readCookie(\'visible.\'+id);\n           if (vis == 1) {\n             $(\'#\'+id).show();\n             $(\'#\'+id+"-period").show();\n             $(\'#\'+id).closest(\'div.dashboard-panels\').find(\'.dashboard-info-panel-wrapper\').hide();\n             $(\'#\'+id).addClass(\'loaded\');\n             loadBarChart(id);\n           }\n         });\n\n         $(\'div.toggle-barchart a\').click(function(e) {\n           e.preventDefault();\n           var barchartid = $(this).attr(\'target-id\');\n           if ($(\'#\'+barchartid).is(":visible")) {\n             bika.lims.SiteView.setCookie(\'visible.\'+barchartid, 0);\n             $(\'#\'+barchartid+\'-period\').hide();\n             $(\'#\'+barchartid).hide();\n             $(\'#\'+barchartid).closest(\'div.dashboard-panels\').find(\'.dashboard-info-panel-wrapper\').show();\n           } else {\n             bika.lims.SiteView.setCookie(\'visible.\'+barchartid, 1);\n             $(\'#\'+barchartid+\'-period\').show();\n             $(\'#\'+barchartid).show();\n             $(\'#\'+barchartid).closest(\'div.dashboard-panels\').find(\'.dashboard-info-panel-wrapper\').hide();\n             loadBarChart(barchartid);\n             /*    if (!$(\'#\'+barchartid).hasClass(\'loaded\')) {\n                loadBarChart(barchartid);\n                $(\'#\'+barchartid).addClass(\'loaded\');\n                }*/\n           }\n         });\n       }\n\n       function loadBarChart(id) {\n         var container = $(\'#\'+id);\n         $(container).find(\'svg\').remove();\n         var raw_data = JSON.parse($(container).attr(\'data\'));\n         var data = raw_data.data;\n         if (data.length == 0 || Object.keys(data[0]).length < 2) {\n           return;\n         }\n         // All available states come sorted from by quantity descending, but we\n         // only want those for which there is at least one entry in data\n         var states = raw_data.states;\n         states = states.filter(function(key) { return key in data[0] });\n\n         $(container).html("");\n         var margin = {top: 10, right: 200, bottom: 50, left: 50},\n             width = $(container).innerWidth() - margin.left - margin.right,\n             height = 200 - margin.top - margin.bottom;\n\n         var x = d3.scale.ordinal().rangeRoundBands([0, width], .1);\n         var y = d3.scale.linear().range([height, 0]);\n         colors = JSON.parse($(container).attr(\'data-colors\'));\n         var color = d3.scale.ordinal().range(colors);\n         color.domain(states);\n\n         var xAxis = d3.svg.axis()\n                       .scale(x)\n                       .orient("bottom")\n                       .ticks(10);\n         var yAxis = d3.svg.axis()\n                       .scale(y)\n                       .orient("left")\n                       .tickSize(-width, 0, 0)\n                       .tickFormat(d3.format(".2s"));\n\n         var svg = d3.select("#"+id).append("svg")\n                     .attr("width", width + margin.left + margin.right)\n                     .attr("height", height + margin.top + margin.bottom)\n                     .append("g")\n                     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");\n\n         data.forEach(function(d) {\n           var y0=0;\n           d.statuses=color.domain().map(function(name) {\n             return {name: name, y0: y0, y1:y0 += +d[name]};\n           });\n           d.total = d.statuses[d.statuses.length - 1].y1;\n         });\n\n         x.domain(data.map(function(d) { return d.date;}));\n         y.domain([0, d3.max(data, function(d) { return d.total; })]);\n\n         svg.append("g")\n            .attr("class", "x axis")\n            .attr("transform", "translate(0," + height + ")")\n            .call(xAxis)\n            .selectAll("text")\n            .style("text-anchor", "end")\n            .style("font-size", "9px")\n            .attr("dx", "-.8em")\n            .attr("dy", "-.55em")\n            .attr("transform", "rotate(-90)" );\n\n         svg.append("g")\n            .attr("class", "y axis")\n            .call(yAxis);\n\n         var state = svg.selectAll(".state")\n                        .data(data)\n                        .enter()\n                        .append("g")\n                        .attr("class", "g")\n                        .attr("transform", function(d) { return "translate(" + x(d.date) + ",0)"; });\n\n         state.selectAll("rect")\n              .data(function(d) { return d.statuses; })\n              .enter()\n              .append("rect")\n              .attr("width", x.rangeBand())\n              .attr("y", function(d) { return y(d.y1); })\n              .attr("height", function(d) { return y(d.y0) - y(d.y1); })\n              .attr("data-date",function(d) { return d.x; })\n              .attr("data-value", function(d) { return d.y1-d.y0; })\n              .attr("data-name", function(d) { return d.name; })\n              .style("fill", function(d) { return colors[d.name]; })\n              .on("mouseout", function() {\n                d3.select(this.parentNode.children[this.parentNode.children.length-1])\n                  .remove();\n              })\n              .on("mouseover",  function() {\n                var date = d3.select(this).attr(\'data-date\');\n                var name = d3.select(this).attr(\'data-name\');\n                var val = name+": "+d3.select(this).attr(\'data-value\');\n                var y = d3.select(this).attr(\'y\');\n                var x = d3.select(this).attr(\'x\');\n                d3.select(this.parentNode)\n                  .append("text")\n                  .attr("fill", "#333")\n                  .style("font-size", "10px")\n                  .style("font-weight", "bold")\n                  .attr("x", x)\n                  .attr("y", 0)\n                  .attr("class", "graph-text-bar")\n                  .text(val);\n              });\n\n         var legend = svg.selectAll(".legend")\n                         .data(states.slice().reverse())\n                         .enter().append("g")\n                         .attr("class", "legend")\n                         .attr("transform", function(d, i) {\n                           return "translate(0," + i * 12 + ")";\n                         });\n\n         legend.append("rect")\n               .attr("x", width + 15)\n               .attr("width", 6)\n               .attr("height", 6)\n               .style("fill", function(d) { return colors[d]; });\n\n         legend.append("text")\n               .attr("x", width + 30)\n               .attr("y", 0)\n               .attr("dy", "6")\n               .text(function(d) { return d; })\n       }\n\n       function load_roles_visibility_links() {\n         $(\'a.dashboard-visibility-link\').click(function(e){\n           e.preventDefault();\n           var parent = $(this).closest(\'div.dashboard-section\');\n           var panel = $(parent).find(\'div.roles-visibility\');\n           if ($(panel).is(\':visible\')) {\n             $(panel).hide();\n           } else {\n             $(panel).show();\n           }\n         });\n       }\n       function dashboard_cookie_controller() {\n         /* Links a linker controller to each dashboard filter selector.\n            This controller reads the cookie data once the selector has been\n            modified and updates its data.\n          */\n         var selector;\n         var selector_section_id;\n         var cookie;\n         var counter;\n         var cookie_id = \'dashboard_filter_cookie\'\n         var filter_selectors = $(\'select.dashboard_filters\');\n         for(counter = 0; counter < filter_selectors.length; counter++){\n           selector = filter_selectors[counter];\n           $(selector).live(\'change\', function(){\n             section_id = $(this).attr(\'section_id\');\n             selected = $(this).find(\':selected\').val();\n             cookie_data = render_cookie_data(bika.lims.SiteView.readCookie(cookie_id));\n             cookie_data[section_id] = selected;\n             cookie_data = build_cookie_data(cookie_data);\n             bika.lims.SiteView.setCookie(\'dashboard_filter_cookie\', cookie_data);\n             window.location.reload(true);\n           });\n         }\n       };\n       function render_cookie_data(data){\n         return JSON.parse(data);\n       };\n       function build_cookie_data(data){\n         return JSON.stringify(data);\n       };\n       function role_permission_input_controller() {\n         /* Ajax post to update registry values */\n         var section_id, role, chk_val;\n         var role_checks = $(\'div.roles-visibility input[type="checkbox"]\');\n         for(counter = 0; counter < role_checks.length; counter++){\n           selector = role_checks[counter];\n           $(selector).live(\'change\', function(){\n             section_id = $(this).attr(\'section_id\');\n             role = $(this).attr(\'role_id\');\n             chk_val = $(this).is(\':checked\');\n             // AJAX post\n             $.ajax({\n               dataType: \'json\',\n               async: false,\n               type: \'POST\',\n               url: \'dashboard_view_permissions_update\',\n               data: {\n                 \'section_name\': section_id,\n                 \'role_id\': role,\n                 \'check_state\': chk_val,\n                 \'_authenticator\': $(\'input[name=\\\'_authenticator\\\']\').val()\n               }\n             });\n           });\n         }\n       }\n     });\n    </script>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906129936
                __attrs_140240906129936 = _static_140241133802128
                __backup_section_140240809073424 = get('section', __marker)

                # <Value u'python:view.get_sections()' (467:33)> -> __iterator
                __token = 15257
                try:
                    __zt_tmp = __attrs_140240906129936
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('python', u'view.get_sections()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240906481168, ) = getitem('repeat')(u'section', __iterator)
                econtext['section'] = None
                for __item in __iterator:
                    econtext['section'] = __item
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8c616b6610> name=None at 7f8c616b6c50> -> __attrs_140240906675536
                    __attrs_140240906675536 = _static_140240906577424
                    __backup_section_id_140240809074064 = get('section_id', __marker)

                    # <Value u'section/id' (468:60)> -> __value
                    __token = 15346
                    try:
                        __zt_tmp = __attrs_140240906675536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140241087907024('path', u'section/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    econtext['section_id'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<div class='dashboard-section'>\n        ")

                    # <Static value=<_ast.Dict object at 0x7f8c61786190> name=None at 7f8c61786650> -> __attrs_140240907054544
                    __attrs_140240907054544 = _static_140240907428240

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<div class='dashboard-section-head'>\n          ")

                    # <Static value=<_ast.Dict object at 0x7f8c6204d590> name=None at 7f8c6204dc10> -> __attrs_140240916974480
                    __attrs_140240916974480 = _static_140240916632976

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<h2 class='dashboard-section-title'>")

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907666512
                    __default_140240907666512 = _DEFAULT_MARKER

                    # <Value u'section/title' (470:27)> -> __cache_140240907051664
                    __token = 15431
                    try:
                        __zt_tmp = __attrs_140240916974480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240907051664 = _static_140241087907024('path', u'section/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'section/title' (470:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c6172af90> -> __condition
                    __expression = __cache_140240907051664

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240907051664
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</h2>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c620bd3d0> name=None at 7f8c6206a610> -> __attrs_140240962432720
                    __attrs_140240962432720 = _static_140240917091280

                    # <Value u'python:False' (471:46)> -> __condition
                    __token = 15530
                    try:
                        __zt_tmp = __attrs_140240962432720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u'False', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="actions">\n            <!-- Disabled, because dysfunctional -->\n\n            <!-- View permissions section -->\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240976073232
                        __attrs_140240976073232 = _static_140241133802128

                        # <Value u'python:view.is_admin_user()' (475:54)> -> __condition
                        __token = 15699
                        try:
                            __zt_tmp = __attrs_140240976073232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('python', u'view.is_admin_user()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n              ')

                            # <Static value=<_ast.Dict object at 0x7f8c616bffd0> name=None at 7f8c616bf750> -> __attrs_140240906190416
                            __attrs_140240906190416 = _static_140240906616784

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a class="dashboard-visibility-link" href="#">\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906190352
                            __attrs_140240906190352 = _static_140241133802128
                            __stream_140240906187856 = []
                            __append_140240906187856 = __stream_140240906187856.append
                            __append_140240906187856(u'Visibility')
                            __msgid_140240906187856 = __re_whitespace(''.join(__stream_140240906187856)).strip()
                            if __msgid_140240906187856:
                                __append(translate(__msgid_140240906187856, mapping=None, default=__msgid_140240906187856, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8c61739050> name=None at 7f8c61739350> -> __attrs_140240907115280
                            __attrs_140240907115280 = _static_140240907112528

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<i class="fas fa-caret-down"></i>\n              </a>\n              ')

                            # <Static value=<_ast.Dict object at 0x7f8c61739fd0> name=None at 7f8c617392d0> -> __attrs_140240906204880
                            __attrs_140240906204880 = _static_140240907116496

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="roles-visibility" style="display:none">\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906639056
                            __attrs_140240906639056 = _static_140241133802128
                            __backup_role_value_pair_140240906188304 = get('role_value_pair', __marker)

                            # <Value u'python:view.get_dashboard_panels_visibility(section_id)' (482:42)> -> __iterator
                            __token = 16084
                            try:
                                __zt_tmp = __attrs_140240906639056
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140241087907024('python', u'view.get_dashboard_panels_visibility(section_id)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                            (__iterator, ____index_140240906640528, ) = getitem('repeat')(u'role_value_pair', __iterator)
                            econtext['role_value_pair'] = None
                            for __item in __iterator:
                                econtext['role_value_pair'] = __item
                                __append(u'\n                  ')

                                # <Static value=<_ast.Dict object at 0x7f8c61729990> name=None at 7f8c61729cd0> -> __attrs_140240907085968
                                __attrs_140240907085968 = _static_140240907049360

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="checkbox">\n                    ')

                                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906930704
                                __attrs_140240906930704 = _static_140241133802128

                                # <label ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<label>\n                      ')

                                # <Static value=<_ast.Dict object at 0x7f8c6170c5d0> name=None at 7f8c6170cad0> -> __attrs_140240906547792
                                __attrs_140240906547792 = _static_140240906929616

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input type="checkbox" value=""')

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906547664
                                __default_140240906547664 = _DEFAULT_MARKER

                                # <Boolean u"python: role_value_pair[1] == 'yes'" (487:43)> -> __attr_checked
                                __token = 16354
                                try:
                                    __zt_tmp = __attrs_140240906547792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_checked = _static_140241087907024('python', u" role_value_pair[1] == 'yes'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                                if (__attr_checked is _DEFAULT_MARKER):
                                    __attr_checked = None
                                else:
                                    if __attr_checked:
                                        __attr_checked = u'checked'
                                    else:
                                        __attr_checked = None
                                if (__attr_checked is not None):
                                    __append((u' checked="%s"' % __attr_checked))

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906550032
                                __default_140240906550032 = _DEFAULT_MARKER

                                # <Substitution u'python: role_value_pair[0]' (488:42)> -> __attr_role_id
                                __token = 16433
                                try:
                                    __zt_tmp = __attrs_140240906547792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_role_id = _static_140241087907024('python', u' role_value_pair[0]', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                                __attr_role_id = __quote(__attr_role_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_role_id is not None):
                                    __append((u' role_id="%s"' % __attr_role_id))

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906550160
                                __default_140240906550160 = _DEFAULT_MARKER

                                # <Substitution u'section_id' (489:44)> -> __attr_section_id
                                __token = 16506
                                try:
                                    __zt_tmp = __attrs_140240906547792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_section_id = _static_140241087907024('path', u'section_id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                                __attr_section_id = __quote(__attr_section_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_section_id is not None):
                                    __append((u' section_id="%s"' % __attr_section_id))

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906548496
                                __default_140240906548496 = _DEFAULT_MARKER

                                # <Boolean u"python: role_value_pair[0] in ['LabManager', 'Manager']" (490:41)> -> __attr_disabled
                                __token = 16561
                                try:
                                    __zt_tmp = __attrs_140240906547792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_disabled = _static_140241087907024('python', u" role_value_pair[0] in ['LabManager', 'Manager']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                                if (__attr_disabled is _DEFAULT_MARKER):
                                    __attr_disabled = None
                                else:
                                    if __attr_disabled:
                                        __attr_disabled = u'disabled'
                                    else:
                                        __attr_disabled = None
                                if (__attr_disabled is not None):
                                    __append((u' disabled="%s"' % __attr_disabled))
                                __append(u'>\n                      ')

                                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906802640
                                __attrs_140240906802640 = _static_140241133802128

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906804816
                                __default_140240906804816 = _DEFAULT_MARKER

                                # <Value u'python: role_value_pair[0]' (492:41)> -> __cache_140240906550736
                                __token = 16708
                                try:
                                    __zt_tmp = __attrs_140240906802640
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140240906550736 = _static_140241087907024('python', u' role_value_pair[0]', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                                # <BinOp left=<Value u'python: role_value_pair[0]' (492:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616ed090> -> __condition
                                __expression = __cache_140240906550736

                                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140240906550736
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'\n                    </label>\n                  </div>\n                ')
                                ____index_140240906640528 -= 1
                                if (____index_140240906640528 > 0):
                                    __append('')
                            if (__backup_role_value_pair_140240906188304 is __marker):
                                del econtext['role_value_pair']
                            else:
                                econtext['role_value_pair'] = __backup_role_value_pair_140240906188304
                            __append(u'\n              </div>\n            ')
                        __append(u'\n\n            <!-- Mine/All filter -->\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6165b8d0> name=None at 7f8c616c5710> -> __attrs_140240906803024
                        __attrs_140240906803024 = _static_140240906205392
                        __backup_section_id_140240917024208 = get('section_id', __marker)

                        # <Value u'section/id' (502:43)> -> __value
                        __token = 17095
                        try:
                            __zt_tmp = __attrs_140240906803024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('path', u'section/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['section_id'] = __value

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<select class="dashboard_filters"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907085904
                        __default_140240907085904 = _DEFAULT_MARKER

                        # <Substitution u'section/id' (501:47)> -> __attr_section_id
                        __token = 17040
                        try:
                            __zt_tmp = __attrs_140240906803024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_section_id = _static_140241087907024('path', u'section/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_section_id = __quote(__attr_section_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_section_id is not None):
                            __append((u' section_id="%s"' % __attr_section_id))
                        __append(u'>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906556944
                        __attrs_140240906556944 = _static_140241133802128
                        __backup_options_140240916929232 = get('options', __marker)

                        # <Value u'python: view.get_filter_options()' (504:32)> -> __value
                        __token = 17181
                        try:
                            __zt_tmp = __attrs_140240906556944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('python', u' view.get_filter_options()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['options'] = __value
                        __backup_option_140240906487504 = get('option', __marker)

                        # <Value u'options' (505:31)> -> __iterator
                        __token = 17247
                        try:
                            __zt_tmp = __attrs_140240906556944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140241087907024('path', u'options', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        (__iterator, ____index_140240906558672, ) = getitem('repeat')(u'option', __iterator)
                        econtext['option'] = None
                        for __item in __iterator:
                            econtext['option'] = __item
                            __append(u'\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8c616b1810> name=None at 7f8c616b19d0> -> __attrs_140240906682064
                            __attrs_140240906682064 = _static_140240906557456

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<option')

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906556240
                            __default_140240906556240 = _DEFAULT_MARKER

                            # <Substitution u'python:option' (507:40)> -> __attr_value
                            __token = 17321
                            try:
                                __zt_tmp = __attrs_140240906682064
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140241087907024('python', u'option', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240916747664
                            __default_140240916747664 = _DEFAULT_MARKER

                            # <Boolean u"python: 'selected' if view.is_filter_selected(section_id, option) else ''" (508:42)> -> __attr_selected
                            __token = 17378
                            try:
                                __zt_tmp = __attrs_140240906682064
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_selected = _static_140241087907024('python', u" 'selected' if view.is_filter_selected(section_id, option) else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
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

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906556048
                            __default_140240906556048 = _DEFAULT_MARKER

                            # <Value u'python:options.getValue(option)' (509:31)> -> __cache_140240906558416
                            __token = 17486
                            try:
                                __zt_tmp = __attrs_140240906682064
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140240906558416 = _static_140241087907024('python', u'options.getValue(option)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:options.getValue(option)' (509:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616b10d0> -> __condition
                            __expression = __cache_140240906558416

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                ')
                            else:
                                __content = __cache_140240906558416
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</option>\n              ')
                            ____index_140240906558672 -= 1
                            if (____index_140240906558672 > 0):
                                __append('')
                        if (__backup_option_140240906487504 is __marker):
                            del econtext['option']
                        else:
                            econtext['option'] = __backup_option_140240906487504
                        if (__backup_options_140240916929232 is __marker):
                            del econtext['options']
                        else:
                            econtext['options'] = __backup_options_140240916929232
                        __append(u'\n            </select>')
                        if (__backup_section_id_140240917024208 is __marker):
                            del econtext['section_id']
                        else:
                            econtext['section_id'] = __backup_section_id_140240917024208
                        __append(u'\n          </div>')
                    __append(u'\n        </div>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c62095250> name=None at 7f8c616f8210> -> __attrs_140240906556688
                    __attrs_140240906556688 = _static_140240916927056

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<div class='dashboard-panels'>\n\n          <!-- Bar-chart panels -->\n          ")

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906681616
                    __attrs_140240906681616 = _static_140241133802128
                    __backup_panel_140240907051472 = get('panel', __marker)

                    # <Value u"python:[p for p in section.get('panels',[]) if p.get('type','')=='bar-chart-panel']" (518:45)> -> __iterator
                    __token = 17764
                    try:
                        __zt_tmp = __attrs_140240906681616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('python', u"[p for p in section.get('panels',[]) if p.get('type','')=='bar-chart-panel']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240906679184, ) = getitem('repeat')(u'panel', __iterator)
                    econtext['panel'] = None
                    for __item in __iterator:
                        econtext['panel'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6171e990> name=None at 7f8c6171efd0> -> __attrs_140240907002384
                        __attrs_140240907002384 = _static_140240907004304
                        __backup_itemnum_140240906847440 = get('itemnum', __marker)

                        # <Value u'repeat/panel/number' (520:37)> -> __value
                        __token = 17998
                        try:
                            __zt_tmp = __attrs_140240907002384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('path', u'repeat/panel/number', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['itemnum'] = __value

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907004944
                        __default_140240907004944 = _DEFAULT_MARKER

                        # <Substitution u"python:'dashboard-bargraph-panel-wrapper %s' % panel.get('class', '')" (519:39)> -> __attr_class
                        __token = 17889
                        try:
                            __zt_tmp = __attrs_140240907002384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'dashboard-bargraph-panel-wrapper %s' % panel.get('class', '')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c6171e5d0> name=None at 7f8c6171e850> -> __attrs_140240809271120
                        __attrs_140240809271120 = _static_140240907003344

                        # <Value u"python:panel.get('data','[]')!='[]'" (521:58)> -> __condition
                        __token = 18079
                        try:
                            __zt_tmp = __attrs_140240809271120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('python', u"panel.get('data','[]')!='[]'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="toggle-barchart">\n                ')

                            # <Static value=<_ast.Dict object at 0x7f8c5b9e9650> name=None at 7f8c5b9e9d50> -> __attrs_140240809270288
                            __attrs_140240809270288 = _static_140240809268816

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a href="#"')

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240809270096
                            __default_140240809270096 = _DEFAULT_MARKER

                            # <Substitution u'python:"bar-chart-%s-%s" % (section["id"],itemnum)' (522:45)> -> __attr_target_id
                            __token = 18162
                            try:
                                __zt_tmp = __attrs_140240809270288
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_target_id = _static_140241087907024('python', u'"bar-chart-%s-%s" % (section["id"],itemnum)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                            __attr_target_id = __quote(__attr_target_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_target_id is not None):
                                __append((u' target-id="%s"' % __attr_target_id))
                            __append(u'>')
                            __stream_140240809268496 = []
                            __append_140240809268496 = __stream_140240809268496.append
                            __append_140240809268496(u'Show/hide timeline summary')
                            __msgid_140240809268496 = __re_whitespace(''.join(__stream_140240809268496)).strip()
                            if __msgid_140240809268496:
                                __append(translate(__msgid_140240809268496, mapping=None, default=__msgid_140240809268496, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</a>\n              </div>')
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c5b9e9450> name=None at 7f8c5b9e9e10> -> __attrs_140240808758736
                        __attrs_140240808758736 = _static_140240809268304

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class=\'bar-chart-period\' style="display:none;"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240808758096
                        __default_140240808758096 = _DEFAULT_MARKER

                        # <Substitution u'python:"bar-chart-%s-%s-period" % (section["id"],itemnum)' (525:63)> -> __attr_id
                        __token = 18376
                        try:
                            __zt_tmp = __attrs_140240808758736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140241087907024('python', u'"bar-chart-%s-%s-period" % (section["id"],itemnum)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240808758224
                        __attrs_140240808758224 = _static_140241133802128

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h3>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240808758672
                        __default_140240808758672 = _DEFAULT_MARKER

                        # <Value u"python:panel.get('name', '')" (526:33)> -> __cache_140240808758544
                        __token = 18491
                        try:
                            __zt_tmp = __attrs_140240808758224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240808758544 = _static_140241087907024('python', u"panel.get('name', '')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:panel.get('name', '')" (526:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5b96cc10> -> __condition
                        __expression = __cache_140240808758544

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240808758544
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</h3>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c5b96c890> name=None at 7f8c5b96cf10> -> __attrs_140240808755472
                        __attrs_140240808755472 = _static_140240808757392

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<div class='h2-legend'>\n                  ")

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884896784
                        __attrs_140240884896784 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140240808757264 = []
                        __append_140240808757264 = __stream_140240808757264.append
                        __append_140240808757264(u'From')
                        __msgid_140240808757264 = __re_whitespace(''.join(__stream_140240808757264)).strip()
                        if __msgid_140240808757264:
                            __append(translate(__msgid_140240808757264, mapping=None, default=__msgid_140240808757264, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>&nbsp;\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884898704
                        __attrs_140240884898704 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884899216
                        __default_140240884899216 = _DEFAULT_MARKER

                        # <Value u'python:plone_view.toLocalizedTime(view.date_from)' (529:37)> -> __cache_140240884897424
                        __token = 18664
                        try:
                            __zt_tmp = __attrs_140240884898704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240884897424 = _static_140241087907024('python', u'plone_view.toLocalizedTime(view.date_from)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:plone_view.toLocalizedTime(view.date_from)' (529:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60209310> -> __condition
                        __expression = __cache_140240884897424

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240884897424
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                  &nbsp;')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884899728
                        __attrs_140240884899728 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140240884897744 = []
                        __append_140240884897744 = __stream_140240884897744.append
                        __append_140240884897744(u'to')
                        __msgid_140240884897744 = __re_whitespace(''.join(__stream_140240884897744)).strip()
                        if __msgid_140240884897744:
                            __append(translate(__msgid_140240884897744, mapping=None, default=__msgid_140240884897744, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>&nbsp;\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884896592
                        __attrs_140240884896592 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884895824
                        __default_140240884895824 = _DEFAULT_MARKER

                        # <Value u'python:plone_view.toLocalizedTime(view.date_to)' (531:37)> -> __cache_140240884896336
                        __token = 18824
                        try:
                            __zt_tmp = __attrs_140240884896592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240884896336 = _static_140241087907024('python', u'plone_view.toLocalizedTime(view.date_to)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:plone_view.toLocalizedTime(view.date_to)' (531:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60209b10> -> __condition
                        __expression = __cache_140240884896336

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240884896336
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                  (')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240884896976
                        __attrs_140240884896976 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140240884897872 = []
                        __append_140240884897872 = __stream_140240884897872.append
                        __append_140240884897872(u'updated every 2 hours')
                        __msgid_140240884897872 = __re_whitespace(''.join(__stream_140240884897872)).strip()
                        if __msgid_140240884897872:
                            __append(translate(__msgid_140240884897872, mapping=None, default=__msgid_140240884897872, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>)\n                </div>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c60209390> name=None at 7f8c60209150> -> __attrs_140240885129936
                        __attrs_140240885129936 = _static_140240884896656

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<ul class='dashboard-time-selector'>\n                  ")

                        # <Static value=<_ast.Dict object at 0x7f8c60242a10> name=None at 7f8c60242590> -> __attrs_140240885129424
                        __attrs_140240885129424 = _static_140240885131792

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240885131280
                        __default_140240885131280 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'd' else ''" (535:44)> -> __attr_class
                        __token = 19074
                        try:
                            __zt_tmp = __attrs_140240885129424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'd' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c60242b10> name=None at 7f8c60242bd0> -> __attrs_140240885132816
                        __attrs_140240885132816 = _static_140240885132048

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240885132688
                        __default_140240885132688 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=d' (535:122)> -> __attr_href
                        __token = 19152
                        try:
                            __zt_tmp = __attrs_140240885132816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=d', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240885129296 = []
                        __append_140240885129296 = __stream_140240885129296.append
                        __append_140240885129296(u'Daily')
                        __msgid_140240885129296 = __re_whitespace(''.join(__stream_140240885129296)).strip()
                        if __msgid_140240885129296:
                            __append(translate(__msgid_140240885129296, mapping=None, default=__msgid_140240885129296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c60242ed0> name=None at 7f8c60242350> -> __attrs_140240885129808
                        __attrs_140240885129808 = _static_140240885133008

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240885130192
                        __default_140240885130192 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'w' else ''" (536:44)> -> __attr_class
                        __token = 19278
                        try:
                            __zt_tmp = __attrs_140240885129808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'w' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c60210110> name=None at 7f8c60210590> -> __attrs_140240884925136
                        __attrs_140240884925136 = _static_140240884924688

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884924944
                        __default_140240884924944 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=w' (536:122)> -> __attr_href
                        __token = 19356
                        try:
                            __zt_tmp = __attrs_140240884925136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=w', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240884928464 = []
                        __append_140240884928464 = __stream_140240884928464.append
                        __append_140240884928464(u'Weekly')
                        __msgid_140240884928464 = __re_whitespace(''.join(__stream_140240884928464)).strip()
                        if __msgid_140240884928464:
                            __append(translate(__msgid_140240884928464, mapping=None, default=__msgid_140240884928464, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c602126d0> name=None at 7f8c60242910> -> __attrs_140240884933520
                        __attrs_140240884933520 = _static_140240884934352

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884934032
                        __default_140240884934032 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'm' else ''" (537:44)> -> __attr_class
                        __token = 19483
                        try:
                            __zt_tmp = __attrs_140240884933520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'm' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c6020ea90> name=None at 7f8c6020e590> -> __attrs_140240884920016
                        __attrs_140240884920016 = _static_140240884918928

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884919504
                        __default_140240884919504 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=m' (537:122)> -> __attr_href
                        __token = 19561
                        try:
                            __zt_tmp = __attrs_140240884920016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=m', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240884919824 = []
                        __append_140240884919824 = __stream_140240884919824.append
                        __append_140240884919824(u'Monthly')
                        __msgid_140240884919824 = __re_whitespace(''.join(__stream_140240884919824)).strip()
                        if __msgid_140240884919824:
                            __append(translate(__msgid_140240884919824, mapping=None, default=__msgid_140240884919824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c60242210> name=None at 7f8c60242d10> -> __attrs_140240884916496
                        __attrs_140240884916496 = _static_140240885129744

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884918416
                        __default_140240884918416 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'q' else ''" (538:44)> -> __attr_class
                        __token = 19689
                        try:
                            __zt_tmp = __attrs_140240884916496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'q' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c6020e950> name=None at 7f8c6020edd0> -> __attrs_140240884919184
                        __attrs_140240884919184 = _static_140240884918608

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884917200
                        __default_140240884917200 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=q' (538:122)> -> __attr_href
                        __token = 19767
                        try:
                            __zt_tmp = __attrs_140240884919184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=q', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240884917008 = []
                        __append_140240884917008 = __stream_140240884917008.append
                        __append_140240884917008(u'Quarterly')
                        __msgid_140240884917008 = __re_whitespace(''.join(__stream_140240884917008)).strip()
                        if __msgid_140240884917008:
                            __append(translate(__msgid_140240884917008, mapping=None, default=__msgid_140240884917008, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c6020ed50> name=None at 7f8c6020e290> -> __attrs_140240896682448
                        __attrs_140240896682448 = _static_140240884919632

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884918224
                        __default_140240884918224 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'b' else ''" (539:44)> -> __attr_class
                        __token = 19897
                        try:
                            __zt_tmp = __attrs_140240896682448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'b' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c60df0e50> name=None at 7f8c60df0b10> -> __attrs_140240897376784
                        __attrs_140240897376784 = _static_140240897379920

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897377872
                        __default_140240897377872 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=b' (539:122)> -> __attr_href
                        __token = 19975
                        try:
                            __zt_tmp = __attrs_140240897376784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=b', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240897378256 = []
                        __append_140240897378256 = __stream_140240897378256.append
                        __append_140240897378256(u'Biannual')
                        __msgid_140240897378256 = __re_whitespace(''.join(__stream_140240897378256)).strip()
                        if __msgid_140240897378256:
                            __append(translate(__msgid_140240897378256, mapping=None, default=__msgid_140240897378256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c60df03d0> name=None at 7f8c60df0a90> -> __attrs_140240897378896
                        __attrs_140240897378896 = _static_140240897377232

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897378192
                        __default_140240897378192 = _DEFAULT_MARKER

                        # <Substitution u"python:'selected' if view.periodicity == 'y' else ''" (540:44)> -> __attr_class
                        __token = 20104
                        try:
                            __zt_tmp = __attrs_140240897378896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'selected' if view.periodicity == 'y' else ''", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>')

                        # <Static value=<_ast.Dict object at 0x7f8c60df0090> name=None at 7f8c60df0490> -> __attrs_140240897378576
                        __attrs_140240897378576 = _static_140240897376400

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897380240
                        __default_140240897380240 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/portal_url}/senaite-dashboard?p=y' (540:122)> -> __attr_href
                        __token = 20182
                        try:
                            __zt_tmp = __attrs_140240897378576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('string', u'${view/portal_url}/senaite-dashboard?p=y', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')
                        __stream_140240897379728 = []
                        __append_140240897379728 = __stream_140240897379728.append
                        __append_140240897379728(u'Yearly')
                        __msgid_140240897379728 = __re_whitespace(''.join(__stream_140240897379728)).strip()
                        if __msgid_140240897379728:
                            __append(translate(__msgid_140240897379728, mapping=None, default=__msgid_140240897379728, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</a></li>\n                </ul>\n              </div>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c60212610> name=None at 7f8c60d46250> -> __attrs_140240961015696
                        __attrs_140240961015696 = _static_140240884934160

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<div class='bar-chart' style='display:none'")

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884347024
                        __default_140240884347024 = _DEFAULT_MARKER

                        # <Substitution u'python:"bar-chart-%s-%s" % (section["id"],itemnum)' (544:38)> -> __attr_id
                        __token = 20383
                        try:
                            __zt_tmp = __attrs_140240961015696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140241087907024('python', u'"bar-chart-%s-%s" % (section["id"],itemnum)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884348496
                        __default_140240884348496 = _DEFAULT_MARKER

                        # <Substitution u'panel/data' (545:30)> -> __attr_data
                        __token = 20465
                        try:
                            __zt_tmp = __attrs_140240961015696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_data = _static_140241087907024('path', u'panel/data', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_data = __quote(__attr_data, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_data is not None):
                            __append((u' data="%s"' % __attr_data))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906591184
                        __default_140240906591184 = _DEFAULT_MARKER

                        # <Substitution u'panel/datacolors' (546:36)> -> __attr_data_colors
                        __token = 20514
                        try:
                            __zt_tmp = __attrs_140240961015696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_data_colors = _static_140241087907024('path', u'panel/datacolors', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_data_colors = __quote(__attr_data_colors, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_data_colors is not None):
                            __append((u' data-colors="%s"' % __attr_data_colors))
                        __append(u'>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c61683a50> name=None at 7f8c61683e50> -> __attrs_140240897364496
                        __attrs_140240897364496 = _static_140240906369616

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="bar-chart-no-data">')
                        __stream_140240906367184 = []
                        __append_140240906367184 = __stream_140240906367184.append
                        __append_140240906367184(u'There is no available data for the selected period')
                        __msgid_140240906367184 = __re_whitespace(''.join(__stream_140240906367184)).strip()
                        if __msgid_140240906367184:
                            __append(translate(__msgid_140240906367184, mapping=None, default=__msgid_140240906367184, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>\n              </div>\n            </div>')
                        if (__backup_itemnum_140240906847440 is __marker):
                            del econtext['itemnum']
                        else:
                            econtext['itemnum'] = __backup_itemnum_140240906847440
                        __append(u'\n          ')
                        ____index_140240906679184 -= 1
                        if (____index_140240906679184 > 0):
                            __append('')
                    if (__backup_panel_140240907051472 is __marker):
                        del econtext['panel']
                    else:
                        econtext['panel'] = __backup_panel_140240907051472
                    __append(u'\n\n          <!-- Simple panels -->\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240906201616
                    __attrs_140240906201616 = _static_140241133802128
                    __backup_panel_140240907052624 = get('panel', __marker)

                    # <Value u"python:[p for p in section.get('panels',[]) if p.get('type','')=='simple-panel']" (554:43)> -> __iterator
                    __token = 20848
                    try:
                        __zt_tmp = __attrs_140240906201616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('python', u"[p for p in section.get('panels',[]) if p.get('type','')=='simple-panel']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240906199248, ) = getitem('repeat')(u'panel', __iterator)
                    econtext['panel'] = None
                    for __item in __iterator:
                        econtext['panel'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6165a450> name=None at 7f8c6165ab50> -> __attrs_140240884351184
                        __attrs_140240884351184 = _static_140240906200144
                        __backup_num_140240906189584 = get('num', __marker)

                        # <Value u'panel/number' (556:33)> -> __value
                        __token = 21006
                        try:
                            __zt_tmp = __attrs_140240884351184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('path', u'panel/number', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['num'] = __value
                        __backup_numclass_140240906639888 = get('numclass', __marker)

                        # <Value u"python:'' if num==0 else 'highlight'" (557:32)> -> __value
                        __token = 21052
                        try:
                            __zt_tmp = __attrs_140240884351184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('python', u"'' if num==0 else 'highlight'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['numclass'] = __value

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div style="min-width: 12em;"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884352720
                        __default_140240884352720 = _DEFAULT_MARKER

                        # <Substitution u"python:'card my-2 dashboard-info-panel-wrapper %s %s' % (panel.get('class', ''), numclass)" (558:39)> -> __attr_class
                        __token = 21131
                        try:
                            __zt_tmp = __attrs_140240884351184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('python', u"'card my-2 dashboard-info-panel-wrapper %s %s' % (panel.get('class', ''), numclass)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c60cc3250> name=None at 7f8c6172ca50> -> __attrs_140240907508176
                        __attrs_140240907508176 = _static_140240896143952

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240896145552
                        __default_140240896145552 = _DEFAULT_MARKER

                        # <Substitution u'panel/link' (559:38)> -> __attr_href
                        __token = 21263
                        try:
                            __zt_tmp = __attrs_140240907508176
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('path', u'panel/link', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c61799fd0> name=None at 7f8c61799bd0> -> __attrs_140240897183312
                        __attrs_140240897183312 = _static_140240907509712

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<div class='dashboard-info-panel'>\n                  ")

                        # <Static value=<_ast.Dict object at 0x7f8c60167610> name=None at 7f8c60167ed0> -> __attrs_140240884233808
                        __attrs_140240884233808 = _static_140240884233744

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="dashboard-info-panel-vertbar">\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f8c60167d10> name=None at 7f8c60167510> -> __attrs_140240945803536
                        __attrs_140240945803536 = _static_140240884235536

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="vertbar-remaining"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884235280
                        __default_140240884235280 = _DEFAULT_MARKER

                        # <Substitution u"python:'height: {}%'.format(100 - panel.get('percentage', 0))" (563:47)> -> __attr_style
                        __token = 21486
                        try:
                            __zt_tmp = __attrs_140240945803536
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140241087907024('python', u"'height: {}%'.format(100 - panel.get('percentage', 0))", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((u' style="%s"' % __attr_style))
                        __append(u'></div>\n                    ')

                        # <Static value=<_ast.Dict object at 0x7f8c60df2690> name=None at 7f8c60d5c610> -> __attrs_140240897189776
                        __attrs_140240897189776 = _static_140240897386128

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="vertbar-done"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240897189520
                        __default_140240897189520 = _DEFAULT_MARKER

                        # <Substitution u"python:'height: {}%'.format(panel.get('percentage', 0))" (565:47)> -> __attr_style
                        __token = 21649
                        try:
                            __zt_tmp = __attrs_140240897189776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140241087907024('python', u"'height: {}%'.format(panel.get('percentage', 0))", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((u' style="%s"' % __attr_style))
                        __append(u'></div>\n                  </div>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c60207890> name=None at 7f8c60207810> -> __attrs_140240907369552
                        __attrs_140240907369552 = _static_140240884889744

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<div class='dashboard-info-panel-number'>")

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240884890192
                        __default_140240884890192 = _DEFAULT_MARKER

                        # <Value u'panel/number' (567:36)> -> __cache_140240884888784
                        __token = 21774
                        try:
                            __zt_tmp = __attrs_140240907369552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240884888784 = _static_140241087907024('path', u'panel/number', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'panel/number' (567:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c60207190> -> __condition
                        __expression = __cache_140240884888784

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240884888784
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</div>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c61777850> name=None at 7f8c61777390> -> __attrs_140240907369488
                        __attrs_140240907369488 = _static_140240907368528

                        # <Value u"python:panel.get('legend','')" (568:100)> -> __condition
                        __token = 21931
                        try:
                            __zt_tmp = __attrs_140240907369488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('python', u"panel.get('legend','')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u"<div class='dashboard-info-panel-total'>")

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907367056
                            __default_140240907367056 = _DEFAULT_MARKER

                            # <Value u'panel/legend' (568:36)> -> __cache_140240907368912
                            __token = 21867
                            try:
                                __zt_tmp = __attrs_140240907369488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140240907368912 = _static_140241087907024('path', u'panel/legend', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                            # <BinOp left=<Value u'panel/legend' (568:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61777890> -> __condition
                            __expression = __cache_140240907368912

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140240907368912
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>')
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c61777190> name=None at 7f8c61777790> -> __attrs_140240885325904
                        __attrs_140240885325904 = _static_140240907366800

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u"<div class='dashboard-info-panel-description'>")

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240907367632
                        __default_140240907367632 = _DEFAULT_MARKER

                        # <Value u'panel/description' (569:36)> -> __cache_140240907368016
                        __token = 22005
                        try:
                            __zt_tmp = __attrs_140240885325904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240907368016 = _static_140241087907024('path', u'panel/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'panel/description' (569:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c61777d90> -> __condition
                        __expression = __cache_140240907368016

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240907368016
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</div>\n                </div>\n              </a>\n            </div>')
                        if (__backup_numclass_140240906639888 is __marker):
                            del econtext['numclass']
                        else:
                            econtext['numclass'] = __backup_numclass_140240906639888
                        if (__backup_num_140240906189584 is __marker):
                            del econtext['num']
                        else:
                            econtext['num'] = __backup_num_140240906189584
                        __append(u'\n          ')
                        ____index_140240906199248 -= 1
                        if (____index_140240906199248 > 0):
                            __append('')
                    if (__backup_panel_140240907052624 is __marker):
                        del econtext['panel']
                    else:
                        econtext['panel'] = __backup_panel_140240907052624
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6165abd0> name=None at 7f8c6165a750> -> __attrs_140240907369360
                    __attrs_140240907369360 = _static_140240906202064

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<div class='clearfix'></div>\n        </div>\n      </div>")
                    if (__backup_section_id_140240809074064 is __marker):
                        del econtext['section_id']
                    else:
                        econtext['section_id'] = __backup_section_id_140240809074064
                    __append(u'\n    ')
                    ____index_140240906481168 -= 1
                    if (____index_140240906481168 > 0):
                        __append('')
                if (__backup_section_140240809073424 is __marker):
                    del econtext['section']
                else:
                    econtext['section'] = __backup_section_140240809073424
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240907368784
                __attrs_140240907368784 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240906679952
                __default_140240906679952 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (578:34)> -> __cache_140240906578448
                __token = 22284
                try:
                    __zt_tmp = __attrs_140240907368784
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240906578448 = _static_140241087907024('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (578:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c616b6ad0> -> __condition
                __expression = __cache_140240906578448

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input/>')
                else:
                    __content = __cache_140240906578448
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'here/main_template/macros/master' (2:23)> -> __macro
            __token = 66
            try:
                __zt_tmp = __attrs_140240809071184
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140241087907024('path', u'here/main_template/macros/master', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __token = 66
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140240928802208 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140240928802208
            __i18n_domain = __previous_i18n_domain_140240809072016
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }