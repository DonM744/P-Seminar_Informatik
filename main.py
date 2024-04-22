from flask import Flask
from flask import render_template_string

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
    <h1>Lehrer</h1>

<table>
  <tr>
    <th>Herr ...</th>
    <th>Frau ...</th>
    <th>Herr ...</th>
  </tr>
  <tr>
    <td>Deutsch</td>
    <td>Mathematik</td>
    <td>Französisch</td>
   </tr>
   <tr>
     <td>Argumentieren</td>
     <td>Stochastik</td>
     <td>"Passé Composé></td>
   </tr>
</table>
    </html>
    """)

@app.route('/dateien')
def dateien():
    return render_template_string("""
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
    """)

if __name__ == '__main__':
    app.run(debug=True)

