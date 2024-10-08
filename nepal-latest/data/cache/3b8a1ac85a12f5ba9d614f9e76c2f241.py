# -*- coding: utf-8 -*-
__filename = u'/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/worksheet/templates/print/sample_by_column.pt'

__tokens = {410: (u'python:view.getWorksheet()', 14, 66), 467: (u' worksheet/laborator', 15, 29), 518: (u'  worksheet/port', 16, 28), 565: (u'   worksheet/', 17, 27), 609: (u'    worksheet/analyses_ti', 18, 26), 836: (u'worksheet/id', 22, 137), 932: (u'laboratory/url', 26, 30), 1007: (u'string:++plone++senaite.core.static/images/senaite.svg', 27, 58), 1126: (u'worksheet/url', 31, 30), 1154: (u'worksheet/id', 31, 58), 1307: (u'worksheet/date_created', 37, 25), 1421: (u"python:('mailto:%s' % worksheet['createdby']['email'])", 39, 30), 1490: (u'worksheet/createdby/fullname', 39, 99), 1625: (u'worksheet/date_printed', 43, 25), 1739: (u"python:('mailto:%s' % worksheet['printedby']['email'])", 45, 30), 1808: (u'worksheet/printedby/fullname', 45, 99), 1950: (u"python:('mailto:%s' % worksheet['analyst']['email'])", 49, 30), 2017: (u'worksheet/analyst/fullname', 49, 97), 2150: (u'python:view.splitList(ars,view.getNumColumns())', 54, 39), 2334: (u'ars', 59, 29), 2483: (u'ar/id', 60, 143), 2642: (u'ars', 67, 29), 2684: (u'ar/client/url', 68, 36), 2712: (u'ar/client/name', 68, 64), 2854: (u'ars', 73, 29), 2980: (u'ar/sample/sample_type', 74, 120), 2896: (u'ar/sample/sample_type/url', 74, 36), 2936: (u'ar/sample/sample_type/title', 74, 76), 3124: (u'ars', 79, 29), 3166: (u'ar/sample/url', 80, 36), 3194: (u'ar/sample/id', 80, 64), 3336: (u'ars', 85, 29), 3354: (u'ar/sample/date_sampled', 85, 47), 3502: (u'ars', 90, 29), 3520: (u'ar/date_received', 90, 47), 3620: (u'python:len(ars)+1', 94, 38), 3734: (u'anstitles', 96, 32), 3773: (u'antitle', 97, 27), 3862: (u'ars', 99, 38), 3911: (u'python:view.get_analyses_data_by_title(ar, antitle)', 100, 43), 3998: (u'analyses', 101, 33), 4056: (u'analyses', 102, 47), 4108: (u'string:${analysis/review_state}', 103, 41), 4184: (u' repeat/analysis/star', 104, 43), 4247: (u"z python: is_first and clazz or '{} repeat'.format(claz", 105, 39), 4344: (u"zz python: '{} result'.format(cla", 106, 38), 4405: (u'clazz', 106, 99), 4456: (u'analysis/formatted_result', 107, 43), 4525: (u'string:${analysis/formatted_result}', 108, 41), 4614: (u'string:${analysis/unit}', 109, 41), 4732: (u'not:analysis/formatted_result', 111, 49), 4956: (u'not:analyses', 117, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168037618448 = {u'href': u"python:('mailto:%s' % worksheet['printedby']['email'])", }
_static_140168037443472 = {u'href': u'ar/sample/url', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047768144 = {u'href': u'ar/sample/sample_type/url', }
_static_140168037439824 = {u'id': u'footer', }
_static_140168037650640 = {u'src': u'string:++plone++senaite.core.static/images/senaite.svg', u'class': u'logo', u'height': u'25', }
_static_140168037438544 = {u'colspan': u'python:len(ars)+1', u'class': u'analyses', }
_static_140168026350160 = {u'data-addQuietZone': u'true', u'data-code': u'code128', u'data-id': u'ar/id', u'data-barHeight': u'15', u'data-showHRI': u'false', u'class': u'barcode', }
_static_140168026263632 = {u'href': u'laboratory/url', }
_static_140168026279632 = {u'data-addQuietZone': u'true', u'data-code': u'code128', u'data-id': u'worksheet/id', u'data-barHeight': u'15', u'data-showHRI': u'false', u'class': u'barcode', }
_static_140168037529808 = {u'class': u'clazz', }
_static_140168037424848 = {u'href': u"python:('mailto:%s' % worksheet['createdby']['email'])", }
_static_140168026269840 = {u'class': u'content', }
_static_140168257770128 = {}
_static_140168026264592 = {u'class': u'lab-logo', }
_static_140168026268944 = {u'href': u"python:('mailto:%s' % worksheet['analyst']['email'])", }
_static_140168026285904 = {u'class': u'', }
_static_140168208991440 = __compile_zt_expr
_static_140168026279440 = {u'class': u'barcode-container', }
_static_140168026352720 = {u'class': u'requestid', }
_static_140168037652240 = {u'class': u'subheader', }
_static_140168047152528 = {u'href': u'ar/client/url', }
_static_140168083082896 = {u'href': u'worksheet/url', }
_static_140168037639888 = {u'id': u'header', }
_static_140168026366864 = {u'class': u'no-result', }

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
            __append(u'<!--\n    Worksheet AR-by-column Template\n\n    All data is available using the worksheet dictionary.\n    Example for accessing and displaying data:\n\n    <p tal:content="python:worksheet[\'laboratory\'][\'title\']"></p>\n    or\n    <p tal:content="worksheet/laboratory/title"></p>\n\n    See README.txt for further details about the dict structure\n\n-->\n')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047838480
            __attrs_140168047838480 = _static_140168257770128
            __backup_worksheet_140168047840848 = get('worksheet', __marker)

            # <Value u'python:view.getWorksheet()' (14:66)> -> __value
            __token = 410
            try:
                __zt_tmp = __attrs_140168047838480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.getWorksheet()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['worksheet'] = __value
            __backup_laboratory_140168046864144 = get('laboratory', __marker)

            # <Value u'worksheet/laboratory' (15:29)> -> __value
            __token = 467
            try:
                __zt_tmp = __attrs_140168047838480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'worksheet/laboratory', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['laboratory'] = __value
            __backup_portal_140168047840592 = get('portal', __marker)

            # <Value u'worksheet/portal' (16:28)> -> __value
            __token = 518
            try:
                __zt_tmp = __attrs_140168047838480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'worksheet/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_ars_140168047840080 = get('ars', __marker)

            # <Value u'worksheet/ars' (17:27)> -> __value
            __token = 565
            try:
                __zt_tmp = __attrs_140168047838480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'worksheet/ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['ars'] = __value
            __backup_anstitles_140168047840656 = get('anstitles', __marker)

            # <Value u'worksheet/analyses_titles' (18:26)> -> __value
            __token = 609
            try:
                __zt_tmp = __attrs_140168047838480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'worksheet/analyses_titles', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['anstitles'] = __value
            __previous_i18n_domain_140168047837264 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17a6d0> name=None at 7f7b6a17a250> -> __attrs_140168037639376
            __attrs_140168037639376 = _static_140168037639888

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="header">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b696a4e10> name=None at 7f7b696a4110> -> __attrs_140168026277712
            __attrs_140168026277712 = _static_140168026279440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div class='barcode-container'>\n      ")

            # <Static value=<_ast.Dict object at 0x7f7b696a4ed0> name=None at 7f7b696a4b90> -> __attrs_140168026265360
            __attrs_140168026265360 = _static_140168026279632

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div class='barcode' data-code='code128' data-showHRI='false' data-barHeight='15' data-addQuietZone='true'")

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026267088
            __default_140168026267088 = _DEFAULT_MARKER

            # <Substitution u'worksheet/id' (22:137)> -> __attr_data_id
            __token = 836
            try:
                __zt_tmp = __attrs_140168026265360
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_id = _static_140168208991440('path', u'worksheet/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_data_id = __quote(__attr_data_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_id is not None):
                __append((u' data-id="%s"' % __attr_data_id))
            __append(u'>\n      </div>\n    </div>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b696a1410> name=None at 7f7b696a4d50> -> __attrs_140168026265744
            __attrs_140168026265744 = _static_140168026264592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u"<div class='lab-logo'>\n      ")

            # <Static value=<_ast.Dict object at 0x7f7b696a1050> name=None at 7f7b696a13d0> -> __attrs_140168026264144
            __attrs_140168026264144 = _static_140168026263632

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026266256
            __default_140168026266256 = _DEFAULT_MARKER

            # <Substitution u'laboratory/url' (26:30)> -> __attr_href
            __token = 932
            try:
                __zt_tmp = __attrs_140168026264144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('path', u'laboratory/url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17d0d0> name=None at 7f7b6a17dd50> -> __attrs_140168037653136
            __attrs_140168037653136 = _static_140168037650640

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img class="logo" height="25"')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037651600
            __default_140168037651600 = _DEFAULT_MARKER

            # <Substitution u'string:++plone++senaite.core.static/images/senaite.svg' (27:58)> -> __attr_src
            __token = 1007
            try:
                __zt_tmp = __attrs_140168037653136
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140168208991440('string', u'++plone++senaite.core.static/images/senaite.svg', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'/>\n      </a>\n    </div>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026266640
            __attrs_140168026266640 = _static_140168257770128

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6ccd0e90> name=None at 7f7b6a17d510> -> __attrs_140168037591184
            __attrs_140168037591184 = _static_140168083082896

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037592976
            __default_140168037592976 = _DEFAULT_MARKER

            # <Substitution u'worksheet/url' (31:30)> -> __attr_href
            __token = 1126
            try:
                __zt_tmp = __attrs_140168037591184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('path', u'worksheet/url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037651856
            __default_140168037651856 = _DEFAULT_MARKER

            # <Value u'worksheet/id' (31:58)> -> __cache_140168037653456
            __token = 1154
            try:
                __zt_tmp = __attrs_140168037591184
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037653456 = _static_140168208991440('path', u'worksheet/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/id' (31:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a17ded0> -> __condition
            __expression = __cache_140168037653456

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037653456
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</a>\n    </h1>\n  </div>\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17d710> name=None at 7f7b6a17d450> -> __attrs_140168037592912
            __attrs_140168037592912 = _static_140168037652240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="subheader">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168092195792
            __attrs_140168092195792 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037423952
            __attrs_140168037423952 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168037421328 = []
            __append_140168037421328 = __stream_140168037421328.append
            __append_140168037421328(u'Created on')
            __msgid_140168037421328 = __re_whitespace(''.join(__stream_140168037421328)).strip()
            if __msgid_140168037421328:
                __append(translate(__msgid_140168037421328, mapping=None, default=__msgid_140168037421328, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037424080
            __attrs_140168037424080 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037423888
            __default_140168037423888 = _DEFAULT_MARKER

            # <Value u'worksheet/date_created' (37:25)> -> __cache_140168037423568
            __token = 1307
            try:
                __zt_tmp = __attrs_140168037424080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037423568 = _static_140168208991440('path', u'worksheet/date_created', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/date_created' (37:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a1456d0> -> __condition
            __expression = __cache_140168037423568

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037423568
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037423312
            __attrs_140168037423312 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168037421584 = []
            __append_140168037421584 = __stream_140168037421584.append
            __append_140168037421584(u'by')
            __msgid_140168037421584 = __re_whitespace(''.join(__stream_140168037421584)).strip()
            if __msgid_140168037421584:
                __append(translate(__msgid_140168037421584, mapping=None, default=__msgid_140168037421584, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6a145ed0> name=None at 7f7b6a145a90> -> __attrs_140168026341264
            __attrs_140168026341264 = _static_140168037424848

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026339152
            __default_140168026339152 = _DEFAULT_MARKER

            # <Substitution u"python:('mailto:%s' % worksheet['createdby']['email'])" (39:30)> -> __attr_href
            __token = 1421
            try:
                __zt_tmp = __attrs_140168026341264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('python', u"('mailto:%s' % worksheet['createdby']['email'])", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037422096
            __default_140168037422096 = _DEFAULT_MARKER

            # <Value u'worksheet/createdby/fullname' (39:99)> -> __cache_140168037424336
            __token = 1490
            try:
                __zt_tmp = __attrs_140168026341264
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037424336 = _static_140168208991440('path', u'worksheet/createdby/fullname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/createdby/fullname' (39:99)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a145f90> -> __condition
            __expression = __cache_140168037424336

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037424336
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</a>\n    </div>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026338128
            __attrs_140168026338128 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026338704
            __attrs_140168026338704 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168026339664 = []
            __append_140168026339664 = __stream_140168026339664.append
            __append_140168026339664(u'Printed on')
            __msgid_140168026339664 = __re_whitespace(''.join(__stream_140168026339664)).strip()
            if __msgid_140168026339664:
                __append(translate(__msgid_140168026339664, mapping=None, default=__msgid_140168026339664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026339408
            __attrs_140168026339408 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026337616
            __default_140168026337616 = _DEFAULT_MARKER

            # <Value u'worksheet/date_printed' (43:25)> -> __cache_140168026339920
            __token = 1625
            try:
                __zt_tmp = __attrs_140168026339408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168026339920 = _static_140168208991440('path', u'worksheet/date_printed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/date_printed' (43:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b3d50> -> __condition
            __expression = __cache_140168026339920

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168026339920
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026340752
            __attrs_140168026340752 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168026337936 = []
            __append_140168026337936 = __stream_140168026337936.append
            __append_140168026337936(u'by')
            __msgid_140168026337936 = __re_whitespace(''.join(__stream_140168026337936)).strip()
            if __msgid_140168026337936:
                __append(translate(__msgid_140168026337936, mapping=None, default=__msgid_140168026337936, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b6a175310> name=None at 7f7b6a175a10> -> __attrs_140168037621648
            __attrs_140168037621648 = _static_140168037618448

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037618512
            __default_140168037618512 = _DEFAULT_MARKER

            # <Substitution u"python:('mailto:%s' % worksheet['printedby']['email'])" (45:30)> -> __attr_href
            __token = 1739
            try:
                __zt_tmp = __attrs_140168037621648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('python', u"('mailto:%s' % worksheet['printedby']['email'])", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026346256
            __default_140168026346256 = _DEFAULT_MARKER

            # <Value u'worksheet/printedby/fullname' (45:99)> -> __cache_140168026349264
            __token = 1808
            try:
                __zt_tmp = __attrs_140168037621648
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168026349264 = _static_140168208991440('path', u'worksheet/printedby/fullname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/printedby/fullname' (45:99)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b5290> -> __condition
            __expression = __cache_140168026349264

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168026349264
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</a>\n    </div>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037619536
            __attrs_140168037619536 = _static_140168257770128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168069635664
            __attrs_140168069635664 = _static_140168257770128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140168083137680 = []
            __append_140168083137680 = __stream_140168083137680.append
            __append_140168083137680(u'Analysed by')
            __msgid_140168083137680 = __re_whitespace(''.join(__stream_140168083137680)).strip()
            if __msgid_140168083137680:
                __append(translate(__msgid_140168083137680, mapping=None, default=__msgid_140168083137680, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>:&nbsp;\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b696a2510> name=None at 7f7b696a2610> -> __attrs_140168026267984
            __attrs_140168026267984 = _static_140168026268944

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026271632
            __default_140168026271632 = _DEFAULT_MARKER

            # <Substitution u"python:('mailto:%s' % worksheet['analyst']['email'])" (49:30)> -> __attr_href
            __token = 1950
            try:
                __zt_tmp = __attrs_140168026267984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('python', u"('mailto:%s' % worksheet['analyst']['email'])", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026269456
            __default_140168026269456 = _DEFAULT_MARKER

            # <Value u'worksheet/analyst/fullname' (49:97)> -> __cache_140168026271504
            __token = 2017
            try:
                __zt_tmp = __attrs_140168026267984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168026271504 = _static_140168208991440('path', u'worksheet/analyst/fullname', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'worksheet/analyst/fullname' (49:97)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696a2690> -> __condition
            __expression = __cache_140168026271504

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168026271504
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</a>\n    </div>\n  </div>\n\n  <!-- Repeat the table every 4 ARs -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b696a2890> name=None at 7f7b6a1756d0> -> __attrs_140168026269584
            __attrs_140168026269584 = _static_140168026269840
            __backup_ars_140168047840976 = get('ars', __marker)

            # <Value u'python:view.splitList(ars,view.getNumColumns())' (54:39)> -> __iterator
            __token = 2150
            try:
                __zt_tmp = __attrs_140168026269584
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('python', u'view.splitList(ars,view.getNumColumns())', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168026269968, ) = getitem('repeat')(u'ars', __iterator)
            econtext['ars'] = None
            for __item in __iterator:
                econtext['ars'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="content">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026270992
                __attrs_140168026270992 = _static_140168257770128

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168083170896
                __attrs_140168083170896 = _static_140168257770128

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append(u'<thead>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037653712
                __attrs_140168037653712 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b696b6c50> name=None at 7f7b6aa4e990> -> __attrs_140168026350992
                __attrs_140168026350992 = _static_140168026352720

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="requestid">')
                __stream_140168046899088 = []
                __append_140168046899088 = __stream_140168046899088.append
                __append_140168046899088(u'Request ID')
                __msgid_140168046899088 = __re_whitespace(''.join(__stream_140168046899088)).strip()
                if __msgid_140168046899088:
                    __append(translate(__msgid_140168046899088, mapping=None, default=__msgid_140168046899088, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026352272
                __attrs_140168026352272 = _static_140168257770128
                __backup_ar_140168047344336 = get('ar', __marker)

                # <Value u'ars' (59:29)> -> __iterator
                __token = 2334
                try:
                    __zt_tmp = __attrs_140168026352272
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168026350672, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b696b6250> name=None at 7f7b696b6e50> -> __attrs_140168026317520
                    __attrs_140168026317520 = _static_140168026350160

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u"<div class='barcode' data-code='code128' data-showHRI='false' data-barHeight='15' data-addQuietZone='true'")

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026317200
                    __default_140168026317200 = _DEFAULT_MARKER

                    # <Substitution u'ar/id' (60:143)> -> __attr_data_id
                    __token = 2483
                    try:
                        __zt_tmp = __attrs_140168026317520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_id = _static_140168208991440('path', u'ar/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_data_id = __quote(__attr_data_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_id is not None):
                        __append((u' data-id="%s"' % __attr_data_id))
                    __append(u'></div>\n          </th>')
                    ____index_140168026350672 -= 1
                    if (____index_140168026350672 > 0):
                        __append('\n          ')
                if (__backup_ar_140168047344336 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168047344336
                __append(u'\n        </tr>\n      </thead>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026350096
                __attrs_140168026350096 = _static_140168257770128

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append(u'<tbody>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026320080
                __attrs_140168026320080 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026318864
                __attrs_140168026318864 = _static_140168257770128

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>')
                __stream_140168026316880 = []
                __append_140168026316880 = __stream_140168026316880.append
                __append_140168026316880(u'Client')
                __msgid_140168026316880 = __re_whitespace(''.join(__stream_140168026316880)).strip()
                if __msgid_140168026316880:
                    __append(translate(__msgid_140168026316880, mapping=None, default=__msgid_140168026316880, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026319952
                __attrs_140168026319952 = _static_140168257770128
                __backup_ar_140168026384976 = get('ar', __marker)

                # <Value u'ars' (67:29)> -> __iterator
                __token = 2642
                try:
                    __zt_tmp = __attrs_140168026319952
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168026317264, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa8cd90> name=None at 7f7b6aa8cfd0> -> __attrs_140168047150480
                    __attrs_140168047150480 = _static_140168047152528

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047151696
                    __default_140168047151696 = _DEFAULT_MARKER

                    # <Substitution u'ar/client/url' (68:36)> -> __attr_href
                    __token = 2684
                    try:
                        __zt_tmp = __attrs_140168047150480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('path', u'ar/client/url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047152592
                    __default_140168047152592 = _DEFAULT_MARKER

                    # <Value u'ar/client/name' (68:64)> -> __cache_140168047149200
                    __token = 2712
                    try:
                        __zt_tmp = __attrs_140168047150480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047149200 = _static_140168208991440('path', u'ar/client/name', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'ar/client/name' (68:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa8ce90> -> __condition
                    __expression = __cache_140168047149200

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168047149200
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n          </td>')
                    ____index_140168026317264 -= 1
                    if (____index_140168026317264 > 0):
                        __append('\n          ')
                if (__backup_ar_140168026384976 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168026384976
                __append(u'\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026320784
                __attrs_140168026320784 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047151568
                __attrs_140168047151568 = _static_140168257770128

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>')
                __stream_140168047149776 = []
                __append_140168047149776 = __stream_140168047149776.append
                __append_140168047149776(u'Sample Type')
                __msgid_140168047149776 = __re_whitespace(''.join(__stream_140168047149776)).strip()
                if __msgid_140168047149776:
                    __append(translate(__msgid_140168047149776, mapping=None, default=__msgid_140168047149776, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047150544
                __attrs_140168047150544 = _static_140168257770128
                __backup_ar_140168307498704 = get('ar', __marker)

                # <Value u'ars' (73:29)> -> __iterator
                __token = 2854
                try:
                    __zt_tmp = __attrs_140168047150544
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168047151504, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6ab23250> name=None at 7f7b6ab23150> -> __attrs_140168047769872
                    __attrs_140168047769872 = _static_140168047768144

                    # <Value u'ar/sample/sample_type' (74:120)> -> __condition
                    __token = 2980
                    try:
                        __zt_tmp = __attrs_140168047769872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'ar/sample/sample_type', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047768784
                        __default_140168047768784 = _DEFAULT_MARKER

                        # <Substitution u'ar/sample/sample_type/url' (74:36)> -> __attr_href
                        __token = 2896
                        try:
                            __zt_tmp = __attrs_140168047769872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140168208991440('path', u'ar/sample/sample_type/url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047768464
                        __default_140168047768464 = _DEFAULT_MARKER

                        # <Value u'ar/sample/sample_type/title' (74:76)> -> __cache_140168047768528
                        __token = 2936
                        try:
                            __zt_tmp = __attrs_140168047769872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140168047768528 = _static_140168208991440('path', u'ar/sample/sample_type/title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                        # <BinOp left=<Value u'ar/sample/sample_type/title' (74:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6ab23750> -> __condition
                        __expression = __cache_140168047768528

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140168047768528
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</a>')
                    __append(u'\n          </td>')
                    ____index_140168047151504 -= 1
                    if (____index_140168047151504 > 0):
                        __append('\n          ')
                if (__backup_ar_140168307498704 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168307498704
                __append(u'\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047768208
                __attrs_140168047768208 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047770960
                __attrs_140168047770960 = _static_140168257770128

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>')
                __stream_140168047770512 = []
                __append_140168047770512 = __stream_140168047770512.append
                __append_140168047770512(u'Sample')
                __msgid_140168047770512 = __re_whitespace(''.join(__stream_140168047770512)).strip()
                if __msgid_140168047770512:
                    __append(translate(__msgid_140168047770512, mapping=None, default=__msgid_140168047770512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047769744
                __attrs_140168047769744 = _static_140168257770128
                __backup_ar_140168047008272 = get('ar', __marker)

                # <Value u'ars' (79:29)> -> __iterator
                __token = 3124
                try:
                    __zt_tmp = __attrs_140168047769744
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168047771152, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f7b6a14a790> name=None at 7f7b6a14a3d0> -> __attrs_140168037442384
                    __attrs_140168037442384 = _static_140168037443472

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037443408
                    __default_140168037443408 = _DEFAULT_MARKER

                    # <Substitution u'ar/sample/url' (80:36)> -> __attr_href
                    __token = 3166
                    try:
                        __zt_tmp = __attrs_140168037442384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140168208991440('path', u'ar/sample/url', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037445456
                    __default_140168037445456 = _DEFAULT_MARKER

                    # <Value u'ar/sample/id' (80:64)> -> __cache_140168037445008
                    __token = 3194
                    try:
                        __zt_tmp = __attrs_140168037442384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037445008 = _static_140168208991440('path', u'ar/sample/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'ar/sample/id' (80:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a14ae10> -> __condition
                    __expression = __cache_140168037445008

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168037445008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n          </td>')
                    ____index_140168047771152 -= 1
                    if (____index_140168047771152 > 0):
                        __append('\n          ')
                if (__backup_ar_140168047008272 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168047008272
                __append(u'\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037442960
                __attrs_140168037442960 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026282768
                __attrs_140168026282768 = _static_140168257770128

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>')
                __stream_140168026280528 = []
                __append_140168026280528 = __stream_140168026280528.append
                __append_140168026280528(u'Sampling Date')
                __msgid_140168026280528 = __re_whitespace(''.join(__stream_140168026280528)).strip()
                if __msgid_140168026280528:
                    __append(translate(__msgid_140168026280528, mapping=None, default=__msgid_140168026280528, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026282064
                __attrs_140168026282064 = _static_140168257770128
                __backup_ar_140168047845072 = get('ar', __marker)

                # <Value u'ars' (85:29)> -> __iterator
                __token = 3336
                try:
                    __zt_tmp = __attrs_140168026282064
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168026281488, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026282640
                    __default_140168026282640 = _DEFAULT_MARKER

                    # <Value u'ar/sample/date_sampled' (85:47)> -> __cache_140168026283792
                    __token = 3354
                    try:
                        __zt_tmp = __attrs_140168026282064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168026283792 = _static_140168208991440('path', u'ar/sample/date_sampled', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'ar/sample/date_sampled' (85:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696a5dd0> -> __condition
                    __expression = __cache_140168026283792

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n          ')
                    else:
                        __content = __cache_140168026283792
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</td>')
                    ____index_140168026281488 -= 1
                    if (____index_140168026281488 > 0):
                        __append('\n          ')
                if (__backup_ar_140168047845072 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168047845072
                __append(u'\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026281936
                __attrs_140168026281936 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026283664
                __attrs_140168026283664 = _static_140168257770128

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>')
                __stream_140168026281680 = []
                __append_140168026281680 = __stream_140168026281680.append
                __append_140168026281680(u'Date received')
                __msgid_140168026281680 = __re_whitespace(''.join(__stream_140168026281680)).strip()
                if __msgid_140168026281680:
                    __append(translate(__msgid_140168026281680, mapping=None, default=__msgid_140168026281680, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037440912
                __attrs_140168037440912 = _static_140168257770128
                __backup_ar_140168026331280 = get('ar', __marker)

                # <Value u'ars' (90:29)> -> __iterator
                __token = 3502
                try:
                    __zt_tmp = __attrs_140168037440912
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168037439312, ) = getitem('repeat')(u'ar', __iterator)
                econtext['ar'] = None
                for __item in __iterator:
                    econtext['ar'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037440336
                    __default_140168037440336 = _DEFAULT_MARKER

                    # <Value u'ar/date_received' (90:47)> -> __cache_140168037438800
                    __token = 3520
                    try:
                        __zt_tmp = __attrs_140168037440912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037438800 = _static_140168208991440('path', u'ar/date_received', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'ar/date_received' (90:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a149d10> -> __condition
                    __expression = __cache_140168037438800

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n          ')
                    else:
                        __content = __cache_140168037438800
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</td>')
                    ____index_140168037439312 -= 1
                    if (____index_140168037439312 > 0):
                        __append('\n          ')
                if (__backup_ar_140168026331280 is __marker):
                    del econtext['ar']
                else:
                    econtext['ar'] = __backup_ar_140168026331280
                __append(u'\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037439056
                __attrs_140168037439056 = _static_140168257770128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b6a149450> name=None at 7f7b6a1497d0> -> __attrs_140168037440592
                __attrs_140168037440592 = _static_140168037438544

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="analyses"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037438032
                __default_140168037438032 = _DEFAULT_MARKER

                # <Substitution u'python:len(ars)+1' (94:38)> -> __attr_colspan
                __token = 3620
                try:
                    __zt_tmp = __attrs_140168037440592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_colspan = _static_140168208991440('python', u'len(ars)+1', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_colspan = __quote(__attr_colspan, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_colspan is not None):
                    __append((u' colspan="%s"' % __attr_colspan))
                __append(u'>')
                __stream_140168037438928 = []
                __append_140168037438928 = __stream_140168037438928.append
                __append_140168037438928(u'Analyses')
                __msgid_140168037438928 = __re_whitespace(''.join(__stream_140168037438928)).strip()
                if __msgid_140168037438928:
                    __append(translate(__msgid_140168037438928, mapping=None, default=__msgid_140168037438928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</th>\n        </tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037440720
                __attrs_140168037440720 = _static_140168257770128
                __backup_antitle_140168047171920 = get('antitle', __marker)

                # <Value u'anstitles' (96:32)> -> __iterator
                __token = 3734
                try:
                    __zt_tmp = __attrs_140168037440720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140168208991440('path', u'anstitles', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                (__iterator, ____index_140168037439952, ) = getitem('repeat')(u'antitle', __iterator)
                econtext['antitle'] = None
                for __item in __iterator:
                    econtext['antitle'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037403920
                    __attrs_140168037403920 = _static_140168257770128

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th>')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168160146192
                    __default_140168160146192 = _DEFAULT_MARKER

                    # <Value u'antitle' (97:27)> -> __cache_140168160145744
                    __token = 3773
                    try:
                        __zt_tmp = __attrs_140168037403920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168160145744 = _static_140168208991440('path', u'antitle', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'antitle' (97:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b7164f5d0> -> __condition
                    __expression = __cache_140168160145744

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168160145744
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</th>\n          <!-- (Partial) Result -->\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037404624
                    __attrs_140168037404624 = _static_140168257770128
                    __backup_ar_140168083170192 = get('ar', __marker)

                    # <Value u'ars' (99:38)> -> __iterator
                    __token = 3862
                    try:
                        __zt_tmp = __attrs_140168037404624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140168208991440('path', u'ars', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    (__iterator, ____index_140168037400912, ) = getitem('repeat')(u'ar', __iterator)
                    econtext['ar'] = None
                    for __item in __iterator:
                        econtext['ar'] = __item
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037402320
                        __attrs_140168037402320 = _static_140168257770128
                        __backup_analyses_140168082135120 = get('analyses', __marker)

                        # <Value u'python:view.get_analyses_data_by_title(ar, antitle)' (100:43)> -> __value
                        __token = 3911
                        try:
                            __zt_tmp = __attrs_140168037402320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140168208991440('python', u'view.get_analyses_data_by_title(ar, antitle)', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        econtext['analyses'] = __value
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037404304
                        __attrs_140168037404304 = _static_140168257770128

                        # <Value u'analyses' (101:33)> -> __condition
                        __token = 3998
                        try:
                            __zt_tmp = __attrs_140168037404304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('path', u'analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td>\n                ')

                            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037401552
                            __attrs_140168037401552 = _static_140168257770128
                            __backup_analysis_140168026382736 = get('analysis', __marker)

                            # <Value u'analyses' (102:47)> -> __iterator
                            __token = 4056
                            try:
                                __zt_tmp = __attrs_140168037401552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140168208991440('path', u'analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                            (__iterator, ____index_140168037531216, ) = getitem('repeat')(u'analysis', __iterator)
                            econtext['analysis'] = None
                            for __item in __iterator:
                                econtext['analysis'] = __item
                                __append(u'\n                  ')

                                # <Static value=<_ast.Dict object at 0x7f7b6a15f8d0> name=None at 7f7b6a15f310> -> __attrs_140168037529360
                                __attrs_140168037529360 = _static_140168037529808
                                __backup_clazz_140168082135696 = get('clazz', __marker)

                                # <Value u'string:${analysis/review_state}' (103:41)> -> __value
                                __token = 4108
                                try:
                                    __zt_tmp = __attrs_140168037529360
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140168208991440('string', u'${analysis/review_state}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                econtext['clazz'] = __value
                                __backup_is_first_140168037528272 = get('is_first', __marker)

                                # <Value u'repeat/analysis/start' (104:43)> -> __value
                                __token = 4184
                                try:
                                    __zt_tmp = __attrs_140168037529360
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140168208991440('path', u'repeat/analysis/start', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                econtext['is_first'] = __value
                                __backup_clazz_140168037529296 = get('clazz', __marker)

                                # <Value u"python: is_first and clazz or '{} repeat'.format(clazz)" (105:39)> -> __value
                                __token = 4247
                                try:
                                    __zt_tmp = __attrs_140168037529360
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140168208991440('python', u" is_first and clazz or '{} repeat'.format(clazz)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                econtext['clazz'] = __value
                                __backup_clazz_140168037528848 = get('clazz', __marker)

                                # <Value u"python: '{} result'.format(clazz)" (106:38)> -> __value
                                __token = 4344
                                try:
                                    __zt_tmp = __attrs_140168037529360
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140168208991440('python', u" '{} result'.format(clazz)", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                econtext['clazz'] = __value

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div')

                                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037529616
                                __default_140168037529616 = _DEFAULT_MARKER

                                # <Substitution u'clazz' (106:99)> -> __attr_class
                                __token = 4405
                                try:
                                    __zt_tmp = __attrs_140168037529360
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140168208991440('path', u'clazz', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>\n                    ')

                                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037527632
                                __attrs_140168037527632 = _static_140168257770128

                                # <Value u'analysis/formatted_result' (107:43)> -> __condition
                                __token = 4456
                                try:
                                    __zt_tmp = __attrs_140168037527632
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140168208991440('path', u'analysis/formatted_result', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                if __condition:
                                    __append(u'\n                      ')

                                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026305040
                                    __attrs_140168026305040 = _static_140168257770128

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>')

                                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026306064
                                    __default_140168026306064 = _DEFAULT_MARKER

                                    # <Value u'string:${analysis/formatted_result}' (108:41)> -> __cache_140168026306832
                                    __token = 4525
                                    try:
                                        __zt_tmp = __attrs_140168026305040
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140168026306832 = _static_140168208991440('string', u'${analysis/formatted_result}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'string:${analysis/formatted_result}' (108:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696ab690> -> __condition
                                    __expression = __cache_140168026306832

                                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append(u'100')
                                    else:
                                        __content = __cache_140168026306832
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>\n                      ')

                                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026306000
                                    __attrs_140168026306000 = _static_140168257770128

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>')

                                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026306448
                                    __default_140168026306448 = _DEFAULT_MARKER

                                    # <Value u'string:${analysis/unit}' (109:41)> -> __cache_140168026306704
                                    __token = 4614
                                    try:
                                        __zt_tmp = __attrs_140168026306000
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140168026306704 = _static_140168208991440('string', u'${analysis/unit}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'string:${analysis/unit}' (109:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696abf90> -> __condition
                                    __expression = __cache_140168026306704

                                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append(u'ml')
                                    else:
                                        __content = __cache_140168026306704
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>\n                    ')
                                __append(u'\n                    ')

                                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026305552
                                __attrs_140168026305552 = _static_140168257770128

                                # <Value u'not:analysis/formatted_result' (111:49)> -> __condition
                                __token = 4732
                                try:
                                    __zt_tmp = __attrs_140168026305552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140168208991440('not', u'analysis/formatted_result', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                                if __condition:
                                    __append(u'\n                      ')

                                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026285136
                                    __attrs_140168026285136 = _static_140168257770128

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>&nbsp;</span>\n                    ')
                                __append(u'\n                  </div>')
                                if (__backup_clazz_140168037528848 is __marker):
                                    del econtext['clazz']
                                else:
                                    econtext['clazz'] = __backup_clazz_140168037528848
                                if (__backup_clazz_140168037529296 is __marker):
                                    del econtext['clazz']
                                else:
                                    econtext['clazz'] = __backup_clazz_140168037529296
                                if (__backup_is_first_140168037528272 is __marker):
                                    del econtext['is_first']
                                else:
                                    econtext['is_first'] = __backup_is_first_140168037528272
                                if (__backup_clazz_140168082135696 is __marker):
                                    del econtext['clazz']
                                else:
                                    econtext['clazz'] = __backup_clazz_140168082135696
                                __append(u'\n                ')
                                ____index_140168037531216 -= 1
                                if (____index_140168037531216 > 0):
                                    __append('')
                            if (__backup_analysis_140168026382736 is __marker):
                                del econtext['analysis']
                            else:
                                econtext['analysis'] = __backup_analysis_140168026382736
                            __append(u'\n              </td>')
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f7b696ba390> name=None at 7f7b6a140c10> -> __attrs_140168026308112
                        __attrs_140168026308112 = _static_140168026366864

                        # <Value u'not:analyses' (117:33)> -> __condition
                        __token = 4956
                        try:
                            __zt_tmp = __attrs_140168026308112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140168208991440('not', u'analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u"<td class='no-result'>\n                ")

                            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026286864
                            __attrs_140168026286864 = _static_140168257770128

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>X</div>\n              </td>')
                        __append(u'\n            ')
                        if (__backup_analyses_140168082135120 is __marker):
                            del econtext['analyses']
                        else:
                            econtext['analyses'] = __backup_analyses_140168082135120
                        __append(u'\n          ')
                        ____index_140168037400912 -= 1
                        if (____index_140168037400912 > 0):
                            __append('')
                    if (__backup_ar_140168083170192 is __marker):
                        del econtext['ar']
                    else:
                        econtext['ar'] = __backup_ar_140168083170192
                    __append(u'\n        </tr>')
                    ____index_140168037439952 -= 1
                    if (____index_140168037439952 > 0):
                        __append('\n        ')
                if (__backup_antitle_140168047171920 is __marker):
                    del econtext['antitle']
                else:
                    econtext['antitle'] = __backup_antitle_140168047171920
                __append(u'\n      </tbody>\n    </table>\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6a149950> name=None at 7f7b6a149690> -> __attrs_140168037402896
                __attrs_140168037402896 = _static_140168037439824

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="footer">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696a6750> name=None at 7f7b696a6850> -> __attrs_140168026285200
                __attrs_140168026285200 = _static_140168026285904

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="">')
                __stream_140168026287248 = []
                __append_140168026287248 = __stream_140168026287248.append
                __append_140168026287248(u'\n        Legend: Results in ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026286352
                __attrs_140168026286352 = _static_140168257770128

                # <em ... (0:0)
                # --------------------------------------------------------
                __append_140168026287248(u'<em>italic</em> font are pending, results in ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026285520
                __attrs_140168026285520 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append_140168026287248(u'<strong>bold</strong> font are verified.\n      ')
                __msgid_140168026287248 = __re_whitespace(''.join(__stream_140168026287248)).strip()
                if __msgid_140168026287248:
                    __append(translate(__msgid_140168026287248, mapping=None, default=__msgid_140168026287248, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n    </div>\n  </div>')
                ____index_140168026269968 -= 1
                if (____index_140168026269968 > 0):
                    __append('\n  ')
            if (__backup_ars_140168047840976 is __marker):
                del econtext['ars']
            else:
                econtext['ars'] = __backup_ars_140168047840976
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140168047837264
            if (__backup_anstitles_140168047840656 is __marker):
                del econtext['anstitles']
            else:
                econtext['anstitles'] = __backup_anstitles_140168047840656
            if (__backup_ars_140168047840080 is __marker):
                del econtext['ars']
            else:
                econtext['ars'] = __backup_ars_140168047840080
            if (__backup_portal_140168047840592 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168047840592
            if (__backup_laboratory_140168046864144 is __marker):
                del econtext['laboratory']
            else:
                econtext['laboratory'] = __backup_laboratory_140168046864144
            if (__backup_worksheet_140168047840848 is __marker):
                del econtext['worksheet']
            else:
                econtext['worksheet'] = __backup_worksheet_140168047840848
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }