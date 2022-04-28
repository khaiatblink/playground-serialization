from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class ContactNumber:
    contact_number_type: str
    contact_number: str


@dataclass
class Patient:
    first_name: str
    middle_name: Optional[str]
    last_name: str
    suffix: Optional[str]
    birth_date: date
    # contact_numbers: Optional[List[ContactNumber]]
    email: Optional[str]
    zip_code: Optional[str]
