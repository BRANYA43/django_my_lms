from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from courses.forms import CourseCreateForm, CourseUpdateForm
from courses.models import Course


# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    queryset = Course.objects.all()
    template_name = 'courses/list.html'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class CourseDetailView(DetailView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/detail.html'


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
