from time import sleep

from test.page.base_func import BasePage
from test.page.obs_locators import *


class PublicComponent(BasePage):

    def create(self):
        self.click(ComponentLoc.create_btn)

    def edit(self):
        self.click(ComponentLoc.edit_btn)

    def delete(self):
        self.click(ComponentLoc.del_btn)

    def get_cell_values(self, row='', col=''):
        if row and col:
            loc = ([row], [col])
        elif row and not col:
            loc = ([row], col)
        elif not row and col:
            loc = (row, [col])
        else:
            loc = (row, col)
        return self.elements_text(*ComponentLoc.cell).format(loc)


class ObsLoginPage(BasePage):
    def login(self, url, usr, pwd):
        self.get(url)
        self.send_keys(usr, *ObsLoginLoc.user)
        self.send_keys(pwd, *ObsLoginLoc.pwd)
        self.click(*ObsLoginLoc.submit)
        sleep(2)

    def logout(self):
        self.click(*ObsLoginLoc.logout)


