# https://github.com/preti-joao/documents/blob/main/python/introducao.md

import random



# funções python
# https://www.w3schools.com/python/python_strings_methods.asp

#Lista de Exercícios referentes a estruturas de iteração (repetição)
import random

def ex1():
    for x in range(10):
        print(x)
    for x in range(1,10,2): #(inicio(.),fim(°),intervalo)
        print(x)
    for x in range (10,1,-1):
        print(x)

def ex2():
    option = -1
    while option != 0:
        option = int(input('Choose an option (0 to exit):'))
        print(option)

#1.Faça um programa que imprima todos os números de 1 até 100.
def q1():
    for num in range (1,101):
        print(num)

#2. Faça um programa que imprima todos os números pares de 100 até 1.
def q2():
    for num in range (100,0,-1):
        print (num)

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def q3():
    for num in range (0,501,5):
        print(num)

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.
def q4():
    count = 0
    while (count < 3):
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        sexo = input('Sexo (F/M): ')[0].upper() #.upper() transforma em maiúsculo | .strip() tira espaços
        count += 1

        if (idade > 21) and (sexo == 'M'):
            print (f'{nome} tem mais de 21 anos.')

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q5():
    erro = True
    num1 = 0
    num2 = 0
    while erro == True:
        try:
            num1 = int(input('1º Número: '))
        except ValueError:
            print('Erro 01: Valor inválido! \nDigite um número inteiro.')
        except:
            print('Erro 404: Not Found.')
        else:
            erro = False
        finally:
            print('...')
    erro = True
    while erro == True:
        try:
            num2 = int(input('2º Número: '))
        except ValueError:
            print('Erro 01: Valor inválido! \nDigite um número inteiro.')
        except:
            print('Erro 404: Not Found.')
        else:
            erro = False
        finally:
            print('...')
        count = 0
        soma = 0
        while (count < num1):
            soma = soma + num2
            count += 1
        if (count == num1):
            print (f'{num1} * {num2} = {soma}')
    # for _ in range(num1):
    # soma += num2


#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21
def q6():
    num1 = 0
    num2 = 1
    soma = 0
    print(num2)
    for count in range(1,21):
        soma = num1 + num2
        num1 = num2
        num2 = soma
        print(soma)

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
 #def q7():




#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q8():
    count = 0
    while (count <= 10):
        nome = input('Nome: ')
        salario = float(input('Salário bruto: R$'),2)
        if (salario < 1300):
            print(f'IRRF: Isento.')
        if (1300 <= salario < 2300):
            print (f'IRRF: R${salario*0.1}.')
        if (2300 <= salario):
            print (f'IRRF: R${salario*0.15}.')

        count += 1

#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.
def q9():
    somaId = 0
    somaIdReg = 0
    somaIdBom = 0
    somaIdExe = 0
    somaReg = 0
    somaBom = 0
    somaExe = 0
    count = 0
    while (count < 3):
        erro = True
        while (erro == True):
            try:
                idade = int(input('Idade: '))
                somaId += idade
            except ValueError:
                print('Erro 01: Valor inválido! \nDigite um número inteiro.')
            else:
                erro = False
        erro = True
        while (erro == True):
            try:
                opiniao = int(input('''
                1 - Regular
                2 - Bom
                3 - Excelente
                Digite sua opinião (de 1 a 3):
                '''))
                if (opiniao < 1 or opiniao > 3):
                    raise BaseException('Erro 01: Valor inválido! \nDigite um número de 1 a 3.') #cria um erro fora do except
                if (opiniao == 1):
                    somaIdReg = int(somaIdReg + idade)
                    somaReg += 1
                if (opiniao == 2):
                    somaIdBom = int(somaIdBom + idade)
                    somaBom += 1
                if (opiniao == 3):
                    somaIdExe = int(somaIdExe + idade)
                    somaExe += 1

            except ValueError:
                print('Erro 01: Valor inválido! \nDigite um número inteiro.')
                erro = True
            except BaseException as e:
                print(e)
                erro = True
            else:
                erro = False
                count += 1

    print(f'''
    ----------- Resultados -----------


    Pessoas entrevistadas: {count}
    Média das idades Geral: {round((somaId/count),2)}

    Responderam Regular:
    {somaReg} Pessoas
    Média das idades: {round((somaIdReg/count),2)}
    {round(((somaReg*100)/count),2)}% do total

    Responderam Bom:
    {somaBom} Pessoas
    Média das idades: {round((somaIdBom/count),2)}
    {round(((somaBom*100)/count),2)}% do total

    Responderam Exelente:
    {somaExe} Pessoas
    Média das idades: {round((somaIdExe/count),2)}
    {round(((somaExe*100)/count),2)}% do total

    ''')

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.

def q10():

# Reduzido para 3 países, 3 jogadores cada.
#peso e idade aleatorios pra cada jogador.
    pais1 = 'Austrália'
    pais2 = 'Brasil'
    pais3 = 'Canadá' 

    peso = [[round((random.randint(50,100) + random.random()),2) for _ in range(3)] for _ in range(3)] #cria matriz 3x3 com rand 50-100 + rand float 0-1 
    idade = [[random.randint(17,60) for _ in range(3)] for _ in range(3)] #cria matriz 3x3 com rand 17-60 para idade
 
    # for a in peso:
    #     print(a)
    # for a in idade:
    #     print(a)

    jpesado = [999,999,999]
    pesado = [0,0,0]
    jjovem = [999,999,999]
    jovem = [999,999,999]
    for p in range(3):
        for j in range(0,3):
            if jovem[p] > idade[p][j]:    # verificação idades por país [p] pais e [j] jogador
                jovem[p] = idade[p][j]    # se a idade for maior do que a última verificada, a variável passa a receber o valor da atual (maior)
                jjovem[p] = j+1           # para identificação do "Jogador {jjovem[0]}" no print mais em baixo. Índice +1, pq começa em 0.
            if pesado[p] < peso [p][j]:   # mesmo procedimento, mas agora para peso. 
                pesado[p] = peso[p][j]    # o mais pesado é o que prevalece
                jpesado[p] = j+1          # para identificação do "Jogador {jpesado[0]}" no print abaixo. Índice +1, pq começa em 0.
     

    print (f'''
    Lista oficial

    |{pais1}:
    |
    |Jogador 1: {idade[0][0]} anos, {peso[0][0]}kg
    |Jogador 2: {idade[0][1]} anos, {peso[0][1]}kg
    |Jogador 3: {idade[0][2]} anos, {peso[0][2]}kg
    |
    |Idade média do time: {round(((idade[0][0] + idade[0][1] + idade[0][2])/3),2)}
    |Peso médio do time: {round(((peso[0][0] + peso[0][1] + peso[0][2])/3),2)}
    |Jogador mais jovem do time: Jogador {jjovem[0]} - {jovem[0]} anos.
    |Jogador mais pesado do time: Jogador {jpesado[0]} - {pesado[0]}kg.

    |{pais2}:
    |
    |Jogador 1: {idade[1][0]} anos, {peso[1][0]}kg
    |Jogador 2: {idade[1][1]} anos, {peso[1][1]}kg
    |Jogador 3: {idade[1][2]} anos, {peso[1][2]}kg
    |
    |Idade média do time: {round(((idade[1][0] + idade[1][1] + idade[1][2])/3),2)}
    |Peso médio do time: {round(((peso[1][0] + peso[1][1] + peso[1][2])/3),2)}
    |Jogador mais jovem do time: Jogador {jjovem[1]} - {jovem[1]} anos.
    |Jogador mais pesado do time: Jogador {jpesado[1]} - {pesado[1]}kg.

    |{pais3}:
    |
    |Jogador 1: {idade[2][0]} anos, {peso[2][0]}kg
    |Jogador 2: {idade[2][1]} anos, {peso[2][1]}kg
    |Jogador 3: {idade[2][2]} anos, {peso[2][2]}kg
    |
    |Idade média do time: {round(((idade[2][0] + idade[2][1] + idade[2][2])/3),2)}
    |Peso médio do time: {round(((peso[2][0] + peso[2][1] + peso[2][2])/3),2)}
    |Jogador mais jovem do time: Jogador {jjovem[2]} - {jovem[2]} anos.
    |Jogador mais pesado do time: Jogador {jpesado[2]} - {pesado[2]}kg.
            ''')


#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    controle = True
    dentro = 0
    fora = 0


    while controle == True:
        try:
            num = int(input('Digite um número inteiro (0 para encerrar): '))
            if (num == 0):
                controle = False
            if (100 <= num <= 200):
                dentro += 1 
            if (num < 100 or num > 200):
                fora += 1
        except ValueError:
            print(f'''
Erro 01: Valor inválido!
Digite um número inteiro.

''')
        except:
            print('Erro 404: Not Found.')
    
    print (f''' 
    {dentro + fora} Números digitados no total.
    {dentro} Números entre 100 e 200.
    ''')

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():
    pahabit = 5000000
    panatal = (pahabit*0.03)
    pbhabit = 7000000
    pbnatal = (pbhabit*0.02)
    cont = 0

    while pahabit <= pbhabit:
        pahabit += panatal
        pbhabit += pbnatal
        panatal = (pahabit*0.03)
        pbnatal = (pbhabit*0.02)
        cont += 1

    print(f'O país A, levará {cont} anos para ultrapassar o país B em população.')


#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2
def q13():
    cod = -1
    conta = dict()
    while True:
        cod = int(input('Digite o número do consumidor (ou 0 para encerrar):'))
        if cod == 0:
            break
        consumidor = input('''
Digite o número referente ao tipo de consumidor:
1 - Residencial
2 - Comercial
3 - Industrial
''')
        consumo = int(input('Digite o consumo em kWh:'))

        if consumidor == '1':
            conta[cod] = consumo*0.3
        if consumidor == '2':
            conta[cod] = consumo*0.5
        if consumidor == '3':
            conta[cod] = consumo*0.7

    print(conta)




#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos

#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

#19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado comnota >= 7.0

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.

#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.

questao = int(input('Qual questão executar? '))
eval(f'q{questao}()')