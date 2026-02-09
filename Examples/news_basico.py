import requests
from bs4 import BeautifulSoup



def extraer():
    response = requests.get("https://news.ycombinator.com/")
    data = {"Titulos": [], "Puntos": [], "Fecha": [], "Comentarios": []}
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")

        titulos = soup.find_all("span", class_="titleline")
        extras = soup.find_all("span", class_="subline")

        for item in titulos:
            data["Titulos"].append(item.text)

        for item in extras:
            puntos = item.find("span", class_="score")
            fecha = item.find("span", class_="age")
            if puntos:
                data["Puntos"].append(puntos.text)
            else:
                data["Puntos"].append("0 puntos")

            data["Fecha"].append(fecha["title"].split()[0].split("T")[0])

            comments = item.find_all("a")[-1]

            if "comments" in comments.text or "Comentarios" in comments.text:
                data["Comentarios"].append(comments.text)
            else:
                data["Comentarios"].append("0 comments")
    print(data)

# desventajas de beautifulsoup solamente se puede trabajar en paginas estaticas, paginas que no se actualizan.
# selenium

if __name__ == '__main__':
    extraer()