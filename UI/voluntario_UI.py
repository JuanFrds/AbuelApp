from BACK_END.voluntario import Voluntario  # IMPORT DE LA CLASE VOLUNTARIO
from UI import funciones


# UI PARA INGRESAR NUEVOS VOLUNTARIOS
def pantallaAlta():
    funciones.limpiarConsola()
    funciones.menuConfirmacion("¿Desea cargar un nuevo voluntario?")

    print("\n-----ALTA DE VOLUNTARIO-----")

    # CREACION DE NUEVO OBJETO DE VOLUNTARIO PARA PROCEDER CON LA CARGA DE DATOS
    unVoluntario = Voluntario()

    # CARGA DE NOMBRE
    unVoluntario.nombre = funciones.verificar_nombreApellido("nombre")

    # CARGA DE APELLIDO
    unVoluntario.apellido = funciones.verificar_nombreApellido("apellido")

    # CARGA DE DIRECCION
    unVoluntario.direccion = funciones.elegir_direccion()

    # CARGA DE SEXO
    unVoluntario.sexo = funciones.elegir_sexo()

    # UNA VEZ QUE PASA TODAS LAS COMPROBACIONES SE PROCEDE A GUARDAR EL VOLUNTARIO
    unVoluntario.guardar_nuevo()


def pantallaDetalle():
    funciones.limpiarConsola()
    print("-----DETALLE DE VOLUNTARIO-----\n")

    codigoCorrecto = False

    while not codigoCorrecto:
        idvoluntario = input("Ingrese ID de voluntario: ")
        if idvoluntario.isnumeric():
            codigoCorrecto = True
            idvoluntario = int(idvoluntario)
        else:
            print("Código incorrecto")

    unVoluntario = Voluntario.cargar_voluntario(idvoluntario)

    if unVoluntario is not None:
        print("ID: ", unVoluntario.id)
        print("Nombre : ", unVoluntario.nombre)
        print("Apellido: ", unVoluntario.apellido)
        print("Direccion: ", unVoluntario.direccion)
        print("Sexo: ", unVoluntario.sexo)
    else:
        print("No se encontró voluntario")

    input("\nPresione ENTER para continuar")


def pantallaListar():
    funciones.limpiarConsola()

    listar_voluntarios = Voluntario.listar_voluntarios()

    if listar_voluntarios is not None:
        print("ID", "\t", "Nombre", "\t", "Apellido")
        for unVoluntario in listar_voluntarios:
            print(unVoluntario.id, "\t", unVoluntario.nombre, "\t", unVoluntario.apellido)

    else:
        print("No existen registros")
        input("Presione ENTER para continuar")


def pantallaModificar():
    funciones.limpiarConsola()

    unVoluntario = None

    def editar_voluntario():

        # EDITAR NOMBRE
        print("Nombre : ", unVoluntario.nombre)
        if funciones.menuConfirmacion("¿Desea editar el nombre?"):
            unVoluntario.nombre = funciones.verificar_nombreApellido("nuevo nombre: ")

        # EDITAR APELLIDO
        print("Apellido actual: ", unVoluntario.apellido)
        if funciones.menuConfirmacion("¿Desea editar el apellido?"):
            unVoluntario.apellido = funciones.verificar_nombreApellido("nuevo apellido: ")

        # EDITAR DIRECCION
        print("Dirección actual: ", unVoluntario.direccion)
        if funciones.menuConfirmacion("¿Desea editar la dirección?"):
            unVoluntario.direccion = funciones.elegir_direccion()

        # EDITAR SEXO
        print("Sexo actual: ", unVoluntario.sexo)
        if funciones.menuConfirmacion("¿Desea editar el sexo?"):
            unVoluntario.sexo = funciones.elegir_sexo()

        # AL PASAR LAS VERIFICACIONES SE GUARDAN LOS CAMBIOS
        unVoluntario.guardar_cambios()

    print("MODIFICACIÓN DE VOLUNTARIO")
    codigoCorrecto = False
    while not codigoCorrecto:
        funciones.limpiarConsola()
        idvoluntario = input("Ingrese ID de VOLUNTARIO: ")
        if idvoluntario.isnumeric():
            codigoCorrecto = True
            idvoluntario = int(idvoluntario)
        else:
            print("ID de voluntario debe ser numérico")

    unVoluntario = Voluntario.cargar_voluntario(idvoluntario)

    if unVoluntario is not None:
        editar_voluntario()
    else:
        print("No se encontró voluntario")
    input("Presione ENTER para continuar")


def pantallaEliminar():
    funciones.limpiarConsola()

    idvoluntario = int(input("Ingrese id del voluntario que desea eliminar: "))

    if idvoluntario is not None:
        if funciones.menuConfirmacion("¿Está seguro que desea eliminar al voluntario #{}".format(idvoluntario)):
            Voluntario.eliminar_voluntario(idvoluntario)
            print("¡Voluntario #", idvoluntario, " eliminado!")
        else:
            print("Cancelado por el usuario")
    else:
        print("ERROR")
