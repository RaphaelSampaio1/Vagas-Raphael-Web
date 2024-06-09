from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'titulo' : 'Analista de Dados',
        'Localização' : 'São Paulo, Brasil',
        'Salario' : 6800
    },
    {
        'id': 2,
        'titulo' : 'Desenvolvedor Front-end',
        'Localização' : 'São Paulo, Brasil',
       
    },
    {
        'id': 3,
        'titulo' : 'Engenheiro de dados PL',
        'Localização' : 'Santa Catarina, Brasil',
        'Salario' : 13200
    },
    {
        'id': 4,
        'titulo' : 'Gestor de Tragego',
        'Localização' : 'Remoto',
        'Salario' : 9800
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',JOBS=JOBS,company_name='Sampaio')

app.run(host='0.0.0.0',debug=True)