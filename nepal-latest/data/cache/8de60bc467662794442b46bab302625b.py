# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/datagrid/datagrid_display.pt'

__tokens = {1548: (u'widget/render', 36, 42), 312: (u'view/widgets', 9, 26), 359: (u'string:table table-sm table-striped table-responsive ${view/display_table_css_class}', 10, 33), 474: (u' view/id_prefi', 11, 29), 566: (u'view/columns', 14, 36), 643: (u"python:column['mode'] != 'hidden'", 16, 31), 712: (u'column/label', 17, 33), 837: (u'column/required', 20, 35), 1154: (u'view/name_prefix', 30, 46), 1203: (u' view/id_prefi', 31, 31), 1256: (u'view/widgets', 32, 34), 1300: (u"python:widget.mode != 'hidden' and not widget.name.endswith('AA') and not widget.name.endswith('TT')", 33, 29), 1438: (u'widget/klass', 34, 36), 1721: (u'view/counterMarker', 43, 34)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240780916176 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240748635728 = {u'data-id_prefix': u'view/id_prefix', u'id': u'datagridwidget-tbody', u'data-name_prefix': u'view/name_prefix', }
_static_140241133802128 = {}
_static_140240612168400 = {u'type': u'hidden', }
_static_140240776686800 = {u'class': u'', }
_static_140240612171088 = {u'class': u'required', u'title': u'Required', }
_static_140240776684752 = {u'class': u'datagridwidget-table-view', u'id': u'view/id_prefix', }
_static_140240748635984 = {u'class': u'header', }
_static_140240606443920 = {u'class': u'widget/klass', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240604787792
            __attrs_140240604787792 = _static_140241133802128
            __append(u'\n              ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240789376272
            __attrs_140240789376272 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240789375440
            __default_140240789375440 = _DEFAULT_MARKER

            # <Value u'widget/render' (36:42)> -> __cache_140240604790736
            __token = 1548
            try:
                __zt_tmp = __attrs_140240789376272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240604790736 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'widget/render' (36:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4f6e7e90> -> __condition
            __expression = __cache_140240604790736

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div></div>')
            else:
                __content = __cache_140240604790736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n            ')
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

            # <Static value=<_ast.Dict object at 0x7f8c59edf5d0> name=None at 7f8c59edf210> -> __attrs_140240604538256
            __attrs_140240604538256 = _static_140240780916176
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240776687120
            __attrs_140240776687120 = _static_140241133802128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c59ad64d0> name=None at 7f8c59ad62d0> -> __attrs_140240776685968
            __attrs_140240776685968 = _static_140240776684752

            # <Value u'view/widgets' (9:26)> -> __condition
            __token = 312
            try:
                __zt_tmp = __attrs_140240776685968
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/widgets', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <table ... (0:0)
                # --------------------------------------------------------
                __append(u'<table')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240776684688
                __default_140240776684688 = _DEFAULT_MARKER

                # <Substitution u'string:table table-sm table-striped table-responsive ${view/display_table_css_class}' (10:33)> -> __attr_class
                __token = 359
                try:
                    __zt_tmp = __attrs_140240776685968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140241087907024('string', u'table table-sm table-striped table-responsive ${view/display_table_css_class}', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'datagridwidget-table-view', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240776686672
                __default_140240776686672 = _DEFAULT_MARKER

                # <Substitution u'view/id_prefix' (11:29)> -> __attr_id
                __token = 474
                try:
                    __zt_tmp = __attrs_140240776685968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140241087907024('path', u'view/id_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u' >\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c59ad6cd0> name=None at 7f8c59ad6bd0> -> __attrs_140240763235536
                __attrs_140240763235536 = _static_140240776686800

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append(u'<thead class="">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240763232656
                __attrs_140240763232656 = _static_140241133802128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240748634320
                __attrs_140240748634320 = _static_140241133802128
                __backup_column_140240756361488 = get('column', __marker)

                # <Value u'view/columns' (14:36)> -> __iterator
                __token = 566
                try:
                    __zt_tmp = __attrs_140240748634320
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/columns', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240748634512, ) = getitem('repeat')(u'column', __iterator)
                econtext['column'] = None
                for __item in __iterator:
                    econtext['column'] = __item
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c58016750> name=None at 7f8c580167d0> -> __attrs_140240748637584
                    __attrs_140240748637584 = _static_140240748635984

                    # <Value u"python:column['mode'] != 'hidden'" (16:31)> -> __condition
                    __token = 643
                    try:
                        __zt_tmp = __attrs_140240748637584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u"column['mode'] != 'hidden'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<th class="header">\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240803782288
                        __attrs_140240803782288 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240803779856
                        __default_140240803779856 = _DEFAULT_MARKER

                        # <Value u'column/label' (17:33)> -> __cache_140240803781968
                        __token = 712
                        try:
                            __zt_tmp = __attrs_140240803782288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240803781968 = _static_140241087907024('path', u'column/label', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'column/label' (17:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5b4ada90> -> __condition
                        __expression = __cache_140240803781968

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240803781968
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c4fdf1d50> name=None at 7f8c4fdf1f10> -> __attrs_140240612169808
                        __attrs_140240612169808 = _static_140240612171088

                        # <Value u'column/required' (20:35)> -> __condition
                        __token = 837
                        try:
                            __zt_tmp = __attrs_140240612169808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('path', u'column/required', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:
                            __previous_i18n_domain_140240612170384 = __i18n_domain
                            __i18n_domain = u'plone'

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="required"')

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612169168
                            __default_140240612169168 = _DEFAULT_MARKER

                            # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f8c4fdf1b10> at 7f8c4fdf19d0> -> __attr_title
                            __attr_title = u'Required'
                            __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            if (__attr_title is not None):
                                __append((u' title="%s"' % __attr_title))
                            __append(u'>\n                &nbsp;\n              </span>')
                            __i18n_domain = __previous_i18n_domain_140240612170384
                        __append(u'\n            </th>')
                    __append(u'\n          ')
                    ____index_140240748634512 -= 1
                    if (____index_140240748634512 > 0):
                        __append('')
                if (__backup_column_140240756361488 is __marker):
                    del econtext['column']
                else:
                    econtext['column'] = __backup_column_140240756361488
                __append(u'\n        </tr>\n      </thead>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c58016650> name=None at 7f8c58016990> -> __attrs_140240612171344
                __attrs_140240612171344 = _static_140240748635728

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append(u'<tbody id="datagridwidget-tbody"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612169744
                __default_140240612169744 = _DEFAULT_MARKER

                # <Substitution u'view/name_prefix' (30:46)> -> __attr_data_name_prefix
                __token = 1154
                try:
                    __zt_tmp = __attrs_140240612171344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_name_prefix = _static_140241087907024('path', u'view/name_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_data_name_prefix = __quote(__attr_data_name_prefix, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_name_prefix is not None):
                    __append((u' data-name_prefix="%s"' % __attr_data_name_prefix))

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240612168528
                __default_140240612168528 = _DEFAULT_MARKER

                # <Substitution u'view/id_prefix' (31:31)> -> __attr_data_id_prefix
                __token = 1203
                try:
                    __zt_tmp = __attrs_140240612171344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_id_prefix = _static_140241087907024('path', u'view/id_prefix', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_data_id_prefix = __quote(__attr_data_id_prefix, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_id_prefix is not None):
                    __append((u' data-id_prefix="%s"' % __attr_data_id_prefix))
                __append(u'>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240606442576
                __attrs_140240606442576 = _static_140241133802128
                __backup_widget_140240752399376 = get('widget', __marker)

                # <Value u'view/widgets' (32:34)> -> __iterator
                __token = 1256
                try:
                    __zt_tmp = __attrs_140240606442576
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'view/widgets', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240606444176, ) = getitem('repeat')(u'widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c4f87b990> name=None at 7f8c4f87be50> -> __attrs_140240606442960
                    __attrs_140240606442960 = _static_140240606443920

                    # <Value u"python:widget.mode != 'hidden' and not widget.name.endswith('AA') and not widget.name.endswith('TT')" (33:29)> -> __condition
                    __token = 1300
                    try:
                        __zt_tmp = __attrs_140240606442960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u"widget.mode != 'hidden' and not widget.name.endswith('AA') and not widget.name.endswith('TT')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tr')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240606443664
                        __default_140240606443664 = _DEFAULT_MARKER

                        # <Substitution u'widget/klass' (34:36)> -> __attr_class
                        __token = 1438
                        try:
                            __zt_tmp = __attrs_140240606442960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('path', u'widget/klass', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n            ')
                        __token = None
                        render_widget_row(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        __append(u'\n          </tr>')
                    __append(u'\n        ')
                    ____index_140240606444176 -= 1
                    if (____index_140240606444176 > 0):
                        __append('')
                if (__backup_widget_140240752399376 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_140240752399376
                __append(u'\n      </tbody>\n    </table>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c4fdf12d0> name=None at 7f8c58016310> -> __attrs_140240604789264
            __attrs_140240604789264 = _static_140240612168400

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604790672
            __default_140240604790672 = _DEFAULT_MARKER

            # <Value u'view/counterMarker' (43:34)> -> __cache_140240606445264
            __token = 1721
            try:
                __zt_tmp = __attrs_140240604789264
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240606445264 = _static_140241087907024('path', u'view/counterMarker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/counterMarker' (43:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4f87bad0> -> __condition
            __expression = __cache_140240606445264

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden"/>')
            else:
                __content = __cache_140240606445264
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n  </div>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_row': render_widget_row, 'render': render, }