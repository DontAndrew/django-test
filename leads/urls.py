

from django.contrib import admin
from django.urls import path

from .views import home, lead

app_name = "leads"

urlpatterns = [
    path('', home),
    path('lead/', lead),

]