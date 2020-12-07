#### Python Intermediate #####

## Gráficos com Matplotlib ##

import matplotlib.pyplot as plt

ano = [1950,1970,1990,2010]

pop = [32.519,35.692,45.263,46.972]

# Gráfico de linhas

plt.plot(ano, pop)

plt.show()

# Gráfico por pontos

plt.scatter(ano, pop)

plt.show()

# Podemos colocar também escala log

plt.scatter(ano, pop)
plt.yscale("log")
plt.show()

# Histogramas

# Primeiro vamos criar os dados para depois plotar

import numpy as np

dados = np.random.normal(1500,5,300)

# Com os dados criados vamos gerar nosso histograma

plt.hist(dados)
plt.show

# Para limpar o gráfico use:

plt.clf()

# Agora vamos fazer o histograma com 5 intervalos

plt.hist(dados,5)
plt.show()
plt.clf()

# Customizando os gráficos

plt.plot(ano, pop)
plt.xlabel('ano')
plt.ylabel('população')
plt.title("População por ano")
plt.yticks([0,10,20,30,40,50], ['0','10 mi','20 mi','30mi', '40mi','50mi'])
plt.show()
plt.clf()

# Agora vamos incluir uma terceira variável em nosso gráfico de PIB

pib = [100,120,150,190]

import numpy as np
np_pib = np.array(pib)

np_pib*=30 # eu multipliquei por 30 para ficar mais visível no gráfico
plt.scatter(ano,pop, s = np_pib)
plt.xlabel('ano')
plt.ylabel('população')
plt.title("População por ano e PIB")
plt.yticks([0,10,20,30,40,50], ['0','10 mi','20 mi','30mi', '40mi','50mi'])
plt.show()
plt.clf()

# Para melhorar ainda mais o gráfico vamos incluir cores e transparência c e alpha, respectivamente

cor = ['red','yellow','green','green']

plt.scatter(ano,pop, s = np_pib, c= cor, alpha=0.7)
plt.xlabel('ano')
plt.ylabel('população')
plt.title("População por ano e PIB")
plt.yticks([0,10,20,30,40,50], ['0','10 mi','20 mi','30mi', '40mi','50mi'])

# Vamos adicionar também infos específicas e uma grade

plt.text(1950,32.519,"Crise pós guerra")
plt.text(1970,35.692,"Industrialização")
plt.text(1990,45.623,"Era da informática")

plt.grid(True)

plt.show()
plt.clf()

## Dicionários ##

# Vamos começar usando um método de busca sem o dicionário para fazermos uma comparação das metodologias

paises = ['espanha', 'frança', 'alemanha', 'noruega']

capitais = ['madri','paris','berlim','oslo']

ind_ale = paises.index('alemanha')

print(capitais[ind_ale])

# Agora com dicionários, fazendo agrupamentos

europa = {'espanha':'madri', 'frança':'paris', 'alemanha':'berlim', 'noruega':'oslo'}
print(europa)

# Nessa estrutura os países são as chaves do dicionário. Chaves são objetos imutáveis no dicionário

print(europa.keys())

print(europa['noruega'])

# Podemos adicionar mais países também 

europa['italia']='veneza' # eu sei que está errado, mas vamos corrigir no próximo exemplo de código

'italia' in europa

print(europa)

# Diferente das chaves em si, o conteúdos delas pode mudar, agora vamos corrigir a capital da Itália

europa['italia'] = 'roma'

print('italia' in europa)

print(europa)

# Podemos também usar a função del para apagar algum conteúdo desejado

del(europa['italia'])

print(europa)

# Diferenças entre listas e dicionários

    # Listas são indexadas por um range de números enquanto dicionários são por chaves únicas
    # Listas são melhores para dados sequências enquanto dicionários tem um desempenho melhor como tabelas
    
# Vamos complicar um pouco e lidar com dicionários dentro de dicionários

europa =   {'espanha':{'capital':'madrid','pop':10},
            'frança':{'capital':'paris','pop':8},
            'alemanha':{'capital':'berlim','pop':12},
            'noruega':{'capital':'oslo','pop':4}
            }

print(europa['frança']['capital'])

# Agora adicionaremos mais dados

dados_italia = {'capital':'roma','pop':7}
europa['italia'] = dados_italia

print(europa)

## Pandas ##

# Quando usamos pandas, lidamos muito com data frames que de uma forma simplista podemos chamar de tabelas

import pandas as pd

df_europa = pd.DataFrame(europa)

print(df_europa)

# A visualização não ficou muito boa, então vamos transpor esse DF

df_europa = df_europa.T

print(df_europa)

# Agora sim!

# Vamos começar a trabalhar com arquivos externos agora. No exemplo abaixo estou trabalhando com um arquivo local do meu PC

dist_resp = pd.read_csv('C:/Users/mathe/Desktop/Python Folder/DFs/distribuicao_respiradores.csv')

dist_resp

# Podemos usar uma coluna como índice também

dist_resp = pd.read_csv('C:/Users/mathe/Desktop/Python Folder/DFs/nz_cigarrete_berraviour.csv', index_col=1)

# Vamos ajustar a entrada de dados porque no Brasil usamos virgula ao invés de ponto como separador decimal, ao contrário do python

dist_resp = pd.read_csv('C:/Users/mathe/Desktop/Python Folder/DFs/distribuicao_respiradores.csv',delimiter=';',decimal=',')

dist_resp

# Verificando os tipos

type(dist_resp['FORNECEDOR'])

type(dist_resp[['FORNECEDOR']])

# Selecionando dados específicos

dist_resp[1:4]

# Selecionando com loc e iloc

# para trabalhar com estes dados usaremos outro DF

dados = pd.read_csv('C:/Users/mathe/Desktop/Python Folder/DFs/dados_pop.csv',delimiter=';',decimal=',')

dados.index = ['BR','AR','UR','CH']

dados

# loc é usado para a encontrarmos de acordo com a descrição

dados.loc['AR']

# selecionando desse jeito temos o panda series cru

# porém se utilizarmos como demonstrado abaixo, temos o Data Frame

dados.loc[['AR']]

# Podemos também fazer seleções múltiplas

dados.loc[['AR','CH']]

# E também selecionar quais colunas devem ser vistas

dados.loc[['AR','CH'],['populacao','pib']]

dados.loc[:,['pais','pib']]

# iloc usa a posição da entrada ao invés da descrição

dados.iloc[[1,3],[0,1]]

## Operadores de comparação ##

# Servem para fins de comparação e filtro


2==3
1<3

# Eles também funcionam para textos, seguindo ordem alfabética

'Matheus' > 'Antonio'

# as comparações devem ser feitas sempre com objetos do mesmo tipo, a não ser em numpy arrays

import numpy as np
seq = np.array([1,2,3,4,5])
seq > 2

# Os operadores lógicos são:
    # < : Menor
    # > : Maior
    # <= : Menor ou igual
    # >= : Maior ou igual
    # == : Igual
    # != : Diferente
    
# Outro ponto importa é que python é uma linguagem "Case sentitive" o que significa que maiúsculas e minúsculas impactam na comparação

'python' == 'PyThoN'

# True equivale a 1 também

True == 1 

## Operadores lógicos ##

    # and : Operador lógico "e", condições devem ser atendidas
    
x = 3
    
x > 1 and x < 4

    # or : Operador lógico "ou", se qualquer uma das condições for verdadeira, o resutado será verdadeiro
    
x > 1 or x < 2

    # not : Operador lógico "não", transforma o booleano em seu inverso

not(True)

# Para numpy arrays não podemos usar os operadors lógicos diretamente, e sim via funções, que são elas

np.logical_and(seq > 1, seq < 3)
np.logical_or(seq > 1, seq < 3)
np.logical_not(seq==1)

## Operadores condicionais ##

    # São eles if, else, elif
    
    # if : Se uma determinada condição for atendida, execute derminado comando. No exemplo abaixo vamos fazer um teste para identificar se o número é par:
        
z = 4

if z % 2 == 0:
    print(str(z) + " é par")
    
    # Ponto importante: Python é um linguagem identada, ou seja, devemos usar o "tab" para mostrar para o código onde a condição começa e termina

# Caso a condição não seja atendida, podemos colocar uma segunda ação para o programa

z = 5

if z % 2 == 0:
    print(str(z) + " é par") # Para verdadeiro
else :
    print(str(z)+ " é impar") # Para falso

# No caso de buscarmos mais possíveis soluções, podemos usar o elif

z = 9

if z % 2 == 0:
    print(str(z) + ' é divisível por 2')
elif z % 3 == 0:
    print(str(z) + ' é divisível por 3')
else :
    print(str(z) + ' não é divisível nem por 2, nem por 3')

# O operador de comparação sempre parará na primeira condição a ser atendidada. Vamos ver o exemplo do número 6 que atende ambas as condições:

z = 6

if z % 2 == 0:
    print(str(z) + ' é divisível por 2')
elif z % 3 == 0:
    print(str(z) + ' é divisível por 3')
else :
    print(str(z) + ' não é divisível nem por 2, nem por 3')

## Filtrando DF com pandas e operadores ##

    # vamos resgatar o DF dados
    
print(dados)

    # selecionamos o pib

dados.loc[:,'pib']

    # criamos um booleano com a condição desejada

dados.loc[:,'pib'] > 50

mais_ricos = dados.loc[:,'pib'] > 50

    # exibimos os resultados

dados[mais_ricos]

    # podemos fazer isso diretamente também

dados[dados['pib']>50]

    # como pandas é criado sobre numpy podemos usar os operadores numpy também

np.logical_and(dados['pib'] > 50, dados['pib'] < 90)

dados[np.logical_and(dados['pib'] > 50, dados['pib'] < 90)]    

## Loops ##

# Loops são iterações no código. Usamos para repetir os mesmos comandos até uma determinada condição ser atendida

# While loop: iteração até determinada condição ser atendidade
    
k = 100

while k > 1:
    k /= 4 # significa o mesmo que k = k/4
    print(k)
    
# quando o valor chegou em 0.39, a iteração parou


# For Loop: para cada variável em uma sequência, exectuar uma ação determinada

# vamos resgatar a lista países para esse exemplo

print(paises)

# se quiséssemos listar cada item separadamente no código sem ter redundância, poderíamos usar o foor loop

for i in paises:
    print(i)
    
# podemos adicionar mais informações também

for j,i in enumerate(paises):
    print('País ' + str(j) + ': ' + i)
    
# podemos usar outras funções também

for i in paises:
    print(i.upper())
    
# e até outras formas de escrever também

for j,i in enumerate(paises):
    print('País {}: {}'.format(j,i)) # {} com .format facilita na hora de mostrar um resultado
    
# loops em estruturas de dados

# dicionários

europa = {'espanha':'madri', 'frança':'paris', 'alemanha':'berlim', 'noruega':'oslo'}
print(europa)

for key, value in europa.items():
    print (key + ': ' + str(value))
    
# np arrays

for value in np_pib:
    print(value)
    
# Pandas Data Frames

for v in dados:
    print(v)

# para iteração no pandas precisamos ser mais específicos

for l, r  in dados.iterrows():
    print(l)
    print(r)

for l, r  in dados.iterrows():
    print(l + ': ' + r['capital'].capitalize())

# Vamos criar uma coluna com o comprimento do nome dos paises

dados

for l, r in dados.iterrows():
    dados.loc[l,'comp_nome'] = len(r['pais'])
    
print(dados)

# o método acima funciona para criar uma nova coluna, mas para grandes volumes de dados pode se tornar um problema, nesse caso fazemos assim:
    
dados['comp_nome'] = dados['pais'].apply(len)

print(dados)
