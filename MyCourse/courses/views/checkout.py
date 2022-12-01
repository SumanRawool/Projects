from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from courses.models import Course, Video, Payment
from time import time
import razorpay
from mycourse.settings import *

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
user = None



def checkout(request, slug):
    course = Course.objects.get(slug=slug)

    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    if action == 'create_payment':
        amount = int((course.price - (course.price * course.discount * 0.01)) * 100)
        currency = "INR"
        notes = {
            "email": user.email,
            "name": f'{user.first_name}{user.last_name}'
        }
        reciept = f"mycourse_{int(time())}"
        order = client.order.create({'receipt': reciept, 'notes': notes, 'amount': amount, 'currency': currency})
        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get(id)
        payment.save()
    context = {
        "course": course,
        "order": order,
        "payment": payment
    }
    return render(request, template_name="courses/check_out.html", context=context)
