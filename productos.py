from dba import dba
class Producto():
    def __init__(self,id,nombre,precio,categoria,marca):
        self.id=0
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.marca=marca

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_categoria(self):
        return self.categoria
    def get_marca(self):
        return self.marca



    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_precio(self,precio):
        self.precio=precio
    def set_categoria(self,categoria):
        self.categoria=categoria
    def set_marca(self,marca):
        self.marca=marca


    def save(self):
        sql="INSERT INTO productos (nombre,precio,id_categoria,id_marca) values (%s,%s,%s,%s)"
        val=(self.get_nombre(),self.get_precio(),self.get_categoria(),self.get_marca())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql="DELETE FROM productos where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def listar_pro(self):
        sql="SELECT * FROM productos ORDER BY nombre ASC"
        dba.get_cursor().execute(sql)
        dba.get_conexion().commit()
        result=dba.get_cursor().fetchall()
        return result
        