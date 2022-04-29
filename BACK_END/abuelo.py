from DB.conexion import DAO
from BACK_END.voluntario import Voluntario
from UI import funciones 

class Abuelo:

    def __init__(self, usuario, contra, nombre, apellido, tel, celular, direccion, sexo):
        self.usuario = usuario
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.celular = celular
        self.direccion = direccion
        self.sexo = sexo
        self.ayudante = None

    def iniciar_sesion(usuario):
        try:
            dao = DAO()
            sql = f'select contra, nombre, apellido, tel, celular, direccion, sexo from abuelo where usuario=\'{usuario}\';'
            lista = dao.recuperarRegistro(sql)
            return Abuelo(usuario,lista[0],lista[1],lista[2],lista[3],lista[4], lista[5], lista[6])
        except Exception as e:
            print(e)
    
    #  UI PARA INGRESAR NUEVOS ABUELOS
    def resgistrarse(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO abuelo (usuario, contra, nombre, apellido, tel, celular, direccion, sexo) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}');"
            sql = sql.format(self.usuario, self.contra, self.nombre, self.apellido, self.tel, self.celular, self.direccion, self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE abuelo SET contra = '{0}', nombre = '{1}', apellido = '{2}', tel = '{3}', celular = '{4}', direccion = '{5}', sexo = '{6}' WHERE usuario = '{7}';"
            sql = sql.format(self.contra, self.nombre, self.apellido, self.tel, self.celular, self.direccion, self.sexo, self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def mostrarDatos(self):
        print('Nombre:',self.nombre)
        print('Apellido:',self.apellido)
        print('Tel.:',self.tel)
        print('Celular:',self.celular)
        print('Dirección:',self.direccion)
        print('Sexo:',self.sexo)
    
    def eliminarme(self):
        try:
            dao = DAO()
            sql = "DELETE FROM abuelo WHERE usuario = '{0}'"
            sql = sql.format(self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def lista_volutariosDisponibles(self):
        miLatLong = funciones.latitudLongitud(self.direccion)
        l = Voluntario.lista_voluntariosDisponibles()
        listaVolDisp = []
        for usr in l:
            if (funciones.haversine(miLatLong, funciones.latitudLongitud(usr[1]))) <= 1:
                listaVolDisp = list(listaVolDisp) + [(usr)]
        return listaVolDisp

    def pedirAyuda(self,usr_voluntario):
        try:
            dao = DAO()
            sql = f"UPDATE voluntario SET peticionAyuda = '{self.usuario}' WHERE usuario = '{usr_voluntario}';"
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def mostrarDatosVoluntario(self, ayudante):
        try:
            dao = DAO()
            sql = f"SELECT nombre, apellido, celular, tel FROM voluntario WHERE usuario = '{ayudante}'"
            datos = dao.recuperarRegistro(sql)
            print(
                'Datos del voluntario para que pueda comunicarse:\n'
                'Nombre:',datos[0],'\n'
                'Apellido:',datos[1],'\n'
                'Celular:',datos[2],'\n'
                'Tel.:',datos[3],
                    )
        except Exception as e:
            print(e)

    def actualizarPedido(self):
        try:
            dao = DAO()
            sql = f"SELECT ayudante FROM abuelo WHERE usuario = '{self.usuario}';"
            ayudante = dao.recuperarRegistro(sql)
            if ayudante[0] != None and ayudante[0] != '0':
                self.mostrarDatosVoluntario(ayudante[0])
                return 'aceptado'
            elif ayudante[0] == '0':
                print('El voluntario a rechazado su pedido')
                return 'rechazado'
            else: return 'sigue'
        except Exception as e:
            print(e)
    
    def ayudaCompletadaORechazada(self):
        try:
            dato = 'NULL'
            dao = DAO()
            sql = "UPDATE abuelo SET ayudante = {0} WHERE usuario = '{1}';"
            sql = sql.format(str(dato),self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def verificar_login(usuario, contra):
        try:
            dao = DAO()
            sql = f"SELECT contra FROM abuelo WHERE usuario='{usuario}' AND contra='{contra}';"
            if dao.recuperarRegistro(sql):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            
    @staticmethod
    def verificar_usuarioDisponible(usuario):
        try:
            dao = DAO()
            sql = "SELECT usuario FROM abuelo;"
            lista_usr = dao.recuperarRegistro(sql)
            verif = True
            if lista_usr != None:
                for usr in lista_usr:
                    if usr == usuario:
                        verif = False
                        return verif
            return verif
        except Exception as e:
            print(e)
            