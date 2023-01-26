from django.contrib import admin
from django.urls import path, re_path

from students.views import get_students, create_student_view, update_student, detail_student
from students.views import index
from students.views import view_with_param
from students.views import view_without_param
from teachers.views import get_render_list, get_render_create, get_render_update, get_render_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('teachers/', get_render_list),
    path('teachers/create/', get_render_create),
    path('teachers/update/<int:pk>/', get_render_update),
    path('teachers/detail/<int:pk>/', get_render_detail)

    # path('test/route/param/', view_without_param),          # test/route/param/
    # path(r'test/route/<str:value>/', view_with_param),       # test/route/df;lkjhrlkjgf's/
]
