from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from .models import Teacher


def get_render_list(request: HttpRequest):
    teachers = Teacher.objects.all().order_by('first_name')
    return render(request=request,
                  template_name='teachers/list.html',
                  context={'title': 'List of Teachers', 'teachers': teachers})
