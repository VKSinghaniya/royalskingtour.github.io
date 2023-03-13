from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    location=models.CharField(max_length=60)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_name=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    terminal=models.CharField(max_length=100)
    def __str__(self):
        return self.flight_name


class Booking(models.Model):
    p_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email_id = models.EmailField()
    address = models.TextField(max_length=100)
    t_date = models.DateField()
    dep_from = models.CharField(max_length=50)
    des_from = models.CharField(max_length=50)
    date = models.DateField()
    def __str__(self):
        return self.p_name




class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    Email = models.EmailField(max_length=60)
    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField()


