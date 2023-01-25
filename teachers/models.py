from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        __tablename__ = 'teachers'

    def __repr__(self):
        return f'<Teacher({self.first_name} {self.last_name})>'

    @classmethod
    def generate_data(cls, count: int):
        faker = Faker()
        for _ in range(count):
            teacher = cls()
            teacher.first_name = faker.first_name()
            teacher.last_name = faker.last_name()
            teacher.email = f'{teacher.first_name}@test.com'
            teacher.save()
