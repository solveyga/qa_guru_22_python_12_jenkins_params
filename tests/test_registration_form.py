import pytest
import os
from selene import browser, have, be
from selenium import webdriver


@pytest.fixture
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    yield
    browser.element('#closeLargeModal').click()
    browser.quit()


def test_submit_form_with_all_filled_fields(browser_settings):
    browser.element('#firstName').set_value('Firstname')

    browser.element('#lastName').set_value('Lastname')

    browser.element('#userEmail').set_value('first_last@example.com')

    browser.element("label[for='gender-radio-2']").click()

    browser.element('#userNumber').set_value('9110000000')

    # browser.execute_script(
    #    'document.querySelectorAll("#google_ads_iframe_, [id^=google_ads_]")'
    #    '.forEach(element => element.remove())'
    # )

    browser.element('#dateOfBirthInput').click()  # .should(be.visible).should(be.clickable).click()
    browser.element('.react-datepicker__month-select').element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="2000"]').click()
    browser.element('.react-datepicker__day--010').click()

    browser.element('#subjectsInput').type('English').press_enter()

    browser.element("label[for='hobbies-checkbox-2']").click()  # .should(be.visible).should(be.clickable).click()
    # browser.element("#hobbies-checkbox-2").should(have.attribute("checked"))

    browser.element('#currentAddress').set_value('2920 Zoo Dr, San Diego, CA 92101')

    browser.element('#uploadPicture').type(os.path.abspath('flower.jpg'))

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()

    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.element('#submit').click()

    browser.element('.table-responsive').all('td').should(
        have.texts(
            'Student Name', 'Firstname Lastname',
            'Student Email', 'first_last@example.com',
            'Gender', 'Female',
            'Mobile', '9110000000',
            'Date of Birth', "10 January,2000",
            'Subjects', 'English',
            'Hobbies', 'Reading',
            'Picture', 'flower.jpg',
            'Address', '2920 Zoo Dr, San Diego, CA 92101',
            'State and City', 'Uttar Pradesh Agra'
        )
    )