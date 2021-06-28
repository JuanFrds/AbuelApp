from UI import funciones
from UI import abuelo_UI
from BACK_END.abuelo import Abuelo


class MenuAbuelo:

    def __init__(self, usuario):
        self.abuelo = Abuelo.iniciar_sesion(usuario)
        self.opcion = 0

    def imprimirMenu(self):
        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4, 5: self.opcion5}

        while self.opcion != '5':
            funciones.limpiarConsola()
            print(f"\n=== {self.abuelo.usuario} =======================")
            print("Opción 1:\t Ver mi perfil")
            print("Opción 2:\t Modificar perfil")
            print("Opción 3:\t Solicitar ayuda")
            print("Opción 4:\t Eliminar usuario")
            print("Opción 5:\t Salir")
            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if int(self.opcion) > 0 & int(self.opcion) <= 5:
                    function = opciones[int(self.opcion)]
                    function()
                else:
                    print('\nOpción incorrecta')
            else:
                print('\nOpción incorrecta')

    def opcion1(self):
        abuelo_UI.verMiPerfil(self.abuelo)

    def opcion2(self):
        abuelo_UI.modificarPerfil(self.abuelo)

    def opcion3(self):
        abuelo_UI.solicitarAyuda(self.abuelo)

    def opcion4(self):
        abuelo_UI.eliminarUsuario(self.abuelo)
        self.opcion5()
        self.opcion = '5'

    def opcion5(self):
        print('Saliendo...')
