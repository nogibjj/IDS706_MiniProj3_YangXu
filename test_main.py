import main
import polars as pl

def test_load_data():
    data = main.load_data()

    # Check if the data is loaded as DataFrame and is not empty
    assert isinstance(data, pl.DataFrame)
    assert data.height > 0

    # Check if known columns 'Product', 'Price', and 'Quantity' are present
    for col in ["Product", "Price", "Quantity"]:
        assert col in data.columns

def test_get_descriptive_statistics():
    data = main.load_data()
    stats = main.get_descriptive_statistics(data)

    # Ensure 'Product' and 'Date' columns aren't in the statistics
    assert "Product" not in stats
    assert "Date" not in stats

    # For numerical columns, check if statistical indices are present
    for col in ["Price", "Quantity"]:
        assert col in stats
        for stat in ["mean", "median", "std"]:
            assert stat in stats[col]

