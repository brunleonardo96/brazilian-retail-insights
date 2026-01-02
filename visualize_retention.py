import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Caricamento dati
df = pd.read_csv('retention_results.csv')

# 2. Trasformazione: Creiamo la matrice per la Heatmap (Pivot Table)
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

# Aggiungi QUESTA RIGA per salvare l'immagine!
plt.savefig('retention_heatmap.png') # Salva l'immagine nella stessa cartella dello script

plt.show() # Questa riga mostra il grafico a schermo