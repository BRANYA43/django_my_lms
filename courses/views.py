from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from courses.forms import CourseCreateForm, CourseUpdateForm
from courses.models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
