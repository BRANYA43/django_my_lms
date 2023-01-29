from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateTeacherForm
from .forms import UpdateTeacherForm
from .models import Teacher


def get_render_list(request: HttpRequest):
    teachers = Teacher.objects.all().order_by('first_name')
    return render(request=request,
                  template_name='teachers/list.html',
                  context={'teachers': teachers})


def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request=request,
                  template_name='teachers/create.html',
                  context={'form': form})


def get_render_update(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request=request,
                  template_name='teachers/update.html',
                  context={'form': form})


def get_render_detail(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    return render(request=request,
                  template_name='teachers/detail.html',
                  context={'teacher': teacher})


def get_render_delete(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request=request,
                  template_name='teachers/delete.html',
                  context={'teacher': teacher})