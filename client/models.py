from django.db import models

# Create your models here.


class Address (models.Model):
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class Client (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    address = models.ManyToManyField(Address, related_name='clients')


class Profile (models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    about_me = models.TextField()
    avatar = models.FileField(upload_to='pictures')



