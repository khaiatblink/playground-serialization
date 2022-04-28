from marshmallow import fields, EXCLUDE, Schema, post_load

from models import Patient

class ContactNumberSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    contact_number_type = fields.String()
    contact_number = fields.String()


class PatientSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    first_name = fields.String()
    middle_name = fields.String(required=False, load_default=None)
    last_name = fields.String()
    suffix = fields.String(required=False, load_default=None)
    birth_date = fields.Date()
    # contact_numbers = fields.Nested(ContactNumberSchema, required=False, allow_none=True, load_default=[])
    email = fields.Email(required=False, allow_none=True, load_default=None)
    zip_code = fields.String(required=False, load_default=None)

    @post_load
    def _create_instance(self, data, **kwargs):
        return Patient(**data)
