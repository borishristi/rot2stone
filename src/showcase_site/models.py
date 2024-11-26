from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Devis(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField()
    service = models.CharField(max_length=50)
    # hour = models.DateTimeField()
    message = models.TextField()
