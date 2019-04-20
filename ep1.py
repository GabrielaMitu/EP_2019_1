# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriela Yukari Mitu, gabrielaym@al.insper.edu.br
# - aluno B: Gabriella Escobar Cukier, gabriellaec@al.insper.edu.br

horas=10
dinheiro=0
armas=[]
presentes=[]
aliados=[]
def carregar_cenarios():
    cenarios = {
        "Terraço (o início da aventura)": {
            "título": "Super Terraço do Prédio Novo",
            "descricao": "Você está no terraço gigante do segundo prédio do Insper",
            "opcoes": {
                "Escadas": "Descer para o quinto andar de escadas",
                "Elevador": "usar o elevador para descer"
            }
        },
        "Quinto andar": {
            "titulo": "Andar para refletir",
            "descricao": "o quinto andar não tem muitas coisas para fazer"
                         "então vamos refletir",
            "opcoes": {
                "Escadas": "fugir para o quarto andar" 
            }
        },
        "Quarto andar": {
            "titulo": "Andar da fuga",
            "descricao": "um pouco de sossego nesse andar",
            "opcoes": {
                "Terceiro andar": "Ir direto para o FabLab"
                                  "no terceiro andar para construir armas"
            }
        },
        "Terceiro andar": {
            "titulo": "o melhor andar!!",
            "descricao": "Aqui se encontra o famoso FabLab, lar de muitos"
                       "engenheiros, onde tudo pode ser construído!!"
                       "E a grandiosa máquina de café para dar"
                       "aquela turbinada!!",
            "opcoes": {
                "FabLab": "vamos construir!!",
                "Máquina de café": "comprar café",
                "Segundo andar": "ir para o andar do tobogã"
            }
        },
        "Máquina de café": {
            "titulo": "maquininha de café gostoso",
            "descricao": "muuuito café para comprar",
            "opcoes": {
                "comprar café": "2 reais",
                "não comprar café": "muito caro! Não tenho esse dinheiro",
            }
        },
        "FabLab": {
            "titulo": "melhor sala para futuros engenheiros!!",
            "descricao": "Aqui se encontra a super impressora 3D avançada"
                         "do Insper, mas prenda o cabelo para utilizá-la!!",
            "opcoes": {
                "Impressora 3D": "usar impressora 3D super avançada",
                "Terceiro andar": "corredor",
                "Ah não": "Me recuso a prender o cabelo!"
            }
        },            
        "Professor do lab": {
            "titulo": "Professor do FabLab",
            "descricao": "O professor insiste para você prender o cabelo,"
                         "mas você continua recusando!"
                         "Ele se torna um monstro!!",
            "opcoes": {
                "lutar": "se lutar ganha 2 reais!",
                "fugir": "prefiro prender o cabelo",
            }
        }, 
        "Impressora 3D": {
            "titulo": "uma bela máquina",
            "descricao": "Essa máquina pode fazer armas!!,",
            "opcoes": {
                "Martelo feito na impressora 3D: amassa o computador inimigo': 'leva 2 horas para fazer, mas é potente',
                "Imprimir cupcakes":"presentes podem te ajudar a fazer aliados",
                "FabLab": "voltar para a sala dos engenheiros",
            }
        },
        "Segundo andar": {
            "titulo": "o andar do tobogã",
            "descricao": "O tobogã hoje magicamente te teletransporta"
                         "para o prédio antigo do Insper!! Mágico!!"
                         "Porém custa 2 reais",
            "opcoes": {
                "usar tobogã": "te teletransporta para o prédio antigo do Insper, mas custa 2 reais",
                "Voltar para o terceiro andar": "retornar e matar um monstro"
        }
    },
    "Biblioteca": {
        "titulo":
        "descrição: 
        "opcoes": {
            "compultador": "consultar para achar livros",
            "bibliotecários": "perguntar onde os livros estão"
        }        
    },
     "Computador": {
            "titulo": "",
            "descricao": "",
                         
            "opcoes": {
                "Lutar contra o programa que localiza livros": "você pode encontrar o manual de construção da máquina do tempo, mas isso irá te custar uma hora",
                "Fugir": "sair correndo para a biblioteca",
        }
    },
     "Pessoa": {
            "titulo": "",
            "descricao": "",
            "opcoes": {
                "Lutar": "Você pode conquistar o manual de instruções para a máquina do tempo, mas isso irá te custar uma hora",
                "Fugir": "Sair correndo para a biblioteca",
        }
    },
   "Nerdbox": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Abrir manual": "desvendar todos os segredos da máquina do tempo",
        }
    },
    "Manual": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Pegar os elevadores": "vamos encontrar o que é necessário para construir a máquina do tempo! yayy!",
        }
    },
    "Elevadores": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Ir para o quarto andar": "contém os segredos da engenharia",
            "Ir para o segundo andar": "o help desk sempre pode te ajudar!"
            "Ir para o décimo primeiro andar": "etapa final do projeto! É aconselhável você visitar os outros andares antes"
        }
    },
    "Segundo andar": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Luta": "podem ser fofos, mas mesmo assim são monstros! e você ganhará dois reais",
            "Amizade": "faça um novo amigo e ainda ganhe um aliado para a construção!"
            "Fuga": "corra até o elevador!"
        }
    },
    "Quarto andar": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Laboratório de InstruMed": "ache circuitos e instrumentos para a construção",
            "Materiais": "são importantes para a máquina!",
            "Sala 401": "aula de DeSoft: você vai virar um mestre em programação, mas vai levar 2 horas" ,
            "Fuga":"pegue o elevador para outros andares",
            "Máquina de café":"um cafezinho é sempre bom para acordar"
        }
    },
    "Materiais": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Pegar materiais": "pegue o que precisa e volte para a entrada do quarto andar",
        }
    },
    "Laboratório de InstruMed": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Material": "pegar o que precisa para o circuito da máquina",
            "Voltar para a entrada": "volte para a entrada do quarto andar",
        }
    },
    "Sala 401": {
        "titulo":
        "descrição: 
        "opcoes": 
            "Assistir aula": "Aprenda tudo que você precisa para programar a sua máquina do tempo" ,
            "Fugir":"voltar para a entrada do quarto andar"
        }
    },
    "Aula": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Sair da sala": "volte para a entrada do quarto andar",
        }
    },
     "Décimo primeiro andar": {
        "titulo":
        "descrição: 
        "opcoes": {
            "Construir a máquina do tempo": "volte no tempo e tire A+ no EP (ou retorne a uma época em que computadores ainda não existiam)",
            "Voltar ao elevador": "encontre o material necessário para construir sua máquina" 
        }
    },
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Você acordou no Terraço do prédio novo do Insper depois de beber muito no dia anterior porque foi muito mal nas PIs e tem o trabalho inteiro de DesSoft para fazer para o dia seguinte.")
    print()
    print("Não vai dar tempo de fazer o trabalho para amanhã. Porém, há uma solução! Você deve construir uma máquina do tempo e voltar para o passado, podendo, assim, fazer o trabalho com calma")
    print()
    print('Faltam 10 horas para a entrega do EP. \Mas cuidado! O tempo é relativo e você pode perder algumas horas com obstáculos ou derrotas em combates!')
    print()
    print('Além disso, você gastou todo o seu dinheiro em bebidas e agora está pobre, sem dinheiro na carteira')


    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        
        print(cenario_atual)

        
        
        
        opcoes = "Suas opções são: " cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
             opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True

        else:
            for lugar, resumo in opcoes.items():
                print('-' + lugar + ": " + resumo)
            
            escolha = input("O que vai fazer? ")
            if escolha in opcoes:
                nome_cenario_atual=escolha
                
        #no terraco
                if escolha == 'Escadas':
                    nome_cenario_atual = "Quarto andar"
                    
        #na maquina de cafe    
                elif escolha == 'Comprar café':
                    if dinheiro >= 2:
                        dinheiro-=2
                        horas+=2
                        print('Você gastou 2 reais')
                        print('Mas está mais acordado e ganhou tempo!')
                        print('Você tem mais duas horas!')
                        print('Restam {0} horas'.format(horas))
                        print('Você agora tem {0} reais'.format(dinheiro))
                        nome_cenario_atual = "Terceiro andar"
                    else:
                        print('Você não pode pagar isso!')
                        print('Que pena! Você morreu!')
                        print('Zerou o EP e está de DP')
                        game_over = True
                elif escolha == "Não comprar café":
                    nome_cenario_atual = "Terceiro andar"
                
     #impressora 3d
                elif escolha == "Martelo" or escolha == "Carrinho":
                    armas.append(escolha)
                    for a in armas:
                        print('Você possui agora: ' + a)
                    print('Você está retornando ao FabLab')
                    nome_cenario_atual = "FabLab"
                elif escolha == 'Cupcakes':
                    presentes.append(escolha)
                    for p in presentes:
                        print('Você possui agora: ' + p)
                    print('Você está retornando ao FabLab')
                    nome_cenario_atual = "FabLab"
                elif escolha == 'Fugir pro Lab':
                    nome_cenario_atual = "FabLab"

                        
###########                
            # ah nao:
                elif escolha == "Lutar contra monstro do Lab":
                        if len(armas) == 0:
                            print('Você não tem nenhuma arma para lutar!')
                            print('O monstro te devorou!')
                            game_over = True
                            
                        else:
                            arma_escolhida=input('Qual arma você quer usar?  ')
                            if arma_escolhida in armas:
                                if arma_escolhida == 'Martelo':
                                    dinheiro+=4
                                    print('Parabéns! Você venceu!')
                                    print('A insper está grata')
                                    print('Por isso você ganhou 4 reais!')
                                    print('Você agora tem {0} reais'.format(dinheiro))
                                    nome_cenario_atual = "FabLab"

                                    
                                elif arma_escolhida == 'Carrinho':
                                    dinheiro+=3
                                    print('Parabéns! Você venceu!')
                                    print('A insper está grata')
                                    print('Por isso você ganhou 3 reais!')
                                    print('Você agora tem {0} reais'.format(dinheiro))
                                    nome_cenario_atual = "FabLab"
                                
                            else:
                                    print('Você não tem essa arma')
                                    print('Está perdido demais, nem sabe o que tem')
                                    print('Não vai entregar o EP e está de DP!')
                                    game_over = True
                elif escolha == 'Fugir pro Lab':
                        nome_cenario_atual == "FabLab"
                        
            # segundo andar
                elif escolha == 'Teletransporte':
                    if dinheiro >= 2:
                        dinheiro-=2
                        horas+=4
                        print('Você gastou 2 reais')
                        print('Mas conseguiu trocar de prédio')
                        print('Parabéns, está mais perto de construir a máquina do tempo!')
                        print('Ganhou quatro horas')
                        print('Restam {0} horas'.format(horas))
                        print('Você agora tem {0} reais'.format(dinheiro))
                        nome_cenario_atual = 'Biblioteca'
                    else:
                        print('Você não pode pagar isso!')
                        print('Que pena! Você morreu!')
                        print('Zerou o EP e está de DP')
                        game_over = True
            
        # biblioteca
                elif escolha == "Lutar contra pessoa" or escolha == "Lutar contra o computador":
                        if len(armas) == 0:
                            print('Você não tem nenhuma arma para lutar!')
                            print('O monstro ganhou!')
                            print('Game Over para você...')
                            game_over = True
                        else:
                            arma_escolhida=input('Qual arma você quer usar? ')
                            if arma_escolhida in armas:
                                if arma_escolhida == 'Martelo':
                                    horas-=2
                                    print('Parabéns! Você venceu!')
                                    print('Ganhou o manual')
                                    print('Mas demora para achar os livros...')
                                    print('Você perdeu duas horas')
                                    print('Restam {0} horas'.format(horas))
                                    nome_cenario_atual = 'Nerdbox'

                                elif arma_escolhida == 'Carrinho':
                                    horas-=3
                                    print('Parabéns! Você venceu!')
                                    print('Ganhou o manual')
                                    print('Mas demora para achar os livros...')
                                    print('Você perdeu três horas')
                                    print('Restam {0} horas'.format(horas))
                                    nome_cenario_atual = 'Nerdbox'
                            else:
                                print('Você não tem essa arma')
                                print('Está perdido demais, nem sabe o que tem')
                                print('Não vai entregar o EP e está de DP!')
                                game_over = True
                                
                elif escolha == 'Fugir para a biblioteca':
                        nome_cenario_atual = 'Biblioteca'
                        
                        
                                
    # andar 2
                elif escolha == 'Lutar':
                        if len(armas) == 0:
                            print('Você não tem nenhuma arma para lutar!')
                            print('O monstro ganhou!')
                            print('Game Over para você...')
                            game_over = True
                        else:
                            arma_escolhida=input('Qual arma você quer usar? ')
                            if arma_escolhida in armas:
                                if arma_escolhida == 'Martelo':
                                    dinheiro+=3
                                    horas-=1
                                    print('Parabéns! Você venceu!')
                                    print('Ganhou três reais!')
                                    print('Mas perdeu uma hora no combate')
                                    print('Restam {0} horas'.format(horas))
                                    print('Você agora tem {0} reais'.format(dinheiro))
                                    nome_cenario_atual = 'Elevadores'
  
                                elif arma_escolhida == 'Carrinho':
                                    horas-=1
                                    dinheiro+=2
                                    print('Parabéns! Você venceu!')
                                    print('Ganhou dois reais!')
                                    print('Mas perdeu uma hora no combate')
                                    print('Restam {0} horas'.format(horas))
                                    print('Você agora tem {0} reais'.format(dinheiro))
                                    nome_cenario_atual = 'Elevadores'
                            else:
                                print('Você não tem essa arma')
                                print('Está perdido demais, nem sabe o que tem')
                                print('Não vai entregar o EP e está de DP!')
                                game_over = True
                elif escolha == 'Amigos':
                        if len(presentes) == 0:
                            print('Você não tem nenhum presente para dar!')
                            print('O monstro não gostou de você!')
                            print('Por isso, te devorou...')
                            game_over = True
                        else:
                            
                            requisitos.append('Aliado')
                            print('O monstro adorou seu presente!')
                            print('Você ganhou um aliado!')
                            nome_cenario_atual = 'Elevadores'
                elif escolha == 'Fugir':
                        nome_cenario_atual = 'Elevadores'
            # desoft
                elif escolha == "Aula":
                    requisitos.append('Programação')
                    horas-=2
                    print('Eba! Agora você já sabe programar')
                    print('Pode usar isso na sua máquina do tempo')
                    print('Mas a aula levou duas horas')
                    print('Restam {0} horas'.format(horas))
                    nome_cenario_atual = "Aula"
              
                
            #materiais
                elif nome_cenario_atual == "Materiais":
                    requisitos.append('Materiais')
                    nome_cenario_atual = "Materiais"
                    
                
            # ultima fase
                elif escolha == "Construir a máquina do tempo":
                    if 'Materiais' and 'Programação'and 'Aliado' in requisitos:
                        print('Parabéns!')
                        print('Você construiu sua máquina do tempo!')
                        print('Agora volte para o passado e termine seu EP!')
                    else:
                        print('Você não tem os requisitos necessários...')
                        print('O que você tem agora é: ')
                        for r in requisitos:
                            print(r)
                        final=['voltar para os elevadores', 'desistir']
                        print('Você pode: {0} ou {1}'.format(final[0],final[1]))
                        escolha=input('O que quer fazer? ')
                        if escolha in final:
                            if escolha == 'voltar para os elevadores':
                                nome_cenario_atual = 'Elevadores'
                            else:
                                print('Foi por pouco...')
                                print('Você perdeu...')
                                game_over= True
                        else:
                            print('Você está indeciso demais!')
                            print('Foi por pouco...')
                            print('Você perdeu...')
                            game_over= True
            else:
                print('Sua indecisão foi sua ruína!')
                print('Zerou o EP e está de DP')
                game_over= True

main()
