import os

from jsonschema import validate
from dotenv import load_dotenv

from hh_project.schemas.json import python
from hh_project.utils.api_helper import api_request

name = os.getenv('name')
passw = os.getenv('passw')
load_dotenv()


class Hh_api:

    def login_api(self):
        result = api_request(url='https://saratov.hh.ru', endpoint='/account/login', method='POST', params=(
            {'username': 'qaqurupython@gmail.com', 'password': '12344321', 'q': 'backurl=%2F'}))
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'

    def search_python(self):
        result = api_request(url='https://saratov.hh.ru', endpoint='/vacancysuggest', method='GET',
                             params=({'q': 'PYTHON'}))
        body = result.json()
        validate(body, schema=python)
        assert result.status_code == 200

    def search_job(self):
        result = api_request(url='https://saratov.hh.ru', endpoint='/vacancies/prodavec', method='GET',
                             params=({'hhtmFromLabel': 'rainbow_profession', 'hhtmFrom': 'main'}))
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'text/html; charset=utf-8'

    def all_services(self):
        result = api_request(url='https://saratov.hh.ru', endpoint='/services', method='GET',
                             params=({'disableBrowserCache': 'true'}))
        assert result.status_code == 200
        assert result.headers['vary'] == 'Accept-Encoding'

    def not_found(self):
        result = api_request(url='https://saratov.hh.ru', endpoint='/search/vacancy2', method='GET',
                             params=({'text': 'gdsfg2', 'area': '24', 'hhtmFrom': 'main',
                                      'hhtmFromLabel': 'vacancy_search_line'}))
        assert result.status_code == 404

hh_api = Hh_api()