from pages.registration_page import RegistrationPage
from data.users import User


def test_registration_form_with_all_fields():

    user = User()
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)

