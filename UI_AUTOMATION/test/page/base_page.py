import os
import time
import xlrd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from utils.config import REPORT_PATH
from utils.log import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url, maximize_window=True, time_sync=30):
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(time_sync)
        return self

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))  # 等待元素在页面可见
            return self.driver.find_element(*loc)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def find_elements(self, *loc):
        try:
            items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(loc))  # 等待元素在DOM都出现
            return items
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def elements_text(self, *loc):
        items = []
        items_elements = self.find_elements(*loc)
        for item in items_elements:
            items.append(item.text.strip())
        return items

    def move_to_element(self, *loc):
        aim_loc = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(aim_loc).perform()

    def click(self, *loc):
        try:
            self.find_element(*loc).click()
        except WebDriverException:
            self.save_screen_shot()
            logger.error("Element {} is not clickable".format(loc))

    def send_keys(self,  value, *loc):
        element = self.find_element(*loc)
        element.click()
        element.clear()
        element.send_keys(value)

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def in_pages(self, txt):
        return txt in self.driver.page_source

    def switch_frame(self, loc):
        self.driver.switch_to.frame(loc)

    def default_content(self):
        self.driver.switch_to.default_content()

    def switch_window(self, n=1):
        # 打开顺序：1,2,3,4,5
        # 句柄顺序：0,4,3,2,1
        newest_window = self.driver.window_handles[n]
        self.driver.switch_to.window(newest_window)

    @staticmethod
    def get_latest_file(download_dir):
        """获取最新的文件"""
        lists = os.listdir(download_dir)
        lists.sort(key=lambda fn: os.path.getmtime(download_dir + '\\' + fn))
        file_path = os.path.join(download_dir, lists[-1])
        return file_path

    @staticmethod
    def get_data(file_path):
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_index(0)
        rows = []
        cols = []
        for j in range(0, sheet.nrows):
            rows.append(list(sheet.row_values(j, 0, sheet.ncols)))
        for i in range(0, sheet.ncols):
            cols.append(list(sheet.col_values(i, 0, sheet.nrows)))
        return rows, cols, book.sheet_names()
    # 返回3个列表组成的元组







