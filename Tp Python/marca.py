from dba import dba

class Marca():
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