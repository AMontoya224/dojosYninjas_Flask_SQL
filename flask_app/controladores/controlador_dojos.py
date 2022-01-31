from flask import render_template, request, session, redirect, url_for
from flask_app import app
from flask_app.modelos.modelo_dojos import Dojos
from datetime import datetime


@app.route( '/dojos', methods=["GET"] )
def despliegaDojos():
    listaDojos = Dojos.obtenerListaDojos()
    return render_template( "dojos.html", listaDojos=listaDojos)

@app.route( '/ninjas', methods=["GET"] )
def mostrarNinjas():
    listaDojos = Dojos.obtenerListaDojos()
    return render_template("ninjas.html", listaDojos=listaDojos)

@app.route( '/dojos/<idDojo>', methods=["GET"] )
def mostrarDojos( idDojo ):
    encontrarDojo = {
        "dojo_id" : idDojo
    }
    ninjas = Dojos.obtenerListaConNinjas(encontrarDojo)
    if ninjas == ():
        ninjas = []
        lista = {
            "name" : idDojo
        }
        ninjas.append(lista)
    return render_template( "dojos_show.html", ninjas=ninjas)


@app.route( '/dojos/<idDojo>', methods=["POST"] )
def irDojoID(idDojo):
    return redirect(url_for( 'mostrarDojos', idDojo=idDojo ))

@app.route( '/dojos', methods=["POST"] )
def irDojos():
    return redirect( '/dojos' )

@app.route( '/dojos/new', methods=["POST"] )
def crearDojo_P():
    nuevoDojo = {
        "name" : request.form["name"],
        "created_at" : datetime.today(),
        "update_at" : datetime.today()
    }
    session["name"] = request.form["name"]
    session["created_at"] = datetime.today()
    session["update_at"] = datetime.today()
    Dojos.agregaDojo( nuevoDojo )
    return redirect( '/dojos' )

@app.route( '/ninjas', methods=["POST"] )
def mostrarNinjas_P():
    return redirect( '/ninjas' )