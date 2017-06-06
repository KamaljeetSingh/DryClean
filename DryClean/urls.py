
from django.conf.urls import url,include
from django.contrib import admin
from User import urls
from Order import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('User.urls')),
    url(r'^',include('Order.urls')),
]
