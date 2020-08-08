from django.urls import path
from shop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("outer/", views.outer, name="outer"),
    path("top/", views.top, name="top"),
    path("skirt/", views.skirt, name="skirt"),
    path("pants/", views.pants, name="pants"),
    path("cart/", views.cart, name="cart"),
    path("cart/checkout/", views.checkout, name="checkout"),
]