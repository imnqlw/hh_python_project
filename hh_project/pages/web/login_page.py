import allure
from selene import browser, have

from tests.mobile.conftest import name, passw


class LoginPage:
    @allure.step('Открытие страницы')
    def open(self):
        browser.open('/')

    @allure.step('Авторизация')
    def login(self):
        browser.open('https://saratov.hh.ru/')
        browser.element('[href="/account/login?backurl=%2F&hhtmFrom=main"]').click()
        browser.element('[data-qa="expand-login-by-password"]').click()
        browser.element('[data-qa="login-input-username"]').type(name)
        browser.element('[data-qa="login-input-password"]').type(passw)
        browser.element('[data-qa="account-login-submit"]').click()

    @allure.step('Проверка авторизации')
    def check_login(self):
        browser.element('[data-qa="mainmenu_applicantProfile"]').click()
        browser.element('[href="/applicant/settings?from=header_new&hhtmFromLabel=header_new&hhtmFrom=main"]').click()
        browser.element('[data-template-name="fio"]').should(have.text('Quru'))


login_page = LoginPage()
