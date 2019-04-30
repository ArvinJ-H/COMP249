from bottle import Bottle, debug, static_file, template, request, redirect, response

from database import get_likes, add_like

app = Bottle()
debug(True)

@app.route('/')
def index(db):
    """Generate the main page"""

    info = {
        'title': 'My Main Page',
        'likes': get_likes(db),
    }

    return template('index', info )


@app.post('/like')
def handle_like(db):
    """Handle submission of the like form"""

    name = request.forms.get("name")

    thing = request.forms.get("thing")

    add_like(db, name, thing)

    return redirect('/')

@app.route("/")
def hello_again():
    if request.get_cookie(visited):
        count = int(count)+1
        response.set_cookie("visited",str(count))
        return "welcomeback"+ str(count) + "time"
    else:
        response.set_cookie("visited", "1")
        return "Nice to meet you"

@app.route('/static/<filepath:path>')
def static(filepath):

    return static_file(filepath, root='static')


if __name__=='__main__':

    from bottle.exe import sqlite
    from database import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))

    app.run()