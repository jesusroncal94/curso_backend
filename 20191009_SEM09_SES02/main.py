from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hola Pachaqtec</h1>'

@app.route('/alumnos')
def alumnos():
    return 'Lista de alumnos'

@app.route('/profesores')
def profesores():
    return 'Lista de profesores'

@app.route('/alumnos/notas')
def alumnosNotas():
    return 'Lista de notas [Alumno]'

@app.route('/alumnos/<id>/notas')
def alumnosNotasGet(id):
    return f'<h1>Lista de notas [Alumno - ID: {id}]</h1>'

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Página no encontrada...</h1>', 404

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug = True)
