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
