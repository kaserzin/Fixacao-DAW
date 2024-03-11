
from flask import *
from db import Atleta

app = Flask(__name__)
a = Atleta

@app.route('/')
def list_boardgames():
    atletas = a.listar_atleta()
    return render_template("volei.html", atletas=atletas)

@app.route("/remover/<int:chave>")
def apagar(chave):
    a.remove_atleta(chave)
    return redirect('/')

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.novo_atleta(dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    return render_template('form_volei.html', atleta=None, title='Novo Atleta')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.atualiza_atleta(chave, dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    atleta = a.detalha_atleta(chave)
    return render_template('form_volei.html', atleta=atleta, title='Editar Atleta')



if __name__ == '__main__':
    app.run()
