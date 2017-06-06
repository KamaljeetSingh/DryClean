from django.contrib import admin
from .models import *
# Register your models here

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(OrderPlaced)
admin.site.register(OrderInfo)
admin.site.register(DeliverTo)
admin.site.register(OrderItems)

