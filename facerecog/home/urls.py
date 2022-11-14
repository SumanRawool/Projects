from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [   
    path('', views.home, name='home'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('addTeacher/', views.addTeacher, name='addTeacher'),
    path('attendanceReport/', views.attendanceReport, name='attendanceReport'),
    path('takePresenty/', views.takePresenty, name='takePresenty'),
    path('scan',views.scan,name='scan'),
    #path('scan/<str:name>',views.scan,name='scan'),
    path('addSubject/', views.addSubject, name='addSubject'),
    path('attendanceSheet/', views.attendanceSheet, name='attendanceSheet'),
    #path('addDegree/', views.addDegree, name='addDegree'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
