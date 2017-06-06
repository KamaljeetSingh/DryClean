from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    url(r'^$', views.loginForm, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^items/$', views.items, name='items'),
    url(r'^test/$', views.test, name='test'),
    url(r'^myorders/$', views.myorders, name='myorders'),
    url(r'^myorders/order/(?P<pk>[0-9]+)', views.orderdisplay, name='orderdisplay'),

]