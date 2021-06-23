from urllib.request import install_opener
from UI import funciones
from UI import voluntario_UI
from BACK_END.voluntario import Voluntario



class MenuVoluntario:

    def __init__(self,usuario):
        self.voluntario = Voluntario.iniciar_sesion(usuario)
        self.opcion = 0

    def imprimirMenu(self):
        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4, 5: self.opcion5,
                    6: self.opcion6}

        while self.opcion != '6':
            funciones.limpiarConsola()
            print(f"\n==={self.voluntario.usuario}===================")
            print("Opción 1:\t Ver mi perfil")
            print("Opción 2:\t Modificar perfil")
            print("Opción 3:\t Cambiar disponibilidad")
            print("Opción 4:\t Recargar")
            print("Opción 5:\t Eliminar usuario")
            print("Opción 6:\t Salir\n")
            print(voluntario_UI.mensajeDisponibilidad(self.voluntario))
            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if int(self.opcion) > 0 & int(self.opcion) <= 6:
                    function = opciones[int(self.opcion)]
                    function()
                else:
                    print('\nOpción incorrecta')
            else: 
                print('\nOpción incorrecta')

    def opcion1(self):
        voluntario_UI.verMiPerfil(self.voluntario)

    def opcion2(self):
        voluntario_UI.modificarPerfil(self.voluntario)

    def opcion3(self):
        voluntario_UI.cambiarDisponibilidad(self.voluntario)

    def opcion4(self):
        voluntario_UI.recargar(self.voluntario)

    def opcion5(self):
        voluntario_UI.eliminarUsuario(self.voluntario)
        self.opcion6()
        self.opcion = '6'

    def opcion6(self):
        print('Saliendo...')