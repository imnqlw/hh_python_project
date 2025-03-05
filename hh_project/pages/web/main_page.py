import allure
from selene import browser, have, command
import time


@allure.tag("WEB")
class MainPage:

    @allure.step('Открытие страницы')
    def open(self):
        browser.open('/')

    @allure.step('Поиск работы с параметрами')
    def search_with_parameters(self):
        browser.open('/')
        browser.element('[href="/search/vacancy/advanced?hhtmFrom=main"]').click()
        browser.element('[class="magritte-radio-input___-IM3Y_3-0-37"][value="between1And3"]').perform(command.js.scroll_into_view).click()
        browser.element('[data-qa="advanced-search__employment_form-item_FULL"][value="FULL"]').click()
        browser.element('[data-qa="vacancysearch__keywords-input"]').set_value('IT').press_enter()


    @allure.step('Проверка работы с параметрами')
    def check_search_with_parameters(self):
        browser.element('[data-qa="title-container"][class="magritte-text-alignment-left___BreG5_6-1-0"]').should(have.text('IT'))

    @allure.step('Продвижение резюме')
    def promotion_resume(self):
        browser.open('/')
        browser.element('[data-qa="mainmenu_applicantServices"]').click()
        browser.element('[href="/applicant-services/hhpro?hhtmFrom=services&hhtmFromLabel=menu"]').click()

    @allure.step('Проверка продвижения резюме')
    def check_promotion_resume(self):
        browser.element('[class="iBoZ7I7___title"]').should(have.text('Работа найдётся скорее с hh PRO'))

    @allure.step('Выбор города')
    def fill_city(self):
        browser.open('/')
        browser.element('[data-qa="mainmenu_areaSwitcher"][class="bloko-link bloko-link_pseudo"]').click()
        browser.element('[data-qa="geo-switcher-search"][class="magritte-field___9S8Tw_7-1-10"]').type('Саратов')
        time.sleep(1)
        browser.element('[class="magritte-radio-input___-IM3Y_3-0-37 magritte-radio-input-unchecked___J-rPE_3-0-37"]').click()



    @allure.step('Выбор компании')
    def search_company(self):
        browser.element('#a11y-search-input').type('Qiwi').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-qa="employersList"][class="magritte-tab___B0BeU_6-0-0 magritte-tab_primary___3Of2H_6-0-0"]').click()
        browser.element('[href="/employer/3125?hhtmFrom=employers_list"]').click()

    @allure.step('Выбор работы')
    def fill_resume(self):
        browser.element('#a11y-search-input').type('Специалист Яндекс').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[class="magritte-tab___B0BeU_6-0-0 magritte-tab_primary___3Of2H_6-0-0"]').click()


    @allure.step('Поиск по фильтрам')
    def fill_job(self):
        browser.element('#a11y-search-input').type('Python').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()


    @allure.step('Проверка по городу')
    def should_have_city(self):
        browser.element('[data-qa="mainmenu_areaSwitcher"]').should(have.text('Саратов'))

    @allure.title('Проверка информации')
    def should_have_company(self):
        browser.element('.g-user-content').should(have.text('QIWI'))

    @allure.step('Проверка работы')
    def should_have_job(self):
        browser.element('.magritte-text-alignment-left___BreG5_6-1-0').should(have.text('вакансий'))

    @allure.step('Проверка резюме')
    def should_have_resume(self):
        browser.element('[class="magritte-text___gMq2l_6-1-0 magritte-text-overflow___UBrTV_6-1-0 magritte-text-typography-medium___cp79S_6-1-0 magritte-text-style-primary___8SAJp_6-1-0"]').should(have.text('резюме'))

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



main = MainPage()
