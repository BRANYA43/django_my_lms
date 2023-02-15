
from django.urls import path

from .views import StudentListView, StudentUpdateView
from .views import create_student_view
from .views import detail_student
from .views import delete_student

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', create_student_view, name='create'),
    # path('update/<int:pk>/', update_student, name='update'),
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
