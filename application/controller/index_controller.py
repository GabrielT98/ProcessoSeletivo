from datetime import datetime

from application import app
from flask import Flask, render_template, request, redirect
from application.model.dao.competicao_dao import CompeticaoDao
from application.model.entily.atleta import Atleta
from application.model.entily.competicao import Competicao
from application.model.entily.local import Local


competicao_dao = CompeticaoDao()
list_competicao = competicao_dao.listar_competicoes()
qtd = 0


@app.route("/")
def index():
    return render_template("index.html",list_competicao = list_competicao)

@app.route("/qtdatlta",methods=["POST"])
def qtd():
    global qtd
    qtd = int(request.form.get('qtd',None))
    return redirect("adicionar.html")



@app.route("/adicionar.html")
def adicionar():
    return render_template("adicionar.html",qtd =qtd)
@app.route("/add",methods=["POST"])
def add():
    nome_competicao = request.form.get('nome')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    local = Local(cidade,endereco)
    data_str = request.form.get('data')
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M')
    id = len(list_competicao)+1
    i =1
    while i <= int(qtd):
        nome_participante = request.form.get('nome-{}'.format(i),None)
        idade_participante = int(request.form.get('idade-{}'.format(i)),None)
        altura_participante = float(request.form.get('altura-{}'.format(i)),None)
        peso_participante = float(request.form.get('peso-{}'.format(i)),None)
        atleta = Atleta(nome_participante,idade_participante,altura_participante,peso_participante)
        competicao_dao.add_participante(atleta)
        i+=1
    competicao = Competicao(id,nome_competicao,local,data)
    competicao_dao.add_competicao(competicao)

    return render_template("index.html",list_competicao=list_competicao)

app.route('/encerrar/<id>')
def encerrar(id):
    for competicao in list_competicao:
        if competicao.get_id() == int(id):
            competicao.mudar_status()
            return render_template("index.html",list_competicao = list_competicao)

