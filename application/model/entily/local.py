class Local ():
    def __init__(self,cidade: str,endereco: str):
        self.__cidade = cidade

        self.__endereco = endereco

    def get_cidade(self):
        return self.__cidade
    def get_endereco(self):
        return self.__endereco