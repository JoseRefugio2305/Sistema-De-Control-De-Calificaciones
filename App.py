import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from filasalumnos import *
#import mariadb
# initializations
app = Flask(__name__)

#Conexion con mariadb usando la libreria de mysql
app.config['MYSQL_HOST'] = '127.0.0.1' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'RefugioRivera23'
app.config['MYSQL_DB'] = 'instituto'
mariadb = MySQL(app)

#Esta clave es para proteger nuestra sesion
app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    cur = mariadb.connection.cursor()
    cur.execute('SELECT * FROM Grupo')
    data = cur.fetchall()
    columnas = [description[0] for description in cur.description]
    #Se renderiza la plantilla de html y se le mandan los datos que resultan de la consulta anterior
    return render_template('pruebaindex.html', grupos = data, nombcolumnas=columnas)


@app.route('/login')
def Login():
    print("Hola")
    return render_template('login2.html')


@app.route('/addgrupo', methods = ['POST'])
def AgregarGrupo():
    if request.method == 'POST':
        idgrupo = request.form['ID_Grupo']
        nombgrupo = request.form['Nombre']
        aula = request.form['Aula']
        turno = request.form['Turno']
        jefegrupo = request.form['Jefe_Grupo']
        cur = mariadb.connection.cursor()
        cur.execute('INSERT INTO grupo (ID_Grupo, Nombre, Aula, Turno, Jefe_Grupo)VALUES (%s, %s, %s, %s, %s)', 
        (idgrupo, nombgrupo,aula, turno, jefegrupo))
        mariadb.connection.commit()
        flash('El grupo se agrego correctamente')
        return redirect(url_for('Index'))


@app.route('/editGrupo/<id>')
def ObtenerGrupo(id):
    cur = mariadb.connection.cursor()
    cur.execute('SELECT * FROM grupo WHERE ID_Grupo = %s', (id))
    data = cur.fetchall()
    return render_template('edit-grupo.html', grupoelegido = data[0])

@app.route('/updateGrupo/<id>', methods = ['POST'])
def ActualizarGrupo(id):
    if request.method == 'POST':
        idgrupo = request.form['ID_Grupo']
        nombgrupo = request.form['Nombre']
        aula = request.form['Aula']
        turno = request.form['Turno']
        jefegrupo = request.form['Jefe_Grupo']
        cur = mariadb.connection.cursor()
        cur.execute("""
        UPDATE grupo
        SET ID_Grupo = %s,
            Nombre = %s,
            Aula = %s,
            Turno = %s,
            Jefe_Grupo = %s
        WHERE ID_Grupo = %s
        """, (idgrupo, nombgrupo,aula, turno, jefegrupo, id))
        mariadb.connection.commit()
        flash('Se actualizaron correctamente los datos del grupo')
        return redirect(url_for('Index'))

@app.route('/deleteGrupo/<string:id>')
def EliminarGrupo(id):
    cur = mariadb.connection.cursor()
    cur.execute('DELETE FROM grupo WHERE ID_Grupo = {0}'.format(id))
    mariadb.connection.commit()
    flash('El grupo se borro correctamente')
    return redirect(url_for('Index'))

@app.route('/ListaCalificaciones/<id>')
def ListaCalificaciones(id):
    cur = mariadb.connection.cursor()
    cur2= mariadb.connection.cursor()
    cur3= mariadb.connection.cursor()
    cur.execute('SELECT * FROM Alumno')
    cur2.execute('SELECT CONCAT_WS(" ", Nombre, Ap_Pat_Al, Ap_Mat_Al) AS Alumno FROM Alumno')
    data = cur.fetchall()
    datanombal = cur2.fetchall()
    columnas = [description[0] for description in cur.description]
    cur3.execute('SELECT Nombre FROM Grupo WHERE ID_Grupo= {0}'.format(id))
    grupos = cur3.fetchall()
    grupoelegido = grupos[0]
    #datos = datosacomodados(data, datanombal)
    #print(datos)
    return render_template('listacalificaciones.html', alumnos=data, nombcolumnas=columnas, grupo = grupoelegido[0])


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
