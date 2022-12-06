# Zombie_Dice

Este é um projeto da PUC-PR para o curso de Análise e Desenvolvimento de Sistemas.

Baseado no jogo de tabuleiro Zombie Dice de Steve Jackson. Esse projeto tem como objetivo replicar as funções do jogo fisico.

Cada jogador é um Zumbi, e o objetivo final é comer 13 ou mais cérebros.

É um jogo bem simples de ser jogado, a condição inicial é de ter no minimo 2 jogadores(zumbis) e o jogo já pode ser iniciado. O primeiro passo é digitar o nome dos jogadores,
então o código irá acionar as condições para sortear os dados. Existem 3 tipos de dados com faces diferentes:

- Verde ('C','P','C','T','P','C')
- Amarelo ('T','P','C','T','P','C')
- Vermelho ('T','P','T','C','P','T')

 A letra "C" representa os cerébros ou os pontos.
 A letra "T" representa os tiros, indicando que o zumbi tomou um tiro.
 A letra "P" representa os passos, indicando que uma vitima fugiu. 

Em cada turno o jogador "pega" 3 dados com cores aleatórias, e o console irá mostrar quais dados e faces foram sorteadas. Após jogar os dados e não ter um total de 3 tiros
o jogador atual pode jogar novamente os dados ou encerrar o seu turno.

Foram implementadas as condições de vitória e de derrota, ao final do jogo é exibido no console o vencedor e os perdedores.

Um trabalho desenvolvido pelo estudante Izildo Junior para a disciplina de Raciocínio computacional com a linguagem Python.
