import sys
import os

# ✅ Fix import error by adding project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

def test_place_order():
    driver = webdriver.Chrome()
    driver.maximize_window()

    home = HomePage(driver)
    signup = SignupPage(driver)
    product = ProductPage(driver)
    checkout = CheckoutPage(driver)
    payment = PaymentPage(driver)

    # Flow
    home.open()
    home.go_to_login()
    signup.register_user()
    home.go_to_products()
    product.wait_for_product_list()
    product.add_product_to_cart(1)
    product.add_product_to_cart(2)
    home.go_to_cart()
    checkout.proceed_to_checkout()
    checkout.click_place_order()
    payment.fill_payment_and_submit()

    driver.quit()
