from django.core.exceptions import ValidationError


def clean_content(value):

    if value == "abc":
        raise ValidationError("Cannot be abc")
    return value