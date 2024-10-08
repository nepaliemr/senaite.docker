# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/z3cform/widgets/uidreference/display.pt'

__tokens = {223: (u'view/get_value', 7, 24), 295: (u'python:view.render_reference(uid)', 8, 32), 359: (u'python:rendered', 9, 28), 474: (u'rendered', 11, 39), 529: (u'python:not rendered', 13, 28), 600: (u'uid', 14, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240776685392 = {u'class': u'p-1 mb-1 mr-1 bg-light border rounded', }
_static_140240782654288 = {u'class': u'list-unstyled d-table-row', }
_static_140241133802128 = {}
_static_140240776685456 = {u'class': u'd-inline-block', }
_static_140240764291728 = {u'class': u'text-danger', }
_static_140240605377360 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<_ast.Dict object at 0x7f8c4f777350> name=None at 7f8c60d26790> -> __attrs_140240782652880
            __attrs_140240782652880 = _static_140240605377360
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c5a087b50> name=None at 7f8c5a087950> -> __attrs_140240748637776
            __attrs_140240748637776 = _static_140240782654288

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="list-unstyled d-table-row">\n    <!-- list all referenced UIDs -->\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c59ad6790> name=None at 7f8c59ad6e10> -> __attrs_140240776687312
            __attrs_140240776687312 = _static_140240776685456
            __backup_uid_140240803781840 = get('uid', __marker)

            # <Value u'view/get_value' (7:24)> -> __iterator
            __token = 223
            try:
                __zt_tmp = __attrs_140240776687312
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'view/get_value', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240776684432, ) = getitem('repeat')(u'uid', __iterator)
            econtext['uid'] = None
            for __item in __iterator:
                econtext['uid'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="d-inline-block">\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240776686544
                __attrs_140240776686544 = _static_140241133802128
                __backup_rendered_140240750206352 = get('rendered', __marker)

                # <Value u'python:view.render_reference(uid)' (8:32)> -> __value
                __token = 295
                try:
                    __zt_tmp = __attrs_140240776686544
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u'view.render_reference(uid)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['rendered'] = __value
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c59ad6750> name=None at 7f8c59ad64d0> -> __attrs_140240776684240
                __attrs_140240776684240 = _static_140240776685392

                # <Value u'python:rendered' (9:28)> -> __condition
                __token = 359
                try:
                    __zt_tmp = __attrs_140240776684240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'rendered', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="p-1 mb-1 mr-1 bg-light border rounded">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240764290000
                    __attrs_140240764290000 = _static_140241133802128

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764292176
                    __default_140240764292176 = _DEFAULT_MARKER

                    # <Value u'rendered' (11:39)> -> __cache_140240764290768
                    __token = 474
                    try:
                        __zt_tmp = __attrs_140240764290000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240764290768 = _static_140241087907024('path', u'rendered', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'rendered' (11:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58f04390> -> __condition
                    __expression = __cache_140240764290768

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span/>')
                    else:
                        __content = __cache_140240764290768
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n        </div>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c58f04a90> name=None at 7f8c58f045d0> -> __attrs_140240764289296
                __attrs_140240764289296 = _static_140240764291728

                # <Value u'python:not rendered' (13:28)> -> __condition
                __token = 529
                try:
                    __zt_tmp = __attrs_140240764289296
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u'not rendered', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="text-danger">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240764289552
                    __attrs_140240764289552 = _static_140241133802128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764291600
                    __default_140240764291600 = _DEFAULT_MARKER

                    # <Value u'uid' (14:29)> -> __cache_140240764289104
                    __token = 600
                    try:
                        __zt_tmp = __attrs_140240764289552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140240764289104 = _static_140241087907024('path', u'uid', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                    # <BinOp left=<Value u'uid' (14:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c58f04e10> -> __condition
                    __expression = __cache_140240764289104

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140240764289104
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n        </div>')
                __append(u'\n      ')
                if (__backup_rendered_140240750206352 is __marker):
                    del econtext['rendered']
                else:
                    econtext['rendered'] = __backup_rendered_140240750206352
                __append(u'\n    </li>')
                ____index_140240776684432 -= 1
                if (____index_140240776684432 > 0):
                    __append('\n    ')
            if (__backup_uid_140240803781840 is __marker):
                del econtext['uid']
            else:
                econtext['uid'] = __backup_uid_140240803781840
            __append(u'\n  </ul>\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }