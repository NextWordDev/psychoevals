class Eval:
    def __init__(self, **kwargs):
        self._fields = kwargs

    def get_field(self, field_name):
        return self._fields.get(field_name)

    def set_field(self, field_name, value):
        self._fields[field_name] = value

    def get_all_fields(self):
        return self._fields

    def __getattr__(self, field_name):
        return self.get_field(field_name)

    def __str__(self):
        return str(self._fields)
