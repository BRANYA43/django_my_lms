from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import CreateTeacherForm
from .forms import UpdateTeacherForm
from .models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('update:list')


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
