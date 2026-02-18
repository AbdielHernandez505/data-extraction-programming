
# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 17 de febrero de 2026
# Descripción: Desarrollar un proceso de Web Scraping. Desarrollar una función que reciba como parámetro el nombre de
# un producto a buscar dentro de una página de compras seleccionada. Esta función contendrá el código necesario para
# realizar la búsqueda del producto en dicha página.
# La función deberá incluir la capacidad de visitar un número determinado de páginas de resultados de la búsqueda.
# Para cada una de estas páginas, se deberá capturar una imagen usando Selenium y guardar las capturas de pantalla
# en una carpeta específica. El número de páginas a visitar también deberá ser un parámetro de la función.

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar():
    busqueda = input("Ingresa el producto a buscar: ") # Se le pide al usuario el producto a buscar

    numero = int(input("Numero de paginas a capturar: ")) # Numero de paginas de resultados que hara el programa.

    print("Iniciando...")

    time.sleep(1)

    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200,800") # Configurar las medidas en que se abrirá el navegador
    navegador = webdriver.Chrome(options=opc, service=s)
    navegador.get("https://www.amazon.com.mx/") # poner la pagina web que abrirá el navegador. Yo seleccione AMAZON

    time.sleep(2) # El tiempo que estará en pausa antes de ejecutar la siguiente opción

    txtbuscar = navegador.find_element(By.ID, "twotabsearchtextbox") # ID para el buscador

    txtbuscar.send_keys(busqueda) # Escribir en el buscador

    txtbuscar.send_keys(Keys.ENTER) # Darle literalmente a la tecla ENTER, así evitamos usar el botón de buscar del propio amazon
    time.sleep(2)
    navegador.save_screenshot(f"images/pagina_1.png") # Despues de un lapso de tiempo, toma captura de la pagina 1.
    time.sleep(2)

    # Entramos a un ciclo, donde el rango es el número que el usuario introdujo antes.
    # Pero el -1 se usa porque ya contamos la primera pagina como el "primer numero"
    # que dicto el usuario. Así no habria 5 capturas de 4 paginas que pidio el usuario

    for i in range(numero-1):
        time.sleep(2)
        btn = navegador.find_element(By.CLASS_NAME, "s-pagination-next") # busca el elemento del boton "siguiennte"

        btn.click() # hace clic en el boton
        time.sleep(2)
        navegador.save_screenshot(f"images/pagina_{i+2}.png") # guarda la captura,
        time.sleep(2)                                           # el +2 porque ya inicializamos las capturas, sino se remplazaria.

    navegador.close() # Cerrar el navegador

if __name__ == "__main__":
    buscar()