from typing import List
from application.model.entily.atleta import Atleta
from application.model.entily.competicao import Competicao
from application.model.entily.local import Local

class CompeticaoDao():
    def __init__(self):
        self.__list_participantes = []
        self.__list_competicoes =   []

    def listar_competicoes(self):
        return self.__list_competicoes

    def add_competicao(self,competicao):
        self.__list_competicoes.append(competicao)

    def listar_participantes(self):
        return self.__list_participantes

    def add_participante(self,atleta):
        self.__list_participantes.append(atleta)
