# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/remarks.pt'

__tokens = {26: (u'python:view.collection', 1, 26), 79: (u" python:options.get('report_options', {}", 2, 29), 148: (u"s python:bool(report_options.get('show_remarks', False", 3, 26), 225: (u'python:show_remarks', 4, 18), 312: (u'collection', 7, 27), 402: (u'python:model.getRemarks()', 9, 29), 453: (u'remarks', 10, 24), 557: (u'model/getId', 12, 58), 612: (u'remarks', 13, 35), 671: (u'record/id', 14, 49), 752: (u'record/user_id', 15, 68), 822: (u'record/user_id', 16, 53), 897: (u'record/user_name', 17, 57), 970: (u'record/created_ulocalized', 18, 53), 1098: (u'record/html_content', 21, 40)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574122225232 = {u'class': u'row section-remarks no-gutters', }
_static_140574122257040 = {u'class': u'record-username', }
_static_140574121810064 = {u'class': u'record', u'id': u'record/id', }
_static_140574123234256 = {u'class': u'remarks_history', }
_static_140574121807120 = {u'class': u'record-content', }
_static_140574121804304 = {u'class': u'record-date', }
_static_140574122819920 = {u'class': u'record-header border-bottom', }
_static_140574122257808 = {u'class': u'record-user', }
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123238864
            __attrs_140574123238864 = _static_140574442558096
            __backup_collection_140574123235856 = get('collection', __marker)

            # <Value u'python:view.collection' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574123238864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['collection'] = __value
            __backup_report_options_140574122301968 = get('report_options', __marker)

            # <Value u"python:options.get('report_options', {})" (2:29)> -> __value
            __token = 79
            try:
                __zt_tmp = __attrs_140574123238864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"options.get('report_options', {})", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['report_options'] = __value
            __backup_show_remarks_140574123198736 = get('show_remarks', __marker)

            # <Value u"python:bool(report_options.get('show_remarks', False))" (3:26)> -> __value
            __token = 148
            try:
                __zt_tmp = __attrs_140574123238864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u"bool(report_options.get('show_remarks', False))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['show_remarks'] = __value

            # <Value u'python:show_remarks' (4:18)> -> __condition
            __token = 225
            try:
                __zt_tmp = __attrs_140574123238864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'show_remarks', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574122222928 = __i18n_domain
                __i18n_domain = u'senaite.impress'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122224720
                __attrs_140574122224720 = _static_140574442558096
                __backup_model_140574123789776 = get('model', __marker)

                # <Value u'collection' (7:27)> -> __iterator
                __token = 312
                try:
                    __zt_tmp = __attrs_140574122224720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574122222096, ) = getitem('repeat')(u'model', __iterator)
                econtext['model'] = None
                for __item in __iterator:
                    econtext['model'] = __item
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fd9f69eae50> name=None at 7fd9f69ea4d0> -> __attrs_140574122224272
                    __attrs_140574122224272 = _static_140574122225232
                    __backup_remarks_140574123138640 = get('remarks', __marker)

                    # <Value u'python:model.getRemarks()' (9:29)> -> __value
                    __token = 402
                    try:
                        __zt_tmp = __attrs_140574122224272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u'model.getRemarks()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['remarks'] = __value

                    # <Value u'remarks' (10:24)> -> __condition
                    __token = 453
                    try:
                        __zt_tmp = __attrs_140574122224272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'remarks', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="row section-remarks no-gutters">\n      ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ae13d0> name=None at 7fd9f6ae1b10> -> __attrs_140574122267728
                        __attrs_140574122267728 = _static_140574123234256

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="remarks_history">\n        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121809872
                        __attrs_140574121809872 = _static_140574442558096

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h2>')
                        __stream_140574123138128 = []
                        __append_140574123138128 = __stream_140574123138128.append
                        __append_140574123138128(u'Remarks for ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808336
                        __attrs_140574121808336 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121808016
                        __default_140574121808016 = _DEFAULT_MARKER

                        # <Value u'model/getId' (12:58)> -> __cache_140574121809744
                        __token = 557
                        try:
                            __zt_tmp = __attrs_140574121808336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574121809744 = _static_140574397981968('path', u'model/getId', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'model/getId' (12:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6985d10> -> __condition
                        __expression = __cache_140574121809744

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140574123138128(u'<span/>')
                        else:
                            __content = __cache_140574121809744
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140574123138128(__content)
                        __msgid_140574123138128 = __re_whitespace(''.join(__stream_140574123138128)).strip()
                        if __msgid_140574123138128:
                            __append(translate(__msgid_140574123138128, mapping=None, default=__msgid_140574123138128, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</h2>\n        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808144
                        __attrs_140574121808144 = _static_140574442558096
                        __backup_record_140574123053840 = get('record', __marker)

                        # <Value u'remarks' (13:35)> -> __iterator
                        __token = 612
                        try:
                            __zt_tmp = __attrs_140574121808144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('path', u'remarks', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574121811728, ) = getitem('repeat')(u'record', __iterator)
                        econtext['record'] = None
                        for __item in __iterator:
                            econtext['record'] = __item
                            __append(u'\n          ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6985890> name=None at 7fd9f6985ad0> -> __attrs_140574122820368
                            __attrs_140574122820368 = _static_140574121810064

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="record"')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121809808
                            __default_140574121809808 = _DEFAULT_MARKER

                            # <Substitution u'record/id' (14:49)> -> __attr_id
                            __token = 671
                            try:
                                __zt_tmp = __attrs_140574122820368
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140574397981968('path', u'record/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))
                            __append(u'>\n            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6a7c150> name=None at 7fd9f6a7c210> -> __attrs_140574122257424
                            __attrs_140574122257424 = _static_140574122819920

                            # <Value u'record/user_id' (15:68)> -> __condition
                            __token = 752
                            try:
                                __zt_tmp = __attrs_140574122257424
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'record/user_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="record-header border-bottom">\n              ')

                                # <Static value=<_ast.Dict object at 0x7fd9f69f2d90> name=None at 7fd9f69f2c50> -> __attrs_140574122256784
                                __attrs_140574122256784 = _static_140574122257808

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="record-user">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122255888
                                __default_140574122255888 = _DEFAULT_MARKER

                                # <Value u'record/user_id' (16:53)> -> __cache_140574122257744
                                __token = 822
                                try:
                                    __zt_tmp = __attrs_140574122256784
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574122257744 = _static_140574397981968('path', u'record/user_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'record/user_id' (16:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f2390> -> __condition
                                __expression = __cache_140574122257744

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574122257744
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n              ')

                                # <Static value=<_ast.Dict object at 0x7fd9f69f2a90> name=None at 7fd9f69f2710> -> __attrs_140574123303376
                                __attrs_140574123303376 = _static_140574122257040

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="record-username">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122256592
                                __default_140574122256592 = _DEFAULT_MARKER

                                # <Value u'record/user_name' (17:57)> -> __cache_140574122256656
                                __token = 897
                                try:
                                    __zt_tmp = __attrs_140574123303376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574122256656 = _static_140574397981968('path', u'record/user_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'record/user_name' (17:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f2690> -> __condition
                                __expression = __cache_140574122256656

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574122256656
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n              ')

                                # <Static value=<_ast.Dict object at 0x7fd9f6984210> name=None at 7fd9f6af2d10> -> __attrs_140574121805584
                                __attrs_140574121805584 = _static_140574121804304

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="record-date">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123306384
                                __default_140574123306384 = _DEFAULT_MARKER

                                # <Value u'record/created_ulocalized' (18:53)> -> __cache_140574123306512
                                __token = 970
                                try:
                                    __zt_tmp = __attrs_140574121805584
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574123306512 = _static_140574397981968('path', u'record/created_ulocalized', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'record/created_ulocalized' (18:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6af2050> -> __condition
                                __expression = __cache_140574123306512

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574123306512
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n            </div>')
                            __append(u'\n            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6984d10> name=None at 7fd9f6984a50> -> __attrs_140574123230672
                            __attrs_140574123230672 = _static_140574121807120

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="record-content">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121806160
                            __default_140574121806160 = _DEFAULT_MARKER

                            # <Value u'record/html_content' (21:40)> -> __cache_140574122255632
                            __token = 1098
                            try:
                                __zt_tmp = __attrs_140574123230672
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574122255632 = _static_140574397981968('path', u'record/html_content', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'record/html_content' (21:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6984b50> -> __condition
                            __expression = __cache_140574122255632

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574122255632
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n          </div>\n        ')
                            ____index_140574121811728 -= 1
                            if (____index_140574121811728 > 0):
                                __append('')
                        if (__backup_record_140574123053840 is __marker):
                            del econtext['record']
                        else:
                            econtext['record'] = __backup_record_140574123053840
                        __append(u'\n      </div>\n    </div>')
                    if (__backup_remarks_140574123138640 is __marker):
                        del econtext['remarks']
                    else:
                        econtext['remarks'] = __backup_remarks_140574123138640
                    __append(u'\n  ')
                    ____index_140574122222096 -= 1
                    if (____index_140574122222096 > 0):
                        __append('')
                if (__backup_model_140574123789776 is __marker):
                    del econtext['model']
                else:
                    econtext['model'] = __backup_model_140574123789776
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140574122222928
            if (__backup_show_remarks_140574123198736 is __marker):
                del econtext['show_remarks']
            else:
                econtext['show_remarks'] = __backup_show_remarks_140574123198736
            if (__backup_report_options_140574122301968 is __marker):
                del econtext['report_options']
            else:
                econtext['report_options'] = __backup_report_options_140574122301968
            if (__backup_collection_140574123235856 is __marker):
                del econtext['collection']
            else:
                econtext['collection'] = __backup_collection_140574123235856
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }