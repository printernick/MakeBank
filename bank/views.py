from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    return render(request, 'bank/home.html')

@login_required
def account(request):
    savings = Product.objects.filter(user=request.user, product_type = "SV")
    checking = Product.objects.filter(user=request.user, product_type = "CH")
    money_market = Product.objects.filter(user=request.user, product_type = "MM")
    CD = Product.objects.filter(user=request.user, product_type = "CD")
    IRA_CD = Product.objects.filter(user=request.user, product_type = "IC")

    context = {
        "title": str(request.user).capitalize(),
        "savings": savings,
        "checking": checking,
        "money_market": money_market,
        "CD": CD,
        "IRA_CD": IRA_CD
    }
    return render(request, 'bank/account.html', context)