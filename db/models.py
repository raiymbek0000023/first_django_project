from django.db import models
from manage import init_django

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Platform(Model):
    title = models.CharField(max_length=255)

class Publisher(Model):
    title=models.CharField(max_length=255)

class Genre(Model):
    title=models.CharField(max_length=255)


class Customer(Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    da