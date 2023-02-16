from django.urls import path

from groups.views import GroupListView, GroupCreateView, GroupUpdateView, GroupDetailView, GroupDeleteView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('create/', GroupCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', GroupDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='delete'),
    ]
