#Júlia Carvalho de Souza Castro TIA:32022298 
#Gabriel Batista Cristiano. TIA:32090722 
#Fábio Silveira Tanikawa. TIA:32092563

def boasvindas():
    print(" *** Boas vindas ao Quiz de ciência da computação ***")
    print(" Perguntas serão feitas e você terá que respode-lás\n Ao fim do Quiz, você receberá uma classificação de acordo com seus acertos")
    print(" Não tenha medo em errar, o jogo está aqui para te ensinar\n Responnda com a letra correspondente a alternativa correta")
    print(" Então, vamos começar!!!\n")

def Nivel():
    print(" Escolha o nivel de dificuldade:\n")
    level = int(input(" 1. Facil\n 2. Médio\n 3. Difícil\n"))
    while(level > 3 or level < 1):
        level = int(input(" Opção inválida. Digite uma das opções a seguir:\n 1. Facil\n 2. Médio\n 3. Difícil\n"))
    return level
    
def Perguntas ():
    print ("Hoje, um computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Um computador pode possuir inúmeros atributos, dentre eles armazenamento de dados, processamento de dados, por exemplo. Mas no passado, mais precisamente antes da década de 1920, o computador era um termo associado á?...")
    res1 = input ("\n a)objetos decorativos\n b)pessoas que realizavam cálculos\n c)cumbucas\n d)jogos de tabuleiro\n e)foguetes de mesa\n")
    
    print ("A APPLE® é sem dúvida uma das maiores empresas (senão a maior) produtoras de “elementos eletrônicos”. A maçã é pop: todo mundo já viu, todo mundo conhece, mas o que representa literalmente a ideia de ter como símbolo de uma empresa de tecnologia uma maçã mordida?")
    res2 = input ("\n a) O suicídio de Alan Turing \n b)A descoberta da gravidade por Isaac Newton \n c) Ao conhecimento de Adão e Eva \n d) Representação do Vale do Silício como uma fruta \n e) Nenhuma das alternativas\n")
    
    print ("Os dois primeiros modelos computacionais foram, com certeza, foram muito importantes para a computação. Primeiro veio o modelo de Turing e depois o de Von Neumann. Assine a alternativa certa em relação a esse dois modelos?")
    res3 = input (" a) Apesar de o modelo de Neumann conseguir executar todos os programas ,apenas o modelo de Turing era considerado universal\n b) Os computadores construídos com base no modelo de Turing armazenavam apenas os dados em suas memórias, já o modelo de Neumann armazenavam os dados e os programas\n c) O modelo de Neumann armazenava programas feito em cobol, já o modelo de Turing armazenava programas feito em ASP\n d) Computadores com base no modelo de Neumann aceitavam dados de entrada e o armazenavam, já o modelo de Turing apenas aceitavam dados de entrada e gerava dados de saída sem armazena-los\n e) Nenhuma das alternativas\n")

    print ("Sistema operativo ou operacional é um programa ou um conjunto de programas cuja função é gerenciar os recursos do sistema (definir qual programa recebe atenção do processador, gerenciar memória, criar um sistema de arquivos, etc). Qual destes não é um sistema operacional?")
    res4 = input (" a) Windows\n b) Chrome OS\n c) Mac OS X\n d) Linux Ubuntu\n e) Object Pascal\n")
    return res1, res2, res3, res4


def main ():
    boasvindas()
    opcao = Nivel()

    if(opcao == 1):
        Perguntas()
    elif(opcao == 2):
        print("Deu Certo!")


main()
