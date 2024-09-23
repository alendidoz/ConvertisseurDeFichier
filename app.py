from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Dossier pour stocker les fichiers téléchargés
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fonction pour gérer la conversion (exemple simple)
def convert_file(file, format):
    # Logique de conversion ici, par exemple avec un module comme pydub pour MP3
    return f"Le fichier {file.filename} a été converti en {format}."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        format = request.form['format']
        
        # Sauvegarder le fichier téléchargé
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        # Appeler la fonction de conversion
        result = convert_file(file, format)
        
        return result  # Remplace par une redirection ou un message sur la page

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
