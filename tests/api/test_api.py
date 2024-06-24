import allure
from hh_project.pages.api.login_page import login_page
from hh_project.pages.api.search_page import search_page


@allure.tag('web')
@allure.title('Successful login')
def test_hh_login():
    login_page.login_user()


@allure.tag('web')
@allure.title('Search Python')
def test_search_python():
    search_page.search_python()


@allure.tag('web')
@allure.title('Search Job')
def test_search_job():
    search_page.search_job()


@allure.tag('web')
@allure.title('Select all services')
def test_all_services():
    search_page.all_services()


@allure.tag('web')
@allure.title('Not found')
def test_hh_404():
    search_page.not_found()
