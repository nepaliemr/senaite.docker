# -*- coding: utf-8 -*-
__filename = '/home/senaite/senaitelims/eggs/cp27mu/plone.app.discussion-3.4.7-py2.7.egg/plone/app/discussion/browser/comments.pt'

__tokens = {46: (u'view/can_reply', 1, 46), 104: (u' view/is_discussion_allowe', 2, 42), 183: (u'd view/anonymous_discussion_allow', 3, 50), 261: (u'ed view/edit_comment_allo', 4, 41), 336: (u'wed view/delete_own_comment_all', 5, 45), 398: (u'Anon view/is_anon', 6, 25), 449: (u'eview view/can_', 7, 27), 496: (u'eplies python:view.get_replies(can', 8, 24), 566: (u'replies python:view.has_replies(ca', 9, 27), 643: (u'terImage view/show_commen', 10, 33), 699: (u'   errors options/state/getErro', 11, 20), 760: (u'     wtool context/@@plone_too', 12, 18), 825: (u' auth_token context/@@authenticator/t', 13, 22), 902: (u'python:isDiscussionAllowed or has_replies', 14, 26), 1025: (u'python:isAnon and not isAnonymousDiscussionAllowed', 18, 24), 1115: (u'view/login_action', 19, 37), 1554: (u'has_replies', 30, 24), 1449: (u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'", 29, 31), 1611: (u'replies', 31, 43), 1690: (u'reply_dict/comment', 34, 35), 1749: (u' reply/getI', 35, 39), 1796: (u'h reply_dict/depth|python', 36, 33), 1857: (u"th python: depth > 10 and '10' or de", 37, 32), 1939: (u'url python:view.get_commenter_home_url(username=reply.author_usern', 38, 41), 2051: (u'link python:author_home_url and not i', 39, 40), 2131: (u't_url python:view.get_commenter_portrait(reply.author_use', 40, 36), 2231: (u"_state python:wtool.getInfoFor(reply, 'review_state', ", 41, 35), 2323: (u'canEdit python:view.can_edi', 42, 29), 2390: (u'anDelete python:view.can_dele', 43, 30), 2460: (u"olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 44, 30), 2795: (u"python:canReview or review_state == 'published'", 47, 32), 2614: (u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 45, 39), 2750: (u' comment_i', 46, 35), 2903: (u'showCommenterImage', 49, 57), 2970: (u'has_author_link', 50, 46), 3039: (u'author_home_url', 51, 52), 3291: (u'portrait_url', 56, 50), 3354: (u' reply/author_nam', 57, 49), 3606: (u'not: has_author_link', 63, 40), 3673: (u'portrait_url', 64, 45), 3731: (u' reply/author_nam', 65, 44), 3931: (u'has_author_link', 71, 42), 4055: (u'author_home_url', 73, 48), 3988: (u'reply/author_name', 72, 40), 4187: (u'not: has_author_link', 76, 45), 4252: (u'reply/author_name', 77, 43), 4319: (u'not: reply/author_name', 78, 45), 4617: (u'python:view.format_time(reply.modification_date)', 83, 38), 4858: (u'reply/getText', 90, 49), 5156: (u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 97, 45), 5294: (u'string:${reply/absolute_url}/@@delete-own-comment', 98, 53), 5396: (u" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 99, 51), 5520: (u'd string:delete-${comment_i', 100, 47), 6147: (u'python:canDelete', 112, 45), 6218: (u'string:${reply/absolute_url}/@@moderate-delete-comment', 113, 53), 6322: (u' string:delete-${comment_id', 114, 48), 6768: (u'python:isEditCommentAllowed and canEdit', 123, 49), 7066: (u'auth_token', 127, 44), 7128: (u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 128, 50), 7499: (u'not: auth_token', 134, 47), 7571: (u'string:${reply/absolute_url}/@@edit-comment', 135, 55), 7666: (u' string:edit-${comment_id', 136, 50), 8392: (u'canReview', 152, 45), 8452: (u'reply_dict/actions|nothing', 153, 49), 8632: (u' action/i', 155, 50), 8533: (u'string:${reply/absolute_url}/@@transmit-comment', 154, 53), 8691: (u'd string:${action/id}-${comment_i', 156, 47), 8823: (u'action/id', 157, 94), 9064: (u'action/title', 161, 57), 9384: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 170, 39), 9665: (u'python: has_replies and not isDiscussionAllowed', 178, 28), 9918: (u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 187, 24), 10026: (u'view/login_action', 188, 37), 10355: (u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 197, 54), 10581: (u'view/comment_transform_message', 202, 28), 10780: (u'view/form/render', 207, 40)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140574257290256 = {u'type': u'submit', u'name': u'form.button.TransmitComment', u'value': u'action/title', u'class': u'context', }
_static_140574270390800 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140574284377488 = {u'class': u'discreet', }
_static_140574284377296 = {u'class': u'comment', u'id': u'comment_id', }
_static_140574270562960 = {u'type': u'submit', u'name': u'form.button.EditComment', u'value': u'Edit', u'class': u'context', }
_static_140574268941968 = {u'href': u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', u'class': u'pat-plone-modal context commentactionsform', }
_static_140574257195088 = {u'class': u'reply', }
_static_140574268020240 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140574269062736 = {u'id': u'commenting', u'class': u'reply', }
_static_140574270567760 = {u'action': u'view/login_action', }
_static_140574397981968 = __compile_zt_expr
_static_140574442558096 = {}
_static_140574269060112 = {u'action': u'view/login_action', }
_static_140574284438864 = {u'class': u'commentActions', }
_static_140574269060752 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140574284437264 = {u'style': u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", u'name': u'delete', u'id': u'string:delete-${comment_id}', u'method': u'post', u'action': u'', u'class': u'commentactionsform', }
_static_140574268058512 = {u'class': u'commentDate', }
_static_140574270171088 = {u'type': u'hidden', u'name': u'workflow_action', u'value': u'action/id', }
_static_140574266193552 = {u'class': u'commentImage', }
_static_140574284482192 = {u'class': u'documentByLine', }
_static_140574268919312 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:edit-${comment_id}', u'name': u'edit', u'method': u'get', }
_static_140574268021456 = {u'href': u'', }
_static_140574397982672 = __C2ZContextWrapper
_static_140574266171088 = {u'href': u'', }
_static_140574270167504 = {u'class': u'reply', }
_static_140574268943632 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:${action/id}-${comment_id}', u'name': u'', u'method': u'get', }
_static_140574270569744 = {u'class': u'discussion', }
_static_140574270452752 = {u'type': u'submit', u'name': u'form.button.DeleteComment', u'value': u'Delete', u'class': u'destructive', }
_static_140574268915856 = {u'class': u'context reply-to-comment-button hide allowMultiSubmit', }
_static_140574284483280 = {u'src': u'defaultUser.png', u'alt': u'', u'class': u'defaultuserimg', u'height': u'32', }
_static_140574270453264 = {u'action': u'', u'class': u'commentactionsform', u'id': u'string:delete-${comment_id}', u'name': u'delete', u'method': u'post', }
_static_140574270570064 = {u'type': u'submit', u'class': u'standalone loginbutton', u'value': u'Log in to add comments', }
_static_140574284441936 = {u'class': u'commentBody', }

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

            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270209232
            __attrs_140574270209232 = _static_140574442558096
            __backup_userHasReplyPermission_140574270567888 = get('userHasReplyPermission', __marker)

            # <Value u'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/can_reply', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_140574270569680 = get('isDiscussionAllowed', __marker)

            # <Value u'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/is_discussion_allowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_140574270346768 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value u'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/anonymous_discussion_allowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_140574270170000 = get('isEditCommentAllowed', __marker)

            # <Value u'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/edit_comment_allowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_140574270457424 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value u'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/delete_own_comment_allowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_140574268944144 = get('isAnon', __marker)

            # <Value u'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/is_anonymous', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_140574284475216 = get('canReview', __marker)

            # <Value u'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/can_review', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_140574270453456 = get('replies', __marker)

            # <Value u'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.get_replies(canReview)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_140574257263888 = get('has_replies', __marker)

            # <Value u'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('python', u'view.has_replies(canReview)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_140574268984144 = get('showCommenterImage', __marker)

            # <Value u'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'view/show_commenter_image', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_140574270165200 = get('errors', __marker)

            # <Value u'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'options/state/getErrors|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_140574270364816 = get('wtool', __marker)

            # <Value u'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@plone_tools/workflow', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_140574266167632 = get('auth_token', __marker)

            # <Value u'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140574397981968('path', u'context/@@authenticator/token|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value u'python:isDiscussionAllowed or has_replies' (14:26)> -> __condition
            __token = 902
            try:
                __zt_tmp = __attrs_140574270209232
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140574397981968('python', u'isDiscussionAllowed or has_replies', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140574270167632 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff7019d0> name=None at 7fd9ff701150> -> __attrs_140574270168464
                __attrs_140574270168464 = _static_140574270167504

                # <Value u'python:isAnon and not isAnonymousDiscussionAllowed' (18:24)> -> __condition
                __token = 1025
                try:
                    __zt_tmp = __attrs_140574270168464
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff763550> name=None at 7fd9ff763690> -> __attrs_140574270569296
                    __attrs_140574270569296 = _static_140574270567760

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270568784
                    __default_140574270568784 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (19:37)> -> __attr_action
                    __token = 1115
                    try:
                        __zt_tmp = __attrs_140574270569296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140574397981968('path', u'view/login_action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff763e50> name=None at 7fd9ff763a10> -> __attrs_140574284387792
                    __attrs_140574284387792 = _static_140574270570064

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284389072
                    __default_140574284389072 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7fda004a3ad0> at 7fda004a3990> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff763d10> name=None at 7fd9ff763d90> -> __attrs_140574284387152
                __attrs_140574284387152 = _static_140574270569744

                # <Value u'has_replies' (30:24)> -> __condition
                __token = 1554
                try:
                    __zt_tmp = __attrs_140574284387152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('path', u'has_replies', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284386768
                    __default_140574284386768 = _DEFAULT_MARKER

                    # <Substitution u"python: showCommenterImage and 'discussion showCommenterImage' or 'discussion'" (29:31)> -> __attr_class
                    __token = 1449
                    try:
                        __zt_tmp = __attrs_140574284387152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140574397981968('python', u" showCommenterImage and 'discussion showCommenterImage' or 'discussion'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', u'discussion', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284375760
                    __attrs_140574284375760 = _static_140574442558096
                    __backup_reply_dict_140574270394832 = get('reply_dict', __marker)

                    # <Value u'replies' (31:43)> -> __iterator
                    __token = 1611
                    try:
                        __zt_tmp = __attrs_140574284375760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140574397981968('path', u'replies', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    (__iterator, ____index_140574284377168, ) = getitem('repeat')(u'reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7fda0048ecd0> name=None at 7fda0048ee90> -> __attrs_140574284376976
                        __attrs_140574284376976 = _static_140574284377296
                        __backup_reply_140574257266064 = get('reply', __marker)

                        # <Value u'reply_dict/comment' (34:35)> -> __value
                        __token = 1690
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('path', u'reply_dict/comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_140574270206480 = get('comment_id', __marker)

                        # <Value u'reply/getId' (35:39)> -> __value
                        __token = 1749
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('path', u'reply/getId', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_140574270346896 = get('depth', __marker)

                        # <Value u'reply_dict/depth|python:0' (36:33)> -> __value
                        __token = 1796
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('path', u'reply_dict/depth|python:0', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_140574257223248 = get('depth', __marker)

                        # <Value u"python: depth > 10 and '10' or depth" (37:32)> -> __value
                        __token = 1857
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u" depth > 10 and '10' or depth", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_140574268981904 = get('author_home_url', __marker)

                        # <Value u'python:view.get_commenter_home_url(username=reply.author_username)' (38:41)> -> __value
                        __token = 1939
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_140574284389904 = get('has_author_link', __marker)

                        # <Value u'python:author_home_url and not isAnon' (39:40)> -> __value
                        __token = 2051
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'author_home_url and not isAnon', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_140574270568400 = get('portrait_url', __marker)

                        # <Value u'python:view.get_commenter_portrait(reply.author_username)' (40:36)> -> __value
                        __token = 2131
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_140574270222736 = get('review_state', __marker)

                        # <Value u"python:wtool.getInfoFor(reply, 'review_state', 'none')" (41:35)> -> __value
                        __token = 2231
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u"wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_140574270208528 = get('canEdit', __marker)

                        # <Value u'python:view.can_edit(reply)' (42:29)> -> __value
                        __token = 2323
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'view.can_edit(reply)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_140574267902928 = get('canDelete', __marker)

                        # <Value u'python:view.can_delete(reply)' (43:30)> -> __value
                        __token = 2390
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u'view.can_delete(reply)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_140574270345872 = get('colorclass', __marker)

                        # <Value u"python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (44:30)> -> __value
                        __token = 2460
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140574397981968('python', u"lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value u"python:canReview or review_state == 'published'" (47:32)> -> __condition
                        __token = 2795
                        try:
                            __zt_tmp = __attrs_140574284376976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140574397981968('python', u"canReview or review_state == 'published'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284374736
                            __default_140574284374736 = _DEFAULT_MARKER

                            # <Substitution u"python:'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (45:39)> -> __attr_class
                            __token = 2614
                            try:
                                __zt_tmp = __attrs_140574284376976
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140574397981968('python', u"'comment replyTreeLevel{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', u'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284375120
                            __default_140574284375120 = _DEFAULT_MARKER

                            # <Substitution u'comment_id' (46:35)> -> __attr_id
                            __token = 2750
                            try:
                                __zt_tmp = __attrs_140574284376976
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140574397981968('path', u'comment_id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))
                            __append(u'>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff337690> name=None at 7fd9ff3373d0> -> __attrs_140574266195408
                            __attrs_140574266195408 = _static_140574266193552

                            # <Value u'showCommenterImage' (49:57)> -> __condition
                            __token = 2903
                            try:
                                __zt_tmp = __attrs_140574266195408
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'showCommenterImage', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="commentImage">\n                    ')

                                # <Static value=<_ast.Dict object at 0x7fd9ff4f5ad0> name=None at 7fd9ff4f5d10> -> __attrs_140574268019600
                                __attrs_140574268019600 = _static_140574268021456

                                # <Value u'has_author_link' (50:46)> -> __condition
                                __token = 2970
                                try:
                                    __zt_tmp = __attrs_140574268019600
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140574397981968('path', u'has_author_link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268020048
                                    __default_140574268020048 = _DEFAULT_MARKER

                                    # <Substitution u'author_home_url' (51:52)> -> __attr_href
                                    __token = 3039
                                    try:
                                        __zt_tmp = __attrs_140574268019600
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140574397981968('path', u'author_home_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>\n                         ')

                                    # <Static value=<_ast.Dict object at 0x7fda004a8ad0> name=None at 7fda004a86d0> -> __attrs_140574267901968
                                    __attrs_140574267901968 = _static_140574284483280

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284482768
                                    __default_140574284482768 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (56:50)> -> __attr_src
                                    __token = 3291
                                    try:
                                        __zt_tmp = __attrs_140574267901968
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140574397981968('path', u'portrait_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284481936
                                    __default_140574284481936 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (57:49)> -> __attr_alt
                                    __token = 3354
                                    try:
                                        __zt_tmp = __attrs_140574267901968
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140574397981968('path', u'reply/author_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />\n                    </a>')
                                __append(u'\n                    ')

                                # <Static value=<_ast.Dict object at 0x7fd9ff4f5610> name=None at 7fd9ff4f5110> -> __attrs_140574257266640
                                __attrs_140574257266640 = _static_140574268020240

                                # <Value u'not: has_author_link' (63:40)> -> __condition
                                __token = 3606
                                try:
                                    __zt_tmp = __attrs_140574257266640
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140574397981968('not', u' has_author_link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<img')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257265168
                                    __default_140574257265168 = _DEFAULT_MARKER

                                    # <Substitution u'portrait_url' (64:45)> -> __attr_src
                                    __token = 3673
                                    try:
                                        __zt_tmp = __attrs_140574257266640
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140574397981968('path', u'portrait_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', u'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((u' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257262672
                                    __default_140574257262672 = _DEFAULT_MARKER

                                    # <Substitution u'reply/author_name' (65:44)> -> __attr_alt
                                    __token = 3731
                                    try:
                                        __zt_tmp = __attrs_140574257266640
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140574397981968('path', u'reply/author_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((u' alt="%s"' % __attr_alt))
                                    __append(u' class="defaultuserimg" height="32" />')
                                __append(u'\n                </div>')
                            __append(u'\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fda004a8690> name=None at 7fd9ff4f5350> -> __attrs_140574270360464
                            __attrs_140574270360464 = _static_140574284482192

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="documentByLine">\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574270359952
                            __attrs_140574270359952 = _static_140574442558096
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff331ed0> name=None at 7fd9ff331310> -> __attrs_140574266169872
                            __attrs_140574266169872 = _static_140574266171088

                            # <Value u'has_author_link' (71:42)> -> __condition
                            __token = 3931
                            try:
                                __zt_tmp = __attrs_140574266169872
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'has_author_link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266167696
                                __default_140574266167696 = _DEFAULT_MARKER

                                # <Substitution u'author_home_url' (73:48)> -> __attr_href
                                __token = 4055
                                try:
                                    __zt_tmp = __attrs_140574266169872
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140574397981968('path', u'author_home_url', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))
                                __append(u'>')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270357712
                                __default_140574270357712 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (72:40)> -> __cache_140574270358992
                                __token = 3988
                                try:
                                    __zt_tmp = __attrs_140574266169872
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574270358992 = _static_140574397981968('path', u'reply/author_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (72:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff730750> -> __condition
                                __expression = __cache_140574270358992

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                            Poster Name\n                        ')
                                else:
                                    __content = __cache_140574270358992
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</a>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574266168976
                            __attrs_140574266168976 = _static_140574442558096

                            # <Value u'not: has_author_link' (76:45)> -> __condition
                            __token = 4187
                            try:
                                __zt_tmp = __attrs_140574266168976
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u' has_author_link', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574266170000
                                __default_140574266170000 = _DEFAULT_MARKER

                                # <Value u'reply/author_name' (77:43)> -> __cache_140574266169488
                                __token = 4252
                                try:
                                    __zt_tmp = __attrs_140574266168976
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140574266169488 = _static_140574397981968('path', u'reply/author_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                                # <BinOp left=<Value u'reply/author_name' (77:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff3313d0> -> __condition
                                __expression = __cache_140574266169488

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<span />')
                                else:
                                    __content = __cache_140574266169488
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268058704
                            __attrs_140574268058704 = _static_140574442558096

                            # <Value u'not: reply/author_name' (78:45)> -> __condition
                            __token = 4319
                            try:
                                __zt_tmp = __attrs_140574268058704
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('not', u' reply/author_name', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')
                                __stream_140574268058640 = []
                                __append_140574268058640 = __stream_140574268058640.append
                                __append_140574268058640(u'Anonymous')
                                __msgid_140574268058640 = __re_whitespace(''.join(__stream_140574268058640)).strip()
                                if u'label_anonymous':
                                    __append(translate(u'label_anonymous', mapping=None, default=__msgid_140574268058640, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</span>')
                            __append(u'\n                    \n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268056272
                            __attrs_140574268056272 = _static_140574442558096
                            __stream_140574270359312 = []
                            __append_140574270359312 = __stream_140574270359312.append
                            __append_140574270359312(u'says:')
                            __msgid_140574270359312 = __re_whitespace(''.join(__stream_140574270359312)).strip()
                            if u'label_says':
                                __append(translate(u'label_says', mapping=None, default=__msgid_140574270359312, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff4feb90> name=None at 7fd9ff4fe410> -> __attrs_140574284443536
                            __attrs_140574284443536 = _static_140574268058512

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentDate">')

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268058000
                            __default_140574268058000 = _DEFAULT_MARKER

                            # <Value u'python:view.format_time(reply.modification_date)' (83:38)> -> __cache_140574270360336
                            __token = 4617
                            try:
                                __zt_tmp = __attrs_140574284443536
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574270360336 = _static_140574397981968('python', u'view.format_time(reply.modification_date)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'python:view.format_time(reply.modification_date)' (83:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4fedd0> -> __condition
                            __expression = __cache_140574270360336

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                         8/23/2001 12:40:44 PM\n                    ')
                            else:
                                __content = __cache_140574270360336
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</div>\n                </div>\n\n                ')

                            # <Static value=<_ast.Dict object at 0x7fda0049e950> name=None at 7fd9ff730390> -> __attrs_140574284441680
                            __attrs_140574284441680 = _static_140574284441936

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentBody">\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574284438160
                            __attrs_140574284438160 = _static_140574442558096

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574284440592
                            __default_140574284440592 = _DEFAULT_MARKER

                            # <Value u'reply/getText' (90:49)> -> __cache_140574284443408
                            __token = 4858
                            try:
                                __zt_tmp = __attrs_140574284438160
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140574284443408 = _static_140574397981968('path', u'reply/getText', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                            # <BinOp left=<Value u'reply/getText' (90:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fda0049e350> -> __condition
                            __expression = __cache_140574284443408

                            # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span />')
                            else:
                                __content = __cache_140574284443408
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'\n\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fda0049dd50> name=None at 7fda0049d750> -> __attrs_140574284435600
                            __attrs_140574284435600 = _static_140574284438864

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="commentActions">\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fda0049d710> name=None at 7fda0049d990> -> __attrs_140574268018512
                            __attrs_140574268018512 = _static_140574284437264

                            # <Value u'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (97:45)> -> __condition
                            __token = 5156
                            try:
                                __zt_tmp = __attrs_140574268018512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('python', u'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268015568
                                __default_140574268015568 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@delete-own-comment' (98:53)> -> __attr_action
                                __token = 5294
                                try:
                                    __zt_tmp = __attrs_140574268018512
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140574397981968('string', u'${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268017168
                                __default_140574268017168 = _DEFAULT_MARKER

                                # <Substitution u"python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (99:51)> -> __attr_style
                                __token = 5396
                                try:
                                    __zt_tmp = __attrs_140574268018512
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_style = _static_140574397981968('python', u"view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_style is not None):
                                    __append((u' style="%s"' % __attr_style))

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268018640
                                __default_140574268018640 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (100:47)> -> __attr_id
                                __token = 5520
                                try:
                                    __zt_tmp = __attrs_140574268018512
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140574397981968('string', u'delete-${comment_id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7fd9ff747410> name=None at 7fd9ff747810> -> __attrs_140574270453328
                                __attrs_140574270453328 = _static_140574270452752

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270454352
                                __default_140574270454352 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7fd9ff747fd0> at 7fd9ff747f50> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff747610> name=None at 7fd9ff747150> -> __attrs_140574257222480
                            __attrs_140574257222480 = _static_140574270453264

                            # <Value u'python:canDelete' (112:45)> -> __condition
                            __token = 6147
                            try:
                                __zt_tmp = __attrs_140574257222480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('python', u'canDelete', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <form ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<form name="delete"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257225104
                                __default_140574257225104 = _DEFAULT_MARKER

                                # <Substitution u'string:${reply/absolute_url}/@@moderate-delete-comment' (113:53)> -> __attr_action
                                __token = 6218
                                try:
                                    __zt_tmp = __attrs_140574257222480
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_action = _static_140574397981968('string', u'${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_action is not None):
                                    __append((u' action="%s"' % __attr_action))
                                __append(u' method="post" class="commentactionsform"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257222352
                                __default_140574257222352 = _DEFAULT_MARKER

                                # <Substitution u'string:delete-${comment_id}' (114:48)> -> __attr_id
                                __token = 6322
                                try:
                                    __zt_tmp = __attrs_140574257222480
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140574397981968('string', u'delete-${comment_id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))
                                __append(u'>\n                            ')

                                # <Static value=<_ast.Dict object at 0x7fd9ff738210> name=None at 7fd9ff7381d0> -> __attrs_140574268943568
                                __attrs_140574268943568 = _static_140574270390800

                                # <input ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<input name="form.button.DeleteComment" class="destructive" type="submit"')

                                # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268942672
                                __default_140574268942672 = _DEFAULT_MARKER

                                # <Translate msgid=u'label_delete' node=<_ast.Str object at 0x7fd9ff5d6110> at 7fd9ff5d6b50> -> __attr_value
                                __attr_value = u'Delete'
                                __attr_value = translate(u'label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_value is not None):
                                    __append((u' value="%s"' % __attr_value))
                                __append(u' />\n                        </form>')
                            __append(u'\n\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268944208
                            __attrs_140574268944208 = _static_140574442558096

                            # <Value u'python:isEditCommentAllowed and canEdit' (123:49)> -> __condition
                            __token = 6768
                            try:
                                __zt_tmp = __attrs_140574268944208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('python', u'isEditCommentAllowed and canEdit', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:
                                __append(u"\n                          <!-- plone 5 will have auth_token available\n                               so we'll use modal pattern -->\n                          ")

                                # <Static value=<_ast.Dict object at 0x7fd9ff5d6690> name=None at 7fd9ff5d6410> -> __attrs_140574268916432
                                __attrs_140574268916432 = _static_140574268941968

                                # <Value u'auth_token' (127:44)> -> __condition
                                __token = 7066
                                try:
                                    __zt_tmp = __attrs_140574268916432
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140574397981968('path', u'auth_token', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<a class="pat-plone-modal context commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268940944
                                    __default_140574268940944 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (128:50)> -> __attr_href
                                    __token = 7128
                                    try:
                                        __zt_tmp = __attrs_140574268916432
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140574397981968('string', u'${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((u' href="%s"' % __attr_href))
                                    __append(u'>')
                                    __stream_140574268942416 = []
                                    __append_140574268942416 = __stream_140574268942416.append
                                    __append_140574268942416(u'Edit')
                                    __msgid_140574268942416 = __re_whitespace(''.join(__stream_140574268942416)).strip()
                                    if u'Edit':
                                        __append(translate(u'Edit', mapping=None, default=__msgid_140574268942416, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                    __append(u'</a>')
                                __append(u'\n                          ')

                                # <Static value=<_ast.Dict object at 0x7fd9ff5d0e10> name=None at 7fd9ff5d0450> -> __attrs_140574268917072
                                __attrs_140574268917072 = _static_140574268919312

                                # <Value u'not: auth_token' (134:47)> -> __condition
                                __token = 7499
                                try:
                                    __zt_tmp = __attrs_140574268917072
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140574397981968('not', u' auth_token', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268916880
                                    __default_140574268916880 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@edit-comment' (135:55)> -> __attr_action
                                    __token = 7571
                                    try:
                                        __zt_tmp = __attrs_140574268917072
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140574397981968('string', u'${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268918608
                                    __default_140574268918608 = _DEFAULT_MARKER

                                    # <Substitution u'string:edit-${comment_id}' (136:50)> -> __attr_id
                                    __token = 7666
                                    try:
                                        __zt_tmp = __attrs_140574268917072
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140574397981968('string', u'edit-${comment_id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                              ')

                                    # <Static value=<_ast.Dict object at 0x7fd9ff762290> name=None at 7fd9ff762c50> -> __attrs_140574270564624
                                    __attrs_140574270564624 = _static_140574270562960

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.EditComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270566096
                                    __default_140574270566096 = _DEFAULT_MARKER

                                    # <Translate msgid=u'label_edit' node=<_ast.Str object at 0x7fd9ff762bd0> at 7fd9ff762090> -> __attr_value
                                    __attr_value = u'Edit'
                                    __attr_value = translate(u'label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                          </form>')
                                __append(u'\n                        ')
                            __append(u"\n\n\n                        <!-- Workflow actions (e.g. 'publish') -->\n                        ")

                            # <Static value=<_ast.Dict object at 0x7fd9ff5d6d10> name=None at 7fd9ff5d6890> -> __attrs_140574270171024
                            __attrs_140574270171024 = _static_140574268943632

                            # <Value u'canReview' (152:45)> -> __condition
                            __token = 8392
                            try:
                                __zt_tmp = __attrs_140574270171024
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('path', u'canReview', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:
                                __backup_action_140574268019280 = get('action', __marker)

                                # <Value u'reply_dict/actions|nothing' (153:49)> -> __iterator
                                __token = 8452
                                try:
                                    __zt_tmp = __attrs_140574270171024
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140574397981968('path', u'reply_dict/actions|nothing', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                (__iterator, ____index_140574270170320, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<form')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270563024
                                    __default_140574270563024 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (155:50)> -> __attr_name
                                    __token = 8632
                                    try:
                                        __zt_tmp = __attrs_140574270171024
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_name = _static_140574397981968('path', u'action/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_name = __quote(__attr_name, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_name is not None):
                                        __append((u' name="%s"' % __attr_name))

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270172752
                                    __default_140574270172752 = _DEFAULT_MARKER

                                    # <Substitution u'string:${reply/absolute_url}/@@transmit-comment' (154:53)> -> __attr_action
                                    __token = 8533
                                    try:
                                        __zt_tmp = __attrs_140574270171024
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140574397981968('string', u'${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', u'', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((u' action="%s"' % __attr_action))
                                    __append(u' method="get" class="commentactionsform"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574270170896
                                    __default_140574270170896 = _DEFAULT_MARKER

                                    # <Substitution u'string:${action/id}-${comment_id}' (156:47)> -> __attr_id
                                    __token = 8691
                                    try:
                                        __zt_tmp = __attrs_140574270171024
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140574397981968('string', u'${action/id}-${comment_id}', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((u' id="%s"' % __attr_id))
                                    __append(u'>\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7fd9ff7027d0> name=None at 7fd9ff702650> -> __attrs_140574257288272
                                    __attrs_140574257288272 = _static_140574270171088

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input type="hidden" name="workflow_action"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257289168
                                    __default_140574257289168 = _DEFAULT_MARKER

                                    # <Substitution u'action/id' (157:94)> -> __attr_value
                                    __token = 8823
                                    try:
                                        __zt_tmp = __attrs_140574257288272
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140574397981968('path', u'action/id', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                            ')

                                    # <Static value=<_ast.Dict object at 0x7fd9feab9c10> name=None at 7fd9feab9050> -> __attrs_140574257195600
                                    __attrs_140574257195600 = _static_140574257290256

                                    # <input ... (0:0)
                                    # --------------------------------------------------------
                                    __append(u'<input name="form.button.TransmitComment" class="context" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574257196816
                                    __default_140574257196816 = _DEFAULT_MARKER

                                    # <Translate msgid=None node=<Substitution u'action/title' (161:57)> at 7fd9feaa2990> -> __attr_value

                                    # <Substitution u'action/title' (161:57)> -> __attr_value
                                    __token = 9064
                                    try:
                                        __zt_tmp = __attrs_140574257195600
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_value = _static_140574397981968('path', u'action/title', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    if (__attr_value is not None):
                                        __append((u' value="%s"' % __attr_value))
                                    __append(u' />\n                        </form>')
                                    ____index_140574270170320 -= 1
                                    if (____index_140574270170320 > 0):
                                        __append('\n                        ')
                                if (__backup_action_140574268019280 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140574268019280
                            __append(u'\n                    </div>\n\n\n                </div>\n                ')

                            # <Static value=<_ast.Dict object at 0x7fd9ff5d0090> name=None at 7fda0049db10> -> __attrs_140574257195024
                            __attrs_140574257195024 = _static_140574268915856

                            # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (170:39)> -> __condition
                            __token = 9384
                            try:
                                __zt_tmp = __attrs_140574257195024
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140574397981968('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<button class="context reply-to-comment-button hide allowMultiSubmit">')
                                __stream_140574284438800 = []
                                __append_140574284438800 = __stream_140574284438800.append
                                __append_140574284438800(u'\n                    Reply\n                ')
                                __msgid_140574284438800 = __re_whitespace(''.join(__stream_140574284438800)).strip()
                                if u'label_reply':
                                    __append(translate(u'label_reply', mapping=None, default=__msgid_140574284438800, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                                __append(u'</button>')
                            __append(u'\n            </div>')
                        if (__backup_colorclass_140574270345872 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_140574270345872
                        if (__backup_canDelete_140574267902928 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_140574267902928
                        if (__backup_canEdit_140574270208528 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_140574270208528
                        if (__backup_review_state_140574270222736 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_140574270222736
                        if (__backup_portrait_url_140574270568400 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_140574270568400
                        if (__backup_has_author_link_140574284389904 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_140574284389904
                        if (__backup_author_home_url_140574268981904 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_140574268981904
                        if (__backup_depth_140574257223248 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140574257223248
                        if (__backup_depth_140574270346896 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140574270346896
                        if (__backup_comment_id_140574270206480 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_140574270206480
                        if (__backup_reply_140574257266064 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_140574257266064
                        __append(u'\n\n        ')
                        ____index_140574284377168 -= 1
                        if (____index_140574284377168 > 0):
                            __append('')
                    if (__backup_reply_dict_140574270394832 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_140574270394832
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda0048ed90> name=None at 7fda0048e3d0> -> __attrs_140574257194256
                    __attrs_140574257194256 = _static_140574284377488

                    # <Value u'python: has_replies and not isDiscussionAllowed' (178:28)> -> __condition
                    __token = 9665
                    try:
                        __zt_tmp = __attrs_140574257194256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140574397981968('python', u' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="discreet">')
                        __stream_140574284375824 = []
                        __append_140574284375824 = __stream_140574284375824.append
                        __append_140574284375824(u'\n            Commenting has been disabled.\n        ')
                        __msgid_140574284375824 = __re_whitespace(''.join(__stream_140574284375824)).strip()
                        if u'label_commenting_disabled':
                            __append(translate(u'label_commenting_disabled', mapping=None, default=__msgid_140574284375824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>')
                    __append(u'\n\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9feaa2850> name=None at 7fda0048e890> -> __attrs_140574269062288
                __attrs_140574269062288 = _static_140574257195088

                # <Value u'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (187:24)> -> __condition
                __token = 9918
                try:
                    __zt_tmp = __attrs_140574269062288
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="reply">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff5f3410> name=None at 7fd9ff5f38d0> -> __attrs_140574269059408
                    __attrs_140574269059408 = _static_140574269060112

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574269062928
                    __default_140574269062928 = _DEFAULT_MARKER

                    # <Substitution u'view/login_action' (188:37)> -> __attr_action
                    __token = 10026
                    try:
                        __zt_tmp = __attrs_140574269059408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140574397981968('path', u'view/login_action', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fd9ff5f3690> name=None at 7fd9ff5f3950> -> __attrs_140574268985296
                    __attrs_140574268985296 = _static_140574269060752

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="standalone loginbutton" type="submit"')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574268983312
                    __default_140574268983312 = _DEFAULT_MARKER

                    # <Translate msgid=u'label_login_to_add_comments' node=<_ast.Str object at 0x7fd9ff5f3a50> at 7fd9ff5f3110> -> __attr_value
                    __attr_value = u'Log in to add comments'
                    __attr_value = translate(u'label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n        </form>\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fd9ff5f3e50> name=None at 7fd9ff5f3e10> -> __attrs_140574268984016
                __attrs_140574268984016 = _static_140574269062736

                # <Value u'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (197:54)> -> __condition
                __token = 10355
                try:
                    __zt_tmp = __attrs_140574268984016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140574397981968('python', u'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="commenting" class="reply">\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574268984592
                    __attrs_140574268984592 = _static_140574442558096

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<fieldset>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267931216
                    __attrs_140574267931216 = _static_140574442558096

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<legend>')
                    __stream_140574268983696 = []
                    __append_140574268983696 = __stream_140574268983696.append
                    __append_140574268983696(u'Add comment')
                    __msgid_140574268983696 = __re_whitespace(''.join(__stream_140574268983696)).strip()
                    if u'label_add_comment':
                        __append(translate(u'label_add_comment', mapping=None, default=__msgid_140574268983696, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</legend>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267928976
                    __attrs_140574267928976 = _static_140574442558096

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p>')

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267928784
                    __default_140574267928784 = _DEFAULT_MARKER

                    # <Value u'view/comment_transform_message' (202:28)> -> __cache_140574267929936
                    __token = 10581
                    try:
                        __zt_tmp = __attrs_140574267928976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267929936 = _static_140574397981968('path', u'view/comment_transform_message', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/comment_transform_message' (202:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4df510> -> __condition
                    __expression = __cache_140574267929936

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n            ')
                    else:
                        __content = __cache_140574267929936
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>\n\n            ')

                    # <Static value=<_ast.Dict object at 0x7fda09b69290> name=None at 7fda09b69190> -> __attrs_140574267931088
                    __attrs_140574267931088 = _static_140574442558096

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __default_140574267929104
                    __default_140574267929104 = _DEFAULT_MARKER

                    # <Value u'view/form/render' (207:40)> -> __cache_140574267930064
                    __token = 10780
                    try:
                        __zt_tmp = __attrs_140574267931088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140574267930064 = _static_140574397981968('path', u'view/form/render', econtext=econtext)(_static_140574397982672(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/form/render' (207:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fda09b693d0> at 7fd9ff4df910> -> __condition
                    __expression = __cache_140574267930064

                    # <Symbol value=<DEFAULT> at 7fda09b693d0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div />')
                    else:
                        __content = __cache_140574267930064
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n        </fieldset>\n    </div>')
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140574270167632
            if (__backup_auth_token_140574266167632 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_140574266167632
            if (__backup_wtool_140574270364816 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_140574270364816
            if (__backup_errors_140574270165200 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140574270165200
            if (__backup_showCommenterImage_140574268984144 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_140574268984144
            if (__backup_has_replies_140574257263888 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_140574257263888
            if (__backup_replies_140574270453456 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_140574270453456
            if (__backup_canReview_140574284475216 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_140574284475216
            if (__backup_isAnon_140574268944144 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140574268944144
            if (__backup_isDeleteOwnCommentAllowed_140574270457424 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_140574270457424
            if (__backup_isEditCommentAllowed_140574270170000 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_140574270170000
            if (__backup_isAnonymousDiscussionAllowed_140574270346768 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_140574270346768
            if (__backup_isDiscussionAllowed_140574270569680 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_140574270569680
            if (__backup_userHasReplyPermission_140574270567888 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_140574270567888
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }