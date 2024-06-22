
import allure

from hh_project.pages.page_api import hh_api


@allure.tag('web')
@allure.title('Successful login')
def test_hh_login():
    hh_api.login_api()


@allure.tag('web')
@allure.title('Search Python')
def test_search_python():
    hh_api.search_python()


@allure.tag('web')
@allure.title('Search Job')
def test_search_job():
    hh_api.search_job()


@allure.tag('web')
@allure.title('Select all services')
def test_all_services():
    hh_api.all_services()


@allure.tag('web')
@allure.title('Not found')
def test_hh_404():
    hh_api.not_found()
