# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1451242853.874243
_enable_loop = True
_template_filename = '/home/defiant/demo/demo/templates/search/payload.mako'
_template_uri = '/search/payload.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        from demo.lib import query_process
        
        highlightExtract = query_process.TextMachine(extractLength=40,
            highlightTemplate='<span class=highlight>%s</span>',
            escape=h.html_escape).process
        
        highlight = query_process.TextMachine(
            highlightTemplate='<span class=highlight>%s</span>',
            escape=h.html_escape).process
        
        xapian_file_name = 0
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['xapian_file_name','highlight','highlightExtract','query_process'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(escape(c.matches.get_matches_estimated()))
        __M_writer(u' result(s)<br>\n\n')
        # SOURCE LINE 17
        for matchIndex, match in enumerate(c.matches):
            # SOURCE LINE 18

            content = match.document.get_data()[:6000]
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['content'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 20
            __M_writer(u'\n<br>\n<div id=result')
            # SOURCE LINE 22
            __M_writer(escape(matchIndex))
            __M_writer(u' class=tabOFF>\n    ')
            # SOURCE LINE 23
            __M_writer(escape(h.literal(match.document.get_value(xapian_file_name))))
            __M_writer(u'\n</div>\n[<a class=linkOFF href="')
            # SOURCE LINE 25
            __M_writer(escape(h.url('search_download', fileName=match.document.get_value(xapian_file_name))))
            __M_writer(u'">download</a>]<br>\n<div id=result')
            # SOURCE LINE 26
            __M_writer(escape(matchIndex))
            __M_writer(u'_ class=tab_>\n    ')
            # SOURCE LINE 27
            __M_writer(escape(h.literal(highlight(c.queryString, content))))
            __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


