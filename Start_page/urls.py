
from django.contrib import admin
from django.urls import path, re_path
from .views import Homepage, Base, Landing_page


# URLConf
urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("base/", Base.as_view(), name="base"),
    path("landing_page/", Landing_page.as_view()),
    ]