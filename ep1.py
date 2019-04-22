# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriela Yukari Mitu, gabrielaym@al.insper.edu.br
# - aluno B: Gabriella Escobar Cukier, gabriellaec@al.insper.edu.br
import random

def carregar_cenarios():
    cenarios = {
        "Terraço (o início da aventura)": {
            "titulo": "Super Terraço do Prédio Novo",
            "descricao": "Você está no terraço gigante do prédio "
                         "novo do Insper",
            "opcoes": {
                "Escadas": "Descer para o quinto andar de escadas",
            }
        },
        "Quarto andar do prédio novo": {
            "titulo": "Andar da fuga",
            "descricao": "um pouco de sossego nesse andar",
            "opcoes": {
                "Terceiro andar": "Ir direto para o FabLab "
                                  "no terceiro andar para construir armas"
            }
        },
        "Terceiro andar do prédio novo": {
            "titulo": "o melhor andar!!",
            "descricao": "Aqui se encontra o famoso FabLab, lar de muitos "
                       "engenheiros, onde tudo pode ser construído!! "
                       "E a grandiosa máquina de café para dar "
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
            "descricao": "Aqui se encontra a super impressora 3D avançada "
                         "do Insper, mas prenda o cabelo para utilizá-la!!",
            "opcoes": {
                "Impressora 3D": "usar impressora 3D super avançada",
                "Terceiro andar": "corredor",
                "Ah não": "Me recuso a prender o cabelo!"
            }
        },            
       "Ah não": {
            "titulo": "Professor do FabLab",
            "descricao": "O professor insiste para você prender o cabelo, "
                         "mas você continua recusando! "
                         "Ele se torna um monstro!!",
            "opcoes": {
                "Lutar": "Lutar contra monstro do Lab":,
                "Fugir": "prefiro prender o cabelo",
            }
        }, 
        "Impressora 3D": {
            "titulo": "Uma bela máquina",
            "descricao": "Essa máquina pode fazer armas!!",
            "opcoes": {
                "Martelo": "Corta o inimigo (leva 2 horas para fazer, mas é potente)",
                "Carrinho": "atropela o inimigo (leva 1 hora para fazer)",
                "Cupcakes":"presentes podem te ajudar a fazer aliados",
                "FabLab": "voltar para a sala dos engenheiros",
            }
        },
        "Segundo andar do prédio novo": {
            "titulo": "O andar do tobogã",
            "descricao": "O tobogã hoje magicamente te teletransporta "
                         "para o prédio antigo do Insper!! Mágico!! "
                         "Porém custa 2 reais",
            "opcoes": {
                "usar tobogã": "te teletransporta para o prédio antigo do Insper, mas custa 2 reais",
                "Voltar para o terceiro andar": "retornar e matar um monstro"
        }
    },
    "Biblioteca": {
            "titulo": "Há todos os tipos de livros aqui!!",
            "descricao": "Procure o manual!!",
        "opcoes": {
            "Computador": "consultar para achar livros",
            "Pessoa": "perguntar onde os livros estão"
        }        
    },
    "Computador": {
            "titulo": "O computador misterioso da biblioteca",
            "descricao": "você tenta procurar o manual pelo pc, "
                         "mas ele não mostra a localização do manual. "
                         "Você fica com raiva e chuta o computador. "
                         "Ele revela ser um monstro disfarçado "
                         "e tenta te matar",                        
            "opcoes": {
                "Lutar contra o programa que localiza livros": "você pode encontrar o manual de construção da máquina do tempo, mas isso irá te custar uma hora",
                "Fugir": "sair correndo para a biblioteca",
        }
    },
      "Pessoa": {
            "titulo": "A pessoa da biblioteca",
            "descricao": "Você pergunta sobre a localização do manual, "
                         "mas ela nega dar a informação para você. "
                         "Você insiste. "
                         "Ela revela ser um monstro disfarçado "
                         "e tenta te matar",
            "opcoes": {
                "Lutar": "Você pode conquistar o manual de instruções para a máquina do tempo, mas isso irá te custar uma hora",
                "Fugir": "Sair correndo para a biblioteca",
        }
    },
    "Nerdbox": {
        "titulo": "Paraíso dos estudiosos",
        "descricao": "Aqui você encontra sossego!! "
                     "O melhor lugar de estudos do Insper!!",
        "opcoes": {
            "Manual": "desvendar todos os segredos de como construir a máquina do tempo",
        }
    },
     "Manual": {
        "titulo": "Manual da salvação",
        "descricao": "Nele, são revelados os materiais, a programação "
                     "e que é nessário ao menos um aliado "
                     "para a construção da máquina",
        "opcoes": {
            "Elevador do prédio velho": "vamos encontrar o que é necessário para construir a máquina do tempo! yayy!",
        }
    },
     "Elevador do prédio velho": {
        "titulo": "Elevador da felicidade",
        "descricao": "Os elevadores desse prédio estão funcionando!! Yaayy!", 
        "opcoes": {
            "Ir para o quarto andar": "contém os segredos da engenharia",
            "Ir para o segundo andar": "o help desk sempre pode te ajudar!",
            "Ir para o décimo primeiro andar": "etapa final do projeto! É aconselhável você visitar os outros andares antes"
        }
    },
    "Segundo andar do prédio velho": {
        "titulo": "O andar peculiar",
        "descricao": "Meu deus!! Tem muitos monstros no HelpDesk!! "
                     "Mas por algum motivo, eles são fofos...",
        "opcoes": {
            "Lutar": "podem ser fofos, mas mesmo assim são monstros! Você ganhará ainda dois reais",
            "Amigos": "Faça um novo amigo e ainda ganhe um aliado para a construção!",
            "Fugir": "Corra até o elevador!"
        }
    },
    "Quarto andar do prédio velho": {
        "titulo": "O famoso andar dos engenheiros do prédio velho",
        "descricao": "Mãos a obra!!",
        "opcoes": {
            "Laboratório de InstruMed": "ache circuitos e instrumentos para a construção",
            "Materiais": "são importantes para a máquina!",
            "Aula": "aula de DeSoft: você vai virar um mestre em programação, mas vai levar 2 horas" ,
            "Fuga":"pegue o elevador para outros andares",
            "Máquina de café":"um cafezinho é sempre bom para acordar"
        }
    },
    "Materiais": {
        "titulo": "Materiais essenciais para a construção da máquina",
        "descricao": "Você tenta pegar os materiais, "
                    "mas havia um monstro escondido ali",
        "opcoes": {
            "Pegar materiais": "pegue o que precisa e volte para a entrada do quarto andar",
        }
    },
    "Laboratório de InstruMed": {
        "titulo": "O laboratório popular dos engenheiros",
        "descricao": "Muitos instrumentos aqui, um ótimo lugar para "
                    "fazer experimentos e cicuitos elétricos!! "
                    "Mas sempre tem relatório!!",
        "opcoes": {
            "Material": "pegar o que precisa para o circuito da máquina",
            "Voltar para a entrada": "volte para a entrada do quarto andar",
        }
    },
     "Décimo primeiro andar": {
        "titulo": "O andar da vitória",
        "descricao": "Há um terraço bastante espaçoso aqui!! "
                     "Perfeito para construir a máquina do tempo!!",
        "opcoes": {
            "Construir a máquina do tempo": "volte no tempo e tire A+ no EP (ou retorne a uma época em que computadores ainda não existiam)",
            "Voltar ao elevador": "encontre o material necessário para construir sua máquina" 
        }
    }}
    nome_cenario_atual = "Terraço (o início da aventura)"
    return cenarios, nome_cenario_atual


def main():
    horas=10

    dinheiro=2

    armas={}

    presentes={}

    requisitos=[]

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    
    vitoria=False
    
    vidas_jogador = 16


#### add mais monstros
    monstros = {
            "Golem":{
                    "descricao": "",
                    "vida":10, 
                    "dano":5
                            },
            "Jupyter notebook":{
                    "descricao": "",
                    "vida":8, 
                    "dano":8
                    }
            }
            
            
############# add mais perguntas
    conhecimento={"5 primeiros dígitos de pi, sem vírgula":"31415",
              "Capital da Austrália":"Canberra",
              "Capital da Islândia":"Reykjavik",
              "Capital do Acre":"Rio Branco",
              "Capital dos EUA":"Washington",
              "Ano do início da Revolução Francesa":"1789",
              "Ano do fim da Segunda Guerra Mundial":"1945",
              }
    
    
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
        if nome_cenario_atual=="Terraço (o início da aventura)":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("------------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Escadas"])
                  print()
        if nome_cenario_atual=="Quarto andar do prédio novo":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Quarto andar do prédio novo")
                  print("---------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Terceiro andar do prédio novo"])
                  print()
        if nome_cenario_atual=="Terceiro andar do prédio novo":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Terceiro andar do prédio novo")
                  print("-----------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["FabLab"])
                  print(cenario_atual["opcoes"]["Máquina de café"])
                  print(cenario_atual["opcoes"]["Segundo andar"])
                  print()
        if nome_cenario_atual=="Máquina de café":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Máquina de café")
                  print("---------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Comprar café"])
                  print(cenario_atual["opcoes"]["Não comprar café"])
                  print()
        if nome_cenario_atual=="FabLab":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("FabLab")
                  print("------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Impressora 3D"])
                  print(cenario_atual["opcoes"]["Terceiro andar"])
                  print(cenario_atual["opcoes"]["Ah não"])
                  print()                        
        if nome_cenario_atual=="Ah não":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Ah não")
                  print("------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Lutar"])
                  print(cenario_atual["opcoes"]["Fugir"])
                  print()
        if nome_cenario_atual=="Impressora 3D":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Impressora 3D")
                  print("-------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Martelo"])
                  print(cenario_atual["opcoes"]["Carrinho"])
                  print(cenario_atual["opcoes"]["Cupcakes"])
                  print(cenario_atual["opcoes"]["Fugir pro Lab"])
                  print()
        if nome_cenario_atual=="Segundo andar do prédio novo":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Segundo andar do prédio novo")
                  print("----------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Tobogã"])
                  print(cenario_atual["opcoes"]["Terceiro andar do prédio novo"])
                  print()
        if nome_cenario_atual=="Biblioteca":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Biblioteca")
                  print("----------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Lutar contra pessoa"])
                  print(cenario_atual["opcoes"]["Lutar contra o computador"])
                  print(cenario_atual["opcoes"]["Fugir para a biblioteca"])
                  print()
        if nome_cenario_atual=="Nerdbox":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Nerdbox")
                  print("-------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Manual"])
                  print(cenario_atual["opcoes"]["Biblioteca"])
                  print(cenario_atual["opcoes"]["Elevador do prédio velho"])
                  print()
        if nome_cenario_atual=="Manual":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Manual")
                  print("------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print()
        if nome_cenario_atual=="Elevador do prédio velho":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Elevador do prédio velho")
                  print("------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Segundo andar do prédio velho"])
                  print(cenario_atual["opcoes"]["Quarto andar do prédio velho"])
                  print()
        if nome_cenario_atual=="Segundo andar do prédio velho":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Segundo andar do prédio velho")
                  print("-----------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Lutar"])
                  print(cenario_atual["opcoes"]["Amigos"])
                  print(cenario_atual["opcoes"]["Fugir"])
                  print()
        if nome_cenario_atual=="Quarto andar do prédio velho":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Quarto andar do prédio velho")
                  print("----------------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcoes"]["Aula"])
                  print(cenario_atual["opcoes"]["Materiais"])
                  print(cenario_atual["opcoes"]["Laboratório de InstruMed"])
                  print()
        if nome_cenario_atual=="Décimo primeiro andar":
                  cenario_atual=cenarios[nome_cenario_atual]
                  print("Décimo primeiro andar")
                  print("---------------------")
                  print(cenario_atual["titulo"])
                  print(cenario_atual["descricao"])
                  print(cenario_atual["opcao"]["Construir a máquina do tempo"])
                  print(cenario_atual["opcao"]["Elevador do prédio velho"])
                  print()
                        
        #print(cenario_atual)

        
        
        
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
                    nome_cenario_atual="Quarto andar do prédio novo"
                    
        #na maquina de café
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
                elif escolha == 'FabLab':
                    nome_cenario_atual = "FabLab"
                    cenario_atual=cenarios[nome_cenario_atual]
                    
    # ah nao:
                        
##COMBATE!##            
              elif escolha == "Lutar":
                         print('-'*len('combate'))
                    print('COMBATE')
                    print('-'*len('combate'))

            #definindo monstro
                    monstro = random.choice(list(monstros.keys()))
                    vidas_monstro = monstros[monstro]["vida"]
                    dano_monstro = monstros[monstro]["dano"]
                    descricao_monstro = monstros[monstro]["descricao"]
                    
                    print (len('GAME ON')*"-")
                    print ("GAME ON")
                    print (len('GAME ON')*"-")                    
                    print()
                    print('Seu adversário é: {0}'.format(monstro))
                    print(descricao_monstro)
                    print('Ele causa {0} de dano e tem {1} vidas'.format(dano_monstro,vidas_monstro))
                    print()
                    
                    print('Responda com 1 ou 2:')
                    resposta = int(input('Quer entrar no combate (1) ou fugir (2)? '))
                    
                    if resposta == 2:
                        print('Para fugir, você deve passar no desafio')
                        num_a=random.randint(1,20)
                        num_b=random.randint(1,3)
                        resultado = int(input('Quanto é {0} elevado a {1}? '.format(num_a,num_b)))
                        if resultado != num_a**num_b:
                            print('Sua fuga deu errado')
                            print('Agora terá que lutar')
                            resposta=1
                        else:
                            nome_cenario_atual = 'FabLab'
                    if resposta == 1:
                        print('É hora do combate!!!')
                        print()
                       
            #armas e vidas
                    if len(armas) != 0:
                        print('Você possui: ')
                        for a in armas.keys():
                            print(a)
                        arma_escolhida=input('Escolha uma arma: ')
                        while arma_escolhida not in armas:
                            print('Você não tem essa arma')
                            arma_escolhida=input('Escolha outra arma: ')
                        print('Sua arma de combate é: {0}'.format(arma_escolhida))  
                        dano_arma=armas[arma_escolhida]
                        print('Ela causa {0} de dano'.format(dano_arma))
                        print()
                    else:
                        game_over=True
                        
            #início do combate
                    print('O combate começa agora')
                    print('Acerte a pergunta para atacar. Se errar, o monstro te ataca')
                    while vidas_jogador > 0 and vidas_monstro > 0:
                        teste= random.choice(list(conhecimento.keys()))
                        respondido = input(teste + ': ')
                        if respondido == conhecimento[teste]:
                            print('Correto!')
                            print('É sua vez de atacar')
                            vidas_monstro -= dano_arma
                            print('Seu adversário perdeu {0} e agora tem {1} vidas'.format(dano_arma,vidas_monstro))
                            print('você tem agora {0} vidas'.format(vidas_jogador))
                        else:
                            print('Resposta incorreta')
                            print('Ahhh! O monstro vai te atacar')
                            vidas_jogador-=dano_monstro
                            print('Você perdeu {0} e agora tem {1} vidas'.format(dano_monstro,vidas_jogador))
                            print('O montro tem agora {0} vidas'.format(vidas_monstro))
                            
            #resultados da luta
                    if vidas_jogador <= 0:
                        print('Meus pêsames, você morreu...')
                        game_over = True
                    elif vidas_monstro <= 0:
                        print('Parabéns, você venceu o monstro!')
                        premio_vida=random.randint(1,8)
                        premio_dinheiro=random.randint(1,15)
                        premio_horas=random.randint(1,5)
                        vidas_jogador+=premio_vida
                        dinheiro+=premio_dinheiro
                        horas+=premio_horas
                        print('Você ganhou {0} e agora tem {1} vidas'.format(premio_vida,vidas_jogador))
                        print('Você ganhou {0} e agora tem {1} reais'.format(premio_dinheiro,dinheiro))
                        print('Você ganhou {0} e agora tem {1} horas'.format(premio_horas,horas))
                        nome_cenario_atual = "FabLab"
                elif escolha == 'Fugir':
                        nome_cenario_atual == "FabLab"
                        
            # segundo andar
                nome_cenario_atual="Segundo andar do prédio novo"
                cenario_atual=cenarios[nome_cenario_atual]
                print("Segundo andar do prédio novo")
                print("----------------------------")
                print(cenario_atual["titulo"])
                print(cenario_atual["descricao"])
                print()
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
        #Se o jogador quiser lutar contra o monstro, precisa jogar o Jogo do Chute
                elif escolha == 'Lutar':
                        print('-'*len('monstro do chute'))
                        print('MONSTRO DO CHUTE')
                        print('-'*len('monstro do chute'))
                        print('Você enfrentará o Monstro do Chute')
                        print('Ele pensará em um número de 1 a 20 e você tem 5 tentativas para adivinhar qual é')
                        print('Boa sorte!')
                        VALOR_MAXIMO = 20
                        MAX_TENTATIVAS = 5
                        
                        num_secreto = random.randint(1, VALOR_MAXIMO)
                        
                        num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO))) 
                        while num_chute < 1 or num_chute > VALOR_MAXIMO: 
                            print("Valor invalido. Tente novamente") 
                            num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO)))
                            
              #tem 5 tentativas para acertar o valor
                        contador = 1
                        while num_chute != num_secreto and contador < MAX_TENTATIVAS:
                            contador += 1
                            if num_chute < num_secreto: 
                                print("Muito baixo") 
                            elif num_chute > num_secreto: 
                                print("Muito alto")
                            num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO))) 
                        while num_chute < 1 or num_chute > VALOR_MAXIMO: 
                            print("Valor invalido") 
                            num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO)))
                            
                       #se não conseguir, perde o jogo
                        if num_chute != num_secreto: 
                            print("Que pena, você perdeu!") 
                            print('O jogo acabou...')
                            game_over=True
                       #se conseguir, ganha prêmios, que são melhores no caso de o número de tentativas ser inferior ou igual a 3
                        else: 
                            print("Acertou em {0} tentativas".format(contador))
                            if contador <=3:
                                premio_dinheiro+=5
                                premio_horas+=3
                            else:
                                premio_dinheiro+=3
                                premio_horas+=1
                            dinheiro+=premio_dinheiro
                            horas+=premio_horas
                            print('Você ganhou {0} e agora tem {1} vidas'.format(premio_vida,vidas_jogador))
                            print('Você ganhou {0} e agora tem {1} reais'.format(premio_dinheiro,dinheiro))
                            print('Você ganhou {0} e agora tem {1} horas'.format(premio_horas,horas))
                            
                            #terminada a luta, volta para os elevadores
                            print('Você está retornando aos elevadores'
                            nome_cenario_atual = 'Elevadores'

                                
           #Se o jogador quiser fazer um amigo/aliado              
                elif escolha == 'Amigos':
                        if len(presentes) == 0:
                            print('Você não tem nenhum presente para dar!')
                            print('O monstro não gostou de você!')
                            print('Por isso, te devorou...')
                            game_over = True
                            
                        else:
                             requisitos.append('Aliado')
                            print('Voce deu um: ')
                            for p, d in presentes.items():
                                print(p + ': ' + d)
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
              
                
                
            #laboratório de instrumed
                elif escolha == 'Laboratório de InstruMed':
                     print('Relatório surpresa!!!')
                     horas-=5
                     print('Você perdeu 5 horas e agora tem {0}'.format(horas))
                     nome_cenario_atual = 'Laboratório de InstruMed'
                    
                    
            #materiais
                elif nome_cenario_atual == "Materiais":
                    requisitos.append('Materiais')
                    nome_cenario_atual = "Materiais"
                    
                
            # ultima fase
                elif escolha == "Construir a máquina do tempo":
                  #o jogador deve ter todos os requisitos necessários para a construção
                    if 'Materiais' and 'Programação'and 'Aliado' in requisitos:
                        print('Parabéns!')
                        print('Você construiu sua máquina do tempo!')
                        print('Agora volte para o passado e termine seu EP!')
                        vitoria = True
                 #caso contrário, pode sair do jogo ou retornar ao mesmo para tentar obter os itens que faltam
                    else:
                        print('Você não tem os requisitos necessários...')
                        print('O que você tem agora é: ')
                        for r in requisitos:
                            print(r)
                        final=['voltar para os elevadores', 'desistir']
                        print('Você pode: {0} (1) ou {1} (2)'.format(final[0],final[1]))
                        escolha=int(input('O que quer fazer? (responda com 1 ou 2)'))
                        if escolha in final:
                            if escolha == 1:
                                nome_cenario_atual = 'Elevadores'
                            else:
                                print('Foi por pouco...')
                                print('Você perdeu...')
                                game_over= True
                        else:
                            print('Você está indeciso demais!')
                            print('Foi por pouco...')
                            print('Você perdeu...')
                            game_over = True
            else:
                print('Essa não é uma opção!')
                print('Você tem mais uma chance apenas de acertar!')
                escolha = input("O que vai fazer? ")
                if escolha in opcoes:
                    nome_cenario_atual=escolha
                else:
                    print('Sua indecisão foi sua ruína!')
                    print('Zerou o EP e está de DP')
                    game_over= True
                    
                    
 # fim do jogo
#se o jogador ganhar
if vitoria:
        print('Parabéns!')
        print('Você construiu sua máquina do tempo!')
        print('Agora volte para o passado e termine seu EP!')


main()
