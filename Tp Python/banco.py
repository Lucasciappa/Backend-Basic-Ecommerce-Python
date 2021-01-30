from dba import dba
class Banco():
    def __init__(self,nombre):
        self.id=0
        self.nombre=nombre
    
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_id(self,id):
        self.id=id

    def acreditar(self,monto):
        self.balance=self.balance+monto
    def debitar(self,monto):
        self.balance=self.balance-monto
        
    def save(self):
        sql=("insert into bancos (nombre) values(%s)")
        val=(self.get_nombre(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
        