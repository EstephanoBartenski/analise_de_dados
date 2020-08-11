# comparando times com gráfico box and whiskers chart

import matplotlib.pylab as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

plt.figure(figsize=(5, 8))

liv_overall = fifa.loc[fifa['Club'] == 'Liverpool']['Overall']
mancity_overall = fifa.loc[fifa['Club'] == 'Manchester City']['Overall']
brighton_overall = fifa.loc[fifa['Club'] == 'Brighton & Hove Albion']['Overall']

labels = ['Liverpool', 'M. City', 'Brighton']

boxes = plt.boxplot([liv_overall, mancity_overall, brighton_overall], labels=labels, patch_artist=True, medianprops={'linewidth': 2, 'color':'r'})
for box in boxes['boxes']:
    # set edge color
    box.set(color='k', linewidth=2)

    # set fill color
    box.set(facecolor='#e0e0e0')

plt.title('FIFA18 - Comparação de clubes')
plt.ylabel('FIFA18 - Classificação média do clube')

plt.grid()

plt.show()