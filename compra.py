from dba import dba
from usuario import Usuario
from datetime import date
from dba import db
class Compra():
    def __init__(self,id,usuario,precio_final,nombre):
        self.id=id
        self.fecha_compra=date.today()
        self.productos=[]
        self.usuario=usuario
        self.precio_final=0
        self.nombre=nombre

    def get_id (self):
        return self.id
    def get_fecha_compra(self):
        return self.fecha_compra
    def get_productos(self):
        return self.productos
    def get_usuario(self):
        return self.usuario
    def get_precio_final(self):
        return self.precio_final
    def get_nombre(self):
        return self.nombre

    def set_id(self,id):
        self.id=id
    def set_fecha_compra(self,fecha_compra):
        self.fecha_compra=fecha_compra
    def set_productos(self,productos):
        self.productos=productos
    def set_usuario(self,usuario):
        self.usuario=usuario
    def set_precio_final(self,precio_final):
        self.precio_final=precio_final
    def set_nombre(self,nombre):
        self.nombre=nombre

    def save(self):
        sql=("insert into compras (fecha_compra,id_usuario,precio_final,nombre) values(%s,%s,%s,%s)")
        val=(self.get_fecha_compra(),self.get_usuario().get_id(),self.get_precio_final(),self.get_nombre())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

