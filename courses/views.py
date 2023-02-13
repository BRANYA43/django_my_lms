from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from courses.models import Course


# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    queryset = Course.objects.all()
    template_name = 'courses/list.html'


class CourseCreateView(CreateView):
    ...


class CourseUpdateView(UpdateView):
    ...


class CourseDetailView(DetailView):
    ...


class CourseDeleteView(DeleteView):
    ...
