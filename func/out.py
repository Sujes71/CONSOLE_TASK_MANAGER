from unicodedata import numeric
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

username = "jesus.perez"
password = "26z3R%Y$jB^7"
url = "http://81.47.129.87:8080/"

def signout(project, task, description):
    if len(description) < 20:
        print("[!] Please enter a description with a length of more than 20 characters")
    #elif len(time) != 5:
    #     print("[!] Please enter a valid time with a length of 5 characters")
    else:
        iter = 2
        button_iter = 0
        driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        driver.get(url)

        driver.find_element("name", "ctl00$MainContent$UserName").send_keys(username)
        driver.find_element("name", "ctl00$MainContent$Password").send_keys(password)
        driver.find_element("id","MainContent_LoginButton").click()
        driver.find_element("id","imputaciones").click()

        while Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$ddlOficina")).first_selected_option.text == "Fuera de Oficina":
            iter += 1
            button_iter += 1
            
        Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$ddlOficina")).options[2].click()
        sleep(1)
        Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$ddlProyecto")).options[int(project)].click()
        sleep(1)
        Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$ddlTareas")).options[int(task)].click()
        driver.find_element("id", f"MainContentPlaceHolder_RepetidorDia_GridView_dia_{datetime.today().weekday()}_buttonComment_{button_iter}").click();
        driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$Observaciones").send_keys(description)
        #driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl04$GridView_dia$ctl0{iter}$Fin").send_keys(time)
        sleep(0.5)
        driver.find_element("id", "MainContentPlaceHolder_ButtonEntrada").click()


        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("[!] no alert detected")

        sleep(0.5)
        driver.find_element("id", "btnAceptar").click()
        sleep(2);

        driver.quit()

        print("[+] Fichaje realizado exitosamente!")

def listout():
    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.minimize_window()
    driver.get(url)

    driver.find_element("name", "ctl00$MainContent$UserName").send_keys(username)
    driver.find_element("name", "ctl00$MainContent$Password").send_keys(password)
    driver.find_element("id","MainContent_LoginButton").click()
    driver.find_element("id","imputaciones").click()
    countp = 0
    countt = 0
    total = 0
    print("\n")
    for project in Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl02$ddlProyecto")).options:
        total = 0
        if project.text == "" : continue
        countp += 1
        Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl02$ddlProyecto")).options[int(countp)].click()
        sleep(1)
        print(str([countp]) + " " + project.text)
        for task in Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl02$ddlTareas")).options:
            total += 1
            if task.text == "" :
                countt = 0
                continue
            countt += 1
            print("\n    "+ str(countt) + ". " + task.text[4:])
            if len(Select(driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl02$ddlTareas")).options) == total:
                print("")
    driver.quit()