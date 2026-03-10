
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

def extraer(html, data):
    soup = BeautifulSoup(html, "html.parser")

    titulos = soup.find_all("span", class_="titleline")
    extras = soup.find_all("td", class_="subtext")

    for item in titulos:
        data["titulos"].append(item.text)

    for item in extras:
        puntos = item.find("span", class_="score")
        fecha = item.find("span", class_="age")
        if puntos:
            data["puntos"].append(puntos.text)
        else:
            data["puntos"].append("0 points")

        data["fecha"].append(fecha["title"].split()[0].split("T")[0])

        comentarios = item.find_all("a")[-1]
        if "comments" in comentarios.text or "comment" in comentarios.text:
            data["comentarios"].append(comentarios.text)
        else:
            data["comentarios"].append("0 comments")


def navegar(paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200,800")
    navegador = webdriver.Chrome(service= s, options= opc)
    navegador.get("https://news.ycombinator.com/")
    time.sleep(3)

    data = {"titulos": [], "puntos": [], "fecha": [], "comentarios": []}
    for pag in range(0, paginas):
        time.sleep(1)
        extraer(navegador.page_source, data)
        time.sleep(3)
        next = navegador.find_element(By.LINK_TEXT,"More") #link text es para los links que hay en las paginas
        next.click()


    df = pd.DataFrame(data)
    df.to_csv("datasets/news_v2.csv")
    navegador.close()



if __name__ == "__main__":
    paginas = 3
    navegar(paginas)