from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher_id', 'created')

admin.site.register(Course, CourseAdmin)