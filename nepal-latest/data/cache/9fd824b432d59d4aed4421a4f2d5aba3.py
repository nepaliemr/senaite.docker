# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/path_bar.pt'

__tokens = {85: (u'view/breadcrumbs', 3, 30), 127: (u' view/is_rt', 4, 24), 167: (u"python:is_rtl and 'rtl' or 'ltr'", 5, 26), 345: (u'view/navigation_root_url', 9, 61), 424: (u'breadcrumbs', 12, 33), 474: (u'repeat/crumb/end', 13, 36), 523: (u' crumb/absolute_ur', 14, 31), 576: (u'e crumb/Tit', 15, 32), 626: (u"python: is_last and 'active breadcrumb-item' or 'breadcrumb-item'", 16, 34), 723: (u' string:breadcrumbs-${repeat/crumb/number', 17, 30), 818: (u'not: url', 19, 27), 862: (u'url', 20, 34), 901: (u" python:is_last and 'text-secondary", 21, 34), 965: (u'title', 22, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574270457488 = {u'aria-label': u'breadcrumb', }
_static_140574270207504 = {u'id': u'breadcrumbs-home', u'class': u'breadcrumb-item', }
_static_140574267889808 = {u'href': u'#', u'class': u"python:is_last and 'text-secondary'", }
_static_140574270207632 = {u'class': u"python: is_last and 'active breadcrumb-item' or 'breadcrumb-item'", u'id': u'string:breadcrumbs-${repeat/crumb/number}', }
_static_140574442558096 = {}
_static_140574270457808 = {u'class': u'breadcrumb', u'dir': u"python:is_rtl and 'rtl' or 'ltr'", }
_static_140574397982672 = __C2ZContextWrapper
_static_140574397981968 = __compile_zt_expr
_static_140574270230032 = {u'href': u'#', }

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

            # <Static value=<_ast.Dict object at 0x7fd9ff748690> name=None at 7fd9ff748390> -> __attrs_140574270455952
            __attrs_140574270455952 = _static_140574270457488

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append(u'<nav aria-label="breadcrumb">\n  ')

            # <Static value=<_ast.Dict object at 0x7fd9ff7487d0> name=None at 7fd9ff7489d0> -> __attrs_140574270208976
            __attrs_140574270208976 = _static_140574270457808
            __backup_breadcrumbs_140574270459024 = get('breadcrumbs', __marker)

            # <Value u'view/breadcrumbs' (3:30)> -> __value
            __token = 85
            try:
                __zt_tmp = __attrs_140574270208976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/breadcrumbs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __backup_is_rtl_140574270456208 = get('is_rtl', __marker)

            # <Value u'view/is_rtl' (4:24)> -> __value
            __token = 127
            try:
                __zt_tmp = __attrs_140574270208976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/is_rtl', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['is_rtl'] = __value
            __previous_i18n_domain_140574270207824 = __i18n_domain
            __i18n_domain = u'plone'

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append(u'<ol class="breadcrumb"')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270208784
            __default_140574270208784 = _DEFAULT_MARKER

            # <Substitution u"python:is_rtl and 'rtl' or 'ltr'" (5:26)> -> __attr_dir
            __token = 167
            try:
                __zt_tmp = __attrs_140574270208976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_140574397981968('python', u"is_rtl and 'rtl' or 'ltr'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_dir is not None):
                __append((u' dir="%s"' % __attr_dir))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fd9ff70b610> name=None at 7fd9ff70bc90> -> __attrs_140574270228304
            __attrs_140574270228304 = _static_140574270207504

            # <li ... (0:0)
            # --------------------------------------------------------
            __append(u'<li id="breadcrumbs-home" class="breadcrumb-item">\n      ')

            # <Static value=<_ast.Dict object at 0x7fd9ff710e10> name=None at 7fd9ff710350> -> __attrs_140574284346128
            __attrs_140574284346128 = _static_140574270230032

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270229328
            __default_140574270229328 = _DEFAULT_MARKER

            # <Substitution u'view/navigation_root_url' (9:61)> -> __attr_href
            __token = 345
            try:
                __zt_tmp = __attrs_140574284346128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140574397981968('path', u'view/navigation_root_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')
            __stream_140574270226512 = []
            __append_140574270226512 = __stream_140574270226512.append
            __append_140574270226512(u'Home')
            __msgid_140574270226512 = __re_whitespace(''.join(__stream_140574270226512)).strip()
            if u'Home':
                __append(translate(u'Home', mapping=None, default=__msgid_140574270226512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n    </li>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270224208
            __attrs_140574270224208 = _static_140574442558096
            __backup_crumb_140574270207120 = get('crumb', __marker)

            # <Value u'breadcrumbs' (12:33)> -> __iterator
            __token = 424
            try:
                __zt_tmp = __attrs_140574270224208
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140574397981968('path', u'breadcrumbs', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            (__iterator, ____index_140574270225296, ) = getitem('repeat')(u'crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270206736
                __attrs_140574270206736 = _static_140574442558096
                __backup_is_last_140574284359376 = get('is_last', __marker)

                # <Value u'repeat/crumb/end' (13:36)> -> __value
                __token = 474
                try:
                    __zt_tmp = __attrs_140574270206736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'repeat/crumb/end', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['is_last'] = __value
                __backup_url_140574270397136 = get('url', __marker)

                # <Value u'crumb/absolute_url' (14:31)> -> __value
                __token = 523
                try:
                    __zt_tmp = __attrs_140574270206736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'crumb/absolute_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['url'] = __value
                __backup_title_140574267914704 = get('title', __marker)

                # <Value u'crumb/Title' (15:32)> -> __value
                __token = 576
                try:
                    __zt_tmp = __attrs_140574270206736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140574397981968('path', u'crumb/Title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                econtext['title'] = __value
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fd9ff70b690> name=None at 7fd9ff70bd50> -> __attrs_140574270224400
                __attrs_140574270224400 = _static_140574270207632

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270224720
                __default_140574270224720 = _DEFAULT_MARKER

                # <Substitution u"python: is_last and 'active breadcrumb-item' or 'breadcrumb-item'" (16:34)> -> __attr_class
                __token = 626
                try:
                    __zt_tmp = __attrs_140574270224400
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140574397981968('python', u" is_last and 'active breadcrumb-item' or 'breadcrumb-item'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270223696
                __default_140574270223696 = _DEFAULT_MARKER

                # <Substitution u'string:breadcrumbs-${repeat/crumb/number}' (17:30)> -> __attr_id
                __token = 723
                try:
                    __zt_tmp = __attrs_140574270224400
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140574397981968('string', u'breadcrumbs-${repeat/crumb/number}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7fd9ff4d5890> name=None at 7fd9ff4d5390> -> __attrs_140574284338832
                __attrs_140574284338832 = _static_140574267889808

                # <Negate value=<Value u'not: url' (19:27)> at 7fda00485ad0> -> __cache_140574284339920

                # <Value u'not: url' (19:27)> -> __cache_140574284339920
                __token = 818
                try:
                    __zt_tmp = __attrs_140574284338832
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574284339920 = _static_140574397981968('not', u' url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                __cache_140574284339920 = not __cache_140574284339920
                __condition = __cache_140574284339920
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284338384
                    __default_140574284338384 = _DEFAULT_MARKER

                    # <Substitution u'url' (20:34)> -> __attr_href
                    __token = 862
                    try:
                        __zt_tmp = __attrs_140574284338832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140574397981968('path', u'url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284340048
                    __default_140574284340048 = _DEFAULT_MARKER

                    # <Substitution u"python:is_last and 'text-secondary'" (21:34)> -> __attr_class
                    __token = 901
                    try:
                        __zt_tmp = __attrs_140574284338832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('python', u"is_last and 'text-secondary'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267891536
                __default_140574267891536 = _DEFAULT_MARKER

                # <Value u'title' (22:26)> -> __cache_140574267888656
                __token = 965
                try:
                    __zt_tmp = __attrs_140574284338832
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140574267888656 = _static_140574397981968('path', u'title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                # <BinOp left=<Value u'title' (22:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4d5c50> -> __condition
                __expression = __cache_140574267888656

                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n            crumb\n          ')
                else:
                    __content = __cache_140574267888656
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __condition = __cache_140574284339920
                if __condition:
                    __append(u'</a>')
                __append(u'\n        </li>\n      ')
                if (__backup_title_140574267914704 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140574267914704
                if (__backup_url_140574270397136 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_140574270397136
                if (__backup_is_last_140574284359376 is __marker):
                    del econtext['is_last']
                else:
                    econtext['is_last'] = __backup_is_last_140574284359376
                __append(u'\n    ')
                ____index_140574270225296 -= 1
                if (____index_140574270225296 > 0):
                    __append('')
            if (__backup_crumb_140574270207120 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_140574270207120
            __append(u'\n\n  </ol>')
            __i18n_domain = __previous_i18n_domain_140574270207824
            if (__backup_is_rtl_140574270456208 is __marker):
                del econtext['is_rtl']
            else:
                econtext['is_rtl'] = __backup_is_rtl_140574270456208
            if (__backup_breadcrumbs_140574270459024 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_140574270459024
            __append(u'\n</nav>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }