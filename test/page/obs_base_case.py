import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from test.page.obs_pages import ObsLoginPage
from utils.config import Config
from utils.config import DRIVER_PATH

DRIVER = DRIVER_PATH + '\chromedriver.exe'
GECKO = DRIVER_PATH + '\geckodriver.exe'
c = Config()
URL = c.get('ObsLoginUrl')
USR = c.get('ObsAccount')['userName']
PWD = c.get('ObsAccount')['password']
UA = c.get('ua')


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER)
        # self.driver = webdriver.Firefox(executable_path=GECKO)
        self.url = URL
        self.name = USR
        self.pwd = PWD

        obs = ObsLoginPage(self.driver)
        obs.login(self.url, self.name, self.pwd)
        WebDriverWait(self.driver, 30).until(ec.title_is(u"obs管理系统"))

    def test_logout(self):
        ObsLoginPage(self.driver).logout()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


