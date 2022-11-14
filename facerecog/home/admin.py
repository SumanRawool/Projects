from dataclasses import fields
from django.contrib import admin
from home.models import *

# Register your models here.
#admin.site.register(Profile)

class UserAdmin(admin.ModelAdmin):
    model=Profile
    fields=['first_name',
            'middle_name',
           'last_name',
            'phone',
            'email',
            'date',
            'password',
            'image',
            'type']
    list_display=('id',
            'first_name',
            'middle_name',
           'last_name',
            'phone',
            'email',
            'date',
            'password',
            'image',
            'type',
            'degree')
class SubjectAdmin(admin.ModelAdmin):
        model=Subject
        fields=['subject_id','subject_name']
        list_display=('subject_id','subject_name')
class ClassAdmin(admin.ModelAdmin):
        model=Class
        fields=['class_id','class_name']
        list_display=('class_id','class_name')
class LectureAdmin(admin.ModelAdmin):
        model=Lecture
        fields=['classid','subjectid','teacher_id','date']
        list_display=('classid','subjectid','teacher_id','date')
class PresentyAdmin(admin.ModelAdmin):
        model=Presenty
        fields=['lectu_id','stud_id','presenty']
        list_display=('lectu_id','stud_id','presenty')
admin.site.register(Profile,UserAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(Presenty,PresentyAdmin)