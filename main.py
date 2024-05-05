        return None, None

def create_database(titles, prices):
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT,
                       precio TEXT)''')
    for title, price in zip(titles, prices):
        cursor.execute("INSERT INTO productos (titulo, precio) VALUES (?, ?)", (title.text.strip(), price.text.strip()))
    conn.commit()
    conn.close()

titles, prices = extract_data(url)

if titles and prices:
    create_database(titles, prices)
    print("Datos almacenados en la base de datos 'productos.db'.")
else:
    print("No se pudo extraer datos de la página.")
