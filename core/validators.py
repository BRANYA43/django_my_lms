import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALID_DOMAINS = ('gmail.com',
                 'yahoo.com',)


def validate_email_domain(value: str):
    domain = value.split('@')[1]
    if domain not in VALID_DOMAINS:
        raise ValidationError(f'Email domain {domain} is not correct.')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains: tuple):
        self.domains = tuple(domains) if domains else VALID_DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[1]
        if domain not in self.domains:
            raise ValidationError(f'This email domain {domain} is not correct.')


def validate_email_unique(value: str):
    from .models import Student
    emails = [email['email'] for email in Student.objects.values('email').order_by('email')]

    if value in emails:
        raise ValidationError(f'Email: {value} is not unique.')


def validate_phone_number(value: str):
    pattern = r'^(\+38)?\s?(0\d\d|\(0\d\d\))\s?(\d{3}(\s|\-)?\d{2}(\s|\-)?\d{2}|\d{2}(\s|\-)?\d{3}(\s|\-)?\d{2}|\d{2}(\s|\-)?\d{2}(\s|\-)?\d{3})$'
    if re.search(pattern, value) is None:
        raise ValidationError(
            '''Phone number is not correct.
Examples correct phone number:
    +380XXXXXXXXX
    +38 0XX XXX XX XX
    +38 0XX XX XXX XX
    +38 0XX XX XX XXX
    +0XXXXXXXXX
    0XX XXX XX XX
    0XX XX XXX XX
    0XX XX XX XXX''')
