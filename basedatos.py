import pymysql

def dame_conexion():
    #estos parametros se tendrian que cambiar si lo subimos a produccion en un servidor web
    return pymysql.connect(
        host = 'localhost',
        port = 3307,
        user = 'root',
        password = '',
        db = 'basedatosflask'
    )
    
def insertar_articulo(nombre, precio):
    conexion = dame_conexion()
    #el cursor apunta al dato
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO articulo (nombre,precio) VALUES (%s,%s)",(nombre, precio))
        conexion.commit()
        conexion.close()

def listar_articulos():
    conexion = dame_conexion()
    articulos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulo")
        # cursor.fetchall() me devuelve todos
        articulos = cursor.fetchall()
        conexion.close()
        return articulos
    
def elimnar_articulo(id):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articulo WHERE id=%s",(id))
        conexion.commit()
        conexion.close()
        
def obtener_articulo(id):
    conexion = dame_conexion()
    articulo = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulo WHERE id = %s", (id))
        # cursor.fetchone() me devuelve el primero que encuentra
        articulo = cursor.fetchone()
        conexion.close()
        return articulo

def actualizar_articulo(id, nombre, precio):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE articulo SET nombre= %s, precio= %s WHERE id = %s",(nombre,precio,id))
        conexion.commit()
        conexion.close()


    """
    
    if __name__ == '__main__':
    #dame_conexion()
    articulos = listar_articulos()
    print(articulos)
    
    """
