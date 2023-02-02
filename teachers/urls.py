from django.urls import path

from .views import get_render_list
from .views import get_render_create
from .views import get_render_update
from .views import get_render_detail
from .views import get_render_delete

app_name = 'teachers'

urlpatterns = [
    path('', get_render_list, name='list'),
    path('create/', get_render_create, name='create'),
    path('update/<int:pk>/', get_render_update, name='update'),
    path('detail/<int:pk>/', get_render_detail, name='detail'),
    path('delete/<int:pk>/', get_render_delete, name='delete')
    ]
