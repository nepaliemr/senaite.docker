# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {173: (u'view/enabled|nothing', 4, 25), 226: (u' view/isViewTemplate|nothin', 5, 31), 276: (u'python:enabled and isViewTemplate', 6, 20), 391: (u'view/site_url', 10, 32), 463: (u'view/next', 13, 26), 503: (u' view/previou', 14, 29), 543: (u'python:previous is not None or next is not None', 15, 24), 650: (u'previous', 19, 44), 795: (u'previous/url', 22, 35), 999: (u'previous/title', 26, 55), 1108: (u'next', 31, 40), 1241: (u'next/url', 34, 35), 1393: (u'next/title', 37, 55)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574397982672 = __C2ZContextWrapper
_static_140574268000528 = {u'class': u'arrow', }
_static_140574268001680 = {u'href': u'previous/url', u'title': u'Go to previous item', }
_static_140574270168080 = {u'class': u'previous', }
_static_140574442558096 = {}
_static_140574270208656 = {u'class': u'pagination', }
_static_140574266194000 = {u'class': u'label', }
_static_140574267904528 = {u'href': u'next/url', u'title': u'Go to next item', }
_static_140574269032464 = {u'class': u'label', }
_static_140574397981968 = __compile_zt_expr
_static_140574270395984 = {u'class': u'next', }
_static_140574270569872 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140574266170640 = {u'class': u'arrow', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff763d90> name=None at 7fd9ff763ed0> -> __attrs_140574270566672
            __attrs_140574270566672 = _static_140574270569872
            __backup_enabled_140574270567376 = get('enabled', __marker)

            # <Value u'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140574270566672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/enabled|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140574270347472 = get('isViewTemplate', __marker)

            # <Value u'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_140574270566672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/isViewTemplate|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value u'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_140574270566672
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'enabled and isViewTemplate', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270568784 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270208976
                __attrs_140574270208976 = _static_140574442558096
                __backup_portal_url_140574270569680 = get('portal_url', __marker)

                # <Value u'view/site_url' (10:32)> -> __value
                __token = 391
                try:
                    __zt_tmp = __attrs_140574270208976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/site_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff70ba90> name=None at 7fd9ff70b8d0> -> __attrs_140574270209168
                __attrs_140574270209168 = _static_140574270208656
                __backup_next_140574270206992 = get('next', __marker)

                # <Value u'view/next' (13:26)> -> __value
                __token = 463
                try:
                    __zt_tmp = __attrs_140574270209168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/next', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_140574270569232 = get('previous', __marker)

                # <Value u'view/previous' (14:29)> -> __value
                __token = 503
                try:
                    __zt_tmp = __attrs_140574270209168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'view/previous', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value u'python:previous is not None or next is not None' (15:24)> -> __condition
                __token = 543
                try:
                    __zt_tmp = __attrs_140574270209168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'previous is not None or next is not None', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<nav class="pagination">\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270166288
                    __attrs_140574270166288 = _static_140574442558096

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff701c10> name=None at 7fd9ff701090> -> __attrs_140574270166416
                    __attrs_140574270166416 = _static_140574270168080

                    # <Value u'previous' (19:44)> -> __condition
                    __token = 650
                    try:
                        __zt_tmp = __attrs_140574270166416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'previous', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="previous">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4f0d90> name=None at 7fd9ff4f0d10> -> __attrs_140574268001744
                        __attrs_140574268001744 = _static_140574268001680

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267999056
                        __default_140574267999056 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_previous_item' node=<_ast.Str object at 0x7fd9ff4f0090> at 7fd9ff4f0750> -> __attr_title
                        __attr_title = u'Go to previous item'
                        __attr_title = translate(u'title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268000656
                        __default_140574268000656 = _DEFAULT_MARKER

                        # <Substitution u'previous/url' (22:35)> -> __attr_href
                        __token = 795
                        try:
                            __zt_tmp = __attrs_140574268001744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140574397981968('path', u'previous/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4f0910> name=None at 7fd9ff4f0b90> -> __attrs_140574270395600
                        __attrs_140574270395600 = _static_140574268000528

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff337850> name=None at 7fd9ff33b890> -> __attrs_140574266195536
                        __attrs_140574266195536 = _static_140574266194000

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140574270611040_itemtitle = ''
                        __stream_140574270398352 = []
                        __append_140574270398352 = __stream_140574270398352.append
                        __append_140574270398352(u'\n              Previous:\n              ')
                        __stream_140574270611040_itemtitle = []
                        __append_140574270611040_itemtitle = __stream_140574270611040_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266193808
                        __attrs_140574266193808 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266195088
                        __default_140574266195088 = _DEFAULT_MARKER

                        # <Value u'previous/title' (26:55)> -> __cache_140574266194128
                        __token = 999
                        try:
                            __zt_tmp = __attrs_140574266193808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574266194128 = _static_140574397981968('path', u'previous/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'previous/title' (26:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff337490> -> __condition
                        __expression = __cache_140574266194128

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140574270611040_itemtitle(u'<span />')
                        else:
                            __content = __cache_140574266194128
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140574270611040_itemtitle(__content)
                        __append_140574270398352(u'${itemtitle}')
                        __stream_140574270611040_itemtitle = ''.join(__stream_140574270611040_itemtitle)
                        __append_140574270398352(u'\n            ')
                        __msgid_140574270398352 = __re_whitespace(''.join(__stream_140574270398352)).strip()
                        if u'label_previous_item':
                            __append(translate(u'label_previous_item', mapping={u'itemtitle': __stream_140574270611040_itemtitle, }, default=__msgid_140574270398352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </a>\n        </li>')
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff739650> name=None at 7fd9ff4f0450> -> __attrs_140574266193680
                    __attrs_140574266193680 = _static_140574270395984

                    # <Value u'next' (31:40)> -> __condition
                    __token = 1108
                    try:
                        __zt_tmp = __attrs_140574266193680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('path', u'next', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="next">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff4d9210> name=None at 7fd9ff4d9e10> -> __attrs_140574269032720
                        __attrs_140574269032720 = _static_140574267904528

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269033488
                        __default_140574269033488 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_next_item' node=<_ast.Str object at 0x7fd9ff5ec1d0> at 7fd9ff5ec150> -> __attr_title
                        __attr_title = u'Go to next item'
                        __attr_title = translate(u'title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269031888
                        __default_140574269031888 = _DEFAULT_MARKER

                        # <Substitution u'next/url' (34:35)> -> __attr_href
                        __token = 1241
                        try:
                            __zt_tmp = __attrs_140574269032720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140574397981968('path', u'next/url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff5ec810> name=None at 7fd9ff5ec4d0> -> __attrs_140574269032016
                        __attrs_140574269032016 = _static_140574269032464

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140574270610560_itemtitle = ''
                        __stream_140574269034256 = []
                        __append_140574269034256 = __stream_140574269034256.append
                        __append_140574269034256(u'\n              Next:\n              ')
                        __stream_140574270610560_itemtitle = []
                        __append_140574270610560_itemtitle = __stream_140574270610560_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266168208
                        __attrs_140574266168208 = _static_140574442558096

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266168144
                        __default_140574266168144 = _DEFAULT_MARKER

                        # <Value u'next/title' (37:55)> -> __cache_140574266168080
                        __token = 1393
                        try:
                            __zt_tmp = __attrs_140574266168208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140574266168080 = _static_140574397981968('path', u'next/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                        # <BinOp left=<Value u'next/title' (37:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff331550> -> __condition
                        __expression = __cache_140574266168080

                        # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140574270610560_itemtitle(u'<span />')
                        else:
                            __content = __cache_140574266168080
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140574270610560_itemtitle(__content)
                        __append_140574269034256(u'${itemtitle}')
                        __stream_140574270610560_itemtitle = ''.join(__stream_140574270610560_itemtitle)
                        __append_140574269034256(u'\n            ')
                        __msgid_140574269034256 = __re_whitespace(''.join(__stream_140574269034256)).strip()
                        if u'label_next_item':
                            __append(translate(u'label_next_item', mapping={u'itemtitle': __stream_140574270610560_itemtitle, }, default=__msgid_140574269034256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fd9ff331d10> name=None at 7fd9ff331490> -> __attrs_140574266169872
                        __attrs_140574266169872 = _static_140574266170640

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n          </a>\n        </li>')
                    __append(u'\n\n        &nbsp;\n\n      </ul>\n\n    </nav>')
                if (__backup_previous_140574270569232 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140574270569232
                if (__backup_next_140574270206992 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140574270206992
                __append(u'\n\n  ')
                if (__backup_portal_url_140574270569680 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140574270569680
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140574270568784
            if (__backup_isViewTemplate_140574270347472 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140574270347472
            if (__backup_enabled_140574270567376 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140574270567376
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }