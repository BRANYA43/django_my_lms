import datetime
from decimal import Decimal
from random import randint

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=10_000)

    class Meta(PersonModel.Meta):
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    def __repr__(self):
        return f'<Teacher({self.first_name} {self.last_name})>'

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = randint(10_000, 100_000)
        return teacher
