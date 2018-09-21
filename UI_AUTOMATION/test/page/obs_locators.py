from selenium.webdriver.common.by import By


class ComponentLoc:

    create_btn = (By.XPATH, "//span[text()='创建']")
    edit_btn = (By.XPATH, "//span[text()='修改']")
    del_btn = (By.XPATH, "//span[text()='删除']")
    query_btn = (By.XPATH, "//span[text()=' 筛选']")

    # form
    cell = (By.XPATH, "//table/tbody/tr{}/td{}/div")


class ObsLoginLoc:
    user = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    submit = (By.NAME, 'dosubmit')
    logout = (By.XPATH, "//span[text()='登出']")
