__author__ = 'Arvin Han'

from bottle import Bottle, debug, static_file, template, request, redirect, response
import os
import model
app = Bottle()
# Bottle.debug(True)

@app.route('/')
def root():
    "Present the main page"
    db = model.connect()
    data = model.list_enrolments(db)

    return template('index.html',data=data)


def hello_again():
    cookie = request.get_cookie(visited)
    if cookie:
        count = int(count)+1
        response.set_cookie("visited",str(count))
        return "welcomeback"+ str(count) + "time"

    response.set_cookie("visited", "1")
    return "Nice to meet you"


@app.route('/create')
def create():
    db = model.connect()
    model.create_tables(db)
    db.close()
    redirect('/')



@app.route('/units',method="POST")
def unit():
    db = model.connect()
    name = request.forms.get('name')
    for unit in request.forms.getall('unit'):
        model.add_enrollment(db,name,unit)
    db.close()
    redirect('/')

if __name__ == "__main__":
    #
    # from bottle.ext import sqlite
    # # install the database plugin
    # app.install(sqlite.Plugin(dbfile=model.DATABASE_NAME))

    app.run()
