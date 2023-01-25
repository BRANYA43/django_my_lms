from django import forms

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name',
                  'last_name',
                  'email',
                  ]