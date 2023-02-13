import re

from django import forms
from django_filters import FilterSet

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'city',
            'phone',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()

    def clean_phone(self):
        pattern = r'\d+'
        ret = '+38 '
        value = self.cleaned_data.get('phone')
        value = ''.join(re.findall(pattern, value))
        if value[:2] == '38':
            value = value[2:]
        ret += f'({value[:3]}) {value[3:6]}-{value[6:8]}-{value[-2:]}'
        return ret


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'contains'],
            'last_name': ['exact', 'startswith'],
        }