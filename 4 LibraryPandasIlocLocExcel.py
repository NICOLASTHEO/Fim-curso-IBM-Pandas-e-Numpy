print('hello, world!')
# biblioteca PANDAS, ler cvs e Excel
# #Usando LOC, ILOC e IX
#importando biblioteca PANDAS, lendo arquivo on-line, e apresentando-o
import pandas as pd

csv_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df=pd.read_csv(csv_path)
df.head()

#UMA VEZ BAIXADO A BIBLIOTECA XLRD CONSEGUIREMOS ABRIR E LER ARQUIVOS DE EXCEL

xlsx_path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df=pd.read_excel(xlsx_path)
df.head()
#pode-se acessar determinada coluna ou linha. Ex. acessarei a coluna 'LENGTH'
x=df[['Length']]
x
#ou
print(x)

#Podemos ver o Type, a classe dos dados que estamos observando, e a biblioteca usada, exatamente no local que especificamos.
x=df[["Artist"]]
type(x)
#devolverá: class pandas.core.frame.DataFrame

#PODEMOS FAZER A MESMA OBSERVAÇÃO E ANÁLISA PARA VÁRIAS COLUNAS ESPECIFICADAS. EX.:
y=df[['Artist','Length','Genre']]
y


#Usando LOC, ILOC e IX

# ACESSAR VALORES COM OLOC - ILOC interagirá com dois elementos da tabela, sendo o primento para linha e o segundo para número.
#representação por números:
df.iloc[0,0] #[linha, coluna]
df.iloc[0,2]
df.iloc[1,0]
df.iloc[1,2]

#LOC acessa a coluna usando o seu NOME - LOC: faz dois argumentos integragirem: integers e columns (linhas, que são núemros inteiros e nomes de colunas) 
df.loc[0,'Artist'] # result. "Michael Jackson" #---> [linha e coluna]
df.loc[0,'Released']# 1982
df.loc[1,"Artist"] # "AC/DC"
df.loc[1,"Released"] # 1980

#IX - Por padrão, ix procurará um rótulo. Se o IX não encontrar um rótulo, ele usará um número inteiro. 
# Isso significa que você pode selecionar dados usando números de coluna e números de linha ou cabeçalhos de coluna e nomes de linha usando ix.
# No Pandas versão 0.20.0 e posterior, o ix está obsoleto. --> Ou seja, IX NÃO INTERESSA, ESTÁ EM DESUSO!!!


#Slicing:
#CRIANDO UM NOVO DATAFRAME COM ILOC SLICING
#O resultado é um quadro de dados composto pelas linhas e colunas selecionadas.
df.iloc[0:2, 0:3] #mostra os resultados exatos de tais linhas e colunas como Output
z=df.iloc[0:2, 0:3] # Resultado um novo Dataframe com os valores constantes nas duas primeiras linhas e as três primeiras colunas à variável Z.
z #Z é uma nova planilha a ser trabalhada.
#mesma coisa mas com LOL
df.loc[0:2,"Artist":"Released"]

#SALVAR, POR EXEMPLO, UMA COLUNA COMO UM DF (DATAFRAME)
q=df[['Rating']] #não preciso saber o número de linhas, o Python se encarrega.
q
#OU ainda:
q=df.loc[0:7, "Rating"]
q


df['Released'].unique() 
#resultado, somento os elementos únicos da coluna RELEASED: 1982,1980,1973,1992,1977,1976

# O sistema pode me devolver determinados valores. Ex:
df["Released"]>=1980   # devolverá True ou False, True só os números forem maiores ou iguais a 1980

#Pode-se gerar um novo dataframe com elementos selecionados. EX.: em uma lista digitaremos
df1=df[df['Released']>1980]
#surgirá uma nova lista, com TODOS (linhas e colunas gerais) os dados que possuirem valor maior que 1980 
#salvar o novo dataframe:
df1.to_csv('new songs.csv')


