from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        date_naissance = request.form['date_naissance']
        identifiant = request.form['identifiant']
        mot_de_passe = hashlib.sha256(request.form['mot_de_passe'].encode()).hexdigest()
        question_securite = request.form['question_securite']
        reponse_securite = hashlib.sha256(request.form['reponse_securite'].encode()).hexdigest()

        conn = sqlite3.connect('banque.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO utilisateurs (nom, prenom, date_naissance, identifiant, mot_de_passe, question_securite, reponse_securite) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nom, prenom, date_naissance, identifiant, mot_de_passe, question_securite, reponse_securite))
        conn.commit()
        conn.close()

        return "Inscription réussie ! <a href='/connexion'>Se connecter</a>"

    return render_template_string('''
    <form method="POST">
        Nom: <input type="text" name="nom" required><br>
        Prénom: <input type="text" name="prenom" required><br>
        Date de naissance: <input type="date" name="date_naissance" required><br>
        Identifiant: <input type="text" name="identifiant" required><br>
        Mot de passe: <input type="password" name="mot_de_passe" required><br>
        Question de sécurité: <input type="text" name="question_securite" required><br>
        Réponse: <input type="text" name="reponse_securite" required><br>
        <button type="submit">S'inscrire</button>
    </form>
    ''')
