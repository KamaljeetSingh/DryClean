$(document).ready(function () {
        $('#next1').click(function(){
            console.log("helloo");
            console.log(obj);
            if(Object.keys(obj).length == 0) {
                alert("Select one or more items to proceed");
                return false;
            }
            $('#choose').hide();
            $('#schedule').show();
        });
});
