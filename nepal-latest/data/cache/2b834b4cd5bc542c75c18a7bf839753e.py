# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/datagrid/datagrid_input.pt'

__tokens = {2005: (u'widget/render', 35, 40), 397: (u'view/extra', 9, 36), 411: (u' view/id_prefi', 9, 50), 486: (u'view/columns', 12, 34), 565: (u'string:header cell-${repeat/column/number}', 14, 35), 638: (u" python: cssclass + (column['mode'] == 'hidden' and ' datagridwidget-hidden-data' or ''", 15, 29), 764: (u'cssclass', 16, 36), 806: (u'column/label', 17, 31), 901: (u'column/required', 19, 33), 1058: (u'column/description', 20, 50), 1091: (u'column/description', 20, 83), 1209: (u'view/allow_insert', 23, 42), 1276: (u'view/allow_delete', 24, 42), 1343: (u'view/allow_reorder', 25, 42), 1411: (u'view/allow_reorder', 26, 42), 1534: (u'view/name_prefix', 29, 72), 1566: (u' view/id_prefi', 29, 104), 1616: (u'view/widgets', 30, 32), 1876: (u'python:view._includeRow(widget.name)', 33, 27), 1665: (u"python:'%s row-%d%s' % (widget.klass, repeat['widget'].number(), widget.mode=='hidden' and ' hidden' or '')", 31, 34), 1812: (u" python:widget.name.split('.')[-1", 32, 38), 2155: (u'view/counterMarker', 41, 46), 2266: (u'string:${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.js', 43, 60), 2441: (u'string:${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.css', 44, 86)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240612399440 = {u'src': u'', u'type': u'text/javascript', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240759775184 = {u'class': u'header', }
_static_140240755171728 = {u'class': u"python:'%s row-%d%s' % (widget.klass, repeat['widget'].number(), widget.mode=='hidden' and ' hidden' or '')", u'data-index': u"python:widget.name.split('.')[-1]", }
_static_140240791785168 = {u'class': u'header', }
_static_140240756766928 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140241133802128 = {}
_static_140240766774928 = {u'data-mode': u'row', u'data-extra': u'view/extra', u'class': u'table table-hover table-responsive table-sm table-borderless datagridwidget-table-view', u'id': u'view/id_prefix', }
_static_140240759773840 = {u'data-id_prefix': u'view/id_prefix', u'class': u'datagridwidget-body', u'data-name_prefix': u'view/name_prefix', }
_static_140240762816784 = {u'class': u'required', u'title': u'Required', }
_static_140240763235024 = {u'media': u'screen', u'href': u'', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140240759774288 = {u'class': u'header', }
_static_140240759772112 = {u'class': u'header', }
_static_140240762815504 = {u'class': u'formHelp', }
_static_140240791785232 = {u'class': u'header', }
_static_140240604789584 = {u'type': u'hidden', }

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

    def render_widget_row(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240755173008
            __attrs_140240755173008 = _static_140241133802128
            __append(u'\n            ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240612400784
            __attrs_140240612400784 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612398224
            __default_140240612398224 = _DEFAULT_MARKER

            # <Value u'widget/render' (35:40)> -> __cache_140240612397136
            __token = 2005
            try:
                __zt_tmp = __attrs_140240612400784
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240612397136 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'widget/render' (35:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4fe29810> -> __condition
            __expression = __cache_140240612397136

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div></div>')
            else:
                __content = __cache_140240612397136
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n          ')
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

            # <Static value=<_ast.Dict object at 0x7f8c587d78d0> name=None at 7f8c587d7e90> -> __attrs_140240612231952
            __attrs_140240612231952 = _static_140240756766928
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c59162e90> name=None at 7f8c59162390> -> __attrs_140240766774224
            __attrs_140240766774224 = _static_140240766774928

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table table-hover table-responsive table-sm table-borderless datagridwidget-table-view" data-mode="row"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766772880
            __default_140240766772880 = _DEFAULT_MARKER

            # <Substitution u'view/extra' (9:36)> -> __attr_data_extra
            __token = 397
            try:
                __zt_tmp = __attrs_140240766774224
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_extra = _static_140241087907024('path', u'view/extra', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_data_extra = __quote(__attr_data_extra, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_extra is not None):
                __append((u' data-extra="%s"' % __attr_data_extra))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766771792
            __default_140240766771792 = _DEFAULT_MARKER

            # <Substitution u'view/id_prefix' (9:50)> -> __attr_id
            __token = 411
            try:
                __zt_tmp = __attrs_140240766774224
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140241087907024('path', u'view/id_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240766772944
            __attrs_140240766772944 = _static_140241133802128

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append(u'<thead>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240768293648
            __attrs_140240768293648 = _static_140241133802128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606106960
            __attrs_140240606106960 = _static_140241133802128
            __backup_column_140240610145680 = get('column', __marker)

            # <Value u'view/columns' (12:34)> -> __iterator
            __token = 486
            try:
                __zt_tmp = __attrs_140240606106960
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/columns', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240791782224, ) = getitem('repeat')(u'column', __iterator)
            econtext['column'] = None
            for __item in __iterator:
                econtext['column'] = __item
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c5a93cf10> name=None at 7f8c5a93c110> -> __attrs_140240791783312
                __attrs_140240791783312 = _static_140240791785232
                __backup_cssclass_140240780914960 = get('cssclass', __marker)

                # <Value u'string:header cell-${repeat/column/number}' (14:35)> -> __value
                __token = 565
                try:
                    __zt_tmp = __attrs_140240791783312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('string', u'header cell-${repeat/column/number}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['cssclass'] = __value
                __backup_cssclass_140240782651792 = get('cssclass', __marker)

                # <Value u"python: cssclass + (column['mode'] == 'hidden' and ' datagridwidget-hidden-data' or '')" (15:29)> -> __value
                __token = 638
                try:
                    __zt_tmp = __attrs_140240791783312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u" cssclass + (column['mode'] == 'hidden' and ' datagridwidget-hidden-data' or '')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['cssclass'] = __value

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240791784080
                __default_140240791784080 = _DEFAULT_MARKER

                # <Substitution u'cssclass' (16:36)> -> __attr_class
                __token = 764
                try:
                    __zt_tmp = __attrs_140240791783312
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140241087907024('path', u'cssclass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'header', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240791783696
                __attrs_140240791783696 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240791784528
                __default_140240791784528 = _DEFAULT_MARKER

                # <Value u'column/label' (17:31)> -> __cache_140240791782160
                __token = 806
                try:
                    __zt_tmp = __attrs_140240791783696
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240791782160 = _static_140241087907024('path', u'column/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'column/label' (17:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a93c690> -> __condition
                __expression = __cache_140240791782160

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'title')
                else:
                    __content = __cache_140240791782160
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c58d9c910> name=None at 7f8c5a93c510> -> __attrs_140240762816976
                __attrs_140240762816976 = _static_140240762816784

                # <Value u'column/required' (19:33)> -> __condition
                __token = 901
                try:
                    __zt_tmp = __attrs_140240762816976
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'column/required', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:
                    __previous_i18n_domain_140240762818128 = __i18n_domain
                    __i18n_domain = u'plone'

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="required"')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762818512
                    __default_140240762818512 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f8c58d9c8d0> at 7f8c58d9cd10> -> __attr_title
                    __attr_title = u'Required'
                    __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>&nbsp;</span>')
                    __i18n_domain = __previous_i18n_domain_140240762818128
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8c58d9c410> name=None at 7f8c58d9c3d0> -> __attrs_140240762814992
                __attrs_140240762814992 = _static_140240762815504

                # <Value u'column/description' (20:50)> -> __condition
                __token = 1058
                try:
                    __zt_tmp = __attrs_140240762814992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'column/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="formHelp">')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240762816080
                    __default_140240762816080 = _DEFAULT_MARKER

                    # <Value u'column/description' (20:83)> -> __cache_140240762816464
                    __token = 1091
                    try:
                        __zt_tmp = __attrs_140240762814992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240762816464 = _static_140241087907024('path', u'column/description', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'column/description' (20:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58d9c610> -> __condition
                    __expression = __cache_140240762816464

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Description')
                    else:
                        __content = __cache_140240762816464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n          </th>')
                if (__backup_cssclass_140240782651792 is __marker):
                    del econtext['cssclass']
                else:
                    econtext['cssclass'] = __backup_cssclass_140240782651792
                if (__backup_cssclass_140240780914960 is __marker):
                    del econtext['cssclass']
                else:
                    econtext['cssclass'] = __backup_cssclass_140240780914960
                __append(u'\n        ')
                ____index_140240791782224 -= 1
                if (____index_140240791782224 > 0):
                    __append('')
            if (__backup_column_140240610145680 is __marker):
                del econtext['column']
            else:
                econtext['column'] = __backup_column_140240610145680
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c5a93ced0> name=None at 7f8c5a93ca10> -> __attrs_140240759774736
            __attrs_140240759774736 = _static_140240791785168

            # <Value u'view/allow_insert' (23:42)> -> __condition
            __token = 1209
            try:
                __zt_tmp = __attrs_140240759774736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/allow_insert', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="header"></th>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c58ab5c50> name=None at 7f8c58ab5a50> -> __attrs_140240759774864
            __attrs_140240759774864 = _static_140240759774288

            # <Value u'view/allow_delete' (24:42)> -> __condition
            __token = 1276
            try:
                __zt_tmp = __attrs_140240759774864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/allow_delete', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="header"></th>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c58ab5fd0> name=None at 7f8c58ab55d0> -> __attrs_140240759773200
            __attrs_140240759773200 = _static_140240759775184

            # <Value u'view/allow_reorder' (25:42)> -> __condition
            __token = 1343
            try:
                __zt_tmp = __attrs_140240759773200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/allow_reorder', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="header"></th>')
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c58ab53d0> name=None at 7f8c58ab5410> -> __attrs_140240604790352
            __attrs_140240604790352 = _static_140240759772112

            # <Value u'view/allow_reorder' (26:42)> -> __condition
            __token = 1411
            try:
                __zt_tmp = __attrs_140240604790352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/allow_reorder', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th class="header"></th>')
            __append(u'\n      </tr>\n    </thead>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c58ab5a90> name=None at 7f8c58ab5cd0> -> __attrs_140240604788688
            __attrs_140240604788688 = _static_140240759773840

            # <tbody ... (0:0)
            # --------------------------------------------------------
            __append(u'<tbody class="datagridwidget-body"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604789072
            __default_140240604789072 = _DEFAULT_MARKER

            # <Substitution u'view/name_prefix' (29:72)> -> __attr_data_name_prefix
            __token = 1534
            try:
                __zt_tmp = __attrs_140240604788688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_name_prefix = _static_140241087907024('path', u'view/name_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_data_name_prefix = __quote(__attr_data_name_prefix, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_name_prefix is not None):
                __append((u' data-name_prefix="%s"' % __attr_data_name_prefix))

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604789520
            __default_140240604789520 = _DEFAULT_MARKER

            # <Substitution u'view/id_prefix' (29:104)> -> __attr_data_id_prefix
            __token = 1566
            try:
                __zt_tmp = __attrs_140240604788688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_id_prefix = _static_140241087907024('path', u'view/id_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_data_id_prefix = __quote(__attr_data_id_prefix, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_id_prefix is not None):
                __append((u' data-id_prefix="%s"' % __attr_data_id_prefix))
            __append(u'>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240755171984
            __attrs_140240755171984 = _static_140241133802128
            __backup_widget_140240762491088 = get('widget', __marker)

            # <Value u'view/widgets' (30:32)> -> __iterator
            __token = 1616
            try:
                __zt_tmp = __attrs_140240755171984
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/widgets', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240755174672, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c58652190> name=None at 7f8c58652c10> -> __attrs_140240755172688
                __attrs_140240755172688 = _static_140240755171728

                # <Value u'python:view._includeRow(widget.name)' (33:27)> -> __condition
                __token = 1876
                try:
                    __zt_tmp = __attrs_140240755172688
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'view._includeRow(widget.name)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755172496
                    __default_140240755172496 = _DEFAULT_MARKER

                    # <Substitution u"python:'%s row-%d%s' % (widget.klass, repeat['widget'].number(), widget.mode=='hidden' and ' hidden' or '')" (31:34)> -> __attr_class
                    __token = 1665
                    try:
                        __zt_tmp = __attrs_140240755172688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"'%s row-%d%s' % (widget.klass, repeat['widget'].number(), widget.mode=='hidden' and ' hidden' or '')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755174544
                    __default_140240755174544 = _DEFAULT_MARKER

                    # <Substitution u"python:widget.name.split('.')[-1]" (32:38)> -> __attr_data_index
                    __token = 1812
                    try:
                        __zt_tmp = __attrs_140240755172688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_index = _static_140241087907024('python', u"widget.name.split('.')[-1]", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_data_index = __quote(__attr_data_index, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_index is not None):
                        __append((u' data-index="%s"' % __attr_data_index))
                    __append(u'>\n          ')
                    __token = None
                    render_widget_row(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append(u'\n        </tr>')
                __append(u'\n      ')
                ____index_140240755174672 -= 1
                if (____index_140240755174672 > 0):
                    __append('')
            if (__backup_widget_140240762491088 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240762491088
            __append(u'\n    </tbody>\n  </table>\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7b50> name=None at 7f8c4f6e72d0> -> __attrs_140240612398864
            __attrs_140240612398864 = _static_140240604789584

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240755171472
            __default_140240755171472 = _DEFAULT_MARKER

            # <Value u'view/counterMarker' (41:46)> -> __cache_140240755175312
            __token = 2155
            try:
                __zt_tmp = __attrs_140240612398864
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240755175312 = _static_140241087907024('path', u'view/counterMarker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/counterMarker' (41:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58652110> -> __condition
            __expression = __cache_140240755175312

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" />')
            else:
                __content = __cache_140240755175312
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n  <!-- static resources -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4fe29950> name=None at 7f8c4fe29d50> -> __attrs_140240763236112
            __attrs_140240763236112 = _static_140240612399440

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240763232976
            __default_140240763232976 = _DEFAULT_MARKER

            # <Substitution u'string:${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.js' (43:60)> -> __attr_src
            __token = 2266
            try:
                __zt_tmp = __attrs_140240763236112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140241087907024('string', u'${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.js', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c58e02ad0> name=None at 7f8c58e02490> -> __attrs_140240763233296
            __attrs_140240763233296 = _static_140240763235024

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="stylesheet"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240763232656
            __default_140240763232656 = _DEFAULT_MARKER

            # <Substitution u'string:${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.css' (44:86)> -> __attr_href
            __token = 2441
            try:
                __zt_tmp = __attrs_140240763233296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140241087907024('string', u'${view/portal_url}/++resource++senaite.core.z3cform.static/datagrid.css', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' type="text/css" media="screen"/>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_row': render_widget_row, 'render': render, }