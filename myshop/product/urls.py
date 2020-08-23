from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("outer/", views.outer, name='outer'),
    path("top/", views.top, name='top'),
    path("pants/", views.pants, name='pants'),
    path("skirt/", views.skirt, name='skirt'),
]