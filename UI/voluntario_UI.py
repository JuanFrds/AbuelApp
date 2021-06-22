from BACK_END.voluntario import Voluntario  # IMPORT DE LA CLASE VOLUNTARIO
from UI import funciones


# UI PARA INGRESAR NUEVOS VOLUNTARIOS
def Registro():
    usr = input('Ingrese un nombre de usuario:')
    if(Voluntario.verificar_usuarioDisponible(usr)):
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

def verMiPerfil(voluntario):
    print('\nSus datos son los siguientes:\n')
    voluntario.mostrarDatos()
    continuar = input('\nOprima cualquier tecla para continuar...')

def modificarPerfil(voluntario):
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
            voluntario.nombre = nombre
            if funciones.menuConfirmacion('¿Seguro quiere modificar su nombre?'):
                voluntario.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombreApellido('Apellido')
            voluntario.apellido = apellido
            if funciones.menuConfirmacion('¿Seguro quiere modificar su apellido?'):
                voluntario.guardar_cambios()
        elif resp == '3':
            celular = input('Ingrese un numero de celular:')
            voluntario.celular = celular
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                voluntario.guardar_cambios()
        elif resp == '4':
            telefono = input('Ingrese un numero de telefono:')
            voluntario.tel = telefono
            if funciones.menuConfirmacion('¿Seguro quiere modificar su telefono?'):
                voluntario.guardar_cambios()
        elif resp == '5':
            direccion = funciones.verificarDireccion()
            voluntario.direccion = direccion
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                voluntario.guardar_cambios()
        elif resp == '6':
            print('Saliendo...')
        else:
            print('Tecla incorrecta.')

def recargar(voluntario):
    voluntario.actualizarNotificacion()
    voluntario.ayudaCompletadaORechazada()
    seguir = input('\nOprima cualquiera tecla para continuar...')

def eliminarUsuario(voluntario):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        voluntario.eliminarme()

def mensajeDisponibilidad(voluntario):
    if voluntario.mostrarDisponibilidad() == 'Disponible':
        return '*Su estado es: Disponible. Podria recibir peticiones de ayuda.'
    else:
        return '*Su estado es: No disponible. Cambielo si quiere recibir peticiones de ayuda'

def cambiarDisponibilidad(voluntario):
    voluntario.cambiarDisponibilidad()
    print(f'Su disponibilidad cambio a: {voluntario.mostrarDisponibilidad()}')
    continuar = input('Oprima cualquier tecla para continuar...')

# def pantallaAlta():
#     funciones.limpiarConsola()
#     funciones.menuConfirmacion("¿Desea cargar un nuevo voluntario?")

#     print("\n-----ALTA DE VOLUNTARIO-----")

#     # CREACION DE NUEVO OBJETO DE VOLUNTARIO PARA PROCEDER CON LA CARGA DE DATOS
#     unVoluntario = Voluntario()

#     # CARGA DE NOMBRE
#     unVoluntario.nombre = funciones.verificar_nombreApellido("nombre")

#     # CARGA DE APELLIDO
#     unVoluntario.apellido = funciones.verificar_nombreApellido("apellido")

#     # CARGA DE DIRECCION
#     unVoluntario.direccion = funciones.elegir_direccion()

#     # CARGA DE SEXO
#     unVoluntario.sexo = funciones.elegir_sexo()

#     # UNA VEZ QUE PASA TODAS LAS COMPROBACIONES SE PROCEDE A GUARDAR EL VOLUNTARIO
#     unVoluntario.guardar_nuevo()


# def pantallaDetalle():
#     funciones.limpiarConsola()
#     print("-----DETALLE DE VOLUNTARIO-----\n")

#     codigoCorrecto = False

#     while not codigoCorrecto:
#         idvoluntario = input("Ingrese ID de voluntario: ")
#         if idvoluntario.isnumeric():
#             codigoCorrecto = True
#             idvoluntario = int(idvoluntario)
#         else:
#             print("Código incorrecto")

#     unVoluntario = Voluntario.cargar_voluntario(idvoluntario)

#     if unVoluntario is not None:
#         print("ID: ", unVoluntario.id)
#         print("Nombre : ", unVoluntario.nombre)
#         print("Apellido: ", unVoluntario.apellido)
#         print("Direccion: ", unVoluntario.direccion)
#         print("Sexo: ", unVoluntario.sexo)
#     else:
#         print("No se encontró voluntario")

#     input("\nPresione ENTER para continuar")


# def pantallaListar():
#     funciones.limpiarConsola()

#     listar_voluntarios = Voluntario.listar_voluntarios()

#     if listar_voluntarios is not None:
#         print("ID", "\t", "Nombre", "\t", "Apellido")
#         for unVoluntario in listar_voluntarios:
#             print(unVoluntario.id, "\t", unVoluntario.nombre, "\t", unVoluntario.apellido)

#     else:
#         print("No existen registros")
#         input("Presione ENTER para continuar")


# def pantallaModificar():
#     funciones.limpiarConsola()

#     unVoluntario = None

#     def editar_voluntario():

#         # EDITAR NOMBRE
#         print("Nombre : ", unVoluntario.nombre)
#         if funciones.menuConfirmacion("¿Desea editar el nombre?"):
#             unVoluntario.nombre = funciones.verificar_nombreApellido("nuevo nombre: ")

#         # EDITAR APELLIDO
#         print("Apellido actual: ", unVoluntario.apellido)
#         if funciones.menuConfirmacion("¿Desea editar el apellido?"):
#             unVoluntario.apellido = funciones.verificar_nombreApellido("nuevo apellido: ")

#         # EDITAR DIRECCION
#         print("Dirección actual: ", unVoluntario.direccion)
#         if funciones.menuConfirmacion("¿Desea editar la dirección?"):
#             unVoluntario.direccion = funciones.elegir_direccion()

#         # EDITAR SEXO
#         print("Sexo actual: ", unVoluntario.sexo)
#         if funciones.menuConfirmacion("¿Desea editar el sexo?"):
#             unVoluntario.sexo = funciones.elegir_sexo()

#         # AL PASAR LAS VERIFICACIONES SE GUARDAN LOS CAMBIOS
#         unVoluntario.guardar_cambios()

#     print("MODIFICACIÓN DE VOLUNTARIO")
#     codigoCorrecto = False
#     while not codigoCorrecto:
#         funciones.limpiarConsola()
#         idvoluntario = input("Ingrese ID de VOLUNTARIO: ")
#         if idvoluntario.isnumeric():
#             codigoCorrecto = True
#             idvoluntario = int(idvoluntario)
#         else:
#             print("ID de voluntario debe ser numérico")

#     unVoluntario = Voluntario.cargar_voluntario(idvoluntario)

#     if unVoluntario is not None:
#         editar_voluntario()
#     else:
#         print("No se encontró voluntario")
#     input("Presione ENTER para continuar")


# def pantallaEliminar():
#     funciones.limpiarConsola()

#     idvoluntario = int(input("Ingrese id del voluntario que desea eliminar: "))

#     if idvoluntario is not None:
#         if funciones.menuConfirmacion("¿Está seguro que desea eliminar al voluntario #{}".format(idvoluntario)):
#             Voluntario.eliminar_voluntario(idvoluntario)
#             print("¡Voluntario #", idvoluntario, " eliminado!")
#         else:
#             print("Cancelado por el usuario")
#     else:
#         print("ERROR")
