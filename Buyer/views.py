from django.contrib.auth.views import LoginView

class BuyerLoginView(LoginView):
    template_name = 'login.html'
