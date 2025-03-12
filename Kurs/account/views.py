from django.shortcuts import render, redirect
from django.views import View
from course.models import Course
from django.db.models import Q
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
# Create your views here.

class Welcome(View):
    def get(self, request):
        query = request.GET.get('t', '')
        courses = Course.objects.filter(Q(title__icontains=query)|Q(teacher__icontains=query))
        return render(request, template_name='welcome.html', context={'courses':courses})


def about(request):
    return render(request, template_name='about.html')

def contact(request):
    return render(request, template_name='contact.html')


def singup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password']) 
            user.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'singup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('interface')
    else:
        form = LoginForm()
    return render(request, template_name='login.html', context={'form':form})

def logout_user(request):
    logout(request)
    return redirect('welcome')

def interface(request):
    user = request.user
    courses = Course.objects.all()
    return render(request, template_name='interface.html', context={'user':user, 'courses':courses})