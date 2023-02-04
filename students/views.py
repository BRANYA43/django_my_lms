from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from webargs.fields import Str
from webargs.djangoparser import use_args

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
                  context={'title': 'Detail of student', 'student': student})


# @csrf_exempt
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form .is_valid():
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

