import requests
import json
import pandas as pd




def astros():
    url = "http://api.open-notify.org/astros" # ENDPOINT
    response = requests.get(url) # Peticion a las APIS. Lo que cambia es que hacemos con ello
    # A partir de aqui
    if response.status_code == 200:
        data = response.json()
        # text = json.dumps(data, indent=4, sort_keys=True)
        personas = data['people']

        # PAsarlo a data frame
        df = pd.DataFrame(personas)
        df.to_csv('datasets/iss_people.csv', index=False)

        for persona in personas:
            print(persona['name'])


        # print(type(data))
        # print(text)
    else:
        print("Error en la respuesta: ", response.status_code)


def paises(pais):
    url = f"https://restcountries.com/v3.1/name/{pais}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pais = data[0]
        nombre_oficial = pais['name']['official']
        poblacion = pais['population']
        capital = pais["capital"][0]
        region = pais["region"]
        print("Nombre oficial: ", nombre_oficial)
        print("Poblacion: ", poblacion)
        print("Capital: ", capital)
        print("Region: ", region)

    else:
        print("Error en la respuesta: ", response.status_code)


def clima():

    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": 32.5027,
        "longitude": -117.0037,
        "timezone" : "America/Los_Angeles",
        "hourly":"temperature_2m"
    }
    response = requests.get(url, params=parametros)

    if response.status_code == 200:
        data = response.json()
        time = data['hourly']['time']
        temperature = data['hourly']['temperature_2m']

        d = {"time": time, "temperature": temperature}
        df = pd.DataFrame(d)
        df.to_csv('datasets/clima.csv', index=False)

        print("Temperatura actual: ", temperature)
        print("Time: ", time)
    else:
        print("Error en la respuesta: ", response.status_code)


if __name__ == '__main__':
    #astros()
    #paises("mexico")
    clima()