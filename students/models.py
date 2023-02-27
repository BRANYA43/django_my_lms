from random import choice

from django.db import models

from core.models import PersonModel

from groups.models import Group


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        ret = f'{self.first_name} {self.last_name}'
        if self.group:
            ret += f' ({self.group.title})'
        else:
            ret += ' ()'
        return ret

    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        return student
