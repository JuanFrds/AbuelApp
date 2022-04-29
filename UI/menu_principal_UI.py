from BACK_END.abuelo import Abuelo
from BACK_END.voluntario import Voluntario
from UI import menu_abuelo_UI
from UI import menu_voluntario_UI
from UI import voluntario_UI
from UI import abuelo_UI
import getpass
import os
import time


class MenuPrincipal:

    def __init__(self):
        self.opcion = 0

    def imprimirMenu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3}

        while self.opcion != '3':
            os.system('clear')
            print("=== BIENVENIDO A ABUELAPP ===")
            print("Opción 1:\t INGRESAR")
            print("Opción 2:\t REGISTRARSE")
            # print("Opción 3:\t ")
            print("Opción 3:\t SALIR")

            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if 0 < int(self.opcion) <= 4:
                    os.system('clear')
                    function = opciones[int(self.opcion)]
                    function()
                    
    # INICIO DE SESION
    def opcion1(self):
        print('Como quiere ingresar:')
        print(
            'Opcion 1:\tComo abuelo\n' +
            'Opcion 2:\tComo voluntario\n' +
            'Opcion 3:\tAtras')
        resp = input('\nSeleccione opción: ')

        # PIDE EL USUARIO Y CONTRASEÑA Y VERIFICA QUE COINCIDAN PARA INICIAR SESIÓN
        if resp == '1':
            os.system('clear')
            print('Ingresar como abuelo.')
            usuario = input('\nIngrese su usuario: ')
            contra = getpass.getpass('\nIngrese su contraseña: ')
            if Abuelo.verificar_login(usuario, contra):
                menuAbuelo = menu_abuelo_UI.MenuAbuelo(usuario)
                menuAbuelo.imprimirMenu()
            else:
                os.system('clear')
                print('Usuario o contraseña incorrecta.')
                time.sleep(1)
                os.system('clear')
                return self.opcion1()
        elif resp == '2':
            os.system('clear')
            print('Ingresar como voluntario.')
            usuario = input('\nIngrese su usuario: ')
            contra = getpass.getpass('\nIngrese su contraseña: ')
            if Voluntario.verificar_login(usuario, contra):
                menuVoluntario = menu_voluntario_UI.MenuVoluntario(usuario)
                menuVoluntario.imprimirMenu()
            else:
                os.system('clear')
                print('Usuario o contraseña incorrecta.')
                time.sleep(1)
                os.system('clear')
                return self.opcion1()
        elif resp == '3':
            pass
        else:
            # print('\nOpción incorrecta')
            os.system('clear')
            return self.opcion1()

    # REGISTRO
    def opcion2(self):
        print('Como quiere registrarse:')
        print(
            'Opcion 1:\tComo abuelo\n' +
            'Opcion 2:\tComo voluntario\n'
            'Opcion 3:\tAtras'
        )
        resp = input('\nSeleccione opción: ')
        # MEDIANTE UNA LISTA RETORNADA CREA UN OBJETO Y SUBE LOS DATOS A LA BASE DE DATOS
        if resp == '1':
            lista = abuelo_UI.Registro()
            abuelo = Abuelo(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
            abuelo.resgistrarse()
            abuelo = None
            menuAbuelo = menu_abuelo_UI.MenuAbuelo(lista[0])
            menuAbuelo.imprimirMenu()
        elif resp == '2':
            lista = voluntario_UI.Registro()
            voluntario = Voluntario(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
            voluntario.resgistrarse()
            voluntario = None
            menuVoluntario = menu_voluntario_UI.MenuVoluntario(lista[0])
            menuVoluntario.imprimirMenu()
        elif resp == '3':
            pass
        else:
            os.system('clear')
            return self.opcion2()

    def opcion3(self):
        print("GRACIAS POR USAR ABUELAPP")
        time.sleep(1)
        self.opcion = '3'
