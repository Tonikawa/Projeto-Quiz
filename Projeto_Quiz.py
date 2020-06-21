#Júlia Carvalho de Souza Castro TIA:32022298 
#Gabriel Batista Cristiano. TIA:32090722 
#Fábio Silveira Tanikawa. TIA:32092563

import time

def boasvindas():
    print(" *** Boas vindas ao Quiz de ciência da computação ***")
    print(" Perguntas serão feitas e você terá que respode-lás\n Ao fim do Quiz, você receberá uma classificação de acordo com seus acertos")
    print(" Não tenha medo em errar, o jogo está aqui para te ensinar\n Responnda com a letra correspondente a alternativa correta")
    print(" Então, vamos começar!!!\n")

def Nivel():
    time.sleep(5)
    print(" Escolha o nivel de dificuldade:\n")
    level = int(input(" 1.Maratona\n 2. Facil\n 3. Médio\n 4. Difícil\n"))
    while(level > 4 or level < 1):
        level = int(input(" Opção inválida. Digite uma das opções a seguir:\n 1.Maratona\n 2. Facil\n 3. Médio\n 4. Difícil\n"))
    return level
    
def Maratona():
    cont = 0
    print ("Hoje, um computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Um computador pode possuir inúmeros atributos, dentre eles armazenamento de dados, processamento de dados, por exemplo. Mas no passado, mais precisamente antes da década de 1920, o computador era um termo associado á?...")
    res1 = input ("\n a)objetos decorativos\n b)pessoas que realizavam cálculos\n c)cumbucas\n d)jogos de tabuleiro\n e)foguetes de mesa\n")
    if(res1 == 'b'):
        print("CORRETO! :D")
        cont = cont+1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘B’\n Antes da década de 1920, o computador era um termo associado a pessoas que realizavam cálculos, geralmente liderados por físicos em sua maioria homens.")

    time.sleep(5)
    print ("A APPLE® é sem dúvida uma das maiores empresas (senão a maior) produtoras de “elementos eletrônicos”. A maçã é pop: todo mundo já viu, todo mundo conhece, mas o que representa literalmente a ideia de ter como símbolo de uma empresa de tecnologia uma maçã mordida?")
    res2 = input ("\n a) O suicídio de Alan Turing \n b)A descoberta da gravidade por Isaac Newton \n c) Ao conhecimento de Adão e Eva \n d) Representação do Vale do Silício como uma fruta \n e) Nenhuma das alternativas\n")
    if(res2 == 'e'):
        print("CORRETO! :D")
        cont = cont+1
    else:
        print("ERRADO:(\n Resposta correta: Letra ‘E’\n Apesar da APPLE® ser uma empresa criativa em seus produtos, ela não foi criativa ao criar sua logo. Todas as alternativas são apenas teorias não confirmadas pela APPLE®. Realmente te pegamos nessa!")

    time.sleep(5)
    print ("Os dois primeiros modelos computacionais foram, com certeza, foram muito importantes para a computação. Primeiro veio o modelo de Turing e depois o de Von Neumann. Assine a alternativa certa em relação a esse dois modelos?")
    res3 = input (" a) Apesar de o modelo de Neumann conseguir executar todos os programas ,apenas o modelo de Turing era considerado universal\n b) Os computadores construídos com base no modelo de Turing armazenavam apenas os dados em suas memórias, já o modelo de Neumann armazenavam os dados e os programas\n c) O modelo de Neumann armazenava programas feito em cobol, já o modelo de Turing armazenava programas feito em ASP\n d) Computadores com base no modelo de Neumann aceitavam dados de entrada e o armazenavam, já o modelo de Turing apenas aceitavam dados de entrada e gerava dados de saída sem armazena-los\n e) Nenhuma das alternativas\n")
    if(res3 == 'b'):
        print("CORRETO! :D")
        cont = cont+1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘B’\n Apesar de ambos os modelos terem varias mudanças entre si. Apenas os computadores com base no modelo de Neumann armazenavam dados e programas juntos em suas memórias, visando o fato de foi Von Neumann que propôs que programas e dados são na verdade a mesma coisa (sequencia de bits).")

    time.sleep(5)
    print ("Sistema operativo ou operacional é um programa ou um conjunto de programas cuja função é gerenciar os recursos do sistema (definir qual programa recebe atenção do processador, gerenciar memória, criar um sistema de arquivos, etc). Qual destes não é um sistema operacional?")
    res4 = input (" a) Windows\n b) Chrome OS\n c) Mac OS X\n d) Linux Ubuntu\n e) Object Pascal\n")
    if(res4 == 'e'):
        print("CORRETO! :D")
        cont = cont+1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘E’\n Existem vários sistemas operacionais pelo mundo, mas Object Pascal não é um sistema operacional, ele é na verdade uma linguagem de programação.")

    return res1, res2, res3, res4


def main():
    boasvindas()
    opcao = Nivel()

    if(opcao == 1):
        Maratona()
    elif(opcao == 2):
        Perguntas_Facil()
    elif(opcao == 3):
        Perguntas_Medio()
    else:
        Perguntas_Dificil()

main()
