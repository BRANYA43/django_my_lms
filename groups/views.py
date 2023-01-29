from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .forms import CreateGroupForm, UpdateGroupForm
from .models import Group


def get_render_list(request: HttpRequest):
    groups = Group.objects.all().order_by('start_date')
    return render(request=request,
                  template_name='groups/list.html',
                  context={'groups': groups})


def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('groups:list')

    token = get_token(request)
    return render(request=request,
                  template_name='groups/create.html',
                  context={'form': form})


def get_render_update(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    token = get_token(request)
    return render(request=request,
                  template_name='groups/update.html',
                  context={'form': form})


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
