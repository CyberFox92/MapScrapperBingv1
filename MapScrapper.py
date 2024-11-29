from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time

#VARIABLES
"""DIRECTION COUNTERS"""
totalesRight = 0
totalesLeft = 0
totalesUp = 0
totalesDown = 0

"""TO SEARCH"""
search_objective = ""

"""RUTE/ID OF EXTENSION"""
extension_path = "./Extension.crx"
extension_id = "ofbhiclojhjkggpnapcnjjjdjlgcikdf"

"""TABS"""
mapScrapperTab = "https://mapsscraper.net/"
extensionTab = "chrome-extension://ofbhiclojhjkggpnapcnjjjdjlgcikdf/popup.html"

"""MAP"""
principalMap = ""
mapa = ""

"""SEARCH BAR"""
search_bar = ""

"""EXTENSION FRAME"""
iframes = ""
iframesOk = False

#FUNCTIONS

def inicializar_navegador():
    # Inicializamos el WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.bing.com/maps") # Abrimos Bing Maps
    return driver

def closeTabs():
    closeURL = [extensionTab, mapScrapperTab]
    for handle in windows:
        driver.switch_to.window(handle)  # Cambiar al contexto de la pestaña
        if driver.current_url in closeURL:
            print(f"Cerrando la ventana con URL: {driver.current_url}")
            driver.close()  # Cerrar la pestaña
    # Si aún queda una ventana abierta, puedes quedarte con ella
    remaining_windows = driver.window_handles
    if len(remaining_windows) == 1:
        driver.switch_to.window(remaining_windows[0])
        print(f"Quedando en la ventana con URL: {driver.current_url}")

def moveRight(driver, mapa, pixeles=100, duracion=0.5):
    """
    Hace el movimiento de un elemento que se le indique a la derecha.
    
    :param driver: Instancia del navegador controlado por Selenium.
    :param mapa: Identificacion del elemento a mover
    :param pixeles: Cantidad de píxeles a mover hacia la derecha (por defecto 100).
    :param duracion: Duración del movimiento en segundos (simula movimiento paulatino).
    """
    # Crear una instancia de ActionChains
    acciones = ActionChains(driver)

    # Hacer clic y mantener el clic en el centro del canvas
    acciones.move_to_element(mapa).click_and_hold()

    # Dividir el movimiento en pasos para simular la duración
    pasos = int(duracion * 10)  # Por ejemplo, 10 pasos por segundo
    desplazamiento_por_paso = pixeles / pasos

    for _ in range(pasos):
        acciones.move_by_offset(desplazamiento_por_paso, 0)
        acciones.pause(0.1)  # Pausa entre pasos para simular un movimiento suave

    # Soltar el clic
    acciones.release().perform()

def moveLeft(driver, mapa, pixeles=100, duracion=0.5):
    """
    Hace el movimiento de un elemento que se le indique a la izquierda.
    
    :param driver: Instancia del navegador controlado por Selenium.
    :param mapa: Identificacion del elemento a mover
    :param pixeles: Cantidad de píxeles a mover hacia la izquierda (por defecto 100).
    :param duracion: Duración del movimiento en segundos (simula movimiento paulatino).
    """
    # Crear una instancia de ActionChains
    acciones = ActionChains(driver)

    # Hacer clic y mantener el clic en el centro del canvas
    acciones.move_to_element(mapa).click_and_hold()

    # Dividir el movimiento en pasos para simular la duración
    pasos = int(duracion * 10)  # Por ejemplo, 10 pasos por segundo
    desplazamiento_por_paso = -pixeles / pasos

    for _ in range(pasos):
        acciones.move_by_offset(desplazamiento_por_paso, 0)
        acciones.pause(0.1)  # Pausa entre pasos para simular un movimiento suave

    # Soltar el clic
    acciones.release().perform()

def moveUp(driver, mapa, pixeles=100, duracion=0.5):
    """
    Hace el movimiento de un elemento que se le indique hacia arriba.
    
    :param driver: Instancia del navegador controlado por Selenium.
    :param mapa: Identificacion del elemento a mover
    :param pixeles: Cantidad de píxeles a mover hacia arriba (por defecto 100).
    :param duracion: Duración del movimiento en segundos (simula movimiento paulatino).
    """
    try:
        acciones = ActionChains(driver)

        # Centrar el cursor en el mapa con el offset deseado
        acciones.move_to_element_with_offset(mapa, -140, 140).click_and_hold().perform()

        # Iniciar movimiento hacia arriba
        pasos = int(duracion * 10)  # Número de pasos para simular el movimiento
        desplazamiento_por_paso = -pixeles / pasos  # Eje Y negativo

        for _ in range(pasos):
            acciones.move_by_offset(0, desplazamiento_por_paso).pause(0.1).perform()

        # Soltar el clic al finalizar el movimiento
        acciones.release().perform()

    except Exception as e:
        print(f"Error en moveUp: {e}")

def moveDown(driver, mapa, pixeles=100, duracion=0.5):
    """
    Hace el movimiento de un elemento que se le indique hacia abajo.
    
    :param driver: Instancia del navegador controlado por Selenium.
    :param mapa: Identificacion del elemento a mover
    :param pixeles: Cantidad de píxeles a mover hacia abajo (por defecto 100).
    :param duracion: Duración del movimiento en segundos (simula movimiento paulatino).
    """
    try:
        acciones = ActionChains(driver)

        # Centrar el cursor en el mapa con el offset
        acciones.move_to_element_with_offset(mapa, -140, 170).click_and_hold().perform()

        # Iniciar movimiento hacia abajo
        pasos = int(duracion * 10)  # Número de pasos para simular el movimiento
        desplazamiento_por_paso = pixeles / pasos  # Eje Y positivo

        for _ in range(pasos):
            acciones.move_by_offset(0, desplazamiento_por_paso).pause(0.1).perform()

        # Soltar el clic al finalizar el movimiento
        acciones.release().perform()

    except Exception as e:
        print(f"Error en moveDown: {e}")

search_objective = str(input("Que deseas buscar?"))

# Configurar opciones de Chrome para cargar la extensión
options = Options()
options.add_extension(extension_path)

driver = inicializar_navegador()

# Maximizamos la ventana para una mejor visualización
driver.maximize_window()

driver.get(f"chrome-extension://{extension_id}/popup.html")
print("Esperando que se carguen las ventanas")
time.sleep(5)

# Obtener todos los identificadores de las ventanas/pestañas
windows = driver.window_handles
time.sleep(1)

closeTabs()

time.sleep(1)

while iframesOk == False:
    try:
        iframes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME,
                                                                               'iframe'))) 
        # Verificar si la lista de iframes está vacía
        if iframes:
            iframesOk = True
            break
        if not iframes:
            raise Exception("No se encontraron iframes en la página.")
    except Exception as e:
            print("Error al encontrar iframes o interactuar con ellos:", e)
            # Recargar la página
            ActionChains(driver).send_keys(Keys.F5).perform()
            time.sleep(7)
            # Esperar un momento para que la página cargue
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))

time.sleep(2)

try:
    search_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "maps_sb")))

    # Hacemos clic en el campo de búsqueda (por si se necesita hacer clic para enfocarlo)
    search_bar.click()

    # Enviamos el texto al campo de búsqueda
    search_bar.send_keys(search_objective)
    
    # Enviamos la búsqueda (simulando el Enter)
    search_bar.send_keys(Keys.ENTER)

except Exception as e:
    print("Error al encontrar o interactuar con el campo de búsqueda:", e)

# Esperamos un poco para que la página cargue los resultados
time.sleep(7)

principalMap = driver.find_element(By.ID, "mapContainer")
mapa = principalMap.find_element(By.CLASS_NAME, "maplibregl-control-container")
driver.switch_to.frame('UNIQUE-ROOT-by69bq5xiupb')

# Comprobación de los botones dentro del iframe
buttons = driver.find_elements(By.TAG_NAME, "button")

# Recorremos los botones encontrados y verificamos su texto
for i, button in enumerate(buttons, start=1):
    button_text = button.text.strip()  # Obtenemos el texto del botón
        
    # Comprobamos si el texto es "Start Extraction"
    if button_text == "Start Extraction":
        button.click()
        print("Botón clickeado con éxito.")
                
        # Selector del div padre
        div_selector = "div.flex.flex-row.items-center.mb-2"
    
        # Textos esperados
        texto_esperando = "Please wait a moment."
        texto_listo = "Please move the map to discover more businesses nearby."
            
        while True:
            try:
                # Localizar el div padre con los textos de estado
                contenedor = driver.find_element(By.CSS_SELECTOR, div_selector)
            
                # Buscar todas las etiquetas <b> dentro del contenedor
                textos_b = [b.text for b in contenedor.find_elements(By.TAG_NAME, "b")]

                # Comparar los textos encontrados con los textos esperados
                if texto_esperando in textos_b:
                    print("Esperando a que el texto cambie...")
                    time.sleep(1)  # Ajustar el tiempo de espera según sea necesario

                elif texto_listo in textos_b:
                    driver.switch_to.default_content()
                    print("Texto detectado: 'Please move the map to discover more businesses nearby.'")

                    if totalesRight <= 5:
                        moveRight(driver, mapa, 80, 0.5)
                        totalesRight += 1
                        print("Se ha movido el mapa ", totalesRight, "veces.")
                    elif totalesRight == 6:
                        for i in range(totalesRight):
                            moveLeft(driver, mapa, 80, 0.2)
                        print(f"Se ha devulto el mapa",totalesRight,"movimentos")
                        totalesRight += 1
                    elif totalesRight == 7:
                        totalesRight += 1
                    else:
                        pass

                    if totalesRight == 8 and totalesLeft <= 5:
                        moveLeft(driver, mapa, 80, 0.5)
                        print("Se ha movido el mapa", totalesLeft, "veces.")
                        totalesLeft += 1
                    elif totalesLeft == 6:
                        for i in range(totalesLeft):
                            moveRight(driver, mapa, 80, 0.2)
                        print("Se ha devulto el mapa",totalesLeft,"movimentos")
                        totalesLeft += 1
                    elif totalesLeft == 7:
                        totalesLeft += 1
                    else:
                        pass
                    
                    if totalesLeft == 8 and totalesUp <= 5:
                        moveUp(driver, mapa, 80, 0.5)
                        totalesUp += 1
                        print("Se ha movido el mapa", totalesUp, "veces.")
                    elif totalesUp == 6:
                        for i in range(totalesUp):
                            moveDown(driver, mapa, 80, 0.2)
                        print("Se ha devuelto el mapa hacia abajo", totalesUp, "movimientos")
                        totalesUp += 1  
                    elif totalesUp == 7:
                        totalesUp += 1
                    else:
                        pass

                    if totalesUp == 8 and totalesDown <= 5:
                        moveDown(driver, mapa, 80, 0.5)
                        print("Se ha movido el mapa", totalesDown, "veces")
                        totalesDown += 1
                    elif totalesDown == 6:
                        for i in range(totalesDown):
                            moveUp(driver, mapa, 80, 0.2)
                        print("Se ha devuelto el mapa hacia arriba", totalesDown, "movimientos")
                        totalesDown += 1  # Avanzar para evitar que vuelva a entrar en este bloque
                    elif totalesDown == 7:
                        totalesDown += 1
                    else:
                        pass

                    driver.switch_to.frame('UNIQUE-ROOT-by69bq5xiupb')

                    time.sleep(2)

                    if totalesDown > 7 and totalesUp > 7 and totalesRight > 7 and totalesLeft > 7:
                        print("Se ha terminado el movimiento del mapa, comenzando la descarga de datos...")
                        print(totalesDown)
                        time.sleep(1)
                        botonDownload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                    "button.ivu-btn.ivu-btn-primary.w-full")))
                        botonDownload.click()
                        time.sleep(1)

                        downloadXlsx = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                         "//img[@alt='xlsx']/ancestor::li")))
                        # Paso 4: Mover el cursor hacia la opción y hacer clic
                        ActionChains(driver).move_to_element(downloadXlsx).click().perform()
                        print("Ha finalizado la descarga, cerrando el programa...")
                        time.sleep(7)
                        driver.quit()   

                else:
                    print(f"Texto inesperado detectado: {textos_b}")
                    time.sleep(1)

            except Exception as e:
                print(f"Error al buscar el elemento o texto: {e}")

                time.sleep(1)
    
    else:
        pass

quit()
