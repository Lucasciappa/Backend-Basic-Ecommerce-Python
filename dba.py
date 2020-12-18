import mysql.connector

dbconf={
    "host":"localhost",
    "user":"root",
    "password":"",
    "database":"ecommerce"
}

class db():
    def __init__(self):
        self.conexion=mysql.connector.connect(**dbconf)
        self.cursor=self.conexion.cursor()

    def get_cursor(self):
        return self.cursor
    def get_conexion(self):
        return self.conexion

dba=db()


"""
sql="SELECT * FROM productos ORDER BY nombre ASC"
        dba.get_cursor().execute(sql)
        result=dba.get_cursor().fetchall()
        for i in result:
            datos= "{0}. Nombre: {1}        | Precio: ${2} "
            print(datos.format(i[0],i[1],i[2],i[3],i[4]))
"""