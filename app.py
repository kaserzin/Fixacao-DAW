
from flask import *
from db import listar_atleta, remove_atleta, novo_atleta, detalha_atleta, atualiza_atleta

app = Flask(__name__)


@app.route('/')
def list_boardgames():
    atletas = listar_atleta()
    return render_template("volei.html", atletas=atletas)

@app.route("/remover/<int:chave>")
def apagar(chave):
    remove_atleta(chave)
    return redirect('/')

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        novo_atleta(dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    return render_template('form_volei.html', atleta=None, title='Novo Atleta')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualiza_atleta(chave, dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    atleta = detalha_atleta(chave)
    return render_template('form_volei.html', atleta=atleta, title='Editar Atleta')



if __name__ == '__main__':
    # Execução do servidor flask
    app.run()
