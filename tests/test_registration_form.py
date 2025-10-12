from pages.registration_page import RegistrationPage
from data.users import User
import allure


@allure.feature("Проверка заполнения формы")
def test_registration_form_with_all_fields():

    user = User()
    registration_page = RegistrationPage()

    open_page(registration_page)
    register_user(registration_page, user)
    check_registration(registration_page, user)


@allure.step('Открыть страницу')
def open_page(registration_page):
    registration_page.open()


@allure.step('Зарегистрировать пользователя')
def register_user(registration_page, user):
    registration_page.register(user)


@allure.step('Проверить регистрацию пользователя')
def check_registration(registration_page, user):
    registration_page.should_have_registered(user)
