@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        identifiant = request.form['identifiant']
        mot_de_passe = hashlib.sha256(request.form['mot_de_passe'].encode()).hexdigest()

        conn = sqlite3.connect('banque.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        user = cursor.fetchone()
        conn.close()

        if user and user[4] == mot_de_passe:
            return "Connexion réussie !"
        else:
            return "Identifiant ou mot de passe incorrect."

    return render_template_string('''
    <form method="POST">
        Identifiant: <input type="text" name="identifiant" required><br>
        Mot de passe: <input type="password" name="mot_de_passe" required><br>
        <button type="submit">Se connecter</button>
    </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
