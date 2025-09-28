from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import StaleElementReferenceException , NoSuchElementException

serv_obj = Service("C:/Users/Bhavani/PycharmProjects/qa-automation/driver/geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT,"Signup / Login").click()

#Verify invalid credentials
try:
    ads = driver.find_elements(By.XPATH,"//*[@id='ad-container'] | //*[@id='banner-nologo'] | //*[@class='creative end-card']")
    for ad in ads:
        driver.execute_script("arguments[0].remove();", ad)

    driver.find_element(By.XPATH, "//input[contains(@data-qa,'login-email')]").send_keys("test_9@gmail.com")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("124")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.clear()
    error = driver.find_element(By.XPATH,"//p[contains(text(),'incorrect')]")
    if error.is_displayed():
        print("Enter Valid credentials: ",error.text)
        password.clear()
    # Passing valid credentials
        password.send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    if driver.find_element(By.LINK_TEXT,"Logout").is_displayed():
        print("Successfully Logged In")
    else:
        print("Login failed")
except (StaleElementReferenceException, NoSuchElementException ) as e:
    print("Exception is thrown", e)

driver.find_element(By.LINK_TEXT,"Logout").click()
driver.quit()



