# Gráfico de pizza pra qtd de destros e canhotos

import matplotlib.pylab as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

canhotos = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0] # zero pra pegar o primeiro pq dá array
destros = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels = ['Canhotos', 'Destros']
colors = ['#783164', '#4020a1']
explode = (.05, .05)
plt.pie([destros, canhotos], labels=labels, colors=colors, autopct='%.2f %%', explode=explode)
plt.title('FIFA20 - Relação destros/canhotos', fontdict={'fontsize': 'x-large', 'fontweight': 'bold'})
plt.show()