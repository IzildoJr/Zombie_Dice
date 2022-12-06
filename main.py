class Dados:
    def __init__(self, cor, lados, ladoSorteado):
        self.cor = cor
        self.lados = lados
        self.ladoSorteado = ladoSorteado

class Jogador:
    def __init__(self, nome, cerebros, tiros):
        self.nome = nome
        self.cerebros = cerebros
        self.tiros = tiros