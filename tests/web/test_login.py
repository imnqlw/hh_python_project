import allure

from hh_project.pages.home_page import MainPage


@allure.tag("WEB")
@allure.title('Выбор города')
@allure.epic('Город')
@allure.story('Саратов')
@allure.feature('Выбор города')
@allure.label('owner')
@allure.severity('high')
def test_search_city():
    main = MainPage()
    main.select_city()
    main.check_city()


@allure.title('Авторизация')
@allure.epic('Авторизация')
@allure.story('Авторизация')
@allure.feature('Авторизация')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_login():
    main = MainPage()
    main.login()








@allure.title('Поиск компании')
@allure.epic('Компания')
@allure.story('Ищем компанию')
@allure.feature('Нашли')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search_company():
    main = MainPage()
    main.find_company()
    main.check_company()

@allure.title('Поиск резюме')
@allure.epic('Резюме')
@allure.story('Ищем резюме')
@allure.feature('Нашли')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search_resume():
    main = MainPage()
    main.search_resume()
    main.check_resume()

@allure.title('Поиск работы')
@allure.epic('Работа')
@allure.story('Ищем работу')
@allure.feature('Работа')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search_job():
    main = MainPage()
    main.search_job()
    main.check_job()
