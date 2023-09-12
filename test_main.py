import main
import pandas as pd

def test_load_data():
    data = main.load_data()
    # Check if the data is loaded as DataFrame and is not empty
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

    # Check if known columns 'Product', 'Price', and 'Quantity' are present
    for col in ["Product", "Price", "Quantity"]:
        assert col in data.columns

def test_get_descriptive_statistics():
    data = main.load_data()
    stats = main.get_descriptive_statistics(data)

    # Ensure 'Product' column isn't in the statistics
    assert "Product" not in stats.columns

    # For numerical columns, check if statistical indices are present
    for col in ["Price", "Quantity"]:
        assert col in stats.columns
        for stat in ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]:
            assert stat in stats.index

