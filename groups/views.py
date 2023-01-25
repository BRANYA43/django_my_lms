from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from .forms import CreateGroupForm
from .models import Group


def get_render_list(request):
    groups = Group.objects.all().order_by('start_date')
    return render(request=request,
                  template_name='groups/list.html',
                  context={'title': 'List of Group', 'groups': groups})


def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    return render(request=request,
                  template_name='groups/create.html',
                  context={'token': token,
                           'title': 'Create new Group',
                           'as_table': form.as_table()})

