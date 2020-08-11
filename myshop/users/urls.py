from django.urls import path
from .views import SignUpView, SignInView
from users import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]