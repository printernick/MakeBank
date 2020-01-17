from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse
from users.forms import UploadFileForm, UserUpdateForm
from .models import Product, Document



@login_required
def profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if user_update_form.is_valid() and upload_file_form.is_valid():
            if 'file' in request.FILES:
                instance = Document(file=request.FILES['file'], user=request.user)
                instance.save()
            user_update_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect("bank-profile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        upload_file_form = UploadFileForm()

    documents = Document.objects.filter(user=request.user)

    context = {
        "title": "Profile",
        "user_update_form": user_update_form,
        "upload_file_form": upload_file_form,
        "documents": documents
    }

    return render(request, 'bank/profile.html', context)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_type', 'money']

    def form_valid(self, form):
        form.instance.user = self.request.user
        if ((form.instance.product_type == "SV" and form.instance.money < 500)
            or (form.instance.product_type == "CH" and form.instance.money < 100)
            or (form.instance.product_type == "MM" and form.instance.money < 1000)
            or (form.instance.product_type == "CD" and form.instance.money < 1)
            or (form.instance.product_type == "IC" and form.instance.money < 1000)):

            messages.warning(self.request, "Below minimum balance")
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('bank-account')

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
        "IRA_CD": IRA_CD,
    }
    return render(request, 'bank/account.html', context)