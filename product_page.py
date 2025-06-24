from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class ProductPage(BasePage):
    ALL_PRODUCTS_TEXT = (By.XPATH, "//h2[text()='All Products']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-dismiss='modal']")

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def wait_for_product_list(self):
        self.wait.until(EC.presence_of_element_located(self.ALL_PRODUCTS_TEXT))

    def add_product_to_cart(self, product_number):
        # Hover over product
        product_locator = (By.XPATH, f"(//div[@class='product-image-wrapper'])[{product_number}]")
        product = self.wait.until(EC.presence_of_element_located(product_locator))
        self.actions.move_to_element(product).perform()
        self.scroll_to(product)
        time.sleep(1)

        # Click 'Add to cart'
        add_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//a[@data-product-id='{product_number}']")))
        self.click_js(add_button)

        # Handle 'Continue Shopping' popup
        try:
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
            continue_btn.click()
            print(f" 'Continue' popup dismissed after product {product_number}")
        except:
            print(f" 'Continue' popup not found for product {product_number}")
