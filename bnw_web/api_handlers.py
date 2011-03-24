
from bnw_xmpp import command_clubs
from bnw_xmpp import command_delete
from bnw_xmpp import command_except
from bnw_xmpp import command_help
from bnw_xmpp import command_interface
from bnw_xmpp import command_login
from bnw_xmpp import command_onoff
from bnw_xmpp import command_ping
from bnw_xmpp import command_pm
from bnw_xmpp import command_search
from bnw_xmpp import command_post
from bnw_xmpp import command_register
from bnw_xmpp import command_show
from bnw_xmpp import command_subscription
from bnw_xmpp import command_vcard
from bnw_xmpp import command_userlist

handlers = {
    "register":             command_register.cmd_register,
    "search":               command_search.cmd_search,
    "interface":            command_interface.cmd_interface,
    "subscriptions/add":    command_subscription.cmd_subscribe,
    "subscriptions/del":    command_subscription.cmd_unsubscribe,
    "subscriptions":        command_subscription.cmd_subscriptions,
    "feed":                 command_show.cmd_feed,
    "show":                 command_show.cmd_show,
    "post":                 command_post.cmd_post,
    "comment":              command_post.cmd_comment,
    "recommend":            command_post.cmd_recommend,
    "on":                   command_onoff.cmd_on,
    "off":                  command_onoff.cmd_off,
    "delete":               command_delete.cmd_delete,
    "pm":                   command_pm.cmd_pm,
    "userlist":             command_userlist.cmd_userlist,
    "clubs":             command_clubs.cmd_clubs,
    "tags":             command_clubs.cmd_tags,
}