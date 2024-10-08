# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/datagrid/datagridrow_display.pt'

__tokens = {30: (u'view/subform/widgets/values', 1, 30), 88: (u"python:widget.mode == 'hidden' and 'datagridwidget-hidden-data' or 'datagridwidget-cell'", 2, 28), 204: (u'widget/error', 3, 24), 250: (u'widget/error/render', 4, 32), 327: (u'widget/render', 7, 32), 525: (u'string:${view/name}-empty-marker', 14, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240756018704 = {u'class': u"python:widget.mode == 'hidden' and 'datagridwidget-hidden-data' or 'datagridwidget-cell'", }
_static_140241133802128 = {}
_static_140240779871632 = {u'type': u'hidden', u'name': u'field-empty-marker', u'value': u'1', }
_static_140240604787600 = {u'class': u'datagridwidget-hidden-data d-none', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240604790416
            __attrs_140240604790416 = _static_140241133802128
            __backup_widget_140240756359952 = get('widget', __marker)

            # <Value u'view/subform/widgets/values' (1:30)> -> __iterator
            __token = 30
            try:
                __zt_tmp = __attrs_140240604790416
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/subform/widgets/values', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240604789392, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7f8c58720e10> name=None at 7f8c4f6e7710> -> __attrs_140240748637136
                __attrs_140240748637136 = _static_140240756018704

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240748634384
                __default_140240748634384 = _DEFAULT_MARKER

                # <Substitution u"python:widget.mode == 'hidden' and 'datagridwidget-hidden-data' or 'datagridwidget-cell'" (2:28)> -> __attr_class
                __token = 88
                try:
                    __zt_tmp = __attrs_140240748637136
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140241087907024('python', u"widget.mode == 'hidden' and 'datagridwidget-hidden-data' or 'datagridwidget-cell'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240748635728
                __attrs_140240748635728 = _static_140241133802128

                # <Value u'widget/error' (3:24)> -> __condition
                __token = 204
                try:
                    __zt_tmp = __attrs_140240748635728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'widget/error', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240748634768
                    __default_140240748634768 = _DEFAULT_MARKER

                    # <Value u'widget/error/render' (4:32)> -> __cache_140240748634512
                    __token = 250
                    try:
                        __zt_tmp = __attrs_140240748635728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240748634512 = _static_140241087907024('path', u'widget/error/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'widget/error/render' (4:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58016f50> -> __condition
                    __expression = __cache_140240748634512

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>\n      error\n    </div>')
                    else:
                        __content = __cache_140240748634512
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240779870288
                __attrs_140240779870288 = _static_140241133802128

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779871248
                __default_140240779871248 = _DEFAULT_MARKER

                # <Value u'widget/render' (7:32)> -> __cache_140240779871184
                __token = 327
                try:
                    __zt_tmp = __attrs_140240779870288
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240779871184 = _static_140241087907024('path', u'widget/render', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/render' (7:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c59de0e50> -> __condition
                __expression = __cache_140240779871184

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140240779871184
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  </td>\n')
                ____index_140240604789392 -= 1
                if (____index_140240604789392 > 0):
                    __append('')
            if (__backup_widget_140240756359952 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140240756359952
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c4f6e7390> name=None at 7f8c4f6e7d50> -> __attrs_140240779874192
            __attrs_140240779874192 = _static_140240604787600

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td class="datagridwidget-hidden-data d-none">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c59de0590> name=None at 7f8c59de0710> -> __attrs_140240779873488
            __attrs_140240779873488 = _static_140240779871632

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779872400
            __default_140240779872400 = _DEFAULT_MARKER

            # <Substitution u'string:${view/name}-empty-marker' (14:31)> -> __attr_name
            __token = 525
            try:
                __zt_tmp = __attrs_140240779873488
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140241087907024('string', u'${view/name}-empty-marker', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', u'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u' type="hidden" value="1"/>\n</td>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }