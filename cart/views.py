from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem, Order, OrderItem
from catalogue.models import ComicBook
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, comic_id):
    comic = get_object_or_404(ComicBook, id=comic_id)
    item, created = CartItem.objects.get_or_create(user=request.user, comic=comic)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:view_cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_cost() for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                comic=item.comic,
                price=item.comic.price,
                quantity=item.quantity
            )
        cart_items.delete()
        return redirect('cart:order_confirmation', order_id=order.id)

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/confirmation.html', {'order': order})
