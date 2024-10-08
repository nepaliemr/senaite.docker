# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.spotlight/src/senaite/app/spotlight/templates/spotlight.pt'

__tokens = {482: (u'view/viewlet', 12, 37), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140182527297424 = __C2ZContextWrapper
_static_140182573187728 = {}
_static_140182386431376 = u'master'
_static_140182527296720 = __compile_zt_expr

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

            # <Static value=<_ast.Dict object at 0x7f7ecc7a8290> name=None at 7f7ecc7a8190> -> __attrs_140182386431824
            __attrs_140182386431824 = _static_140182573187728
            __previous_i18n_domain_140182386431888 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140182599750272 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ec158d590> name=None at 7f7ec158dbd0> -> __value
            __value = _static_140182386431376
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7ecc7a8290> name=None at 7f7ecc7a8190> -> __attrs_140182386434192
                __attrs_140182386434192 = _static_140182573187728
                __append(u'\n    ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7ecc7a8290> name=None at 7f7ecc7a8190> -> __attrs_140182386434576
                __attrs_140182386434576 = _static_140182573187728
                __append(u'\n      <!-- Render the viewlet -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7ecc7a8290> name=None at 7f7ecc7a8190> -> __attrs_140182386436048
                __attrs_140182386436048 = _static_140182573187728

                # <Symbol value=<DEFAULT> at 7f7ecc7a83d0> -> __default_140182386435920
                __default_140182386435920 = _DEFAULT_MARKER

                # <Value u'view/viewlet' (12:37)> -> __cache_140182386435536
                __token = 482
                try:
                    __zt_tmp = __attrs_140182386436048
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140182386435536 = _static_140182527296720('path', u'view/viewlet', econtext=econtext)(_static_140182527297424(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/viewlet' (12:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7ecc7a83d0> at 7f7ec158e690> -> __condition
                __expression = __cache_140182386435536

                # <Symbol value=<DEFAULT> at 7f7ecc7a83d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140182386435536
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n    ')
            _slots = econtext[u'__slot_content'] = _deque((__fill_content, ))

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140182386431824
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140182527296720('path', u'here/main_template/macros/master', econtext=econtext)(_static_140182527297424(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140182599750272 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140182599750272
            __i18n_domain = __previous_i18n_domain_140182386431888
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }