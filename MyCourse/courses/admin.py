from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning,Video
# Register your models here.

class VideoAdmin(admin.TabularInline):
    model=Video

class TagAdmin(admin.TabularInline):
    model=Tag

class LearningAdmin(admin.TabularInline):
    model=Learning

class PrerequisteAdmin(admin.TabularInline):
    model=Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin,LearningAdmin,PrerequisteAdmin,VideoAdmin]

admin.site.register(Course,CourseAdmin)
admin.site.register(Video,)
