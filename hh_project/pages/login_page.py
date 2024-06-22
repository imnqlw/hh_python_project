import allure
from selene import command
from selene import browser, have
from dotenv import load_dotenv
import os

name = os.getenv('name')
passw = os.getenv('passw')
load_dotenv()


@allure.tag("WEB")
class MainPage:

    def load_env(self):
        load_dotenv()

    @allure.step('Открытие страницы')
    def open(self):
        browser.open('/')

    @allure.step('Выбор города')
    def fill_city(self):
        browser.element('.supernova-navi-item_area-switcher-button').click()
        browser.element('[href="https://saratov.hh.ru/?customDomain=1"]').click()

    @allure.step('Выбор компании')
    def search_company(self):
        browser.element('#a11y-search-input').type('Qiwi').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('[href="/employer/3125"]').click()

    @allure.step('Выбор работы')
    def fill_resume(self):
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="serp-item__title"]').click()

    @allure.step('Поиск по фильтрам')
    def fill_job(self):
        browser.element('#a11y-search-input').type('Python').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[name=part_time][value=start_after_sixteen]+span').click()
        browser.element('[name=salary][value="45000"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[class=bloko-checkbox__input][value="124"]+span').perform(command.js.scroll_into_view).click()
        browser.element('[name=education][value="not_required_or_not_specified"]+span').click()

    @allure.step('Проверка по городу')
    def should_have_city(self):
        browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))

    @allure.title('Проверка информации')
    def should_have_company(self):
        browser.element('.g-user-content').should(have.text('QIWI'))

    @allure.step('Проверка работы')
    def should_have_job(self):
        browser.element('[data-qa="bloko-header-3"]').should(have.text('Python'))

    @allure.step('Проверка резюме')
    def should_have_resume(self):
        browser.close_current_tab()
        browser.switch_to_tab(0)
        browser.element('[data-qa="resume-block-experience"]').should(have.text('Яндекс'))

    @allure.step('Авторизация')
    def login(self):
        browser.open('https://saratov.hh.ru/')
        browser.element('[href="/account/login?backurl=%2F&hhtmFrom=main"]').click()
        browser.element('[data-qa="expand-login-by-password"]').click()
        browser.element('[data-qa="login-input-username"]').type(name)
        browser.element('[data-qa="login-input-password"]').type(passw)
        browser.element('[data-qa="account-login-submit"]').click()

    def check_login(self):
        browser.element('[data-qa="mainmenu_applicantProfile"]').click()
        browser.element('[href="/applicant/settings?from=header_new&hhtmFromLabel=header_new&hhtmFrom=main"]').click()
        browser.element('[data-template-name="fio"]').should(have.text('Quru'))

    @allure.step('Выбор города')
    def select_city(self):
        self.open()
        self.fill_city()

    @allure.step('Проверка города')
    def check_city(self):
        self.should_have_city()

    @allure.step('Выбор компании')
    def find_company(self):
        self.open()
        self.search_company()

    @allure.step('Проверка компании')
    def check_company(self):
        self.should_have_company()

    @allure.step('Выбор работы')
    def search_resume(self):
        self.open()
        self.fill_resume()

    @allure.step('Проверка работы')
    def check_resume(self):
        self.should_have_resume()

    @allure.step('Поиск по фильтрам')
    def search_job(self):
        self.open()
        self.fill_job()

    @allure.step('Проверка пофильтрам')
    def check_job(self):
        self.should_have_job()
