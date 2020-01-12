from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'MakeBank account created for {username}!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    context = {'form': form, 'title': "Sign Up"}
    return render(request, 'users/register.html', context)