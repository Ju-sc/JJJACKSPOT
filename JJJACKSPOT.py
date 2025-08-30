import random
import numpy as np
import keyboard
import time
import os
import msvcrt
import emoji



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpatecld():
    while msvcrt.kbhit():
        msvcrt.getch()


def credito(investimento_jogador):
    
    while True:
        
        print("===========================================")
        print("   →     🪙 " " 1 crédito = 💰 R$ 2 " "     ←")
        print("===========================================")
        saldo_str = input ("\nInsira a quantidade de saldo desejado: ")
        limpar_tela()
        try:
            saldo_int = int(saldo_str)
            if saldo_int <0:
                print ("❌", " Valor inválido, O valor inserido foi negativo. ", "❌")
            investimento_jogador += saldo_int 
            if (saldo_int % 2 == 0) and (saldo_int > 0):
                print("♠️—————————————————♦️")
                print (f"  Valor aceito: {saldo_int}")
                print("♠️—————————————————♦️")
                return saldo_int, investimento_jogador
            else:
                print("🔢"" Só serão aceitos valores pares. Ex: 2, 10, 200. " "🔢")
                time.sleep(2)
                limpar_tela()

        except ValueError:
            print ("❌"" Insira um valor válido. ""❌")
            time.sleep(2)
            limpar_tela()
         

dnv = True
jogou = 0
investimento_jogador = 0
ganhostotais = 0
jogou_vlrfinal = 0
saldo_jogador = 0
qtdJogada = 0
sorte = 0
limpar_tela()
print(f"╔═══════════════════╗")
print("\033[1m   ♠️ BEM VINDO! ♥️\033[0m")
print("  \033[1m♣️ AO JJJACKSPOT ♦️\033[0m")
print(f"╚═══════════════════╝")
time.sleep(0.8)
limpar_tela()

print(f"╔═══════════════════╗")
print("\033[1m   ♦️ BEM VINDO! ♣️\033[0m")
print("  \033[1m♠️ AO JJJACKSPOT ♥️\033[0m")
print(f"╚═══════════════════╝")
time.sleep(0.8)
limpar_tela()

print(f"╔═══════════════════╗")
print("\033[1m   ♥️ BEM VINDO! ♠️\033[0m")
print("  \033[1m♦️ AO JJJACKSPOT ♣️\033[0m")
print(f"╚═══════════════════╝")
time.sleep(0.8)
limpar_tela()

while (dnv == True):
    sorte = random.randint(6,12)
    confirmado = True
    saldo_jogador, invstjogador = credito(investimento_jogador)
    qtdcred = saldo_jogador / 2
    jogousorte = 0
    text = "{:.1f}".format(qtdcred)
    if text.endswith(".0"):
        text = text[:-2]
        print(f"╔═══════════════════╗")
        print("‖  🪙 " f" Créditos: {text} ‖ ")
        print(f"╚═══════════════════╝")
        qtdJogada = int(qtdcred)
    
    while qtdJogada > 0:
        print("Pressione a tecla ENTER para continuar ou ESC para encerrar...")

        while True:
            limpatecld()
            eventotecld = keyboard.read_event()
            if eventotecld.event_type == keyboard.KEY_DOWN:
                tecla = eventotecld.name
                break

        time.sleep(0.2)
        if tecla == 'enter':
            limpar_tela()
            jogou += 1
            jogousorte += 1
            ranvet = []
            qtdJogada -= 1
            print("\nJogadas restantes", qtdJogada)
    
            for i in range(0,9):
                rans = random.randrange(0, 9)
                ranvet.append(rans)
            matriznumpy = np.array(ranvet).reshape(3, 3)
            ran = matriznumpy
            print (jogousorte)
            print(sorte)

            if jogousorte == sorte:
                print("♥️———————————♣️")
                for i,linha in enumerate(ran):
                    print(f"│ { ' │ '.join(map(str, linha)) } │", end='')
                    if i == 0:
                        print(" ")
                        print("♥️———————————♣️")
                    elif i == 1:
                        print("\n♥️———————————♣️",end='')
                        print("⏕¶")
                    else:
                        print(" ‖\n♦️———————————♠️ ‖\n             🔴")
                print("")
                ran[1][1] = ran[1][0]
                ran[1][2] = ran[1][0]
                print ("\n🃏" "\033[1mJ A C K P O T\033[0m" "🃏")
                ganhostotais += 20
                jogousorte = 0
                sorte = random.randint(6,12)
            else:
                print("♥️———————————♣️")
                for i,linha in enumerate(ran):
                    print(f"│ { ' │ '.join(map(str, linha)) } │", end='')
                    if i == 0:
                        print(" ")
                        print("♥️———————————♣️")
                    elif i == 1:
                        print("\n♥️———————————♣️",end='')
                        print("⏕¶")
                    else:
                        print(" ‖\n♦️———————————♠️ ‖\n             🔴")
                print("")

                if ran[1][0] == ran[1][1] == ran[1][2]:
                    print ("\n🃏" "\033[1mJ A C K P O T\033[0m" "🃏")
                    sorte = random.randint(6,12)
                    ganhostotais += 20
                    jogousorte = 0
                    
                    
                if ran[0][2] == ran[1][1] == ran[2][0]:
                    print("\n " " 🥳BÔNUS! GANHOU DEZ RODADAS! " " 🥳")
                    qtdJogada += 10
                    

                if ran[0][0] == ran[1][1] == ran[2][2]:
                    qtdJogada += 10
                    print("\n " " 🥳BÔNUS! GANHOU DEZ RODADAS! " " 🥳")
                    
                if qtdJogada <= 0:
                    while confirmado == True:
                        limpatecld()
                        JogarDnv = input("Deseja jogar denovo?(s-n)").lower()
                        if (JogarDnv == "sim") or (JogarDnv == "s"):
                            print("\nEntão vamos lá de novo! 🕺")
                            dnv = True
                            confirmado = False
                        elif (JogarDnv == "não") or (JogarDnv == "nao") or (JogarDnv == "n"):
                            dnv = False
                            confirmado = False
                            limpar_tela()
                            print(f"╔═══════════════════════════╗")
                            print(f"  🎰 jogou: {jogou}")
                            print(f"  🤑 total ganho no jogo: {ganhostotais}")
                            print(f"╚═══════════════════════════╝")
                            print("\nObrigado por jogar e volte sempre!")
                            exit()
                        else:
                            print("\nInformação inválida, tente novamente\n")
        elif tecla == 'esc':
            print("Jogo encerrado.\n")    
            print(f"╔═══════════════════════════╗")
            print(f"  🎰 jogou: {jogou}")
            print(f"  🤑 total ganho no jogo: {ganhostotais}")
            print(f"╚═══════════════════════════╝")
            
            exit()         
        else:
            print("Inválido tente novamente.\n")

