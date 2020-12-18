from dba import dba

class Categoria():
    def __init__(self,nombre):
        self.id=0
        self.nombre=nombre

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre

    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre



    # Registrar Categoria
    def save(self):
        sql="INSERT INTO categorias (ID,nombre) values (%s,%s)"
        val=(self.get_id(),self.get_nombre())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    # Eliminar Categoria
    def delete(self):
        sql="DELETE FROM categorias where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
