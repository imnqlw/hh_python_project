import allure

from tests.web.main_page import MainPage, main


@allure.tag("WEB")
@allure.title('Выбор города')
@allure.epic('Город')
@allure.story('Саратов')
@allure.feature('Выбор Саратова')
@allure.label('owner')
@allure.severity('high')
def test_search_city():
    main.select_city()
    main.check_city()


@allure.title('Авторизация')
@allure.epic('Авторизация')
@allure.story('Авторизация')
@allure.feature('Проверка авторизации')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_login():
    main.login()
    main.check_login()


@allure.title('Поиск компании')
@allure.epic('Компания')
@allure.story('Ищем компанию')
@allure.feature('Нашли')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search_company():
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
    main.search_job()
    main.check_job()


@allure.title('Поиск работы c параметрами')
@allure.epic('IT')
@allure.story('IT')
@allure.feature('IT')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search_with_parameters():
    main.search_with_parameters()
    main.check_search_with_parameters()


@allure.title('Проджвиение резюме')
@allure.epic('Проджвиение резюме')
@allure.story('Проджвиение резюме')
@allure.feature('Найти работу быстрее')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_promotion_resume():
    main.promotion_resume()
    main.check_promotion_resume()

