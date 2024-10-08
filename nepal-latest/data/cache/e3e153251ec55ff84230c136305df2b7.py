# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/analysisrequest/templates/analysisrequest_view.pt'

__tokens = {550: (u'senaite_theme/icon_data/sample', 17, 38), 677: (u'context/id', 20, 56), 831: (u'python:view.is_hazardous()', 23, 26), 898: (u'senaite_theme/icon_data/hazardous', 24, 38), 1111: (u'python:view.exclude_invoice()', 28, 26), 1181: (u'senaite_theme/icon_data/invoice_exclude', 29, 38), 1384: (u'python:view.is_retest()', 33, 26), 1448: (u'senaite_theme/icon_data/retest', 34, 38), 1825: (u'provider:senaite.sampleheader', 47, 38), 2067: (u'provider:senaite.abovesamplesections', 54, 38), 2304: (u'provider:senaite.samplesections', 61, 38), 2548: (u'provider:senaite.belowsamplesections', 68, 38), 2762: (u'provider:senaite.samplefooter', 75, 38), 231: (u'here/main_template/macros/master', 5, 23), 231: (u'here/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168047838608 = {u'class': u'col-sm-12', }
_static_140168026286800 = {u'class': u'sample-icon', u'title': u'Sample', }
_static_140168026388368 = {u'class': u'row', u'id': u'above-sample-sections', }
_static_140168037591312 = {u'class': u'row', }
_static_140168047442320 = {u'class': u'hazardous-icon', u'title': u'Hazardous', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168047212752 = {u'class': u'col-sm-12', }
_static_140168026388688 = {u'class': u'row', }
_static_140168037443216 = {u'class': u'col-sm-12', }
_static_140168046891408 = {u'class': u'col-sm-12', }
_static_140168257770128 = {}
_static_140168046893520 = {u'class': u'row', u'id': u'sample-sections', }
_static_140168026337872 = u'master'
_static_140168026389904 = {u'class': u'col-sm-12', }
_static_140168046865744 = {u'class': u'retest-icon', u'title': u'Results have been withdrawn', }
_static_140168037445072 = {u'class': u'row', u'id': u'below-sample-sections', }
_static_140168026220368 = {u'class': u'exclude-from-invoice-icon', u'title': u'Exclude from invoice', }
_static_140168047441808 = {u'class': u'documentFirstHeading', }

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

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026337680
            __attrs_140168026337680 = _static_140168257770128
            __previous_i18n_domain_140168026339024 = __i18n_domain
            __i18n_domain = u'senaite.core'
            __backup_macroname_140168053734928 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b696b3250> name=None at 7f7b696b3a90> -> __value
            __value = _static_140168026337872
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026285776
                __attrs_140168026285776 = _static_140168257770128
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026285456
                __attrs_140168026285456 = _static_140168257770128

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1>\n        <!-- Sample icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b696a6ad0> name=None at 7f7b696a6ed0> -> __attrs_140168026343568
                __attrs_140168026343568 = _static_140168026286800

                # <i ... (0:0)
                # --------------------------------------------------------
                __append(u'<i class="sample-icon"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026344592
                __default_140168026344592 = _DEFAULT_MARKER

                # <Translate msgid=None node=<_ast.Str object at 0x7f7b696b4050> at 7f7b696b48d0> -> __attr_title
                __attr_title = u'Sample'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026343312
                __attrs_140168026343312 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026342480
                __default_140168026342480 = _DEFAULT_MARKER

                # <Value u'senaite_theme/icon_data/sample' (17:38)> -> __cache_140168026344336
                __token = 550
                try:
                    __zt_tmp = __attrs_140168026343312
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168026344336 = _static_140168208991440('path', u'senaite_theme/icon_data/sample', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'senaite_theme/icon_data/sample' (17:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b4710> -> __condition
                __expression = __cache_140168026344336

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <svg ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<svg />')
                else:
                    __content = __cache_140168026344336
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </i>\n        <!-- Title -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad3790> name=None at 7f7b696b4810> -> __attrs_140168047441168
                __attrs_140168047441168 = _static_140168047441808

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="documentFirstHeading">')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026345424
                __default_140168026345424 = _DEFAULT_MARKER

                # <Value u'context/id' (20:56)> -> __cache_140168026343824
                __token = 677
                try:
                    __zt_tmp = __attrs_140168047441168
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168026343824 = _static_140168208991440('path', u'context/id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/id' (20:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696b4910> -> __condition
                __expression = __cache_140168026343824

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168026343824
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n        <!-- Hazardous icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aad3990> name=None at 7f7b6aad3d10> -> __attrs_140168047440272
                __attrs_140168047440272 = _static_140168047442320

                # <Value u'python:view.is_hazardous()' (23:26)> -> __condition
                __token = 831
                try:
                    __zt_tmp = __attrs_140168047440272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'view.is_hazardous()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="hazardous-icon"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047440912
                    __default_140168047440912 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f7b6aad3050> at 7f7b6aad34d0> -> __attr_title
                    __attr_title = u'Hazardous'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026218640
                    __attrs_140168026218640 = _static_140168257770128

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026220688
                    __default_140168026220688 = _DEFAULT_MARKER

                    # <Value u'senaite_theme/icon_data/hazardous' (24:38)> -> __cache_140168047442064
                    __token = 898
                    try:
                        __zt_tmp = __attrs_140168026218640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168047442064 = _static_140168208991440('path', u'senaite_theme/icon_data/hazardous', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'senaite_theme/icon_data/hazardous' (24:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aad3e10> -> __condition
                    __expression = __cache_140168047442064

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <svg ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<svg />')
                    else:
                        __content = __cache_140168047442064
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n        </i>')
                __append(u'\n        <!-- Exclude Invoice Icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b69696750> name=None at 7f7b69696150> -> __attrs_140168026221392
                __attrs_140168026221392 = _static_140168026220368

                # <Value u'python:view.exclude_invoice()' (28:26)> -> __condition
                __token = 1111
                try:
                    __zt_tmp = __attrs_140168026221392
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'view.exclude_invoice()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="exclude-from-invoice-icon"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168026218768
                    __default_140168026218768 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f7b696960d0> at 7f7b69696290> -> __attr_title
                    __attr_title = u'Exclude from invoice'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046862672
                    __attrs_140168046862672 = _static_140168257770128

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046864208
                    __default_140168046864208 = _DEFAULT_MARKER

                    # <Value u'senaite_theme/icon_data/invoice_exclude' (29:38)> -> __cache_140168026219536
                    __token = 1181
                    try:
                        __zt_tmp = __attrs_140168046862672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168026219536 = _static_140168208991440('path', u'senaite_theme/icon_data/invoice_exclude', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'senaite_theme/icon_data/invoice_exclude' (29:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b69696610> -> __condition
                    __expression = __cache_140168026219536

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <svg ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<svg />')
                    else:
                        __content = __cache_140168026219536
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n        </i>')
                __append(u'\n        <!-- Retest Icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa46d50> name=None at 7f7b6aa46810> -> __attrs_140168037619344
                __attrs_140168037619344 = _static_140168046865744

                # <Value u'python:view.is_retest()' (33:26)> -> __condition
                __token = 1384
                try:
                    __zt_tmp = __attrs_140168037619344
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('python', u'view.is_retest()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="retest-icon"')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037620880
                    __default_140168037620880 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f7b6aa46cd0> at 7f7b6aa46f50> -> __attr_title
                    __attr_title = u'Results have been withdrawn'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037621520
                    __attrs_140168037621520 = _static_140168257770128

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037619664
                    __default_140168037619664 = _DEFAULT_MARKER

                    # <Value u'senaite_theme/icon_data/retest' (34:38)> -> __cache_140168037620624
                    __token = 1448
                    try:
                        __zt_tmp = __attrs_140168037621520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037620624 = _static_140168208991440('path', u'senaite_theme/icon_data/retest', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'senaite_theme/icon_data/retest' (34:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a175e90> -> __condition
                    __expression = __cache_140168037620624

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <svg ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<svg />')
                    else:
                        __content = __cache_140168037620624
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n        </i>')
                __append(u'\n      </h1>\n    ')
            _slots = econtext[u'__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168026285392
                __attrs_140168026285392 = _static_140168257770128
                __append(u'\n    ')
            _slots = econtext[u'__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168083035728
                __attrs_140168083035728 = _static_140168257770128
                __append(u'\n\n      <!-- Viewlet manager: sample header -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696bf8d0> name=None at 7f7b696bf0d0> -> __attrs_140168026390288
                __attrs_140168026390288 = _static_140168026388688

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b696bfd90> name=None at 7f7b696bfad0> -> __attrs_140168026386896
                __attrs_140168026386896 = _static_140168026389904

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037496848
                __attrs_140168037496848 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037498704
                __default_140168037498704 = _DEFAULT_MARKER

                # <Value u'provider:senaite.sampleheader' (47:38)> -> __cache_140168026387920
                __token = 1825
                try:
                    __zt_tmp = __attrs_140168037496848
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168026387920 = _static_140168208991440('provider', u'senaite.sampleheader', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.sampleheader' (47:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b696bfa10> -> __condition
                __expression = __cache_140168026387920

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140168026387920
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </div>\n      </div>\n\n      <!-- Viewlet manager: above sample sections -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b696bf790> name=None at 7f7b696bf810> -> __attrs_140168046894288
                __attrs_140168046894288 = _static_140168026388368

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row" id="above-sample-sections">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa4d190> name=None at 7f7b6aa4db90> -> __attrs_140168046891280
                __attrs_140168046891280 = _static_140168046891408

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168046894672
                __attrs_140168046894672 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046893584
                __default_140168046893584 = _DEFAULT_MARKER

                # <Value u'provider:senaite.abovesamplesections' (54:38)> -> __cache_140168046894928
                __token = 2067
                try:
                    __zt_tmp = __attrs_140168046894672
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168046894928 = _static_140168208991440('provider', u'senaite.abovesamplesections', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.abovesamplesections' (54:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa4d250> -> __condition
                __expression = __cache_140168046894928

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140168046894928
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </div>\n      </div>\n\n      <!-- Viewlet manager: sample sections -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa4d9d0> name=None at 7f7b6aa4d850> -> __attrs_140168037443280
                __attrs_140168037443280 = _static_140168046893520

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row" id="sample-sections">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14a690> name=None at 7f7b6a14a710> -> __attrs_140168037445328
                __attrs_140168037445328 = _static_140168037443216

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047839888
                __attrs_140168047839888 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047840720
                __default_140168047840720 = _DEFAULT_MARKER

                # <Value u'provider:senaite.samplesections' (61:38)> -> __cache_140168037643024
                __token = 2304
                try:
                    __zt_tmp = __attrs_140168047839888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037643024 = _static_140168208991440('provider', u'senaite.samplesections', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.samplesections' (61:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a17b190> -> __condition
                __expression = __cache_140168037643024

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140168037643024
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </div>\n      </div>\n\n      <!-- Viewlet manager: below sample sections -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a14add0> name=None at 7f7b6a14af10> -> __attrs_140168047839184
                __attrs_140168047839184 = _static_140168037445072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row" id="below-sample-sections">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6ab34590> name=None at 7f7b6ab34550> -> __attrs_140168037589648
                __attrs_140168037589648 = _static_140168047838608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037590352
                __attrs_140168037590352 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037589712
                __default_140168037589712 = _DEFAULT_MARKER

                # <Value u'provider:senaite.belowsamplesections' (68:38)> -> __cache_140168037592016
                __token = 2548
                try:
                    __zt_tmp = __attrs_140168037590352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037592016 = _static_140168208991440('provider', u'senaite.belowsamplesections', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.belowsamplesections' (68:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a16e590> -> __condition
                __expression = __cache_140168037592016

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140168037592016
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </div>\n      </div>\n\n      <!-- Viewlet manager: sample footer -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a16e910> name=None at 7f7b6a16e390> -> __attrs_140168047212624
                __attrs_140168047212624 = _static_140168037591312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6aa9b8d0> name=None at 7f7b6aa9b050> -> __attrs_140168047212304
                __attrs_140168047212304 = _static_140168047212752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168047213776
                __attrs_140168047213776 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168047210640
                __default_140168047210640 = _DEFAULT_MARKER

                # <Value u'provider:senaite.samplefooter' (75:38)> -> __cache_140168047210704
                __token = 2762
                try:
                    __zt_tmp = __attrs_140168047213776
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168047210704 = _static_140168208991440('provider', u'senaite.samplefooter', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'provider:senaite.samplefooter' (75:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa9b690> -> __condition
                __expression = __cache_140168047210704

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div></div>')
                else:
                    __content = __cache_140168047210704
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </div>\n      </div>\n\n    ')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'here/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140168026337680
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140168208991440('path', u'here/main_template/macros/master', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140168053734928 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140168053734928
            __i18n_domain = __previous_i18n_domain_140168026339024
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }