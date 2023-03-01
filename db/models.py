from django.db import models
from manage import init_django
import datetime

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Platform(Model):
    title = models.CharField(max_length=255) 
    # def __str__(self):
    #     return self.title

class Publisher(Model):
    title=models.CharField(max_length=255)
    # def __str__(self):
        # return self.title
    
class Genre(Model):
    title=models.CharField(max_length=255)
    # def __str__(self):
        # return self.title

class Customer(Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    dateofBirth=models.DateField()

class ContentRating(Model):
    title=models.CharField(max_length=255)
    ageLimit=models.IntegerField()
    description=models.CharField(max_length=255)
    # def __str__(self):
        # return self.title, self.ageLimit, self.description

class Products(Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    platform=models.ForeignKey(Platform, on_delete=models.CASCADE)
    relaeseDate=models.DateField()
    publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price=models.IntegerField()
    contentrating=models.ForeignKey(ContentRating, on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    isAviable=models.BooleanField()
    # def __str__(self):
        # return self.get_queryset, title, self.description, self.platform, self.relaeseDate, self.publisher, self.price, self.contentrating, self.isAviable

class Sales(Model):
    products=models.ForeignKey(Products, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    dateofSales=models.DateField()
class Discont(Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    datefrom=models.DateField()
    dateuntil=models.DateField()
    prc=models.DecimalField(decimal_places=100, max_digits=155)

class Wish_list(Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
class WL_P(Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    wish_list=models.ForeignKey(Customer, on_delete=models.CASCADE)
