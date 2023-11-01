from django.core.exceptions import ValidationError

class IntegerFieldValidator:
    def __init__(self, min_length, max_length, field_name):
        self.min_length = min_length
        self.max_length = max_length
        self.field_name = field_name

    def __call__(self, value):
        if len(str(value)) != self.min_length and len(str(value)) != self.max_length:
            raise ValidationError(f'{self.field_name} length needs to be {self.min_length} or {self.max_length}')