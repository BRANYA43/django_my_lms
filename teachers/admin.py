from django.contrib import admin

from groups.admin import TeacherInlineTable
from .models import Teacher


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

    inlines = (TeacherInlineTable,)