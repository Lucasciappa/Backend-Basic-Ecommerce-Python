from dba import dba
from ciudad import Ciudad
from banco import Banco
import base64
class Usuario():
    def __init__(self,id,nombre,apellido,fecha_nac,interes,celular,email,password,genero,billetera,ciudad,banco):
        self.id=0
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nac=fecha_nac
        self.interes=interes
        self.celular=celular
        self.email=email
        self.password=self.encriptar_pass(password)
        self.genero=genero
        self.billetera=0
        self.ciudad=ciudad
        self.banco=banco

    
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_fecha_nac(self):
        return self.fecha_nac
    def get_interes(self):
        return self.interes
    def get_celular (self):
        return self.celular
    def get_email (self):
        return self.email
    def get_password(self):
        return self.password
    def get_genero (self):
        return self.genero
    def get_billetera(self):
        return self.billetera
    def get_ciudad(self):
        return self.ciudad
    def get_banco (self):
        return self.banco
    
    def set_id(self,id):
        self.id=id
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_apellido(self,apellido):
        self.apellido=apellido
    def set_fecha_nac(self,fecha_nac):
        self.fecha_nac=fecha_nac
    def set_interes(self,interes):
        self.interes=interes
    def set_celular(self,celular):
        self.celular=celular
    def set_email(self,email):
        self.email=email   
    def set_password(self,password):
        self.password=self.encriptar_pass(password)
    def encriptar_pass(self,password):
        return base64.encodebytes(bytes(password, 'utf-8')) 
    def desencriptar_pass(self,password):
        return base64.decodebytes(password).decode("UTF-8")
    def set_genero(self,genero):
        self.genero=genero
    def set_billetera(self,billetera):
        self.billetera=billetera
    def set_ciudad(self,ciudad):
        self.ciudad=ciudad
    def set_banco(self,banco):
        self.banco=banco
      
# Registrar Usuarios
    def save(self):
        sql="INSERT INTO usuarios (nombre, apellido,fecha_nac, interes,celular,email,contraseña,genero,billetera,id_ciudad,id_banco) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self.get_nombre(),self.get_apellido(),self.get_fecha_nac(),self.get_interes(),self.get_celular(),self.get_email(),self.get_password(),self.get_genero(),self.get_billetera(),self.get_ciudad(),self.get_banco())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
# Eliminar Usuarios
    def delete(self):
        sql="DELETE FROM usuarios where id=%s"
        val=(self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

# Modificar Usuarios
    def update(self,dic):
        sql="select ID from usuarios where email=%s"
        val=(self.get_email(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_nombre(dic["nombre"])
        self.set_apellido(dic["apellido"])
        self.set_fecha_nac(dic["fecha_nac"])
        self.set_interes(dic["interes"])
        self.set_celular(dic["celular"])
        self.set_email(dic["email"])
        self.set_password(dic["password"])
        self.set_genero(dic["genero"])
        
        sql="UPDATE usuarios set nombre=%s, apellido=%s, fecha_nac=%s, interes=%s, celular=%s, email=%s, contraseña=%s, genero=%s,id_ciudad=%s,id_banco=%s where id=%s"
        val=(self.get_nombre(),self.get_apellido(),self.get_fecha_nac(),self.get_interes(),self.get_celular(),self.get_email(),self.get_password(),self.get_genero(),self.get_ciudad(),self.get_banco(),result[0])
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        print(f"\n{self.get_nombre()} {self.get_apellido()}, sus datos fueron modificados Satifactoriamente!!\n")


    def update_billetera(self,id):
        sql="UPDATE usuarios set billetera=%s where id=%s"
        val=(self.get_billetera(),self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    