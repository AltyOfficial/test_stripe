import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Item, Order


class Command(BaseCommand):
    help = 'Загрузка данных в БД.'

    def handle(self, **kwargs):
        data_path = settings.BASE_DIR / 'project/data'

        with open(f'{data_path}/items.csv', 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                name, description, price, currency = row
                Item.objects.get_or_create(
                    name=name,
                    description=description,
                    price=price,
                    currency=currency
                )
        self.stdout.write(self.style.SUCCESS('ПРОДУКТЫ ЗАГРУЖЕНЫ'))

        with open(f'{data_path}/orders.csv', 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                order = Order.objects.create()
                for item in row:
                    order.items.add(item)
        self.stdout.write(self.style.SUCCESS('ЗАКАЗЫ ЗАГРУЖЕНЫ'))
