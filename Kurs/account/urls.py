from django.urls import path
from .views import Welcome, about, contact, singup, login_user, logout_user, interface
urlpatterns = [
    path('', Welcome.as_view(), name='welcome'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('singup/', singup, name='singup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('interface/', interface, name='interface'),
]