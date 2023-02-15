from django.urls import path

from groups.views import GroupListView, GroupCreateView, GroupUpdateView
from groups.views import get_render_detail
from groups.views import get_render_delete

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('create/', GroupCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', get_render_detail, name='detail'),
    path('delete/<int:pk>/', get_render_delete, name='delete'),
    ]
