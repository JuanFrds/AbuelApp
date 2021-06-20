from UI import menu_abuelo_UI
from UI import menu_voluntario_UI
from UI import funciones


class MenuPrincipal:

    def imprimirMenu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4}

        opcion = 0

        while opcion != '4':

            funciones.limpiarConsola()
            print("\n=== MENU PRINCIPAL ===")
            print("Opción 1:\t Abuelo")
            print("Opción 2:\t Voluntario")
            print("Opción 3:\t Ver pedidos de ayuda activos ")
            print("Opción 4:\t SALIR")

            opcion = input("\nSeleccione opción: ")

            if opcion.isnumeric():
                if 0 < int(opcion) <= 4:
                    function = opciones[int(opcion)]
                    function()

    # ABUELO
    def opcion1(self):
        unMenuAbuelo = menu_abuelo_UI.MenuAbuelo()
        unMenuAbuelo.imprimirMenu()

    # VOLUNTARIO
    def opcion2(self):
        unMenuVoluntario = menu_voluntario_UI.MenuVoluntario()
        unMenuVoluntario.imprimirMenu()

    # PEDIDOS DE AYUDA
    def opcion3(self):
        print("Pedidos de ayuda (EN CONSTRUCCION")

    # MENSAJE DE SALIDA
    def opcion4(self):
        print("\nGRACIAS POR USAR ABUELAPP")
        input("\nPRESIONE ENTER PARA CONTINUAR...")
