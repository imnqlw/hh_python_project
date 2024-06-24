import os
from dotenv import load_dotenv


base_url = 'https://hh.ru/'
name = os.getenv('name')
passw = os.getenv('passw')
text = os.getenv('text')
wrong_pass = os.getenv('wrong_pass')
load_dotenv()