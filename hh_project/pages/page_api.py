import os

from dotenv import load_dotenv

from hh_project.utils.api_helper import api_request

name = os.getenv('name')
passw = os.getenv('passw')
base_url = os.getenv('base_url')
load_dotenv()


class Hh_api:

    def login_api(self):
        result = api_request(url=base_url, endpoint='/account/login', method='POST', params=(
            {'username': 'qaqurupython@gmail.com', 'password': '12344321', 'q': 'backurl=%2F'}))
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'

    def search_python(self):
        result = api_request(url=base_url, endpoint='/search/vacancy', method='GET',
                             params=({'q': 'PYTHON'}))


        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'text/html; charset=utf-8'

    def search_job(self):
        result = api_request(url=base_url, endpoint='/vacancies/prodavec', method='GET',
                             params=({'hhtmFromLabel': 'rainbow_profession', 'hhtmFrom': 'main'}))
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'text/html; charset=utf-8'

    def all_services(self):
        result = api_request(url=base_url, endpoint='/services', method='GET',
                             params=({'disableBrowserCache': 'true'}))
        assert result.status_code == 200
        assert result.headers['vary'] == 'Accept-Encoding'

    def not_found(self):
        result = api_request(url=base_url, endpoint='/search/vacancy2', method='GET',
                             params=({'text': 'gdsfg2', 'area': '24', 'hhtmFrom': 'main',
                                      'hhtmFromLabel': 'vacancy_search_line'}))
        assert result.status_code == 404


hh_api = Hh_api()
