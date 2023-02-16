from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='name', max_length=255)
    description = models.TextField(verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')
    currency = models.CharField(
        verbose_name='currency',
        max_length=20,
        default='usd'
    )

    class Meta:
        ordering = ['-price']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders', blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.pk}'
