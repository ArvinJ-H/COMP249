from bottle import Bottle

app = Bottle()


@app.route('/')

def index():

    return 


if __name__ == '__main__':
    app.run();