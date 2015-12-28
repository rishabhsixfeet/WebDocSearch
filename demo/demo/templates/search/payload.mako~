<%
from demo.lib import query_process

highlightExtract = query_process.TextMachine(extractLength=64,
    highlightTemplate='<span class=highlight>%s</span>',
    escape=h.html_escape).process

highlight = query_process.TextMachine(
    highlightTemplate='<span class=highlight>%s</span>',
    escape=h.html_escape).process

xapian_file_name = 0
%>

${c.matches.get_matches_estimated()} result(s)<br>

% for matchIndex, match in enumerate(c.matches):
<%
    content = match.document.get_data()
%>
<br>
<div id=result${matchIndex} class=tabOFF>
    ${h.literal(highlightExtract(c.queryString, content))}
</div>
[<a class=linkOFF href="${h.url('search_download', fileName=match.document.get_value(xapian_file_name))}">download</a>]<br>
<div id=result${matchIndex}_ class=tab_>
    ${h.literal(highlight(c.queryString, content))}
</div>
% endfor
