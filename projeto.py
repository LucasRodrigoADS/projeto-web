from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jogos = [
    {'Nome do Jogo': 'State of decay 2', 'Preço': 'R$ 79,99', 'Nota':66},
    {'Nome do Jogo': 'Mass Effect Legendary Edition', 'Preço': 'R$ 299,99','Nota':86},
    {'Nome do Jogo': 'Dragon Age: Origins', 'Preço': 'R$ 59,00', 'Nota':91},
    {'Nome do Jogo': 'Forza Horizon 5', 'Preço': 'R$ 249,99', 'Nota':95},
    {'Nome do Jogo': 'Tales From the Borderlands: A Telltale Game Series', 'Preço': 'R$ 104,90', 'Nota':86},
    {'Nome do Jogo': 'Stardew Valley', 'Preço': 'R$ 24,99', 'Nota':89},
    {'Nome do Jogo': 'The Witcher 3: Wild Hunt', 'Preço': 'R$ 79,99', 'Nota':93},
    {'Nome do Jogo': 'Dead by Daylight', 'Preço': 'R$ 29,80', 'Nota':71},
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
    novo = { 'Nome do Jogo':f'{nome_jogo}', 'Preço':f'R$ {preco}', 'Nota': nota }

    jogos.append(novo) # adição do novo jogo à lista

    return redirect('https://5000-coral-crayfish-6c1897a5.ws-us18.gitpod.io/')

@app.route('/remover', methods=['POST'])
def remover():
    remove = request.form['remove']
    remove = int(remove)
    del jogos[remove-1]
    
    return redirect('https://5000-coral-crayfish-6c1897a5.ws-us18.gitpod.io/')

@app.route('/buscar', methods=['POST'])
def buscar():
    busca = request.form['busca']
    jogo_dict = dict()
    for jogo in jogos: 
        if busca.lower() in jogo['Nome do Jogo'].lower():
            jogo_dict.update(jogo)
            jogo_posicao = [jogo_dict]
            return render_template('busca.html', jogo_lista=jogo_posicao)

    return render_template('botão.html')
        

app.run(debug=True)
