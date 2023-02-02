from django import forms

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name',
                  'last_name',
                  'birthday',
                  'salary',
                  'email',
                  ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name',
                  'last_name',
                  'birthday',
                  'salary',
                  'email',
                  ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }