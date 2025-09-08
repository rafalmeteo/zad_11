import matplotlib.pyplot as plt
from sentiment_analysis import analyze_sentiment
from data_loader import load_reviews

df = load_reviews()
df["sentiment"] = df["review"].apply(analyze_sentiment)

sentiment_counts = df["sentiment"].value_counts()

plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.title("Sentiment Analysis of Reviews")
plt.show()
