from django.urls import path
from .views import CourseInfo, AddCourse, EditCourse, DeleteCourse

urlpatterns = [
    path('info/<int:pk>/', CourseInfo.as_view(), name='info'),
    path('addcourse/', AddCourse.as_view(), name='addcourse'),
    path('editcourse/<int:pk>/', EditCourse.as_view(), name='editcourse'),
    path('deletecourse/<int:pk>/', DeleteCourse.as_view(), name='deletecourse'),
]