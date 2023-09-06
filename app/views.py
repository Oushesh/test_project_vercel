from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def home(request):
    return render(request,'home.html',{'posts':BlogPost.objects.all()})

