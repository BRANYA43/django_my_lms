from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from students.models import Student
from .forms import GroupCreateForm, GroupUpdateForm
from .models import Group


def get_render_list(request: HttpRequest):
    groups = Group.objects.all().order_by('start_date')
    return render(request=request,
                  template_name='groups/list.html',
                  context={'groups': groups})


def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = GroupCreateForm()
        return render(request=request,
                      template_name='groups/create.html',
                      context={'form': form})

    elif request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))


def get_render_update(request: HttpRequest, pk: int):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'GET':
        form = GroupUpdateForm(instance=group, initial=students)
        return render(request=request,
                      template_name='groups/update.html',
                      context={'form': form, 'group': group})
    elif request.method == 'POST':
        form = GroupUpdateForm(data=request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))


def get_render_detail(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    return render(request=request,
                  template_name='groups/detail.html',
                  context={'group': group})


def get_render_delete(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        print('POST')
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request=request,
                  template_name='groups/delete.html',
                  context={'group': group})
