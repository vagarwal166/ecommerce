
from .models import *
from django import views
from django.urls import path
from . import views
from .views import *


app_name = 'buyy'

urlpatterns = [
    path('',views.product,name='product'),
    path("productdetail/<int:pk>/", views.ProductDetail.as_view(), name="productdetail"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),

    path('add/<int:id>/', views.cart_add, name='add'),
    path('tem_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
    # path('payment/', views.PaymentView.as_view(), name="payment"),
]

