# ChowTest

ChowTest is a Python library for conducting the Chow Test, which tests for structural breaks in the coefficients of two linear regressions.

## Instalation (Google colab)

```
!git clone https://github.com/SergeyHSE/ChowTest.git

%cd ChowTest

!pip install .
```

## Usage

To use ChowTest, follow these steps:

1. Import the `chowtest` function:

    ```python
    from ChowTest import chowtest
    ```

2. Prepare your data:

    - `X`: Independent variable(s) as a Pandas DataFrame column(s).
    - `y`: Dependent variable as a Pandas DataFrame column (subset).
    - `last_index_in_model_1`: Index of the final point prior to the assumed structural break (index value).
    - `first_index_in_model_2`: Index of the first point following the assumed structural break (index value).
    - `significance_level`: The significance level for hypothesis testing (float).

3. Call the `chowtest` function:

    ```python
    results = chowtest(X, y, last_index_in_model_1, first_index_in_model_2, significance_level)
    Chow_Stat, p_value = results
    ```

4. Display the results:

    ```python
    print("Chow Statistic:", Chow_Stat)
    print("P-value:", p_value)
    ```

Make sure to replace the placeholder values (`X`, `y`, `last_index_in_model_1`, `first_index_in_model_2`, `significance_level`) with your actual data and parameters.

