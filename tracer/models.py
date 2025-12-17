from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.TextField(max_length=100,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Index(models.Model):
    name = models.TextField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    note = models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    name = models.TextField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    note = models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Sea(models.Model):
    name = models.TextField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    company = models.TextField(max_length=100,null=True,blank=True)
    message = models.TextField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
