# -*- coding: utf-8 -*-
__filename = 'main'

__tokens = {31: (u'here/manage_page_header', 1, 31), 89: (u'here/manage_tabs', 3, 29), 229: (u"python:getattr(here.aq_explicit, 'has_order_support', 0)", 8, 38), 309: (u' modules/AccessControl/getSecurityManage', 9, 22), 383: (u"t python: 'position' if has_order_support else 'i", 10, 31), 458: (u"ey python:request.get('skey',default_so", 11, 22), 523: (u"key python:request.get('rkey','a", 12, 21), 585: (u"_alt python:'desc' if rkey=='asc' else ", 13, 24), 649: (u'  obs python: here.manage_get_sortedObjects(sortkey = skey, revkey =', 14, 18), 777: (u'string:${request/URL1}/', 16, 31), 834: (u'obs', 18, 30), 929: (u'obs', 19, 89), 992: (u"python:'thead-light sorted_%s'%(request.get('rkey',''))", 20, 57), 1422: (u"python:'Sort %s by Meta-Type'%( rkey_alt.upper() )", 28, 39), 1511: (u" python:'?skey=meta_type&rkey=%s'%( rkey_alt ", 29, 37), 1596: (u"s python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or No", 30, 37), 1966: (u"python:'Sort %s by Name'%( rkey_alt.upper() )", 38, 39), 2050: (u" python:'?skey=id&rkey=%s'%( rkey_alt ", 39, 37), 2128: (u"s python:request.get('skey',None)=='id' and 'zmi-sort_key' or No", 40, 37), 2807: (u"python:'Sort %s by File-Size'%( rkey_alt.upper() )", 51, 39), 2896: (u" python:'?skey=get_size&rkey=%s'%( rkey_alt ", 52, 37), 2980: (u"s python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or No", 53, 37), 3412: (u"python:'Sort %s by Modification Date'%( rkey_alt.upper() )", 62, 39), 3509: (u" python:'?skey=_p_mtime&rkey=%s'%( rkey_alt ", 63, 37), 3593: (u"s python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or No", 64, 37), 3895: (u'obs', 73, 34), 3933: (u'nocall:ob_dict/obj', 74, 32), 4167: (u'ob_dict/id', 76, 104), 4511: (u' ob/meta_type | defaul', 79, 122), 4483: (u'ob/zmi_icon | default', 79, 94), 4590: (u'ob/meta_type | default', 80, 53), 4757: (u"python:'%s/manage_workspace'%(ob_dict['id'])", 84, 40), 4841: (u'ob_dict/id', 85, 37), 4974: (u'ob/wl_isLocked | nothing', 86, 111), 5148: (u'ob/title|nothing', 89, 74), 5213: (u'ob/title', 90, 46), 5321: (u'python:context.externalEditLink_(ob)', 93, 42), 5522: (u'python:here.compute_size(ob)', 97, 76), 5654: (u'python:here.last_modified(ob)', 99, 81), 5855: (u"python:sm.checkPermission('Delete objects', context)", 107, 21), 5924: (u'obs', 107, 90), 5965: (u'not:context/dontAllowCopyAndPaste|nothing', 108, 35), 6228: (u'delete_allowed', 110, 114), 6469: (u'here/cb_dataValid', 112, 118), 6632: (u'delete_allowed', 114, 115), 6779: (u"python:sm.checkPermission('Import/Export objects', context)", 115, 128), 6956: (u"python: has_order_support and sm.checkPermission('Manage properties', context)", 118, 64), 7508: (u'python:range(1,min(5,len(obs)))', 125, 38), 7554: (u'val', 125, 84), 7600: (u'python:range(5,len(obs),5)', 126, 38), 7641: (u'val', 126, 79), 8081: (u'not:obs', 135, 26), 8195: (u'here/title_or_id', 137, 57), 8299: (u'not:context/dontAllowCopyAndPaste|nothing', 140, 35), 8461: (u'here/cb_dataValid', 141, 118), 8637: (u"python:sm.checkPermission('Import/Export objects', context)", 143, 128), 11569: (u'here/manage_page_footer', 240, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140241087907024 = __compile_zt_expr
_static_140240749874320 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Cut', u'name': u'manage_cutObjects:method', }
_static_140240896144464 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Delete', u'name': u'manage_delObjects:method', }
_static_140240779789072 = {u'class': u'badge badge-warning', u'title': u'This item has been locked by WebDAV', }
_static_140240781528656 = {u'type': u'checkbox', u'id': u'checkAll', u'onclick': u'checkbox_all();', }
_static_140241133802128 = {}
_static_140240758626000 = {u'title': u'Move selected items to bottom', u'type': u'submit', u'name': u'manage_move_objects_to_bottom:method', u'value': u'Move to bottom', u'class': u'btn btn-primary', }
_static_140240764050128 = {u'scope': u'col', u'class': u'zmi-object-id', }
_static_140240771338960 = {u'class': u'zmi-typename_show', }
_static_140240752319632 = {u'scope': u'col', u'class': u'zmi-object-size text-right hidden-xs', }
_static_140240763232912 = {u'class': u'zmi-object-title hidden-xs', }
_static_140240781386832 = {u'href': u'?skey=_p_mtime&rkey=asc', u'class': u"python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or None", u'title': u'Sort Ascending by Modification Date', }
_static_140240763666704 = {u'class': u'text-right zmi-object-date hidden-xs pl-3', }
_static_140240767225104 = {u'class': u'fa fa-search tablefilter', u'onclick': u"$('#tablefilter').focus()", }
_static_140240813725584 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Rename', u'name': u'manage_renameForm:method', }
_static_140240750885968 = {u'action': u'string:${request/URL1}/', u'name': u'objectItems', u'method': u'post', }
_static_140240782654224 = {u'class': u'container-fluid', }
_static_140241087907728 = __C2ZContextWrapper
_static_140240789375056 = {u'class': u'table table-striped table-hover table-sm objectItems', }
_static_140240605186064 = {u'scope': u'col', u'class': u'zmi-object-date text-right hidden-xs', }
_static_140240763232336 = {u'class': u'fa fa-lock', }
_static_140240767336144 = {u'scope': u'col', u'class': u'zmi-object-check text-right', }
_static_140240780687824 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Paste', u'name': u'manage_pasteObjects:method', }
_static_140240789374928 = {u'class': u'form-group zmi-controls', }
_static_140240604538256 = {u'title': u'Move selected items to top', u'type': u'submit', u'name': u'manage_move_objects_to_top:method', u'value': u'Move to top', u'class': u'btn btn-primary', }
_static_140240776555152 = {u'class': u'fa fa-sort', }
_static_140240780686416 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Import/Export', u'name': u'manage_importExportForm:method', }
_static_140240809812240 = {u'class': u'form-group row zmi-controls', }
_static_140240781526992 = {u'scope': u'col', u'class': u'zmi-object-type', }
_static_140240762492240 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Copy', u'name': u'manage_copyObjects:method', }
_static_140240605187600 = {u'class': u'fa fa-sort', }
_static_140240766772432 = {u'class': u'thead-light', }
_static_140240776230160 = {u'href': u'?skey=id&rkey=asc', u'class': u"python:request.get('skey',None)=='id' and 'zmi-sort_key' or None", u'title': u'Sort Ascending by Name', }
_static_140240604788688 = {u'href': u'?skey=get_size&rkey=asc', u'class': u"python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or None", u'title': u'Sort Ascending by File-Size', }
_static_140240809162448 = {u'class': u'btn btn-primary', u'type': u'submit', u'name': u'manage_move_objects_up:method', u'value': u'Move up', u'title': u'Move selected items up', }
_static_140240606532432 = {u'class': u'zmi-object-check text-right', u'onclick': u"$(this).children('input').trigger('click');", }
_static_140240803781200 = {u'class': u'form-control', u'name': u'delta:int', }
_static_140240780687696 = {u'class': u'form-group', }
_static_140240790298128 = {u'class': u'alert alert-info mt-4 mb-4', }
_static_140240752316496 = {u'title': u'Filter object list by entering a name. Pressing the Enter key starts recursive search.', u'type': u'text', u'id': u'tablefilter', u'name': u'obj_ids:tokens', }
_static_140240756017104 = {u'class': u'text-right zmi-object-size hidden-xs', }
_static_140240764556176 = {u'class': u'zmi-object-type', u'onclick': u"$(this).prev().children('input').trigger('click')", }
_static_140240609143504 = {u'class': u'zmi-object-id', }
_static_140240763800080 = {u'class': u'fa fa-sort', }
_static_140240759773456 = {u'class': u'btn btn-primary', u'type': u'submit', u'name': u'manage_move_objects_down:method', u'value': u'Move down', u'title': u'Move selected items down', }
_static_140240610149008 = {u'class': u'fa fa-sort', }
_static_140240764050576 = {u'href': u'?skey=meta_type&rkey=asc', u'class': u"python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None", u'title': u'Sort Ascending by Meta-Type', }
_static_140240609141200 = {u'class': u'sr-only', }
_static_140240813718160 = {u'class': u'container-fluid', }
_static_140240779872080 = {u'class': u'col-xs-2', }
_static_140240609142864 = {u'class': u'fas fa-ban text-danger', u'title': u'Broken object', }
_static_140240606534672 = {u'value': u'ob_dict/id', u'type': u'checkbox', u'class': u'checkbox-list-item', u'onclick': u"event.stopPropagation();$(this).parent().parent().toggleClass('checked');", u'name': u'ids:list', }
_static_140240906203088 = {u'href': u"python:'%s/manage_workspace'%(ob_dict['id'])", }
_static_140240765944272 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Paste', u'name': u'manage_pasteObjects:method', }
_static_140240809765456 = {u'type': u'submit', u'class': u'btn btn-primary', u'value': u'Import/Export', u'name': u'manage_importExportForm:method', }

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

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240750205904
            __attrs_140240750205904 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240750206288
            __default_140240750206288 = _DEFAULT_MARKER

            # <Value u'here/manage_page_header' (1:31)> -> __cache_140240606022672
            __token = 31
            try:
                __zt_tmp = __attrs_140240750205904
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240606022672 = _static_140241087907024('path', u'here/manage_page_header', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a35de10> -> __condition
            __expression = __cache_140240606022672

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240606022672
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240782653840
            __attrs_140240782653840 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240782654416
            __default_140240782654416 = _DEFAULT_MARKER

            # <Value u'here/manage_tabs' (3:29)> -> __cache_140240782652176
            __token = 89
            try:
                __zt_tmp = __attrs_140240782653840
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240782652176 = _static_140241087907024('path', u'here/manage_tabs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a087b90> -> __condition
            __expression = __cache_140240782652176

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240782652176
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c5a087b10> name=None at 7f8c5a0872d0> -> __attrs_140240778949584
            __attrs_140240778949584 = _static_140240782654224

            # <main ... (0:0)
            # --------------------------------------------------------
            __append(u'<main class="container-fluid">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8c5823bc50> name=None at 7f8c5823bdd0> -> __attrs_140240606442512
            __attrs_140240606442512 = _static_140240750885968
            __backup_has_order_support_140240750204816 = get('has_order_support', __marker)

            # <Value u"python:getattr(here.aq_explicit, 'has_order_support', 0)" (8:38)> -> __value
            __token = 229
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"getattr(here.aq_explicit, 'has_order_support', 0)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['has_order_support'] = __value
            __backup_sm_140240750206864 = get('sm', __marker)

            # <Value u'modules/AccessControl/getSecurityManager' (9:22)> -> __value
            __token = 309
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('path', u'modules/AccessControl/getSecurityManager', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['sm'] = __value
            __backup_default_sort_140240750884624 = get('default_sort', __marker)

            # <Value u"python: 'position' if has_order_support else 'id'" (10:31)> -> __value
            __token = 383
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u" 'position' if has_order_support else 'id'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['default_sort'] = __value
            __backup_skey_140240750884816 = get('skey', __marker)

            # <Value u"python:request.get('skey',default_sort)" (11:22)> -> __value
            __token = 458
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"request.get('skey',default_sort)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_140240750884432 = get('rkey', __marker)

            # <Value u"python:request.get('rkey','asc')" (12:21)> -> __value
            __token = 523
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"request.get('rkey','asc')", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_140240606441744 = get('rkey_alt', __marker)

            # <Value u"python:'desc' if rkey=='asc' else 'asc'" (13:24)> -> __value
            __token = 585
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u"'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_obs_140240606442640 = get('obs', __marker)

            # <Value u'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:18)> -> __value
            __token = 649
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140241087907024('python', u' here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            econtext['obs'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240750885904
            __default_140240750885904 = _DEFAULT_MARKER

            # <Substitution u'string:${request/URL1}/' (16:31)> -> __attr_action
            __token = 777
            try:
                __zt_tmp = __attrs_140240606442512
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140241087907024('string', u'${request/URL1}/', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240789374672
            __attrs_140240789374672 = _static_140241133802128

            # <Value u'obs' (18:30)> -> __condition
            __token = 834
            try:
                __zt_tmp = __attrs_140240789374672
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('path', u'obs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c5a6f0850> name=None at 7f8c5a6f08d0> -> __attrs_140240789374544
                __attrs_140240789374544 = _static_140240789375056

                # <Value u'obs' (19:89)> -> __condition
                __token = 929
                try:
                    __zt_tmp = __attrs_140240789374544
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'obs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<table class="table table-striped table-hover table-sm objectItems">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c591624d0> name=None at 7f8c59162050> -> __attrs_140240607976144
                    __attrs_140240607976144 = _static_140240766772432

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<thead')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240766774544
                    __default_140240766774544 = _DEFAULT_MARKER

                    # <Substitution u"python:'thead-light sorted_%s'%(request.get('rkey',''))" (20:57)> -> __attr_class
                    __token = 992
                    try:
                        __zt_tmp = __attrs_140240607976144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'thead-light', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240607974992
                    __attrs_140240607974992 = _static_140241133802128

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tr>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c591ebed0> name=None at 7f8c591eb2d0> -> __attrs_140240612171472
                    __attrs_140240612171472 = _static_140240767336144

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th scope="col" class="zmi-object-check text-right">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c59f74e50> name=None at 7f8c4fdf1450> -> __attrs_140240781527248
                    __attrs_140240781527248 = _static_140240781528656

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n            </th>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c59f747d0> name=None at 7f8c59f74e10> -> __attrs_140240764048784
                    __attrs_140240764048784 = _static_140240781526992

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th scope="col" class="zmi-object-type">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ec9c90> name=None at 7f8c58ec9850> -> __attrs_140240764048208
                    __attrs_140240764048208 = _static_140240764050576

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764048976
                    __default_140240764048976 = _DEFAULT_MARKER

                    # <Substitution u"python:'Sort %s by Meta-Type'%( rkey_alt.upper() )" (28:39)> -> __attr_title
                    __token = 1422
                    try:
                        __zt_tmp = __attrs_140240764048208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140241087907024('python', u"'Sort %s by Meta-Type'%( rkey_alt.upper() )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', u'Sort Ascending by Meta-Type', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764051344
                    __default_140240764051344 = _DEFAULT_MARKER

                    # <Substitution u"python:'?skey=meta_type&rkey=%s'%( rkey_alt )" (29:37)> -> __attr_href
                    __token = 1511
                    try:
                        __zt_tmp = __attrs_140240764048208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('python', u"'?skey=meta_type&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764049808
                    __default_140240764049808 = _DEFAULT_MARKER

                    # <Substitution u"python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None" (30:37)> -> __attr_class
                    __token = 1596
                    try:
                        __zt_tmp = __attrs_140240764048208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c59ab6a90> name=None at 7f8c59ab69d0> -> __attrs_140240776231696
                    __attrs_140240776231696 = _static_140240776555152

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ec9ad0> name=None at 7f8c58ec9250> -> __attrs_140240776231504
                    __attrs_140240776231504 = _static_140240764050128

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th scope="col" class="zmi-object-id">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c59a67510> name=None at 7f8c59a673d0> -> __attrs_140240763797776
                    __attrs_140240763797776 = _static_140240776230160

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240776231312
                    __default_140240776231312 = _DEFAULT_MARKER

                    # <Substitution u"python:'Sort %s by Name'%( rkey_alt.upper() )" (38:39)> -> __attr_title
                    __token = 1966
                    try:
                        __zt_tmp = __attrs_140240763797776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140241087907024('python', u"'Sort %s by Name'%( rkey_alt.upper() )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', u'Sort Ascending by Name', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604881040
                    __default_140240604881040 = _DEFAULT_MARKER

                    # <Substitution u"python:'?skey=id&rkey=%s'%( rkey_alt )" (39:37)> -> __attr_href
                    __token = 2050
                    try:
                        __zt_tmp = __attrs_140240763797776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('python', u"'?skey=id&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'?skey=id&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240763799248
                    __default_140240763799248 = _DEFAULT_MARKER

                    # <Substitution u"python:request.get('skey',None)=='id' and 'zmi-sort_key' or None" (40:37)> -> __attr_class
                    __token = 2128
                    try:
                        __zt_tmp = __attrs_140240763797776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"request.get('skey',None)=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n                Name\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c58e8ca10> name=None at 7f8c58e8ce90> -> __attrs_140240790920528
                    __attrs_140240790920528 = _static_140240763800080

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-sort"></i>\n              </a>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c591d0d10> name=None at 7f8c5a869710> -> __attrs_140240767223248
                    __attrs_140240767223248 = _static_140240767225104

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-search tablefilter" onclick="$(\'#tablefilter\').focus()"></i>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c58399050> name=None at 7f8c58399b90> -> __attrs_140240752316880
                    __attrs_140240752316880 = _static_140240752316496

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input id="tablefilter" name="obj_ids:tokens" type="text" title="Filter object list by entering a name. Pressing the Enter key starts recursive search." />\n            </th>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c58399c90> name=None at 7f8c58399390> -> __attrs_140240764291536
                    __attrs_140240764291536 = _static_140240752319632

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th scope="col" class="zmi-object-size text-right hidden-xs">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c4f6e77d0> name=None at 7f8c4f6e7c10> -> __attrs_140240605185872
                    __attrs_140240605185872 = _static_140240604788688

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604790608
                    __default_140240604790608 = _DEFAULT_MARKER

                    # <Substitution u"python:'Sort %s by File-Size'%( rkey_alt.upper() )" (51:39)> -> __attr_title
                    __token = 2807
                    try:
                        __zt_tmp = __attrs_140240605185872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140241087907024('python', u"'Sort %s by File-Size'%( rkey_alt.upper() )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', u'Sort Ascending by File-Size', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604789648
                    __default_140240604789648 = _DEFAULT_MARKER

                    # <Substitution u"python:'?skey=get_size&rkey=%s'%( rkey_alt )" (52:37)> -> __attr_href
                    __token = 2896
                    try:
                        __zt_tmp = __attrs_140240605185872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('python', u"'?skey=get_size&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'?skey=get_size&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240604790224
                    __default_140240604790224 = _DEFAULT_MARKER

                    # <Substitution u"python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or None" (53:37)> -> __attr_class
                    __token = 2980
                    try:
                        __zt_tmp = __attrs_140240605185872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"request.get('skey',None)=='get_size' and 'zmi-sort_key' or None", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n                Size\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c4f748e10> name=None at 7f8c4f748490> -> __attrs_140240605186768
                    __attrs_140240605186768 = _static_140240605187600

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c4f748810> name=None at 7f8c4f748b50> -> __attrs_140240781386896
                    __attrs_140240781386896 = _static_140240605186064

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<th scope="col" class="zmi-object-date text-right hidden-xs">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c59f52450> name=None at 7f8c59f52050> -> __attrs_140240610152144
                    __attrs_140240610152144 = _static_140240781386832

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610151376
                    __default_140240610151376 = _DEFAULT_MARKER

                    # <Substitution u"python:'Sort %s by Modification Date'%( rkey_alt.upper() )" (62:39)> -> __attr_title
                    __token = 3412
                    try:
                        __zt_tmp = __attrs_140240610152144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140241087907024('python', u"'Sort %s by Modification Date'%( rkey_alt.upper() )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', u'Sort Ascending by Modification Date', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610151760
                    __default_140240610151760 = _DEFAULT_MARKER

                    # <Substitution u"python:'?skey=_p_mtime&rkey=%s'%( rkey_alt )" (63:37)> -> __attr_href
                    __token = 3509
                    try:
                        __zt_tmp = __attrs_140240610152144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140241087907024('python', u"'?skey=_p_mtime&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'?skey=_p_mtime&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610151952
                    __default_140240610151952 = _DEFAULT_MARKER

                    # <Substitution u"python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or None" (64:37)> -> __attr_class
                    __token = 3593
                    try:
                        __zt_tmp = __attrs_140240610152144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140241087907024('python', u"request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or None", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n                Last Modified\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8c4fc04290> name=None at 7f8c4fc04950> -> __attrs_140240610151056
                    __attrs_140240610151056 = _static_140240610149008

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<i class="fa fa-sort"></i>\n              </a>\n            </th>\n          </tr>\n        </thead>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240781387920
                    __attrs_140240781387920 = _static_140241133802128

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tbody>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240610149136
                    __attrs_140240610149136 = _static_140241133802128
                    __backup_ob_dict_140240789376208 = get('ob_dict', __marker)

                    # <Value u'obs' (73:34)> -> __iterator
                    __token = 3895
                    try:
                        __zt_tmp = __attrs_140240610149136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('path', u'obs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240610149712, ) = getitem('repeat')(u'ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<tr>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240610148816
                        __attrs_140240610148816 = _static_140241133802128
                        __backup_ob_140240607977424 = get('ob', __marker)

                        # <Value u'nocall:ob_dict/obj' (74:32)> -> __value
                        __token = 3933
                        try:
                            __zt_tmp = __attrs_140240610148816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140241087907024('nocall', u'ob_dict/obj', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        econtext['ob'] = __value
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c4f891350> name=None at 7f8c4f891f10> -> __attrs_140240606532816
                        __attrs_140240606532816 = _static_140240606532432

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c4f891c10> name=None at 7f8c4f891910> -> __attrs_140240764556880
                        __attrs_140240764556880 = _static_140240606534672

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="checkbox" class="checkbox-list-item" name="ids:list" onclick="event.stopPropagation();$(this).parent().parent().toggleClass(\'checked\');"')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240764558416
                        __default_140240764558416 = _DEFAULT_MARKER

                        # <Substitution u'ob_dict/id' (76:104)> -> __attr_value
                        __token = 4167
                        try:
                            __zt_tmp = __attrs_140240764556880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140241087907024('path', u'ob_dict/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' />\n              </td>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c58f45390> name=None at 7f8c5bb77f90> -> __attrs_140240764556432
                        __attrs_140240764556432 = _static_140240764556176

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="zmi-object-type" onclick="$(this).prev().children(\'input\').trigger(\'click\')">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c4fb0e850> name=None at 7f8c4fb0e310> -> __attrs_140240609143056
                        __attrs_140240609143056 = _static_140240609142864

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<i')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240609141840
                        __default_140240609141840 = _DEFAULT_MARKER

                        # <Substitution u'ob/meta_type | default' (79:122)> -> __attr_title
                        __token = 4511
                        try:
                            __zt_tmp = __attrs_140240609143056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140241087907024('path', u'ob/meta_type | default', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', u'Broken object', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240609143568
                        __default_140240609143568 = _DEFAULT_MARKER

                        # <Substitution u'ob/zmi_icon | default' (79:94)> -> __attr_class
                        __token = 4483
                        try:
                            __zt_tmp = __attrs_140240609143056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140241087907024('path', u'ob/zmi_icon | default', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'fas fa-ban text-danger', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c4fb0e1d0> name=None at 7f8c4fb0e250> -> __attrs_140240609144272
                        __attrs_140240609144272 = _static_140240609141200

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="sr-only">')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240609142928
                        __default_140240609142928 = _DEFAULT_MARKER

                        # <Value u'ob/meta_type | default' (80:53)> -> __cache_140240609142544
                        __token = 4590
                        try:
                            __zt_tmp = __attrs_140240609144272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240609142544 = _static_140241087907024('path', u'ob/meta_type | default', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'ob/meta_type | default' (80:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4fb0e810> -> __condition
                        __expression = __cache_140240609142544

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Broken object')
                        else:
                            __content = __cache_140240609142544
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                </i>\n              </td>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c4fb0ead0> name=None at 7f8c4fb0e3d0> -> __attrs_140240906621264
                        __attrs_140240906621264 = _static_140240609143504

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="zmi-object-id">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c6165afd0> name=None at 7f8c6165af50> -> __attrs_140240779788752
                        __attrs_140240779788752 = _static_140240906203088

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779788368
                        __default_140240779788368 = _DEFAULT_MARKER

                        # <Substitution u"python:'%s/manage_workspace'%(ob_dict['id'])" (84:40)> -> __attr_href
                        __token = 4757
                        try:
                            __zt_tmp = __attrs_140240779788752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140241087907024('python', u"'%s/manage_workspace'%(ob_dict['id'])", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240779789520
                        __attrs_140240779789520 = _static_140241133802128

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240779789648
                        __default_140240779789648 = _DEFAULT_MARKER

                        # <Value u'ob_dict/id' (85:37)> -> __cache_140240779791312
                        __token = 4841
                        try:
                            __zt_tmp = __attrs_140240779789520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240779791312 = _static_140241087907024('path', u'ob_dict/id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'ob_dict/id' (85:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c59dcced0> -> __condition
                        __expression = __cache_140240779791312

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>Id</span>')
                        else:
                            __content = __cache_140240779791312
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c59dcc310> name=None at 7f8c59dcc650> -> __attrs_140240763235472
                        __attrs_140240763235472 = _static_140240779789072

                        # <Value u'ob/wl_isLocked | nothing' (86:111)> -> __condition
                        __token = 4974
                        try:
                            __zt_tmp = __attrs_140240763235472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('path', u'ob/wl_isLocked | nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="badge badge-warning" title="This item has been locked by WebDAV">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8c58e02050> name=None at 7f8c58e02b50> -> __attrs_140240763233744
                            __attrs_140240763233744 = _static_140240763232336

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<i class="fa fa-lock"></i>\n                  </span>')
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8c58e02290> name=None at 7f8c58e02490> -> __attrs_140240759947600
                        __attrs_140240759947600 = _static_140240763232912

                        # <Value u'ob/title|nothing' (89:74)> -> __condition
                        __token = 5148
                        try:
                            __zt_tmp = __attrs_140240759947600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('path', u'ob/title|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="zmi-object-title hidden-xs">\n                    &nbsp;(')

                            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240610329296
                            __attrs_140240610329296 = _static_140241133802128

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610330512
                            __default_140240610330512 = _DEFAULT_MARKER

                            # <Value u'ob/title' (90:46)> -> __cache_140240610331536
                            __token = 5213
                            try:
                                __zt_tmp = __attrs_140240610329296
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140240610331536 = _static_140241087907024('path', u'ob/title', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                            # <BinOp left=<Value u'ob/title' (90:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4fc30650> -> __condition
                            __expression = __cache_140240610331536

                            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span></span>')
                            else:
                                __content = __cache_140240610331536
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u')\n                  </span>')
                        __append(u'\n                </a>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240610331344
                        __attrs_140240610331344 = _static_140241133802128

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610331088
                        __default_140240610331088 = _DEFAULT_MARKER

                        # <Value u'python:context.externalEditLink_(ob)' (93:42)> -> __cache_140240610331728
                        __token = 5321
                        try:
                            __zt_tmp = __attrs_140240610331344
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240610331728 = _static_140241087907024('python', u'context.externalEditLink_(ob)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:context.externalEditLink_(ob)' (93:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4fc306d0> -> __condition
                        __expression = __cache_140240610331728

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<a>\n                  Edit using external editor\n                </a>')
                        else:
                            __content = __cache_140240610331728
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n              </td>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c587207d0> name=None at 7f8c4fc30b50> -> __attrs_140240884352400
                        __attrs_140240884352400 = _static_140240756017104

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="text-right zmi-object-size hidden-xs">')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240610330960
                        __default_140240610330960 = _DEFAULT_MARKER

                        # <Value u'python:here.compute_size(ob)' (97:76)> -> __cache_140240606535056
                        __token = 5522
                        try:
                            __zt_tmp = __attrs_140240884352400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240606535056 = _static_140241087907024('python', u'here.compute_size(ob)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:here.compute_size(ob)' (97:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c4fc300d0> -> __condition
                        __expression = __cache_140240606535056

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              ')
                        else:
                            __content = __cache_140240606535056
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</td>\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8c58e6c110> name=None at 7f8c58e6cf50> -> __attrs_140240897003024
                        __attrs_140240897003024 = _static_140240763666704

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<td class="text-right zmi-object-date hidden-xs pl-3">')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240763669712
                        __default_140240763669712 = _DEFAULT_MARKER

                        # <Value u'python:here.last_modified(ob)' (99:81)> -> __cache_140240757974352
                        __token = 5654
                        try:
                            __zt_tmp = __attrs_140240897003024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240757974352 = _static_140241087907024('python', u'here.last_modified(ob)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'python:here.last_modified(ob)' (99:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c589dbfd0> -> __condition
                        __expression = __cache_140240757974352

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              ')
                        else:
                            __content = __cache_140240757974352
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</td>\n            ')
                        if (__backup_ob_140240607977424 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_140240607977424
                        __append(u'\n          </tr>')
                        ____index_140240610149712 -= 1
                        if (____index_140240610149712 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_140240789376208 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_140240789376208
                    __append(u'\n        </tbody>\n      </table>')
                __append(u'\n\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c5a6f07d0> name=None at 7f8c5a6f0ed0> -> __attrs_140240609142608
                __attrs_140240609142608 = _static_140240789374928
                __backup_delete_allowed_140240750886160 = get('delete_allowed', __marker)

                # <Value u"python:sm.checkPermission('Delete objects', context)" (107:21)> -> __value
                __token = 5855
                try:
                    __zt_tmp = __attrs_140240609142608
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140241087907024('python', u"sm.checkPermission('Delete objects', context)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                econtext['delete_allowed'] = __value

                # <Value u'obs' (107:90)> -> __condition
                __token = 5924
                try:
                    __zt_tmp = __attrs_140240609142608
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('path', u'obs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="form-group zmi-controls">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240813725520
                    __attrs_140240813725520 = _static_140241133802128

                    # <Value u'not:context/dontAllowCopyAndPaste|nothing' (108:35)> -> __condition
                    __token = 5965
                    try:
                        __zt_tmp = __attrs_140240813725520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('not', u'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8c5be29790> name=None at 7f8c5be29c50> -> __attrs_140240749873488
                        __attrs_140240749873488 = _static_140240813725584

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="btn btn-primary" type="submit" name="manage_renameForm:method" value="Rename" />\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8c58144c90> name=None at 7f8c58144b50> -> __attrs_140240762493904
                        __attrs_140240762493904 = _static_140240749874320

                        # <Value u'delete_allowed' (110:114)> -> __condition
                        __token = 6228
                        try:
                            __zt_tmp = __attrs_140240762493904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('path', u'delete_allowed', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input class="btn btn-primary" type="submit" name="manage_cutObjects:method" value="Cut" />')
                        __append(u'\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8c58d4d550> name=None at 7f8c58d4d590> -> __attrs_140240765944912
                        __attrs_140240765944912 = _static_140240762492240

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="btn btn-primary" type="submit" name="manage_copyObjects:method" value="Copy" />\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8c590981d0> name=None at 7f8c59098190> -> __attrs_140240764914256
                        __attrs_140240764914256 = _static_140240765944272

                        # <Value u'here/cb_dataValid' (112:118)> -> __condition
                        __token = 6469
                        try:
                            __zt_tmp = __attrs_140240764914256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140241087907024('path', u'here/cb_dataValid', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                        __append(u'\n        ')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c60cc3450> name=None at 7f8c60cc3a50> -> __attrs_140240768292496
                    __attrs_140240768292496 = _static_140240896144464

                    # <Value u'delete_allowed' (114:115)> -> __condition
                    __token = 6632
                    try:
                        __zt_tmp = __attrs_140240768292496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'delete_allowed', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="btn btn-primary" type="submit" name="manage_delObjects:method" value="Delete" />')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8c5ba62a50> name=None at 7f8c592d5790> -> __attrs_140240811339472
                    __attrs_140240811339472 = _static_140240809765456

                    # <Value u"python:sm.checkPermission('Import/Export objects', context)" (115:128)> -> __condition
                    __token = 6779
                    try:
                        __zt_tmp = __attrs_140240811339472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('python', u"sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                    __append(u'\n      </div>')
                if (__backup_delete_allowed_140240750886160 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_140240750886160
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c5be27a90> name=None at 7f8c60db3bd0> -> __attrs_140240813717264
                __attrs_140240813717264 = _static_140240813718160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="container-fluid">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c5ba6e110> name=None at 7f8c5ba6eb90> -> __attrs_140240809814032
                __attrs_140240809814032 = _static_140240809812240

                # <Value u"python: has_order_support and sm.checkPermission('Manage properties', context)" (118:64)> -> __condition
                __token = 6956
                try:
                    __zt_tmp = __attrs_140240809814032
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u" has_order_support and sm.checkPermission('Manage properties', context)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="form-group row zmi-controls">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c5b9cf6d0> name=None at 7f8c5b9cf710> -> __attrs_140240787902352
                    __attrs_140240787902352 = _static_140240809162448

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="submit" name="manage_move_objects_up:method" value="Move up" title="Move selected items up" class="btn btn-primary" />\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240759774352
                    __attrs_140240759774352 = _static_140241133802128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>/</span>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c58ab5910> name=None at 7f8c58ab5650> -> __attrs_140240779871056
                    __attrs_140240779871056 = _static_140240759773456

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="submit" name="manage_move_objects_down:method" value="Move down" title="Move selected items down" class="btn btn-primary" />\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240779872016
                    __attrs_140240779872016 = _static_140241133802128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>by</span>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c59de0750> name=None at 7f8c59de0790> -> __attrs_140240604538064
                    __attrs_140240604538064 = _static_140240779872080

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="col-xs-2">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8c5b4ada50> name=None at 7f8c5b4ad810> -> __attrs_140240803779152
                    __attrs_140240803779152 = _static_140240803781200

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<select class="form-control" name="delta:int">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240749520464
                    __attrs_140240749520464 = _static_140241133802128
                    __backup_val_140240789374224 = get('val', __marker)

                    # <Value u'python:range(1,min(5,len(obs)))' (125:38)> -> __iterator
                    __token = 7508
                    try:
                        __zt_tmp = __attrs_140240749520464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('python', u'range(1,min(5,len(obs)))', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240749520976, ) = getitem('repeat')(u'val', __iterator)
                    econtext['val'] = None
                    for __item in __iterator:
                        econtext['val'] = __item

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240772705424
                        __default_140240772705424 = _DEFAULT_MARKER

                        # <Value u'val' (125:84)> -> __cache_140240772705040
                        __token = 7554
                        try:
                            __zt_tmp = __attrs_140240749520464
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240772705040 = _static_140241087907024('path', u'val', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'val' (125:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5970a890> -> __condition
                        __expression = __cache_140240772705040

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240772705040
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>')
                        ____index_140240749520976 -= 1
                        if (____index_140240749520976 > 0):
                            __append('\n              ')
                    if (__backup_val_140240789374224 is __marker):
                        del econtext['val']
                    else:
                        econtext['val'] = __backup_val_140240789374224
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240749521296
                    __attrs_140240749521296 = _static_140241133802128
                    __backup_val_140240606535120 = get('val', __marker)

                    # <Value u'python:range(5,len(obs),5)' (126:38)> -> __iterator
                    __token = 7600
                    try:
                        __zt_tmp = __attrs_140240749521296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140241087907024('python', u'range(5,len(obs),5)', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    (__iterator, ____index_140240749521488, ) = getitem('repeat')(u'val', __iterator)
                    econtext['val'] = None
                    for __item in __iterator:
                        econtext['val'] = __item

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<option>')

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240749522768
                        __default_140240749522768 = _DEFAULT_MARKER

                        # <Value u'val' (126:79)> -> __cache_140240749520528
                        __token = 7641
                        try:
                            __zt_tmp = __attrs_140240749521296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140240749520528 = _static_140241087907024('path', u'val', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                        # <BinOp left=<Value u'val' (126:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c580ee510> -> __condition
                        __expression = __cache_140240749520528

                        # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140240749520528
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</option>')
                        ____index_140240749521488 -= 1
                        if (____index_140240749521488 > 0):
                            __append('\n              ')
                    if (__backup_val_140240606535120 is __marker):
                        del econtext['val']
                    else:
                        econtext['val'] = __backup_val_140240606535120
                    __append(u'\n            </select>\n          </div>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c4f6aa590> name=None at 7f8c4f6aa950> -> __attrs_140240758624592
                    __attrs_140240758624592 = _static_140240604538256

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="submit" name="manage_move_objects_to_top:method" value="Move to top" class="btn btn-primary" title="Move selected items to top" />\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c5899d6d0> name=None at 7f8c5899d710> -> __attrs_140240758624464
                    __attrs_140240758624464 = _static_140240758626000

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="submit" name="manage_move_objects_to_bottom:method" value="Move to bottom" class="btn btn-primary" title="Move selected items to bottom" />\n        </div>')
                __append(u'\n      </div>\n    ')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240789375888
            __attrs_140240789375888 = _static_140241133802128

            # <Value u'not:obs' (135:26)> -> __condition
            __token = 8081
            try:
                __zt_tmp = __attrs_140240789375888
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140241087907024('not', u'obs', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
            if __condition:
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c5a7d1e10> name=None at 7f8c5a7d15d0> -> __attrs_140240790298448
                __attrs_140240790298448 = _static_140240790298128

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="alert alert-info mt-4 mb-4">\n        There are currently no items in ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240780687056
                __attrs_140240780687056 = _static_140241133802128

                # <em ... (0:0)
                # --------------------------------------------------------
                __append(u'<em>')

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240790294672
                __default_140240790294672 = _DEFAULT_MARKER

                # <Value u'here/title_or_id' (137:57)> -> __cache_140240790294928
                __token = 8195
                try:
                    __zt_tmp = __attrs_140240780687056
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140240790294928 = _static_140241087907024('path', u'here/title_or_id', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

                # <BinOp left=<Value u'here/title_or_id' (137:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c5a7d1150> -> __condition
                __expression = __cache_140240790294928

                # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140240790294928
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</em>.\n      </div>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8c59ea7950> name=None at 7f8c59ea7550> -> __attrs_140240780688528
                __attrs_140240780688528 = _static_140240780687696

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="form-group">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240780688336
                __attrs_140240780688336 = _static_140241133802128

                # <Value u'not:context/dontAllowCopyAndPaste|nothing' (140:35)> -> __condition
                __token = 8299
                try:
                    __zt_tmp = __attrs_140240780688336
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('not', u'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8c59ea79d0> name=None at 7f8c59ea74d0> -> __attrs_140240612746704
                    __attrs_140240612746704 = _static_140240780687824

                    # <Value u'here/cb_dataValid' (141:118)> -> __condition
                    __token = 8461
                    try:
                        __zt_tmp = __attrs_140240612746704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140241087907024('path', u'here/cb_dataValid', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                    __append(u'\n        ')
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8c59ea7450> name=None at 7f8c59ea7390> -> __attrs_140240612747856
                __attrs_140240612747856 = _static_140240780686416

                # <Value u"python:sm.checkPermission('Import/Export objects', context)" (143:128)> -> __condition
                __token = 8637
                try:
                    __zt_tmp = __attrs_140240612747856
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140241087907024('python', u"sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                __append(u'\n      </div>\n    ')
            __append(u'\n  </form>')
            if (__backup_obs_140240606442640 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_140240606442640
            if (__backup_rkey_alt_140240606441744 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_140240606441744
            if (__backup_rkey_140240750884432 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_140240750884432
            if (__backup_skey_140240750884816 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_140240750884816
            if (__backup_default_sort_140240750884624 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_140240750884624
            if (__backup_sm_140240750206864 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_140240750206864
            if (__backup_has_order_support_140240750204816 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_140240750204816
            __append(u'\n</main>\n\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240813725200
            __attrs_140240813725200 = _static_140241133802128

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script>\n  // +++++++++++++++++++++++++++\n  // checkbox_all: Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById(\'checkAll\').checked) {\n      $(\'table.objectItems tbody tr\').addClass(\'checked\');\n    } else {\n      $(\'table.objectItems tbody tr\').removeClass(\'checked\');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<_ast.Dict object at 0x7f8c595bd2d0> name=None at 7f8c595bd290> -> __attrs_140240771339600
            __attrs_140240771339600 = _static_140240771338960

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="zmi-typename_show">\' + $(this).text() + \'</span>\')\n      });\n      $(\'th.zmi-object-id\').addClass(\'zmi-typename_show\');\n    }\n\n  });\n\n</script>\n\n')

            # <Static value=<_ast.Dict object at 0x7f8c6ef69290> name=None at 7f8c6ef69190> -> __attrs_140240771340304
            __attrs_140240771340304 = _static_140241133802128

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __default_140240771340176
            __default_140240771340176 = _DEFAULT_MARKER

            # <Value u'here/manage_page_footer' (240:31)> -> __cache_140240771339856
            __token = 11569
            try:
                __zt_tmp = __attrs_140240771340304
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140240771339856 = _static_140241087907024('path', u'here/manage_page_footer', econtext=econtext)(_static_140241087907728(econtext, __zt_tmp))

            # <BinOp left=<Value u'here/manage_page_footer' (240:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8c6ef693d0> at 7f8c595bd6d0> -> __condition
            __expression = __cache_140240771339856

            # <Symbol value=<DEFAULT> at 7f8c6ef693d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140240771339856
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }