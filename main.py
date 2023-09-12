import pandas as pd
import matplotlib.pyplot as plt

def plot_data_distribution(data, column_name):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column_name], bins=10, edgecolor="k", alpha=0.7)
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{column_name}_distribution.png")
    plt.show()

def load_data():
    return pd.read_csv("dataset_sample.csv")

def get_descriptive_statistics(data):
    return data.describe()

def main():
    data = load_data()
    stats = get_descriptive_statistics(data)
    print(stats)

    plot_data_distribution(data, "Price")

if __name__ == "__main__":
    main()
