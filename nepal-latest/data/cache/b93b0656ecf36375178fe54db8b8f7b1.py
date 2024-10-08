# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/footer.pt'

__tokens = {213: (u'view/render_footer_portlets', 8, 57), 181: (u'nothing', 8, 25), 520: (u'view/year', 12, 63)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from chameleon.tal import ErrorInfo as _ErrorInfo

_static_140574397982672 = __C2ZContextWrapper
_static_140574267907728 = {u'id': u'senaite-footer', }
_static_140574268015568 = {u'class': u'row', }
_static_140574284375824 = {u'class': u'fa fa-hashtag', }
_static_140574284438544 = {u'class': u'fa fa-code-branch', }
_static_140574268916368 = {u'href': u'https://www.senaite.com', u'target': u'_blank', }
_static_140574442558096 = {}
_static_140574266195792 = {u'class': u'fas fa-book', }
_static_140574266195408 = {u'href': u'https://github.com/senaite/senaite.lims', u'target': u'_blank', u'class': u'nav-link', u'title': u'Browse the code on GitHub', }
_static_140574284377232 = {u'href': u'https://twitter.com/senaitelims', u'target': u'_blank', u'class': u'nav-link', u'title': u'Spread the word on Twitter', }
_static_140574270359632 = {u'class': u'fas fa-globe', }
_static_140574268916752 = {u'class': u'float-right', }
_static_140574270359568 = {u'href': u'https://www.senaite.com/docs/quickstart.html', u'target': u'_blank', u'class': u'nav-link', u'title': u'Browse the Docs', }
_static_140574270569808 = {u'href': u'https://gitter.im/senaite', u'target': u'_blank', u'class': u'nav-link', u'title': u'Talk with us on Gitter', }
_static_140574268942928 = {u'class': u'fas fa-comments', }
_static_140574397981968 = __compile_zt_expr
_static_140574284443024 = {u'href': u'https://www.senaite.com', u'target': u'_blank', u'class': u'nav-link', u'title': u'Visit the Website', }
_static_140574268056016 = {u'class': u'col-md-12', }
_static_140574266170640 = {u'class': u'float-left', }
_static_140574268020688 = {u'title': u'Copyright', }
_static_140574270172624 = {u'class': u'nav nav-pills', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff4d9e90> name=None at 7fd9ff4d9090> -> __attrs_140574268018640
            __attrs_140574268018640 = _static_140574267907728
            __previous_i18n_domain_140574268014800 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer id="senaite-footer">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4f43d0> name=None at 7fd9ff4f4450> -> __attrs_140574268017680
            __attrs_140574268017680 = _static_140574268015568

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff4fe1d0> name=None at 7fd9ff4fe150> -> __attrs_140574268056720
            __attrs_140574268056720 = _static_140574268056016

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-md-12">\n      ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268058384
            __attrs_140574268058384 = _static_140574442558096

            # <hr ... (0:0)
            # --------------------------------------------------------
            __append(u'<hr/>\n      <!-- footer portlets -->\n      ')
            ____fallback_140574442882608 = len(__stream)
            try:

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266167888
                __attrs_140574266167888 = _static_140574442558096

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266168656
                __default_140574266168656 = _DEFAULT_MARKER

                # <Value u'view/render_footer_portlets' (8:57)> -> __cache_140574266170448
                __token = 213
                try:
                    __zt_tmp = __attrs_140574266167888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574266170448 = _static_140574397981968('path', u'view/render_footer_portlets', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/render_footer_portlets' (8:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff331990> -> __condition
                __expression = __cache_140574266170448

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140574266170448
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            except (Exception, ) as __exc:
                econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                if (on_error_handler is not None):
                    on_error_handler(__exc)
                del __stream[____fallback_140574442882608:]

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>')

                # <Value u'nothing' (8:25)> -> __content
                __token = 181
                try:
                    __zt_tmp = __attrs_140574268056720
                except get('NameError', NameError):
                    __zt_tmp = None

                __content = _static_140574397981968('path', u'nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
                __append(u'</div>')

            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff331d10> name=None at 7fd9ff331210> -> __attrs_140574268020880
            __attrs_140574268020880 = _static_140574266170640

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="float-left">\n        ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268019728
            __attrs_140574268019728 = _static_140574442558096
            __stream_140574255149856_senaitelims = ''
            __stream_140574255149856_copyright = ''
            __stream_140574255149856_current_year = ''
            __stream_140574268019472 = []
            __append_140574268019472 = __stream_140574268019472.append
            __append_140574268019472(u'\n          ')
            __stream_140574255149856_copyright = []
            __append_140574255149856_copyright = __stream_140574255149856_copyright.append

            # <Static value=<_ast.Dict object at 0x7fd9ff4f57d0> name=None at 7fd9ff4f5c90> -> __attrs_140574268916944
            __attrs_140574268916944 = _static_140574268020688

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_140574255149856_copyright(u'<abbr')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268917264
            __default_140574268917264 = _DEFAULT_MARKER

            # <Translate msgid=u'title_copyright' node=<_ast.Str object at 0x7fd9ff4f5810> at 7fd9ff4f5b50> -> __attr_title
            __attr_title = u'Copyright'
            __attr_title = translate(u'title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append_140574255149856_copyright((u' title="%s"' % __attr_title))
            __append_140574255149856_copyright(u'>&copy;</abbr>')
            __append_140574268019472(u'${copyright}')
            __stream_140574255149856_copyright = ''.join(__stream_140574255149856_copyright)
            __append_140574268019472(u'\n          2017-')
            __stream_140574255149856_current_year = []
            __append_140574255149856_current_year = __stream_140574255149856_current_year.append

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268916304
            __attrs_140574268916304 = _static_140574442558096

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268917392
            __default_140574268917392 = _DEFAULT_MARKER

            # <Value u'view/year' (12:63)> -> __cache_140574268918160
            __token = 520
            try:
                __zt_tmp = __attrs_140574268916304
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140574268918160 = _static_140574397981968('path', u'view/year', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/year' (12:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff5d0ad0> -> __condition
            __expression = __cache_140574268918160

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140574268918160
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140574255149856_current_year(__content)
            __append_140574268019472(u'${current_year}')
            __stream_140574255149856_current_year = ''.join(__stream_140574255149856_current_year)
            __append_140574268019472(u'\n          ')
            __stream_140574255149856_senaitelims = []
            __append_140574255149856_senaitelims = __stream_140574255149856_senaitelims.append

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268918096
            __attrs_140574268918096 = _static_140574442558096
            __append_140574255149856_senaitelims(u'\n            ')

            # <Static value=<_ast.Dict object at 0x7fd9ff5d0290> name=None at 7fd9ff5d0f90> -> __attrs_140574270172816
            __attrs_140574270172816 = _static_140574268916368

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140574255149856_senaitelims(u'<a href="https://www.senaite.com" target="_blank">')
            __stream_140574268917840 = []
            __append_140574268917840 = __stream_140574268917840.append
            __append_140574268917840(u'SENAITE LIMS')
            __msgid_140574268917840 = __re_whitespace(''.join(__stream_140574268917840)).strip()
            if u'label_senaite':
                __append_140574255149856_senaitelims(translate(u'label_senaite', mapping=None, default=__msgid_140574268917840, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append_140574255149856_senaitelims(u'</a>\n          ')
            __append_140574268019472(u'${senaitelims}')
            __stream_140574255149856_senaitelims = ''.join(__stream_140574255149856_senaitelims)
            __append_140574268019472(u'\n        ')
            __msgid_140574268019472 = __re_whitespace(''.join(__stream_140574268019472)).strip()
            if u'description_copyright':
                __append(translate(u'description_copyright', mapping={u'current_year': __stream_140574255149856_current_year, u'copyright': __stream_140574255149856_copyright, u'senaitelims': __stream_140574255149856_senaitelims, }, default=__msgid_140574268019472, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'\n      </div>\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff5d0410> name=None at 7fd9ff5d0110> -> __attrs_140574268021200
            __attrs_140574268021200 = _static_140574268916752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="float-right">\n        ')

            # <Static value=<_ast.Dict object at 0x7fd9ff702dd0> name=None at 7fd9ff702e50> -> __attrs_140574270170896
            __attrs_140574270170896 = _static_140574270172624

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul class="nav nav-pills">\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270170128
            __attrs_140574270170128 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fda0049ed90> name=None at 7fda0049e750> -> __attrs_140574284441936
            __attrs_140574284441936 = _static_140574284443024

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" href="https://www.senaite.com" title="Visit the Website" target="_blank">')

            # <Static value=<_ast.Dict object at 0x7fd9ff730850> name=None at 7fd9ff730710> -> __attrs_140574270359376
            __attrs_140574270359376 = _static_140574270359632

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-globe"></i></a></li>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270170704
            __attrs_140574270170704 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fd9ff730810> name=None at 7fd9ff730b50> -> __attrs_140574266194064
            __attrs_140574266194064 = _static_140574270359568

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" href="https://www.senaite.com/docs/quickstart.html" title="Browse the Docs" target="_blank">')

            # <Static value=<_ast.Dict object at 0x7fd9ff337f50> name=None at 7fd9ff337850> -> __attrs_140574266192400
            __attrs_140574266192400 = _static_140574266195792

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-book"></i></a></li>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266195600
            __attrs_140574266195600 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fd9ff337dd0> name=None at 7fd9ff337ed0> -> __attrs_140574284437136
            __attrs_140574284437136 = _static_140574266195408

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" href="https://github.com/senaite/senaite.lims" title="Browse the code on GitHub" target="_blank">')

            # <Static value=<_ast.Dict object at 0x7fda0049dc10> name=None at 7fda0049d8d0> -> __attrs_140574284438416
            __attrs_140574284438416 = _static_140574284438544

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fa fa-code-branch"></i></a></li>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284439376
            __attrs_140574284439376 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fda0048ec90> name=None at 7fda0048ec50> -> __attrs_140574284375120
            __attrs_140574284375120 = _static_140574284377232

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" href="https://twitter.com/senaitelims" title="Spread the word on Twitter" target="_blank">')

            # <Static value=<_ast.Dict object at 0x7fda0048e710> name=None at 7fda0048efd0> -> __attrs_140574270569296
            __attrs_140574270569296 = _static_140574284375824

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fa fa-hashtag"></i></a></li>\n          ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284438992
            __attrs_140574284438992 = _static_140574442558096

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fd9ff763d50> name=None at 7fd9ff763b90> -> __attrs_140574270567568
            __attrs_140574270567568 = _static_140574270569808

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a class="nav-link" href="https://gitter.im/senaite" title="Talk with us on Gitter" target="_blank">')

            # <Static value=<_ast.Dict object at 0x7fd9ff5d6a50> name=None at 7fd9ff5d6450> -> __attrs_140574268941520
            __attrs_140574268941520 = _static_140574268942928

            # <i ... (0:0)
            # --------------------------------------------------------
            __append(u'<i class="fas fa-comments"></i></a></li>\n        </ul>\n      </div>\n    </div>\n  </div>\n</footer>')
            __i18n_domain = __previous_i18n_domain_140574268014800
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }