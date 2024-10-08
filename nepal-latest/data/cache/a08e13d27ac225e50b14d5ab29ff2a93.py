# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/bika/lims/browser/worksheet/views/../templates/slot_header.pt'

__tokens = {79: (u'options/data', 3, 22), 268: (u'data/position', 9, 57), 396: (u'data/item_img', 13, 48), 499: (u'data/item_url|nothing', 16, 32), 552: (u'data/item_title|nothing', 17, 29), 623: (u'data/additional_item_icons', 19, 31), 691: (u'icon|nothing', 20, 39), 863: (u'data/parent_img|nothing', 28, 48), 976: (u'data/parent_url|nothing', 31, 32), 1031: (u'data/parent_title|nothing', 32, 29), 1118: (u'nocall:data/sample_type_obj', 36, 23), 1257: (u'data/sample_type_img|nothing', 40, 48), 1375: (u'data/sample_type_url|nothing', 43, 32), 1435: (u'data/sample_type_title|nothing', 44, 29), 1527: (u'nocall:data/sample_point_obj', 48, 23), 1668: (u'data/sample_point_img|nothing', 52, 48), 1787: (u'data/sample_point_url|nothing', 55, 32), 1848: (u'data/sample_point_title|nothing', 56, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168037591184 = {u'class': u'img', }
_static_140168037562128 = {u'href': u'', }
_static_140168037635472 = {u'href': u'', }
_static_140168037629584 = {u'class': u'img', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168037638928 = {u'href': u'', }
_static_140168257770128 = {}
_static_140168037566032 = {u'href': u'', }
_static_140168037651536 = {u'class': u'table  table-sm table-borderless slot-header-table', }
_static_140168037641040 = {u'class': u'img', }
_static_140168037619600 = {u'class': u'slot-header', }
_static_140168037627600 = {u'class': u'badge badge-secondary', }
_static_140168037565136 = {u'class': u'img', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6a175790> name=None at 7f7b6a1753d0> -> __attrs_140168026346128
            __attrs_140168026346128 = _static_140168037619600
            __backup_data_140168037621008 = get('data', __marker)

            # <Value u'options/data' (3:22)> -> __value
            __token = 79
            try:
                __zt_tmp = __attrs_140168026346128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'options/data', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['data'] = __value
            __previous_i18n_domain_140168037651216 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="slot-header">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17d450> name=None at 7f7b6a17ded0> -> __attrs_140168037652944
            __attrs_140168037652944 = _static_140168037651536

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table  table-sm table-borderless slot-header-table">\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037651472
            __attrs_140168037651472 = _static_140168257770128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037651344
            __attrs_140168037651344 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n        <!-- Position -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a1776d0> name=None at 7f7b6a177f90> -> __attrs_140168037628176
            __attrs_140168037628176 = _static_140168037627600

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="badge badge-secondary">')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037627344
            __default_140168037627344 = _DEFAULT_MARKER

            # <Value u'data/position' (9:57)> -> __cache_140168037626448
            __token = 268
            try:
                __zt_tmp = __attrs_140168037628176
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037626448 = _static_140168208991440('path', u'data/position', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'data/position' (9:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a177350> -> __condition
            __expression = __cache_140168037626448

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140168037626448
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</span>\n      </td>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037628880
            __attrs_140168037628880 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n        <!-- Object Type Icon -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a177e90> name=None at 7f7b6a177e50> -> __attrs_140168037628752
            __attrs_140168037628752 = _static_140168037629584

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037627088
            __default_140168037627088 = _DEFAULT_MARKER

            # <Value u'data/item_img' (13:48)> -> __cache_140168037628432
            __token = 396
            try:
                __zt_tmp = __attrs_140168037628752
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037628432 = _static_140168208991440('path', u'data/item_img', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'data/item_img' (13:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a1771d0> -> __condition
            __expression = __cache_140168037628432

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img class="img"/>')
            else:
                __content = __cache_140168037628432
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n        <!-- Object Title Link -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a179590> name=None at 7f7b6a179ed0> -> __attrs_140168037635344
            __attrs_140168037635344 = _static_140168037635472

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037634448
            __default_140168037634448 = _DEFAULT_MARKER

            # <Substitution u'data/item_url|nothing' (16:32)> -> __attr_href
            __token = 499
            try:
                __zt_tmp = __attrs_140168037635344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('path', u'data/item_url|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037637072
            __attrs_140168037637072 = _static_140168257770128

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037636880
            __default_140168037636880 = _DEFAULT_MARKER

            # <Value u'data/item_title|nothing' (17:29)> -> __cache_140168037636048
            __token = 552
            try:
                __zt_tmp = __attrs_140168037637072
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037636048 = _static_140168208991440('path', u'data/item_title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'data/item_title|nothing' (17:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a179350> -> __condition
            __expression = __cache_140168037636048

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            else:
                __content = __cache_140168037636048
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n        </a>\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037635728
            __attrs_140168037635728 = _static_140168257770128
            __backup_icon_140168037652496 = get('icon', __marker)

            # <Value u'data/additional_item_icons' (19:31)> -> __iterator
            __token = 623
            try:
                __zt_tmp = __attrs_140168037635728
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140168208991440('path', u'data/additional_item_icons', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            (__iterator, ____index_140168037637456, ) = getitem('repeat')(u'icon', __iterator)
            econtext['icon'] = None
            for __item in __iterator:
                econtext['icon'] = __item

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037637776
                __attrs_140168037637776 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037637968
                __default_140168037637968 = _DEFAULT_MARKER

                # <Value u'icon|nothing' (20:39)> -> __cache_140168037634192
                __token = 691
                try:
                    __zt_tmp = __attrs_140168037637776
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037634192 = _static_140168208991440('path', u'icon|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'icon|nothing' (20:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a179f90> -> __condition
                __expression = __cache_140168037634192

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168037634192
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </span>')
                ____index_140168037637456 -= 1
                if (____index_140168037637456 > 0):
                    __append('\n        ')
            if (__backup_icon_140168037652496 is __marker):
                del econtext['icon']
            else:
                econtext['icon'] = __backup_icon_140168037652496
            __append(u'\n      </td>\n    </tr>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037629008
            __attrs_140168037629008 = _static_140168257770128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037638608
            __attrs_140168037638608 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td></td>\n      ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037641936
            __attrs_140168037641936 = _static_140168257770128

            # <td ... (0:0)
            # --------------------------------------------------------
            __append(u'<td>\n        <!-- Parent Type Icon -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17ab50> name=None at 7f7b6a17a610> -> __attrs_140168037641680
            __attrs_140168037641680 = _static_140168037641040

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037640080
            __default_140168037640080 = _DEFAULT_MARKER

            # <Value u'data/parent_img|nothing' (28:48)> -> __cache_140168037640592
            __token = 863
            try:
                __zt_tmp = __attrs_140168037641680
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037640592 = _static_140168208991440('path', u'data/parent_img|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'data/parent_img|nothing' (28:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a17a450> -> __condition
            __expression = __cache_140168037640592

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img class="img"/>')
            else:
                __content = __cache_140168037640592
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n        <!-- Parent Title Link -->\n        ')

            # <Static value=<_ast.Dict object at 0x7f7b6a17a310> name=None at 7f7b6a17a490> -> __attrs_140168037592464
            __attrs_140168037592464 = _static_140168037638928

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037590672
            __default_140168037590672 = _DEFAULT_MARKER

            # <Substitution u'data/parent_url|nothing' (31:32)> -> __attr_href
            __token = 976
            try:
                __zt_tmp = __attrs_140168037592464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140168208991440('path', u'data/parent_url|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>\n          ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037590544
            __attrs_140168037590544 = _static_140168257770128

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037592912
            __default_140168037592912 = _DEFAULT_MARKER

            # <Value u'data/parent_title|nothing' (32:29)> -> __cache_140168037590608
            __token = 1031
            try:
                __zt_tmp = __attrs_140168037590544
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140168037590608 = _static_140168208991440('path', u'data/parent_title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

            # <BinOp left=<Value u'data/parent_title|nothing' (32:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a16e5d0> -> __condition
            __expression = __cache_140168037590608

            # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span/>')
            else:
                __content = __cache_140168037590608
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n        </a>\n      </td>\n    </tr>\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037592336
            __attrs_140168037592336 = _static_140168257770128

            # <Value u'nocall:data/sample_type_obj' (36:23)> -> __condition
            __token = 1118
            try:
                __zt_tmp = __attrs_140168037592336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('nocall', u'data/sample_type_obj', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037589264
                __attrs_140168037589264 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td></td>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037592784
                __attrs_140168037592784 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n        <!-- Sample Type Icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a16e890> name=None at 7f7b6a16e190> -> __attrs_140168037563664
                __attrs_140168037563664 = _static_140168037591184

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037562192
                __default_140168037562192 = _DEFAULT_MARKER

                # <Value u'data/sample_type_img|nothing' (40:48)> -> __cache_140168037560912
                __token = 1257
                try:
                    __zt_tmp = __attrs_140168037563664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037560912 = _static_140168208991440('path', u'data/sample_type_img|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'data/sample_type_img|nothing' (40:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a1673d0> -> __condition
                __expression = __cache_140168037560912

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img class="img"/>')
                else:
                    __content = __cache_140168037560912
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        <!-- Parent Title Link -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a167710> name=None at 7f7b6a167c50> -> __attrs_140168037560976
                __attrs_140168037560976 = _static_140168037562128

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037563280
                __default_140168037563280 = _DEFAULT_MARKER

                # <Substitution u'data/sample_type_url|nothing' (43:32)> -> __attr_href
                __token = 1375
                try:
                    __zt_tmp = __attrs_140168037560976
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('path', u'data/sample_type_url|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037561616
                __attrs_140168037561616 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037562832
                __default_140168037562832 = _DEFAULT_MARKER

                # <Value u'data/sample_type_title|nothing' (44:29)> -> __cache_140168037561232
                __token = 1435
                try:
                    __zt_tmp = __attrs_140168037561616
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037561232 = _static_140168208991440('path', u'data/sample_type_title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'data/sample_type_title|nothing' (44:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a1675d0> -> __condition
                __expression = __cache_140168037561232

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168037561232
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </a>\n      </td>\n    </tr>')
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037561872
            __attrs_140168037561872 = _static_140168257770128

            # <Value u'nocall:data/sample_point_obj' (48:23)> -> __condition
            __token = 1527
            try:
                __zt_tmp = __attrs_140168037561872
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('nocall', u'data/sample_point_obj', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037566928
                __attrs_140168037566928 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td></td>\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037566544
                __attrs_140168037566544 = _static_140168257770128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append(u'<td>\n        <!-- Sample Point Icon -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1682d0> name=None at 7f7b6a168310> -> __attrs_140168037567312
                __attrs_140168037567312 = _static_140168037565136

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037567440
                __default_140168037567440 = _DEFAULT_MARKER

                # <Value u'data/sample_point_img|nothing' (52:48)> -> __cache_140168037567824
                __token = 1668
                try:
                    __zt_tmp = __attrs_140168037567312
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037567824 = _static_140168208991440('path', u'data/sample_point_img|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'data/sample_point_img|nothing' (52:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a168f50> -> __condition
                __expression = __cache_140168037567824

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img class="img"/>')
                else:
                    __content = __cache_140168037567824
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        <!-- Parent Title Link -->\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a168650> name=None at 7f7b6a168990> -> __attrs_140168037498640
                __attrs_140168037498640 = _static_140168037566032

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037564624
                __default_140168037564624 = _DEFAULT_MARKER

                # <Substitution u'data/sample_point_url|nothing' (55:32)> -> __attr_href
                __token = 1787
                try:
                    __zt_tmp = __attrs_140168037498640
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140168208991440('path', u'data/sample_point_url|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037497808
                __attrs_140168037497808 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037496976
                __default_140168037496976 = _DEFAULT_MARKER

                # <Value u'data/sample_point_title|nothing' (56:29)> -> __cache_140168037496272
                __token = 1848
                try:
                    __zt_tmp = __attrs_140168037497808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037496272 = _static_140168208991440('path', u'data/sample_point_title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'data/sample_point_title|nothing' (56:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a157390> -> __condition
                __expression = __cache_140168037496272

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168037496272
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </a>\n      </td>\n    </tr>')
            __append(u'\n  </table>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140168037651216
            if (__backup_data_140168037621008 is __marker):
                del econtext['data']
            else:
                econtext['data'] = __backup_data_140168037621008
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }