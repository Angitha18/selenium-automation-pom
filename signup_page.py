from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage
import time

class SignupPage(BasePage):
    name = (By.XPATH, "//input[@placeholder='Name']")
    email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")
    gender = (By.ID, "id_gender2")
    password = (By.ID, "password")

    day = (By.ID, "days")
    month = (By.ID, "months")
    year = (By.ID, "years")

    newsletter = (By.ID, "newsletter")
    optin = (By.ID, "optin")

    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zip = (By.ID, "zipcode")
    mob_num = (By.ID, "mobile_number")

    create_acc = (By.XPATH, "//button[@data-qa='create-account']")
    success_msg = (By.TAG_NAME, "h2")
    continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")

    def register_user(self):
        self.enter_text(self.name, "Angitha Nambiar")
        self.enter_text(self.email, f"angitha{int(time.time())}@gmail.com")
        self.click(self.signup_btn)

        self.wait.until(lambda driver: driver.find_element(*self.gender).is_displayed())
        self.click(self.gender)
        self.enter_text(self.password, "123456")

        Select(self.driver.find_element(*self.day)).select_by_visible_text("19")
        Select(self.driver.find_element(*self.month)).select_by_visible_text("March")
        Select(self.driver.find_element(*self.year)).select_by_visible_text("2000")

        self.scroll_to(self.driver.find_element(*self.newsletter))
        self.click(self.newsletter)
        self.click(self.optin)

        self.enter_text(self.first_name, "Angitha")
        self.enter_text(self.last_name, "Nambiar")
        self.enter_text(self.address, "Trinity Abode")
        Select(self.driver.find_element(*self.country)).select_by_visible_text("India")
        self.enter_text(self.state, "Karnataka")
        self.enter_text(self.city, "Bangalore")
        self.enter_text(self.zip, "560083")
        self.enter_text(self.mob_num, "9058362856")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(self.create_acc)

        success_text = self.get_text(self.success_msg)
        assert "ACCOUNT CREATED!" in success_text
        print("Account created")

        try:
            self.driver.execute_script("document.body.click();")
            print("Dismissed popup using JavaScript click on body.")
        except Exception as e:
            print("Could not dismiss popup via JS.", e)

        self.click(self.continue_btn)
