import pandas as pd

def load_reviews(path="data/sample_reviews.csv"):
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_reviews()
    print(df.head())
