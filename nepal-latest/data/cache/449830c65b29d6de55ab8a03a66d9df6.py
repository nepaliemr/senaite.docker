# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.app.listing/src/senaite/app/listing/templates/contents_table_view.pt'

__tokens = {37: (u'context/@@plone_portal_state/portal', 2, 17), 95: (u' python:view.folderitems(', 3, 21), 140: (u"d python:filter(lambda i: i.get('selected'), folderitem", 4, 17), 214: (u'ns python:view.colu', 5, 15), 256: (u'eys python:columns.ke', 6, 18), 399: (u'column_keys', 11, 28), 442: (u"python:columns[key]['title']", 12, 29), 558: (u'selected', 17, 27), 597: (u'column_keys', 18, 28), 643: (u"python:key not in item['replace']", 19, 32), 710: (u'python:item[key]', 20, 31), 799: (u"python:key in item['replace']", 22, 40), 872: (u"python:item['replace'][key]", 23, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140240603792784 = {u'class': u'table table-bordered table-striped table-sm', }
_static_140241087907728 = __C2ZContextWrapper
_static_140241087907024 = __compile_zt_expr
_static_140241133802128 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240786546256
            __attrs_140240786546256 = _static_140241133802128
            __backup_portal_140240762345552 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (2:17)> -> __value
            __token = 37
            try:
                __zt_tmp = __attrs_140240786546256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_folderitems_140240786545232 = get('folderitems', __marker)

            # <Value u'python:view.folderitems()' (3:21)> -> __value
            __token = 95
            try:
                __zt_tmp = __attrs_140240786546256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.folderitems()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['folderitems'] = __value
            __backup_selected_140240786544592 = get('selected', __marker)

            # <Value u"python:filter(lambda i: i.get('selected'), folderitems)" (4:17)> -> __value
            __token = 140
            try:
                __zt_tmp = __attrs_140240786546256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"filter(lambda i: i.get('selected'), folderitems)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['selected'] = __value
            __backup_columns_140240786546512 = get('columns', __marker)

            # <Value u'python:view.columns' (5:15)> -> __value
            __token = 214
            try:
                __zt_tmp = __attrs_140240786546256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'view.columns', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['columns'] = __value
            __backup_column_keys_140240786546640 = get('column_keys', __marker)

            # <Value u'python:columns.keys()' (6:18)> -> __value
            __token = 256
            try:
                __zt_tmp = __attrs_140240786546256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u'columns.keys()', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['column_keys'] = __value
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c4f5f4590> name=None at 7f8c5a43db10> -> __attrs_140240603793104
            __attrs_140240603793104 = _static_140240603792784

            # <table ... (0:0)
            # --------------------------------------------------------
            __append(u'<table class="table table-bordered table-striped table-sm">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240811637200
            __attrs_140240811637200 = _static_140241133802128

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append(u'<thead>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792834512
            __attrs_140240792834512 = _static_140241133802128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append(u'<tr>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792837392
            __attrs_140240792837392 = _static_140241133802128
            __backup_key_140240792835792 = get('key', __marker)

            # <Value u'column_keys' (11:28)> -> __iterator
            __token = 399
            try:
                __zt_tmp = __attrs_140240792837392
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'column_keys', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240792836496, ) = getitem('repeat')(u'key', __iterator)
            econtext['key'] = None
            for __item in __iterator:
                econtext['key'] = __item

                # <th ... (0:0)
                # --------------------------------------------------------
                __append(u'<th>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792837584
                __attrs_140240792837584 = _static_140241133802128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240792837328
                __default_140240792837328 = _DEFAULT_MARKER

                # <Value u"python:columns[key]['title']" (12:29)> -> __cache_140240792835984
                __token = 442
                try:
                    __zt_tmp = __attrs_140240792837584
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240792835984 = _static_140241087907024('python', u"columns[key]['title']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:columns[key]['title']" (12:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5aa3dad0> -> __condition
                __expression = __cache_140240792835984

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240792835984
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</span>\n        </th>')
                ____index_140240792836496 -= 1
                if (____index_140240792836496 > 0):
                    __append('\n        ')
            if (__backup_key_140240792835792 is __marker):
                del econtext['key']
            else:
                econtext['key'] = __backup_key_140240792835792
            __append(u'\n      </tr>\n    </thead>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792836560
            __attrs_140240792836560 = _static_140241133802128

            # <tbody ... (0:0)
            # --------------------------------------------------------
            __append(u'<tbody>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240793252112
            __attrs_140240793252112 = _static_140241133802128
            __backup_item_140240603794576 = get('item', __marker)

            # <Value u'selected' (17:27)> -> __iterator
            __token = 558
            try:
                __zt_tmp = __attrs_140240793252112
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140241087907024('path', u'selected', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            (__iterator, ____index_140240793254352, ) = getitem('repeat')(u'item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append(u'<tr>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240793252176
                __attrs_140240793252176 = _static_140241133802128
                __backup_key_140240792834640 = get('key', __marker)

                # <Value u'column_keys' (18:28)> -> __iterator
                __token = 597
                try:
                    __zt_tmp = __attrs_140240793252176
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140241087907024('path', u'column_keys', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                (__iterator, ____index_140240793254096, ) = getitem('repeat')(u'key', __iterator)
                econtext['key'] = None
                for __item in __iterator:
                    econtext['key'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<td>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240793253776
                    __attrs_140240793253776 = _static_140241133802128

                    # <Value u"python:key not in item['replace']" (19:32)> -> __condition
                    __token = 643
                    try:
                        __zt_tmp = __attrs_140240793253776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u"key not in item['replace']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240793254928
                        __attrs_140240793254928 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240793253392
                        __default_140240793253392 = _DEFAULT_MARKER

                        # <Value u'python:item[key]' (20:31)> -> __cache_140240793255824
                        __token = 710
                        try:
                            __zt_tmp = __attrs_140240793254928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240793255824 = _static_140241087907024('python', u'item[key]', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:item[key]' (20:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5aaa3d90> -> __condition
                        __expression = __cache_140240793255824

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240793255824
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n          ')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240793253712
                    __attrs_140240793253712 = _static_140241133802128

                    # <Value u"python:key in item['replace']" (22:40)> -> __condition
                    __token = 799
                    try:
                        __zt_tmp = __attrs_140240793253712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u"key in item['replace']", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240792832848
                        __attrs_140240792832848 = _static_140241133802128

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240792832144
                        __default_140240792832144 = _DEFAULT_MARKER

                        # <Value u"python:item['replace'][key]" (23:41)> -> __cache_140240792830736
                        __token = 872
                        try:
                            __zt_tmp = __attrs_140240792832848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240792830736 = _static_140241087907024('python', u"item['replace'][key]", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:item['replace'][key]" (23:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5aa3c350> -> __condition
                        __expression = __cache_140240792830736

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240792830736
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n          ')
                    __append(u'\n        </td>')
                    ____index_140240793254096 -= 1
                    if (____index_140240793254096 > 0):
                        __append('\n        ')
                if (__backup_key_140240792834640 is __marker):
                    del econtext['key']
                else:
                    econtext['key'] = __backup_key_140240792834640
                __append(u'\n      </tr>')
                ____index_140240793254352 -= 1
                if (____index_140240793254352 > 0):
                    __append('\n      ')
            if (__backup_item_140240603794576 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140240603794576
            __append(u'\n    </tbody>\n  </table>\n\n')
            if (__backup_column_keys_140240786546640 is __marker):
                del econtext['column_keys']
            else:
                econtext['column_keys'] = __backup_column_keys_140240786546640
            if (__backup_columns_140240786546512 is __marker):
                del econtext['columns']
            else:
                econtext['columns'] = __backup_columns_140240786546512
            if (__backup_selected_140240786544592 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_140240786544592
            if (__backup_folderitems_140240786545232 is __marker):
                del econtext['folderitems']
            else:
                econtext['folderitems'] = __backup_folderitems_140240786545232
            if (__backup_portal_140240762345552 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140240762345552
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }