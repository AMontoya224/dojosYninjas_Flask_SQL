from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__( self, id, first_name, last_name, age, dojo_id, created_at, update_at ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojo_id = dojo_id
        self.created_at = created_at
        self.update_at = update_at
    
    @classmethod
    def agregaNinja( cls, nuevoNinja ):
        query2 = "ALTER TABLE ninjas AUTO_INCREMENT = 1;"
        connectToMySQL( "dojos_ninjas" ).query_db( query2 )
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, update_at) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, %(created_at)s, %(update_at)s);"
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, nuevoNinja )
        return resultado