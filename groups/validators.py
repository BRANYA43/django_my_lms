from datetime import date

from django.core.validators import ValidationError


def validate_start_date(value):
    date_today = date.today()
    if value < date_today:
        raise ValidationError('Group start date can not be in past.')
