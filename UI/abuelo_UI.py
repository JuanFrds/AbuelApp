from typing import SupportsRound
from requests.adapters import Response
from BACK_END.abuelo import Abuelo  # IMPORT DE LA CLASE ABUELO
from UI import funciones  # IMPORT DE FUNCIONES

def Registro():
    usr = input('Ingrese un nombre de usuario:')
    if(Abuelo.verificar_usuarioDisponible(usr)):
        contra = funciones.ingresoContra()
        nombre = funciones.verificar_nombreApellido('nombre')
        apellido = funciones.verificar_nombreApellido('apellido')
        celular = input('Ingrese un numero de celular:')
        direccion = funciones.verificarDireccion()
        sexo =funciones.elegir_sexo()
    else:
        print('Este nombre de usuario esta ocupado, elija otro.')
        Registro()
    lista_usr = [usr,contra,nombre,apellido,celular,direccion,sexo]
    return lista_usr

def verMiPerfil(abuelo):
    print('\nSus datos son los siguientes:')
    abuelo.mostrarDatos()
    continuar = input('\nOprima cualquier tecla para continuar...')

def modificarPerfil(abuelo):
    resp = ''
    while resp != '6':
        print('Selecione que datos desea modificar:')
        print(
            'Opción 1:\tNombre\n'+
            'Opción 2:\tApellido\n'+
            'Opción 3:\tCelular\n'+
            'Opción 4:\tTelefono\n'+
            'Opción 5:\tDirección\n'+
            'Opción 6:\tAtras'
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
            celular = input('Ingrese un numero de celular:')
            abuelo.celular = celular
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                abuelo.guardar_cambios()
        elif resp == '4':
            telefono = input('Ingrese un numero de telefono:')
            abuelo.tel = telefono
            if funciones.menuConfirmacion('¿Seguro quiere modificar su telefono?'):
                abuelo.guardar_cambios()
        elif resp == '5':
            direccion = funciones.verificarDireccion()
            abuelo.direccion = direccion
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                abuelo.guardar_cambios()
        elif resp == '6':
            print('Saliendo...')
        else:
            print('Tecla incorrecta.')

def solicitarAyuda(abuelo):
    list = abuelo.lista_volutariosDisponibles()
    n = 0
    if len(list) > 0:
        print('   Usuario\tDirección')
        for volunt in list:
            n = n + 1
            print(f'{n}. {volunt[0]}\t{volunt[1]}')
        resp = int(input('Elija un usuario de la lista de voluntarios disponibles: '))
        abuelo.pedirAyuda((list[resp-1][0]))
        print('Esperando respuest...')
        respAyuda = 'sigue'
        while(respAyuda == 'sigue'):
            respAyuda = abuelo.actualizarPedido()
            if respAyuda == 'aceptado':
                print('Guarde los datos para que pueda comunicarse con el voluntario')
                salir = input('Oprima cualquier tecla para salir:')
                abuelo.ayudaCompletadaORechazada()
            elif respAyuda == 'rechazado':
                print('Vuelva a pedir ayuda y elija a otro usuario o intente mas tarde')
                abuelo.ayudaCompletadaORechazada()
    else:
        print('No hay voluntarios disponibles, intente mas tarde.')
            
def eliminarUsuario(abuelo):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        abuelo.eliminarme()

# UI PARA INGRESAR NUEVOS ABUELOS
# def pantallaAlta():
#     funciones.limpiarConsola()
#     funciones.menuConfirmacion("¿Desea cargar un nuevo abuelo?")

#     print("\n-----ALTA DE ABUELO-----")

#     # CREACION DE NUEVO OBJETO DE ABUELO PARA PROCEDER CON LA CARGA DE DATOS
#     unAbuelo = Abuelo()

#     #  CARGA DE NOMBRE
#     unAbuelo.nombre = funciones.verificar_nombreApellido("nombre")

#     #  CARGA DE APELLIDO
#     unAbuelo.apellido = funciones.verificar_nombreApellido("apellido")

#     #  CARGA DE DIRECCION
#     unAbuelo.direccion = funciones.elegir_direccion()

#     #  CARGA DE SEXO
#     unAbuelo.sexo = funciones.elegir_sexo()

#     #  UNA VEZ QUE PASA TODAS LAS COMPROBACIONES SE PROCEDE A GUARDAR EL ABUELO
#     Abuelo.guardar_nuevo(unAbuelo)


# #  UI PARA VER DETALLES DE UN ABUELO
# def pantallaDetalle():
#     funciones.limpiarConsola()
#     print("-----DETALLE DE ABUELO-----\n")

#     codigoCorrecto = False

#     while not codigoCorrecto:
#         idabuelo = input("Ingrese ID de abuelo a buscar: ")
#         if idabuelo.isnumeric():
#             codigoCorrecto = True
#             idabuelo = int(idabuelo)
#         else:
#             print("Código incorrecto")

#     funciones.limpiarConsola()

#     unAbuelo = Abuelo().cargar_abuelo(idabuelo)

#     if unAbuelo is not None:
#         print("ID: ", unAbuelo.id)
#         print("Nombre : ", unAbuelo.nombre)
#         print("Apellido: ", unAbuelo.apellido)
#         print("Direccion: ", unAbuelo.direccion)
#         print("Sexo: ", unAbuelo.sexo)
#     else:
#         return None

#     input("\nPresione ENTER para continuar")


# #  UI PARA MOSTRAR UNA LISTA DE TODOS LOS ABUELOS
# def pantallaListar():
#     funciones.limpiarConsola()

#     listar_abuelos = Abuelo.listar_abuelos()

#     if listar_abuelos is not None:
#         print("ID", "\t", "Nombre", "\t", "Apellido")
#         for unAbuelo in listar_abuelos:
#             print(unAbuelo.id, "\t", unAbuelo.nombre, "\t", unAbuelo.apellido)

#     else:
#         print("No existen registros")
#         input("Presione ENTER para continuar")


# def pantallaModificar():
#     funciones.limpiarConsola()

#     unAbuelo = None

#     def editar_abuelo():

#         # EDITAR NOMBRE
#         print("Nombre actual: ", unAbuelo.nombre)
#         if funciones.menuConfirmacion("¿Desea editar el nombre?"):
#             unAbuelo.nombre = funciones.verificar_nombreApellido("nuevo nombre: ")

#         # EDITAR APELLIDO
#         print("Apellido actual: ", unAbuelo.apellido)
#         if funciones.menuConfirmacion("¿Desea editar el apellido?"):
#             unAbuelo.apellido = funciones.verificar_nombreApellido("nuevo apellido: ")

#         # EDITAR DIRECCION
#         print("Dirección actual: ", unAbuelo.direccion)
#         if funciones.menuConfirmacion("¿Desea editar la dirección?"):
#             unAbuelo.direccion = funciones.elegir_direccion()

#         # EDITAR SEXO
#         print("Sexo actual: ", unAbuelo.sexo)
#         if funciones.menuConfirmacion("¿Desea editar el sexo?"):
#             unAbuelo.sexo = funciones.elegir_sexo()

#         # SI PASA TODAS LAS VERIFICACIONES SE GUARDAN LOS CAMBIOS
#         unAbuelo.guardar_cambios()

#     print("-----MODIFICACIÓN DE ABUELO-----\n")
#     codigoCorrecto = False
#     while not codigoCorrecto:
#         idabuelo = input("Ingrese ID de ABUELO: ")
#         if idabuelo.isnumeric():
#             codigoCorrecto = True
#             idabuelo = int(idabuelo)
#         else:
#             print("ID de abuelo debe ser numérico")

#     unAbuelo = Abuelo.cargar_abuelo(idabuelo)
#     if unAbuelo is not None:
#         editar_abuelo()
#     else:
#         print("No se encontró abuelo")

#     input("\nPresione ENTER para continuar")


# #  UI PARA ELIMINAR UN ABUELO
# def pantallaEliminar():
#     funciones.limpiarConsola()

#     idabuelo = int(input("Ingrese id del abuelo que desea eliminar: "))

#     if idabuelo is not None:
#         if funciones.menuConfirmacion("¿Está seguro que desea eliminar al abuelo #{}".format(idabuelo)):
#             Abuelo.eliminar_abuelo(idabuelo)
#             print("¡Abuelo #", idabuelo, " eliminado!")
#         else:
#             print("Cancelado por el usuario")
#     else:
#         print("ERROR")
