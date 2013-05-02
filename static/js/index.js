$(function(){
    $('#search-form').submit(function(e){
        var url = $(this).prop('action');
        var query = $('#search-field').val();
        // Do some ajax call - this is just a quick non-working example.
        $.ajax({
            type : "GET",
            url : url,
            data : { 'query' : query },
            success : function(data){
                var con = $('.first').clone();
                pa = con.children('p');
                pa.text(data.text);
                link = con.children('a');
                link.attr('href', data.link);
                link.text(data.screen_name);
                // con.text(data.text);
                con.removeClass('first');
                $('.first').after(con)
                con.show();
                // console.log(data);
            },
            dataType : 'json'
        });
        // return false to stop the page from submitting
        return false;
    });
});
