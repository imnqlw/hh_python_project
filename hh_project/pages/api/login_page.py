from hh_project.utils.api_helper import api_request
from tests.api.conftest import name, passw


class LoginPage:

    def login_user(self, base_api_url):
        result = api_request(url=base_api_url, endpoint='/account/login', method='POST', params=(
            {'username': name, 'password': passw, 'q': 'backurl=%2F'}))
        assert result.status_code == 403
        #assert 'force_login' in result.text

login_page = LoginPage()