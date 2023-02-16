import stripe
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, pk):
    item = get_object_or_404(Item, id=pk)
    context = {
        'item': item,
        'stripe_key': settings.STRIPE_SECRET_KEY
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