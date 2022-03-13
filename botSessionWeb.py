import json
from botDB import *
from requests import Session
from botTools import query_token
from selenium import webdriver as wd
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


nga = Session()
nga_token = json.loads(query_token('nga'))
headers = nga_token['headers']
cookies = nga_token['cookies']
nga.headers.update(headers)
nga.cookies.update(cookies)


options = wd.ChromeOptions()
options.add_argument('--headless')
options.add_argument(f'--user-data-dir={chrome_profile_path}')

mobile_emulation = {'deviceName': 'iPhone 6/7/8 Plus'}
options.add_experimental_option('mobileEmulation', mobile_emulation)

preferences = {'download_restrictions': 3}
# disable all downloads: https://chromeenterprise.google/policies/?policy=DownloadRestrictions
options.add_experimental_option('prefs', preferences)


def get_driver():
    return wd.Chrome(
        service=Service(
            ChromeDriverManager(
                chrome_type=ChromeType.CHROMIUM).install()
            ),
        options=options)