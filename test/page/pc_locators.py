from selenium.webdriver.common.by import By


class PublicLoc:
    """公共组件"""


class LoginPageLoc:
    """登录"""
    email = (By.ID, "email")
    password = (By.ID, "password")
    sign_in = (By.ID, "js-btnSubmit")


class HomePageLoc:
    """首页"""

    # 标题栏
    user_info = (By.CSS_SELECTOR, "a.siteHeader_userAccountLink")
    sign_in = (By.CSS_SELECTOR, "a.siteHeader_userLinkLogin")
    my_fav = (By.XPATH, "//header/div[2]/div[3]/div[1]/div[1]/div[1]/p/a")
    cart = (By.XPATH, "//header/div[2]/div[3]/div[3]/a[2]/p")
    # 用户信息菜单
    my_order = (By.XPATH, "//ul/li[2]/a")
    my_tickets = (By.XPATH, "//ul/li[3]/a")
    my_message = (By.XPATH, "//ul/li[4]/a")
    my_wallet = (By.XPATH, "//ul/li[5]/a")
    my_points = (By.XPATH, "//ul/li[6]/a")
    my_profile = (By.XPATH, "//ul/li[7]/a")
    my_coupon = (By.XPATH, "//ul/li[8]/a")
    logout = (By.CLASS_NAME, "js-logout")
    # 弹窗
    new_user_pop = (By.CLASS_NAME, "newUserPop")
    close_pop = (By.CLASS_NAME, "layui-layer-setwin")


class UserInfoPageLoc:
    """用户信息页"""
    goods_images = (By.CSS_SELECTOR, "a.orderItem_thumb")
    goods_names = (By.CSS_SELECTOR, "a.orderItem_title")


class GoodsInfoPageLoc:
    """商品详情页"""

    qty = (By.CLASS_NAME, "compInputNumber_input")
    num_plus = (By.CLASS_NAME, "compInputNumber_reduce")
    num_reduce = (By.CLASS_NAME, "compInputNumber_plus")