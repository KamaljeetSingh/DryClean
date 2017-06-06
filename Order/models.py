from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DeliverTo(models.Model):
    options = models.CharField(max_length=100)

    def __str__(self):
        return (self.options)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.category_name)


class Items(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    rate = models.IntegerField()

    def __str__(self):
        return (self.category_id.category_name)+"-"+(self.type)

class OrderInfo(models.Model):
    pickup_date = models.CharField(max_length=100,null=True)
    pickup_time = models.CharField(max_length=100,null=True)
    pickup_add = models.CharField(max_length=100,null=True)
    pickup_city = models.CharField(max_length=100,null=True)
    pickup_pin = models.CharField(max_length=100,null=True)
    del_date = models.CharField(max_length=100,null=True)
    del_time = models.CharField(max_length=100,null=True)
    del_add = models.CharField(max_length=100,null=True)
    del_city = models.CharField(max_length=100,null=True)
    del_pin = models.CharField(max_length=100,null=True)
    del_option = models.ForeignKey(DeliverTo, on_delete=models.CASCADE, null=True)
    total_fare = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class OrderItems(models.Model):
    order_info_id = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.id)


class OrderPlaced(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_info_id = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    order_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user_id.pk)+"-"+str(self.order_info_id.pk)




