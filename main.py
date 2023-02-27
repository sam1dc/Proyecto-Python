# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en una estructura de datos diccionario, en el que la clave de
# cada cliente será su Cédula de Identidad, y el valor será otro diccionario con los datos del
# cliente (nombre, sexo, fecha de nacimiento, dirección, teléfono, correo). Un cliente es
# Tercera edad o Preferente si es sexo femenino y edad mayor o igual a 55 años, o
# masculino y edad mayor o igual a 60 años.
# El Sistema debe llevar el registro de los clientes y debe manejar clave de acceso. Esta
# debe ser encriptada de acuerdo a tres (3) niveles de seguridad: Bajo, medio y fuerte y
# debe cumplir con mínimo 8 dígitos y 10 dígitos máximo (con caracteres como una clave
# de acceso de un banco).

# El Sistema debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente,
# (2) Eliminar cliente,
# (3) Mostrar cliente,
# (4) Listar todos los clientes,
# (5) Listar clientes Tercera edad,
# (6) Terminar.

# En función de la opción elegida el programa deberá hacer lo siguiente:
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de
# datos.
# Preguntar por la Cédula de Identidad del cliente y eliminar sus datos de la base de datos.
# Preguntar por la Cédula de Identidad del cliente y mostrar sus datos, incluyendo el
# cálculo de su edad.
# Mostrar lista de todos los clientes de la base datos con sus datos.
# Mostrar la lista de clientes de Tercera edad o Preferentes de la base de datos con su
# Cédula de Identidad y nombre.
# Terminar el programa.

# Integrantes:

# Lucianny Alvarado CI: 31.038.315
# Andrew González   CI: 32.465.826
# Nairobis Salcedo  CI: 30.997.306
# Ygor Rivera       CI: 30.453.868
# Samuel Cortez     CI: 27.158.842

import hashlib

usuario = {}
cliente = {}
clientes = []
banderaDeSesion = False
bandera = "s"
menuDeSesion = """Bienvenido!, seleccione una de las siguiente opciones en pantalla
1.Registrarse
2.Iniciar Sesion
3.Salir"""

requerimiento = """
Al registar una clave debe contener
* La contraseña debe contener mínimo 8 caracteres.
* Debe contener al menos; minúscula, mayúscula y números.
* No puede haber espacios en blancos en la contraseña.
Si cumple con todos estos requisitos debe retornar el mensaje 'Clave de Acceso Segura'
"""

# Menu de Opciones
menu = """¿Qué opcion deseas realizar?
1.Agregar cliente
2.Eliminar cliente
3.Mostrar cliente
4.Listar todos los clientes
5.Listar clientes preferentes
6.Salir"""

while banderaDeSesion == False:
  print(menuDeSesion)
  opcionDeSesion = int(input())
  if opcionDeSesion == 1:
    print(requerimiento)
    l, u, p, d = 0, 0, 0, 0
    usuario["nombre"] = input("Ingrese un Nombre: ")
    usuario["clave"] = input("Ingrese una Clave de Acceso: ")
    if (len(usuario["clave"]) >= 8 and len(usuario["clave"]) <= 10):
        for i in usuario["clave"]:
            # contando letras minúsculas
            if (i.islower()):
                l+=1           
            # contando letras mayúsculas
            if (i.isupper()):
                u+=1           
            # contando dígitos
            if (i.isdigit()):
                d+=1           
            # contando los caracteres especiales mencionados
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if (l>=1 and u>=1 and p>=3 and d>=3 and l+p+u+d==len(usuario["clave"])):
        print("Nivel de Seguridad de la Clave Fuerte")
        usuario["clave"] =  hashlib.md5(usuario["clave"].encode())
        print("Usuario registrado con exito")
    elif (l>=1 and u>=1 and p>=2 and d>=2 and l+p+u+d==len(usuario["clave"])):
        print("Nivel de Seguridad de la Clave Medio")
        usuario["clave"] =  hashlib.md5(usuario["clave"].encode())
        print("Usuario registrado con exito")
    elif (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(usuario["clave"])):
        print("Nivel de Seguridad de la Clave Bajo")
        usuario["clave"] =  hashlib.md5(usuario["clave"].encode())
        print("Usuario registrado con exito")
    else:
        print("La Clave de Acceso Segura no es segura")
  elif opcionDeSesion == 2:
    if 'nombre' and 'clave' in usuario:
      nombre = input("Usuario: ")
      clave = hashlib.md5(input("Clave: ").encode())
      if(nombre == usuario["nombre"] and clave.hexdigest() == usuario["clave"].hexdigest()):
        banderaDeSesion = True
        bandera = "s"
      else: 
        print("Clave o Usuario invalido")
    else:
      print("No ha registrado un usuario")
  elif opcionDeSesion == 3:
    banderaDeSesion = True
    bandera = "n"
  else:
    print('Opcion Invalidad')
while bandera == "s":
  # Menu de Opciones
  print(f"¡Hola!, Bienvenido {usuario['nombre']} ")
  print(menu)
  op = int(input())  # Guardar opcion
  if op == 1:
    # Guardar cliente
    cliente["ci"] = input("Cedula de Identidad: ")
    cliente["nombre"] = input("Nombre: ")
    cliente["sexo"] = input("Sexo(M/F): ").upper()
    cliente["fechaDeNacimiento"] = input("Fecha de Nacimiento(DD/MM/YYYY): ")
    cliente["direccion"] = input("Dirección: ")
    cliente["tlf"] = input("Tlf: ")
    cliente["correo"] = input("Correo: ")
    cliente["edad"] = 2023 - int(cliente["fechaDeNacimiento"][-4:])
    clientes.append(cliente)
    cliente = {}
  elif op == 2:
    # Eliminar cliente
    bool = False
    cedula = input("Ingrese la cedula del cliente a eliminar: ")
    for item in clientes:
      if item["ci"] == cedula:
        print(f"El Cliente {item['nombre']} a sido eliminado")
        clientes.remove(item)
        bool = True
    if bool == False:
      print("Cliente no encontrado o cedula invalidad")
  elif op == 3:
    booleno = False
    cedula = input("Ingrese la cedula del a mostrar: ")
    print("Cliente")
    for item in clientes:
      if item["ci"] == cedula:
        print(f"""
        CI: {item['ci']}
        Nombre: {item['nombre']}
        Sexo(M/F): {item['sexo']}
        Edad: {item['edad']}
        Fecha de Nacimiento(DD/MM/YYYY): {item['fechaDeNacimiento']}
        Dirección: {item['direccion']}
        Correo: {item['correo']}
        Tlf: {item['tlf']}""")
        booleno = True
    if booleno == False:
      print("Cliente no encontrado o cedula invalidad")
  elif op == 4:
    print("Clientes")
    for item in clientes:
      print(f"""
        CI: {item['ci']}
        Nombre: {item['nombre']}
        Sexo: {item['sexo']}
        Edad: {item['edad']}
        Fecha de Nacimiento: {item['fechaDeNacimiento']}
        Dirección: {item['direccion']}
        Correo: {item['correo']}
        Tlf: {item['tlf']}""")
  elif op == 5:
    print("Clientes de tercera edad o preferente")
    for item in clientes:
      if (item["sexo"] == "F"
          and item['edad'] >= 55) or (item["sexo"] == "M"
                                      and item['edad'] >= 60):
        print(f"""
        CI: {item['ci']}
        Nombre: {item['nombre']}
        Sexo: {item['sexo']}
        Edad: {item['edad']}""")
  elif op == 6:
    bandera = "n"
  else:
    print('Opcion Invalidad')
