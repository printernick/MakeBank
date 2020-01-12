from django.shortcuts import render

def home(request):
    return render(request, 'bank/home.html')

def account(request):
    return render(request, 'bank/account.html', {"title": "account"})