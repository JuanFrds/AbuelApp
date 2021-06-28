from math import atan2, radians, cos, sin, asin, sqrt, trunc
from geopy.format import LATIN1_DEGREE
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import getpass
import os
import bcrypt

# CREE UNA VARIABLE 'GLOBAL' PARA NO TENER QUE DECLARARLA EN CADA METODO
ok = False


def limpiarConsola():
    print('\n')


# CONFIRMA EL MENSAJE PASADO POR PARAMETRO
def menuConfirmacion(mensaje):
    opcion = input(mensaje + "\nPresione '1' para confirmar u otra tecla para cancelar.\n")

    while not opcion or opcion.isspace():
        print("ERROR. INTENTE NUEVAMENTE.")
        opcion = input("Presione '1' para confirmar u otra tecla para cancelar.\n")

    # UNA VEZ QUE TERMINA LA VERIFICACION, CASTEO OPCION A ENTERO PARA CONTINUAR
    if int(opcion) == 1:
        return True
    else:
        print("Cancelado por el usuario.")
        return False


# VERIFICA EL NOMBRE O APELLIDO
def verificar_nombreApellido(nombre_apellido):
    while not ok:
        nombre = input("\nIngrese {}: ".format(nombre_apellido)).title()

        # VERIFICAR LONGITUD
        while len(nombre) <= 0 or len(nombre) > 30:
            nombre = input(
                "{} demasiado corto o largo.\nVuelva a ingresarlo: ".format(nombre_apellido.capitalize())).title()

        # VERIFICAR QUE NO CONTENGA ESPACIOS VACIOS
        while nombre.isspace():
            nombre = input("{} no puede contener espacios vacíos.\nVuelva a ingresarlo: ".format(
                nombre_apellido.capitalize())).title()

        print("\nUsted ha ingresado ", nombre)

        if menuConfirmacion("¿Es correcto el nombre ingresado?"):
            return nombre


# DA OPCIONES PARA QUE EL USUARIO ELIJA EL SEXO
def elegir_sexo():
    lista_sexos = ["MASCULINO", "FEMENINO", "INDEFINIDO"]

    while not ok:
        try:
            limpiarConsola()
            print("\nSELECCIONE SU SEXO:")
            print("1: MASCULINO\n2: FEMENINO\n3: INDEFINIDO")
            opcion = int(input("\nIngrese el número correspondiente a su sexo: "))

            while opcion < 1 or opcion > 3:
                opcion = int(
                    input("\nOpción incorrecta.\nVuelva a ingresar el número correspondiente a su sexo: "))

            #  SE LE RESTA 1 A LA LISTA PARA QUE COINCIDA CON LO QUE INGRESA EL USUARIO
            sexo = lista_sexos[opcion - 1]

            print("\nEl sexo elegido es:", sexo)

            if menuConfirmacion("¿Es correcto el sexo ingresado?"):
                return sexo

        except ValueError:
            print("\nERROR. ESPACIO EN BLANCO\n")


# VERIFICA QUE EL USUARIO NO ESTE VACIO Y/O SOLO CON ESPACIOS
def verificar_usuario():
    usr = input('\nIngrese un nombre de usuario:')
    if usr == '' or usr.isspace():
        print('\nEl nombre de usuario no puede estar vacio. Intente de vuelta.')
        return verificar_usuario()
    else:
        return usr


# ESTA FORMULA CALCULA LA DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA MEDIANTE LA LATITUD Y LONGITUD
def haversine(latlon1, latlon2):
    R = 6372.8

    latD = radians(latlon2[0] - latlon1[0])
    lonD = radians(latlon2[1] - latlon1[1])

    lat1 = radians(latlon1[0])
    lat2 = radians(latlon2[0])

    a = sin(latD / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lonD / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    d = R * c

    return d


# RETORNA LA LATITUD Y LONGITUD DE LA DIRECCION INGRESADA
def latitudLongitud(direccion):
    geolocator = Nominatim(user_agent='AbuelApp')
    loc = geolocator.geocode(direccion)
    list = [loc.latitude, loc.longitude]
    return list


# VERIFICA QUE LA DIRECCION SEA CORRECTA
def verificarDireccion():
    try:
        geolocator = Nominatim(user_agent='AbuelApp')
        print('\n*Siga el siguiente formato: Calle y numero, Barrio (opcional), Localidad (opcional), Departamento, Provincia')
        direccion = input('Ingrese dirección: ')
        loc = geolocator.geocode(direccion)
        loc = loc.address
        return direccion
    except Exception as e:
        print('Dirección incorrecta. Verifique y vuelva a ingresarla.')
        return verificarDireccion()


# VERIFICA QUE LA CONTRASEÑA NO TENGA MENOS DE 8 CARACTERES
def analizar_contra(contra):
    contra = str(contra)
    if contra.isspace() or len(contra) < 8:
        return False
    else:
        return True


# PIDE LA CONTRASEÑA
def ingresoContra():
    contra = getpass.getpass('\nIngrese una contraseña:')
    if analizar_contra(contra):
        return contra
    else:
        print('La contraseña no puede tener menos de 8 caracteres ni tener solo espacios vacios. Intente de nuevo.')
        return ingresoContra()


# VERIFICA QUE EL CELULAR CONTENGA SOLO NUMEROS
def verificar_celular():
    cel = input('Ingrese un numero de celular:')
    if cel.isnumeric():
        return cel
    else:
        print('El celular solo puede contener numeros. Intente de nuevo.')
        return verificar_celular()

def hashearContra(contra):
    contraHash = bcrypt.hashpw(contra.encode('utf-8'),bcrypt.gensalt())
    return contraHash

def verificarContra(contra, contraMysql):
    verif = bcrypt.checkpw(contra.encode('utf-8'), contraMysql)
    return verif