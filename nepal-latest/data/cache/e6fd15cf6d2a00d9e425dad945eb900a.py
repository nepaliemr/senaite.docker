# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/datagrid/datagridrow_input.pt'

__tokens = {285: (u'view/subform/widgets/values', 8, 32), 345: (u"python:('cell-%d ' % repeat['widget'].number()) + ('datagridwidget-hidden-data' if widget.mode == 'hidden' else 'datagridwidget-cell')", 9, 30), 516: (u'widget/render', 10, 34), 560: (u'widget/error', 11, 26), 637: (u'widget/error/render', 12, 36), 868: (u'string:${view/name}-empty-marker', 20, 32), 1006: (u'view/isInsertEnabled', 25, 21), 1304: (u'view/isDeleteEnabled', 36, 21), 1622: (u'view/isReorderEnabled', 47, 21), 1937: (u'view/isReorderEnabled', 58, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240763235152 = {u'class': u'fas fa-trash', }
_static_140240606107152 = {u'type': u'hidden', u'name': u'field-empty-marker', u'value': u'1', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240605380048 = {u'class': u'btn btn-sm btn-outline-secondary dgf--row-movedown', u'title': u'Move down', }
_static_140240782652304 = {u'class': u'datagridwidget-manipulator dgf--row-movedown', }
_static_140240779792272 = {u'class': u'datagridwidget-manipulator insert-row', }
_static_140240759772496 = {u'class': u"python:('cell-%d ' % repeat['widget'].number()) + ('datagridwidget-hidden-data' if widget.mode == 'hidden' else 'datagridwidget-cell')", }
_static_140241133802128 = {}
_static_140240606442640 = {u'class': u'datagridwidget-manipulator delete-row', }
_static_140240770405968 = {u'class': u'small text-danger', }
_static_140240779789200 = {u'class': u'btn btn-sm btn-outline-secondary dgf--row-add', u'title': u'Add row', }
_static_140240605377616 = {u'class': u'fas fa-arrow-down', }
_static_140240606444176 = {u'href': u'', u'class': u'btn btn-sm btn-outline-secondary dgf--row-delete', u'title': u'Delete row', }
_static_140240782653648 = {u'class': u'fas fa-arrow-up', }
_static_140240782652112 = {u'class': u'btn btn-sm btn-outline-secondary dgf--row-moveup', u'title': u'Move up', }
_static_140240780916688 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140240763234768 = {u'class': u'datagridwidget-manipulator dgf--row-moveup', }
_static_140240759773968 = {u'class': u'datagridwidget-hidden-data', }
_static_140240606443920 = {u'class': u'fas fa-plus', }

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

            # <Static value=<_ast.Dict object at 0x7f8c59edf7d0> name=None at 7f8c59edfcd0> -> __attrs_140240759773776
            __attrs_140240759773776 = _static_140240780916688
            __append(u'\n\n  <!-- Data rows -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240759773328
            __attrs_140240759773328 = _static_140241133802128
            __backup_widget_140240605378128 = get('widget', __marker)

            # <Value u'view/subform/widgets/values' (8:32)> -> __iterator
            __token = 285
            try:
                __zt_tmp = __attrs_140240759773328
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/subform/widgets/values', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240759775184, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c58ab5550> name=None at 7f8c58ab5950> -> __attrs_140240759773456
                __attrs_140240759773456 = _static_140240759772496

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240759772112
                __default_140240759772112 = _DEFAULT_MARKER

                # <Substitution u"python:('cell-%d ' % repeat['widget'].number()) + ('datagridwidget-hidden-data' if widget.mode == 'hidden' else 'datagridwidget-cell')" (9:30)> -> __attr_class
                __token = 345
                try:
                    __zt_tmp = __attrs_140240759773456
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140241087907024('python', u"('cell-%d ' % repeat['widget'].number()) + ('datagridwidget-hidden-data' if widget.mode == 'hidden' else 'datagridwidget-cell')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240770407312
                __attrs_140240770407312 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240770406864
                __default_140240770406864 = _DEFAULT_MARKER

                # <Value u'widget/render' (10:34)> -> __cache_140240770406288
                __token = 516
                try:
                    __zt_tmp = __attrs_140240770407312
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240770406288 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/render' (10:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c594d9950> -> __condition
                __expression = __cache_140240770406288

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140240770406288
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c594d9650> name=None at 7f8c594d9f90> -> __attrs_140240770407888
                __attrs_140240770407888 = _static_140240770405968

                # <Value u'widget/error' (11:26)> -> __condition
                __token = 560
                try:
                    __zt_tmp = __attrs_140240770407888
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'widget/error', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="small text-danger">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240770408400
                    __attrs_140240770408400 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240770407568
                    __default_140240770407568 = _DEFAULT_MARKER

                    # <Value u'widget/error/render' (12:36)> -> __cache_140240770404432
                    __token = 637
                    try:
                        __zt_tmp = __attrs_140240770408400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240770404432 = _static_140241087907024('path', u'widget/error/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/error/render' (12:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c594d94d0> -> __condition
                    __expression = __cache_140240770404432

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>error</div>')
                    else:
                        __content = __cache_140240770404432
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n      </div>')
                __append(u'\n    </td>\n  ')
                ____index_140240759775184 -= 1
                if (____index_140240759775184 > 0):
                    __append('')
            if (__backup_widget_140240605378128 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240605378128
            __append(u'\n\n  <!-- Empty marker -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c58ab5b10> name=None at 7f8c58ab5990> -> __attrs_140240770404816
            __attrs_140240770404816 = _static_140240759773968

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="datagridwidget-hidden-data">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c4f829610> name=None at 7f8c4f8294d0> -> __attrs_140240779791312
            __attrs_140240779791312 = _static_140240606107152

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779790736
            __default_140240779790736 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}-empty-marker' (20:32)> -> __attr_name
            __token = 868
            try:
                __zt_tmp = __attrs_140240779791312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('string', u'${view/name}-empty-marker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u' type="hidden" value="1" />\n  </td>\n\n  <!-- Add row -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c59dccf90> name=None at 7f8c59dcc750> -> __attrs_140240779791696
            __attrs_140240779791696 = _static_140240779792272

            # <Value u'view/isInsertEnabled' (25:21)> -> __condition
            __token = 1006
            try:
                __zt_tmp = __attrs_140240779791696
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/isInsertEnabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="datagridwidget-manipulator insert-row">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c59dcc390> name=None at 7f8c59dcc350> -> __attrs_140240606443600
                __attrs_140240606443600 = _static_140240779789200

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button class="btn btn-sm btn-outline-secondary dgf--row-add"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779789648
                __default_140240779789648 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c59dcc510> at 7f8c59dcc4d0> -> __attr_title
                __attr_title = u'Add row'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c4f87b990> name=None at 7f8c4f87bfd0> -> __attrs_140240606443088
                __attrs_140240606443088 = _static_140240606443920

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-plus" />\n    </button>\n  </td>')
            __append(u'\n\n  <!-- Delete row -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4f87b490> name=None at 7f8c4f87b2d0> -> __attrs_140240606444816
            __attrs_140240606444816 = _static_140240606442640

            # <Value u'view/isDeleteEnabled' (36:21)> -> __condition
            __token = 1304
            try:
                __zt_tmp = __attrs_140240606444816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/isDeleteEnabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="datagridwidget-manipulator delete-row">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c4f87ba90> name=None at 7f8c4f87bad0> -> __attrs_140240763233616
                __attrs_140240763233616 = _static_140240606444176

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button href="" class="btn btn-sm btn-outline-secondary dgf--row-delete"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240763233424
                __default_140240763233424 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c58e02790> at 7f8c58e02390> -> __attr_title
                __attr_title = u'Delete row'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c58e02b50> name=None at 7f8c58e02dd0> -> __attrs_140240763233936
                __attrs_140240763233936 = _static_140240763235152

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-trash" />\n    </button>\n  </td>')
            __append(u'\n\n  <!-- Move up -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c58e029d0> name=None at 7f8c58e02950> -> __attrs_140240763232912
            __attrs_140240763232912 = _static_140240763234768

            # <Value u'view/isReorderEnabled' (47:21)> -> __condition
            __token = 1622
            try:
                __zt_tmp = __attrs_140240763232912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/isReorderEnabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="datagridwidget-manipulator dgf--row-moveup">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c5a0872d0> name=None at 7f8c5a087350> -> __attrs_140240782654288
                __attrs_140240782654288 = _static_140240782652112

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button class="btn btn-sm btn-outline-secondary dgf--row-moveup"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240782654992
                __default_140240782654992 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c5a087810> at 7f8c5a0870d0> -> __attr_title
                __attr_title = u'Move up'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c5a0878d0> name=None at 7f8c5a087cd0> -> __attrs_140240782655312
                __attrs_140240782655312 = _static_140240782653648

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-arrow-up" />\n    </button>\n  </td>')
            __append(u'\n\n  <!-- Move down -->\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c5a087390> name=None at 7f8c5a087a10> -> __attrs_140240605377488
            __attrs_140240605377488 = _static_140240782652304

            # <Value u'view/isReorderEnabled' (58:21)> -> __condition
            __token = 1937
            try:
                __zt_tmp = __attrs_140240605377488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'view/isReorderEnabled', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td class="datagridwidget-manipulator dgf--row-movedown">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c4f777dd0> name=None at 7f8c4f777b90> -> __attrs_140240605377552
                __attrs_140240605377552 = _static_140240605380048

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button class="btn btn-sm btn-outline-secondary dgf--row-movedown"')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240605377296
                __default_140240605377296 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f8c4f7777d0> at 7f8c4f7771d0> -> __attr_title
                __attr_title = u'Move down'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c4f777450> name=None at 7f8c4f777110> -> __attrs_140240605378960
                __attrs_140240605378960 = _static_140240605377616

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="fas fa-arrow-down" />\n    </button>\n  </td>')
            __append(u'\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }