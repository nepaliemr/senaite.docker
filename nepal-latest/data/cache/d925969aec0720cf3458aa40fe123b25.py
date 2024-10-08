# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/src/senaite.core/src/senaite/core/browser/viewlets/templates/sampleanalyses.pt'

__tokens = {101: (u'string:table-${view/capture|other}-analyses', 3, 20), 172: (u' python:view.is_collapsed(', 4, 26), 223: (u'l context/@@plone_portal_state/port', 5, 22), 56: (u'python:view.available()', 2, 20), 423: (u'view/icon_name|nothing', 11, 27), 474: (u' view/title|nothin', 12, 27), 553: (u'title', 14, 25), 589: (u'icon|nothing', 15, 28), 636: (u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', 16, 33), 762: (u'title', 17, 66), 936: (u'string:#${id}', 23, 38), 978: (u'collapsed', 24, 26), 1058: (u'not: collapsed', 25, 26), 1195: (u'id', 29, 30), 1231: (u" python:'collapse' if collapsed else 'show", 30, 32), 1314: (u'python:view.contents_table()', 31, 37), 1523: (u'id', 37, 34)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140168208991440 = __compile_zt_expr
_static_140168046976464 = {u'src': u'string:${portal/absolute_url}/senaite_theme/icon/${icon}', }
_static_140168047842512 = {u'class': u'analysis-listing-table', }
_static_140168036673040 = {u'class': u'd-inline-block', }
_static_140168037250256 = {u'class': u'toggle-icon fas fa-toggle-off', }
_static_140168046973648 = {u'class': u'align-middle', }
_static_140168036705360 = {u'class': u'row mb-4', }
_static_140168208992144 = __C2ZContextWrapper
_static_140168036675408 = {u'class': u'col-sm-12', }
_static_140168257770128 = {}
_static_140168037253072 = {u'data-toggle': u'collapse', u'href': u'#', u'class': u'text-decoration-none ml-2', u'data-target': u'string:#${id}', }
_static_140168037793936 = {u'id': u'id', u'class': u"python:'collapse' if collapsed else 'show'", }
_static_140168037796432 = {u'class': u'toggle-icon fas fa-toggle-on', }
_static_140168027214288 = {u'type': u'text/javascript', }

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

            # <Static value=<_ast.Dict object at 0x7f7b6ab354d0> name=None at 7f7b6ab35690> -> __attrs_140168047841552
            __attrs_140168047841552 = _static_140168047842512
            __backup_id_140168026290640 = get('id', __marker)

            # <Value u'string:table-${view/capture|other}-analyses' (3:20)> -> __value
            __token = 101
            try:
                __zt_tmp = __attrs_140168047841552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('string', u'table-${view/capture|other}-analyses', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['id'] = __value
            __backup_collapsed_140168047246480 = get('collapsed', __marker)

            # <Value u'python:view.is_collapsed()' (4:26)> -> __value
            __token = 172
            try:
                __zt_tmp = __attrs_140168047841552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('python', u'view.is_collapsed()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['collapsed'] = __value
            __backup_portal_140168047762576 = get('portal', __marker)

            # <Value u'context/@@plone_portal_state/portal' (5:22)> -> __value
            __token = 223
            try:
                __zt_tmp = __attrs_140168047841552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140168208991440('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            econtext['portal'] = __value

            # <Value u'python:view.available()' (2:20)> -> __condition
            __token = 56
            try:
                __zt_tmp = __attrs_140168047841552
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140168208991440('python', u'view.available()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140168047844944 = __i18n_domain
                __i18n_domain = u'senaite.core'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="analysis-listing-table">\n  ')

                # <Static value=<_ast.Dict object at 0x7f7b6a096450> name=None at 7f7b6be38cd0> -> __attrs_140168036705104
                __attrs_140168036705104 = _static_140168036705360

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="row mb-4">\n    ')

                # <Static value=<_ast.Dict object at 0x7f7b6a08ef50> name=None at 7f7b6a177090> -> __attrs_140168036674256
                __attrs_140168036674256 = _static_140168036675408

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="col-sm-12">\n\n      <!-- Analysis listing title and icon -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a08e610> name=None at 7f7b6a08e690> -> __attrs_140168036672848
                __attrs_140168036672848 = _static_140168036673040
                __backup_icon_140168016890192 = get('icon', __marker)

                # <Value u'view/icon_name|nothing' (11:27)> -> __value
                __token = 423
                try:
                    __zt_tmp = __attrs_140168036672848
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/icon_name|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['icon'] = __value
                __backup_title_140168037234512 = get('title', __marker)

                # <Value u'view/title|nothing' (12:27)> -> __value
                __token = 474
                try:
                    __zt_tmp = __attrs_140168036672848
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140168208991440('path', u'view/title|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                econtext['title'] = __value

                # <Value u'title' (14:25)> -> __condition
                __token = 553
                try:
                    __zt_tmp = __attrs_140168036672848
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3 class="d-inline-block">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa61dd0> name=None at 7f7b6aa610d0> -> __attrs_140168046975504
                    __attrs_140168046975504 = _static_140168046976464

                    # <Value u'icon|nothing' (15:28)> -> __condition
                    __token = 589
                    try:
                        __zt_tmp = __attrs_140168046975504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140168208991440('path', u'icon|nothing', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img')

                        # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046974032
                        __default_140168046974032 = _DEFAULT_MARKER

                        # <Substitution u'string:${portal/absolute_url}/senaite_theme/icon/${icon}' (16:33)> -> __attr_src
                        __token = 636
                        try:
                            __zt_tmp = __attrs_140168046975504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140168208991440('string', u'${portal/absolute_url}/senaite_theme/icon/${icon}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))
                        __append(u'/>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f7b6aa612d0> name=None at 7f7b6aa618d0> -> __attrs_140168037249104
                    __attrs_140168037249104 = _static_140168046973648

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="align-middle">')

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168046976912
                    __default_140168046976912 = _DEFAULT_MARKER

                    # <Value u'title' (17:66)> -> __cache_140168037629136
                    __token = 762
                    try:
                        __zt_tmp = __attrs_140168037249104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140168037629136 = _static_140168208991440('path', u'title', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                    # <BinOp left=<Value u'title' (17:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6aa61890> -> __condition
                    __expression = __cache_140168037629136

                    # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140168037629136
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n      </h3>')
                if (__backup_title_140168037234512 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140168037234512
                if (__backup_icon_140168016890192 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140168016890192
                __append(u'\n\n      <!-- Toggle Button -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a11bfd0> name=None at 7f7b6a11bb50> -> __attrs_140168037251600
                __attrs_140168037251600 = _static_140168037253072

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a href="#" class="text-decoration-none ml-2" data-toggle="collapse"')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037251024
                __default_140168037251024 = _DEFAULT_MARKER

                # <Substitution u'string:#${id}' (23:38)> -> __attr_data_target
                __token = 936
                try:
                    __zt_tmp = __attrs_140168037251600
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_target = _static_140168208991440('string', u'#${id}', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_data_target = __quote(__attr_data_target, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_target is not None):
                    __append((u' data-target="%s"' % __attr_data_target))
                __append(u'>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a11b4d0> name=None at 7f7b6a11b210> -> __attrs_140168037796304
                __attrs_140168037796304 = _static_140168037250256

                # <Value u'collapsed' (24:26)> -> __condition
                __token = 978
                try:
                    __zt_tmp = __attrs_140168037796304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('path', u'collapsed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="toggle-icon fas fa-toggle-off"></i>')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1a0a50> name=None at 7f7b6a1a0b50> -> __attrs_140168037794960
                __attrs_140168037794960 = _static_140168037796432

                # <Value u'not: collapsed' (25:26)> -> __condition
                __token = 1058
                try:
                    __zt_tmp = __attrs_140168037794960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140168208991440('not', u' collapsed', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                if __condition:

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="toggle-icon fas fa-toggle-on"></i>')
                __append(u'\n      </a>\n\n      <!-- Analyis listing table -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b6a1a0090> name=None at 7f7b6a1a0f10> -> __attrs_140168037797520
                __attrs_140168037797520 = _static_140168037793936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div')

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037794320
                __default_140168037794320 = _DEFAULT_MARKER

                # <Substitution u'id' (29:30)> -> __attr_id
                __token = 1195
                try:
                    __zt_tmp = __attrs_140168037797520
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140168208991440('path', u'id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037797264
                __default_140168037797264 = _DEFAULT_MARKER

                # <Substitution u"python:'collapse' if collapsed else 'show'" (30:32)> -> __attr_class
                __token = 1231
                try:
                    __zt_tmp = __attrs_140168037797520
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140168208991440('python', u"'collapse' if collapsed else 'show'", econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n        ')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168037794768
                __attrs_140168037794768 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168037795856
                __default_140168037795856 = _DEFAULT_MARKER

                # <Value u'python:view.contents_table()' (31:37)> -> __cache_140168037796560
                __token = 1314
                try:
                    __zt_tmp = __attrs_140168037794768
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168037796560 = _static_140168208991440('python', u'view.contents_table()', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:view.contents_table()' (31:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b6a1a0b90> -> __condition
                __expression = __cache_140168037796560

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span/>')
                else:
                    __content = __cache_140168037796560
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n      </div>\n\n      <!-- Toggle JS -->\n      ')

                # <Static value=<_ast.Dict object at 0x7f7b697891d0> name=None at 7f7b697893d0> -> __attrs_140168027216848
                __attrs_140168027216848 = _static_140168027214288

                # <script ... (0:0)
                # --------------------------------------------------------
                __append(u'<script type="text/javascript">\n       document.addEventListener("DOMContentLoaded", (event) => {\n         let id=\'')

                # <Static value=<_ast.Dict object at 0x7f7b77369290> name=None at 7f7b77369190> -> __attrs_140168027216912
                __attrs_140168027216912 = _static_140168257770128

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __default_140168027217744
                __default_140168027217744 = _DEFAULT_MARKER

                # <Value u'id' (37:34)> -> __cache_140168027214480
                __token = 1523
                try:
                    __zt_tmp = __attrs_140168027216912
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140168027214480 = _static_140168208991440('path', u'id', econtext=econtext)(_static_140168208992144(econtext, __zt_tmp))

                # <BinOp left=<Value u'id' (37:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7b773693d0> at 7f7b697898d0> -> __condition
                __expression = __cache_140168027214480

                # <Symbol value=<DEFAULT> at 7f7b773693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140168027214480
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\';\n         let toggle_icon = $(\'a[data-target="#\' + id + \'"] i.toggle-icon\');\n         $(\'#\' + id).on(\'show.bs.collapse\', function () {\n           toggle_icon.removeClass("fa-toggle-off");\n           toggle_icon.addClass("fa-toggle-on");\n         });\n         $(\'#\' + id).on(\'hide.bs.collapse\', function () {\n           toggle_icon.removeClass("fa-toggle-on");\n           toggle_icon.addClass("fa-toggle-off");\n         });\n       });\n      </script>\n\n    </div>\n  </div>\n</div>')
                __i18n_domain = __previous_i18n_domain_140168047844944
            if (__backup_portal_140168047762576 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140168047762576
            if (__backup_collapsed_140168047246480 is __marker):
                del econtext['collapsed']
            else:
                econtext['collapsed'] = __backup_collapsed_140168047246480
            if (__backup_id_140168026290640 is __marker):
                del econtext['id']
            else:
                econtext['id'] = __backup_id_140168026290640
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }