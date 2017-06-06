$(document).ready(function () {
       window.del_obj={};
       $('#next3').prop('disabled',true);
       $('#all_obj').prop('disabled',true);
       $('#caption').hide();
       $('#save_del').click(function () {
            var d = new Date($('#del_date').val());
            var day = d.getDate();
            if(day<10)
                day = "0"+day;
            var mon = d.getMonth() + 1;
            if(mon<10)
                mon= "0"+mon;
            var yr = d.getFullYear();
            del_obj['date']= yr + "-" + mon + "-" + day;
            del_obj['time']=$('#del_time option:selected').val();
            del_obj['address']="";
            del_obj['city']="";
            del_obj['pincode']="";
            del_obj['same']="0";
            del_obj['option']=$('input:radio[name=optradio]:checked').val();
            console.log(del_obj);
            if($('#add_select_del1').is(':checked')){
                del_obj['same']="1";
                console.log("clicked");
            }

            else{
            del_obj['address']=$('#del_loc1').val();
            del_obj['city']=$('#del_loc2').val();
            del_obj['pincode']=$('#del_loc3').val();
            if(del_obj['address']=="" || del_obj['city']=="" || del_obj['pincode']=="") {
                alert("You missed out delivery address");
                return;
            }
            }

            console.log(del_obj);

            if(!$('#del_date').val() || del_obj['time']=="" )
            {
                alert('You missed out date or time');
            }
           else {
                $('#next3').prop('disabled',false);
                $('#all_obj').prop('disabled',false);
            }
    });
});
