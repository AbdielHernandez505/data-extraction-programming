
# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 17 de febrero de 2026
# Descripción: PROCESO WEBSCRAPING CON AMAZÓN

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time


def webscraping_amazon(producto, numero_paginas):

    # Diccionario donde guardaremos los datos
    data = {
        "nombre": [],
        "precio": [],
        "rating": []
    }

    # Configuración del navegador
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1200,800")
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://www.amazon.com.mx/")
    time.sleep(2)

    # Buscar producto
    buscador = navegador.find_element(By.ID, "twotabsearchtextbox")
    buscador.send_keys(producto)
    buscador.send_keys(Keys.ENTER)
    time.sleep(3)

    # Recorrer páginas
    for pagina in range(numero_paginas):

        print(f"Extrayendo página {pagina + 1}")

        productos = navegador.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

        for item in productos:

            # --------- Nombre ----------
            try:
                nombre = item.find_element(By.TAG_NAME, "h2").text
            except:
                nombre = "No disponible"

            # --------- Precio ----------
            try:
                precio = item.find_element(By.CLASS_NAME, "a-price-whole").text
            except:
                precio = "No disponible"

            # --------- Rating ----------
            try:
                rating_elemento = item.find_element(By.XPATH, ".//span[contains(@class,'a-icon-alt')]")
                rating_texto = rating_elemento.get_attribute("innerHTML")
                rating = rating_texto.split(" ")[0]
            except:
                rating = "0"

            data["nombre"].append(nombre)
            data["precio"].append(precio)
            data["rating"].append(rating)

        # Ir a siguiente página
        try:
            siguiente = navegador.find_element(By.XPATH, "//a[contains(@class,'s-pagination-next')]")
            siguiente.click()
            time.sleep(3)
        except:
            print("No hay más páginas disponibles.")
            break

    navegador.close()

    # Crear DataFrame
    df = pd.DataFrame(data)

    # Guardar CSV
    df.to_csv("dataset/productos_amazon.csv", index=False)

    return df


if __name__ == "__main__":
    busqueda = "nintendo switch"
    paginas = 3
    df_resultado = webscraping_amazon(busqueda, paginas)
    print(df_resultado.head())