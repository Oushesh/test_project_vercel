from django.shortcuts import render

# Create your views here.
from .models import BlogPost, UserActivity
from django.views.generic import CreateView, DetailView

def home(request):
    return render(request,'home.html',{'posts':BlogPost.objects.all()})

class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "index.html"

class ResultView(DetailView):
    model = UserActivity
    template_name = "result.html"
    context_object_name = "user_activity"
