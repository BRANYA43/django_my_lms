from datetime import date

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    age = models.PositiveIntegerField()
    birthday = models.DateField(default=date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        __tablename__ = 'students'

