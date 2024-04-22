import shutil
from flask import Flask
from flask import render_template_string

import os
import subprocess
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Startseite</title>
        <style>
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li a {
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
        <h1>Startseite</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/kontakte">Kontakte</a></li>
                <li><a href="/dateien">Dateien</a></li>
            </ul>
        </nav>
    </body>
    </html>
    """)

@app.route('/kontakte')
def kontakte():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kontakte</title>
        <style>
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li a {
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
        <h1>Kontakte</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/kontakte">Kontakte</a></li>
                <li><a href="/dateien">Dateien</a></li>
            </ul>
        </nav>
    </body>
    <h3>Lehrer:</h1>


<table>
  <tr>
    <th>Herr Streng </th>
    <th>Herr Weigel </th>
    <th>Frau Bauernfeind </th>

    
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
def root():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dateien</title>
        <style>
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li a {
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
        <h1>Dateien</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/kontakte">Kontakte</a></li>
                <li><a href="/dateien">Dateien</a></li>
            </ul>
        </nav>
    </body>
    </html>
    
        <html>
          <head>
            <h3>Dateien</h3>
          </head>
          <body>
           <p align = "center"> <Strong> Aktuelles Verzeichnis:</Strong> {{current_path}}</p>
           <ul>
           <form action="/md">
                <input type="submit" value="Erstellen"/>
                <input name="folder" type="text" value= "Neuer Ordner "/>
              </form>
           <li><a href="/back"> ← </a><li>
           {% for item in file_list %}
              {% if "." not in item%}
              <li><strong><a href="/cd?path={{current_path + '/' + item}}">{{item}}</a></strong><a href="/rm?dir={{item}}">  🗑</a></li>
              {% elif '.txt' or  '.json' or '.html' in item %}f
              <li><strong><a href = "/view?file={{current_path + '/' + item +'.txt'}}">{{item}}</a></strong></li>
              {% else %}
              <li>{{item}}</li>
              {%endif%}
           {%endfor%}
          </body>
        </html>
    ''', current_path = os.getcwd(),
         file_list = subprocess.check_output('ls', shell=True, cwd= os.getcwd()).decode('utf8').split('\n',))

@app.route('/back')
def back():
    os.chdir('..')
    return redirect('/')

@app.route('/cd')
def cd():
    os.chdir(request.args.get('path'))
    return redirect('/')

@app.route('/view')
def view():
    return subprocess.check_output('cat ' + request.args.get('file'), shell=True).decode('utf-8').replace('n', '<br>')

@app.route('/md')
def md():
    folder_name = request.args.get('folder')
    if folder_name not in os.listdir(os.getcwd()):
        os.mkdir(folder_name)
    else:
        print('Ordnername existiert bereits!')
    return redirect('/')

@app.route('/rm')
def rm():
    shutil.rmtree(os.getcwd() + '/' + request.args.get('dir'))
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
