import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carico i dati
df = pd.read_csv('geo_spending_results.csv')

# 2. Ordino i dati per fatturato
df = df.sort_values(by='total_revenue', ascending=False).head(10)

# 3. Creo il grafico
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Barplot orizzontale
plot = sns.barplot(
    x='total_revenue',
    y='customer_state',
    data=df,
    palette='viridis'
)

plt.title('Top 10 Brazilian States by Total Revenue', fontsize=15)
plt.xlabel('Total Revenue (R$)', fontsize=12)
plt.ylabel('State', fontsize=12)

# Aggiungo i valori delle etichette
for p in plot.patches:
    width = p.get_width()
    plt.text(width + 1, p.get_y() + p.get_height()/2,
             '{:,.0f}'.format(width),
             ha="left", va="center")

plt.tight_layout()
plt.savefig('geo_spending_chart.png')
plt.show()