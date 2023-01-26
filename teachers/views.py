from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from .forms import CreateTeacherForm
from .models import Teacher


def get_render_list(request: HttpRequest):
    teachers = Teacher.objects.all().order_by('first_name')
    return render(request=request,
                  template_name='teachers/list.html',
                  context={'title': 'List of Teachers', 'teachers': teachers})


def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    return render(request=request,
                  template_name='teachers/create.html',
                  context={'token': token, 'title': 'Create new Teacher', 'form': form})


def get_render_update(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    return render(request=request,
                  template_name='teachers/update.html',
                  context={'token': token, 'title': 'Create new Teacher', 'form': form})