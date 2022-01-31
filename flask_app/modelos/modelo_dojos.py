from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__( self, id, name, created_at, update_at ):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.update_at = update_at

    @classmethod
    def obtenerListaDojos( cls ):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL( 'dojos_ninjas' ).query_db( query )
        listaDojos = []
        for dojo in resultado:
            listaDojos.append( cls( dojo["id"], dojo["name"], dojo["created_at"], dojo["update_at"]) )
        return listaDojos

    @classmethod
    def obtenerListaConNinjas(cls, encontrarDojo):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, encontrarDojo )
        return resultado

    @classmethod
    def agregaDojo( cls, nuevoDojo ):
        query2 = "ALTER TABLE ninjas AUTO_INCREMENT = 1;"
        connectToMySQL( "dojos_ninjas" ).query_db( query2 )
        query = "INSERT INTO dojos(name, created_at, update_at) VALUES(%(name)s, %(created_at)s, %(update_at)s);"
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, nuevoDojo )
        return resultado

    @classmethod
    def obtenerDojo(cls, encontrarDojo):
        query = "SELECT * FROM dojos WHERE dojos.name = %(dojo_id)s"
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, encontrarDojo )
        return resultado