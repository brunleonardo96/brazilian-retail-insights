import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Caricamento dati
df = pd.read_csv('retention_results.csv')

# 2. Creiamo la matrice per la Heatmap
cohort_pivot = df.pivot(index='cohort_month', columns='month_number', values='retention_rate')

# 3. Creazione del grafico
plt.figure(figsize=(16, 10))
plt.title('Customer Retention Rate (%) - Olist Brazilian E-commerce', fontsize=16)

sns.heatmap(cohort_pivot,
            annot=True,
            fmt='.1f',
            cmap='YlGnBu',
            linewidths=.5)

plt.xlabel('Mesi dal primo acquisto')
plt.ylabel('Mese della Coorte')


plt.savefig('retention_heatmap.png')

plt.show()