# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/viewlets/templates/detached_partition_viewlet.pt'

__tokens = {46: (u'python: view.context.getDetachedFrom()', 2, 25), 106: (u'python: primary', 3, 20), 620: (u'python:primary.absolute_url()', 16, 32), 675: (u'python:primary.getId()', 17, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047122640 = {u'class': u'visualClear', }
_static_140168026280848 = {u'class': u'title', }
_static_140168037619024 = {u'id': u'portal-alert', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047616528 = {u'href': u'python:primary.absolute_url()', }
_static_140168257770128 = {}
_static_140168046983376 = {u'aria-label': u'Close', u'data-dismiss': u'alert', u'type': u'button', u'class': u'close', }
_static_140168046985040 = {u'aria-hidden': u'true', }
_static_140168026318416 = {u'class': u'portlet-alert-item alert alert-info alert-dismissible', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047123216
            __attrs_140168047123216 = _static_140168257770128
            __backup_primary_140168082037904 = get('primary', __marker)

            # <Value u'python: view.context.getDetachedFrom()' (2:25)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140168047123216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u' view.context.getDetachedFrom()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['primary'] = __value

            # <Value u'python: primary' (3:20)> -> __condition
            __token = 106
            try:
                __zt_tmp = __attrs_140168047123216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u' primary', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047122704 = __i18n_domain
                __i18n_domain = u'senaite.core'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa858d0> name=None at 7f7b6aa85810> -> __attrs_140168047123728
                __attrs_140168047123728 = _static_140168047122640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"></div>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6a175550> name=None at 7f7b6a175f50> -> __attrs_140168037620432
                __attrs_140168037620432 = _static_140168037619024

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-alert">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b696ae650> name=None at 7f7b696ae550> -> __attrs_140168026349264
                __attrs_140168026349264 = _static_140168026318416

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portlet-alert-item alert alert-info alert-dismissible">\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa638d0> name=None at 7f7b6a1497d0> -> __attrs_140168046981904
                __attrs_140168046981904 = _static_140168046983376

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa63f50> name=None at 7f7b6aa63790> -> __attrs_140168046981520
                __attrs_140168046981520 = _static_140168046985040

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span aria-hidden="true">&times;</span>\n      </button>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047158672
                __attrs_140168047158672 = _static_140168257770128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong>')
                __stream_140168037437520 = []
                __append_140168037437520 = __stream_140168037437520.append
                __append_140168037437520(u'Info')
                __msgid_140168037437520 = __re_whitespace(''.join(__stream_140168037437520)).strip()
                if __msgid_140168037437520:
                    __append(translate(__msgid_140168037437520, mapping=None, default=__msgid_140168037437520, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696a5390> name=None at 7f7b696a54d0> -> __attrs_140168047619728
                __attrs_140168047619728 = _static_140168026280848

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="title">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047618512
                __attrs_140168047618512 = _static_140168257770128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140168047616272 = []
                __append_140168047616272 = __stream_140168047616272.append
                __append_140168047616272(u'This is a detached partition from Sample ')
                __msgid_140168047616272 = __re_whitespace(''.join(__stream_140168047616272)).strip()
                if __msgid_140168047616272:
                    __append(translate(__msgid_140168047616272, mapping=None, default=__msgid_140168047616272, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aafe210> name=None at 7f7b6aafe750> -> __attrs_140168047616976
                __attrs_140168047616976 = _static_140168047616528

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047618832
                __default_140168047618832 = _DEFAULT_MARKER

                # <Substitution u'python:primary.absolute_url()' (16:32)> -> __attr_href
                __token = 620
                try:
                    __zt_tmp = __attrs_140168047616976
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('python', u'primary.absolute_url()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047617168
                __default_140168047617168 = _DEFAULT_MARKER

                # <Value u'python:primary.getId()' (17:24)> -> __cache_140168047617744
                __token = 675
                try:
                    __zt_tmp = __attrs_140168047616976
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047617744 = _static_140168208991440('python', u'primary.getId()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:primary.getId()' (17:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aafe0d0> -> __condition
                __expression = __cache_140168047617744

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168047617744
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</a>\n      </p>\n    </div>\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140168047122704
            if (__backup_primary_140168082037904 is __marker):
                del econtext['primary']
            else:
                econtext['primary'] = __backup_primary_140168082037904
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }