'''''PROJETO: Jogo da Velha com Tkinter
 
1. Planeje o jogo:
- O jogo tem uma grade 3x3 (9 botões).
- Dois jogadores (X e O) jogam alternadamente.
- O objetivo é alinhar 3 símbolos na horizontal, vertical ou diagonal.
- Deve ter uma forma de reiniciar o jogo.
- Exibir mensagem quando alguém ganhar ou der empate.
 
2. Crie a janela principal:
- Use tk.Tk() para criar a janela.
- Defina título e tamanho da janela.
 
3. Organize os botões na tela:
- Use um layout com .grid() para organizar os 9 botões em 3 linhas e 3 colunas.
- Cada botão representa uma casa do jogo.
 
4. Controle o turno dos jogadores:
- Crie uma variável para controlar se é a vez do "X" ou do "O".
- A cada clique em um botão, coloque o símbolo correspondente.
 
5. Implemente a função para clicar nos botões:
- Quando o jogador clicar, o botão mostra "X" ou "O".
- O botão fica desabilitado para não poder ser clicado novamente.
- Troque o turno para o próximo jogador.
 
6. Cheque vitória e empate:
- Depois de cada jogada, cheque se algum jogador venceu.
- Verifique todas as linhas, colunas e diagonais.
- Se alguém venceu, mostre uma mensagem e bloqueie os botões.
- Se todas as casas estiverem preenchidas e ninguém venceu, mostre empate.
 
7. Crie botão para reiniciar o jogo
- Um botão “Reiniciar” que limpa todos os botões e reseta o turno para o jogador "X".
 
8. Organize seu código
- Separe o código em funções para ficar mais fácil de entender.
- Use classes se já tiver aprendido (opcional para iniciantes).
 
9. Teste seu jogo
- Jogue para garantir que tudo funciona: vitória, empate, reinício.
- Corrija bugs que aparecerem.
 
10. Melhore o jogo (opcional)
- Mostre mensagens na janela usando Labels.
- Adicione um placar de vitórias.
- Torne a interface mais bonita.'''

'''import tkinter as tk

"""
- Frame com 9 botoes
- Variavel Jogador que alterna turno entre jogador  1 e  2
- Objetivo é alinhar 3 simbolos na vertical, horizoltal ou diagonal
- Jogo pode ser reiniciado
- Exibe msg quando alguem ganhar ou dar empate
'''

#Cria janela
import tkinter as tk
from tkinter import messagebox
 
# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")
janela.geometry("300x350")
 
# Variável que controla o jogador atual ('X' começa)
jogador_atual = "X"
 
# Lista para guardar os botões (casas do jogo)
botoes = []
 
 
# Função para trocar o jogador depois da jogada
def trocar_jogador():
    global jogador_atual
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
 
 
# Função que verifica se alguém venceu ou deu empate
def verificar_vencedor():
    # Posições ganhadoras possíveis (indices da lista botoes)
    vitoria_possiveis = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]  # diagonais
    ]
 
    for pos in vitoria_possiveis:
        b1 = botoes[pos[0]].cget("text")
        b2 = botoes[pos[1]].cget("text")
        b3 = botoes[pos[2]].cget("text")
        if b1 == b2 == b3 and b1 != "":
            messagebox.showinfo("Fim de jogo", f"O jogador {b1} venceu!")
            bloquear_botoes()
            return True
 
    # Verificar empate (todos preenchidos e ninguém venceu)
    preenchidos = True
    for botao in botoes:
        if botao.cget("text") == "":
            preenchidos = False
            break
    if preenchidos:
        messagebox.showinfo("Fim de jogo", "Deu empate!")
        return True
 
    return False
 
 
# Função que bloqueia os botões quando o jogo acaba
def bloquear_botoes():
    for botao in botoes:
        botao.config(state="disabled")
 
 
# Função para reiniciar o jogo
def reiniciar_jogo():
    global jogador_atual
    jogador_atual = "X"
    for botao in botoes:
        botao.config(text="", state="normal")
 
 
# Função chamada quando clica em um botão (jogar)
def jogar(i):
    global jogador_atual
    if botoes[i].cget("text") == "" and not verificar_vencedor():
        botoes[i].config(text=jogador_atual)
        if not verificar_vencedor():
            trocar_jogador()
 
 
# Criar botões e posicionar na janela com grid
for i in range(9):
    botao = tk.Button(janela, text="", font=("Arial", 24), width=5, height=2,
                      command=lambda i=i: jogar(i))
    botao.grid(row=i // 3, column=i % 3)
    botoes.append(botao)
 
# Botão para reiniciar o jogo
botao_reiniciar = tk.Button(janela, text="Reiniciar", font=("Arial", 14), command=reiniciar_jogo)
botao_reiniciar.grid(row=3, column=0, columnspan=3, sticky="nsew")
 
# Executar a janela
janela.mainloop()





