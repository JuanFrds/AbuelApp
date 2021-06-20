from BACK_END.abuelo import Abuelo  # IMPORT DE LA CLASE ABUELO
from UI import funciones  # IMPORT DE FUNCIONES


# UI PARA INGRESAR NUEVOS ABUELOS
def pantallaAlta():
    funciones.limpiarConsola()
    funciones.menuConfirmacion("¿Desea cargar un nuevo abuelo?")

    print("\n-----ALTA DE ABUELO-----")

    # CREACION DE NUEVO OBJETO DE ABUELO PARA PROCEDER CON LA CARGA DE DATOS
    unAbuelo = Abuelo()

    #  CARGA DE NOMBRE
    unAbuelo.nombre = funciones.verificar_nombreApellido("nombre")

    #  CARGA DE APELLIDO
    unAbuelo.apellido = funciones.verificar_nombreApellido("apellido")

    #  CARGA DE DIRECCION
    unAbuelo.direccion = funciones.elegir_direccion()

    #  CARGA DE SEXO
    unAbuelo.sexo = funciones.elegir_sexo()

    #  UNA VEZ QUE PASA TODAS LAS COMPROBACIONES SE PROCEDE A GUARDAR EL ABUELO
    Abuelo.guardar_nuevo(unAbuelo)


#  UI PARA VER DETALLES DE UN ABUELO
def pantallaDetalle():
    funciones.limpiarConsola()
    print("-----DETALLE DE ABUELO-----\n")

    codigoCorrecto = False

    while not codigoCorrecto:
        idabuelo = input("Ingrese ID de abuelo a buscar: ")
        if idabuelo.isnumeric():
            codigoCorrecto = True
            idabuelo = int(idabuelo)
        else:
            print("Código incorrecto")

    funciones.limpiarConsola()

    unAbuelo = Abuelo().cargar_abuelo(idabuelo)

    if unAbuelo is not None:
        print("ID: ", unAbuelo.id)
        print("Nombre : ", unAbuelo.nombre)
        print("Apellido: ", unAbuelo.apellido)
        print("Direccion: ", unAbuelo.direccion)
        print("Sexo: ", unAbuelo.sexo)
    else:
        return None

    input("\nPresione ENTER para continuar")


#  UI PARA MOSTRAR UNA LISTA DE TODOS LOS ABUELOS
def pantallaListar():
    funciones.limpiarConsola()

    listar_abuelos = Abuelo.listar_abuelos()

    if listar_abuelos is not None:
        print("ID", "\t", "Nombre", "\t", "Apellido")
        for unAbuelo in listar_abuelos:
            print(unAbuelo.id, "\t", unAbuelo.nombre, "\t", unAbuelo.apellido)

    else:
        print("No existen registros")
        input("Presione ENTER para continuar")


def pantallaModificar():
    funciones.limpiarConsola()

    unAbuelo = None

    def editar_abuelo():

        # EDITAR NOMBRE
        print("Nombre actual: ", unAbuelo.nombre)
        if funciones.menuConfirmacion("¿Desea editar el nombre?"):
            unAbuelo.nombre = funciones.verificar_nombreApellido("nuevo nombre: ")

        # EDITAR APELLIDO
        print("Apellido actual: ", unAbuelo.apellido)
        if funciones.menuConfirmacion("¿Desea editar el apellido?"):
            unAbuelo.apellido = funciones.verificar_nombreApellido("nuevo apellido: ")

        # EDITAR DIRECCION
        print("Dirección actual: ", unAbuelo.direccion)
        if funciones.menuConfirmacion("¿Desea editar la dirección?"):
            unAbuelo.direccion = funciones.elegir_direccion()

        # EDITAR SEXO
        print("Sexo actual: ", unAbuelo.sexo)
        if funciones.menuConfirmacion("¿Desea editar el sexo?"):
            unAbuelo.sexo = funciones.elegir_sexo()

        # SI PASA TODAS LAS VERIFICACIONES SE GUARDAN LOS CAMBIOS
        unAbuelo.guardar_cambios()

    print("-----MODIFICACIÓN DE ABUELO-----\n")
    codigoCorrecto = False
    while not codigoCorrecto:
        idabuelo = input("Ingrese ID de ABUELO: ")
        if idabuelo.isnumeric():
            codigoCorrecto = True
            idabuelo = int(idabuelo)
        else:
            print("ID de abuelo debe ser numérico")

    unAbuelo = Abuelo.cargar_abuelo(idabuelo)
    if unAbuelo is not None:
        editar_abuelo()
    else:
        print("No se encontró abuelo")

    input("\nPresione ENTER para continuar")


#  UI PARA ELIMINAR UN ABUELO
def pantallaEliminar():
    funciones.limpiarConsola()

    idabuelo = int(input("Ingrese id del abuelo que desea eliminar: "))

    if idabuelo is not None:
        if funciones.menuConfirmacion("¿Está seguro que desea eliminar al abuelo #{}".format(idabuelo)):
            Abuelo.eliminar_abuelo(idabuelo)
            print("¡Abuelo #", idabuelo, " eliminado!")
        else:
            print("Cancelado por el usuario")
    else:
        print("ERROR")
