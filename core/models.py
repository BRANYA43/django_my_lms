import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.validators import ValidateEmailDomain, validate_phone_number


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def _generate(cls):
        return cls()

    @classmethod
    def generate_data(cls, cnt):
        for _ in range(cnt):
            cls._generate().save()


class PersonModel(BaseModel):
    domain = ('gmail.com', 'yahoo.com', 'test.com')
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last_name')
    birthday = models.DateField(default=datetime.date.today, blank=True)  # default='2003-01-01'
    email = models.EmailField(validators=[ValidateEmailDomain(*domain)])
    phone = models.CharField(max_length=20, validators=[validate_phone_number])
    city = models.CharField(max_length=25, null=True, blank=True)

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    class Meta:
        abstract = True

    @classmethod
    def _generate(cls):
        faker = Faker()

        first_name = faker.first_name()
        last_name = faker.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=faker.date_between(start_date='-65y', end_date='-18y'),
            email=f'{first_name}.{last_name}@{faker.random.choice(cls.domain)}',
            phone=f'0{faker.random_int(min=100_000_000, max=999_999_999)}',
            city=faker.city(),
        )
        return obj
