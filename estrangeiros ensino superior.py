#!/usr/bin/env python
# coding: utf-8

# # Análise dos estrangeiros no ensino superior Brasileiro

# ## Importação das bibliotecas necessárias

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt


# ## Leitura das planilhas com o dados
# ### Os arquivos podem levar até 15 minutos para abrir

# In[2]:


df_2018 = pd.read_csv("DM_ALUNO_2018.csv", delimiter = "|", encoding='iso=8859-1', usecols = ['TP_NACIONALIDADE', 'TP_SEXO'])
df_2017 = pd.read_csv("DM_ALUNO_2017.csv", delimiter = "|", encoding='iso=8859-1', usecols = ['TP_NACIONALIDADE', 'TP_SEXO'])
df_2016 = pd.read_csv("DM_ALUNO_2016.csv", delimiter = "|", encoding='iso=8859-1', usecols = ['CO_NACIONALIDADE_ALUNO', 'IN_SEXO_ALUNO'])
df_2015 = pd.read_csv("DM_ALUNO_2015.csv", delimiter = "|", encoding='iso=8859-1', usecols = ['CO_NACIONALIDADE_ALUNO', 'IN_SEXO_ALUNO'])
df_2014 = pd.read_csv("DM_ALUNO_2014.csv", delimiter = "|", encoding='iso=8859-1', usecols = ['CO_NACIONALIDADE_ALUNO', 'IN_SEXO_ALUNO'])                                                                                        


# ## Dicionário de variáveis 

# In[3]:


estrangeiro_2018 = []
mulher_estrangeira_2018 = []
estrangeiro_nat_2018 = []
mulher_estrangeira_nat_2018 = []

estrangeiro_2017 = []
mulher_estrangeira_2017 = []
estrangeiro_nat_2017 = []
mulher_estrangeira_nat_2017 = []

estrangeiro_2016 = []
mulher_estrangeira_2016 = []
estrangeiro_nat_2016 = []
mulher_estrangeira_nat_2016 = []

estrangeiro_2015 = []
mulher_estrangeira_2015 = []
estrangeiro_nat_2015 = []
mulher_estrangeira_nat_2015 = []

estrangeiro_2014 = []
mulher_estrangeira_2014 = []
estrangeiro_nat_2014 = []
mulher_estrangeira_nat_2014 = []


# ## Código para leitura dos dados e os prints dos mesmos

# In[4]:


estrangeiro_2018.append(df_2018.query('(TP_NACIONALIDADE == 3)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_2018.append(df_2018.query('(TP_NACIONALIDADE == 3 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
estrangeiro_nat_2018.append(df_2018.query('(TP_NACIONALIDADE == 2)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_nat_2018.append(df_2018.query('(TP_NACIONALIDADE == 2 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
print('')
print('2018')
print('')
print(f'Temos {(estrangeiro_2018[0])} estrangeiros nas universidades brasileiras em 2018.')
print(f'Temos {(mulher_estrangeira_2018[0])} mulheres estrangeiras nas universidades brasileiras em 2018.')
print(f'Temos {(estrangeiro_nat_2018[0])} brasileiros naturalizados nas universidades brasileiras em 2018.')
print(f'Temos {(mulher_estrangeira_nat_2018[0])} mulheres brasileiras naturalizadas nas universidades brasileiras em 2018.')

estrangeiro_2017.append(df_2017.query('(TP_NACIONALIDADE == 3)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_2017.append(df_2017.query('(TP_NACIONALIDADE == 3 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
estrangeiro_nat_2017.append(df_2017.query('(TP_NACIONALIDADE == 2)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_nat_2017.append(df_2017.query('(TP_NACIONALIDADE == 2 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
print('')
print('2017')
print('')
print(f'Tínhamos {(estrangeiro_2017[0])} estrangeiros nas universidades brasileiras em 2017.')
print(f'Tínhamos {(mulher_estrangeira_2017[0])} mulheres estrangeiras nas universidades brasileiras em 2017.')
print(f'Tínhamos {(estrangeiro_nat_2017[0])} brasileiros naturalizados nas universidades brasileiras em 2017.')
print(f'Tínhamos {(mulher_estrangeira_nat_2017[0])} mulheres brasileiras naturalizadas nas universidades brasileiras em 2017.')


estrangeiro_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('2016')
print('')
print(f'Tínhamos {(estrangeiro_2016[0])} estrangeiros nas universidades brasileiras em 2016.')
print(f'Tínhamos {(mulher_estrangeira_2016[0])} mulheres estrangeiras nas universidades brasileiras em 2016.')
print(f'Tínhamos {(estrangeiro_nat_2016[0])} brasileiros naturalizados nas universidades brasileiras em 2016.')
print(f'Tínhamos {(mulher_estrangeira_nat_2016[0])} mulheres brasileiras naturalizadas nas universidades brasileiras em 2016.')


estrangeiro_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('2015')
print('')
print(f'Tínhamos {(estrangeiro_2015[0])} estrangeiros nas universidades brasileiras em 2015.')
print(f'Tínhamos {(mulher_estrangeira_2015[0])} mulheres estrangeiras nas universidades brasileiras em 2015.')
print(f'Tínhamos {(estrangeiro_nat_2015[0])} brasileiros naturalizados nas universidades brasileiras em 2015.')
print(f'Tínhamos {(mulher_estrangeira_nat_2015[0])} mulheres brasileiras naturalizadas nas universidades brasileiras em 2015.')


estrangeiro_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('2014')
print('')
print(f'Tínhamos {(estrangeiro_2014)[0]} estrangeiros nas universidades brasileiras em 2014.')
print(f'Tínhamos {(mulher_estrangeira_2014[0])} mulheres estrangeiras nas universidades brasileiras em 2014.')
print(f'Tínhamos {(estrangeiro_nat_2014[0])} brasileiros naturalizados nas universidades brasileiras em 2014.')
print(f'Tínhamos {(mulher_estrangeira_nat_2014[0])} mulheres brasileiras naturalizadas nas universidades brasileiras em 2014.')
print('')

print('Total dos estudantes nascidos no exterior, naturalizados ou não, nas universidades brasileiras.')
total = (f'{(estrangeiro_2018[0]) + (estrangeiro_nat_2018[0])}')
print(total)


# ## Código para fazer a análise em gráficos

# In[6]:


x1 = [2014, 2015, 2016, 2017, 2018]
x2 = [2014.1, 2015.1, 2016.1, 2017.1, 2018.1]
y1 = [(int(estrangeiro_2014[0])), (int(estrangeiro_2015[0])), (int(estrangeiro_2016[0])), (int(estrangeiro_2017[0])), (int(estrangeiro_2018[0]))]
y2 = [(int(mulher_estrangeira_2014[0])), (int(mulher_estrangeira_2015[0])), (int(mulher_estrangeira_2016[0])), (int(mulher_estrangeira_2017[0])), (int(mulher_estrangeira_2018[0]))]

plt.title('Alunos estrangeiros nas universidades brasileiras')
plt.xlabel('Ano')
plt.ylabel('Crescimento')

plt.bar(x1, y1, label = 'Estrangeiros')
plt.bar(x2, y2, label = 'Mulheres Estrangeiras')
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)

for i, v in enumerate(y1):
    plt.text(x1[i] - 0.25, v + 200, str(v))
    
for i, v in enumerate(y2):
    plt.text(x2[i] -0.25, v + 200, str(v))

plt.show()

print('Entre 2014 e 2018 tivemos um aumento de 3.097 alunos estrangeiros (15,4%),')
print('uma média de 619,4 estudantes por ano, e um aumento de 1.155 mulheres estrangeiras (12,4%),')
print('uma média de 231 estudantes por ano.')


x1 = [2014, 2015, 2016, 2017, 2018]
x2 = [2014.1, 2015.1, 2016.1, 2017.1, 2018.1]
y1 = [(int(estrangeiro_nat_2014[0])), (int(estrangeiro_nat_2015[0])), (int(estrangeiro_nat_2016[0])), (int(estrangeiro_nat_2017[0])), (int(estrangeiro_nat_2018[0]))]
y2 = [(int(mulher_estrangeira_nat_2014[0])), (int(mulher_estrangeira_nat_2015[0])), (int(mulher_estrangeira_nat_2016[0])), (int(mulher_estrangeira_nat_2017[0])), (int(mulher_estrangeira_nat_2018[0]))]

plt.title('Alunos brasileiros naturalizados nas universidades brasileiras')
plt.xlabel('Ano')
plt.ylabel('Crescimento')

plt.bar (x1, y1, label = 'Brasileiros naturalizados')
plt.bar (x2, y2, label = 'Mulheres brasileiras naturalizadas')
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)

for i, v in enumerate(y1):
    plt.text(x1[i] - 0.25, v + 200, str(v))
    
for i, v in enumerate(y2):
    plt.text(x2[i] -0.25, v + 200, str(v))

plt.show()

print('Entre 2014 e 2018 tivemos um aumento de 526 alunos brasileiros naturalizados (4,7%),')
print('uma média de 105,2 estudantes por ano, e uma queda de 198 alunas brasileiras naturalizadas (3,3%),')   
print('uma média de 39,6 estudantes por ano.')

print('')
print('')
print('')
print('')
print('Relação entre mulheres e homens estrangeiros')
est = int(estrangeiro_2018[0]) - int(mulher_estrangeira_2018[0])
m_est = int(mulher_estrangeira_2018[0])
size = [est, m_est]
plt.pie(size, labels = ['Homens Estrangeiros','Mulheres estrangeiras'], explode = [0.05,0], autopct='%1.1f%%', shadow = True, startangle = 100, radius = 1.8)
plt.show()

print('')
print('')
print('')
print('')
print('\033[1;4mRelação entre mulheres e homens naturalizados\033[m')
nat_est = int(estrangeiro_nat_2018[0]) - int(mulher_estrangeira_nat_2018[0])
nat_m_est = int(mulher_estrangeira_nat_2018[0])
size = [nat_est, nat_m_est]
plt.pie(size, labels = ['Homens Naturalizados','Mulheres Naturalizadas'], explode = [0.05,0], autopct='%1.1f%%', shadow = True, startangle = 100, radius = 1.8)
plt.show()


# In[ ]:




