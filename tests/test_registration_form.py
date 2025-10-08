from pages.registration_page import RegistrationPage

def test_registration_form_with_all_fields():

    test_data = {
        'first_name': 'Firstname',
        'last_name': 'Lastname',
        'email': 'first_last@example.com',
        'gender': 'Female',
        'phone': '9110000000',
        'year': '2000',
        'month': 'January',
        'day': '11',
        'subjects': ['Computer Science', 'English'],
        'hobbies': ['Reading', 'Music'],
        'address': '2920 Zoo Dr, San Diego, CA 92101',
        'state': 'Uttar Pradesh',
        'city': 'Agra',
        'photo': 'flower.jpg'
    }

    registration_page = RegistrationPage()
    registration_page.open()

    (
        registration_page
        .fill_first_name(test_data['first_name'])
        .fill_last_name(test_data['last_name'])
        .fill_email(test_data['email'])
        .fill_phone_number(test_data['phone'])
        .fill_gender(test_data['gender'])
        .fill_date_of_birth(test_data['year'], test_data['month'], test_data['day'])
        .fill_subjects(*test_data['subjects'])
        .fill_hobbies(*test_data['hobbies'])
        .fill_address(test_data['address'])
        .upload_photo(test_data['photo'])
        .fill_state(test_data['state'])
        .fill_city(test_data['city'])
        .submit()
    )

    registration_page.should_have_registered(
        full_name=f'{test_data["first_name"]} {test_data["last_name"]}',
        email=test_data['email'],
        gender=test_data['gender'],
        phone=test_data['phone'],
        date_of_birth = f'{test_data["day"]} {test_data["month"]},{test_data["year"]}',
        subjects=', '.join(test_data['subjects']),
        hobbies=', '.join(test_data['hobbies']),
        address=test_data['address'],
        photo = test_data['photo'],
        state_and_city=f"{test_data['state']} {test_data['city']}"
    )
