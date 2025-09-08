from data_loader import load_reviews

def analyze_sentiment(review: str) -> str:
    if "świetna" in review.lower() or "wysokim" in review.lower():
        return "positive"
    elif "nie działa" in review.lower() or "wolna" in review.lower():
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    df = load_reviews()
    df["sentiment"] = df["review"].apply(analyze_sentiment)
    print(df)
