#!/usr/bin/env python
# coding: utf-8

# # Crescimento dos estrangeiros no ensino superior Brasileiro

# ## Importação das bibliotecas necessárias

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt


# ## Leitura das planilhas com o dados

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

# In[234]:


estrangeiro_2018.append(df_2018.query('(TP_NACIONALIDADE == 3)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_2018.append(df_2018.query('(TP_NACIONALIDADE == 3 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
estrangeiro_nat_2018.append(df_2018.query('(TP_NACIONALIDADE == 2)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_nat_2018.append(df_2018.query('(TP_NACIONALIDADE == 2 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
print('')
print('\033[1;32m2018\033[m')
print('')
print(f'Temos \033[1;4;34m{(estrangeiro_2018[0])}\033[m estrangeiros nas universidades brasileiras em 2018.')
print(f'Temos \033[1;4;34m{(mulher_estrangeira_2018[0])}\033[m mulheres estrangeiras nas universidades brasileiras em 2018.')
print(f'Temos \033[1;4;34m{(estrangeiro_nat_2018[0])}\033[m brasileiros naturalizados nas universidades brasileiras em 2018.')
print(f'Temos \033[1;4;34m{(mulher_estrangeira_nat_2018[0])}\033[m mulheres brasileiras naturalizadas nas universidades brasileiras em 2018.')

estrangeiro_2017.append(df_2017.query('(TP_NACIONALIDADE == 3)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_2017.append(df_2017.query('(TP_NACIONALIDADE == 3 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
estrangeiro_nat_2017.append(df_2017.query('(TP_NACIONALIDADE == 2)')['TP_NACIONALIDADE'].count())
mulher_estrangeira_nat_2017.append(df_2017.query('(TP_NACIONALIDADE == 2 and TP_SEXO == 1)')['TP_NACIONALIDADE'].count())
print('')
print('\033[1;32m2017\033[m')
print('')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_2017[0])}\033[m estrangeiros nas universidades brasileiras em 2017.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_2017[0])}\033[m mulheres estrangeiras nas universidades brasileiras em 2017.')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_nat_2017[0])}\033[m brasileiros naturalizados nas universidades brasileiras em 2017.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_nat_2017[0])}\033[m mulheres brasileiras naturalizadas nas universidades brasileiras em 2017.')


estrangeiro_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2016.append(df_2016.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('\033[1;32m2016\033[m')
print('')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_2016[0])}\033[m estrangeiros nas universidades brasileiras em 2016.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_2016[0])}\033[m mulheres estrangeiras nas universidades brasileiras em 2016.')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_nat_2016[0])}\033[m brasileiros naturalizados nas universidades brasileiras em 2016.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_nat_2016[0])}\033[m mulheres brasileiras naturalizadas nas universidades brasileiras em 2016.')


estrangeiro_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2015.append(df_2015.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('\033[1;32m2015\033[m')
print('')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_2015[0])}\033[m estrangeiros nas universidades brasileiras em 2015.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_2015[0])}\033[m mulheres estrangeiras nas universidades brasileiras em 2015.')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_nat_2015[0])}\033[m brasileiros naturalizados nas universidades brasileiras em 2015.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_nat_2015[0])}\033[m mulheres brasileiras naturalizadas nas universidades brasileiras em 2015.')


estrangeiro_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 3)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 3 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
estrangeiro_nat_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 2)')['CO_NACIONALIDADE_ALUNO'].count())
mulher_estrangeira_nat_2014.append(df_2014.query('(CO_NACIONALIDADE_ALUNO == 2 and IN_SEXO_ALUNO == 1)')['CO_NACIONALIDADE_ALUNO'].count())
print('')
print('\033[1;32m2014\033[m')
print('')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_2014)[0]}\033[m estrangeiros nas universidades brasileiras em 2014.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_2014[0])}\033[m mulheres estrangeiras nas universidades brasileiras em 2014.')
print(f'Tínhamos \033[1;4;34m{(estrangeiro_nat_2014[0])}\033[m brasileiros naturalizados nas universidades brasileiras em 2014.')
print(f'Tínhamos \033[1;4;34m{(mulher_estrangeira_nat_2014[0])}\033[m mulheres brasileiras naturalizadas nas universidades brasileiras em 2014.')
print('')

print('Total dos estudantes nascidos no exterior, naturalizados ou não, nas universidades brasileiras.')
total = (f'\033[1;4;34m{(estrangeiro_2018[0]) + (estrangeiro_nat_2018[0])}\033[m')
print(total)


# ## Código para fazer a análise em gráficos

# In[255]:


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

print('Entre 2014 e 2018 tivemos um aumento de \033[1;4;34m3.097\033[m alunos estrangeiros \033[1;4;34m(15,4%)\033[m, uma média de \033[1;4;34m619,4\033[m estudantes por ano,')
print('e um aumento de \033[1;4;34m1.155\033[m mulheres estrangeiras \033[1;4;34m(12,4%)\033[m, uma média de \033[1;4;34m231\033[m estudantes por ano.')


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

print('Entre 2014 e 2018 tivemos um aumento de \033[1;4;34m526\033[m alunos brasileiros naturalizados\033[1;4;34m(4,7%)\033[m, uma média de \033[1;4;34m105,2\033[m estudantes por ano,')
print('e uma queda de \033[1;4;31m198\033[m alunas brasileiras naturalizadas\033[1;4;31m(3,3%)\033[m, uma média de \033[1;4;31m39,6\033[m estudantes por ano.')

print('')
print('')
print('')
print('')
print('\033[1;4mRelação entre mulheres e homens estrangeiros\033[m')
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




