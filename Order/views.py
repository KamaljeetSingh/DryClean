from django.shortcuts import render,HttpResponse,render_to_response
from django.views.generic import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,  redirect
from .models import *
import datetime
import json
from time import gmtime, strftime, localtime


# Create your views here.
def loginForm(request):
    if request.user.is_authenticated():
        return redirect('order:home')

    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('order:home')
        return HttpResponse('<p>Sorry ! Your Username and Password dont match.</p>')


    return render(request,'Order/login.html',{})


def logout_view(request):
    logout(request)
    return redirect('order:login')


def home(request):
    if request.user.is_authenticated():
        name = request.user.username
        name = name.title()
        cat = Category.objects.all()
        return render(request, 'Order/homepage.html', {'name': name , 'cat': cat })
    else:
        return redirect('order:login')


def items(request):
    if (request.method == "POST"):
        cat = request.POST.getlist('options')
        item_dict={}
        deliver_to = DeliverTo.objects.all()
        orderplaced = OrderPlaced.objects.filter(user_id=request.user.pk)
        flag = 1
        if not orderplaced:
            flag = 0
        for c in cat:
            cat_obj = Category.objects.get(category_name=c)
            item_dict[c]=[]
            d = Items.objects.filter(category_id=cat_obj.pk)
            for i in d:
                item_dict[c].append(i)
        return render(request, 'Order/items.html', {'cat_list':cat, 'name': request.user.username.title(),
                                                    'deliver_to': deliver_to, 'item_dict':item_dict, 'flag':flag,
                                                    'orders':orderplaced})
    else:
        return HttpResponse("not valid")


def test(request):
    if request.is_ajax():
        x = request.POST['items_obj']
        it = json.loads(x)
        print(it)

        z = request.POST['pick_obj']
        pu = json.loads(z)
        print(pu)

        p = request.POST['del_obj']
        de = json.loads(p)
        print(de)

        tot_fare = 0
        del_opt = DeliverTo.objects.get(id=de['option'])

        if(pu['add_id'] != ""):
            z = OrderInfo.objects.get(id=pu['add_id'])
            pu['address']=z.pickup_add
            pu['city']=z.pickup_city
            pu['pincode']=z.pickup_pin

        if(de['same'] == "1"):
            de['address']=pu['address']
            de['city']=pu['city']
            de['pincode']=pu['pincode']

        order_info = OrderInfo()                  #making orderinfo
        order_info.pickup_date = pu['date']
        order_info.pickup_time = pu['time']
        order_info.pickup_add = pu['address']
        order_info.pickup_city = pu['city']
        order_info.pickup_pin = pu['pincode']
        order_info.del_date = de['date']
        order_info.del_time = de['time']
        order_info.del_add = de['address']
        order_info.del_city = de['city']
        order_info.del_pin = de['pincode']
        order_info.del_option = del_opt
        order_info.save()

        for key,value in it.items():
            item = Items.objects.get(id=key)
            order_items = OrderItems()
            order_items.order_info_id = order_info
            order_items.items = item
            order_items.quantity = value
            tot_fare = tot_fare + (int(value)*(item.rate))
            order_items.save()

        order_info1 = OrderInfo.objects.get(pk=order_info.pk)
        order_info1.total_fare = tot_fare
        order_info1.save()

        orderplaced = OrderPlaced()
        orderplaced.user_id = request.user
        orderplaced.order_info_id = order_info
        orderplaced.order_date = strftime("%Y-%m-%d %H:%M:%S", localtime())
        orderplaced.save()

        items_ordered = OrderItems.objects.filter(order_info_id=order_info.pk)

        return render_to_response('Order/placed_order.html', {'order_info':order_info1,'items':items_ordered,
                                                              'date':orderplaced.order_date})


def myorders(request):
    order_placed = OrderPlaced.objects.filter(user_id=request.user.pk)
    return render(request, 'Order/myorders.html', {'orders':order_placed, 'name': request.user.username.title()})


def orderdisplay(request, pk):
    if request.user.is_authenticated():
        orderplaced = OrderPlaced.objects.get(order_info_id=pk)
        if(request.user == orderplaced.user_id):
            order_info = OrderInfo.objects.get(pk=pk)
            items_ordered = OrderItems.objects.filter(order_info_id=pk)

            return render(request, 'Order/placed_order.html', {'order_info': order_info, 'items': items_ordered,
                                                               'date': orderplaced.order_date})
        else:
            return HttpResponse("Order Not Found!")
    else:
        return render(request, 'Order/login.html', {})



















