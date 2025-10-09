import dataclasses
from dataclasses import dataclass, field
from datetime import date
from enum import Enum


@dataclasses.dataclass
class User:
    first_name: str =  'Firstname'
    last_name: str = 'Lastname'
    email: str = 'first_last@example.com'
    gender: str =  'Female'
    phone: str =  '9110000000'
    # date_of_birth: date = date(2000, 1, 1)
    year: str = '2000'
    month: str = 'January'
    day: str = '11'
    subjects: list = field(default_factory=lambda: ['Computer Science', 'English'])
    hobbies: list = field(default_factory=lambda: ['Reading', 'Music'])
    address: str = '2920 Zoo Dr, San Diego, CA 92101'
    state: str = 'Uttar Pradesh'
    city: str = 'Agra'
    photo: str = 'flower.jpg'
