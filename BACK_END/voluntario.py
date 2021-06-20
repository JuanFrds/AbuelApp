from DB.conexion import DAO


class Voluntario:
    id = 0
    nombre = ""
    apellido = ""
    direccion = ""
    sexo = ""

    def __init__(self):
        pass

    def guardar_nuevo(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO voluntario (nombre, apellido, direccion, sexo) VALUES ('{0}','{1}','{2}','{3}');"
            sql = sql.format(self.nombre, self.apellido, self.direccion, self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE voluntario SET nombre = '{0}', apellido = '{1}', direccion = '{2}', sexo = '{3}' WHERE id = {4};"
            sql = sql.format(self.nombre, self.apellido, self.direccion, self.sexo, self.id)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def listar_voluntarios():
        # noinspection PyBroadException
        try:
            dao = DAO()
            resultados = dao.recuperarLista("SELECT id, nombre, apellido, direccion, sexo FROM voluntario ORDER BY id ASC")

            if len(resultados) > 0:
                lista_voluntarios = list()
                for fila in resultados:
                    un_voluntario = Voluntario()
                    un_voluntario.id = fila[0]
                    un_voluntario.nombre = fila[1]
                    un_voluntario.apellido = fila[2]
                    un_voluntario.direccion = fila[3]
                    un_voluntario.sexo = fila[4]
                    lista_voluntarios.append(un_voluntario)

                return lista_voluntarios
            else:
                return None

        except Exception as e:
            print(e)

    @staticmethod
    def cargar_voluntario(idvoluntario):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "SELECT * FROM voluntario WHERE id = {0}"
            sql = sql.format(idvoluntario)
            resultado = dao.recuperarRegistro(sql)

            if resultado is not None:
                un_voluntario = Voluntario()
                un_voluntario.id = resultado[0]
                un_voluntario.nombre = resultado[1]
                un_voluntario.apellido = resultado[2]
                un_voluntario.direccion = resultado[3]
                un_voluntario.sexo = resultado[4]
                return un_voluntario
            else:
                print("No se encuentra el voluntario con el ID ingresado")
                return None
        except Exception as e:
            print(e)

    @staticmethod
    def eliminar_voluntario(idvoluntario):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "DELETE FROM voluntario WHERE id={0}"
            sql = sql.format(idvoluntario)
            dao.insertarOActualizar(sql)

        except Exception as e:
            print(e)
