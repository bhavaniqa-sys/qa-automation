from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


serv_obj = Service("C:/Users/Bhavani/PycharmProjects/qa-automation/driver/geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(5)
try:
    ads = driver.find_elements(By.XPATH,
                               "//*[@id='ad-container'] | //*[@id='banner-nologo'] | //*[@class='creative end-card'] |//*[@class='GoogleActiveViewElement'] |//*[@id='mys-wrapper']")
    for ad in ads:
        driver.execute_script("arguments[0].remove();", ad)

    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    driver.find_element(By.XPATH, "//input[contains(@data-qa,'login-email')]").send_keys("test_9@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    driver.find_element(By.XPATH,"//a[@href='/products']").click()
    products = driver.find_elements(By.XPATH, "//*[text()='Winter Top']/ancestor::div[contains(@class,'product')]")

    for product in products:
        if product.is_displayed():
            added_item_name = product.find_element(By.XPATH, "//*[text()='Winter Top']").text.strip()
            product.find_element(By.XPATH, ".//a[text()='Add to cart']").click()
            break
    driver.find_element(By.LINK_TEXT, "View Cart").click()

except Exception as e:

    # driver.find_element(By.LINK_TEXT,"Products").click()
    print("Error Message:",e)

#Check the Add to cart item and item in cart is same and click on checkout

cartItem = driver.find_element(By.XPATH,"//table[contains(@id,'cart')]//td[contains(@class,'cart')]//a[.='Winter Top']").text
if added_item_name == cartItem:
    driver.find_element(By.XPATH,"//a[normalize-space()='Proceed To Checkout']").click()


# Cart is empty! Click here to buy products.
