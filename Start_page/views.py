from django.shortcuts import render
from django.views import View

# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, "homepage.html", {})
    
class Index(View):
    def get(self, request):
        return render(request, "index.html", {})