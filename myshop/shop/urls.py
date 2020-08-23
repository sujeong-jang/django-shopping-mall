from django.urls import path
from shop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("cart/checkout/", views.checkout, name="checkout"),
    path("board", views.board, name="board"),
]