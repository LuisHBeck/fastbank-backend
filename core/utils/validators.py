from django.core.exceptions import ValidationError

class NumberFieldValidator:
    def __init__(self, length, field_name):
        self.length = length
        self.field_name = field_name

    def __call__(self, value):
        if len(str(value)) != self.length:
            raise ValidationError(f'{self.field_name} length needs to be {self.length}')