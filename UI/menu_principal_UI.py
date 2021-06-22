from BACK_END.abuelo import Abuelo
from BACK_END.voluntario import Voluntario
from UI import menu_abuelo_UI
from UI import menu_voluntario_UI
from UI import voluntario_UI
from UI import abuelo_UI


class MenuPrincipal:

    def imprimirMenu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4}

        opcion = 0

        while opcion != '4':
            print("\n=== BIENVENIDO A ABUELAPP ===")
            print("Opción 1:\t INGRESAR")
            print("Opción 2:\t REGISTRARSE")
            print("Opción 3:\t ")
            print("Opción 4:\t SALIR")

            opcion = input("\nSeleccione opción: ")

            if opcion.isnumeric():
                if 0 < int(opcion) <= 4:
                    function = opciones[int(opcion)]
                    function()

    # ABUELO
    def opcion1(self):
        print('Como quiere ingresar:')
        print(
            'Opcion 1:\tComo abuelo\n'+
            'Opcion 2:\tComo voluntario\n'+
            'Opcion 3:\tSalir')
        resp = input()

        if resp == '1':
            usuario = input('Ingrese su usuario: ')
            contra = input('Ingrese su contraseña: ')
            if Abuelo.verificar_login(usuario,contra):
                menuAbuelo = menu_abuelo_UI.MenuAbuelo(usuario)
                menuAbuelo.imprimirMenu()
            else: 
                print('Usuario o contraseña incorrecta')
        elif resp == '2':
            usuario = input('Ingrese su usuario: ')
            contra = input('Ingrese su contraseña: ')
            if Voluntario.verificar_login(usuario,contra):
                menuVoluntario = menu_voluntario_UI.MenuVoluntario(usuario)
                menuVoluntario.imprimirMenu()
            else: 
                print('Usuario o contraseña incorrecta')
        else:
            print('Volviendo al menu principal')

    # REGISTRO
    def opcion2(self):
        print('Como quiere registrarse:')
        print(
            'Opcion 1:\tComo abuelo\n'+
            'Opcion 2:\tComo voluntario\n'
            'Opcion 3:\tSalir'
            )
        resp = input()

        if resp == '1':
            lista = abuelo_UI.Registro()
            abuelo = Abuelo(lista[0],lista[1],lista[2],lista[3],None,lista[4],lista[5],lista[6])
            abuelo.resgistrarse()
            abuelo = None
            menuAbuelo = menu_abuelo_UI.MenuAbuelo(lista[0])
            menuAbuelo.imprimirMenu()
        elif resp == '2':
            lista = voluntario_UI.Registro()
            voluntario = Voluntario(lista[0],lista[1],lista[2],lista[3],None,lista[4],lista[5],lista[6])
            voluntario.resgistrarse()
            voluntario = None
            menuVoluntario = menu_voluntario_UI.MenuVoluntario(lista[0])
            menuVoluntario.imprimirMenu()
        else:
            print('Volviendo al menu principal')

    # PEDIDOS DE AYUDA
    def opcion3(self):
        pass
    # MENSAJE DE SALIDA
    def opcion4(self):
        print("\nGRACIAS POR USAR ABUELAPP")
        input("\nPRESIONE ENTER PARA CONTINUAR...")