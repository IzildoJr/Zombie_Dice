# ALUNO: IZILDO XAVIER DOS REIS JUNIOR
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

# Importando as bibliotecas e classes para utilizar no jogo.
from random import randint,shuffle
from time import sleep
from main import Dados,Jogador

def verificarLados(lados):
    action = {
        'C':'Cérebro, você comeu um cérebro!\n',
        'P':'Passos, uma vitima fugiu!\n',
        'T':'Tiros, você tomou um tiro\n',
    }
    return action.get(lados, '')

# Função para sortear os dados com a função pop.
def JogaDados(listaDados):
    dado = listaDados.pop()
    numSorteado = randint(0, 5)
    dado.ladoSorteado = dado.lados[numSorteado]
    print('', dado.cor, '', verificarLados(dado.ladoSorteado))

    return dado

# Função para verificação dos lados do dado/jogador Atual e contabilizar os cerébros e tiros.
def verificarDados(listaDadosJogados, jogadorAtual):
    for dado in listaDadosJogados:
        if (dado.ladoSorteado == 'C'):
            jogadorAtual.cerebros = jogadorAtual.cerebros + 1
        elif (dado.ladoSorteado == 'T'):
            jogadorAtual.tiros = jogadorAtual.tiros + 1


print('\n\033[3;7m============ BEM-VINDOS A ZOMBIE DICE ============ \033[0;0m\n')
sleep(0.5)
print('INICIANDO'),sleep(1), print(".", end=" "), sleep(1), print(".", end=" "), sleep(1), print(".", end="\n")
sleep(1)
print('=-' * 50)
# Definindo um número inicial de jogadores e as condições para jogar.
numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("INFORME O NUMERO DE JOGADORES: "))

    if (numJogadores < 2):
        print('\033[1;41mATENÇÃO: O JOGO PRECISA NO MÍNIMO DE 2 JOGADORES PARA COMEÇAR! \033[0;0m\n')
    
listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    listaJogadores.append(Jogador(nome, 0, 0))
# Implementando as faces dos dados em tuplas
ladosDadoVerde = ('C','P','C','T', 'P','C')
ladosDadoAmarelo = ('T','P','C','T','P','C')
ladosDadoVermelho = ('T','P','T','C','P','T')

# Definindo as cores dos dados 
dadoVerde = Dados('\033[1;42m Verde \033[0;0m', ladosDadoVerde, '')
dadoAmarelo = Dados('\033[1;43m Amarelo \033[0;0m', ladosDadoAmarelo, '')
dadoVermelho = Dados('\033[1;41mVermelho \033[0;0m', ladosDadoVermelho, '')

# Implementando a quantidade de dados para cada uma das cores
listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]
# Criando uma variavel para armazenar a lista de dados jogados e uma variavel para o vencedor.
listaDadosJogados = []
vencedor = False
# Loop para rodar o jogo até que uma das condições seja atingida.
print('O JOGO ESTÁ SENDO INICIADO \n')
while vencedor == False:
    for jogadorAtual in listaJogadores:
        print('É a vez de', jogadorAtual.nome + '\n'), sleep(1)
# Comando para embaralhar a lista de dados, alterando as posições deles.
        shuffle(listaDados)
        numSorteado = randint(0, 5) 
# Cada dado recebe uma função para serem jogados.   
        dado1 = JogaDados(listaDados)
        sleep(1)
        dado2 = JogaDados(listaDados)
        sleep(1)
        dado3 = JogaDados(listaDados)
        sleep(1)
        
# Condição para jogar novamente ou não. 
        Game = input('Deseja jogar os dados novamente? [s/sim ou n/nao]')
        if Game == 's':
            print('Jogando os dados novamente\n')

        elif Game == 'n':
            print('Encerrando o turno')

            
        shuffle(listaDados)
# Lista de dados sendo limpa e recebendo novamente as variaveis para a proxima rodada.       
        listaDadosJogados.clear()
        listaDadosJogados.append(dado1)
        listaDadosJogados.append(dado2)
        listaDadosJogados.append(dado3)

        verificarDados(listaDadosJogados, jogadorAtual)
# Score do ultimo jogador de cada rodada
        print('  ' + jogadorAtual.nome)
        print('  ' + 'Cerebros', jogadorAtual.cerebros)
        print('  ' + 'Tiros', jogadorAtual.tiros)
        
        listaDados.append(dado1)
        listaDados.append(dado2)
        listaDados.append(dado3)
        
        shuffle(listaDados)

 # Condição de vitoria. 
    for Jogador in listaJogadores:
        if (Jogador.cerebros >= 13):
            print('O jogador', Jogador.nome, 'é o vencedor\n')
            vencedor = True
# Se algum jogador tomar 3 tiros em uma rodada é eliminado.
    for Jogador in listaJogadores:
        if (Jogador.tiros >= 3):
            print('O jogador', Jogador.nome, 'perdeu\n')
            listaJogadores.remove(Jogador)
# Restando apenas um jogador, o mesmo é o vitorioso.
    if (len(listaJogadores) == 1):
            print('O jogador', listaJogadores[0].nome, 'Ganhou\n')
            vencedor = True
            break
print('Fim de jogo')