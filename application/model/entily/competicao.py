from datetime import datetime
from typing import List

from application.model.entily.local import Local
from application.model.entily.atleta import Atleta
class Competicao():

    def __init__(self,id:int ,nome: str, local: Local,data: datetime):
        self.__id = id
        self.__nome = nome
        self.__local = local
        self.__data = data
        self.__status = "andamento"

    def mudar_status(self):
        self.__status = "Finalizada"

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome
    def get_local(self):
        return self.__local
    def get_data(self):
        return self.__data
    def get_status(self):
        return self.__status