from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from courses.models import Course
from students.models import Student
from .forms import GroupCreateForm, GroupUpdateForm
from .models import Group


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupCreateForm
    template_name = 'groups/create.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        response = super().form_valid(form)

        new_groups = form.save()

        students = form.cleaned_data['students']
        for student in students:
            student.group = new_groups
            student.save()

        return response


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/update.html'
    success_url = reverse_lazy('groups:list')

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            if hasattr(student, 'headman_group'):
                group = student.headman_group
                group.headman = None
                group.save()
            student.save()

        headman_pk = int(form.cleaned_data.get('headman_field'))
        if headman_pk:
            form.instance.headman = Student.objects.get(pk=headman_pk)
        else:
            form.instance.headman = None
        form.save()

        return response


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
