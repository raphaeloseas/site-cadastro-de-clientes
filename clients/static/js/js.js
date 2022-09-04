setTimeout(fade_out, 5000);
function fade_out() {
    $(".messages").fadeOut().empty();
}

$(document).ready(function() {

    var btnDelete = $('.btn-delete');
    var btnSearch = $('#btn-search');
    var btnSearch1 = $('#btn-search1');
    var btnSearch2 = $('#btn-search2');
    var searchForm = $('#search-form');
    var searchForm1 = $('#search-form1');
    var searchForm2 = $('#search-form2');

    $(btnDelete).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja realmente deletar este cliente?');

        if(result) {
            window.location.href = delLink;
        }
    });

    $(btnSearch).on('click', function(){
        searchForm.submit();
    });

    $(btnSearch1).on('click', function(){
        searchForm1.submit();
    });

    $(btnSearch2).on('click', function(){
        searchForm2.submit();
    });


});