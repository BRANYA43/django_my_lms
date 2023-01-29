from django.contrib import admin
from django.urls import path, re_path, include

from groups.views import get_render_list, get_render_create, get_render_update, get_render_detail, get_render_delete

app_name = 'groups'

urlpatterns = [
    path('', get_render_list, name='list'),
    path('create/', get_render_create, name='create'),
    path('update/<int:pk>/', get_render_update, name='update'),
    path('detail/<int:pk>/', get_render_detail, name='detail'),
    path('delete/<int:pk>/', get_render_delete, name='delete'),
    ]
