# -*- coding: utf-8 -*-
#from twisted.words.xish import domish

import random
import datetime
import bnw_core.base
gc = bnw_core.base.gc

formatters = {
    'comment': None,
    'message': None,
    'recommendation': None,
    'message_with_replies': None,
    'messages': None,
}

def format_message(msg):
    result = '+++ [%s] %s:\n' % (
        datetime.datetime.utcfromtimestamp(msg['date']).strftime('%d.%m.%Y %H:%M:%S'),
        msg['user'],)
    if msg['tags']:
        result += 'Tags: %s\n' % (', '.join(msg['tags']),)
    if msg['clubs']:
        result += 'Clubs: %s\n' % (', '.join(msg['clubs']),)
    result += '\n%s\n' % (msg['text'],)
    result += '--- %(id)s (%(rc)d) %(base_url)sp/%(id)s' % { 
               'base_url': gc('webui_base'), 
               'id': msg['id'].upper(),
               'rc':    msg['replycount'],
             }
    return result
    
def format_comment(msg,short=False):
    args = { 'id':    msg['id'].split('/')[1].upper(),
             'author':msg['user'],
             'message':msg['message'].upper(),
             'replyto':None if msg['replyto'] is None else msg['replyto'].upper(),
             'replytotext': msg['replytotext'],
             'text':  msg['text'],
             'num':   msg.get('num',-1),
             'date':  datetime.datetime.utcfromtimestamp(msg['date']).strftime('%d.%m.%Y %H:%M:%S'),
             'web': gc('webui_base'),
           }
    formatstring = '+++ [ %(date)s ] %(author)s'
    if msg['replyto']:
        formatstring += ' (in reply to %(replyto)s):\n'
    else:
        formatstring += ' (in reply to %(message)s):\n'
    if not short:
        formatstring += '>%(replytotext)s\n'
    formatstring += '\n%(text)s\n--- %(message)s/%(id)s (%(num)d) %(web)sp/%(message)s#%(id)s'
    return formatstring % args

def formatter_messages(request,result):
    return 'Search results:\n'+'\n'.join((format_message(msg) for msg in result['messages']))

def formatter_message_with_replies(request,result):
    return format_message(result['message']) + '\n' + \
            '\n'.join((format_comment(c,True) for c in result['replies']))

def formatter_subscriptions(request,result):
    return 'Your subscriptions:\n'+'\n'.join(
        (s['type'][4:].ljust(5)+s['target'].rjust(10)+' '+s.get('from','')
         for s in result['subscriptions']))

def formatter_message(request,result):
    return format_message(result['message'])

def formatter_recommendation(request,result):
    return 'Recommended by @%s: %s\n' % (result['recommender'],result['recocomment']) + \
        format_message(result['message'])

def formatter_comment(request,result):
    return format_comment(result['comment'])

def formatter_search(request,result):
    return '\n\n'.join('%s (%d%%): %s' % (x[0],x[1],x[2]) for x in result['result'])

def formatter_userlist(request,result):
    if not result['users']:
        return 'No more users.'
    return ' '+' '.join(
        '@'+u['name'].ljust(10)+('\n' if i%5==4 else '')
            for i,u in enumerate(result['users']))+'\nuserlist -p '+str(result['page']+1)+' -- next page.'

def formatter_settings(request,result):
    return 'Currrent settings:\n'+'\n'.join('%10s %s' % (k,v) for k,v in result['settings'].iteritems())

def formatter_clubs(request,result):
    return ' '+' '.join(
        ''+u['_id'].ljust(15)+' '+str(int(u['value'])).ljust(3)+('\n' if i%5==4 else '')
            for i,u in enumerate(result['clubs']))