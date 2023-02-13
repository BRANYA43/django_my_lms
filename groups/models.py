from django.db import models
from faker import Faker

from teachers.models import Teacher
from .validators import validate_start_date


class Group(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField(validators=[validate_start_date])
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    headman = models.OneToOneField('students.Student', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='headman_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'

    @classmethod
    def generate_data(cls):
        faker = Faker()
        for title in 'Python', 'C1/C++', 'C#', 'Ruby', 'Java', 'JavaScript', 'Assembler', 'HTML+CSS':
            group = cls()
            group.title = title
            group.start_date = faker.date_between(start_date='+0y', end_date='+5y')
            group.description = faker.text()
            group.save()
