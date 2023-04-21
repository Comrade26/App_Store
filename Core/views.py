from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('Buyer:login')
