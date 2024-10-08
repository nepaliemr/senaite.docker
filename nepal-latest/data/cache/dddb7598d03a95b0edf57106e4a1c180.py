# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/Products.CMFPlone-5.2.14-py2.7.egg/Products/CMFPlone/browser/templates/title.pt'

__tokens = {53: (u'context/Title', 2, 20), 85: (u'title', 3, 17), 107: (u'title', 4, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907024 = __compile_zt_expr
_static_140241087907728 = __C2ZContextWrapper
_static_140240917072592 = {u'class': u'documentFirstHeading', }

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

            # <Static value=<_ast.Dict object at 0x7f8c620b8ad0> name=None at 7f8c620b8b50> -> __attrs_140240917753488
            __attrs_140240917753488 = _static_140240917072592
            __backup_title_140240917090512 = get('title', __marker)

            # <Value u'context/Title' (2:20)> -> __value
            __token = 53
            try:
                __zt_tmp = __attrs_140240917753488
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'context/Title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['title'] = __value

            # <Value u'title' (3:17)> -> __condition
            __token = 85
            try:
                __zt_tmp = __attrs_140240917753488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240917073552
                __default_140240917073552 = _DEFAULT_MARKER

                # <Value u'title' (4:15)> -> __cache_140240917071888
                __token = 107
                try:
                    __zt_tmp = __attrs_140240917753488
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240917071888 = _static_140241087907024('path', u'title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'title' (4:15)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c620b8410> -> __condition
                __expression = __cache_140240917071888

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Title or id')
                else:
                    __content = __cache_140240917071888
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</h1>')
            if (__backup_title_140240917090512 is __marker):
                del econtext['title']
            else:
                econtext['title'] = __backup_title_140240917090512
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }