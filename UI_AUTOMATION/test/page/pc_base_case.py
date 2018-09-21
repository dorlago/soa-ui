import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from test.page.pc_home_page import HomePage, LoginPage
from utils.config import Config
from utils.config import DRIVER_PATH

DRIVER = DRIVER_PATH + '\chromedriver.exe'
GECKO = DRIVER_PATH + '\geckodriver.exe'
c = Config()
URL = c.get('PcLoginUrl')

USR = c.get('PcAccount1')['email']
PWD = c.get('PcAccount1')['password']
UA = c.get('ua')


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER)
        # self.driver = webdriver.Firefox(executable_path=GECKO)
        self.url = URL
        self.name = USR
        self.pwd = PWD

        pc = HomePage(self.driver)
        lg = LoginPage(self.driver)
        pc.get(self.url)
        pc.close_pop_win()
        pc.sign_in()
        lg.login(self.name, self.pwd)
        WebDriverWait(self.driver, 30).until(EC.title_is("GearBest: Online Shopping - Best Gear at Best Prices"))

    def test_logout(self):
        HomePage(self.driver).logout()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
