
from pages.base_page import BasePage
from locator.locators import User
class Userpage(BasePage):

    def get_user_available_balance(self):
        """
        获取用户可用余额
        :return:
        """
        self.wait_ele_presence(User.user_available_balance,"等待跳转到user页面")
        return self.get_ele_text(User.user_available_balance,"获取用户可用余额")[:-1]