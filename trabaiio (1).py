  
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
    time.sleep(3)
    print(" Escolha o nivel de dificuldade:\n")
    level = int(input(" 1.Fácil \n 2.Médio \n 3. Maratona(jogar todas as perguntas)\n"))
    while(level > 3 or level < 1):
        level = int(input(" Opção inválida. Digite uma das opções a seguir:\n 1. Facil\n 2. Médio\n 3. Difícil\n"))
    return level

def P1():
    print ("Hoje, um computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Um computador pode possuir inúmeros atributos, dentre eles armazenamento de dados, processamento de dados, por exemplo. Mas no passado, mais precisamente antes da década de 1920, o computador era um termo associado á?...")
    res1 = input ("\n a)objetos decorativos\n b)pessoas que realizavam cálculos\n c)cumbucas\n d)jogos de tabuleiro\n e)foguetes de mesa\n")
    if(res1 == 'b'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘B’\n Antes da década de 1920, o computador era um termo associado a pessoas que realizavam cálculos, geralmente liderados por físicos em sua maioria homens.")
        ponto = 0
    return ponto

def P2():
    print ("A APPLE® é sem dúvida uma das maiores empresas (senão a maior) produtoras de “elementos eletrônicos”. A maçã é pop: todo mundo já viu, todo mundo conhece, mas o que representa literalmente a ideia de ter como símbolo de uma empresa de tecnologia uma maçã mordida?")
    res2 = input ("\n a) O suicídio de Alan Turing \n b)A descoberta da gravidade por Isaac Newton \n c) Ao conhecimento de Adão e Eva \n d) Representação do Vale do Silício como uma fruta \n e) Nenhuma das alternativas\n")
    if(res2 == 'e'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘E’\n Apesar da APPLE® ser uma empresa criativa em seus produtos, ela não foi criativa ao criar sua logo. Todas as alternativas são apenas teorias não confirmadas pela APPLE®. Realmente te pegamos nessa!")
        ponto = 0
    return ponto

def P3():
    print ("Os dois primeiros modelos computacionais foram, com certeza, foram muito importantes para a computação. Primeiro veio o modelo de Turing e depois o de Von Neumann. Assine a alternativa certa em relação a esse dois modelos?")
    res3 = input (" a) Apesar de o modelo de Neumann conseguir executar todos os programas ,apenas o modelo de Turing era considerado universal\n b) Os computadores construídos com base no modelo de Turing armazenavam apenas os dados em suas memórias, já o modelo de Neumann armazenavam os dados e os programas\n c) O modelo de Neumann armazenava programas feito em cobol, já o modelo de Turing armazenava programas feito em ASP\n d) Computadores com base no modelo de Neumann aceitavam dados de entrada e o armazenavam, já o modelo de Turing apenas aceitavam dados de entrada e gerava dados de saída sem armazena-los\n e) Nenhuma das alternativas\n")
    if(res3 == 'b'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘B’\n Apesar de ambos os modelos terem varias mudanças entre si. Apenas os computadores com base no modelo de Neumann armazenavam dados e programas juntos em suas memórias, visando o fato de foi Von Neumann que propôs que programas e dados são na verdade a mesma coisa (sequencia de bits).")
        ponto = 0
    return ponto

def P4():
    print ("Sistema operativo ou operacional é um programa ou um conjunto de programas cuja função é gerenciar os recursos do sistema (definir qual programa recebe atenção do processador, gerenciar memória, criar um sistema de arquivos, etc). Qual destes não é um sistema operacional?")
    res4 = input (" a) Windows\n b) Chrome OS\n c) Mac OS X\n d) Linux Ubuntu\n e) Object Pascal\n")
    if(res4 == 'e'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘E’\n Existem vários sistemas operacionais pelo mundo, mas Object Pascal não é um sistema operacional, ele é na verdade uma linguagem de programação.")
        ponto = 0
    return ponto

def P5():
    print ("5.	Geralmente chamados de _______ , esses programas se escondem mascarados como arquivos ou softwares legítimos. Depois de baixados e instalados, os _______ alteram o computador e realizam atividades maliciosas sem o conhecimento ou consentimento da vítima. Tendo conhecimento sobre diferentes “vírus de computador”, complete o espaço com a alternativa certa.")
    res5 = input (" a) Spywares\n b)Adwares\n c) Cavalos de troias\n d) Worms\n e) Rasomwares\n")
    if(res5 == 'c'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: letra ’C’. A resposta está explicitada na questão.")
        ponto = 0
    return ponto

def P6():
    print ("6.	A palavra inglesa bug significa literalmente 'inseto', mas ela também possui outro significado para a computação. Qual alternativa representa melhor esse significado?")
    res6 = input (" A) Um tipo de vírus de computador cujo principal objetivo é se espalhar da forma mas abrangente possível pela internet\n B) Refere–se a falhas que ocorrem ao executar algum software ou hardware\n C) Quando um sistema inicia uma atualização de software.Daí que vem a frase “deu bug”\n D) É um termo usado para se referir-se aos e-mails não solicitados, que geralmente são enviados para um grande numero de pessoas\n E) São computadores de usuário finais que foram comprometidos por códigos e/ou algum tipo vírus de computador")
    if(res6 == 'b'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: letra ‘B’. Bug é um jargão da informática que se refere às temidas falhas inesperadas que ocorrem ao executar algum software ou usar um hardware. Esses erros imprevisíveis que prejudicam o funcionamento correto de alguma tecnologia podem desencadear problemas incômodos, como travamentos e roubar informações sigilosas.")
        ponto = 0
    return ponto

def P7():
    print ("Em álgebra booleana, utilizamos quatro operações básicas no nível de bits: NOT (não), AND (e), OR (ou) e XOR (exclusive-OR). Para que essas operações servem?")
    res7 = input (" a) Elas aplicam a mesma operação básica sobre os bits de um padrão individualmente ou sobre dois bits correspondentes em dois padrões\n b) Servem para calcular qualquer tipo de operação com números na ordem dos reais.\n c) Servem para qualquer padrão binário que possam ser utilizado para alterar, obter ou limpar partes de outros padrões binários\n d) Servem para operações de deslocamento, para mover bits em um padrão, modificando suas posições\n e) Nenhuma das alternativas")
    if(res7 == 'a'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: letra ‘A’. Uma operação Lógica é uma operação matemática em Álgebra Booleana cujos valores podem ser iguais a 0 ou 1, o que corresponde a falso ou verdadeiro, respectivamente. Usados para manipular padrões de bits.")
        ponto = 0
    return ponto

def P8():
    print ("8.	Operações de deslocamento movem os bits em um padrão, modificando suas posições. O deslocamento pode ser feito para a direita (shift right) ou para a esquerda (shift left). Como ficaria o número binário ‘10011000’ com deslocamento lógico simples para a esquerda de um bit.")
    res8 = input (" a) 0001100\n b) 0011000\n c) 100010\n d) 0111000\n e) 0001011\n ")
    if(res8 == 'b'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: letra ‘B’. No deslocamento simples as posições deslocadas são preenchidas com zero (nesse caso entra um ‘zero’ pela esquerda). Bits que saem representação do número são perdidos. Seguindo essa regra, chegamos à alternativa ‘b’.")
        ponto = 0
    return ponto

def P9():
    print (" Calculadora pessoal, Computadores, Celulares; são exemplos de aparelhos usados para calcular contas, seja elas complexas ou não. Mas qual foi o primeiro instrumento de calculo usado pelo homem?")
    res9 = input (" a) Kamal\n b) Régua\n c) Ábaco\n d) Polígrafo\n e) Ampulheta\n ")
    if(res9 == 'c'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘C’. Ábaco é um antigo instrumento de cálculo em sistema decimal, com provável origem na Mesopotâmia há mais de 5500 anos a.C., considerado como uma extensão do ato de se contar nos dedos")
        ponto = 0
    return ponto

def P10():
    print ("10.	Alan Mathison Turing(1912-1954) foi um grande matemático, logico, criptoanalista e cientista da computação britânica. Ele foi umas das pessoas que atuaram na descriptação de mensagem da frota naval alemã na Segunda Guerra Mundial. Qual feito de Turing o fez ser considerado pai da computação?")
    res10 = input (" a) Contribuiu na teoria dos conjuntos, ao criar estatísticas para a álgebra\n b) Turing construiu uns dos primeiros computadores, definindo-os matematicamente\n c) Foi um dos primeiros a pensar na possibilidade de uma maquina se tornar inteligente e criou um modelo teórico para um computador universal\n  d) Criou a teoria dos jogos , um ramo da matemática aplicada que estuda situações estratégicas onde jogadores escolhem diferentes ações na tentativa de melhorar seu retorno\n e) Criação do time ‘HUT 8’ , após criar técnicas para quebrar códigos criptografados ")
    if(res10 == 'b'):
        print("CORRETO! :D")
        ponto = 1
    else:
        print("ERRADO :(\n Resposta correta: Letra ‘B’.  Alan Mathison Turing realmente foi importante para a computação já que foi influente no desenvolvimento da ciência da computação e na formalização do conceito de algoritmo e computação com a máquina de Turing, desempenhando um papel importante na criação do computador moderno, Sendo pioneiro na Ciência da Computação.")
        ponto = 0
    return ponto

def Maratona():
    cont = 0
    val1 = P1()
    val2 = P2()
    val3 = P3()
    val4 = P4()
    val5 = P5()
    val6 = P6()
    val7 = P7()
    val8 = P8()
    val9 = P9()
    val10 = P10()
    Total = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10
    return Total
    
def Facil():
    cont=0
    val1 = P1()
    val2 = P2()
    val4 = P4()
    val6 = P6()
    val9 = P9()
    Total = val1 + val2 + val4 + val6 + val9
    return Total

def Medio():
    cont=0
    val3 = P3()
    val5 = P5()
    val7 = P7()
    val8 = P8()
    val10 = P10()
    Total = val3 + val5 + val7 + val8 + val10
    return Total

pergfacil= ["1","2","4","6","9"]
pergmedio= ["3","5","7","8","10"]
pergmaratona= ["1","2","3","4","5","6","7","8","9","10"]

respfacil= ["B", "E", "E", "B", "C"]
respmedio= ["B", "C", "A", "B", "B"]
respmaratona= ["B", "E", "B", "E", "C", "B", "A", "B", "C", "B"]

def final(opcao, Total):
    if opcao==1:
        print ("As perguntas respondidas foram:", pergfacil)
        print ("As respostas dessas questoes eram respectivamente:",respfacil)
        if(Total == 2 or Total == 3):
             print ("Você acertou", Total, "questões\n Você esta na média, falta estudar um pouco mais!")
        elif(Total == 4):
             print ("Você acertou", Total, "questões\n Parabéns! Você aproveitou bem esse semestre.")
        elif(Total == 1):
             print ("Você acertou", Total, "questão\n Não desanime, continue estudando e refaça o quiz")
        elif(Total == 5):
             print ("Parabéns você acertou todas as questões\n Você aproveitou bem esse semestre!")
        elif(Total == 0):
             print ("Você não acertou nenhuma questão :(\n Não desanime, continue estudando e refaça o quiz")

    elif opcao==2:
        print ("As perguntas respondidas foram:", pergmedio)
        print ("As respostas dessas questoes eram respectivamente:",respmedio)
        if(Total == 2 or Total == 3):
             print ("Você acertou", Total, "questões\n Você esta na média, falta estudar um pouco mais!")
        elif(Total == 4):
             print ("Você acertou", Total, "questões\n Parabéns! Você aproveitou bem esse semestre.")
        elif(Total == 1):
             print ("Você acertou", Total, "questão\n Não desanime, continue estudando e refaça o quiz")
        elif(Total == 5):
             print ("Parabéns você acertou todas as questões\n Você aproveitou bem esse semestre!")
        elif(Total == 0):
             print ("Você não acertou nenhuma questão :(\n Não desanime, continue estudando e refaça o quiz")

    elif opcao==3:
        print ("As perguntas respondidas foram:", pergmaratona)
        print ("As respostas dessas questoes eram respectivamente:",respmaratona)
        if(Total == 6 or Total == 7):
             print ("Você acertou", Total, "questões\n Você esta na média, falta estudar um pouco mais!")
        elif(Total == 8 or Total == 9):
             print ("Você acertou", Total, "questões\n Parabéns! Você aproveitou bem esse semestre.")
        elif(Total < 5 and Total > 1):
             print ("Você acertou", Total, "questões\n Não desanime, continue estudando e refaça o quiz")
        elif(Total == 10):
             print ("Parabéns você acertou todas as questões\n Você aproveitou bem esse semestre!")
        elif(Total == 0):
             print ("Você não acertou nenhuma questão :(\n Não desanime, continue estudando e refaça o quiz")




def main():
    boasvindas()
    opcao = Nivel()
    
    if(opcao == 1):
        Total = Facil()
        final(opcao, Total)
    elif(opcao == 2):
        Total = Medio()
        final(opcao, Total)
    elif(opcao == 3):
        Total = Maratona()
        final(opcao, Total)

    
   

main()
