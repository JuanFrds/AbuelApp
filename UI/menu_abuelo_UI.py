from UI import funciones
from UI import abuelo_UI


class MenuAbuelo:

    def __init__(self):
        pass

    def imprimirMenu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4, 5: self.opcion5,
                    6: self.opcion6, 7: self.opcion7}

        opcion = 0

        while opcion != '7':
            funciones.limpiarConsola()
            print("\n=== ABUELO =======================")
            print("Opción 1:\t Listar")
            print("Opción 2:\t Cargar nuevo")
            print("Opción 3:\t Modificar perfil")
            print("Opción 4:\t Ver detalles de abuelo")
            print("Opción 5:\t Eliminar")
            print("Opción 6:\t (EN CONSTRUCCION) Solicitar ayuda)")
            print("Opción 7:\t REGRESAR AL MENU PRINCIPAL")
            opcion = input("\nSeleccione opción: ")

            if opcion.isnumeric():
                if int(opcion) > 0 & int(opcion) <= 6:
                    function = opciones[int(opcion)]
                    function()

    def opcion1(self):
        abuelo_UI.pantallaListar()

    def opcion2(self):
        abuelo_UI.pantallaAlta()

    def opcion3(self):
        abuelo_UI.pantallaModificar()

    def opcion4(self):
        abuelo_UI.pantallaDetalle()

    def opcion5(self):
        abuelo_UI.pantallaEliminar()

    def opcion6(self):
        print("OPCION EN CONSTRUCCION")

    def opcion7(self):
        print("Regresando al menu principal")
