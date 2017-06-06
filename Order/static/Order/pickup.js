$(document).ready(function () {
       window.pick_obj={};
       $('#next2').prop('disabled',true);
       $('#save_pick').click(function () {
            var d = new Date($('#pickup_date').val());
            var day = d.getDate();
            if(day<10)
                day = "0"+day;
            var mon = d.getMonth() + 1;
            if(mon<10)
                mon= "0"+mon;
            var yr = d.getFullYear();
            pick_obj['date']= yr + "-" + mon + "-" + day;
            pick_obj['time']=$('#pickup_time option:selected').val();
            pick_obj['add_id']="";
            pick_obj['address']="";
            pick_obj['city']="";
            pick_obj['pincode']="";
            if($('#add_select1').is(':checked')) {
                console.log("radio 1 checked");
                pick_obj['add_id'] = $('#pickup_saved option:selected').val();
                console.log(pick_obj['add_id']);
                if(pick_obj['add_id']=="")
            {
                alert('You missed out selecting address');
                return;

            }

            }
            else
           {
               pick_obj['address'] = $('#pickup_loc1').val();
               pick_obj['city'] = $('#pickup_loc2').val();
               pick_obj['pincode'] = $('#pickup_loc3').val();
               console.log(pick_obj);
               if(pick_obj['address']=="" || pick_obj['city']=="" || pick_obj['pincode']=="")
            {
                alert('You missed entering address');
                return;

            }

           }
           if(!$('#pickup_date').val() || pick_obj['time']=="")
           {
               alert('You missed out data and time');
           }
           else {
               $('#del_date').prop('min', pick_obj['date']);
               $('#next2').prop('disabled',false);
           }



    });
});

