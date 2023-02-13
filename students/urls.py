
from django.urls import path

from .views import get_students, UpdateStudentView
from .views import create_student_view
from .views import update_student
from .views import detail_student
from .views import delete_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student_view, name='create'),
    # path('update/<int:pk>/', update_student, name='update'),
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
