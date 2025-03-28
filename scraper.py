import requests
from bs4 import BeautifulSoup

def obtener_tarifa_zona(peso, origen, destino):
    url = "https://www.kuronekoyamato.co.jp/ytc/en/search/payment/"
    
    # Simular un navegador con headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extraer la tarifa de la página (Ajustar este selector según el sitio)
        tarifa_element = soup.find(class_="result_price")  
        
        if tarifa_element:
            return tarifa_element.text.strip()
        else:
            return "No se pudo obtener la tarifa."
    else:
        return "Error al acceder a la página."
