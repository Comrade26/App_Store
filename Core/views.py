from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User

class BuyerLoginView(LoginView):
    template_name = 'login.html'

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('Core:login')

def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)
