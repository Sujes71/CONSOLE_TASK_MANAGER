from os import _exit
from tokenize import String
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
from datetime import datetime
import keyboard

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

username = "jesus.perez"
password = "26z3R%Y$jB^7"
url = "http://81.47.129.87:8080/"

def signout(project, task, description, time):
    if len(description) < 20:
        print("[!] Please enter a description with a length of more than 20 characters")
        _exit(0)
        
    done = True
    currenttime = datetime.now().strftime('%H%M%S')
    
    if time != 'None' and time != 'default' and time != '*':
        timeset = str(time)
        timeset = time.replace(':', '').strip()
        while True:
            currenttime = datetime.now().strftime('%H%M%S')
            if done:
                done = False

                if len(timeset) == 4:
                    timeset = timeset + "00"
                if len(timeset) == 6 and timeset.isnumeric() and int(timeset) >= 000000 and int(timeset) <= 235959:
                    t = ':'.join(timeset[i:i+2] for i in range(0, len(timeset), 2))
                    print(f'[+] sign out time configured at {t}')
                else:
                    print(f'[!] error: arg4 [{time}]: expected one valid arg4' )
                    print("""
                    arg4 = time to sign out <optional>
                        """ )
                    _exit(0)
                    
            if currenttime == timeset:
                done = True
                break
            
            elif keyboard.is_pressed('supr'):
                print('[-] sign out time desactivated')
                _exit(0)
            
    if time == 'default' or time == '*':
        timeset = 0
        
        while True:
            currenttime = datetime.now().strftime('%H%M%S')
            
            if done:
                done = False
                if abs(int(currenttime) - 150000) < abs(int(currenttime) - 183000) and (int(currenttime) - 150000) < 0: 
                    timeset = '150000'
                else:
                    timeset = '183000'
                
                t = ':'.join(timeset[i:i+2] for i in range(0, len(timeset), 2))
                print(f'[+] sign out time configured at {t}')

            if currenttime == timeset:
                done = True
                break
            
            elif keyboard.is_pressed('supr'):
                print('[-] sign out time desactivated')
                _exit(0)
    if done:
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
        if iter > 2 and (datetime.today().weekday() == 0 or datetime.today().weekday() == 2):
            if abs(int(currenttime) - 150000) < abs(int(currenttime) - 183000):
                driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$Inicio").send_keys('08:00:00')
            else:                            
                driver.find_element("name", f"ctl00$MainContentPlaceHolder$RepetidorDia$ctl0{datetime.today().weekday()}$GridView_dia$ctl0{iter}$Inicio").send_keys('15:00:00')
            
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
            _exit(0)

        sleep(1)
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