import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carico i dati
df = pd.read_csv('payment_methods_results.csv')

# Pulizia
df = df[df['payment_type'] != 'not_defined']

# 2. Grafico set up
plt.figure(figsize=(12, 6))
sns.set_theme(style="white")

# Grafico a barre per lo scontrino medio (Average Ticket)
ax = sns.barplot(x='payment_type', y='avg_ticket', data=df, palette='magma')

# Etichette sopra le barre
for p in ax.patches:
    ax.annotate(f'R$ {p.get_height():.1f}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'center',
                xytext = (0, 9),
                textcoords = 'offset points')

plt.title('Average Order Value (AOV) by Payment Method', fontsize=15)
plt.xlabel('Payment Type', fontsize=12)
plt.ylabel('Average Value (R$)', fontsize=12)

plt.tight_layout()
plt.savefig('payment_methods_chart.png')
plt.show()