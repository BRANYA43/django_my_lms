from django.contrib import admin
from django.urls import path, re_path

from groups.views import get_render_list_group, get_render_create_group, get_render_update_group, get_render_detail_group
from students.views import get_students, create_student_view, update_student, detail_student
from students.views import index
from students.views import view_with_param
from students.views import view_without_param
from groups.views import get_render_list_group, get_render_create_group, get_render_update_group, get_render_detail_group
from teachers.views import get_render_list_teacher, get_render_create_teacher, get_render_update_teacher, get_render_detail_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('groups/', get_render_list_group),
    path('groups/', get_render_list_group),
    path('groups/create/', get_render_create_group),
    path('groups/update/<int:pk>/', get_render_update_group),
    path('groups/detail/<int:pk>/', get_render_detail_group),
    path('teachers/', get_render_list_teacher),
    path('teachers/create/', get_render_create_teacher),
    path('teachers/update/<int:pk>/', get_render_update_teacher),
    path('teachers/detail/<int:pk>/', get_render_detail_teacher),

    # path('test/route/param/', view_without_param),          # test/route/param/
    # path(r'test/route/<str:value>/', view_with_param),       # test/route/df;lkjhrlkjgf's/
]
