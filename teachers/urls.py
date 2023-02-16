from django.urls import path

from .views import TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDetailView, TeacherDeleteView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', TeacherDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete')
    ]
