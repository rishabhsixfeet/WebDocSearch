# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1451266608.532055
_enable_loop = True
_template_filename = '/home/defiant/demo/demo/templates/search/index.mako'
_template_uri = '/search/index.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<style>\n    .normalFONT {font-family: Arial, Helvetica, sans-serif}\n    .highlight {background-color: yellow; color: black}\n    .linkOFF {color: darkblue; background-color: white}\n    .linkON {color: white; background-color: darkblue}\n    .tabOFF {color: black; background-color: white}\n    .tabON {color: white; background-color: black}\n    .tab_ {display: none}\n</style>\n')
        # SOURCE LINE 12
        __M_writer(escape(h.javascript_link('/jquery-1.4.2.min.js')))
        __M_writer(u'\n<script>\n$(document).ready(function() {\n\n    // When the user clicks the Search button,\n    $(\'#button_search\').click(ajax_search);\n\n    $(\'#query\').keydown(function(event) {\n        switch(event.keyCode) {\n            // When the user presses the ENTER key,\n            case 13:\n                ajax_search();\n                break;\n        };\n    }).focus();\n\n    function ajax_search() {\n        // Load query string\n        var queryString = $.trim($(\'#query\').val());\n        // If the query string is non-empty,\n        if (queryString.length) {\n            // Submit GET request to the URL matching the route named \'search_query\'\n            $.get("')
        # SOURCE LINE 34
        __M_writer(escape(h.url('search_query')))
        __M_writer(u'", {\n                \'q\': queryString\n            }, function(data) {\n                // Display content\n                $(\'#content\').html(data);\n                // Change color when hovering over links\n                $(\'a\').hover(\n                    function () {this.className = this.className.replace(\'OFF\', \'ON\');},\n                    function () {this.className = this.className.replace(\'ON\', \'OFF\');});\n                // Change color when hovering over summaries\n                $(\'.tabOFF\').hover(\n                    function() {this.className = this.className.replace(\'OFF\', \'ON\');},\n                    function() {this.className = this.className.replace(\'ON\', \'OFF\');}\n                ).click(function() {$(\'#\' + this.id + \'_\').toggle();});\n            });\n        }\n    }\n\n});\n</script>\n\n</head>\n<body class=normalFONT>\n    <input id=query>\n    <input id=button_search type=button value=Search>\n    <div id=content>\n    </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


