from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def obtener_tarifa_zona(peso, origen, destino):
    url = "https://www.kuronekoyamato.co.jp/ytc/en/search/payment/"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)

        peso_input = driver.find_element(By.NAME, "weight")
        peso_input.clear()
        peso_input.send_keys(str(peso))

        origen_input = driver.find_element(By.NAME, "from")
        origen_input.send_keys(str(origen))
        
        destino_input = driver.find_element(By.NAME, "to")
        destino_input.send_keys(str(destino))

        destino_input.send_keys(Keys.RETURN)
        time.sleep(2)

        tarifa_element = driver.find_element(By.CLASS_NAME, "result_price")
        tarifa = tarifa_element.text

        return tarifa

    except Exception as e:
        return f"Error al obtener tarifa: {e}"
    finally:
        driver.quit()
