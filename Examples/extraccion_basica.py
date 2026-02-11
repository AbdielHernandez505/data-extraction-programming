from bs4 import BeautifulSoup
import pandas as pd

def pagina() -> str:
    return """
        <html>
            <body> 
                <h1 id="titulo"> Libros Disponibles </h1>
                <div class="libro" data-isbn="900-1">
                    <h2>Python basico</h2>
                    <span class="precio"> $1499 </span>  
                </div>
                
                 <div class="libro" data-isbn="900-2">
                    <h2>Python Intermedio</h2>
                    <span class="precio"> $599 </span>  
                </div>
                
                 <div class="libro" data-isbn="900-3">
                    <h2>Python Avanzado</h2>
                    <span class="precio"> $499 </span>  
                </div>
                
                
            </body>
        </html>
    
    """


def extraer(html:str):
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.div.span.prettify())
    titulo = soup.find("h1", id = "titulo")
    libros = soup.find_all("div", class_="libro")
    print("Cantidad total de libros: ", len(libros))

    data = []





    for item in libros:
        titulo_libro = item.find("h2")
        precio_libro = item.find("span", class_="precio")
        data.append({
            "ISBN": item["data-isbn"],
            "titulo": titulo_libro.text,
            "precio": precio_libro.text.strip()#.replace("$", ""),
        })
    return data


    # print(titulo.text) # <--------------Ambos son lo mismo
    # print(titulo.get_text()) #<______________|

if __name__ == '__main__':
    html = pagina()
    data = extraer(html)
    print(data)
    df = pd.DataFrame(data)
    df.to_csv("datasets/libros.csv", index=False)