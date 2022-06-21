from django.db import models

from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)


class Category(models.Model):
    category = models.CharField(max_length=25)
   
    def __str__(self):
        return f"{self.category}"  

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date=models.DateField()
    image = models.ImageField(upload_to='uploads/product',default="")

    def __str__(self):
        return f"{self.name}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.product}"

class Order(models.Model):

    status = (
        ('pending', 'pending'),
        ('success', 'success'),
        ('failed', 'failed'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=status, default='pending')
    date =  models.DateTimeField()
    order_id = models.CharField(max_length=100, default="")
    amount = models.IntegerField()
    

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Address(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100, default="")
    zip_code = models.IntegerField()
    state = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")


