$(document).ready(function(){
$('#proceed').click(function () {
    if ($("#boom :checkbox:checked").length == 0) {
        alert("You have to check at least one box");
        return false;
}
});
});
