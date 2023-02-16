from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(verbose_name='name', max_length=255)
    description = models.TextField(verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')