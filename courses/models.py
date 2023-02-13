from django.db import models
from faker import Faker

from core.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    lesson_count = models.IntegerField(default=12, blank=True, null=True)

    class Meta(BaseModel.Meta):
        db_table = 'courses'

    @classmethod
    def generate_data(cls, cnt):
        faker = Faker()
        for title in 'PythonPro', "Learning not to write shit's code", 'Django', 'Game development':
            obj = cls(title=title,
                      description=faker.text(),
                      lesson_count=faker.pyint(min_value=12, max_value=36, step=4))
            obj.save()
