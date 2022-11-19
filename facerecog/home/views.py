import email
from math import degrees
from django.db.models import Q
from multiprocessing import context
from pydoc import classname
from select import select
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.template import RequestContext
from home.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
from django.contrib.sessions import *
import cv2
import face_recognition
import numpy as np
import sqlite3

from .forms import ProfileForm


# Create your views here.

def home(request):
    if request.method == 'POST':

        username = request.POST['email']
        passw = request.POST['password']
        try:
            TeacherLogin = Profile.objects.get(email=username, password=passw)
            # email=TeacherLogin.email
            # password = TeacherLogin.password

            # if email == username and password == passw:
            # if Profile.objects.get(email=username,password=passw):
            messages.success(request, "Success")
            print("login seccess")
            request.session['user_id'] = TeacherLogin.id
            request.session['user_email'] = TeacherLogin.email
            return redirect('takePresenty')

        except Profile.DoesNotExist:
            TeacherLogin = None
            messages.error(request, "login failed")
            print("login failed")
            return render(request, 'login.html')

    return render(request, 'login.html')


def adminDashboard(request):
    return render(request, 'adminDashboard.html')


def addStudent(request):
    selectclass = Class.objects.all()
    context = {'success': False}
    if request.POST.get('degree'):
        first = request.POST['first_name']
        middle = request.POST['middle_name']
        last = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        type = 'student'
        degree = request.POST['degree']
        if len(request.FILES) != 0:
            image = request.FILES['image']
        print(first, last, middle, phone, email, date, degree, image)
        savevalue = Profile(first_name=first, middle_name=middle, last_name=last, phone=phone, email=email, date=date,
                            degree=degree, image=image, type=type)
        savevalue.save()
        messages.info(request, 'Student added successfully...')
        return render(request, 'addStudent.html')
    else:
        return render(request, 'addStudent.html', {"Class": selectclass})


def addTeacher(request):
    context = {'success': False}
    if request.method == "POST":
        first = request.POST['first_name']
        middle = request.POST['middle_name']
        last = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        type = 'teacher'
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            password = password1
        else:
            messages.success(request, 'Password and Conform Password not matched.....!')
            return render(request, 'addTeacher.html')
        if len(request.FILES) != 0:
            image = request.FILES['image']
        print(first, last, middle, phone, email, date, password, image)
        # if password1== password2:
        savenewvalue = Profile(first_name=first, middle_name=middle, last_name=last, phone=phone, email=email,
                               date=date, password=password, image=image, type=type)

        savenewvalue.save()
        context = {'success': True}
        messages.success(request, 'The class ' + savenewvalue.password + 'is added successfully...')
        return render(request, 'addTeacher.html', context)

    else:
        return render(request, 'addTeacher.html')


def attendanceReport(request):
    return render(request, 'attendanceReport.html')


def attendanceSheet(request):
    return render(request, 'attendanceSheet.html')


def takePresenty(request):
    if request.method == "POST":
        degree = request.POST['degree']
        # classname=request.POST['class']
        degreename = Profile.objects.filter(type='student')
        for i in degreename:
            if i.degree == degree:
                print(i.first_name)
    print(request.session.get('user_id'))
    print(request.session.get('user_email'))
    selectclass = Class.objects.all()
    selectsubject = Subject.objects.all()
    return render(request, 'takePresenty.html', {"Class": selectclass, "Subject": selectsubject})


def addSubject(request):
    if request.method == "POST":
        if request.POST.get('degree'):
            classname = Class()
            classname.class_name = request.POST.get('degree')
            classname.save()
            messages.info(request, "Degree added successfully")
            return render(request, 'addSubject.html')
        if request.POST.get('subject'):
            subjectname = Subject()
            subjectname.subject_name = request.POST.get('subject')
            subjectname.save()
            messages.info(request, "Subject added successfully")
            return render(request, 'addSubject.html')
    else:
        return render(request, 'addSubject.html')


def scan(request):
    degree = request.POST['degree']
    print(degree)
    print('suman is actiavated')
    known_face_encodings = []
    known_face_names = []

    # profiles = Profile.objects.all()
    profiles = Profile.objects.filter(degree=degree)
    for profile in profiles:
        person = profile.image
        image_of_person = face_recognition.load_image_file(f'media/{person}')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(f'{person}'[:-4])

    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)

                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    profile = Profile.objects.get(Q(image__icontains=name))
                    # print(name)
                    # if profile.present == True:
                    #    pass
                    # else:
                    #    profile.present = True
                    #   profile.save()
                else:
                    print(name)

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return render(request, 'attendanceSheet.html')
    ''' if request.POST.get('degree'):
            first_name=request.POST['first_name']
            print(first_name)
            savevalue=Users()
            savevalue.degree=request.POST.get('degree')
            savevalue.save()
            messages.success(request,'The class '+savevalue.degree+'is added successfully...')
            return render(request, 'addStudent.html')'''
