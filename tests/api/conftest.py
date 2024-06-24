import os
from dotenv import load_dotenv
import pytest

name = os.getenv('name')
passw = os.getenv('passw')
text = os.getenv('text')
wrong_pass = os.getenv('wrong_pass')
load_dotenv()
url = os.getenv('base_url')

@pytest.fixture()
def base_api_url():
    base_url = url
    return base_url