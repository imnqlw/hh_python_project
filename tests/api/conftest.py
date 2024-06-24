import os
from dotenv import load_dotenv
import pytest

url = os.getenv('url')
name = os.getenv('name')
passw = os.getenv('passw')
text = os.getenv('text')
wrong_pass = os.getenv('wrong_pass')
load_dotenv()


@pytest.fixture()
def base_api_url():
    base_url = url
    return base_url