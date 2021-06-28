import threading
from BACK_END.abuelo import Abuelo  # IMPORT DE LA CLASE ABUELO
from UI import funciones  # IMPORT DE FUNCIONES


# PIDE LOS DATOS PARA REGISTRAR UN ABUELO Y RETORNA UNA LISTA CON LOS DATOS
def Registro():
    usr = funciones.verificar_usuario()
    if Abuelo.verificar_usuarioDisponible(usr):
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


# MUESTRA LOS DATOS DEL ABUELO
def verMiPerfil(abuelo):
    print('\nSus datos son los siguientes:')
    abuelo.mostrarDatos()
    continuar = input('\nOprima cualquier tecla para continuar...')


# MODIFICA LOS DATOS QUE QUIERA CAMBIAR EL ABUELO
def modificarPerfil(abuelo):
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
            abuelo.nombre = nombre
            if funciones.menuConfirmacion('¿Seguro quiere modificar su nombre?'):
                abuelo.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombreApellido('Apellido')
            abuelo.apellido = apellido
            if funciones.menuConfirmacion('¿Seguro quiere modificar su apellido?'):
                abuelo.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            abuelo.celular = celular
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                abuelo.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificarDireccion()
            abuelo.direccion = direccion
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                abuelo.guardar_cambios()
        elif resp == '5':
            print('Saliendo...')
        else:
            print('Tecla incorrecta.')


# PIDE AYUDA A LOS VOLUNTARIOS DISPONIBLES QUE ESTEN CERCA
def solicitarAyuda(abuelo):
    list = abuelo.lista_volutariosDisponibles()
    n = 0
    if len(list) > 0:
        print('   Usuario\tDirección')
        for volunt in list:
            n = n + 1
            print(f'{n}. {volunt[0]}\t{volunt[1]}')
        resp = int(input('Elija un usuario de la lista de voluntarios disponibles: '))
        abuelo.pedirAyuda((list[resp - 1][0]))
        print('Cuando el voluntario responda su peticion se le avisara.')
        # CON THREAD HACE EL USO DE LOS HILOS PARA EJECUTAR ESE METODO DE FORMA PARALELA
        segundoPlano = threading.Thread(target=notificacion, args=('sigue', abuelo))
        segundoPlano.start()
    else:
        print('No hay voluntarios disponibles, intente mas tarde.')


# ELIMINA SU USUARIO DE LA BASE DE DATOS
def eliminarUsuario(abuelo):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        abuelo.eliminarme()


# ESTE METODO MEDIANTE UN BUCLE ACTUALIZA PARA VER SI RESPONDIO EL VOLUNTARIO
def notificacion(msj, abuelo):
    while msj == 'sigue':
        msj = abuelo.actualizarPedido()
        if msj == 'aceptado':
            print('\nGuarde los datos para que pueda comunicarse con el voluntario')
            continuar = input('Oprima cualquier tecla para salir:')
            abuelo.ayudaCompletadaORechazada()
        elif msj == 'rechazado':
            print('\nVuelva a pedir ayuda y elija a otro usuario o intente mas tarde')
            continuar = input('Oprima cualquier tecla para continuar...')
            abuelo.ayudaCompletadaORechazada()
