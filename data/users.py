import dataclasses
from dataclasses import dataclass, field


@dataclasses.dataclass
class User:
    first_name: str =  'Firstname'
    last_name: str = 'Lastname'
    email: str = 'first_last@example.com'
    gender: str =  'Female'
    phone: str =  '9110000000'
    year: str =  '2000'
    month: str =  'January'
    day: str =  '11'
    subjects: list = field(default_factory=lambda: ['Computer Science', 'English'])
    hobbies: list = field(default_factory=lambda: ['Reading', 'Music'])
    address: str = '2920 Zoo Dr, San Diego, CA 92101'
    state: str = 'Uttar Pradesh'
    city: str = 'Agra'
    photo: str = 'flower.jpg'


# admin = User(full_name='admina adminovych', email='super+admin@gmail.com')
# guest = User('harry', 'potter@hg.com')