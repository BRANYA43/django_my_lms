from django import forms
from django.contrib import admin

from groups.models import Group


class TeacherInlineTable(admin.TabularInline):
    verbose_name_plural = 'teachers'
    model = Group.teachers.through
    extra = 0
    fields = (
        'get_first_name',
        'get_last_name',
        'get_salary',
    )
    readonly_fields = (
        "get_first_name",
        'get_last_name',
        'get_salary',
    )

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @staticmethod
    def get_teacher_attr(instance, name: str) -> str:
        if instance:
            return instance.teacher.__getattribute__(name)

    def get_first_name(self, instance):
        return self.get_teacher_attr(instance, 'first_name')

    def get_last_name(self, instance):
        return self.get_teacher_attr(instance, 'last_name')

    def get_salary(self, instance):
        return f'${self.get_teacher_attr(instance, "salary")}'

    get_first_name.short_description = 'first name'
    get_last_name.short_description = 'last name'
    get_salary.short_description = 'salary'


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email', 'phone')
    extra = 0
    readonly_fields = ('first_name', 'last_name', 'email', 'phone')

    # show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].choices = [(s.pk, f'{s.first_name} {s.last_name}') for s in self.instance.students.all()]
        self.fields['headman'].choices.insert(0, (0, '<headman>'))

        self.fields['headman'].widget.can_add_related = False
        self.fields['headman'].widget.can_change_related = False
        self.fields['headman'].widget.can_view_related = False
        self.fields['headman'].widget.can_delete_related = False

    class Meta:
        model = Group
        fields = '__all__'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_filter = ('title', 'start_date', 'end_date')
    form = GroupAdminForm
    fields = (
        'title',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
        ('create', 'update')
    )

    readonly_fields = (

        'create',
        'update',
    )
    inlines = [StudentInlineTable, TeacherInlineTable]
