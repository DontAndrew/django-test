from django.shortcuts import render

from .models import Lead

# Create your views here.
def home(request):
    leads = Lead.objects.all()
    contexts = {
        "leads" : leads,
        "name" : "drew",
        "age" : "2",
    }
    return render(request, "home.html", contexts)

def lead(request):

    return render(request, "leads/leads.html")