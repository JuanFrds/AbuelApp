from UI import funciones
from UI import voluntario_UI


class MenuVoluntario:

    def __init__(self):
        pass

    def imprimirMenu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4, 5: self.opcion5,
                    6: self.opcion6, 7: self.opcion7}

        opcion = 0

        while opcion != '7':
            funciones.limpiarConsola()
            print("\n=== VOLUNTARIO ===================")
            print("Opción 1: Listar")
            print("Opción 2: Cargar nuevo")
            print("Opción 3: Modificar perfil")
            print("Opción 4: Ver detalles de voluntario")
            print("Opción 5: Eliminar")
            print("Opción 6: (EN CONSTRUCCION) Postular ayuda")
            print("Opción 7: REGRESAR AL MENU PRINCIPAL")
            opcion = input("\nSeleccione opción: ")

            if opcion.isnumeric():
                if int(opcion) > 0 & int(opcion) <= 6:
                    function = opciones[int(opcion)]
                    function()

    def opcion1(self):
        voluntario_UI.pantallaListar()

    def opcion2(self):
        voluntario_UI.pantallaAlta()

    def opcion3(self):
        voluntario_UI.pantallaModificar()

    def opcion4(self):
        voluntario_UI.pantallaDetalle()

    def opcion5(self):
        voluntario_UI.pantallaEliminar()

    def opcion6(self):
        print("OPCION EN CONSTRUCCION")

    def opcion7(self):
        print("Regresando al menu principal")
