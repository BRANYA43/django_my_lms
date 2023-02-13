from django.urls import path

from courses.views import CourseListView, CourseCreateView, CourseUpdateView, CourseDetailView, CourseDeleteView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
    ]
