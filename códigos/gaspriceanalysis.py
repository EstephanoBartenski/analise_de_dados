import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 15)

preços = pd.read_csv('gas_prices.csv')

# assim é na inteligência (basta incluir/excluir aqui o que quero ou não mostrar)
escolher_países = ['Australia', 'Canada', 'France', 'Germany', 'Italy',
                   'Japan', 'Mexico', 'South Korea', 'UK', 'USA']
for país in preços:
    if país in escolher_países:
        plt.plot(preços['Year'], preços[país], marker='.', label=país)

# assim é na machadada
# plt.plot(preços.Year, preços.USA, 'k.-', label='EUA')
# plt.plot(preços['Year'], preços.UK, 'b.-', label='Reino Unido')
# plt.plot(preços.Year, preços['Canada'], 'r.-', label='Cadaná')
# plt.plot(preços['Year'], preços.Germany, 'm.-', label='Alemanha')
# plt.plot(preços.Year, preços['France'], 'g.-', label='França')

# MÉDIA DOS PREÇOS DOS PAÍSES
col_list = list(preços.columns)
col_list.remove('Year')
preços['Total'] = preços[col_list].sum(axis=1, numeric_only=True)
preços['Total'] = preços['Total'] / 10
média_total = preços['Total'].sum() / preços['Total'].shape[0]
plt.hlines(média_total, 1990, 2008, colors='k', linestyles='dashed', label='PREÇO MÉDIO')

plt.title('Preço do Litro de combustível ao longo dos anos', fontdict={'fontweight': 'bold'}, fontsize='x-large')
plt.xlabel('Ano', fontdict={'fontweight': 'bold', 'fontsize': 'x-large'})
plt.ylabel('Preço (U$)', fontdict={'fontweight': 'bold', 'fontsize': 'x-large'})
plt.xticks(preços['Year'][::3]) # do começo ao final, de 3 em 3
cont = 0
i = [0]
for v in range(0, 6):
    cont += 1.50
    i.append(cont)
plt.yticks(i)
plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')  # só copia o 1.05 1.0
plt.tight_layout()
plt.grid()

# plt.savefig('preçoscombustivel.png', dpi=150)

plt.show()

# como pegr máximos valores de cada país e botar num gráfico de colunas?