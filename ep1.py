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
            escolha = input("O que você quer fazer? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu! Falhou na EP e está de DP!")


# Programa principal. #qualquer coisa
if __name__ == "__main__":
    main()
