from math import atan2, radians, cos, sin, asin, sqrt, trunc
from geopy.format import LATIN1_DEGREE
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

# CREE UNA VARIABLE 'GLOBAL' PARA NO TENER QUE DECLARARLA EN CADA METODO
ok = False


def limpiarConsola():
    print('\n')


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
#Formula que calcula la distancia en KM entre 2 puntos en la tierra:
def haversine(latlon1,latlon2):
    R = 6372.8

    latD = radians(latlon2[0] - latlon1[0])
    lonD = radians(latlon2[1] - latlon1[1])

    lat1 = radians(latlon1[0])
    lat2 = radians(latlon2[0])

    a = sin(latD/2)**2 + cos(lat1) * cos(lat2) * sin(lonD/2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))

    d = R * c

    return d

def latitudLongitud(direccion):
    geolocator = Nominatim(user_agent='AbuelApp')
    loc = geolocator.geocode(direccion)
    list = [loc.latitude,loc.longitude]
    return list

def verificarDireccion():
    try:
        geolocator = Nominatim(user_agent='AbuelApp')
        direccion = input(
                '*Siga el siguiente formato: Calle y numero, Barrio (opcional), Localidad, Departamento, Provincia\n'
                'Ingrese dirección: '
                )
        loc = geolocator.geocode(direccion)
        if loc.address:
            return direccion
    except Exception as e:
        print('Dirección incorrecta. Verifique y vuelva a ingresarla.')
        verificarDireccion()

def verificar_contra(contra):
    contra = str(contra)
    if contra == '' or len(contra) < 8:
        return False
    else:
        return True
        

def ingresoContra():
    contra = str(input('Ingrese un contraseña:'))
    if verificar_contra(contra):
        return contra
    else:
        print('La contraseña no puede tener menos de 8 caracteres. Intente de nuevo.')
        ingresoContra()

