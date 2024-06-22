# Sampaio Vagas



Sampaio Vagas foi um sistema de vagas de emprego com interface simples com Flask.
Nela é contida Informações de envio de e-mail, inscrição para vaga e cadastro de vagas via banco de dados.  Tudo isso feito com Python, HTML/CSS e como framework temos : Flask e Bootstrap.

O banco de dados é SQL SERVER, então caso queira conectar seu banco, ultilize o SQL Server.

Criação de tabelas :

vagas =
CREATE TABLE vagas (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Titulo VARCHAR(250) NOT NULL,
    Localizacao VARCHAR(250) NOT NULL,
    Salario NUMERIC(19, 4) NULL,
    Moeda VARCHAR(10) NULL,
    Responsabilidades VARCHAR(3000) NULL,
    Requisitos VARCHAR(3000) NULL
);


[INSERT] = 


INSERT INTO VAGAS(Titulo, Localizacao, Salario, Moeda, Responsabilidades,Requisitos)
VALUES (
'Desenvolvedor de Automações',
    'São Paulo, SP',                      
    8000.00,                              
    'BRL',                                
    'Desenvolver e manter scripts de automação para testes funcionais e de regressão.',
     '- Experiência comprovada em desenvolvimento de scripts de automação.
     - Conhecimento em linguagens como Python, JavaScript ou similar.
     - Capacidade de analisar e resolver problemas de forma eficiente.
     - Boa comunicação e habilidades interpessoais.'
);
 
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

Para mais informações Entre em contato comigo : https://sampaiodev.com/
