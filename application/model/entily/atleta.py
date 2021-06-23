class Atleta():
    def __init__(self,nome:str,idade:int,altura:float,peso:float):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso
        self.__tempo_corrida = 0
        self.__distancia_dardo = 0

    def set_tempo_corrida(self,tempo):
            self.__tempo_corrida = tempo

    def set_distancia(self,distancia):
            self.__distancia_dardo = distancia

    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_altura(self):
        return self.__altura
    def get_peso(self):
        return self.__peso

    def get_tempo(self):
        return self.__tempo_corrida
    def get_distancia(self):
        return self.__distancia_dardo