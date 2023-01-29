from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

from core.views import index
from teachers.views import get_render_list_teacher, get_render_create_teacher, get_render_update_teacher, get_render_detail_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('teachers/', get_render_list_teacher),
    path('teachers/create/', get_render_create_teacher),
    path('teachers/update/<int:pk>/', get_render_update_teacher),
    path('teachers/detail/<int:pk>/', get_render_detail_teacher),

    # path('test/route/param/', view_without_param),          # test/route/param/
    # path(r'test/route/<str:value>/', view_with_param),       # test/route/df;lkjhrlkjgf's/
]
