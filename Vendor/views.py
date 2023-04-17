# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def vendor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_vendor:
                login(request, user)
                return redirect('vendor_dashboard')
            else:
                return render(request, 'vendor/login.html', {'error_message': 'You are not a vendor.'})
        else:
            return render(request, 'vendor/login.html', {'error_message': 'Invalid login credentials.'})
    else:
        return render(request, 'vendor/login.html')

def vendor_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_vendor = True
            user.save()
            login(request, user)
            return redirect('vendor_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'vendor/signup.html', {'form': form})
