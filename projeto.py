from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jogos = [
    { 'Nome do Jogo': 'State of decay 2', 'Preço': 'R$ 79,99', 'Nota':66 },
    { 'Nome do Jogo': 'Mass Effect Legendary Edition', 'Preço': 'R$ 299,99','Nota':86 },
    { 'Nome do Jogo': 'Dragon Age: Origins', 'Preço': 'R$ 59,00', 'Nota':91 },
    { 'Nome do Jogo': 'Forza Horizon 5', 'Preço': 'R$ 249,99', 'Nota':95 },
    { 'Nome do Jogo': 'Tales From the Borderlands: A Telltale Game Series', 'Preço': 'R$ 104,90', 'Nota':86 },
    { 'Nome do Jogo': 'Stardew Valley', 'Preço': 'R$ 24,99', 'Nota':89 },
    { 'Nome do Jogo': 'The Witcher 3: Wild Hunt', 'Preço': 'R$ 79,99', 'Nota':93 },
    { 'Nome do Jogo': 'Dead by Daylight', 'Preço': 'R$ 29,80', 'Nota':71 },
]

@app.route('/')
def index():
    return render_template('index.html', lista=jogos)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/salvar', methods=['POST']) # <form action='/salvar' method='POST'> salva o formulário
def salvar():
    nome_jogo = request.form['nome_jogo'] # <input name='texto'/> jogo adicionado à lista
    preco = request.form['preco']
    nota = request.form['nota'] 
    jogo_count = len(jogos)
    novo = { 'Nome do Jogo':f'{nome_jogo}', 'Preço':f'R$ {preco}', 'Nota': nota }

    jogos.append(novo) # adição do novo jogo à lista

    return redirect('https://5000-gray-tyrannosaurus-tu1ml5ud.ws-us18.gitpod.io/')

@app.route('/remover', methods=['POST'])
def remover():
    deleta = request.form['deleta']
    deleta = int(deleta)
    if deleta <= len(jogos) and deleta > 0:
        del jogos[deleta-1]
        return redirect('https://5000-gray-tyrannosaurus-tu1ml5ud.ws-us18.gitpod.io/')
    return render_template('erro-remover.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    jogo_lista = []
    busca = request.form['busca']
    for jogo in jogos: 
        if busca.lower() in jogo['Nome do Jogo'].lower():
            jogo_lista.append(jogo)
    return render_template('busca.html', lista=jogo_lista)
        

app.run(debug=True)
