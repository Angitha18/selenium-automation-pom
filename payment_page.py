from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class PaymentPage(BasePage):
    NAME_ON_CARD = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@data-qa='cvc']")
    EXPIRY_MONTH = (By.XPATH, "//input[@data-qa='expiry-month']")
    EXPIRY_YEAR = (By.XPATH, "//input[@data-qa='expiry-year']")
    PAY_BUTTON = (By.XPATH, "//button[@data-qa='pay-button']")
    SUCCESS_MSG = (By.TAG_NAME, "h2")

    def fill_payment_and_submit(self):
        self.enter_text(self.NAME_ON_CARD, "Angitha")
        self.enter_text(self.CARD_NUMBER, "3849242")
        self.enter_text(self.CVC, "344")
        self.enter_text(self.EXPIRY_MONTH, "04")
        self.enter_text(self.EXPIRY_YEAR, "2027")
        self.click(self.PAY_BUTTON)

        # Verify success message
        success_text = self.get_text(self.SUCCESS_MSG)
        assert "ORDER PLACED!" in success_text
        print("Order placed successfully!")
