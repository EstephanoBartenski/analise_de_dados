import matplotlib.pylab as plt

# plt.figure(figsize=(1, 0.5), dpi=100)

labels = ['Categoria 1', 'Categoria 2', 'Categoria 3']
values = [50, 10, 100]

colunas = plt.bar(labels, values, width=0.4, color='grey')
colunas[0].set_hatch('+')
colunas[1].set_hatch('.')
colunas[2].set_hatch('x')

plt.yticks([0, 25, 50, 75, 100])

plt.title('Título do gráfico')

plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

plt.show()