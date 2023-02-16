from random import choice

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, pk):
    item = get_object_or_404(Item, id=pk)
    random_order = None

    if Order.objects.count() > 1:
        order = Order.objects.values_list('pk', flat=True)
        random_pk = choice(order)
        random_order = Order.objects.get(pk=random_pk)

    context = {
        'item': item,
        'order': random_order,
    }

    return render(request, 'item_detail.html', context)


def checkout(request, pk):
    item = get_object_or_404(Item, id=pk)
    product = stripe.Product.create(
        name=item.name,
        description=item.description
    )
    price = stripe.Price.create(
        product=product.id,
        unit_amount=int(item.price * 100),
        currency='usd'
    )
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price.id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
    )

    return redirect(checkout_session.url, code=303)


def checkout_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    items = []
    if order.items.count() > 0:
        for item in order.items.all():
            data = {
                'price_data': {
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': item.price * 100,
                    'currency': item.currency,
                },
                'quantity': 1,
            }
            items.append(data)

    checkout_session = stripe.checkout.Session.create(
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
    )

    return redirect(checkout_session.url, code=303)
