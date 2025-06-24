from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//a[@class='btn btn-default check_out']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[contains(text(),'Place Order')]")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        print("Clicked Proceed to Checkout")

    def click_place_order(self):
        try:
            # Step 1: Force scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            # Step 2: Find the button
            place_order = self.wait.until(
                EC.presence_of_element_located(self.PLACE_ORDER_BUTTON)
            )

            # Step 3: Scroll it into center view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", place_order)
            time.sleep(1)

            # Step 4: Click using JavaScript
            self.driver.execute_script("arguments[0].click();", place_order)
            print("'Place Order' button clicked.")
        except Exception as e:
            print("Failed to click 'Place Order' button:", e)
            self.driver.save_screenshot("place_order_error.png")