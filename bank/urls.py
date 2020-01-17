from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='bank-profile'),
    path('account', views.account, name='bank-account'),
    path('product/new/', views.ProductCreateView.as_view(), name='product-create')
]