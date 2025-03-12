from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.views import View
from .forms import CourseForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CourseInfo(LoginRequiredMixin, View):
    login_url = 'singup'
    def get(self, request, pk):
        user = request.user
        course = get_object_or_404(Course, pk=pk)
        return render(request, template_name='info.html', context={'user':user, 'course':course})
    

class AddCourse(View):
    def get(self, r):
        return render(r, template_name='addcourse.html', context={'form': CourseForm()})
    
    def post(self, r):
        form = CourseForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
            return redirect('interface')
        return render(r, template_name='addcourse.html', context={'form':form})
    

class EditCourse(View):
    def get(self, r, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        return render(r, 'addcourse.html', {'form': form, 'course': course})

    def post(self, r, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(r.POST, r.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('interface')
        return render(r, 'addbook.html', {'form': form, 'course': course})
    
class DeleteCourse(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'delete.html', {'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('interface')