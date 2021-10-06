from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):

    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Out Door')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):

    class STATUS(models.TextChoices):
        PENDING = 'pending', _('Pending')
        OUT_FOR_DELIVERY = 'out_for_delivery', _('Out for delivery')
        DELIVERED = 'delivered', _('Delivered')
       
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS.choices, 
        default=STATUS.PENDING
    )
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
