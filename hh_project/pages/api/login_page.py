from hh_project.utils.api_helper import api_request
from tests.api.conftest import base_url, name, passw


class LoginPage:

    def login_user(self):
        result = api_request(url=base_url, endpoint='/account/login', method='POST', params=(
            {'username': name, 'password': passw, 'q': 'backurl=%2F'}))
        assert result.status_code == 200
        assert 'force_login' in result.text

login_page = LoginPage()