from DB.conexion import DAO


class Voluntario:

    def __init__(self, usuario, contra, nombre, apellido, tel, celular, direccion, sexo):
        self.usuario = usuario
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.celular = celular
        self.direccion = direccion
        self.sexo = sexo
        self.disponibilidad = 0  
        self.peticionAyuda = None

    def iniciar_sesion(usuario):
        try:
            dao = DAO()
            sql = f'select contra, nombre, apellido, tel, celular, direccion, sexo, disponibilidad from voluntario where usuario=\'{usuario}\';'
            lista = dao.recuperarRegistro(sql)
            return Voluntario(usuario,lista[0],lista[1],lista[2],lista[3],lista[4], lista[5], lista[6])
        except Exception as e:
            print(e)     

    def resgistrarse(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO voluntario (usuario, contra, nombre, apellido, tel, celular, direccion, sexo, disponibilidad) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','0');"
            sql = sql.format(self.usuario, self.contra, self.nombre, self.apellido, self.tel, self.celular, self.direccion, self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e) 

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE voluntario SET contra = '{0}', nombre = '{1}', apellido = '{2}', tel = '{3}', celular = '{4}', direccion = '{5}', sexo = '{6}' WHERE usuario = '{7}';"
            sql = sql.format(self.contra, self.nombre, self.apellido, self.tel, self.celular, self.direccion, self.sexo, self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def cambiarDisponibilidad(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            disp = dao.recuperarRegistro(f"select disponibilidad from voluntario where usuario = '{self.usuario}';")
            if disp[0] == 0:
                sql = f"UPDATE voluntario SET disponibilidad = 1 WHERE usuario = '{self.usuario}';"
            else:
                sql = f"UPDATE voluntario SET disponibilidad = 0 WHERE usuario = '{self.usuario}';"
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

    def mostrarDisponibilidad(self):
        try:
            dao = DAO()
            disp = dao.recuperarRegistro(f"select disponibilidad from voluntario where usuario = '{self.usuario}';")
            if disp[0] == 0:
                return 'No disponible' 
            else:
                return 'Disponible'
        except Exception as e:
            print(e)

    def eliminarme(self):
        try:
            dao = DAO()
            sql = "DELETE FROM voluntario WHERE usuario = '{0}';"
            sql = sql.format(self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def mostrarDatosAbuelo(self, abuelo):
        try:
            dao = DAO()
            sql = f"SELECT nombre, apellido, celular, tel FROM abuelo WHERE usuario = '{abuelo}';"
            datos = dao.recuperarRegistro(sql)
            print(
                'Datos del abuelo para que pueda comunicarse:\n'
                'Nombre:',datos[0],'\n'
                'Apellido:',datos[1],'\n'
                'Celular:',datos[2],'\n'
                'Tel.:',datos[3],
                    )
        except Exception as e:
            print(e)

    def actualizarNotificacion(self):
        try:
            dao = DAO()
            resp = ''
            sql = f"SELECT peticionAyuda FROM voluntario WHERE usuario = '{self.usuario}';"
            peticion = dao.recuperarRegistro(sql)
            if peticion[0] != None:
                print(f'El usuario {peticion[0]} solicita su ayuda')
                print('Opcion 1:\tAceptar\nOpcion 2:\tRechazar')
                resp = input()
                if resp == '1':
                    self.mostrarDatosAbuelo(peticion[0])
                    dao.insertarOActualizar(f'UPDATE abuelo SET ayudante = \'{self.usuario}\' WHERE usuario = \'{peticion[0]}\';')
                elif resp == '2':
                    dao.insertarOActualizar(f'UPDATE abuelo SET ayudante = \'0\' WHERE usuario = \'{peticion[0]}\';')
            else:
                print('No tiene ninguna petición de ayuda.')
        except Exception as e:
            print(e)
    
    def ayudaCompletadaORechazada(self):
        try:
            dato = 'NULL'
            dao = DAO()
            sql = "UPDATE voluntario SET peticionAyuda = {0} WHERE usuario = '{1}';"
            sql = sql.format(str(dato),self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def verificar_login(usuario, contra):
        try:
            dao = DAO()
            sql = f"SELECT contra FROM voluntario WHERE usuario='{usuario}' AND contra='{contra}';"
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
            sql = "SELECT usuario FROM voluntario;"
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

    @staticmethod
    def lista_voluntariosDisponibles():
        try:
            dao = DAO()
            sql = "SELECT usuario, direccion FROM voluntario WHERE disponibilidad = 1;"
            lista = dao.recuperarLista(sql)
            return lista
        except Exception as e:
            print(e)