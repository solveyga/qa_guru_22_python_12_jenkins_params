from selene import have, command
from selene.support.shared import browser
from pathlib import Path
from data.users import User, Gender, Hobby


class RegistrationPage:

    GENDER_MAP = {
        Gender.MALE: "label[for='gender-radio-1']",
        Gender.FEMALE: "label[for='gender-radio-2']",
        Gender.OTHER: "label[for='gender-radio-3']"
    }

    HOBBIES_MAP = {
        Hobby.SPORTS: "label[for='hobbies-checkbox-1']",
        Hobby.READING: "label[for='hobbies-checkbox-2']",
        Hobby.MUSIC: "label[for='hobbies-checkbox-3']"
    }

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.address = browser.element('#currentAddress')
        self.photo = browser.element('#uploadPicture')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')


    def open(self):

        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

        return self


    def fill_gender(self, gender):
        browser.element(self.GENDER_MAP[gender]).click()
        return self


    def fill_hobbies(self, *hobbies: Hobby):
        for hobby in hobbies:
            browser.element(self.HOBBIES_MAP[hobby]).click()
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)

        self.fill_gender(user.gender)

        self.phone.type(user.phone)
        self.date_of_birth.click()
        month_index = user.date_of_birth.month - 1
        browser.element('.react-datepicker__month-select').element(f'option[value="{month_index}"]').click()
        browser.element('.react-datepicker__year-select').element(f'option[value="{user.date_of_birth.year}"]').click()
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)'
        ).click()

        for subject in user.subjects:
            self.subjects.type(subject).press_enter()

        self.fill_hobbies(*user.hobbies)

        self.address.type(user.address)

        self.photo.send_keys(Path(f'resources/{user.photo}').absolute().__str__())

        self.state.click()
        browser.all('#state div').element_by(have.exact_text(user.state)).click()
        self.city.click()
        browser.all('#city div').element_by(have.exact_text(user.city)).click()

        self.submit.click()
        return self


    def should_have_registered(self, user: User):

        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender.value,
            user.phone,
            user.date_of_birth.strftime('%d %B,%Y'),
            ', '.join(user.subjects),
            ', '.join([hobby.value for hobby in user.hobbies]),
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        ))
        return self


