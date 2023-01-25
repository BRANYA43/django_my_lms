from django.shortcuts import render

from .models import Group


def get_render_list(request):
    groups = Group.objects.all().order_by('start_date')
    return render(request=request,
                  template_name='groups/list.html',
                  context={'title': 'List of Group', 'groups': groups})

