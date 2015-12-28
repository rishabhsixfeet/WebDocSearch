<html>
<head>
<style>
    .normalFONT {font-family: Arial, Helvetica, sans-serif}
    .highlight {background-color: yellow; color: black}
    .linkOFF {color: darkblue; background-color: white}
    .linkON {color: white; background-color: darkblue}
    .tabOFF {color: black; background-color: white}
    .tabON {color: white; background-color: black}
    .tab_ {display: none}
</style>
${h.javascript_link('/jquery-1.4.2.min.js')}
<script>
$(document).ready(function() {

    // When the user clicks the Search button,
    $('#button_search').click(ajax_search);

    $('#query').keydown(function(event) {
        switch(event.keyCode) {
            // When the user presses the ENTER key,
            case 13:
                ajax_search();
                break;
        };
    }).focus();

    function ajax_search() {
        // Load query string
        var queryString = $.trim($('#query').val());
        // If the query string is non-empty,
        if (queryString.length) {
            // Submit GET request to the URL matching the route named 'search_query'
            $.get("${h.url('search_query')}", {
                'q': queryString
            }, function(data) {
                // Display content
                $('#content').html(data);
                // Change color when hovering over links
                $('a').hover(
                    function () {this.className = this.className.replace('OFF', 'ON');},
                    function () {this.className = this.className.replace('ON', 'OFF');});
                // Change color when hovering over summaries
                $('.tabOFF').hover(
                    function() {this.className = this.className.replace('OFF', 'ON');},
                    function() {this.className = this.className.replace('ON', 'OFF');}
                ).click(function() {$('#' + this.id + '_').toggle();});
            });
        }
    }

});
</script>

</head>
<body class=normalFONT>
    <input id=query>
    <input id=button_search type=button value=Search>
    <div id=content>
    </div>
</body>
</html>
