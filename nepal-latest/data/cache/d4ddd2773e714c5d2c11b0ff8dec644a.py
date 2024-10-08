# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.impress/src/senaite/impress/analysisrequest/templates/interpretations.pt'

__tokens = {26: (u'python:view.collection', 1, 26), 117: (u'collection', 4, 27), 217: (u'python:model.get_resultsinterpretation()', 6, 25), 286: (u" python:any(map(lambda r: r.get('richtext'), ris)", 7, 27), 363: (u'ris', 8, 24), 404: (u'has_ri', 9, 35), 486: (u'model/getId', 10, 73), 533: (u'ris', 11, 27), 568: (u'ri/richtext|nothing', 12, 29), 602: (u'ri/title|nothing', 12, 63), 692: (u'ri/richtext|nothing', 13, 56)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574121810512 = {u'class': u'row section-resultsinterpretation no-gutters', }
_static_140574123258576 = {u'class': u'text-info', }
_static_140574121808144 = {u'class': u'', }
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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574121807184
            __attrs_140574121807184 = _static_140574442558096
            __backup_collection_140574122223056 = get('collection', __marker)

            # <Value u'python:view.collection' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_140574121807184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['collection'] = __value
            __previous_i18n_domain_140574121805840 = __i18n_domain
            __i18n_domain = u'senaite.impress'
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574254440656
            __attrs_140574254440656 = _static_140574442558096
            __backup_model_140574123234064 = get('model', __marker)

            # <Value u'collection' (4:27)> -> __iterator
            __token = 117
            try:
                __zt_tmp = __attrs_140574254440656
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'collection', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574121808528, ) = getitem('repeat')(u'model', __iterator)
            econtext['model'] = None
            for __item in __iterator:
                econtext['model'] = __item
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9f6985a50> name=None at 7fd9f6985e10> -> __attrs_140574121809872
                __attrs_140574121809872 = _static_140574121810512
                __backup_ris_140574122301968 = get('ris', __marker)

                # <Value u'python:model.get_resultsinterpretation()' (6:25)> -> __value
                __token = 217
                try:
                    __zt_tmp = __attrs_140574121809872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u'model.get_resultsinterpretation()', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['ris'] = __value
                __backup_has_ri_140574123254992 = get('has_ri', __marker)

                # <Value u"python:any(map(lambda r: r.get('richtext'), ris))" (7:27)> -> __value
                __token = 286
                try:
                    __zt_tmp = __attrs_140574121809872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('python', u"any(map(lambda r: r.get('richtext'), ris))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['has_ri'] = __value

                # <Value u'ris' (8:24)> -> __condition
                __token = 363
                try:
                    __zt_tmp = __attrs_140574121809872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'ris', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="row section-resultsinterpretation no-gutters">\n      ')

                    # <Static value=<_ast.Dict object at 0x7fd9f6985110> name=None at 7fd9f6985fd0> -> __attrs_140574121808656
                    __attrs_140574121808656 = _static_140574121808144

                    # <Value u'has_ri' (9:35)> -> __condition
                    __token = 404
                    try:
                        __zt_tmp = __attrs_140574121808656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'has_ri', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="">\n        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122307984
                        __attrs_140574122307984 = _static_140574442558096

                        # <h1 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h1>')
                        __stream_140574122310608 = []
                        __append_140574122310608 = __stream_140574122310608.append
                        __append_140574122310608(u'Results Interpretation for ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122308304
                        __attrs_140574122308304 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122307856
                        __default_140574122307856 = _DEFAULT_MARKER

                        # <Value u'model/getId' (10:73)> -> __cache_140574122308368
                        __token = 486
                        try:
                            __zt_tmp = __attrs_140574122308304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574122308368 = _static_140574397981968('path', u'model/getId', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'model/getId' (10:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69ff090> -> __condition
                        __expression = __cache_140574122308368

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140574122310608(u'<span/>')
                        else:
                            __content = __cache_140574122308368
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140574122310608(__content)
                        __msgid_140574122310608 = __re_whitespace(''.join(__stream_140574122310608)).strip()
                        if __msgid_140574122310608:
                            __append(translate(__msgid_140574122310608, mapping=None, default=__msgid_140574122310608, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</h1>\n        ')

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122308688
                        __attrs_140574122308688 = _static_140574442558096
                        __backup_ri_140574123147920 = get('ri', __marker)

                        # <Value u'ris' (11:27)> -> __iterator
                        __token = 533
                        try:
                            __zt_tmp = __attrs_140574122308688
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140574397981968('path', u'ris', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        (__iterator, ____index_140574122308560, ) = getitem('repeat')(u'ri', __iterator)
                        econtext['ri'] = None
                        for __item in __iterator:
                            econtext['ri'] = __item
                            __append(u'\n          ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574122271312
                            __attrs_140574122271312 = _static_140574442558096

                            # <Value u'ri/richtext|nothing' (12:29)> -> __condition
                            __token = 568
                            try:
                                __zt_tmp = __attrs_140574122271312
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'ri/richtext|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <h2 ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<h2>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574122271056
                                __default_140574122271056 = _DEFAULT_MARKER

                                # <Value u'ri/title|nothing' (12:63)> -> __cache_140574122274128
                                __token = 602
                                try:
                                    __zt_tmp = __attrs_140574122271312
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574122274128 = _static_140574397981968('path', u'ri/title|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'ri/title|nothing' (12:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f6950> -> __condition
                                __expression = __cache_140574122274128

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'Department')
                                else:
                                    __content = __cache_140574122274128
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</h2>')
                            __append(u'\n          ')

                            # <Static value=<_ast.Dict object at 0x7fd9f6ae72d0> name=None at 7fd9f6ae7b50> -> __attrs_140574123259728
                            __attrs_140574123259728 = _static_140574123258576

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="text-info">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574123258384
                            __default_140574123258384 = _DEFAULT_MARKER

                            # <Value u'ri/richtext|nothing' (13:56)> -> __cache_140574122270992
                            __token = 692
                            try:
                                __zt_tmp = __attrs_140574123259728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574122270992 = _static_140574397981968('path', u'ri/richtext|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'ri/richtext|nothing' (13:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9f69f6050> -> __condition
                            __expression = __cache_140574122270992

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140574122270992
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n        ')
                            ____index_140574122308560 -= 1
                            if (____index_140574122308560 > 0):
                                __append('')
                        if (__backup_ri_140574123147920 is __marker):
                            del econtext['ri']
                        else:
                            econtext['ri'] = __backup_ri_140574123147920
                        __append(u'\n      </div>')
                    __append(u'\n    </div>')
                if (__backup_has_ri_140574123254992 is __marker):
                    del econtext['has_ri']
                else:
                    econtext['has_ri'] = __backup_has_ri_140574123254992
                if (__backup_ris_140574122301968 is __marker):
                    del econtext['ris']
                else:
                    econtext['ris'] = __backup_ris_140574122301968
                __append(u'\n  ')
                ____index_140574121808528 -= 1
                if (____index_140574121808528 > 0):
                    __append('')
            if (__backup_model_140574123234064 is __marker):
                del econtext['model']
            else:
                econtext['model'] = __backup_model_140574123234064
            __append(u'\n\n')
            __i18n_domain = __previous_i18n_domain_140574121805840
            if (__backup_collection_140574122223056 is __marker):
                del econtext['collection']
            else:
                econtext['collection'] = __backup_collection_140574122223056
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }