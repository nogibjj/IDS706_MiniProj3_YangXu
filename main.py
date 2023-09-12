import polars as pl
import matplotlib.pyplot as plt

def plot_data_distribution(data, column_name):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column_name].to_numpy(), bins=10, edgecolor="k", alpha=0.7)
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{column_name}_distribution.png")
    plt.show()

def load_data():
    return pl.read_csv("dataset_sample.csv")

def get_descriptive_statistics(data):
    stats = {}
    for col in data.columns:
        if data[col].dtype != pl.Object and col != "Date":
            col_stats = {
                "mean": data[col].mean(),
                "median": data[col].median(),
                "std": data[col].std()
            }
            # Only include columns with at least one non-None value
            if any(value is not None for value in col_stats.values()):
                stats[col] = col_stats
    return stats

def main():
    data = load_data()
    stats = get_descriptive_statistics(data)
    for col, values in stats.items():
        print(f"Statistics for {col}:")
        for stat, value in values.items():
            print(f"{stat}: {value}")
        print("\n")

    plot_data_distribution(data, "Price")

if __name__ == "__main__":
    main()
