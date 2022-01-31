from flask_app import app
from flask_app.controladores import controlador_dojos, controlador_ninjas

if __name__ == "__main__":
    app.run( debug = True )