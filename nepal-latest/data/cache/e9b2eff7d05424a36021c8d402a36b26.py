# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/browser/viewlets/../static/resources.pt'

__tokens = {28: (u'string:${view/site_url}/++plone++senaite.core.static/modules/jquery/jquery.min.js', 1, 28), 148: (u'string:${view/site_url}/++plone++senaite.core.static/modules/popperjs/popper.min.js', 1, 148), 270: (u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap/js/bootstrap.min.js', 1, 270), 399: (u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-confirmation2/bootstrap-confirmation.min.js', 1, 399), 552: (u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-select/js/bootstrap-select.min.js', 1, 552), 695: (u'string:${view/site_url}/++plone++senaite.core.static/modules/react/react.production.min.js', 1, 695), 824: (u'string:${view/site_url}/++plone++senaite.core.static/modules/react-dom/react-dom.production.min.js', 1, 824), 986: (u'string:${view/site_url}/++plone++senaite.impress.static/modules/fontawesome-free/css/all.min.css', 1, 986), 1113: (u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-barcode-2.2.0.min.js', 1, 1113), 1243: (u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-qrcode-0.17.0.min.js', 1, 1243), 1373: (u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/d3.js', 1, 1373), 1481: (u'string:${view/site_url}/++plone++senaite.core.static/js/bika.lims.graphics.range.js', 1, 1481), 1628: (u'string:${view/site_url}/++plone++senaite.impress.static/css/bootstrap.min.css', 1, 1628), 1761: (u'string:${view/site_url}/++plone++senaite.impress.static/css/bootstrap-print.css', 1, 1761), 1896: (u'string:${view/site_url}/++plone++senaite.impress.static/css/print.css', 1, 1896), 1996: (u'string:${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.js', 1, 1996), 2143: (u'string:${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.css', 1, 2143)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574279892880 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-confirmation2/bootstrap-confirmation.min.js', }
_static_140574255110416 = {u'href': u'#', u'rel': u'stylesheet', }
_static_140574255109712 = {u'href': u'#', u'rel': u'stylesheet', }
_static_140574268407952 = {u'href': u'#', u'rel': u'stylesheet', }
_static_140574270170576 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/jquery/jquery.min.js', }
_static_140574254005392 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-select/js/bootstrap-select.min.js', }
_static_140574282112272 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/d3.js', }
_static_140574267289168 = {u'href': u'#', u'rel': u'stylesheet', }
_static_140574284364176 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap/js/bootstrap.min.js', }
_static_140574267467664 = {u'src': u'string:${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.js', }
_static_140574269060048 = {u'href': u'#', u'rel': u'stylesheet', }
_static_140574284378064 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/js/bika.lims.graphics.range.js', }
_static_140574397981968 = __compile_zt_expr
_static_140574268019472 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/react-dom/react-dom.production.min.js', }
_static_140574267380112 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-barcode-2.2.0.min.js', }
_static_140574267989520 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/react/react.production.min.js', }
_static_140574236969552 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-qrcode-0.17.0.min.js', }
_static_140574257244368 = {u'src': u'string:${view/site_url}/++plone++senaite.core.static/modules/popperjs/popper.min.js', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff7025d0> name=None at 7fd9ff702d50> -> __attrs_140574438673872
            __attrs_140574438673872 = _static_140574270170576

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255214864
            __default_140574255214864 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/jquery/jquery.min.js' (1:28)> -> __attr_src
            __token = 28
            try:
                __zt_tmp = __attrs_140574438673872
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/jquery/jquery.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9feaae8d0> name=None at 7fd9feaae410> -> __attrs_140574267907024
            __attrs_140574267907024 = _static_140574257244368

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257175056
            __default_140574257175056 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/popperjs/popper.min.js' (1:148)> -> __attr_src
            __token = 148
            try:
                __zt_tmp = __attrs_140574267907024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/popperjs/popper.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fda0048b990> name=None at 7fd9ff45e3d0> -> __attrs_140574257195152
            __attrs_140574257195152 = _static_140574284364176

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266102736
            __default_140574266102736 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap/js/bootstrap.min.js' (1:270)> -> __attr_src
            __token = 270
            try:
                __zt_tmp = __attrs_140574257195152
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/bootstrap/js/bootstrap.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fda00047f90> name=None at 7fda00047b50> -> __attrs_140574254005072
            __attrs_140574254005072 = _static_140574279892880

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267482064
            __default_140574267482064 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-confirmation2/bootstrap-confirmation.min.js' (1:399)> -> __attr_src
            __token = 399
            try:
                __zt_tmp = __attrs_140574254005072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/bootstrap-confirmation2/bootstrap-confirmation.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9fe797c90> name=None at 7fd9fe797250> -> __attrs_140574275651536
            __attrs_140574275651536 = _static_140574254005392

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574275651408
            __default_140574275651408 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/bootstrap-select/js/bootstrap-select.min.js' (1:552)> -> __attr_src
            __token = 552
            try:
                __zt_tmp = __attrs_140574275651536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/bootstrap-select/js/bootstrap-select.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9ff4ede10> name=None at 7fd9ffc3c290> -> __attrs_140574268515664
            __attrs_140574268515664 = _static_140574267989520

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267986384
            __default_140574267986384 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/react/react.production.min.js' (1:695)> -> __attr_src
            __token = 695
            try:
                __zt_tmp = __attrs_140574268515664
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/react/react.production.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9ff4f5310> name=None at 7fd9f7575fd0> -> __attrs_140574268020112
            __attrs_140574268020112 = _static_140574268019472

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268020240
            __default_140574268020240 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/modules/react-dom/react-dom.production.min.js' (1:824)> -> __attr_src
            __token = 824
            try:
                __zt_tmp = __attrs_140574268020112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/modules/react-dom/react-dom.production.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9ff554090> name=None at 7fd9fd769290> -> __attrs_140574267380368
            __attrs_140574267380368 = _static_140574268407952

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267488720
            __default_140574267488720 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.impress.static/modules/fontawesome-free/css/all.min.css' (1:986)> -> __attr_href
            __token = 986
            try:
                __zt_tmp = __attrs_140574267380368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.impress.static/modules/fontawesome-free/css/all.min.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')

            # <Static value=<_ast.Dict object at 0x7fd9ff459190> name=None at 7fd9ff459e90> -> __attrs_140574237087440
            __attrs_140574237087440 = _static_140574267380112

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267383760
            __default_140574267383760 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-barcode-2.2.0.min.js' (1:1113)> -> __attr_src
            __token = 1113
            try:
                __zt_tmp = __attrs_140574237087440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-barcode-2.2.0.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9fd758a50> name=None at 7fd9fd763910> -> __attrs_140574268453968
            __attrs_140574268453968 = _static_140574236969552

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574236984528
            __default_140574236984528 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-qrcode-0.17.0.min.js' (1:1243)> -> __attr_src
            __token = 1243
            try:
                __zt_tmp = __attrs_140574268453968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/thirdparty/jquery-qrcode-0.17.0.min.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fda00265d10> name=None at 7fd9ff475c50> -> __attrs_140574133651728
            __attrs_140574133651728 = _static_140574282112272

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267431824
            __default_140574267431824 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/thirdparty/d3.js' (1:1373)> -> __attr_src
            __token = 1373
            try:
                __zt_tmp = __attrs_140574133651728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/thirdparty/d3.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fda0048efd0> name=None at 7fda0048e510> -> __attrs_140574284377488
            __attrs_140574284377488 = _static_140574284378064

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284375632
            __default_140574284375632 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.core.static/js/bika.lims.graphics.range.js' (1:1481)> -> __attr_src
            __token = 1481
            try:
                __zt_tmp = __attrs_140574284377488
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.core.static/js/bika.lims.graphics.range.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9fe8a5650> name=None at 7fd9fe8a5fd0> -> __attrs_140574255108688
            __attrs_140574255108688 = _static_140574255109712

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574255111568
            __default_140574255111568 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.impress.static/css/bootstrap.min.css' (1:1628)> -> __attr_href
            __token = 1628
            try:
                __zt_tmp = __attrs_140574255108688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.impress.static/css/bootstrap.min.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')

            # <Static value=<_ast.Dict object at 0x7fd9fe8a5910> name=None at 7fd9fe8a5290> -> __attrs_140574267288912
            __attrs_140574267288912 = _static_140574255110416

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268586576
            __default_140574268586576 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.impress.static/css/bootstrap-print.css' (1:1761)> -> __attr_href
            __token = 1761
            try:
                __zt_tmp = __attrs_140574267288912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.impress.static/css/bootstrap-print.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')

            # <Static value=<_ast.Dict object at 0x7fd9ff442e50> name=None at 7fd9ff4429d0> -> __attrs_140574267289360
            __attrs_140574267289360 = _static_140574267289168

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267288976
            __default_140574267288976 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}/++plone++senaite.impress.static/css/print.css' (1:1896)> -> __attr_href
            __token = 1896
            try:
                __zt_tmp = __attrs_140574267289360
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}/++plone++senaite.impress.static/css/print.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')

            # <Static value=<_ast.Dict object at 0x7fd9ff46e790> name=None at 7fd9ff46e190> -> __attrs_140574269063056
            __attrs_140574269063056 = _static_140574267467664

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267879952
            __default_140574267879952 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.js' (1:1996)> -> __attr_src
            __token = 1996
            try:
                __zt_tmp = __attrs_140574269063056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140574397981968('string', u'${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.js', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>')

            # <Static value=<_ast.Dict object at 0x7fd9ff5f33d0> name=None at 7fd9ff5f3a90> -> __attrs_140574133872784
            __attrs_140574133872784 = _static_140574269060048

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257312656
            __default_140574257312656 = _DEFAULT_MARKER

            # <Substitution u'string:${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.css' (1:2143)> -> __attr_href
            __token = 2143
            try:
                __zt_tmp = __attrs_140574133872784
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('string', u'${view/site_url}//++plone++senaite.impress.static/bundles/senaite.impress.css', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' rel="stylesheet"/>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }