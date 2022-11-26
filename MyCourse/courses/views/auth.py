from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from courses.models import Course, Video
from courses.forms import RegistrationForm
from django.views import View

class SignupView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, template_name="courses/signup.html", context={'form': form})
    def post(self,request):
        form = RegistrationForm(request.POST)

        if (form.is_valid()):
            user = form.save()
            if (user is not None):
                return redirect('login')
        return render(request, template_name="courses/signup.html", context={'form': form})

def login(request):
    return render(request,template_name="courses/login.html")