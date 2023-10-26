import pymysql
#CONEXION BD RUDIMENTARIA PERO JALA
class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='isw'
        )
        self.cursor = self.connection.cursor()
        print("Conexion establecida exitosamente")
#AQUI YA ES UNA QUERY
    def select_user(self,name):
        sql = "SELECT * from usuario WHERE Nombre=" +"'"+ name+"'"
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone() 
            print("ID",user[0])
            print("Nombre",user[1])
            print("Telefono",user[2])
            print("E-mail",user[3])
            return user
        except Exception as e:
            return False
            raise

    def select_users(self):
        sql = "SELECT * from usuario"
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall() 
            return user
        except Exception as e:
            raise

    def delete_user(self,name):
        sql = "DELETE from usuario WHERE Nombre=" +"'"+ name+"'"
        try:
            self.cursor.execute(sql)
        except Exception as e:
            return False
            raise
          
#AQUI SE MANDA A LLAMAR
database = DataBase()
database.select_user("Usuario1")