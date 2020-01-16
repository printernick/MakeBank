from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Document
from users.forms import UploadFileForm

def home(request):
    return render(request, 'bank/home.html')

@login_required
def account(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Document(file=request.FILES['file'], user=request.user)
            instance.save()
            messages.success(request, 'Document uploaded successfully!')
    else:
        form = UploadFileForm()

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
        "IRA_CD": IRA_CD,
        "form": form
    }
    print(savings.first()._meta.get_fields())
    return render(request, 'bank/account.html', context)