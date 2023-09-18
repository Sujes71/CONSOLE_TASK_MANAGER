from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time;

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

username = "jesus.perez"
password = "Kotikotos777."

url = "http://81.47.129.87:8080/"

driver = webdriver.Chrome(chrome_options=options,service=Service(ChromeDriverManager().install()))

driver.get(url)

driver.find_element("name", "ctl00$MainContent$UserName").send_keys(username)
driver.find_element("name", "ctl00$MainContent$Password").send_keys(password)
driver.find_element("id","MainContent_LoginButton").click()
driver.find_element("id","imputaciones").click()
driver.find_element("id","MainContentPlaceHolder_ButtonEntrada").click()

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(2);

driver.quit()

print("Fichaje realizado exitosamente!")