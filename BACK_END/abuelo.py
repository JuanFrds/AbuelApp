from DB.conexion import DAO


class Abuelo:
    id = 0
    nombre = ""
    apellido = ""
    direccion = ""
    sexo = ""

    def __init__(self):
        pass

    #  UI PARA INGRESAR NUEVOS ABUELOS
    def guardar_nuevo(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO abuelo (nombre, apellido, direccion, sexo) VALUES ('{0}','{1}','{2}','{3}');"
            sql = sql.format(self.nombre, self.apellido, self.direccion, self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE abuelo SET nombre = '{0}', apellido = '{1}', direccion = '{2}', sexo = '{3}' WHERE id = {4};"
            sql = sql.format(self.nombre, self.apellido, self.direccion, self.sexo, self.id)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def listar_abuelos():
        # noinspection PyBroadException
        try:
            dao = DAO()
            resultados = dao.recuperarLista("SELECT id, nombre, apellido, direccion, sexo FROM abuelo ORDER BY id ASC")

            if len(resultados) > 0:
                lista_abuelos = list()
                for fila in resultados:
                    un_abuelo = Abuelo()
                    un_abuelo.id = fila[0]
                    un_abuelo.nombre = fila[1]
                    un_abuelo.apellido = fila[2]
                    un_abuelo.direccion = fila[3]
                    un_abuelo.sexo = fila[4]
                    lista_abuelos.append(un_abuelo)

                return lista_abuelos
            else:
                return None

        except Exception as e:
            print(e)

    @staticmethod
    def cargar_abuelo(idabuelo):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "SELECT * FROM abuelo WHERE id = {0}"
            sql = sql.format(idabuelo)
            resultado = dao.recuperarRegistro(sql)

            if resultado is not None:
                un_abuelo = Abuelo()
                un_abuelo.id = resultado[0]
                un_abuelo.nombre = resultado[1]
                un_abuelo.apellido = resultado[2]
                un_abuelo.direccion = resultado[3]
                un_abuelo.sexo = resultado[4]
                return un_abuelo
            else:
                print("No se encuentra el abuelo con el ID ingresado")
                return None

        except Exception as e:
            print(e)

    @staticmethod
    def eliminar_abuelo(idabuelo):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "DELETE FROM abuelo WHERE id = {0}"
            sql = sql.format(idabuelo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)
