from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course

def coursePage(request,slug):

    course=Course.objects.get(slug=slug)
    context={
        "course":course
    }
    return render(request,template_name="courses/course_page.html",context=context)