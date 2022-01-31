from flask import request, redirect, session, url_for
from flask_app import app
from flask_app.modelos.modelo_ninjas import Ninjas
from datetime import datetime


@app.route( '/dojos/ninja_new', methods=["POST"] )
def crearNinja_P():
    nuevoNinja = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"],
        "created_at" : datetime.today(),
        "update_at" : datetime.today()
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["age"] = request.form["age"]
    session["dojo_id"] = request.form["dojo_id"]
    session["created_at"] = datetime.today()
    session["update_at"] = datetime.today()
    Ninjas.agregaNinja( nuevoNinja )
    idDojo = request.form["dojo_id"]
    return redirect(url_for( 'mostrarDojos', idDojo=idDojo ))