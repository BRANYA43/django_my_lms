from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

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


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/delete.html'
    success_url = reverse_lazy('groups:list')
