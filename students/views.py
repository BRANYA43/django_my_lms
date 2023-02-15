from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView

from core.views import CustomUpdateBaseView
from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        students = Student.objects.all().order_by('first_name').select_related('group')
        filter_from = StudentFilterForm(data=self.request.GET, queryset=students)
        return filter_from


def detail_student(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request=request,
                  template_name='students/detail.html',
                  context={'student': student})


def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request=request,
                  template_name='students/create.html',
                  context={'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request=request,
                  template_name='students/update.html',
                  context={'form': form})


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request=request,
                  template_name='students/delete.html',
                  context={'student': student})


class CustomUpdateStudentView(CustomUpdateBaseView):
    model = Student
    form_class = UpdateStudentForm
    success_url = 'students:list'
    template_name = 'students/update.html'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
