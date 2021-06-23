from typing import SupportsRound
from requests.adapters import Response
from BACK_END.abuelo import Abuelo  # IMPORT DE LA CLASE ABUELO
from UI import funciones  # IMPORT DE FUNCIONES
import threading

def Registro():
    usr = funciones.verificar_usuario()
    if(Abuelo.verificar_usuarioDisponible(usr)):
        contra = funciones.ingresoContra()
        nombre = funciones.verificar_nombreApellido('nombre')
        apellido = funciones.verificar_nombreApellido('apellido')
        celular = funciones.verificar_celular()
        direccion = funciones.verificarDireccion()
        sexo =funciones.elegir_sexo()
    else:
        print('Este nombre de usuario esta ocupado, elija otro.')
        Registro()
    lista_usr = [usr,contra,nombre,apellido,celular,direccion,sexo]
    return lista_usr

def verMiPerfil(abuelo):
    print('\nSus datos son los siguientes:')
    abuelo.mostrarDatos()
    continuar = input('\nOprima cualquier tecla para continuar...')

def modificarPerfil(abuelo):
    resp = ''
    while resp != '5':
        print('Selecione que datos desea modificar:')
        print(
            'Opción 1:\tNombre\n'+
            'Opción 2:\tApellido\n'+
            'Opción 3:\tCelular\n'+
            'Opción 4:\tDirección\n'+
            'Opción 5:\tAtras'
        )
        resp = input()
        if resp == '1':
            nombre = funciones.verificar_nombreApellido('Nombre')
            abuelo.nombre = nombre
            if funciones.menuConfirmacion('¿Seguro quiere modificar su nombre?'):
                abuelo.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombreApellido('Apellido')
            abuelo.apellido = apellido
            if funciones.menuConfirmacion('¿Seguro quiere modificar su apellido?'):
                abuelo.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            abuelo.celular = celular
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                abuelo.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificarDireccion()
            abuelo.direccion = direccion
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                abuelo.guardar_cambios()
        elif resp == '5':
            print('Saliendo...')
        else:
            print('Tecla incorrecta.')

def solicitarAyuda(abuelo):
    list = abuelo.lista_volutariosDisponibles()
    n = 0
    if len(list) > 0:
        print('   Usuario\tDirección')
        for volunt in list:
            n = n + 1
            print(f'{n}. {volunt[0]}\t{volunt[1]}')
        resp = int(input('Elija un usuario de la lista de voluntarios disponibles: '))
        abuelo.pedirAyuda((list[resp-1][0]))
        print('Cuando el voluntario responda su peticion se le avisara.')
        segundoPlano = threading.Thread(target=notificacion,args=('sigue',abuelo))
        segundoPlano.start()
        # print('Esperando respuest...')
        # respAyuda = 'sigue'
        # while(respAyuda == 'sigue'):
        #     respAyuda = abuelo.actualizarPedido()
        #     if respAyuda == 'aceptado':
        #         print('Guarde los datos para que pueda comunicarse con el voluntario')
        #         salir = input('Oprima cualquier tecla para salir:')
        #         abuelo.ayudaCompletadaORechazada()
        #     elif respAyuda == 'rechazado':
        #         print('Vuelva a pedir ayuda y elija a otro usuario o intente mas tarde')
        #         abuelo.ayudaCompletadaORechazada()
    else:
        print('No hay voluntarios disponibles, intente mas tarde.')
            
def eliminarUsuario(abuelo):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        abuelo.eliminarme()

def notificacion(msj, abuelo):
    while(msj == 'sigue'):
        msj = abuelo.actualizarPedido()
        if msj == 'aceptado':
            print('\nGuarde los datos para que pueda comunicarse con el voluntario')
            continuar = input('Oprima cualquier tecla para salir:')
            abuelo.ayudaCompletadaORechazada()
        elif msj == 'rechazado':
            print('\nVuelva a pedir ayuda y elija a otro usuario o intente mas tarde')
            continuar = input('Oprima cualquier tecla para continuar...')
            abuelo.ayudaCompletadaORechazada()