from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    PRODUCTS_MENU = (By.XPATH, "//a[@href='/products']")
    SIGNUP_LOGIN = (By.LINK_TEXT, "Signup / Login")
    CART_BUTTON = (By.XPATH, "//a[@href='/view_cart']")

    def open(self):
        self.driver.get("https://automationexercise.com/")

    def go_to_login(self):
        self.click(self.SIGNUP_LOGIN)

    def go_to_products(self):
        self.click(self.PRODUCTS_MENU)

    def go_to_cart(self):
        # Scroll to top
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.click(self.CART_BUTTON)
        print("Clicked Cart button")
