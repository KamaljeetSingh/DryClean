$(document).ready(function () {
        $('.saved_add').hide();
        $('.new_add').hide();
        $('.new_add_del').hide();

        $('#add_select1').click(function(){
            $('.saved_add').show();
            $('.new_add').hide();
        });

        $('#add_select2').click(function(){
            $('.saved_add').hide();
            $('.new_add').show();
        });




});
