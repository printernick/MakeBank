from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bank Home</h1>")

def account(request):
    return HttpResponse("<h1>Bank Account</h1>")