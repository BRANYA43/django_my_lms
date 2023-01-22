from django.db import models

from .validators import validate_start_date


class Group(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField(validators=[validate_start_date])
    description = models.TextField(null=True, blank=True)

    class Meta:
        __tablename__ = 'groups'
