from hh_project.utils.api_helper import api_request
from tests.api.conftest import url


class SearchPage:

    def search_python(self):
        result = api_request(url=url, endpoint='/search/vacancy', method='GET',
                             params=({'q': 'PYTHON'}))

        assert result.status_code == 200
        assert 'Python' in result.text

    def search_job(self):
        result = api_request(url=url, endpoint='/vacancies/prodavec', method='GET',
                             params=({'hhtmFromLabel': 'rainbow_profession', 'hhtmFrom': 'main'}))
        assert result.status_code == 200
        assert 'Работа продавцом в Саратове' in result.text

    def all_services(self):
        result = api_request(url=url, endpoint='/services', method='GET',
                             params=({'disableBrowserCache': 'true'}))
        assert result.status_code == 200
        assert 'Сервисы для соискателей' in result.text

    def not_found(self):
        result = api_request(url=url, endpoint='/search/vacancy2', method='GET',
                             params=({'text': 'gdsfg2', 'area': '24', 'hhtmFrom': 'main',
                                      'hhtmFromLabel': 'vacancy_search_line'}))
        assert result.status_code == 404
        assert 'NotFoundError' in result.text


search_page = SearchPage()
