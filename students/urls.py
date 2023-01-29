
from django.urls import path, re_path

from .views import get_students
from .views import create_student_view
from .views import update_student
from .views import detail_student
from .views import delete_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student_view, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
