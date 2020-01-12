from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bank-home'),
    path('account', views.account, name='bank-account')
]