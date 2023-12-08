$(function () {
    $('#A').click(function () {
        $('#content').removeClass().addClass('AAA');
        $('#img').attr('src', './images/top.png');
        $('body').css('background-color', '')
    });
    $('#B').click(function () {
        $('#content').removeClass().addClass('BBB');
        $('#img').attr('src', './images/top_B.png');
        $('body').css('background-color', 'black')
    });
    $('#C').click(function () {
        $('#content').removeClass().addClass('CCC');
        $('#img').attr('src', './images/top_C.png');
        $('body').css('background-color', 'red')
    });



})