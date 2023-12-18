# ChowTest

ChowTest is a Python library for conducting the Chow Test, which tests for structural breaks in the coefficients of two linear regressions.
The null hypothesis (H0) of the Chow Test assumes that there is no structural break in the coefficients of the two linear regressions. In other words, it posits that the relationships between the independent variables and the dependent variable are the same across the specified segments. 
```
If the p-value is less than the chosen significance level (usually 0.05):
    Reject the null hypothesis.
    Conclusion: There are statistically significant evidence of a structural change in the regression coefficients between the two periods.

If the p-value is greater than the chosen significance level:
    Fail to reject the null hypothesis.
    Conclusion: There is no statistically significant evidence of a structural change in the regression coefficients between the two periods.
```

## Instalation

```
1. Download ZIP:
Click on the green "Code" button and select "Download ZIP". Save the ZIP archive to your computer.

2. Extract ZIP Archive:
Unpack the archive into a folder containing python packages.
Rename the subfolder to 'Chowtest' and extract this folder from the main folder, deleting the resulting empty main folder.

3. Install the Package:
!pip install /path/to/your/ChowTest

**For Colab we should load the archive to colab envirment and run the next command:
!unzip /content/ChowTest-main.zip -d /content/ChowTest
and then run this command:
!pip install /content/ChowTest/ChowTest

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

