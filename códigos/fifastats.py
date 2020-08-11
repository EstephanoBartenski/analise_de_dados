import matplotlib.pylab as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

print(fifa.columns)

bins = [40, 50, 60, 70, 80, 90, 100]
plt.hist(fifa['Overall'], bins=bins, color='#4f9c62')
plt.xticks(bins)
plt.ylabel('Nº de jogadores', fontdict={'fontsize': 'x-large'})
plt.xlabel('Habilidade média', fontdict={'fontsize': 'x-large'})
plt.title('FIFA20 - Distribuição das habilidades dos jogadores', fontdict={'fontweight': 'bold', 'fontsize': 'x-large'})
plt.grid()
plt.show()



