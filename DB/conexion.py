import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='mysqlutn',
                db='AbuelApp'
            )
        except Error as ex:
            print("Error al intentar conexión: {0}", format(ex))

    def recuperarLista(self, sentencia):
        if not self.conexion.is_connected(): self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()

    def recuperarRegistro(self, sentencia):
        if not self.conexion.is_connected(): self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()

    def insertarOActualizar(self, sentencia):
        if not self.conexion.is_connected(): self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            self.conexion.commit()
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()

    # def listarPersonas(self):
    #     if self.conexion.is_connected():
    #         try:
    #             cursor = self.conexion.cursor()
    #             cursor.execute("SELECT * FROM persona ORDER BY nombre ASC")
    #             resultados = cursor.fetchall()
    #             return resultados
    #         except Error as ex:
    #             print("Error al intentar la conexión: {0}", format(ex))
    #         finally:
    #             if self.conexion.is_connected():
    #                 self.conexion.close()
    #
    # def registrarPersona(self, persona):
    #     if self.conexion.is_connected():
    #         try:
    #             cursor = self.conexion.cursor()
    #             sql = "INSERT INTO persona (nombre, apellido, direccion, sexo) VALUES ({0},'{1}',{2});"
    #             cursor.execute(sql.format(persona[0], persona[1], persona[2]))
    #             self.conexion.commit()
    #             print("¡Persona registrada!\n")
    #         except Error as ex:
    #             print("Error al intentar la conexión: {0}", format(ex))
    #         finally:
    #             if self.conexion.is_connected():
    #                 self.conexion.close()
    #
    # def eliminarPersona(self, codigo_persona_eliminar):
    #     if self.conexion.is_connected():
    #         try:
    #             cursor = self.conexion.cursor()
    #             sql = "DELETE FROM persona WHERE codigo = {0};"
    #             cursor.execute(sql.format(codigo_persona_eliminar))
    #             self.conexion.commit()
    #             print("¡Persona eliminada!\n")
    #         except Error as ex:
    #             print("Error al intentar la conexión: {0}", format(ex))
    #         finally:
    #             if self.conexion.is_connected():
    #                 self.conexion.close()
    #
    # def actualizardatos_persona(self, persona):
    #     if self.conexion.is_connected():
    #         try:
    #             cursor = self.conexion.cursor()
    #             sql = "UPDATE persona SET nombre='{0}', creditos={1} WHERE codigo={2};"
    #             cursor.execute(sql.format(persona[1], persona[2], persona[0]))
    #             self.conexion.commit()
    #             print("¡Datos de la persona actualizados!\n")
    #         except Error as ex:
    #             print("Error al intentar la conexión: {0}", format(ex))
    #         finally:
    #             if self.conexion.is_connected():
    #                 self.conexion.close()
