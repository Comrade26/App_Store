from django.shortcuts import render
from django.views import View

# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, "homepage.html", {})
    
class Base(View):
    def get(self, request):
        return render(request, "start_page_base.html", {})
    
class Landing_page(View):
    def get(self, request):
        return render(request, "landing_page.html", {})