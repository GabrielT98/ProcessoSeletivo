class Local ():
    def __init__(self,cidade: str,estado:str,endereco: str,numero:int):
        self.__cidade = cidade
        self.__estado = estado
        self.__endereco = endereco
        self.__numero = numero

    def get_cidade(self):
        return self.__cidade
    def get_estado(self):
        return self.__estado
    def get_endereco(self):
        return self.__endereco
    def get_numero(self):
        return self.__numero