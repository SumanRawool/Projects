from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course, Video
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method =="GET":
        form=UserCreationForm()
        return render(request, template_name="courses/signup.html",context={'form':form})
    return HttpResponse("POST REQUEST")
def login(request):
    return render(request,template_name="courses/login.html")