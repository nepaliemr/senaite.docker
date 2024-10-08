# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/publisher.pt'

__tokens = {220: (u'python:view.current_user', 6, 42), 257: (u'reporter', 6, 79), 481: (u'reporter/fullname|reporter/username', 11, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574122250640 = {u'style': u'border:none', }
_static_140574122270416 = {u'class': u'table table-sm table-condensed', }
_static_140574442558096 = {}
_static_140574122252176 = {u'class': u'label', }
_static_140574397981968 = __compile_zt_expr
_static_140574122254160 = {u'class': u'font-weight-bold', }
_static_140574121310800 = {u'class': u'w-100', }
_static_140574121311632 = {u'class': u'row section-signatures no-gutters', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121310352
            __attrs_140574121310352 = _static_140574442558096
            __previous_i18n_domain_140574121310224 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9f690bd90> name=None at 7fd9f690b2d0> -> __attrs_140574121308944
            __attrs_140574121308944 = _static_140574121311632

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row section-signatures no-gutters">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9f690ba50> name=None at 7fd9f690bad0> -> __attrs_140574121309328
            __attrs_140574121309328 = _static_140574121310800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="w-100">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9f69f5ed0> name=None at 7fd9f69f57d0> -> __attrs_140574123241296
            __attrs_140574123241296 = _static_140574122270416

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table table-sm table-condensed">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123240144
            __attrs_140574123240144 = _static_140574442558096

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n           ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123240400
            __attrs_140574123240400 = _static_140574442558096
            __backup_reporter_140574123591184 = get('reporter', __marker)

            # <Value u'python:view.current_user' (6:42)> -> __value
            __token = 220
            try:
                __zt_tmp = __attrs_140574123240400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.current_user', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['reporter'] = __value

            # <Value u'reporter' (6:79)> -> __condition
            __token = 257
            try:
                __zt_tmp = __attrs_140574123240400
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'reporter', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fd9f69f1190> name=None at 7fd9f69f1750> -> __attrs_140574122251472
                __attrs_140574122251472 = _static_140574122250640

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td style="border:none">\n              ')

                # <Static value=<_ast.Dict object at 0x7fd9f69f1f50> name=None at 7fd9f69f1510> -> __attrs_140574122253904
                __attrs_140574122253904 = _static_140574122254160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="font-weight-bold">\n                ')

                # <Static value=<_ast.Dict object at 0x7fd9f69f1790> name=None at 7fd9f69f1610> -> __attrs_140574123155984
                __attrs_140574123155984 = _static_140574122252176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="label">')
                __stream_140574122253264 = []
                __append_140574122253264 = __stream_140574122253264.append
                __append_140574122253264(u'Published By')
                __msgid_140574122253264 = __re_whitespace(''.join(__stream_140574122253264)).strip()
                if __msgid_140574122253264:
                    __append(translate(__msgid_140574122253264, mapping=None, default=__msgid_140574122253264, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n                ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123159504
                __attrs_140574123159504 = _static_140574442558096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n                  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123158672
                __attrs_140574123158672 = _static_140574442558096

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123158800
                __default_140574123158800 = _DEFAULT_MARKER

                # <Value u'reporter/fullname|reporter/username' (11:37)> -> __cache_140574123157328
                __token = 481
                try:
                    __zt_tmp = __attrs_140574123158672
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574123157328 = _static_140574397981968('path', u'reporter/fullname|reporter/username', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'reporter/fullname|reporter/username' (11:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acef90> -> __condition
                __expression = __cache_140574123157328

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140574123157328
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n                </div>\n              </div>\n            </td>\n          ')
            if (__backup_reporter_140574123591184 is __marker):
                del econtext['reporter']
            else:
                econtext['reporter'] = __backup_reporter_140574123591184
            __append(u'\n        </tr>\n      </table>\n    </div>\n  </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140574121310224
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }