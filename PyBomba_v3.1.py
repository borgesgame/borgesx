#---------------------------------------------------------------------#
#       Jogo PyBomba                                                  #
#       Python 3.8.1 08-06-2021 Renan Borgesx                         #  
#---------------------------------------------------------------------#
'''
Releases

2021-06-12 add dicas de celulas suspeitas.
2021-06-12 add instrucoes do jogo.
2021-06-12 add maior_pontuacao do jogador.
2021-06-13 ajuste na dificuldade.
2021-06-14 correcao bug na pontuacao nao registrada.
2021-06-14 correcao bug da jogada " X" aceita.
2021-06-14 add aumento e progressao de fases.

'''
import os
import time
import random

def pyBomba():  
    
    escolha = -1
    partida = 0
    max_pts = 0
    pts = 0
    max_level = 3

    # menu de opções
    while escolha != "0":       
        print("\n    >>>>>>>        PyBomba       <<<<<<<\n")
        print("Max. Pontuação   : "+str(max_pts)+" Pts")
        print("Nvl  Desbloqueado: "+str(max_level -1)+" Fase")
        print("Qtd. Partidas    : "+str(partida)+" Jogadas")
        print("\nOpções [1] [2] ou [0] para Sair.\n")        
        print("[1] Jogar")
        print("[2] Ver instruções")
        print("[0] Sair")
        escolha = input("\n   > Vamos lá, escolha uma opção: ")

        while escolha not in ("0","1","2"):
            escolha = input("    > Oops! Opção Inválida 1, 2 ou 0?: ")

        if escolha == "2":
            os.system('clear')
            print("Instruções:\n")
            print("#1 Escolha células livre de bombas.")            
            print("#2 Siga as [Dicas :] quando houver.")
            print("#3 Evite as células [*] suspeitas.")
            print("#4 Desbloqueie muitas - Fases x - .")
            print("#5 Faça o máximo de pontos ;-)")
            print("\n")

        elif escolha == "1":
            os.system('clear')
            fase = 1
            count = 0
            pts= 0

            # loop da fase
            while fase < max_level and count == ( fase ** 2 -1 ):

                fase = fase + 1

                print("\n\n\n\t\t- FASE "+str(fase-1)+" -")
                time.sleep(3)
                os.system('clear')

                x = gera_campo_minado(fase)
                
                # incluindo o campo sorteado
                bum_l = random.randrange(0,fase)
                bum_c = random.randrange(0,fase)

                count = 0
                fim = False
                jogada = ""
                ctrl = 2
                msg = ""

                # célula com bomba
                bl = x[bum_l][bum_c]
                
                status = "Status: ( Boa Sorte! )\n"
                

                # loop da partida
                while count < ( fase ** 2 -1 ) and fim == False:            
                    
                    # exibe tela do jogo
                    msg, ctrl  = exibe_tela(status, pts, count, fase, max_level, x, bl, msg, ctrl )
                    jog_invalida = True
                    loop_jogada = True

                    # loop da jogada
                    while loop_jogada == True:
                        
                        # capta jogada do jogador
                        '''print(bl)'''
                        jogada = input("\n\n> Escolha : ")
                        
                        # teste se jogada acertou a bomba
                        if str(jogada) == str( x[bum_l][bum_c]):
                            loop_jogada = False
                            jog_invalida = False
                            fim = True
                            status =  "Status: ( Bumm! Célula "+str(jogada)+" tem Bomba! )\n"                    				
                            for l in range(fase):
                                    for c in range(fase):
                                            if str(jogada) != str(x[l][c]):
                                                    x[l][c] = " X"
                            ctrl = 0
                            msg = ""
                            msg, ctrl  = exibe_tela(status, pts, count, fase, max_level, x, bl, msg, ctrl )
                            
                        # testar se jogada e valida                  
                        elif str(jogada) != str( x[bum_l][bum_c]):
                            for l in range(fase):
                                    for c in range(fase):
                                            if str(jogada) != " X" and str(jogada) == str(x[l][c]):
                                                    x[l][c] = " X"
                                                    jog_invalida = False

                            if  jog_invalida == True or str(jogada) == " X":                        
                                status = "Status: ( Célula "+str(jogada)+" Inválida! )\n"
                                ctrl = 1
                                msg, ctrl  = exibe_tela(status, pts, count, fase, max_level, x, bl, msg, ctrl )
                                
                                
                            else:      
                                status = "Status: ( Célula "+str(jogada)+" Verificada )\n"
                                count = count + 1		
                                pts = pts + 100
                                loop_jogada = False
                                
                                if pts > max_pts: # registra maior pontuacao
                                    max_pts = pts
                                

                            
                    # chcagem de andamento do jogo
                    
                    if fim == True or count == (fase ** 2 -1):
                        
                        if count == (fase ** 2 -1) and fase == max_level:
                            os.system('clear')
                            partida = partida + 1
                            print("\n\n\tParabens Voce Ganhou !! \n\n")
                            
                            if (fase -1) == 5:
                                print(">>>\tFim do Jogo !!!\n\nVoce atingiu a pontuação máxima \n\t- "+str(pts)+" pts")
                                print("\n\nPrint a Tela, registre esse momento, \n\tate a proxima ;-)")
                                print("\n\n\n>>> reiniciando em 60 segundos. ;-)")
                                time.sleep(60)
                                os.system('clear')
                            else:                                
                                print("\tFASE "+str(fase)+" [ desbloqueada ] \n\n")
                                time.sleep(2)
                                status = "Status: ( Area 100% Verificada )\n"
                                msg=" PyBomba - Borgesx 2021 \n\n Aguarde ...\n\n >>>>>>> Iniciando novamente \n\n (Sua pontuação sera mantida)"
                                ctrl = 0
                                msg, ctrl  = exibe_tela(status, pts, count, fase, max_level, x, bl, msg, ctrl )
                                time.sleep(7)
                                os.system('clear')
                                fase, count= 1, 0
                                max_level = max_level + 1                           
                        
                        else:
                            if count == (fase ** 2 -1 ) and fase < max_level:
                                fim = True
                                os.system('clear')
                                print("\n\n\n    >>>>>>> MISSAO "+str(fase-1)+" CONCLUÍDA <<<<<<<")
                                time.sleep(1)                

                            else:
                                partida = partida + 1
                                print("\n\n\tVocê Perdeu !! \n\n\tFim do Jogo\n\n")
                                print("[1] Jogar Novamente")
                                print("[0] Voltar ao Menu de Opções")                                
                                dinovo = input("\n\n> Digite 1 ou 0 :")

                                while dinovo not in ['1','0']:
                                    dinovo = input("  > Opcao invalida! Digite 1 ou 0 :")

                                if dinovo == '0' :
                                    os.system('clear')                                    
                                else:
                                    os.system('clear')
                                    fase, count, pts = 1, 0, 0
       
        else:
            print("\nAté a proxima :-) \n\n\n!!!\n\n\n")
            exit()


def exibe_tela( status, pts, count, fase, max_level, x, bl, msg, ctrl ):
        
    # exibicao principal do jogo    
    os.system('clear')
    print(status)
    print("PyBomba  Fase: "+str(fase-1)+" de "+str(max_level-1)+"  Pontuacao: "+str(pts)) 
    for l in range(fase):
        print("\n", end="")
        for c in range(fase):
            print("[ "+str(x[l][c])+" ] ",end="")

    if ctrl == 1:
        print("\n\nTente novamente\n")
        ctrl = 0
    elif ctrl == 2 and count >= random.randrange(1,(fase ** 2)):
        msg = dica_jogo(bl)
        print("\n\n"+msg+"\n")
        ctrl = 0
    else:
        print("\n\n"+msg+"\n")

    return msg, ctrl 

            

def gera_campo_minado(fase):

    # gera células sem repetir    
    lista = []
    x = []

    while len(lista) < (fase ** 2):
        n = random.randrange(10,99) 
        if n not in lista:
            lista.append(n)

    while len(lista) != 0:
        x.append(lista[:fase])
        lista = lista[fase:]

    return x

def dica_jogo(bl):

    # retorna uma dica util para o acerto de celulas
    
    msg =["[Dica :]\n Cuidado, bomba onde resto da divisao de [*] por 2 é igual a "+str(bl%2)+"."
           ,"[Dica :]\n Suspeita de bomba onde resto da divisao de [*] por 2 é igual a "+str(bl%2)+"."
           ,"[Dica :]\n Cuidado, bomba onde resto da divisao de [*] por 3 é igual a "+str(bl%3)+"."
           ,"[Dica :]\n Suspeita de bomba onde o resto da divisao de [*] por 3 é igual a "+str(bl%3)+"."
           ,"[Dica :]\n Cuidado, bomba onde resto da divisao de [*] por 5 é igual a "+str(bl%5)+"."
           ,"[Dica :]\n Suspeita de bomba onde o resto da divisao de [*] por 5 é igual a "+str(bl%5)+"."
           ,"[Dica :]\n Cuidado, bomba pode estar onde [*] é menor que "+str(bl+random.randrange(1,bl))+"."
           ,"[Dica :]\n Cuidado, bomba pode estar onde [*] é maior que "+str(bl-random.randrange(1,bl))+"."
           ,"[Dica :]\n Cuidado, bomba pode estar onde [*] é menor que "+str(bl+random.randrange(1,bl))+"."
           ,"[Dica :]\n Cuidado, bomba pode estar onde [*] é maior que "+str(bl-random.randrange(1,bl))+"."
           ,"[Dica :]\n Fontes seguras afirmam que a bomba esta onde [*] representa + ou - "+str(int((bl/300)*100))+"% de 300."
           ,"[Dica :]\n A bomba pode estar onde [*] representa + ou - "+str(int((bl/150)*100))+"% de 150."
           ,"[Dica :]\n Suspeita de bomba onde [*] representa + ou - "+str(int((bl/200)*100))+"% de 200."
           ]
    
    return msg[random.randrange(0,len(msg))]

pyBomba()
