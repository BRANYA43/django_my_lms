from django.contrib import admin

from students.models import Student


class GroupListFilter(admin.SimpleListFilter):
    from groups.models import Group
    title = 'group'
    parameter_name = 'group_filter'

    def lookups(self, request, model_admin):
        groups = self.Group.objects.all()
        data = [(group.pk, group.title) for group in groups]
        data.insert(0, (0, 'no group'))
        return tuple(data)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                students = Student.objects.all()
            case '0':
                students = Student.objects.filter(group__isnull=True)
            case _:
                students = Student.objects.filter(group=self.Group.objects.get(pk=int(self.value())))
        return students.order_by('first_name', 'last_name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_group_info')
    list_display_links = list_display
    list_per_page = 15
    # list_filter = ('group__title',)
    list_filter = (GroupListFilter,)
    search_fields = ('first_name', 'last_name')

    def get_group_info(self, instance):
        if instance.group:
            return instance.group.title
        else:
            return ''

    get_group_info.short_description = 'group'
    #
    # fields = (
    #     ('first_name', 'last_name'),
    #     ('birthday', 'get_age'),
    #     ('email', 'city'),
    #     'group',
    # )

    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthday', 'get_age'),)}),
        ('Contact', {'fields': (('email', 'city'),)}),
        (' ', {'fields': ('group',)},),
    )

    def get_age(self, instance):
        return f'{instance.get_age()} year(s)'

    get_age.short_description = 'age'
    readonly_fields = (
        'get_age',
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['group'].widget.can_add_related = False
        form.base_fields['group'].widget.can_change_related = False
        form.base_fields['group'].widget.can_view_related = False
        form.base_fields['group'].widget.can_delete_related = False

        return form


admin.site.register(Student, StudentAdmin)
