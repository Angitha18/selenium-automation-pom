from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# Step 1: Open website
driver.get("https://automationexercise.com/")

#Login
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("Angitha Nambiar")
#email = f"angitha{int(time.time())}@gmail.com"
driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("angithanambiar18006@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "id_gender2")))

driver.find_element(By.ID,"id_gender2").click()
driver.find_element(By.ID,"password").send_keys("123456")

#dropdowns
Select(driver.find_element(By.ID,"days")).select_by_visible_text("19")
Select(driver.find_element(By.ID,"months")).select_by_visible_text("March")
Select(driver.find_element(By.ID,"years")).select_by_visible_text("2000")

newsletter = driver.find_element(By.ID, "newsletter")
driver.execute_script("arguments[0].scrollIntoView(true);", newsletter)
wait.until(EC.element_to_be_clickable((By.ID, "newsletter"))).click()

optin = driver.find_element(By.ID, "optin")
driver.execute_script("arguments[0].scrollIntoView(true);", optin)
wait.until(EC.element_to_be_clickable((By.ID, "optin"))).click()

driver.find_element(By.ID,"first_name").send_keys("Angitha")
driver.find_element(By.ID,"last_name").send_keys("Nambiar")

driver.find_element(By.ID,"address1").send_keys("Trinity Abode")
Select(driver.find_element(By.ID,"country")).select_by_visible_text("India")
driver.find_element(By.ID,"state").send_keys("Karnataka")
driver.find_element(By.ID,"city").send_keys("Bangalore")
driver.find_element(By.ID,"zipcode").send_keys("560083")
driver.find_element(By.ID,"mobile_number").send_keys("9058362856")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()
success_text = driver.find_element(By.TAG_NAME,"h2").text
assert "ACCOUNT CREATED!" in success_text
print("Account created")

try:
    driver.execute_script("document.body.click();")
    print("Dismissed popup using JavaScript click on body.")
except Exception as e:
    print("Could not dismiss popup via JS.", e)


driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
# Step 2: Click 'Products' menu
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))).click()

# Step 3: Wait for product list to load
wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='All Products']")))

# Step 4: Scroll to product section
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

# Step 5: Hover over first product
product1_card = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='product-image-wrapper'])[1]")))
actions.move_to_element(product1_card).perform()
driver.execute_script("arguments[0].scrollIntoView(true);", product1_card)
time.sleep(1)

# Step 6: Click 'Add to cart' for product 1 using JS
add_button1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product-id='1']")))
driver.execute_script("arguments[0].click();", add_button1)

# Step 7: Click 'Continue Shopping' on modal
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-dismiss='modal']"))).click()

# Step 8: Hover over second product
product2_card = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='product-image-wrapper'])[2]")))
actions.move_to_element(product2_card).perform()
driver.execute_script("arguments[0].scrollIntoView(true);", product2_card)
time.sleep(1)

# Step 9: Click 'Add to cart' for product 2 using JS
add_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product-id='2']")))
driver.execute_script("arguments[0].click();", add_button2)

# Step 10: Click 'Continue Shopping' again
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-dismiss='modal']"))).click()

# Step 11: Click 'Cart' from top menu
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']"))).click()
try:
    continue_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
    )
    continue_button.click()
    print("'Continue' popup handled.")
except:
    print("'Continue' popup not found or already closed.")

# Step 12: Verify cart items
cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_description")))
assert len(cart_items) >= 2
print("2 products successfully added to cart!")

# Step 8: Dismiss "Save Address?" popup if it exists before clicking Checkout
try:
    # Give the modal a chance to load
    time.sleep(2)

    # Click on a neutral part of the screen to dismiss popup
    body = driver.find_element(By.TAG_NAME, 'body')
    actions.move_to_element_with_offset(body, 10, 10).click().perform()

    # Wait for popup to disappear
    WebDriverWait(driver, 3).until_not(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )

    print("Save Address popup dismissed by clicking on screen.")
except Exception as e:
    print("Popup might not have appeared, or it already disappeared.", e)


#checkout page
checkout = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-default check_out']")))
checkout.click()

#continue_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-dismiss='modal']")))
#continue_btn.click()

#place order
try:
    place_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Place Order')]")))

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", place_order)
    time.sleep(1)  # Let the scroll animation complete

    # Click using JavaScript (more reliable if UI layers overlap)
    driver.execute_script("arguments[0].click();", place_order)

    print("'Place Order' button clicked.")
except Exception as e:
    print("Could not click 'Place Order' button:", e)
    driver.save_screenshot("place_order_click_failed.png")


card_name = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name_on_card']")))
card_name.send_keys("Angitha")

card_no = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='card_number']")))
card_no.send_keys("3849242")

cvv = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='cvc']")))
cvv.send_keys("344")

expiry_month = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='expiry-month']")))
expiry_month.send_keys("04")

expiry_year = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='expiry-year']")))
expiry_year.send_keys("2027")

confirm = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@data-qa='pay-button']")))
confirm.click()

try:
    success_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h2"))
    ).text

    assert "ORDER PLACED!" in success_msg
    print("Order placed successfully!")

except Exception as e:
    print("Order success message not found or did not match expected text.", e)
    driver.save_screenshot("order_success_missing.png")
