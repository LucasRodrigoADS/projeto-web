from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jogos = [
    { 'Nome do Jogo': 'State of decay 2', 'Preço': 'R$ 79.99', 'Nota':66 },
    { 'Nome do Jogo': 'Mass Effect Legendary Edition', 'Preço': 'R$ 299.99','Nota':86 },
    { 'Nome do Jogo': 'Dragon Age: Origins', 'Preço': 'R$ 59.00', 'Nota':91 },
    { 'Nome do Jogo': 'Forza Horizon 5', 'Preço': 'R$ 249.99', 'Nota':95 },
    { 'Nome do Jogo': 'Tales From the Borderlands: A Telltale Game Series', 'Preço': 'R$ 104.90', 'Nota':86 },
    { 'Nome do Jogo': 'Stardew Valley', 'Preço': 'R$ 24.99', 'Nota':89 },
    { 'Nome do Jogo': 'The Witcher 3: Wild Hunt', 'Preço': 'R$ 79.99', 'Nota':93 },
    { 'Nome do Jogo': 'Dead by Daylight', 'Preço': 'R$ 29.80', 'Nota':71 },
]

@app.route('/')     # Página principal
def index():
    return render_template('index.html', lista=jogos)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/salvar', methods=['POST'])   
def salvar():
    nome_jogo = request.form['nome_jogo']   
    preco = request.form['preco']
    nota = request.form['nota'] 
    novo = { 'Nome do Jogo':f'{nome_jogo}', 'Preço':f'R$ {preco}', 'Nota': nota } # dicionário recebendo o novo jogo

    jogos.append(novo) # adição do novo jogo à lista

    return redirect('https://5000-white-mink-pc7apk61.ws-us18.gitpod.io/')

@app.route('/remover', methods=['POST'])
def remover():
    deleta = request.form['deleta']
    if deleta > '':
        deleta = int(deleta)    # compara a posição inserida pelo usuário com o tamanho da lista
        if deleta <= len(jogos) and deleta > 0 and deleta != None: 
            del jogos[deleta-1]                 # deleta o jogo
            return redirect('https://5000-scarlet-swordtail-tgh8x58v.ws-us18.gitpod.io/')
            
    return render_template('erro-remover.html') # caso o if não for respeitado, a pág de erro é retornada

@app.route('/buscar', methods=['POST'])
def buscar():
    jogo_lista = []
    busca = request.form['busca']
    if busca > '':
        for jogo in jogos: 
            if busca.lower() in jogo['Nome do Jogo'].lower():   # compara a busca com os jogos presentes na lista
                jogo_lista.append(jogo)                         # nova lista com os resultados das buscas
        return render_template('busca.html', jogo_lista=jogo_lista)

    return render_template('erro-remover.html') # caso o if não for respeitado, a pág de erro é retornada

app.run(debug=True)
