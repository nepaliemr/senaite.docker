# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/documentactions.pt'

__tokens = {102: (u'view/actions', 4, 33), 195: (u'nocall: context/@@plone/normalizeString', 6, 36), 267: (u'view/actions', 7, 30), 310: (u"python:'document-action-' + normalizeString(daction['id'])", 8, 29), 452: (u'daction/url', 11, 33), 499: (u' daction/link_target|nothin', 12, 34), 561: (u'e daction/descripti', 13, 32), 615: (u'daction/icon', 14, 30), 665: (u"python:daction.get('icon')", 15, 36), 728: (u" python:daction.get('title'", 16, 35), 794: (u"e python:daction.get('title", 17, 36), 856: (u'not:daction/icon', 18, 29), 901: (u"python:daction.get('id')", 19, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574284475152 = {u'id': u'senaite-document-actions', }
_static_140574270458320 = {u'id': u"python:'document-action-' + normalizeString(daction['id'])", }
_static_140574266172496 = {u'class': u'nav nav-pills float-right', }
_static_140574270456784 = {u'title': u'daction/description', u'href': u'', u'class': u'nav-link', u'target': u'daction/link_target|nothing', }
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}
_static_140574267880336 = {u'src': u"python:daction.get('icon')", u'alt': u"python:daction.get('title')", u'title': u"python:daction.get('title')", }

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

            # <Static value=<_ast.Dict object at 0x7fda004a6b10> name=None at 7fda004a6bd0> -> __attrs_140574266173648
            __attrs_140574266173648 = _static_140574284475152
            __previous_i18n_domain_140574266175376 = __i18n_domain
            __i18n_domain = u'senaite.core'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="senaite-document-actions">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266172624
            __attrs_140574266172624 = _static_140574442558096

            # <Value u'view/actions' (4:33)> -> __condition
            __token = 102
            try:
                __zt_tmp = __attrs_140574266172624
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('path', u'view/actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff332450> name=None at 7fd9ff332110> -> __attrs_140574270458512
                __attrs_140574270458512 = _static_140574266172496
                __backup_normalizeString_140574266175248 = get('normalizeString', __marker)

                # <Value u'nocall: context/@@plone/normalizeString' (6:36)> -> __value
                __token = 195
                try:
                    __zt_tmp = __attrs_140574270458512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('nocall', u' context/@@plone/normalizeString', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['normalizeString'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="nav nav-pills float-right">\n      ')

                # <Static value=<_ast.Dict object at 0x7fd9ff7489d0> name=None at 7fd9ff748590> -> __attrs_140574270459472
                __attrs_140574270459472 = _static_140574270458320
                __backup_daction_140574284370704 = get('daction', __marker)

                # <Value u'view/actions' (7:30)> -> __iterator
                __token = 267
                try:
                    __zt_tmp = __attrs_140574270459472
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140574397981968('path', u'view/actions', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                (__iterator, ____index_140574270459280, ) = getitem('repeat')(u'daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270457296
                    __default_140574270457296 = _DEFAULT_MARKER

                    # <Substitution u"python:'document-action-' + normalizeString(daction['id'])" (8:29)> -> __attr_id
                    __token = 310
                    try:
                        __zt_tmp = __attrs_140574270459472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140574397981968('python', u"'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff7483d0> name=None at 7fd9ff748b50> -> __attrs_140574270567952
                    __attrs_140574270567952 = _static_140574270456784

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267882384
                    __default_140574267882384 = _DEFAULT_MARKER

                    # <Substitution u'daction/url' (11:33)> -> __attr_href
                    __token = 452
                    try:
                        __zt_tmp = __attrs_140574270567952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'daction/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u' class="nav-link"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270566992
                    __default_140574270566992 = _DEFAULT_MARKER

                    # <Substitution u'daction/link_target|nothing' (12:34)> -> __attr_target
                    __token = 499
                    try:
                        __zt_tmp = __attrs_140574270567952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140574397981968('path', u'daction/link_target|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((u' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270567824
                    __default_140574270567824 = _DEFAULT_MARKER

                    # <Substitution u'daction/description' (13:32)> -> __attr_title
                    __token = 561
                    try:
                        __zt_tmp = __attrs_140574270567952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140574397981968('path', u'daction/description', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff4d3390> name=None at 7fd9ff4d3fd0> -> __attrs_140574267879888
                    __attrs_140574267879888 = _static_140574267880336

                    # <Value u'daction/icon' (14:30)> -> __condition
                    __token = 615
                    try:
                        __zt_tmp = __attrs_140574267879888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'daction/icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267880208
                        __default_140574267880208 = _DEFAULT_MARKER

                        # <Substitution u"python:daction.get('icon')" (15:36)> -> __attr_src
                        __token = 665
                        try:
                            __zt_tmp = __attrs_140574267879888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140574397981968('python', u"daction.get('icon')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267883216
                        __default_140574267883216 = _DEFAULT_MARKER

                        # <Substitution u"python:daction.get('title')" (16:35)> -> __attr_alt
                        __token = 728
                        try:
                            __zt_tmp = __attrs_140574267879888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140574397981968('python', u"daction.get('title')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267882704
                        __default_140574267882704 = _DEFAULT_MARKER

                        # <Substitution u"python:daction.get('title')" (17:36)> -> __attr_title
                        __token = 794
                        try:
                            __zt_tmp = __attrs_140574267879888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140574397981968('python', u"daction.get('title')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u'/>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284476304
                    __attrs_140574284476304 = _static_140574442558096

                    # <Value u'not:daction/icon' (18:29)> -> __condition
                    __token = 856
                    try:
                        __zt_tmp = __attrs_140574284476304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('not', u'daction/icon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284476176
                        __default_140574284476176 = _DEFAULT_MARKER

                        # <Value u"python:daction.get('id')" (19:27)> -> __cache_140574284473104
                        __token = 901
                        try:
                            __zt_tmp = __attrs_140574284476304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574284473104 = _static_140574397981968('python', u"daction.get('id')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u"python:daction.get('id')" (19:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda004a6b50> -> __condition
                        __expression = __cache_140574284473104

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140574284473104
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n        </a>\n      </li>')
                    ____index_140574270459280 -= 1
                    if (____index_140574270459280 > 0):
                        __append('\n      ')
                if (__backup_daction_140574284370704 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_140574284370704
                __append(u'\n    </ul>')
                if (__backup_normalizeString_140574266175248 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140574266175248
                __append(u'\n  ')
            __append(u'\n</div>')
            __i18n_domain = __previous_i18n_domain_140574266175376
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }