import pandas as pd

def load_csv(filepath):
    """
    Loads a CSV biomechanical data file.
    """
    return pd.read_csv(filepath)

if __name__ == "__main__":
    df = load_csv("../data/sample_data.csv")
    print(df.head())
