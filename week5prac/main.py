__author__ = 'Arvin Han'

import bottle
import os
import model
app = bottle.Bottle()
bottle.debug(True)

@app.route('/')
def root():
    "Present the main page"
    db = model.connect()
    data = model.list_enrolments(db)

    return bottle.template('index.html',data=data)


@app.route('/create')
def create():
    db = model.connect()
    model.create_tables(db)
    db.close()
    bottle.redirect('/')




@app.route('/units',method="POST")
def unit():
    db = model.connect()
    name = bottle.request.forms.get('name')
    for unit in bottle.request.forms.getall('unit'):
        model.add_enrollment(db,name,unit)
    db.close()
    bottle.redirect('/')

if __name__ == "__main__":
    #
    # from bottle.ext import sqlite
    # # install the database plugin
    # app.install(sqlite.Plugin(dbfile=model.DATABASE_NAME))

    app.run()
