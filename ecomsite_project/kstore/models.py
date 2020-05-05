from django_fields import DefaultStaticImageField
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    image1 = DefaultStaticImageField(blank=True, default_image_path='images/blank.png')
    image2= DefaultStaticImageField(blank=True, default_image_path='images/blank.png')
    image3 = DefaultStaticImageField(blank=True, default_image_path='images/blank.png')
    image4 = DefaultStaticImageField(blank=True, default_image_path='images/blank.png')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def get_cart_url(self):
        return reverse('cart', kwargs={'pk': self.pk})
