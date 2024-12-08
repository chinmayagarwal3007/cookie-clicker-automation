from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

end_time = time.time() + 600  # Set the end time for 10 minute from now




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


data_event = driver.find_element(By.ID, value="cookie")
data_event.click()

def buy_upgrade():
    cookie_count = driver.find_element(By.ID, value="money")

    upgrade_mouse = driver.find_element(By.ID, value="buyCursor")
    upgrade_grandma = driver.find_element(By.ID, value="buyGrandma")
    upgrade_factory = driver.find_element(By.ID, value="buyFactory")
    upgrade_mine = driver.find_element(By.ID, value="buyMine")
    upgrade_shipment = driver.find_element(By.ID, value="buyShipment")
    upgrade_chemy = driver.find_element(By.ID, value="buyAlchemy lab")
    upgrade_portal = driver.find_element(By.ID, value="buyPortal")

    if(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyPortal b").text.split()[2].replace(",", ""))):
        upgrade_portal.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split()[3].replace(",", ""))):
        upgrade_chemy.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split()[2].replace(",", ""))):
        upgrade_shipment.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split()[2].replace(",", ""))):
        upgrade_mine.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split()[2].replace(",", ""))):
        upgrade_factory.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split()[2].replace(",", ""))):
        upgrade_grandma.click()
    elif(int(cookie_count.text) >= int(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split()[2].replace(",", ""))):
        upgrade_mouse.click()


def run_task():
    last_check_time = time.time()  # Record the start time (the time when the loop starts)
    
    while True:
        current_time = time.time()
        
        # Perform the "millisecond task"
        data_event.click()
        
        # Check if 5 seconds have passed
        if current_time - last_check_time >= 5:
            buy_upgrade()
            last_check_time = current_time  # Reset the check time to the current time
        
        # Sleep for a short amount (e.g., 1 ms) to prevent high CPU usage
        time.sleep(0.001)

# Start the task
run_task()
