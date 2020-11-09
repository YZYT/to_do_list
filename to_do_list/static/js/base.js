$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('.fixed-action-btn').floatingActionButton({
        direction: 'left',
        // hoverEnabled: false
    });
     $('input#input_text, textarea#textarea2').characterCounter();
})
// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.fixed-action-btn');
//     var instances = M.FloatingActionButton.init(elems, {
//         direction: 'left',
//         hoverEnabled: false
//     });
// });