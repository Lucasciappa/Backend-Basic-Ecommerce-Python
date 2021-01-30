from usuario import Usuario
from productos import Producto
from compra import Compra
from banco import Banco
from ciudad import Ciudad
from categoria import Categoria
from marca import Marca
from validacion import validator
from dba import dba
import getpass

def Menu(): 
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("===================== CompuEcommerce ==================")
            print("======================= BIENVENIDO! ===================")
            print(" 1- Registrarse")
            print(" 2- Entrar")
            print(" 3- Salir")
            print("=======================================================")
            opcion= int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 3:
                print("Opcion incorrecta, intente nuevamente.")
            elif opcion == 3:
                continuar=False
                print("Gracias por usar este sistema.")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        return registrar_us()
    elif opcion == 2:
        return login()

lista_ciudades=[]
lista_bancos=[]  
def registrar_us():
    form_us={}
    print("")
    print("=============== REGISTRACION DE USUARIO ===================")
    form_us["nombre"]=input("Inserte su nombre: ")
    form_us["apellido"]=input("inserte su apellido: ")
    form_us["fecha_nac"]=input("Inserte su fecha de nacimiento (año/mes/dia): ")
    form_us["interes"]=input("¿Que producto es de su interes? : ")
    form_us["celular"]=input("Inserte su celular: ")
    form_us["email"]=input("inserte su email de contacto: ")
    form_us["password"]=getpass.getpass("(Recuerda que tiene que tener mas de 6 caracteres, al menos una mayuscula,un numero y un caracter especial)\n inserte una contraseña: ")
    form_us["cpassword"]=getpass.getpass("confirme su contraseña: ")
    form_us["genero"]=input("Inserte su genero: ")
    form_us["billetera"]=int(input("¿Cuanto dinero quiere tener en su billetera?"))
    form_us["ciudad"]=input("Inserte su ciudad: ")
    form_us["banco"]=input("Inserte el nombre de su banco: ")
    if validator.validar_us(form_us) == {}:
        if len(form_us["ciudad"]) > 3:
            sql="select nombre from ciudades"
            dba.get_cursor().execute(sql)
            result=dba.get_cursor().fetchall()
            for i in result:
                lista_ciudades.append(i[0])
            if (form_us["ciudad"] in lista_ciudades) == True:
                sql="select ID from ciudades where nombre=%s"
                val=(form_us["ciudad"],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                ciu1=Ciudad(form_us["ciudad"])
                ciu1.set_id(result[0])
            else:
                ciu1=Ciudad(form_us["ciudad"])
                sql="INSERT INTO ciudades (nombre) values (%s)"
                val=((form_us["ciudad"]),)
                dba.get_cursor().execute(sql,val)
                dba.get_conexion().commit()
                ciu1.set_id(dba.get_cursor().lastrowid)
        if len (form_us["banco"]) > 6:
            sql="select nombre from bancos"
            dba.get_cursor().execute(sql)
            result=dba.get_cursor().fetchall()
            for n in result:
                lista_bancos.append(n[0])
            if (form_us["banco"] in lista_bancos) == True:
                sql="select ID from bancos where nombre=%s"
                val=(form_us["banco"],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                ban1=Banco(form_us["banco"])
                ban1.set_id(result[0])
            else:
                ban1=Banco(form_us["banco"])
                sql="INSERT INTO bancos (nombre) values (%s)"
                val=((form_us["banco"]),)
                dba.get_cursor().execute(sql,val)
                dba.get_conexion().commit()
                ban1.set_id(dba.get_cursor().lastrowid)
       
        u1=Usuario(0,form_us["nombre"],form_us["apellido"],form_us["fecha_nac"],form_us["interes"],form_us["celular"],form_us["email"],form_us["password"],form_us["genero"],form_us["billetera"],ciu1.get_id(),ban1.get_id())
        u1.save()
        print("Usuario registrado exitosamente!")
        print("==================================================")
    else:
        print(validator.validar_us(form_us))


def login():
    form_login={}
    form_login["email"]=input("\nEscriba su Email: ")
    form_login["password"]=input("Escriba su contraseña: ")
    if (validator.validar_login(form_login) is not False) and (form_login["email"] == ("riki@gmail.com")):
        user=Usuario(*validator.validar_login(form_login))
        print("=========================================================")
        print(f"============ Bienvenido al menu de ADMINISTRADOR!!=======\n")
        return Menu_adm()
    elif validator.validar_login(form_login) is not False:
        user=Usuario(*validator.validar_login(form_login))       
        if 1+1 == 2:
            sql="select ID from usuarios where email=%s"
            val=(form_login["email"],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            user.set_id(result[0])
        if 4+4==8:
            sql="select nombre from bancos where ID=%s"
            val=(user.get_banco(),)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            bank=Banco(result[0])
        print()
        print("=======================================================")
        print(f"============ Bienvenido a CompuEcommerce {user.get_nombre()}!!=======\n")
        return Menu_us(user,bank)
    else:
        print("\nUsuario o contraseña incorrecta.\n")
        return login()

def Menu_us(user,bank):
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print(f"Nombre: {user.get_nombre()} ================= Billetera: ${user.get_billetera()} ====")
            print("========================= INICIO ======================")           
            print(" 1- Ver listado de productos")
            print(" 2- Finalizar compra")
            print(" 3- Modifica tus datos")
            print(" 4- Agregue dinero a tu billetera")
            print(" 5- Cerrar sesion")
            print("=======================================================")
            opcion= int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 5:
                print("\nOpcion incorrecta, intente nuevamente.\n")
            elif opcion == 5:
                continuar=False
                print(f"\nGracias por usar este sistema {user.get_nombre()}!!! \n")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion1(opcion,user,bank)

def Menu_adm():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while (not opcionCorrecta):
            print(f"Nombre: ADMINISTRADOR =================================")
            print("================ INICIO ADMINISTRACIÓN ================")           
            print(" 1- Agregar Productos nuevos")
            print(" 2- Eliminar Productos")
            print(" 3- Eliminar Usuarios")
            print(" 4- Cerrar sesion")
            print("=======================================================")
            opcion= int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 4:
                print("\nOpcion incorrecta, intente nuevamente.\n")
            elif opcion == 4:
                continuar=False
                print(f"\nGracias por usar este sistema!!! \n")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion2(opcion)


def ejecutarOpcion2(opcion):
    if opcion == 1:
        agregue_pro()
    elif opcion == 2:
        eliminar_pro()
    elif opcion == 3:
        eliminar_us()
    else:
        Menu_adm()



lista_categoria=[]
lista_marca=[]
def agregue_pro():
    form_pro={}
    form_pro["nombre"]=input("Nombre del producto nuevo: ")
    form_pro["precio"]=int(input("inserte su precio: "))
    form_pro["categoria"]=input("Inserte su categoria: ")
    form_pro["marca"]=input("Inserte su marca: ")
    form_pro["stock"]=input("Inserte el stock del producto")
    if validator.validar_pro(form_pro) == {}:
        if len(form_pro["categoria"]) > 3:
            sql="select nombre from categorias"
            dba.get_cursor().execute(sql)
            result=dba.get_cursor().fetchall()
            for i in result:
                lista_categoria.append(i[0])
            if (form_pro["categoria"] in lista_categoria) == True:
                sql="select ID from categorias where nombre=%s"
                val=(form_pro["categoria"],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                cat1=Categoria(form_pro["categoria"])
                cat1.set_id(result[0])
            else:
                cat1=Categoria(form_pro["categoria"])
                sql="INSERT INTO categorias (nombre) values (%s)"
                val=(form_pro["categoria"],)
                dba.get_cursor().execute(sql,val)
                dba.get_conexion().commit()
                cat1.set_id(dba.get_cursor().lastrowid)
        if len (form_pro["marca"]) > 3:
            sql="select nombre from marcas"
            dba.get_cursor().execute(sql)
            result=dba.get_cursor().fetchall()
            for n in result:
                lista_marca.append(n[0])
            if (form_pro["marca"] in lista_marca) == True:
                sql="select ID from marcas where nombre=%s"
                val=(form_pro["marca"],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                mar1=Marca(form_pro["marca"])
                mar1.set_id(result[0])
            else:
                mar1=Marca(form_pro["marca"])
                sql="INSERT INTO marcas (nombre) values (%s)"
                val=(form_pro["marca"],)
                dba.get_cursor().execute(sql,val)
                dba.get_conexion().commit()
                mar1.set_id(dba.get_cursor().lastrowid)

       
        p1=Producto(0,form_pro["nombre"],form_pro["precio"],form_pro["categoria"],form_pro["marca"],form_pro["stock"])
        p1.set_categoria(cat1.get_id())
        p1.set_marca(mar1.get_id())
        p1.save()
        print("Producto registrado exitosamente!")
        print("==================================================")
    else:
        print(validator.validar_pro(form_pro))


lista_pro_eli=[]
def eliminar_pro():
    sql="SELECT * FROM categorias"
    dba.get_cursor().execute(sql)
    result=dba.get_cursor().fetchall()
    print("\n================== CATEGORIAS =====================\n")
    for i in result:
        datos= "Código: {:2}  |  Nombre: {:5}"
        print(datos.format(i[0],i[1]))
        print("---------------------------------------------------")
    cat=int(input("\n Seleccione la categoria del producto a eliminar: "))
    if cat > 0 and cat < 11:
        print("\n====================================== PRODUCTOS ========================================\n")
        sql="SELECT ID, nombre, precio from productos WHERE id_categoria=%s"
        val=((cat),)
        dba.get_cursor().execute(sql,val)
        result1=dba.get_cursor().fetchall()
        for i in result1:
            datos= "Código Nº: {:4}  | Nombre: {:40}  |  Precio: ${:8} "
            print(datos.format(i[0],i[1],i[2]))
            print("-------------------------------------------------------------------------------------")
            lista_pro_eli.append(i[0])
        print("Código Nº:  100  | Volver atras")
        papa=int(input("\n Seleccionar código del producto a eliminar: "))
        if (papa in lista_pro_eli) == True:
            sql="DELETE FROM productos where id=%s"
            val=(papa,)
            dba.get_cursor().execute(sql,val)
            dba.get_conexion().commit()
            print("\nProducto eliminado satifactoriamente.\n")
            Menu_adm()
        elif papa == 100:
            eliminar_pro()
        else:
            print("\nOpcion incorrecta, intente nuevamente\n")
            eliminar_pro()
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")
        eliminar_pro()

lista_us_eli=[]
def eliminar_us():
    sql="SELECT id, nombre, apellido, email FROM usuarios"
    dba.get_cursor().execute(sql)
    result=dba.get_cursor().fetchall()
    print("\n=================== USUARIOS ======================\n")
    for i in result:
        datos= "Código: {:2}  |  Nombre: {:8} {:15}  | Email: {:4} "
        print(datos.format(i[0],i[1],i[2],i[3]))
        print("-----------------------------------------------------------------------")
        lista_us_eli.append(i[0])
    print("Código Nº:  100  | Volver atras")
    pepa=int(input("\n Seleccionar código del usuario a eliminar: "))
    if (pepa in lista_us_eli) == True:
        sql="DELETE FROM usuarios where id=%s"
        val=(pepa,)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        print("\nUsuario eliminado satifactoriamente.\n")
        Menu_adm()



lista_ciudades1=[]
lista_bancos1=[]
def ejecutarOpcion1(opcion,user,bank):
    if opcion == 1:
        listar_cat(user)
    elif opcion ==2:
        finalizar(user,bank)
    elif opcion == 3:
        print(f"\nModificaras tus datos {user.get_nombre()} {user.get_apellido()} \n")
        form_modif={}
        form_modif["nombre"]=input("Inserte su nombre: ")
        form_modif["apellido"]=input("inserte su apellido: ")
        form_modif["fecha_nac"]=input("Inserte su fecha de nacimiento (año/mes/dia): ")
        form_modif["interes"]=input("¿Que producto es de su interes? : ")
        form_modif["celular"]=input("Inserte su celular: ")
        form_modif["email"]=input("inserte su email de contacto: ")
        form_modif["password"]=getpass.getpass("(Recuerda que tiene que tener mas de 6 caracteres, al menos una mayuscula,un numero y un caracter especial)\n inserte una contraseña: ")
        form_modif["cpassword"]=getpass.getpass("confirme su contraseña: ")
        form_modif["genero"]=input("Inserte su genero: ")
        form_modif["ciudad"]=input("Inserte su ciudad: ")
        form_modif["banco"]=input("Inserte el nombre de su banco: ")
        if validator.validar_us_modif(form_modif) == {}:
            if len(form_modif["ciudad"]) > 3:
                sql="select nombre from ciudades"
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for i in result:
                    lista_ciudades1.append(i[0])
                if (form_modif["ciudad"] in lista_ciudades1) == True:
                    sql="select ID from ciudades where nombre=%s"
                    val=(form_modif["ciudad"],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    ciu1=Ciudad(form_modif["ciudad"])
                    ciu1.set_id(result[0])
                else:
                    ciu1=Ciudad(form_modif["ciudad"])
                    sql="INSERT INTO ciudades (nombre) values (%s)"
                    val=((form_modif["ciudad"]),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    ciu1.set_id(dba.get_cursor().lastrowid)
            
            if len (form_modif["banco"]) > 6:
                sql="select nombre from bancos"
                dba.get_cursor().execute(sql)
                result=dba.get_cursor().fetchall()
                for n in result:
                    lista_bancos1.append(n[0])
                if (form_modif["banco"] in lista_bancos1) == True:
                    sql="select ID from bancos where nombre=%s"
                    val=(form_modif["banco"],)
                    dba.get_cursor().execute(sql,val)
                    result=dba.get_cursor().fetchone()
                    ban1=Banco(form_modif["banco"])
                    ban1.set_id(result[0])
                else:
                    ban1=Banco(form_modif["banco"])
                    sql="INSERT INTO bancos (nombre) values (%s)"
                    val=((form_modif["banco"]),)
                    dba.get_cursor().execute(sql,val)
                    dba.get_conexion().commit()
                    ban1.set_id(dba.get_cursor().lastrowid)
            
            user=Usuario(0,form_modif["nombre"],form_modif["apellido"],form_modif["fecha_nac"],form_modif["interes"],form_modif["celular"],form_modif["email"],form_modif["password"],form_modif["genero"],user.get_billetera(),ciu1.get_id(),ban1.get_id())
            user.update(form_modif)
        else:
            print(validator.validar_us(form_modif))

    elif opcion == 4:
        bille=int(input(f"\nActualmente tienes ${user.get_billetera()}. ¿Cuanto dinero deseas acreditar?: "))
        user.set_billetera((user.get_billetera()+bille))
        print(f"\nMuchas gracias {user.get_nombre()}, fueron acreditados tus ${user.get_billetera()} \n")
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")

carrito_p=[]
carrito_n=[]
carrito_total=[]
factura=[]
def listar_cat(user):       
    sql="SELECT * FROM categorias"
    dba.get_cursor().execute(sql)
    result=dba.get_cursor().fetchall()
    print("\n===================CATEGORIAS======================\n")
    for i in result:
        datos= "Código: {:2}  |  Nombre: {:5}"
        print(datos.format(i[0],i[1]))
        print("---------------------------------------------------")
    cat=int(input("\n Seleccione el código de su interes: "))
    if cat > 0 and cat < 11:
        listar_pro(cat,user)
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")
        listar_cat(user)
   
listCod=[]
def listar_pro(cat,user):
    print("\n=======================================PRODUCTOS=========================================\n")
    sql="SELECT ID, nombre, precio, stock from productos WHERE id_categoria=%s"
    val=((cat),)
    dba.get_cursor().execute(sql,val)
    result1=dba.get_cursor().fetchall()
    for i in result1:
        datos= "Código Nº: {:4}  | Nombre: {:40}  |  Precio: ${:8}  |  Stock: {:2} "
        print(datos.format(i[0],i[1],i[2],i[3]))
        print("-------------------------------------------------------------------------------------")
        listCod.append(i[0])     
    print("Código Nº:  100  | Volver atras")
    pepe=int(input("\n Seleccionar código para agregar al carrito: "))
    if (pepe in listCod) == True:
        sql="SELECT nombre, precio from productos WHERE ID=%s"
        val=((pepe),)
        dba.get_cursor().execute(sql,val)
        result2=dba.get_cursor().fetchone()
        carrito_n.append(result2[0])
        carrito_p.append(result2[1])
        carrito_total.append(result2[1])
        carrito_total.append(result2[0])
        factura.append(result2)
        print(f"\nEl producto {result2[0]}, de ${result2[1]} fue agregado a tu carrito\n")
        print(f"Llevas gastado ${sum(carrito_p)}\n")
    elif pepe == 100:
        listar_cat(user)
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")
        listar_pro(cat,user)

def finalizar(user,bank):
    print(f"\nEl total de tu compra es de ${sum(carrito_p)}")
    print(f"En tu billetera tienes ${user.get_billetera()}\n")
    ok=input("Escribe 'ok' si estas de acuerdo o 'no' si no lo estas: ")
    if user.get_billetera() < sum(carrito_p):
        print("\nNo puedes realizar la compra. Necesitas agregar dinero en tu billetera.\n")
        Menu_us(user,bank)
    else:
        if ("ok") == ok.lower():
            user.set_billetera(user.get_billetera()-sum(carrito_p))
            print(f"\n{user.get_nombre()}, finalizaste tu compra. Muchas gracias por confiar en nosotros!.")
            print("\nTU FACTURA: ")
            print("===============================================================================")
            
            for i in factura:
                datos="|Producto: {:40} ===>   |Precio: ${:7} "
                print(datos.format(i[0],i[1]))
                print("===============================================================================")
            comp1=Compra(0,user,carrito_p[0],carrito_n[0])
            for i in carrito_n:
                sql="select * from productos where nombre=%s"
                val=(i,)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchall()
                pro_stock=Producto(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],(result[0][5]))
                pro_stock.resta_stock()

            for x, y in zip(carrito_p,carrito_n):
                comp1.set_precio_final(x)
                comp1.set_nombre(y)
                comp1.save()
            print(f"|TOTAL:                                             ===>   |Precio: $ {sum(carrito_p)} ")    
            print("###############################################################################")
            print(f"\n{user.get_nombre()}, Te quedaron ${user.get_billetera()} en tu billetera.\nQUE LO DISFRUTES, VUELVA PRONTO!!\n\n\n\n")
            user.update_billetera(user.get_id())
            Menu()
        elif ("no") == ok.lower():
            print(f"\n{user.get_nombre()} No aceptaste finalizar la compra, seras redirigido al menu.\n")
            Menu_us(user,bank)
        else:
            print("\nRespuesta incorrecta.\n")


Menu()