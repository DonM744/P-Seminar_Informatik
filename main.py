# letzter Stand (3. Juni)

import os
import subprocess
from flask import Flask, render_template_string, redirect, request, session, url_for

#erinnerung (session: speichert Informationen über Benutzer)

app = Flask(__name__)
app.secret_key = 'geheim'

# hier werden neue Accounts (Name & Passwort) zugewiesen
users = {'test': 'test', 'user' : 'user'}


nav_bar = """        
#Navigationsleiste mit Formatierung
<!DOCTYPE html>
<html>
<head>
    <title>Nachhilfemanager</title>
    <style>
    <!--Anlegen des Menüs für Anwendungen-->
        nav ul {            <!--Formatierung des Menüs-->
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;
        }
        nav li {
            float: left;
        }
        nav li a {           <!--Textformatierung-->
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        nav li a:hover {
            background-color: #ddd;
            color: black;
        }
    </style>
</head>
<body>
    <h1>Nachhilfemanager 🏫</h1>
    <nav>
    <!--Anlegen der Links zu Anwendungen-->
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/kontakte">Kontakte</a></li>
            <li><a href="/dateien">Dateien</a></li>
            <li><a href="/forum">Forum</a></li>
            {% if 'username' in session %}
                <li><a href="/logout">Logout</a></li>
            {% else %}
                <li><a href="/login">Login</a></li>
            {% endif %}
        </ul>
    </nav>
</body>
</html>
"""
#Beschränkung für login-pflichtige Aktionen
def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/')
#Methode zum Aufrufen des Home-Bildschirms
def home():
    return render_template_string(nav_bar)

@app.route('/login', methods=['GET', 'POST'])
#Methode zum Einloggen
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template_string(nav_bar + '''
        <form method="post" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/logout')
#Methode zum Ausloggen
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/kontakte')
#Methode zum Aufrufen der Kontakte
@login_required
def kontakte():
    return render_template_string(nav_bar + """
    <h3>Lehrer</h3>
    <table>
      <tr>
        <th>Herr ... </th>
        <th>Herr ... </th>
        <th>Frau ... </th>
      </tr>
      <tr>
        <td>Deutsch </td>
        <td>Mathematik </td>
        <td>Französisch </td>
      </tr>
      <tr>
        <td>Argumentieren </td>
        <td>Stochastik </td>
        <td>Passé Composé</td>
      </tr>
    </table>
    </html>
    """)

@app.route('/dateien')
#Methode zum Aufrufen der Dateien
@login_required
def root():
    #Verzeichnis von Dateien
    return render_template_string(nav_bar + '''
        <html>
          <head>
            <h3>Lernmaterialien</h3>
          </head>
          <body>
           <p align="center"><strong>Aktuelles Verzeichnis:</strong> {{show_current_path}}</p>
           <ul>
           <li><a href="/back">←</a></li>
           {% for item in file_list %}
              {% if "." not in item %}
               <li><strong><a href="/cd?path={{current_path + '/' + item}}">{{item}}</a></strong></li>
              {% else %}
              <li>{{item}}</li>
              {% endif %}
           {% endfor %}
          </body>
        </html>
    ''', show_current_path=os.getcwd().replace('/Users/jonas/PycharmProjects/Nachhilfe Manager', '/Nachhilfe Manager'),
        current_path=os.getcwd(),
        file_list=subprocess.check_output('ls', shell=True, cwd=os.getcwd()).decode('utf8').split('\n'))

@app.route('/cd')
@login_required
def cd():
    os.chdir(request.args.get('path'))
    return redirect('/dateien')

@app.route('/back')
@login_required
def back():
    os.chdir('/Users/jonas/PycharmProjects/Nachhilfe Manager')
    return redirect('/dateien')

@app.route('/forum', methods=['GET', 'POST'])
#Forum zum Posten von Nachrichten
@login_required
def forum():
    if request.method == 'POST':
        message = request.form['message']
        messages.append(message)
        return redirect('/forum')
    return render_template_string(nav_bar + """
        <h3>Forum</h3>
        <form action="/forum" method="post">
            <div align="left" style="width: px; height: 300px; overflow-y: auto; border: 1px solid #ccc;">
            #Speicherung der Nachrichten im Forum
                <div class="message-container">
                    <div>
                          {% for message in messages %}
                           <p>&nbsp;AbsenderName: {{ message }}</p><br>
                          {% endfor %}
                    </div>
                </div>
            </div>
            <p><label>Stelle eine Frage:</label></p>
            <textarea id="message" name="message" rows="4" cols="50"></textarea>
            <br>
            <input type="submit" value="Senden ✉️">
        </form>
    """)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

