    $(document).ready(function() {
        $("#all_obj").click(function () {
            var items = JSON.stringify(obj);
            var pick = JSON.stringify(pick_obj);
            var del = JSON.stringify(del_obj);
            console.log(del);
            alert("final");
            $.ajax({
                type: 'POST',
                url: $(this).attr('href'),
                data: {
                    items_obj: items,
                    pick_obj:pick,
                    del_obj:del,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    $('#delivery').hide();
                    $('#caption').show();
                    $('#order_placed').html(data);
                     // window.location.href= "Order/homepage.html";
                }
            });
        });
    });
