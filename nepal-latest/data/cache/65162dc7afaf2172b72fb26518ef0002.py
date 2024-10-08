# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/attachments.pt'

__tokens = {26: (u'view/collection', 1, 26), 63: (u' view/mode', 2, 20), 104: (u"s python:options.get('report_options', {", 3, 28), 180: (u"ow python:int(report_options.get('attachments_per_row', ", 4, 32), 272: (u'row python:attachments_per_row<1 and 1 or attachments_per', 5, 31), 402: (u'collection', 8, 27), 519: (u"python:model.get_sorted_attachments('r')", 10, 46), 620: (u'attachments', 12, 27), 679: (u'model/getId', 13, 45), 758: (u'attachments', 15, 50), 807: (u'python:len(attachments) > 1', 16, 35), 870: (u'python:range(attachments_per_row)', 17, 33), 944: (u"python:'width:{}%'.format(100/attachments_per_row)", 18, 39), 1051: (u'python:view.group_into_chunks(attachments, attachments_per_row)', 20, 32), 1245: (u'chunk', 23, 39), 1382: (u'string:${attachment/absolute_url}/AttachmentFile', 26, 41), 1637: (u'attachment/getTextTitle|model/getId', 30, 39), 1781: (u'attachment/AttachmentKeys', 33, 39), 1980: (u'attachment/AttachmentFile/filename', 37, 39)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574121832656 = {u'class': u'att_filename', }
_static_140574122310864 = {u'class': u'figure-caption pt-2', }
_static_140574442558096 = {}
_static_140574121789008 = {u'class': u'att_keys', }
_static_140574121811920 = {u'class': u'row section-attachments no-gutters mb-2', }
_static_140574123259600 = {u'class': u'table w-100', }
_static_140574122222480 = {u'style': u"python:'width:{}%'.format(100/attachments_per_row)", }
_static_140574397981968 = __compile_zt_expr
_static_140574122821904 = {u'style': u'border:none;padding-left:0;', u'class': u'align-bottom', }
_static_140574122309584 = {u'class': u'att_for', }
_static_140574122253520 = {u'class': u'figure', }
_static_140574122251984 = {u'src': u'string:${attachment/absolute_url}/AttachmentFile', u'class': u'figure-img img-fluid', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121809232
            __attrs_140574121809232 = _static_140574442558096
            __backup_collection_140574123215120 = get('collection', __marker)

            # <Value u'view/collection' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574121809232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['collection'] = __value
            __backup_model_140574122301968 = get('model', __marker)

            # <Value u'view/model' (2:20)> -> __value
            __token = 63
            try:
                __zt_tmp = __attrs_140574121809232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/model', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['model'] = __value
            __backup_report_options_140574121489424 = get('report_options', __marker)

            # <Value u"python:options.get('report_options', {})" (3:28)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_140574121809232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"options.get('report_options', {})", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['report_options'] = __value
            __backup_attachments_per_row_140574255076240 = get('attachments_per_row', __marker)

            # <Value u"python:int(report_options.get('attachments_per_row', 2))" (4:32)> -> __value
            __token = 180
            try:
                __zt_tmp = __attrs_140574121809232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"int(report_options.get('attachments_per_row', 2))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __backup_attachments_per_row_140574122820240 = get('attachments_per_row', __marker)

            # <Value u'python:attachments_per_row<1 and 1 or attachments_per_row' (5:31)> -> __value
            __token = 272
            try:
                __zt_tmp = __attrs_140574121809232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'attachments_per_row<1 and 1 or attachments_per_row', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['attachments_per_row'] = __value
            __previous_i18n_domain_140574121810704 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808720
            __attrs_140574121808720 = _static_140574442558096
            __backup_model_140574123199760 = get('model', __marker)

            # <Value u'collection' (8:27)> -> __iterator
            __token = 402
            try:
                __zt_tmp = __attrs_140574121808720
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574121810512, ) = getitem('repeat')(u'model', __iterator)
            econtext['model'] = None
            for __item in __iterator:
                econtext['model'] = __item
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9f6985fd0> name=None at 7fd9f6985a10> -> __attrs_140574121808656
                __attrs_140574121808656 = _static_140574121811920

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row section-attachments no-gutters mb-2">\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123259408
                __attrs_140574123259408 = _static_140574442558096
                __backup_attachments_140574123198928 = get('attachments', __marker)

                # <Value u"python:model.get_sorted_attachments('r')" (10:46)> -> __value
                __token = 519
                try:
                    __zt_tmp = __attrs_140574123259408
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"model.get_sorted_attachments('r')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['attachments'] = __value
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123258192
                __attrs_140574123258192 = _static_140574442558096

                # <Value u'attachments' (12:27)> -> __condition
                __token = 620
                try:
                    __zt_tmp = __attrs_140574123258192
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'attachments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h2>')
                    __stream_140574123261392 = []
                    __append_140574123261392 = __stream_140574123261392.append
                    __append_140574123261392(u'\n          Attachments for ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123258640
                    __attrs_140574123258640 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123260432
                    __default_140574123260432 = _DEFAULT_MARKER

                    # <Value u'model/getId' (13:45)> -> __cache_140574123260496
                    __token = 679
                    try:
                        __zt_tmp = __attrs_140574123258640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574123260496 = _static_140574397981968('path', u'model/getId', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'model/getId' (13:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae78d0> -> __condition
                    __expression = __cache_140574123260496

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140574123261392(u'<span/>')
                    else:
                        __content = __cache_140574123260496
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140574123261392(__content)
                    __append_140574123261392(u'\n        ')
                    __msgid_140574123261392 = __re_whitespace(''.join(__stream_140574123261392)).strip()
                    if __msgid_140574123261392:
                        __append(translate(__msgid_140574123261392, mapping=None, default=__msgid_140574123261392, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</h2>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9f6ae76d0> name=None at 7fd9f6ae7650> -> __attrs_140574122222608
                __attrs_140574122222608 = _static_140574123259600

                # <Value u'attachments' (15:50)> -> __condition
                __token = 758
                try:
                    __zt_tmp = __attrs_140574122222608
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'attachments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<table class="table w-100">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122224912
                    __attrs_140574122224912 = _static_140574442558096

                    # <Value u'python:len(attachments) > 1' (16:35)> -> __condition
                    __token = 807
                    try:
                        __zt_tmp = __attrs_140574122224912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u'len(attachments) > 1', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <colgroup ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<colgroup>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9f69ea390> name=None at 7fd9f69eaad0> -> __attrs_140574122222032
                        __attrs_140574122222032 = _static_140574122222480
                        __backup_col_140574123721552 = get('col', __marker)

                        # <Value u'python:range(attachments_per_row)' (17:33)> -> __iterator
                        __token = 870
                        try:
                            __zt_tmp = __attrs_140574122222032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('python', u'range(attachments_per_row)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574122223120, ) = getitem('repeat')(u'col', __iterator)
                        econtext['col'] = None
                        for __item in __iterator:
                            econtext['col'] = __item

                            # <col ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<col')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122223504
                            __default_140574122223504 = _DEFAULT_MARKER

                            # <Substitution u"python:'width:{}%'.format(100/attachments_per_row)" (18:39)> -> __attr_style
                            __token = 944
                            try:
                                __zt_tmp = __attrs_140574122222032
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_style = _static_140574397981968('python', u"'width:{}%'.format(100/attachments_per_row)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_style is not None):
                                __append((u' style="%s"' % __attr_style))
                            __append(u'>')
                            ____index_140574122223120 -= 1
                            if (____index_140574122223120 > 0):
                                __append('\n            ')
                        if (__backup_col_140574123721552 is __marker):
                            del econtext['col']
                        else:
                            econtext['col'] = __backup_col_140574123721552
                        __append(u'\n          </colgroup>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574407549712
                    __attrs_140574407549712 = _static_140574442558096
                    __backup_chunk_140574123234064 = get('chunk', __marker)

                    # <Value u'python:view.group_into_chunks(attachments, attachments_per_row)' (20:32)> -> __iterator
                    __token = 1051
                    try:
                        __zt_tmp = __attrs_140574407549712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('python', u'view.group_into_chunks(attachments, attachments_per_row)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574122820112, ) = getitem('repeat')(u'chunk', __iterator)
                    econtext['chunk'] = None
                    for __item in __iterator:
                        econtext['chunk'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tr>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6a7c910> name=None at 7fd9f6a7c3d0> -> __attrs_140574122251600
                        __attrs_140574122251600 = _static_140574122821904
                        __backup_attachment_140574123196816 = get('attachment', __marker)

                        # <Value u'chunk' (23:39)> -> __iterator
                        __token = 1245
                        try:
                            __zt_tmp = __attrs_140574122251600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('path', u'chunk', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574122254224, ) = getitem('repeat')(u'attachment', __iterator)
                        econtext['attachment'] = None
                        for __item in __iterator:
                            econtext['attachment'] = __item

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="align-bottom" style="border:none;padding-left:0;">\n              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69f1cd0> name=None at 7fd9f69f17d0> -> __attrs_140574122254032
                            __attrs_140574122254032 = _static_140574122253520

                            # <figure ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<figure class="figure">\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69f16d0> name=None at 7fd9f69f1390> -> __attrs_140574122309840
                            __attrs_140574122309840 = _static_140574122251984

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<img class="figure-img img-fluid"')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123215312
                            __default_140574123215312 = _DEFAULT_MARKER

                            # <Substitution u'string:${attachment/absolute_url}/AttachmentFile' (26:41)> -> __attr_src
                            __token = 1382
                            try:
                                __zt_tmp = __attrs_140574122309840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_src = _static_140574397981968('string', u'${attachment/absolute_url}/AttachmentFile', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_src is not None):
                                __append((u' src="%s"' % __attr_src))
                            __append(u'/>\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69ffcd0> name=None at 7fd9f69ff4d0> -> __attrs_140574122309776
                            __attrs_140574122309776 = _static_140574122310864

                            # <figcaption ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<figcaption class="figure-caption pt-2">\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69ff7d0> name=None at 7fd9f69ffad0> -> __attrs_140574121788880
                            __attrs_140574121788880 = _static_140574122309584

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="att_for">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121789776
                            __attrs_140574121789776 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574121790544 = []
                            __append_140574121790544 = __stream_140574121790544.append
                            __append_140574121790544(u'Attachment for')
                            __msgid_140574121790544 = __re_whitespace(''.join(__stream_140574121790544)).strip()
                            if __msgid_140574121790544:
                                __append(translate(__msgid_140574121790544, mapping=None, default=__msgid_140574121790544, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121790096
                            __attrs_140574121790096 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121788560
                            __default_140574121788560 = _DEFAULT_MARKER

                            # <Value u'attachment/getTextTitle|model/getId' (30:39)> -> __cache_140574121791056
                            __token = 1637
                            try:
                                __zt_tmp = __attrs_140574121790096
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574121791056 = _static_140574397981968('path', u'attachment/getTextTitle|model/getId', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'attachment/getTextTitle|model/getId' (30:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6980dd0> -> __condition
                            __expression = __cache_140574121791056

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574121791056
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                  </div>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6980650> name=None at 7fd9f69801d0> -> __attrs_140574121789392
                            __attrs_140574121789392 = _static_140574121789008

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="att_keys">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121832784
                            __attrs_140574121832784 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121834128
                            __default_140574121834128 = _DEFAULT_MARKER

                            # <Value u'attachment/AttachmentKeys' (33:39)> -> __cache_140574121788816
                            __token = 1781
                            try:
                                __zt_tmp = __attrs_140574121832784
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574121788816 = _static_140574397981968('path', u'attachment/AttachmentKeys', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'attachment/AttachmentKeys' (33:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69808d0> -> __condition
                            __expression = __cache_140574121788816

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574121788816
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                  </div>\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fd9f698b0d0> name=None at 7fd9f69ff950> -> __attrs_140574121836048
                            __attrs_140574121836048 = _static_140574121832656

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="att_filename">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121833808
                            __attrs_140574121833808 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574121832976 = []
                            __append_140574121832976 = __stream_140574121832976.append
                            __append_140574121832976(u'Filename:')
                            __msgid_140574121832976 = __re_whitespace(''.join(__stream_140574121832976)).strip()
                            if __msgid_140574121832976:
                                __append(translate(__msgid_140574121832976, mapping=None, default=__msgid_140574121832976, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121475664
                            __attrs_140574121475664 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123144528
                            __default_140574123144528 = _DEFAULT_MARKER

                            # <Value u'attachment/AttachmentFile/filename' (37:39)> -> __cache_140574123144656
                            __token = 1980
                            try:
                                __zt_tmp = __attrs_140574121475664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123144656 = _static_140574397981968('path', u'attachment/AttachmentFile/filename', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'attachment/AttachmentFile/filename' (37:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6acb7d0> -> __condition
                            __expression = __cache_140574123144656

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574123144656
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                  </div>\n                </figcaption>\n              </figure>\n            </td>')
                            ____index_140574122254224 -= 1
                            if (____index_140574122254224 > 0):
                                __append('\n            ')
                        if (__backup_attachment_140574123196816 is __marker):
                            del econtext['attachment']
                        else:
                            econtext['attachment'] = __backup_attachment_140574123196816
                        __append(u'\n          </tr>')
                        ____index_140574122820112 -= 1
                        if (____index_140574122820112 > 0):
                            __append('\n          ')
                    if (__backup_chunk_140574123234064 is __marker):
                        del econtext['chunk']
                    else:
                        econtext['chunk'] = __backup_chunk_140574123234064
                    __append(u'\n        </table>')
                __append(u'\n      ')
                if (__backup_attachments_140574123198928 is __marker):
                    del econtext['attachments']
                else:
                    econtext['attachments'] = __backup_attachments_140574123198928
                __append(u'\n    </div>\n  ')
                ____index_140574121810512 -= 1
                if (____index_140574121810512 > 0):
                    __append('')
            if (__backup_model_140574123199760 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140574123199760
            __append(u'\n\n')
            __i18n_domain = __previous_i18n_domain_140574121810704
            if (__backup_attachments_per_row_140574122820240 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574122820240
            if (__backup_attachments_per_row_140574255076240 is __marker):
                del econtext['attachments_per_row']
            else:
                econtext['attachments_per_row'] = __backup_attachments_per_row_140574255076240
            if (__backup_report_options_140574121489424 is __marker):
                del econtext['report_options']
            else:
                econtext['report_options'] = __backup_report_options_140574121489424
            if (__backup_model_140574122301968 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140574122301968
            if (__backup_collection_140574123215120 is __marker):
                del econtext['collection']
            else:
                econtext['collection'] = __backup_collection_140574123215120
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }