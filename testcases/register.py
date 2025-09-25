import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

serv_obj = Service("C:/Users/Bhavani/PycharmProjects/qa-automation/driver/geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Signup / Login").click()
heading = driver.find_element(By.XPATH,"//h2[.='New User Signup!']").text
assert heading == "New User Signup!"

username = "test1"
driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)

try:
    driver.find_element(By.XPATH, "//input[contains(@data-qa,'signup-email')]").send_keys("test_00@gmail.com")
    driver.find_element(By.XPATH, "//button[.='Signup']").click()
    error = driver.find_element(By.XPATH,"//*[contains(text(),'Email Address already exist!')]")
    if error.is_displayed():
        timestamp = int(time.time())
        new_email = f"test{timestamp}@gmail.com"

        email_field = driver.find_element(By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        email_field.clear()
        email_field.send_keys(new_email)
        driver.find_element(By.XPATH,"//button[.='Signup']").click()

except NoSuchElementException:

    driver.find_element(By.XPATH,"//button[.='Signup']").click()

driver.find_element(By.CSS_SELECTOR,"input[type='radio'][value='Mrs']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("1234")


# Check if ad is present and visible
ad_elements = driver.find_elements(By.XPATH, "//*[name()='path' and @fill='#FAFAFA']")
if ad_elements and ad_elements[0].is_displayed():
    try:
        driver.execute_script("arguments[0].click();", ad_elements[0])
    except (ElementClickInterceptedException, NoSuchElementException):
        pass

Select(driver.find_element(By.ID, "days")).select_by_visible_text("18")
months = driver.find_element(By.ID, "months")
driver.execute_script("arguments[0].scrollIntoView(true);", months)
months.click()  # or use Select if needed
Select(driver.find_element(By.ID, "years")).select_by_visible_text("2019")

driver.find_element(By.XPATH,"//label[.='Receive special offers from our partners!']").click()
driver.find_element(By.ID,"first_name").send_keys("test")
driver.find_element(By.ID,"last_name").send_keys("user")
driver.find_element(By.XPATH,"//input[@name='address1']").send_keys("10, john street")
driver.find_element(By.ID,"state").send_keys("TamilNadu")
driver.find_element(By.ID,"city").send_keys("Chennai")
driver.find_element(By.ID,"zipcode").send_keys("600001")
driver.find_element(By.XPATH,"//input[@id='mobile_number']").send_keys("9876543210")
driver.find_element(By.XPATH,"//button[text()='Create Account']").click()

success = driver.find_element(By.XPATH,"//p[contains(.,'Congratulations!')]")
assert success.text ==  "Congratulations! Your new account has been successfully created!"
print("Account is Created Successfully")
driver.find_element(By.XPATH,"//a[text()='Continue']").click()
logged_as = driver.find_element(By.XPATH,"//a[contains(text(),'Logged')]").text.strip()
actual_username = logged_as.replace("Logged in as "," ").strip()
assert actual_username == username, f"Username:{username},Logged User:{actual_username}"
print("Username is matched")

driver.find_element(By.LINK_TEXT,"Delete Account").click()
deleted = driver.find_element(By.XPATH,"//p[contains(.,'permanently deleted!')]")
assert deleted.text == "Your account has been permanently deleted!"
print("Account is Deleted Permanently")

driver.find_element(By.XPATH,"//a[text()='Continue']").click()
driver.quit()
