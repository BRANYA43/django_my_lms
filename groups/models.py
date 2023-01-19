from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        __tablename__ = 'groups'
