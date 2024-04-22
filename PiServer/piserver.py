import shutil

from flask import Flask
from flask import render_template_string, redirect, request
import os
import subprocess
import socket

app = Flask(__name__)

@app.route('/')
def root():
    return render_template_string('''
        <html>
          <head>
            <title>Raspberry Pi Server</title>
          </head>
          <body>
               <h1 align="center"> Raspberry Pi Server </h1>
               <div style="display: flex; justify-content: center; align-items: center; height: 30%;">
               <img src="{{url_for('static', filename='logo.png')}}" alt="Logo" style="max-width: 50%; max-height: 50%;" />
           </div>
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

if __name__ == "__main__":
    from waitress import serve

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Server ist erreichbar unter http://{local_ip}:4000/")
    serve(app, host=local_ip, port=4000)