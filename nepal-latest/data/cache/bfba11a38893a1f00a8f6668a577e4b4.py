# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/sample_dynamic_specs_viewlet.pt'

__tokens = {51: (u'python:view.get_dynamic_specification()', 2, 30), 112: (u'python:dynamic_spec', 3, 20), 1025: (u'python:dynamic_spec.absolute_url()', 27, 32), 1085: (u'python:dynamic_spec.Title()', 28, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168026274192 = {u'class': u'description', }
_static_140168016766160 = {u'id': u'portal-alert', }
_static_140168016767184 = {u'class': u'visualClear', }
_static_140168047124432 = {u'href': u'python:dynamic_spec.absolute_url()', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168046907280 = {u'aria-hidden': u'true', }
_static_140168047815888 = {u'class': u'portlet-alert-item alert alert-warning alert-dismissible', }
_static_140168046906256 = {u'class': u'title', }
_static_140168257770128 = {}
_static_140168047816144 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168016768272
            __attrs_140168016768272 = _static_140168257770128
            __backup_dynamic_spec_140168016770448 = get('dynamic_spec', __marker)

            # <Value u'python:view.get_dynamic_specification()' (2:30)> -> __value
            __token = 51
            try:
                __zt_tmp = __attrs_140168016768272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.get_dynamic_specification()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['dynamic_spec'] = __value

            # <Value u'python:dynamic_spec' (3:20)> -> __condition
            __token = 112
            try:
                __zt_tmp = __attrs_140168016768272
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'dynamic_spec', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168016768848 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b68d928d0> name=None at 7f7b68d92750> -> __attrs_140168016765520
                __attrs_140168016765520 = _static_140168016767184

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b68d924d0> name=None at 7f7b68d92b90> -> __attrs_140168047815120
                __attrs_140168047815120 = _static_140168016766160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab2ecd0> name=None at 7f7b6ab2e710> -> __attrs_140168047815056
                __attrs_140168047815056 = _static_140168047815888

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-warning alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab2edd0> name=None at 7f7b6ab2e810> -> __attrs_140168046906064
                __attrs_140168046906064 = _static_140168047816144

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa50f90> name=None at 7f7b6aa50dd0> -> __attrs_140168046903568
                __attrs_140168046903568 = _static_140168046907280

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa50b90> name=None at 7f7b6aa50510> -> __attrs_140168046906896
                __attrs_140168046906896 = _static_140168046906256

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026274640
                __attrs_140168026274640 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168026275536 = []
                __append_140168026275536 = __stream_140168026275536.append
                __append_140168026275536(u'\n          The specification has a Dynamic Specification assigned\n        ')
                __msgid_140168026275536 = __re_whitespace(''.join(__stream_140168026275536)).strip()
                if __msgid_140168026275536:
                    __append(translate(__msgid_140168026275536, mapping=None, default=__msgid_140168026275536, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      </p>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696a3990> name=None at 7f7b696a3550> -> __attrs_140168026275408
                __attrs_140168026275408 = _static_140168026274192

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="description">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026273872
                __attrs_140168026273872 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168026272016 = []
                __append_140168026272016 = __stream_140168026272016.append
                __append_140168026272016(u'\n          Be aware that the ranges provided in the spreadsheet file from the\n          dynamic specification might override the ranges manually defined in\n          the list below.\n        ')
                __msgid_140168026272016 = __re_whitespace(''.join(__stream_140168026272016)).strip()
                if __msgid_140168026272016:
                    __append(translate(__msgid_140168026272016, mapping=None, default=__msgid_140168026272016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026275472
                __attrs_140168026275472 = _static_140168257770128

                # <br ... (0:0)
                # --------------------------------------------------------
                __append(u'<br/>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168025871696
                __attrs_140168025871696 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168026274448 = []
                __append_140168026274448 = __stream_140168026274448.append
                __append_140168026274448(u'\n          Visit the Dynamic Specification for additional information:\n        ')
                __msgid_140168026274448 = __re_whitespace(''.join(__stream_140168026274448)).strip()
                if __msgid_140168026274448:
                    __append(translate(__msgid_140168026274448, mapping=None, default=__msgid_140168026274448, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>&nbsp;\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa85fd0> name=None at 7f7b6aa853d0> -> __attrs_140168047122320
                __attrs_140168047122320 = _static_140168047124432

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047120656
                __default_140168047120656 = _DEFAULT_MARKER

                # <Substitution u'python:dynamic_spec.absolute_url()' (27:32)> -> __attr_href
                __token = 1025
                try:
                    __zt_tmp = __attrs_140168047122320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u'dynamic_spec.absolute_url()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047121232
                __default_140168047121232 = _DEFAULT_MARKER

                # <Value u'python:dynamic_spec.Title()' (28:24)> -> __cache_140168047120528
                __token = 1085
                try:
                    __zt_tmp = __attrs_140168047122320
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047120528 = _static_140168208991440('python', u'dynamic_spec.Title()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:dynamic_spec.Title()' (28:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa858d0> -> __condition
                __expression = __cache_140168047120528

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047120528
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>\n      </p>\n    </div>\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140168016768848
            if (__backup_dynamic_spec_140168016770448 is __marker):
                del econtext['dynamic_spec']
            else:
                econtext['dynamic_spec'] = __backup_dynamic_spec_140168016770448
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }