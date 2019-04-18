# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriela Yukari Mitu, gabrielaym@al.insper.edu.br
# - aluno B: Gabriella Escobar Cukier, gabriellaec@al.insper.edu.br

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
                "fugir": "fugir para o quarto andar" 
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
                "não comprar café": "muito caro!!",
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
                "Machado 3D": "ganha +1 de poder",
                "FabLab": "voltar para a sala dos engenheiros",
            }
        },
        "Segundo andar": {
            "titulo": "o andar do tobogã",
            "descricao": "O tobogã hoje magicamente te teletransporta"
                         "para o prédio antigo do Insper!! Mágico!!"
                         "Porém custa 2 reais",
            "opcoes": {
                "usar tobogã": "teleporte para o prédio antigo do Insper",
                "Terceiro andar": "voltar para o terceiro andar"
                                  "e matar um monstro",
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        print(cenario_atual)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal. #qualquer coisa
if __name__ == "__main__":
    main()
