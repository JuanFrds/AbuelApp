from BACK_END.voluntario import Voluntario  # IMPORT DE LA CLASE VOLUNTARIO
from UI import funciones


# PIDE LOS DATOS PARA EL REGISTRO Y LO RETORNA EN UNA LISTA
def Registro():
    usr = input('Ingrese un nombre de usuario:')
    if Voluntario.verificar_usuarioDisponible(usr):
        contra = funciones.ingresoContra()
        nombre = funciones.verificar_nombreApellido('nombre')
        apellido = funciones.verificar_nombreApellido('apellido')
        celular = funciones.verificar_celular()
        direccion = funciones.verificarDireccion()
        sexo = funciones.elegir_sexo()
    else:
        print('Este nombre de usuario esta ocupado, elija otro.')
        return Registro()
    lista_usr = [usr, contra, nombre, apellido, celular, direccion, sexo]
    return lista_usr


# VE LOS DATOS DEL VOLUNTARIO
def verMiPerfil(voluntario):
    print('\nSus datos son los siguientes:\n')
    voluntario.mostrarDatos()
    continuar = input('\nOprima cualquier tecla para continuar...')


# MODIFICA LOS DATOS QUE QUIERA EL VOLUNTARIO
def modificarPerfil(voluntario):
    resp = ''
    while resp != '5':
        print('Selecione que datos desea modificar:')
        print(
            'Opción 1:\tNombre\n' +
            'Opción 2:\tApellido\n' +
            'Opción 3:\tCelular\n' +
            'Opción 4:\tDirección\n' +
            'Opción 5:\tAtras'
        )
        resp = input()
        if resp == '1':
            nombre = funciones.verificar_nombreApellido('Nombre')
            voluntario.nombre = nombre
            if funciones.menuConfirmacion('¿Seguro quiere modificar su nombre?'):
                voluntario.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombreApellido('Apellido')
            voluntario.apellido = apellido
            if funciones.menuConfirmacion('¿Seguro quiere modificar su apellido?'):
                voluntario.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            voluntario.celular = celular
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                voluntario.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificarDireccion()
            voluntario.direccion = direccion
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                voluntario.guardar_cambios()
        elif resp == '5':
            print('Saliendo...')
        else:
            print('Tecla incorrecta.')


# RECARGA VERIFICANDO SI ALGUN ABUELO LE HA SOLICITADO AYUDA
def recargar(voluntario):
    voluntario.actualizarNotificacion()
    voluntario.ayudaCompletadaORechazada()
    seguir = input('\nOprima cualquiera tecla para continuar...')


# ELIMINA EL USUARIO DE LA BASE DE DATOS
def eliminarUsuario(voluntario):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        voluntario.eliminarme()


# MUESTRA POR PANTALLA SI ESTA DISPONIBLE
def mensajeDisponibilidad(voluntario):
    if voluntario.mostrarDisponibilidad() == 'Disponible':
        return '*Su estado es: Disponible. Podria recibir peticiones de ayuda.'
    else:
        return '*Su estado es: No disponible. Cambielo si quiere recibir peticiones de ayuda'


# CAMBIA LA DISPONIBILIDAD DEL USUARIO
def cambiarDisponibilidad(voluntario):
    voluntario.cambiarDisponibilidad()
    print(f'Su disponibilidad cambio a: {voluntario.mostrarDisponibilidad()}')
    continuar = input('Oprima cualquier tecla para continuar...')
