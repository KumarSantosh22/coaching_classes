from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
    message = models.TextField(max_length=300)
    date = models.DateField(auto_now_add=True)

