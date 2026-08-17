import sqlite3 # Importa sqlite para hacer bases de datos

def start():
    conexion = sqlite3.connect("database.sot") # Se conecta a una base de datos, el archivo puede tener cualquier extensión
    cursor = conexion.cursor() # El modulo que trabaja con esta
    return conexion, cursor

def exit_db(conexion):
    conexion.commit() # Guarda Los Cambios
    conexion.close() # Cierra la base de datos

def comprobation():
    conexion, cursor = start()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        passwd TEXT NOT NULL
    )
    """) # Crea una tabla si es que no existe y le dice que tenga 3 columnas, la primera el ID del dato, la segunda, un texto llamado servicio y la ultima otro texto llamado password

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        mail TEXT NOT NULL
    )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS access (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        access_passwd TEXT NOT NULL
    )
    """)
    exit_db(conexion)

def password_db(service, passwd):
    # 1. Nos conectamos al archivo que ya existe
    conexion, cursor = start()
    
    # 2. Insertamos los datos de forma segura usando signos de interrogación (?)
    cursor.execute("""
    INSERT INTO passwords (service, passwd) 
    VALUES (?, ?)
    """, (service, passwd)) # rellena dentro de la tabla passwords una los valores service y passwd, la ? significa que cojera los valores externos que le demos
    
    # 3. Guardamos los cambios y cerramos
    exit_db(conexion)
    return "The password have been added correctly to the database"

def mail_db(service, mail):
    conexion, cursor = start()

    cursor.execute("""
    INSERT INTO mail (service, mail) 
    VALUES (?, ?)
    """, (service, mail))
    exit_db(conexion)
    return "The mail have been added correctly to the database"

def count_passwords():
    conexion, cursor = start()
    
    # 1. Traemos solo la columna 'service' de todas las filas
    cursor.execute("SELECT service FROM passwords") # Busca todos los valores en la tabla que coincidan con service
    
    # 2. fetchall() trae TODAS las filas de la bandeja (no solo una)
    # Nos devolverá una lista de tuplas, por ejemplo: [('Netflix',), ('Spotify',)]
    filas = cursor.fetchall() # Todos los valores anteriormente seleccionados se guardan en la variable filas
    
    exit_db(conexion)
    
    # 3. Limpiamos las tuplas para quedarnos con una lista de texto bonita
    # Esto transforma [('Netflix',), ('Spotify',)] en ['Netflix', 'Spotify']
    servicios = [fila[0] for fila in filas]
    
    # 4. Usamos len() de Python para saber cuántos elementos hay (la altura)
    total = len(servicios)
    
    # 5. Devolvemos AMBOS datos: el número total y la lista de servicios
    return total, servicios

def count_mails():
    conexion, cursor = start()
    
    # 1. Traemos solo la columna 'service' de todas las filas
    cursor.execute("SELECT service FROM mail")
    
    # 2. fetchall() trae TODAS las filas de la bandeja (no solo una)
    # Nos devolverá una lista de tuplas, por ejemplo: [('Netflix',), ('Spotify',)]
    filas = cursor.fetchall()
    
    exit_db(conexion)
    
    # 3. Limpiamos las tuplas para quedarnos con una lista de texto bonita
    # Esto transforma [('Netflix',), ('Spotify',)] en ['Netflix', 'Spotify']
    servicios = [fila[0] for fila in filas]
    
    # 4. Usamos len() de Python para saber cuántos elementos hay (la altura)
    total = len(servicios)
    
    # 5. Devolvemos AMBOS datos: el número total y la lista de servicios
    return total, servicios

def get_password(service):
    """Busca la contraseña de un servicio específico."""
    conexion, cursor = start()
    
    # Buscamos el valor de la columna 'passwd' donde coincida el nombre del servicio
    cursor.execute("SELECT passwd FROM passwords WHERE service = ?", (service,)) # Busca la columna de la tabla que coincida con el servicio y luego obtiene su contraseña
    resultado = cursor.fetchone() # fetchone() trae solo la primera fila encontrada
    
    exit_db(conexion)
    
    if resultado:
        return resultado[0] # Retorna la contraseña (texto limpio)
    return None # Retorna None si el servicio no existe en la base de datos


def get_mail(service):
    """Busca el correo de un servicio específico."""
    conexion, cursor = start()
    
    # Buscamos el valor de la columna 'mail' donde coincida el nombre del servicio
    cursor.execute("SELECT mail FROM mail WHERE service = ?", (service,))
    resultado = cursor.fetchone()
    
    exit_db(conexion)
    
    if resultado:
        return resultado[0] # Retorna el correo (texto limpio)
    return None # Retorna None si el servicio no existe en la base de datos

def del_passwords(passwd_id):
    conexion, cursor = start()
    
    # DELETE FROM le dice qué tabla limpiar, WHERE especifica cuál ID exacto
    cursor.execute("DELETE FROM passwords WHERE id = ?", (passwd_id,))
    
    exit_db(conexion)
    return f"The row with ID {passwd_id} has been deleted from passwords."

def del_mails(mail_id):
    conexion, cursor = start()
    
    # DELETE FROM le dice qué tabla limpiar, WHERE especifica cuál ID exacto
    cursor.execute("DELETE FROM mail WHERE id = ?", (mail_id,))
    
    exit_db(conexion)
    return f"The row with ID {mail_id} has been deleted from mail."

def access_registration(new_access_passwd):
    # """Guarda la contraseña maestra por primera vez."""
    conexion, cursor = start()
    cursor.execute("INSERT INTO access (access_passwd) VALUES (?)", (new_access_passwd,))
    exit_db(conexion)
    return "Contraseña maestra configurada con éxito."

def access():
    # """Busca si ya existe una contraseña maestra guardada."""
    conexion, cursor = start()
    cursor.execute("SELECT access_passwd FROM access WHERE id = 1")
    resultado = cursor.fetchone()
    exit_db(conexion)
    
    if resultado:
        return resultado[0] # Devuelve la contraseña en texto limpio
    return None # Devuelve None si la tabla está vacía
