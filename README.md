# IDS706_MiniProj3_YangXu

This repository is part of the IDS706 course assignments, focusing on Mini Project 3. Building upon the ids706-python-template, it introduces Polars-based descriptive statistics. This script processes data from a CSV file to compute descriptive statistics and generate a visualization for data distribution.

## Overview

Utilizing the Polars library, this project demonstrates essential techniques for statistical analysis on datasets.

## Key Modifications from Original Template

- Transitioned from using Pandas to Polars for data manipulation and analysis.
- Transformed main.py to reflect Polars-based statistical techniques.
- Adjusted test_main.py to work with the Polars functions in main.py.
- Integrated polars within requirements.txt to facilitate data manipulation and statistical functions.

### Requirements

Ensure the presence of:
- Python (Version 3.6 or newer)
- Polars

## Functionality

- **`load_data()`**: Imports the `dataset_sample.csv` and returns a DataFrame.
- **`get_descriptive_statistics(data)`**: Computes descriptive statistics such as mean, median, and standard deviation for each numeric column.
- **`plot_data_distribution(data, column_name)`**: Visualizes and saves a histogram for the specified column.

## Sample Output

- **Descriptive Statistics**:

    ```bash
    Statistics for Date:
    mean: 19602.0
    median: 19602.0
    std: None


    Statistics for Product:
    mean: None
    median: None
    std: None


    Statistics for Price:
    mean: 1.4333333333333331
    median: 1.2
    std: 0.8455767262643882


    Statistics for Quantity:
    mean: 38.111111111111114
    median: 42.0
    std: 14.084072958881999
    ```

- **Data Visualization**:
<<<<<<< HEAD

=======

>>>>>>> 95df988b7c9f0da098f69dc63788444a4dbd55a8
  ![Price Distribution](Price_distribution.png)


[![example workflow](https://github.com/nogibjj/IDS706_MiniProj3_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj3_YangXu/actions/workflows/cicd.yml)
