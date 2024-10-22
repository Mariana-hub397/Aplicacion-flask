from flask import Flask, render_template, request, redirect, url_for
from confing import *
from animal_data import Animal

# Conexión a la base de datos
con_bd = Conexion()

app = Flask(__name__)


@app.route('/')
def index():
    # Obtenemos todos los datos de bienestar animal de la base de datos
    datos_animales = con_bd['BienestarAnimal']
    animales_registrados = datos_animales.find()
    return render_template('index.html', animales=animales_registrados)


@app.route('/guardar_animal', methods=['POST'])
def agregar_animal():
    datos_animales = con_bd['BienestarAnimal']
    
    # Recogemos los datos del formulario
    animal_id = request.form['animal_id']
    alimentacion = request.form['alimentacion']
    salud = request.form['salud']
    comportamiento = request.form['comportamiento']
    manejo_ambiental = request.form['manejo_ambiental']
    fecha = request.form['fecha']
    
    if animal_id and alimentacion and salud and comportamiento and manejo_ambiental and fecha:
        # Creamos un objeto de tipo AnimalData y lo insertamos en la base de datos
        animal = {
            'animal_id': animal_id,
            'alimentacion': alimentacion,
            'salud': salud,
            'comportamiento': comportamiento,
            'manejo_ambiental': manejo_ambiental,
            'fecha': fecha
        }
        datos_animales.insert_one(animal)
        return redirect(url_for('index'))
    else:
        return "Error al guardar los datos del animal"


@app.route('/eliminar_animal/<string:animal_id>')
def eliminar(animal_id):
    datos_animales = con_bd['BienestarAnimal']
    datos_animales.delete_one({'animal_id': animal_id})
    return redirect(url_for('index'))


@app.route('/editar_animal/<string:animal_id>', methods=['POST'])
def editar(animal_id):
    datos_animales = con_bd['BienestarAnimal']
    
    # Recogemos los nuevos datos del formulario
    alimentacion = request.form['alimentacion']
    salud = request.form['salud']
    comportamiento = request.form['comportamiento']
    manejo_ambiental = request.form['manejo_ambiental']
    fecha = request.form['fecha']
    
    if alimentacion and salud and comportamiento and manejo_ambiental and fecha:
        datos_animales.update_one({'animal_id': animal_id}, {'$set':{
            'alimentacion': alimentacion,
            'salud': salud,
            'comportamiento': comportamiento,
            'manejo_ambiental': manejo_ambiental,
            'fecha': fecha
        }})
        return redirect(url_for('index'))
    else:
        return "Error al editar los datos del animal"


@app.route('/visualizar')
def visualizar():
    datos_animales = con_bd['BienestarAnimal']
    animales_registrados = datos_animales.find()
    return render_template('visualizar.html', animales=animales_registrados)


if __name__ == '__main__':
    app.run(debug=True)
