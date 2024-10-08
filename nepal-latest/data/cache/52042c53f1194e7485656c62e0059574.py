# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/colophon.pt'

__tokens = {}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574270302032 = {u'class': u'text-center text-muted', }
_static_140574284374160 = {u'href': u'http://plone.org', u'title': u'This site was built using the Plone Open Source CMS/WCM.', }
_static_140574269060240 = {u'id': u'senaite-colophon', }
_static_140574270569360 = {u'class': u'list-inline', }
_static_140574269061904 = {u'class': u'container-fluid', }
_static_140574266165008 = {u'class': u'col-md-12', }
_static_140574442558096 = {}
_static_140574266165840 = {u'class': u'row', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff5f3490> name=None at 7fd9ff5f3690> -> __attrs_140574269060880
            __attrs_140574269060880 = _static_140574269060240
            __previous_i18n_domain_140574269059856 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="senaite-colophon">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff5f3b10> name=None at 7fd9ff5f36d0> -> __attrs_140574266163664
            __attrs_140574266163664 = _static_140574269061904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="container-fluid">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff330a50> name=None at 7fd9ff330f10> -> __attrs_140574266163472
            __attrs_140574266163472 = _static_140574266165840

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff330710> name=None at 7fd9ff330850> -> __attrs_140574270301712
            __attrs_140574270301712 = _static_140574266165008

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-md-12">\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff722750> name=None at 7fd9ff722e50> -> __attrs_140574270301840
            __attrs_140574270301840 = _static_140574270302032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="text-center text-muted">\n          ')

            # <Static value=<_ast.Dict object at 0x7fd9ff763b90> name=None at 7fd9ff763410> -> __attrs_140574270570128
            __attrs_140574270570128 = _static_140574270569360

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="list-inline">\n            ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270569744
            __attrs_140574270569744 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>\n              ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270567120
            __attrs_140574270567120 = _static_140574442558096

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span>')
            __stream_140574270570000 = []
            __append_140574270570000 = __stream_140574270570000.append
            __append_140574270570000(u'SENAITE is powered by')
            __msgid_140574270570000 = __re_whitespace(''.join(__stream_140574270570000)).strip()
            if u'label_powered_by':
                __append(translate(u'label_powered_by', mapping=None, default=__msgid_140574270570000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</span>\n              ')

            # <Static value=<_ast.Dict object at 0x7fda0048e090> name=None at 7fda0048e110> -> __attrs_140574284374352
            __attrs_140574284374352 = _static_140574284374160

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284376208
            __default_140574284376208 = _DEFAULT_MARKER

            # <Translate msgid=u'title_built_with_plone' node=<_ast.Str object at 0x7fda0048eb10> at 7fda0048e8d0> -> __attr_title
            __attr_title = u'This site was built using the Plone Open Source CMS/WCM.'
            __attr_title = translate(u'title_built_with_plone', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>')
            __stream_140574284376144 = []
            __append_140574284376144 = __stream_140574284376144.append
            __append_140574284376144(u'\n                Plone &amp; Python')
            __msgid_140574284376144 = __re_whitespace(''.join(__stream_140574284376144)).strip()
            if u'label_powered_by_plone':
                __append(translate(u'label_powered_by_plone', mapping=None, default=__msgid_140574284376144, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n            </li>\n          </ul>\n        </div>\n\n      </div>\n    </div>\n  </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140574269059856
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }