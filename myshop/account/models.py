from django.db import models

class Account(models.Moel):
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator('^09\d{9}$', message="Invalid phone number.")])
    date_joined = model.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "accounts"
