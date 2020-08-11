# Gráfico de pizza pra distirbuição dos pesos
# como está 1212lbs preciso separa o número do lbs
import matplotlib.pylab as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

fifa['Weight'] = [float(x.strip('lbs')) if type(x) == str else x for x in fifa['Weight']]
fifa['Weight'] /= 2.205

leve = list()
médio = list()
pesado = list()
for value in fifa['Weight']:
    if value < 70:
        leve.append(value)
    elif 70 <= value < 90:
        médio.append(value)
    elif value >= 90:
        pesado.append(value)
print(len(leve))
print(len(médio))
print(len(pesado))
pesos = [len(leve), len(médio), len(pesado)]
labels = ['Peso igual ou menor que 70 Kg', 'Peso entre 70 e 90 Kg', 'Peso igual ou maior que 90 Kg']
colors = ['#fbff00', '#3cff00', '#d12121']
explode = (.05, .05, .05)
plt.pie(pesos, colors=colors, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.title('FIFA20 - Distribuição dos pesos dos jogadores', fontdict={'fontweight': 'bold', 'fontsize': 'x-large'})
plt.xlabel('')
plt.ylabel('')
plt.show()