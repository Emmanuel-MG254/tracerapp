from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Anonymous"

class Index(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Inquiry"

class Price(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Price Inquiry"

class Sea(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Sea Freight Inquiry"

class Shipment(models.Model):
    SHIPMENT_TYPES = [
        ('air', 'Air Freight'),
        ('sea', 'Sea Freight'),
        ('road', 'Road Freight'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    tracking_number = models.CharField(max_length=20, unique=True)
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=20)
    recipient_name = models.CharField(max_length=100)
    recipient_email = models.EmailField()
    recipient_phone = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    shipment_type = models.CharField(max_length=10, choices=SHIPMENT_TYPES)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tracking_number} - {self.sender_name} to {self.recipient_name}"

class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    shipment_type = models.CharField(max_length=10, choices=Shipment.SHIPMENT_TYPES)
    special_requirements = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Quote for {self.name} - {self.origin} to {self.destination}"


class Air(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Air Freight Inquiry"
class Road(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name or "Road Freight Inquiry"