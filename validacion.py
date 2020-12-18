from dba import dba
from usuario import Usuario
from validate_email import validate_email
import base64


class Validator():
    
    def __init__(self):
        pass
    def validar_us(self,dic):
        datos_finales={}
        errores={}
        SpecialSym=[".","-","_","@","#","%"]
        for x, y in dic.items():
            datos_finales[x]=y.strip()
        
        if datos_finales["nombre"]=="":
            errores["nombre"]=="campo nombre incompleto"
        if datos_finales["apellido"]=="":
            errores["apellido"]=="campo apellido incompleto"
        if datos_finales["fecha_nac"]=="":
            errores["fecha_nac"]=="campo fecha de nacimiento incompleto"
        if datos_finales["interes"]=="":
            errores["interes"]=="campo interes incompleto"
        if datos_finales["celular"]=="":
            errores["celular"]=="campo celular incompleto"
        
        if datos_finales["email"]=="":
            errores["email"]=="campo email incompleto"
        elif validate_email(datos_finales["email"]) == False:
            errores["email"]="El campo Email no tiene formato Mail"


        if datos_finales["password"]=="":
            errores["password"]=="campo password incompleto"
        elif len(datos_finales["password"])< 6:
            errores["password"]="La contraseña debe tener al menos 7 caracteres"
        elif not any(char.isdigit() for char in datos_finales["password"]):
            errores["password"]='Password debe tener un caracter numeral'
        elif not any(char.isupper() for char in datos_finales["password"]):
            errores["password"]='Password debe tener una palabra mayuscula'
        elif not any(char.islower() for char in datos_finales["password"]):
            errores["password"]='Password debe tener minusculas'
        elif not any(char in SpecialSym for char in datos_finales["password"]):
            errores["password"]='Password debe tener al menos un caracter especial $@#'
        
        elif datos_finales["cpassword"]=="":
            errores["cpassword"]="campo password incompleto"
        elif datos_finales["cpassword"]!=datos_finales["password"]:
            errores["cpassword"]="Las contraseñas no coinciden"
        if datos_finales["genero"]=="":
            errores["genero"]=="campo genero incompleto"
        if datos_finales["celular"].isdigit()==False:
            errores["celular"]="El celular contiene letras."
        if datos_finales["ciudad"]=="":
            errores["ciudad"]=="Campo ciudad incompleto."
        if datos_finales["banco"]=="":
            errores["banco"]=="Campo banco incompleto."

        




        if errores=={}:
            sql="select ID from usuarios where email=%s"
            val=(datos_finales["email"],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores["email"]="El email ya esta registrado en nuestra base"
                return errores

        if errores=={}:
            sql="select ID from usuarios where celular=%s"
            val=(datos_finales["celular"],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores["celular"]="El numero ya esta registrado en nuestra base"
        
                return errores
        return errores

    def validar_pro(self,dic):
        datos_finales={}
        errores={}
        for x, y in dic.items():
            datos_finales[x]=str(y).strip()
        
        if datos_finales["nombre"]=="":
            errores["nombre"]=="campo nombre incompleto"
        if datos_finales["precio"]=="":
            errores["precio"]=="campo precio incompleto"
        if datos_finales["categoria"]=="":
            errores["categoria"]=="campo categoria incompleto"
        if datos_finales["marca"]=="":
            errores["marca"]=="campo marca incompleto"
        if errores=={}:
            sql="select ID from productos where nombre=%s"
            val=(datos_finales["nombre"],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores["nombre"]="El producto ya esta registrado en nuestra base, deberias modificarlo"
                return errores
        return errores
    
    def validar_login(self,dic):
        sql="select * from usuarios where email=%s"
        val=(dic["email"],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchall()
        if result==[]:
            return False
        if base64.decodebytes(bytes(result[0][7].strip(),"utf-8")).decode("UTF-8")==dic["password"]:
            return result[0]            
        else:
            return False

    def validar_us_modif(self,dic):
        datos_finales={}
        errores={}
        SpecialSym=[".","-","_","@","#","%"]
        for x, y in dic.items():
            datos_finales[x]=y.strip()
        
        if datos_finales["nombre"]=="":
            errores["nombre"]=="campo nombre incompleto"
        if datos_finales["apellido"]=="":
            errores["apellido"]=="campo apellido incompleto"
        if datos_finales["fecha_nac"]=="":
            errores["fecha_nac"]=="campo fecha de nacimiento incompleto"
        if datos_finales["interes"]=="":
            errores["interes"]=="campo interes incompleto"
        if datos_finales["celular"]=="":
            errores["celular"]=="campo celular incompleto"
        
        if datos_finales["email"]=="":
            errores["email"]=="campo email incompleto"
        elif validate_email(datos_finales["email"]) == False:
            errores["email"]="El campo Email no tiene formato Mail"


        if datos_finales["password"]=="":
            errores["password"]=="campo password incompleto"
        elif len(datos_finales["password"])< 6:
            errores["password"]="La contraseña debe tener al menos 7 caracteres"
        elif not any(char.isdigit() for char in datos_finales["password"]):
            errores["password"]='Password debe tener un caracter numeral'
        elif not any(char.isupper() for char in datos_finales["password"]):
            errores["password"]='Password debe tener una palabra mayuscula'
        elif not any(char.islower() for char in datos_finales["password"]):
            errores["password"]='Password debe tener minusculas'
        elif not any(char in SpecialSym for char in datos_finales["password"]):
            errores["password"]='Password debe tener al menos un caracter especial $@#'
        
        elif datos_finales["cpassword"]=="":
            errores["cpassword"]="campo password incompleto"
        elif datos_finales["cpassword"]!=datos_finales["password"]:
            errores["cpassword"]="Las contraseñas no coinciden"
        if datos_finales["genero"]=="":
            errores["genero"]=="campo genero incompleto"
        if datos_finales["celular"].isdigit()==False:
            errores["celular"]="El celular contiene letras."
        if datos_finales["ciudad"]=="":
            errores["ciudad"]=="Campo ciudad incompleto."
        if datos_finales["banco"]=="":
            errores["banco"]=="Campo banco incompleto."


        if errores=={}:
            sql="select ID from usuarios where celular=%s"
            val=(datos_finales["celular"],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores["celular"]="El numero ya esta registrado en nuestra base"
        
                return errores
        return errores


validator=Validator()



