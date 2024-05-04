from bs4 import BeautifulSoup
import requests
import sqlite3

# Constantes
url = "https://www.shein.com.co/RecommendSelection/Women-Clothing-sc-017172961.html?adp=&categoryJump=true&ici=co_tab03navbar03&src_identifier=fc%3DWomen%20Clothing%60sc%3DWomen%20Clothing%60tc%3D0%60oc%3D0%60ps%3Dtab03navbar03%60jc%3DitemPicking_017172961&src_module=topcat&src_tab_page_id=page_home1714834898146"

# Realizar una solicitud GET para obtener el contenido de la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Extraer el HTML de la respuesta
    html_content = response.content

    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar el elemento que contiene el título
    title_elements = soup.find_all('a', class_='goods-title-link--jump')

    # Extraer el texto de cada título y guardarlos en una lista
    titles = [title_element.text.strip() for title_element in title_elements]

    # Encontrar los elementos que contienen los precios
    product_elements = soup.find_all('a', class_='S-product-card__img-container')

    # Extraer el precio de cada elemento
    origin_prices = [product_element.get('data-us-origin-price') for product_element in product_elements]


    # Encontrar todos los elementos <img> dentro del elemento <a> con la clase "S-product-card__img-container"
    image_elements = soup.find_all('a', class_='S-product-card__img-container')

    # Extraer la URL de la imagen de cada elemento
    image_urls = [image_element.find('img')['src'] for image_element in image_elements]

    # Inicializar la conexión con la base de datos SQLite
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()

    # Crear una tabla para almacenar los datos si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            imagen_url TEXT,
            precio TEXT
        )
    ''')

    # Insertar los datos recolectados en la tabla
    for title, image_url, product in zip(titles, image_urls, origin_prices):
        cursor.execute('INSERT INTO productos (titulo, imagen_url, precio) VALUES (?, ?, ?)', (title, image_url, product))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print("Operacion EXITOSA")

else:
    print("Verificación no exitosa")
