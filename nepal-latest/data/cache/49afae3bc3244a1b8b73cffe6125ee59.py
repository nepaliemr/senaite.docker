# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/results.pt'

__tokens = {26: (u'python:view.collection', 1, 26), 82: (u' string:', 2, 32), 124: (u'l string', 3, 31), 172: (u'ms python', 4, 36), 245: (u'collection', 6, 27), 409: (u'python:view.get_analyses_by_poc(model)', 11, 41), 466: (u'analyses_by_poc', 11, 98), 581: (u'python:view.get_categories_by_poc(model)', 14, 59), 640: (u'python:view.sort_items(categories_by_poc.get(poc))', 14, 118), 1450: (u'repeat/category/start', 31, 46), 1640: (u'category/Title', 34, 49), 2608: (u'not:repeat/category/start', 52, 46), 2798: (u'category/Title', 55, 49), 3041: (u'python:view.get_analyses_by(model, poc=poc , category=category)', 62, 61), 3324: (u'analysis/Accredited', 65, 132), 3290: (u'accredited_symbol', 65, 98), 3439: (u'not:analysis/ScientificName', 67, 53), 3549: (u'analysis/title', 68, 80), 3666: (u'analysis/ScientificName', 70, 53), 3765: (u'analysis/title', 71, 73), 3899: (u'python:view.get_result_variables(analysis)', 74, 69), 3954: (u'interims', 74, 124), 4022: (u'python:results_interims.append(interims)', 75, 57), 4077: (u'python: len(results_interims)', 75, 112), 4328: (u"python:analysis and analysis.getMethodTitle() or ''", 79, 115), 4405: (u'python:view.hyphenize(method_title)', 79, 192), 4609: (u'python:model.get_formatted_result(analysis)', 82, 76), 4851: (u'python:model.get_formatted_unit(analysis)', 85, 75), 5040: (u'analysis/Uncertainty', 88, 53), 5085: (u'python:model.get_formatted_uncertainty(analysis)', 88, 98), 5194: (u"python:'(RT)' if model.is_retest(analysis) else ''", 89, 51), 5305: (u'python:model.get_formatted_specs(analysis)', 90, 51), 5553: (u'python: model.is_out_of_range(analysis)', 94, 93), 5643: (u' python: analysis.getResultsRange(', 95, 49), 5728: (u"  python: results_range.get('rangecomment", 96, 48), 5836: (u'out_of_range', 97, 61), 6073: (u'outofrange_symbol', 100, 158), 6281: (u'comment', 104, 81), 6303: (u'comment', 104, 103), 6575: (u'python:category.Comments', 113, 61), 6647: (u'category_comments', 114, 45), 6786: (u'category_comments', 116, 74), 6994: (u'results_interims', 121, 45), 7189: (u'results_interims', 124, 57), 7273: (u'repeat/interims/number', 125, 52), 7363: (u'interims', 126, 64), 7481: (u'repeat/interim/index', 128, 57), 7564: (u'repeat/interim/index', 129, 59), 7658: (u'interim/title', 130, 57), 7734: (u'interim/formatted_value', 132, 57), 7818: (u'interim/formatted_unit', 133, 57)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574123269328 = {u'class': u'font-italic', }
_static_140574122222800 = {u'class': u'w-100', }
_static_140574123183888 = {u'style': u'width: 25%', }
_static_140574123277840 = {u'class': u'text-left border-r-0 border-l-0 result', }
_static_140574122258256 = {u'colspan': u'3', }
_static_140574122261840 = {u'class': u'specs', }
_static_140574397981968 = __compile_zt_expr
_static_140574122307728 = {u'style': u'font-family:Lucida Console, Courier, monospace;', u'class': u'font-weight-light outofrange text-danger', }
_static_140574123233104 = {u'style': u'width: 10%', }
_static_140574123226896 = {u'class': u'analysis border-0', }
_static_140574122325520 = {u'class': u'text-secondary methodtitle', }
_static_140574122261136 = {u'class': u'units', }
_static_140574442558096 = {}
_static_140574121805264 = {u'class': u'specs border-r-0 border-l-0', }
_static_140574123593552 = {u'class': u'pl-2', }
_static_140574123232464 = {u'style': u'width: 15%', }
_static_140574121798800 = {u'class': u'result', }
_static_140574123225872 = {u'class': u'small border-0', }
_static_140574123226832 = {u'class': u'border-0', }
_static_140574122257872 = {u'class': u'text-danger small', }
_static_140574123182032 = {u'style': u'width: 35%;', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574123229520 = {u'style': u'width: 20%', }
_static_140574123636816 = {u'class': u'font-weight-normal', }
_static_140574121804688 = {u'class': u'outofrange border-r-0 border-l-0', }
_static_140574123558544 = {u'style': u'font-family:sans;', u'class': u'text-success', }
_static_140574123216464 = {u'class': u'analysis border-r-0 border-l-0', }
_static_140574123599248 = {u'class': u'text-center align-middle', }
_static_140574122222992 = {u'class': u'row section-results no-gutters', }
_static_140574123277776 = {u'class': u'text-left border-r-0 border-l-0 unit', }
_static_140574121801104 = {u'class': u'category_comments', }
_static_140574121796624 = {u'class': u'text-left', }
_static_140574121803728 = {u'colspan': u'3', }
_static_140574123603472 = {u'class': u'mt-2', }
_static_140574121802384 = {u'class': u'list-unstyled results_interims', }
_static_140574121799184 = {u'class': u'text-left text-muted font-italic', }
_static_140574123212880 = {u'class': u'small', }
_static_140574123184080 = {u'class': u'table border-0 table-sm table-condensed', }
_static_140574123199504 = {u'class': u'analysis', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123155984
            __attrs_140574123155984 = _static_140574442558096
            __backup_collection_140574123254480 = get('collection', __marker)

            # <Value u'python:view.collection' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574123155984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['collection'] = __value
            __backup_accredited_symbol_140574123135312 = get('accredited_symbol', __marker)

            # <Value u'string:\u2605' (2:32)> -> __value
            __token = 82
            try:
                __zt_tmp = __attrs_140574123155984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('string', u'\u2605', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['accredited_symbol'] = __value
            __backup_outofrange_symbol_140574123156816 = get('outofrange_symbol', __marker)

            # <Value u'string:\u26a0' (3:31)> -> __value
            __token = 124
            try:
                __zt_tmp = __attrs_140574123155984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('string', u'\u26a0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['outofrange_symbol'] = __value

            # <Value u'python:[]' (4:36)> -> __value
            __token = 172
            try:
                __zt_tmp = __attrs_140574123155984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'[]', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['results_interims'] = __value
            rcontext['results_interims'] = __value
            __previous_i18n_domain_140574123155920 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123155600
            __attrs_140574123155600 = _static_140574442558096
            __backup_model_140574123158992 = get('model', __marker)

            # <Value u'collection' (6:27)> -> __iterator
            __token = 245
            try:
                __zt_tmp = __attrs_140574123155600
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574123158352, ) = getitem('repeat')(u'model', __iterator)
            econtext['model'] = None
            for __item in __iterator:
                econtext['model'] = __item
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9f69ea590> name=None at 7fd9f69ea710> -> __attrs_140574122222160
                __attrs_140574122222160 = _static_140574122222992

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row section-results no-gutters">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9f69ea4d0> name=None at 7fd9f69eaed0> -> __attrs_140574122222416
                __attrs_140574122222416 = _static_140574122222800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="w-100">\n        <!-- Point of Capture -->\n        ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122224784
                __attrs_140574122224784 = _static_140574442558096
                __backup_analyses_by_poc_140574122224848 = get('analyses_by_poc', __marker)

                # <Value u'python:view.get_analyses_by_poc(model)' (11:41)> -> __value
                __token = 409
                try:
                    __zt_tmp = __attrs_140574122224784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'view.get_analyses_by_poc(model)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['analyses_by_poc'] = __value
                __backup_poc_140574122223248 = get('poc', __marker)

                # <Value u'analyses_by_poc' (11:98)> -> __iterator
                __token = 466
                try:
                    __zt_tmp = __attrs_140574122224784
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'analyses_by_poc', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574123240784, ) = getitem('repeat')(u'poc', __iterator)
                econtext['poc'] = None
                for __item in __iterator:
                    econtext['poc'] = __item
                    __append(u'\n\n          <!-- Analysis Category -->\n          ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123238288
                    __attrs_140574123238288 = _static_140574442558096
                    __backup_categories_by_poc_140574122223056 = get('categories_by_poc', __marker)

                    # <Value u'python:view.get_categories_by_poc(model)' (14:59)> -> __value
                    __token = 581
                    try:
                        __zt_tmp = __attrs_140574123238288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140574397981968('python', u'view.get_categories_by_poc(model)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    econtext['categories_by_poc'] = __value
                    __backup_category_140574123237584 = get('category', __marker)

                    # <Value u'python:view.sort_items(categories_by_poc.get(poc))' (14:118)> -> __iterator
                    __token = 640
                    try:
                        __zt_tmp = __attrs_140574123238288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('python', u'view.sort_items(categories_by_poc.get(poc))', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574123240080, ) = getitem('repeat')(u'category', __iterator)
                    econtext['category'] = None
                    for __item in __iterator:
                        econtext['category'] = __item
                        __append(u'\n\n            <!-- Analysis in POC and Category -->\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ad4fd0> name=None at 7fd9f6ae2450> -> __attrs_140574123182416
                        __attrs_140574123182416 = _static_140574123184080

                        # <table ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<table class="table border-0 table-sm table-condensed">\n              ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123180880
                        __attrs_140574123180880 = _static_140574442558096

                        # <colgroup ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<colgroup>\n                <!-- Category -->\n                ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ad47d0> name=None at 7fd9f6ad48d0> -> __attrs_140574123183376
                        __attrs_140574123183376 = _static_140574123182032

                        # <col ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<col style="width: 35%;">\n                  <!-- Result -->\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ad4f10> name=None at 7fd9f6ad4810> -> __attrs_140574123722384
                        __attrs_140574123722384 = _static_140574123183888

                        # <col ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<col style="width: 25%">\n                    <!-- Unit -->\n                    ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ae0cd0> name=None at 7fd9f6ae0890> -> __attrs_140574123231888
                        __attrs_140574123231888 = _static_140574123232464

                        # <col ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<col style="width: 15%">\n                      <!-- Range -->\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ae0150> name=None at 7fd9f6ae0490> -> __attrs_140574123232912
                        __attrs_140574123232912 = _static_140574123229520

                        # <col ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<col style="width: 20%">\n                        <!-- Out of Range -->\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6ae0f50> name=None at 7fd9f6ae0d90> -> __attrs_140574123230928
                        __attrs_140574123230928 = _static_140574123233104

                        # <col ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<col style="width: 10%">\n                        </colgroup>\n                        <!-- repeat/category/start to conditionally display the full header only for the first item -->\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123233040
                        __attrs_140574123233040 = _static_140574442558096

                        # <Value u'repeat/category/start' (31:46)> -> __condition
                        __token = 1450
                        try:
                            __zt_tmp = __attrs_140574123233040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'repeat/category/start', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <thead ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<thead>\n                          ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6adc050> name=None at 7fd9f6adc590> -> __attrs_140574123213328
                            __attrs_140574123213328 = _static_140574123212880

                            # <tr ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<tr class="small">\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6adce50> name=None at 7fd9f6adc2d0> -> __attrs_140574123213008
                            __attrs_140574123213008 = _static_140574123216464

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="analysis border-r-0 border-l-0">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123277264
                            __attrs_140574123277264 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123214416
                            __default_140574123214416 = _DEFAULT_MARKER

                            # <Value u'category/Title' (34:49)> -> __cache_140574123216528
                            __token = 1640
                            try:
                                __zt_tmp = __attrs_140574123277264
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123216528 = _static_140574397981968('path', u'category/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'category/Title' (34:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6adc510> -> __condition
                            __expression = __cache_140574123216528

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'Category')
                            else:
                                __content = __cache_140574123216528
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                            </th>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6aebe10> name=None at 7fd9f6adc950> -> __attrs_140574123276048
                            __attrs_140574123276048 = _static_140574123277840

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="text-left border-r-0 border-l-0 result">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123274512
                            __attrs_140574123274512 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574123277648 = []
                            __append_140574123277648 = __stream_140574123277648.append
                            __append_140574123277648(u'Result')
                            __msgid_140574123277648 = __re_whitespace(''.join(__stream_140574123277648)).strip()
                            if __msgid_140574123277648:
                                __append(translate(__msgid_140574123277648, mapping=None, default=__msgid_140574123277648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                            </th>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6aebdd0> name=None at 7fd9f6aeba10> -> __attrs_140574123277072
                            __attrs_140574123277072 = _static_140574123277776

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="text-left border-r-0 border-l-0 unit">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121806288
                            __attrs_140574121806288 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574123275856 = []
                            __append_140574123275856 = __stream_140574123275856.append
                            __append_140574123275856(u'Unit')
                            __msgid_140574123275856 = __re_whitespace(''.join(__stream_140574123275856)).strip()
                            if __msgid_140574123275856:
                                __append(translate(__msgid_140574123275856, mapping=None, default=__msgid_140574123275856, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                            </th>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69845d0> name=None at 7fd9f6adc1d0> -> __attrs_140574121805136
                            __attrs_140574121805136 = _static_140574121805264

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="specs border-r-0 border-l-0">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121804624
                            __attrs_140574121804624 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140574121804112 = []
                            __append_140574121804112 = __stream_140574121804112.append
                            __append_140574121804112(u'Range')
                            __msgid_140574121804112 = __re_whitespace(''.join(__stream_140574121804112)).strip()
                            if __msgid_140574121804112:
                                __append(translate(__msgid_140574121804112, mapping=None, default=__msgid_140574121804112, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                            </th>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6984390> name=None at 7fd9f6984850> -> __attrs_140574121806672
                            __attrs_140574121806672 = _static_140574121804688

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="outofrange border-r-0 border-l-0">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121807824
                            __attrs_140574121807824 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span/>\n                            </th>\n                          </tr>\n                        </thead>')
                        __append(u'\n\n                        <!-- repeat/category/not:start to display the alternative header for subsequent items -->\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121807184
                        __attrs_140574121807184 = _static_140574442558096

                        # <Value u'not:repeat/category/start' (52:46)> -> __condition
                        __token = 2608
                        try:
                            __zt_tmp = __attrs_140574121807184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('not', u'repeat/category/start', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <thead ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<thead>\n                          ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6adf310> name=None at 7fd9f6adf790> -> __attrs_140574123225936
                            __attrs_140574123225936 = _static_140574123225872

                            # <tr ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<tr class="small border-0">\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6adf710> name=None at 7fd9f6adfd90> -> __attrs_140574123227216
                            __attrs_140574123227216 = _static_140574123226896

                            # <th ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<th class="analysis border-0">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123228368
                            __attrs_140574123228368 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123226384
                            __default_140574123226384 = _DEFAULT_MARKER

                            # <Value u'category/Title' (55:49)> -> __cache_140574123228240
                            __token = 2798
                            try:
                                __zt_tmp = __attrs_140574123228368
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123228240 = _static_140574397981968('path', u'category/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'category/Title' (55:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6adf3d0> -> __condition
                            __expression = __cache_140574123228240

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'Category')
                            else:
                                __content = __cache_140574123228240
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                            </th>\n                          </tr>\n                        </thead>')
                        __append(u'\n\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fd9f6adf6d0> name=None at 7fd9f6984710> -> __attrs_140574123225488
                        __attrs_140574123225488 = _static_140574123226832

                        # <tbody ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tbody class="border-0">\n                          ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123144592
                        __attrs_140574123144592 = _static_140574442558096
                        __backup_analysis_140574123183696 = get('analysis', __marker)

                        # <Value u'python:view.get_analyses_by(model, poc=poc , category=category)' (62:61)> -> __iterator
                        __token = 3041
                        try:
                            __zt_tmp = __attrs_140574123144592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('python', u'view.get_analyses_by(model, poc=poc , category=category)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574123198480, ) = getitem('repeat')(u'analysis', __iterator)
                        econtext['analysis'] = None
                        for __item in __iterator:
                            econtext['analysis'] = __item
                            __append(u'\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123196624
                            __attrs_140574123196624 = _static_140574442558096

                            # <tr ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<tr>\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6ad8c10> name=None at 7fd9f6ad84d0> -> __attrs_140574267352272
                            __attrs_140574267352272 = _static_140574123199504

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="analysis">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6b30690> name=None at 7fd9f6b30710> -> __attrs_140574123560016
                            __attrs_140574123560016 = _static_140574123558544

                            # <Value u'analysis/Accredited' (65:132)> -> __condition
                            __token = 3324
                            try:
                                __zt_tmp = __attrs_140574123560016
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'analysis/Accredited', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="text-success" style="font-family:sans;">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123558352
                                __default_140574123558352 = _DEFAULT_MARKER

                                # <Value u'accredited_symbol' (65:98)> -> __cache_140574123558032
                                __token = 3290
                                try:
                                    __zt_tmp = __attrs_140574123560016
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574123558032 = _static_140574397981968('path', u'accredited_symbol', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'accredited_symbol' (65:98)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b301d0> -> __condition
                                __expression = __cache_140574123558032

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                                ')
                                else:
                                    __content = __cache_140574123558032
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>')
                            __append(u'\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123558224
                            __attrs_140574123558224 = _static_140574442558096

                            # <Value u'not:analysis/ScientificName' (67:53)> -> __condition
                            __token = 3439
                            try:
                                __zt_tmp = __attrs_140574123558224
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u'analysis/ScientificName', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fd9f6b43850> name=None at 7fd9f6b4e610> -> __attrs_140574123267408
                                __attrs_140574123267408 = _static_140574123636816

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="font-weight-normal">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123680976
                                __default_140574123680976 = _DEFAULT_MARKER

                                # <Value u'analysis/title' (68:80)> -> __cache_140574123559952
                                __token = 3549
                                try:
                                    __zt_tmp = __attrs_140574123267408
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574123559952 = _static_140574397981968('path', u'analysis/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'analysis/title' (68:80)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b307d0> -> __condition
                                __expression = __cache_140574123559952

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574123559952
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n                                </span>')
                            __append(u'\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123268368
                            __attrs_140574123268368 = _static_140574442558096

                            # <Value u'analysis/ScientificName' (70:53)> -> __condition
                            __token = 3666
                            try:
                                __zt_tmp = __attrs_140574123268368
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'analysis/ScientificName', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fd9f6ae9cd0> name=None at 7fd9f6ae9810> -> __attrs_140574123268752
                                __attrs_140574123268752 = _static_140574123269328

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="font-italic">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123270096
                                __default_140574123270096 = _DEFAULT_MARKER

                                # <Value u'analysis/title' (71:73)> -> __cache_140574123268880
                                __token = 3765
                                try:
                                    __zt_tmp = __attrs_140574123268752
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574123268880 = _static_140574397981968('path', u'analysis/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'analysis/title' (71:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6ae9050> -> __condition
                                __expression = __cache_140574123268880

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574123268880
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n                                </span>')
                            __append(u'\n\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123269648
                            __attrs_140574123269648 = _static_140574442558096
                            __backup_interims_140574123275344 = get('interims', __marker)

                            # <Value u'python:view.get_result_variables(analysis)' (74:69)> -> __value
                            __token = 3899
                            try:
                                __zt_tmp = __attrs_140574123269648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('python', u'view.get_result_variables(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['interims'] = __value

                            # <Value u'interims' (74:124)> -> __condition
                            __token = 3954
                            try:
                                __zt_tmp = __attrs_140574123269648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'interims', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:
                                __append(u'\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122327056
                                __attrs_140574122327056 = _static_140574442558096
                                __backup_dummy_140574123560272 = get('dummy', __marker)

                                # <Value u'python:results_interims.append(interims)' (75:57)> -> __value
                                __token = 4022
                                try:
                                    __zt_tmp = __attrs_140574122327056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140574397981968('python', u'results_interims.append(interims)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                econtext['dummy'] = __value

                                # <sup ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<sup>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122327440
                                __default_140574122327440 = _DEFAULT_MARKER

                                # <Value u'python: len(results_interims)' (75:112)> -> __cache_140574268933456
                                __token = 4077
                                try:
                                    __zt_tmp = __attrs_140574122327056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574268933456 = _static_140574397981968('python', u' len(results_interims)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'python: len(results_interims)' (75:112)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6a03290> -> __condition
                                __expression = __cache_140574268933456

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574268933456
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</sup>')
                                if (__backup_dummy_140574123560272 is __marker):
                                    del econtext['dummy']
                                else:
                                    econtext['dummy'] = __backup_dummy_140574123560272
                                __append(u'\n                                ')
                            if (__backup_interims_140574123275344 is __marker):
                                del econtext['interims']
                            else:
                                econtext['interims'] = __backup_interims_140574123275344
                            __append(u'\n\n                                <!-- Method -->\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6a03610> name=None at 7fd9f6a03250> -> __attrs_140574121797136
                            __attrs_140574121797136 = _static_140574122325520
                            __backup_method_title_140574123557520 = get('method_title', __marker)

                            # <Value u"python:analysis and analysis.getMethodTitle() or ''" (79:115)> -> __value
                            __token = 4328
                            try:
                                __zt_tmp = __attrs_140574121797136
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('python', u"analysis and analysis.getMethodTitle() or ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['method_title'] = __value

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="text-secondary methodtitle">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122326864
                            __default_140574122326864 = _DEFAULT_MARKER

                            # <Value u'python:view.hyphenize(method_title)' (79:192)> -> __cache_140574123560528
                            __token = 4405
                            try:
                                __zt_tmp = __attrs_140574121797136
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123560528 = _static_140574397981968('python', u'view.hyphenize(method_title)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:view.hyphenize(method_title)' (79:192)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6a03cd0> -> __condition
                            __expression = __cache_140574123560528

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574123560528
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>')
                            if (__backup_method_title_140574123557520 is __marker):
                                del econtext['method_title']
                            else:
                                econtext['method_title'] = __backup_method_title_140574123557520
                            __append(u'\n                              </td>\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6982410> name=None at 7fd9f6ae9c10> -> __attrs_140574121797008
                            __attrs_140574121797008 = _static_140574121796624

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="text-left">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6982c90> name=None at 7fd9f6982c50> -> __attrs_140574121797264
                            __attrs_140574121797264 = _static_140574121798800

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="result">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121796944
                            __default_140574121796944 = _DEFAULT_MARKER

                            # <Value u'python:model.get_formatted_result(analysis)' (82:76)> -> __cache_140574121798544
                            __token = 4609
                            try:
                                __zt_tmp = __attrs_140574121797264
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574121798544 = _static_140574397981968('python', u'model.get_formatted_result(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:model.get_formatted_result(analysis)' (82:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6982ad0> -> __condition
                            __expression = __cache_140574121798544

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'23')
                            else:
                                __content = __cache_140574121798544
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                              </td>\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6982e10> name=None at 7fd9f6982a10> -> __attrs_140574121799248
                            __attrs_140574121799248 = _static_140574121799184

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="text-left text-muted font-italic">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69f3a90> name=None at 7fd9f69f3850> -> __attrs_140574122258576
                            __attrs_140574122258576 = _static_140574122261136

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="units">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122259152
                            __default_140574122259152 = _DEFAULT_MARKER

                            # <Value u'python:model.get_formatted_unit(analysis)' (85:75)> -> __cache_140574122261392
                            __token = 4851
                            try:
                                __zt_tmp = __attrs_140574122258576
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574122261392 = _static_140574397981968('python', u'model.get_formatted_unit(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:model.get_formatted_unit(analysis)' (85:75)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f3150> -> __condition
                            __expression = __cache_140574122261392

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574122261392
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                              </td>\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69f3d50> name=None at 7fd9f69f3c50> -> __attrs_140574122259536
                            __attrs_140574122259536 = _static_140574122261840

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="specs">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122259984
                            __attrs_140574122259984 = _static_140574442558096

                            # <Value u'analysis/Uncertainty' (88:53)> -> __condition
                            __token = 5040
                            try:
                                __zt_tmp = __attrs_140574122259984
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'analysis/Uncertainty', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122258960
                                __default_140574122258960 = _DEFAULT_MARKER

                                # <Value u'python:model.get_formatted_uncertainty(analysis)' (88:98)> -> __cache_140574122259344
                                __token = 5085
                                try:
                                    __zt_tmp = __attrs_140574122259984
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574122259344 = _static_140574397981968('python', u'model.get_formatted_uncertainty(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'python:model.get_formatted_uncertainty(analysis)' (88:98)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f3250> -> __condition
                                __expression = __cache_140574122259344

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574122259344
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>')
                            __append(u'\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123598672
                            __attrs_140574123598672 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123600848
                            __default_140574123600848 = _DEFAULT_MARKER

                            # <Value u"python:'(RT)' if model.is_retest(analysis) else ''" (89:51)> -> __cache_140574123600208
                            __token = 5194
                            try:
                                __zt_tmp = __attrs_140574123598672
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123600208 = _static_140574397981968('python', u"'(RT)' if model.is_retest(analysis) else ''", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u"python:'(RT)' if model.is_retest(analysis) else ''" (89:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b3a410> -> __condition
                            __expression = __cache_140574123600208

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574123600208
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123598160
                            __attrs_140574123598160 = _static_140574442558096

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123599632
                            __default_140574123599632 = _DEFAULT_MARKER

                            # <Value u'python:model.get_formatted_specs(analysis)' (90:51)> -> __cache_140574123598032
                            __token = 5305
                            try:
                                __zt_tmp = __attrs_140574123598160
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574123598032 = _static_140574397981968('python', u'model.get_formatted_specs(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:model.get_formatted_specs(analysis)' (90:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b3a550> -> __condition
                            __expression = __cache_140574123598032

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'50 - 60')
                            else:
                                __content = __cache_140574123598032
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                              </td>\n\n                              <!-- Out of range column -->\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6b3a590> name=None at 7fd9f6b3a850> -> __attrs_140574123601744
                            __attrs_140574123601744 = _static_140574123599248
                            __backup_out_of_range_140574123216848 = get('out_of_range', __marker)

                            # <Value u'python: model.is_out_of_range(analysis)' (94:93)> -> __value
                            __token = 5553
                            try:
                                __zt_tmp = __attrs_140574123601744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('python', u' model.is_out_of_range(analysis)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['out_of_range'] = __value
                            __backup_results_range_140574123215696 = get('results_range', __marker)

                            # <Value u'python: analysis.getResultsRange()' (95:49)> -> __value
                            __token = 5643
                            try:
                                __zt_tmp = __attrs_140574123601744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('python', u' analysis.getResultsRange()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['results_range'] = __value
                            __backup_comment_140574123214864 = get('comment', __marker)

                            # <Value u"python: results_range.get('rangecomment')" (96:48)> -> __value
                            __token = 5728
                            try:
                                __zt_tmp = __attrs_140574123601744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140574397981968('python', u" results_range.get('rangecomment')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            econtext['comment'] = __value

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td class="text-center align-middle">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122311312
                            __attrs_140574122311312 = _static_140574442558096

                            # <Value u'out_of_range' (97:61)> -> __condition
                            __token = 5836
                            try:
                                __zt_tmp = __attrs_140574122311312
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'out_of_range', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:
                                __append(u'\n\n                                  <!-- Out of range symbol -->\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fd9f69ff090> name=None at 7fd9f69ffa10> -> __attrs_140574122256272
                                __attrs_140574122256272 = _static_140574122307728

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span class="font-weight-light outofrange text-danger" style="font-family:Lucida Console, Courier, monospace;">')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122307856
                                __default_140574122307856 = _DEFAULT_MARKER

                                # <Value u'outofrange_symbol' (100:158)> -> __cache_140574122310032
                                __token = 6073
                                try:
                                    __zt_tmp = __attrs_140574122256272
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574122310032 = _static_140574397981968('path', u'outofrange_symbol', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'outofrange_symbol' (100:158)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69ff6d0> -> __condition
                                __expression = __cache_140574122310032

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                                  ')
                                else:
                                    __content = __cache_140574122310032
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n\n                                  <!-- Out-of-range comment -->\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fd9f69f2dd0> name=None at 7fd9f69f2d10> -> __attrs_140574122254800
                                __attrs_140574122254800 = _static_140574122257872

                                # <Value u'comment' (104:81)> -> __condition
                                __token = 6281
                                try:
                                    __zt_tmp = __attrs_140574122254800
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140574397981968('path', u'comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span class="text-danger small">')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122255120
                                    __default_140574122255120 = _DEFAULT_MARKER

                                    # <Value u'comment' (104:103)> -> __cache_140574122257104
                                    __token = 6303
                                    try:
                                        __zt_tmp = __attrs_140574122254800
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140574122257104 = _static_140574397981968('path', u'comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'comment' (104:103)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f2a10> -> __condition
                                    __expression = __cache_140574122257104

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140574122257104
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>')
                                __append(u'\n\n                                ')
                            __append(u'\n\n                              </td>')
                            if (__backup_comment_140574123214864 is __marker):
                                del econtext['comment']
                            else:
                                econtext['comment'] = __backup_comment_140574123214864
                            if (__backup_results_range_140574123215696 is __marker):
                                del econtext['results_range']
                            else:
                                econtext['results_range'] = __backup_results_range_140574123215696
                            if (__backup_out_of_range_140574123216848 is __marker):
                                del econtext['out_of_range']
                            else:
                                econtext['out_of_range'] = __backup_out_of_range_140574123216848
                            __append(u'\n                            </tr>\n                          ')
                            ____index_140574123198480 -= 1
                            if (____index_140574123198480 > 0):
                                __append('')
                        if (__backup_analysis_140574123183696 is __marker):
                            del econtext['analysis']
                        else:
                            econtext['analysis'] = __backup_analysis_140574123183696
                        __append(u'\n                        </tbody>\n\n                        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123198608
                        __attrs_140574123198608 = _static_140574442558096
                        __backup_category_comments_140574123239824 = get('category_comments', __marker)

                        # <Value u'python:category.Comments' (113:61)> -> __value
                        __token = 6575
                        try:
                            __zt_tmp = __attrs_140574123198608
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'category.Comments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['category_comments'] = __value

                        # <tfoot ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tfoot>\n                          ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122257552
                        __attrs_140574122257552 = _static_140574442558096

                        # <Value u'category_comments' (114:45)> -> __condition
                        __token = 6647
                        try:
                            __zt_tmp = __attrs_140574122257552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'category_comments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <tr ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<tr>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f69f2f50> name=None at 7fd9f69f2b10> -> __attrs_140574122255696
                            __attrs_140574122255696 = _static_140574122258256

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td colspan="3">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6983590> name=None at 7fd9f6983610> -> __attrs_140574121802320
                            __attrs_140574121802320 = _static_140574121801104

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="category_comments">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121799888
                            __default_140574121799888 = _DEFAULT_MARKER

                            # <Value u'category_comments' (116:74)> -> __cache_140574121800080
                            __token = 6786
                            try:
                                __zt_tmp = __attrs_140574121802320
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574121800080 = _static_140574397981968('path', u'category_comments', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'category_comments' (116:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6983c90> -> __condition
                            __expression = __cache_140574121800080

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                      Category Comments\n                              ')
                            else:
                                __content = __cache_140574121800080
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                            </td>\n                          </tr>')
                        __append(u'\n                          ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121802448
                        __attrs_140574121802448 = _static_140574442558096

                        # <Value u'results_interims' (121:45)> -> __condition
                        __token = 6994
                        try:
                            __zt_tmp = __attrs_140574121802448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('path', u'results_interims', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <tr ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<tr>\n                            ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6983fd0> name=None at 7fd9f6983ed0> -> __attrs_140574121802064
                            __attrs_140574121802064 = _static_140574121803728

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<td colspan="3">\n                              ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6983a90> name=None at 7fd9f6983cd0> -> __attrs_140574123603792
                            __attrs_140574123603792 = _static_140574121802384

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<ul class="list-unstyled results_interims">\n                                ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6b3b610> name=None at 7fd9f6b3b5d0> -> __attrs_140574123603984
                            __attrs_140574123603984 = _static_140574123603472
                            __backup_interims_140574122311440 = get('interims', __marker)

                            # <Value u'results_interims' (124:57)> -> __iterator
                            __token = 7189
                            try:
                                __zt_tmp = __attrs_140574123603984
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140574397981968('path', u'results_interims', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            (__iterator, ____index_140574123604240, ) = getitem('repeat')(u'interims', __iterator)
                            econtext['interims'] = None
                            for __item in __iterator:
                                econtext['interims'] = __item

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<li class="mt-2">\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123589712
                                __attrs_140574123589712 = _static_140574442558096

                                # <sup ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<sup>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123605072
                                __default_140574123605072 = _DEFAULT_MARKER

                                # <Value u'repeat/interims/number' (125:52)> -> __cache_140574123602384
                                __token = 7273
                                try:
                                    __zt_tmp = __attrs_140574123589712
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574123602384 = _static_140574397981968('path', u'repeat/interims/number', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'repeat/interims/number' (125:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6b3b4d0> -> __condition
                                __expression = __cache_140574123602384

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140574123602384
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</sup>\n                                  ')

                                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123590096
                                __attrs_140574123590096 = _static_140574442558096
                                __backup_interim_140574122257360 = get('interim', __marker)

                                # <Value u'interims' (126:64)> -> __iterator
                                __token = 7363
                                try:
                                    __zt_tmp = __attrs_140574123590096
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140574397981968('path', u'interims', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                (__iterator, ____index_140574123589776, ) = getitem('repeat')(u'interim', __iterator)
                                econtext['interim'] = None
                                for __item in __iterator:
                                    econtext['interim'] = __item
                                    __append(u'\n                                    ')

                                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123591696
                                    __attrs_140574123591696 = _static_140574442558096
                                    __append(u'\n                                      ')

                                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574123592848
                                    __attrs_140574123592848 = _static_140574442558096

                                    # <Value u'repeat/interim/index' (128:57)> -> __condition
                                    __token = 7481
                                    try:
                                        __zt_tmp = __attrs_140574123592848
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140574397981968('path', u'repeat/interim/index', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    if __condition:

                                        # <br ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<br/>')
                                    __append(u'\n                                      ')

                                    # <Static value=<_ast.Dict object at 0x7fd9f6b38f50> name=None at 7fd9f6b38b90> -> __attrs_140574123592720
                                    __attrs_140574123592720 = _static_140574123593552

                                    # <Value u'repeat/interim/index' (129:59)> -> __condition
                                    __token = 7564
                                    try:
                                        __zt_tmp = __attrs_140574123592720
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140574397981968('path', u'repeat/interim/index', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<span class="pl-2"/>')
                                    __append(u'\n                                      ')

                                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808528
                                    __attrs_140574121808528 = _static_140574442558096

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121808016
                                    __default_140574121808016 = _DEFAULT_MARKER

                                    # <Value u'interim/title' (130:57)> -> __cache_140574121811088
                                    __token = 7658
                                    try:
                                        __zt_tmp = __attrs_140574121808528
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140574121811088 = _static_140574397981968('path', u'interim/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'interim/title' (130:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6985a10> -> __condition
                                    __expression = __cache_140574121811088

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140574121811088
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>\n:\n                                      ')

                                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121811280
                                    __attrs_140574121811280 = _static_140574442558096

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121809872
                                    __default_140574121809872 = _DEFAULT_MARKER

                                    # <Value u'interim/formatted_value' (132:57)> -> __cache_140574121808272
                                    __token = 7734
                                    try:
                                        __zt_tmp = __attrs_140574121811280
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140574121808272 = _static_140574397981968('path', u'interim/formatted_value', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'interim/formatted_value' (132:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69852d0> -> __condition
                                    __expression = __cache_140574121808272

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140574121808272
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>\n                                      ')

                                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121808976
                                    __attrs_140574121808976 = _static_140574442558096

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span>')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574121810640
                                    __default_140574121810640 = _DEFAULT_MARKER

                                    # <Value u'interim/formatted_unit' (133:57)> -> __cache_140574121810832
                                    __token = 7818
                                    try:
                                        __zt_tmp = __attrs_140574121808976
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140574121810832 = _static_140574397981968('path', u'interim/formatted_unit', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                    # <BinOp left=<Value u'interim/formatted_unit' (133:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f6985f10> -> __condition
                                    __expression = __cache_140574121810832

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140574121810832
                                        __content = __quote(__content, None, '\xad', None, None)
                                        if (__content is not None):
                                            __append(__content)
                                    __append(u'</span>\n                                    \n                                  ')
                                    ____index_140574123589776 -= 1
                                    if (____index_140574123589776 > 0):
                                        __append('')
                                if (__backup_interim_140574122257360 is __marker):
                                    del econtext['interim']
                                else:
                                    econtext['interim'] = __backup_interim_140574122257360
                                __append(u'\n                                </li>')
                                ____index_140574123604240 -= 1
                                if (____index_140574123604240 > 0):
                                    __append('\n                                ')
                            if (__backup_interims_140574122311440 is __marker):
                                del econtext['interims']
                            else:
                                econtext['interims'] = __backup_interims_140574122311440
                            __append(u'\n                              </ul>\n                            </td>\n                          </tr>')
                        __append(u'\n                        </tfoot>')
                        if (__backup_category_comments_140574123239824 is __marker):
                            del econtext['category_comments']
                        else:
                            econtext['category_comments'] = __backup_category_comments_140574123239824
                        __append(u'\n                      </table>\n                    ')
                        ____index_140574123240080 -= 1
                        if (____index_140574123240080 > 0):
                            __append('')
                    if (__backup_category_140574123237584 is __marker):
                        del econtext['category']
                    else:
                        econtext['category'] = __backup_category_140574123237584
                    if (__backup_categories_by_poc_140574122223056 is __marker):
                        del econtext['categories_by_poc']
                    else:
                        econtext['categories_by_poc'] = __backup_categories_by_poc_140574122223056
                    __append(u'\n\n                  ')
                    ____index_140574123240784 -= 1
                    if (____index_140574123240784 > 0):
                        __append('')
                if (__backup_poc_140574122223248 is __marker):
                    del econtext['poc']
                else:
                    econtext['poc'] = __backup_poc_140574122223248
                if (__backup_analyses_by_poc_140574122224848 is __marker):
                    del econtext['analyses_by_poc']
                else:
                    econtext['analyses_by_poc'] = __backup_analyses_by_poc_140574122224848
                __append(u'\n                </div>\n              </div>\n            ')
                ____index_140574123158352 -= 1
                if (____index_140574123158352 > 0):
                    __append('')
            if (__backup_model_140574123158992 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140574123158992
            __append(u'\n          ')
            __i18n_domain = __previous_i18n_domain_140574123155920
            if (__backup_outofrange_symbol_140574123156816 is __marker):
                del econtext['outofrange_symbol']
            else:
                econtext['outofrange_symbol'] = __backup_outofrange_symbol_140574123156816
            if (__backup_accredited_symbol_140574123135312 is __marker):
                del econtext['accredited_symbol']
            else:
                econtext['accredited_symbol'] = __backup_accredited_symbol_140574123135312
            if (__backup_collection_140574123254480 is __marker):
                del econtext['collection']
            else:
                econtext['collection'] = __backup_collection_140574123254480
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }