from time import sleep
from test.page.pc_locators import *
from test.page.base_func import BasePage


class PublicComponent(BasePage):
    pass


class LoginPage(BasePage):

    def login(self, email, pwd):
        self.send_keys(email, *LoginPageLoc.email)
        sleep(0.5)
        self.send_keys(pwd, *LoginPageLoc.password)
        sleep(0.5)
        self.click(*LoginPageLoc.sign_in)


class HomePage(BasePage):

    def visit_gb(self, url):
        self.get(url)

    def sign_in(self):
        self.click(*HomePageLoc.sign_in)
        sleep(2)

    def logout(self):
        self.move_to_element(*HomePageLoc.user_info)
        sleep(0.5)
        self.click(*HomePageLoc.logout)
        sleep(2)

    def close_pop_win(self):
        if self.find_element(*HomePageLoc.new_user_pop):
            self.save_screen_shot()
            self.click(*HomePageLoc.close_pop)