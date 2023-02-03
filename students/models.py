import datetime
from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.validators import validate_phone_number

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name',
                                  validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthday = models.DateField(default=date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[])
    phone = models.CharField(max_length=20, validators=[validate_phone_number])
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        __tablename__ = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday} {self.email}'

    @classmethod
    def generate_fake_data(cls, count: int):
        faker = Faker()
        for _ in range(count):
            student = cls()
            student.first_name = faker.first_name()
            student.last_name = faker.last_name()
            student.email = f'{student.last_name}@{faker.random.choice(VALID_DOMAINS)}'
            student.birthday = faker.date_between(start_date='-65y', end_date='-18y')
            student.phone = f'0{faker.random_int(min=100000000, max=9999999999)}'
            student.save()

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years
