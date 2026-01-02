import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

# 1. Carico i dati campionati
df = pd.read_csv('reviews_data.csv')

# 2. NLP Sentiment Score
df['sentiment_score'] = df['review_comment_message'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# 3. Sentiment Score vs Review Score
plt.figure(figsize=(10, 6))
sns.boxplot(x='review_score', y='sentiment_score', data=df, palette='RdYlGn')

plt.title('NLP Sentiment Score vs. Star Rating (Validation)', fontsize=14)
plt.xlabel('Star Rating (1-5)', fontsize=12)
plt.ylabel('TextBlob Polarity Score', fontsize=12)
plt.axhline(0, color='red', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('sentiment_validation_plot.png')
plt.show()