from selene import have, command
from selene.support.shared import browser
from pathlib import Path


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')

    def open(self):

        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self, gender):
        genders = {
            'Male': "label[for='gender-radio-1']",
            'Female': "label[for='gender-radio-2']",
            'Other': "label[for='gender-radio-3']"
        }
        browser.element(genders[gender]).click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, *subjects):
        for subject in subjects:
            browser.element('#subjectInput').type(subject).press_enter()
        return self

    def fill_hobby(self, *hobbies):
        hobbies_map = {
            'Sports': "label[for='hobbies-checkbox-1']",
            'Reading': "label[for='hobbies-checkbox-2']",
            'Music': "label[for='hobbies-checkbox-3']"
        }
        for hobby in hobbies_map:
            browser.element(hobbies_map[hobby]).click()
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def upload_photo(self, file_name):
        browser.element('#uploadPicture').set_value(
            str(Path(__file__).parent.parent.joinpath('resources', file_name))
        )
        return self

    def fill_state(self, state):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def fill_city(self, city):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit(self):

        browser.element('#submit').click()
        return self

    def should_have_registered(self):
        pass

