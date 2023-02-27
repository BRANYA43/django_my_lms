from django.contrib import admin

from .models import Teacher


class GroupInlineTable(admin.TabularInline):
    verbose_name_plural = 'groups'
    model = Teacher.groups.through
    extra = 0
    fields = (
        'get_title',
    )
    readonly_fields = (
        "get_title",
    )

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @staticmethod
    def get_group_attr(instance, name: str):
        if instance:
            return instance.group.__getattribute__(name)

    def get_title(self, instance):
        return self.get_group_attr(instance, 'title')

    get_title.short_description = 'title'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = list_display
    list_per_page = 15
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthday', 'get_age'),)}),
        ('Contact', {'fields': (('email', 'city', 'phone'),)}),
        (' ', {'fields': ('salary',)},),
    )

    def get_age(self, instance):
        return f'{instance.get_age()} year(s)'

    get_age.short_description = 'age'
    readonly_fields = (
        'get_age',
    )
    inlines = [GroupInlineTable, ]
