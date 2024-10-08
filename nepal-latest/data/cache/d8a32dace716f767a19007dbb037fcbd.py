# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.dexterity-2.6.11-py2.7.egg/plone/app/dexterity/browser/default_page_warning.pt'

__tokens = {182: (u'context/@@plone_context_state/is_default_page|nothing', 5, 19), 616: (u'string:${context/aq_inner/aq_parent/absolute_url}/edit', 15, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140240781707792 = {u'id': u'dialogTitle', }
_static_140241133802128 = {}
_static_140240781708624 = {u'href': u'', }
_static_140240801245264 = {u'aria-labelledby': u'dialogTitle', u'role': u'alertdialog', u'class': u'portalMessage info', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240801245520
            __attrs_140240801245520 = _static_140241133802128
            __previous_i18n_domain_140240801245776 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8c5b242850> name=None at 7f8c5b242550> -> __attrs_140240781707152
            __attrs_140240781707152 = _static_140240801245264

            # <Value u'context/@@plone_context_state/is_default_page|nothing' (5:19)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_140240781707152
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'context/@@plone_context_state/is_default_page|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portalMessage info" role="alertdialog" aria-labelledby="dialogTitle">\n  ')

                # <Static value=<_ast.Dict object at 0x7f8c59fa0a10> name=None at 7f8c59fa05d0> -> __attrs_140240781708816
                __attrs_140240781708816 = _static_140240781707792

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append(u'<strong id="dialogTitle">')
                __stream_140240781709008 = []
                __append_140240781709008 = __stream_140240781709008.append
                __append_140240781709008(u'\n      Info\n  ')
                __msgid_140240781709008 = __re_whitespace(''.join(__stream_140240781709008)).strip()
                if __msgid_140240781709008:
                    __append(translate(__msgid_140240781709008, mapping=None, default=__msgid_140240781709008, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</strong>\n  ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240781706960
                __attrs_140240781706960 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')
                __stream_140240606029056_go_here = ''
                __stream_140240781705936 = []
                __append_140240781705936 = __stream_140240781705936.append
                __append_140240781705936(u'\n      You are editing the default view of a container. If you wanted to edit the container itself,\n     ')
                __stream_140240606029056_go_here = []
                __append_140240606029056_go_here = __stream_140240606029056_go_here.append

                # <Static value=<_ast.Dict object at 0x7f8c59fa0d50> name=None at 7f8c59fa0150> -> __attrs_140240762917840
                __attrs_140240762917840 = _static_140240781708624

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_140240606029056_go_here(u'<a')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240748634896
                __default_140240748634896 = _DEFAULT_MARKER

                # <Substitution u'string:${context/aq_inner/aq_parent/absolute_url}/edit' (15:29)> -> __attr_href
                __token = 616
                try:
                    __zt_tmp = __attrs_140240762917840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140241087907024('string', u'${context/aq_inner/aq_parent/absolute_url}/edit', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_140240606029056_go_here((u' href="%s"' % __attr_href))
                __append_140240606029056_go_here(u'>')
                __stream_140240781709072 = []
                __append_140240781709072 = __stream_140240781709072.append
                __append_140240781709072(u'go here')
                __msgid_140240781709072 = __re_whitespace(''.join(__stream_140240781709072)).strip()
                if u'label_edit_default_view_container_go_here':
                    __append_140240606029056_go_here(translate(u'label_edit_default_view_container_go_here', mapping=None, default=__msgid_140240781709072, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append_140240606029056_go_here(u'</a>')
                __append_140240781705936(u'${go_here}')
                __stream_140240606029056_go_here = ''.join(__stream_140240606029056_go_here)
                __append_140240781705936(u'.\n  ')
                __msgid_140240781705936 = __re_whitespace(''.join(__stream_140240781705936)).strip()
                if u'label_edit_default_view_container':
                    __append(translate(u'label_edit_default_view_container', mapping={u'go_here': __stream_140240606029056_go_here, }, default=__msgid_140240781705936, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n</div>')
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140240801245776
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }