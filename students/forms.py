from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'city',
        ]
        exclude = [

        ]

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()
