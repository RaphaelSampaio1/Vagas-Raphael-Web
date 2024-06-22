from flask import Flask, render_template, jsonify, request
import urllib
from flask_sqlalchemy import SQLAlchemy
import pyodbc

app = Flask(__name__)

# Configuração da string de conexão
dados_conexao = (
    "Driver={SQL Server};"
    "Server=HOME_PC\\SQLEXPRESS;"
    "Database=sampaiovagas;"
    "Trusted_Connection=yes;"  # Usando autenticação do Windows
)

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(dados_conexao)}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Classe modelo para a tabela 'vagas'
class Vaga(db.Model):
    __tablename__ = 'vagas'
    Id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(250), nullable=False)
    Localizacao = db.Column(db.String(250), nullable=False)
    Salario = db.Column(db.Numeric(19, 4), nullable=True)
    Moeda = db.Column(db.String(10), nullable=True)
    Responsabilidades = db.Column(db.String(3000), nullable=True)
    Requisitos = db.Column(db.String(3000), nullable=True)
    

# Função para estabelecer a conexão
def conectar_bd():
    try:
        # Conectar ao banco de dados
        conexao = pyodbc.connect(dados_conexao)
        print('\033[1;32mConexão feita com sucesso!')
        # Fechar a conexão
        conexao.close()
        return True
    except pyodbc.Error as err:
        print(f'\033[1;31mErro na conexão: {err}')
        return False

# HOME
@app.route("/")
def hello_world():
    if conectar_bd():
        # Consultar todas as vagas do banco de dados
        try:
            jobs = []
            vagas = Vaga.query.all()
            for vaga in vagas:
                job = {
                    'Id': vaga.Id,
                    'titulo': vaga.Titulo,
                    'Localizacao': vaga.Localizacao,
                    'Responsabilidades': vaga.Responsabilidades
                }
                if vaga.Salario is not None:
                    job['Salario'] = float(vaga.Salario)
                jobs.append(job)
            return render_template('home.html', JOBS=jobs, company_name='Sampaio')
        except Exception as e:
            print(f'\033[1;31mErro ao consultar vagas: {e}')
            return 'Erro ao consultar vagas.'
    else:
        return 'Erro ao conectar ao banco de dados.'

# TELA DE ITENS DA VAGA
@app.route("/sobre-vaga/<int:id>")
def mostrar_vaga(id):
    vaga = Vaga.query.get(id)
    if vaga is None:
        return 'Vaga não encontrada', 404
    job = {
        'Id': vaga.Id,
        'Titulo': vaga.Titulo,
        'Localizacao': vaga.Localizacao,
        'Salario': float(vaga.Salario) if vaga.Salario else None,
        'Moeda': vaga.Moeda,
        'Responsabilidades': vaga.Responsabilidades,
        'Requisitos': vaga.Requisitos
    }
    return render_template('vaga.html', vaga=job)


# PAGINA APÓS ENVIO
@app.route("/vaga/<id>/enviado", methods = ['post'])
def inscricao_vaga(id):
    # Store this in da DB
    
    # Send a email

    # Capturar dados do formulário
    data = request.form.to_dict()
    vaga = Vaga.query.get(id)
    data['Titulo'] = vaga.Titulo
    
    return render_template('envio_vaga.html', vaga = data)



@app.route("/api/vagas")
def lista_vagas():
    jobs = Vaga.query.all()  # Busca todas as vagas do banco
    job_list = []
    for job in jobs:
        job_data = {
            'Id': job.Id,
            'Titulo': job.Titulo,
            'Localizacao': job.Localizacao,
            'Salario': float(job.Salario) if job.Salario else None,
            'Moeda': job.Moeda,
            'Responsabilidades': job.Responsabilidades,
            'Requisitos': job.Requisitos if job.Requisitos else 'Requisito não especificado'
        }
        job_list.append(job_data)
    return jsonify(job_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
