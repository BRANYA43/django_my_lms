from django import forms

from courses.models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass
