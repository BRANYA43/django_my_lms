import re

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
            'phone',
        ]
        exclude = [

        ]

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()

    # def clean_phone(self):
    #     ret = ''
    #     value = self.cleaned_data.get('phone')
    #     for elem in value:
    #         if elem.isdigit():
    #             ret += elem
    #         elif elem in '()-+':
    #             ret += elem
    #     return ret

    def clean_phone(self):
        pattern = r'\d+'
        ret = '+38 '
        value = self.cleaned_data.get('phone')
        value = ''.join(re.findall(pattern, value))
        if value[:2] == '38':
            value = value[2:]
        ret += f'({value[:3]}) {value[3:6]}-{value[6:8]}-{value[-2:]}'
        return ret
