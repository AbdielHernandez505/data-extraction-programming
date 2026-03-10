from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def login():
    user = "standard_user"
    password = "secret_sauce"


    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200,800")
    navegador = webdriver.Chrome(options = opc, service = s)
    navegador.get("https://www.saucedemo.com/")
    time.sleep(2)

    txtuser = navegador.find_element(By.ID,"user-name") # <--- tener cuidado con los valores. Deben ser exactos.
    txtPassword = navegador.find_element(By.ID,"password")
    btnlogin = navegador.find_element(By.ID, "login-button")

    txtuser.send_keys(user)
    time.sleep(2)
    txtPassword.send_keys(password)
    time.sleep(2)
    btnlogin.click()
    time.sleep(3)

    navegador.close()

def loginv2():
    user = "standard_user"
    password = "secret_sauce"

    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200,800")
    navegador = webdriver.Chrome(options=opc, service=s)
    navegador.get("https://www.saucedemo.com/")
    time.sleep(2)

    txtuser = navegador.find_element(By.ID, "user-name")  # <--- tener cuidado con los valores. Deben ser exactos.
    txtPassword = navegador.find_element(By.ID, "password")
    btnlogin = navegador.find_element(By.ID, "login-button")

    txtuser.send_keys(user)
    time.sleep(2)

    txtPassword.send_keys(password)
    txtPassword.send_keys(Keys.ENTER) # Forma uno de iniciar sesion con ENTER

    time.sleep(2)



    try:
        error = navegador.find_element(By.CLASS_NAME, "error-message-container.error")
        print("Login incorrecto")
        print("Mensaje:",error.text)
        navegador.save_screenshot("imagenes/error_login.png")
    except:
        print("Login exitoso")
        navegador.save_screenshot("imagenes/login.png")

    time.sleep(3)
    #btnlogin.click() # Forma dos de iniciar sesion con el boton LOGIN
    #time.sleep(3)

    navegador.close()




if __name__ == "__main__":
    loginv2()