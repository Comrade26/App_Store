from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, EditProfileForm, EditVendorForm
from .models import User, chula_email_validator
from Vendor.models import Vendor


class BuyerLoginView(LoginView):
    template_name = 'login.html'

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('Core:login')

@login_required
def profile(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    context = {'user': request.user, 'vendor': vendor}
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    vendor_user = request.user
    user = request.user
    vendor = Vendor.objects.filter(user=user).first()
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=user)
        vendor_form = EditVendorForm(request.POST, instance=vendor)
        if user_form.is_valid() and vendor_form.is_valid():
            user_form.save()
            vendor_form.save()
            messages.success(request, "Profile has been updated successfully.")
            return redirect('Core:profile')
    else:
        user_form = EditProfileForm(instance=user)
        vendor_form = EditVendorForm(instance=vendor)
    context = {'user_form': user_form, 'vendor_form': vendor_form, 'vendor_user': vendor_user}
    return render(request, 'edit_profile.html', context)

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('Core:profile')
    template_name = 'change_password.html'

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)

def my_logout_view(request):
    logout(request)
    return redirect('/')