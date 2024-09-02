from django.shortcuts import render,redirect
from bookApp.models import *
from .models import *
import stripe

# Set up Stripe API key
stripe.api_key = 'sk_test_51PthdTJJgbTVJRUfDxgpENCXFHAanGauijot7cm9yneCQBtmMKqf2caZmM5fq7Bpowj3WYY13SsPxpE3f2M0X85g00DwOPG58z'

# Create your views here.
def userBookDetails(request):
    book=Book.objects.all()
    return render(request, 'user/userBookDetails.html', {'book':book})

def userBookdisplay(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request, 'user/userBookdisplay.html',{'books':book})

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_cost = sum(item.book.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'user/view_cart.html', {'cart_items': cart_items, 'total': total_cost,'total_items':total_items})

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def buy_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_cost = sum(item.book.price * item.quantity for item in cart_items)

    try:
        # Create a Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_cost * 100),  # Convert to cents
            currency='usd',
            payment_method_types=['card'],
            description='Payment for books in cart',
        )
    except stripe.error.CardError as e:
        print(e)
        # Handle card errors
        return render(request, 'user/payment_error.html', {'error': e.user_message})
    except stripe.error.InvalidRequestError as e:
        
        print(e)
        # Handle invalid request errors
        return render(request, 'user/payment_error.html', {'error': e.user_message})
    except Exception as e:
        print(e)
        # Handle other exceptions
        return render(request, 'user/payment_error.html', {'error': 'An error occurred'})

    # Render the payment form
    return render(request, 'user/buy_cart.html', {'payment_intent': payment_intent, 'total': total_cost})

def payment_success(request):
    payment_intent_id = request.GET.get('payment_intent_id')
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    except stripe.error.InvalidRequestError as e:
        print(e)
        # Handle invalid request errors
        return render(request, 'user/payment_error.html', {'error': e.user_message})
    except Exception as e:
        print(e)
        # Handle other exceptions
        return render(request, 'user/payment_error.html', {'error': 'An error occurred'})

    if payment_intent.status == 'succeeded':
        # Update the cart status to "paid"
        cart = Cart.objects.get(user=request.user)
        cart.status = 'paid'
        cart.save()

        # Clear the cart items
        CartItem.objects.filter(cart=cart).delete()

        # Display a success message
        return render(request, 'user/payment_success.html')
    else:
        # Display an error message
        return render(request, 'user/payment_error.html')