from math import ceil
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from  .models import Product
from django.views.generic.detail import DetailView
from buyy.models import Product
from .models import *
import datetime
# import razorpay
from mysite import settings
from .forms import AddressForm
from django.contrib.auth.decorators import login_required
import cart
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

# client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))

# class PaymentView(View):

#     def post(self, request):
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             form.instance.user = self.request.user
#             form.save()
#         address = form.instance
#         cart = Cart(request)
#         user = request.user
#         today = datetime.datetime.now()
#         final_price = 0
#         order = Order.objects.create(user=user,date=today,amount=final_price)
#         all_orderlines = []
#         for product in cart.cart.values():
#             quantity = int(product.get('quantity'))
#             price = int(product.get('price'))
#             product = int(product.get('product_id'))

#             all_orderlines.append(OrderLine(order=order, product_id=product, quantity=quantity))
#             final_price += price*quantity
#         orderline = OrderLine.objects.bulk_create(all_orderlines)

#         order.amount = final_price 

#         # callback_url = 'http://'+ str(get_current_site(request))+ "/handlerequest/"
#         razorpay_order = client.order.create(dict(amount=final_price*100,currency=settings.order_currency,
#                                             payment_capture='1'))

#         order.order_id = razorpay_order['id']
#         order.save()
#         cart.clear()
#         orderlines = OrderLine.objects.filter(order=order)
#         context = {'order':order,'order_id':razorpay_order['id'],
#                    'final_price':final_price, 'razorpay_merchant_id':settings.razorpay_id,
#                     'orderlines':orderlines, 'address':address}
#         return render(request, 'buyy/payment.html', context)


def product(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params={'no_of_slides':nslides, 'range':range(1,nslides), 'product': products}
    return render(request,'buyy/product.html', params,)

class ProductDetail(DetailView):
    model = Product
    template_name = 'buyy/product_detail.html'


# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("buyy:cart_detail")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("buyy:cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("buyy:cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    q = cart.cart.get(str(product.id))
    if q.get('quantity')==1:
        item_clear(request, id)
    else:
        cart.decrement(product=product)
    return redirect("buyy:cart_detail")




# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("buyy:cart_detail")


# @login_required(login_url="/users/login")
def cart_detail(request):
    form = AddressForm()
    return render(request, 'buyy/cart.html', {'form': form})

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def checkout(request):
    return HttpResponse("We are at checkout")