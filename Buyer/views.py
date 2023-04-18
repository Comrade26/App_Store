from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.shortcuts import render, redirect
# from .forms import BuyerLoginForm

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             customer = Customer.objects.create(
#                 user=user,
#                 phone_number=request.POST.get('phone_number'),
#                 address=request.POST.get('address'),
#                 city=request.POST.get('city'),
#                 state=request.POST.get('state'),
#                 country=request.POST.get('country'),
#             )
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def buyer_login(request):
#     if request.method == 'POST':
#         form = BuyerLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('buyer_profile')
#     else:
#         form = BuyerLoginForm()
#     return render(request, 'buyer_login.html', {'form': form})

# def buyer_logout(request):
#     logout(request)
#     return redirect('home')