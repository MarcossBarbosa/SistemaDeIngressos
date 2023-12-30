from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    nome = "Marcos Vinicius dos Santos"
    return render_template('index.html', nome=nome)

@app.route('/Tela_de_Login')

def Tela_de_Login():
    return render_template('Tela_de_Login.html')

if __name__ == '__main__':
    app.run(debug=True)