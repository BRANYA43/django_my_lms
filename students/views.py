from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from core.views import CustomUpdateBaseView
from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


def get_students(request):
    students = Student.objects.all().order_by('birthday')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={'filter_form': filter_form}
    )


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


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
