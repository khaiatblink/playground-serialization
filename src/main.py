import json
from serializers import PatientSchema


def main():
    initial_data = {"patient": {
                "first_name": "John",
                "last_name": "Doe",
                "birth_date": "1999-01-01",
                "contact_numbers": [{
                    "contact_number_type": "Mobile",
                    "contact_number": "9999999999"
                }],
                "email": None,
                "zip_code": "90001",
                "gender": "M",
            },}
    json_payload = json.dumps(initial_data)
    patient_payload = json.loads(json_payload).get("patient")

    patient = PatientSchema().load(patient_payload)
    print(patient)

main()
