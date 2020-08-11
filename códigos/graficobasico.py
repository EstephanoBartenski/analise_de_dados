# MATPLOTLIB (PLT) = Gráfico básico
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# GRÁFICO BÁSICO
x = np.arange(1, 11, 1)
y = x ** 2

# redimensionando gráfico
#plt.figure(figsize=(3, 2), dpi=150)  # se for pra imprimir, dpi >= 300 ou fica pixelado

# primeira linha
'''plt.plot(x, y,
         label='2x',
         color='black',
         linewidth=2,
         marker='.',
         linestyle='dashed',  # ou escreve '--' ou '..' 'dotted' etc
         markersize='10',
         markerfacecolor='red',
         markeredgecolor='black')'''
plt.plot(x, y, 'k.--', label='quadrado') # [color][marker][line] (mais rápido)


# segunda linha
x2 = np.arange(1, 11, 1)
# plt.plot(x2, x2 ** 3, 'r.--', label='cubo')
# quebrando a segunda linha em duas partes
plt.plot(x2[:6], x2[:6]**3, 'b.--', label='cubo 1º ramo')
plt.plot(x2[5:], x2[5:]**3, 'm.--', label='cubo 2º ramo')


plt.title('Gráfico simples', fontdict={'fontname': 'Cambria',
                                    'fontsize': 'x-large'})

plt.xlabel('Eixo das abcissas', fontdict={'fontname': 'Cambria',
                                             'fontsize': 'large'})

plt.ylabel('Eixo das ordenadas', fontdict={'fontname': 'Cambria',
                                                         'fontsize': 'large'})

plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.yticks([0, 25, 50, 75, 100])

plt.legend()  # pra mostrar as legendas
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()


# plt.savefig('pornografico.png', dpi=100)

plt.show()