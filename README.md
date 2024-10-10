# Pandas and API (Python Data Science)

## Introduction to NumPy

**NumPy** is a fundamental Python library for scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays efficiently.

### Why NumPy?

- **Efficiency**: NumPy arrays are faster and more memory-efficient than Python lists.
- **Mathematical Operations**: Provides a vast range of operations for linear algebra, Fourier transforms, and random number generation.
- **Interoperability**: Works seamlessly with Pandas, Matplotlib, and other scientific libraries.

## Introduction to Pandas

**Pandas** is a powerful Python library for data manipulation and analysis, built on top of NumPy. It provides flexible and intuitive data structures like **DataFrames** and **Series**, which allow for easy manipulation of structured data.

### Why Pandas?

- **Fast**: Pandas is built on NumPy, offering high-performance data analysis tools.
- **Flexible**: It provides numerous functions for data transformation, filtering, and grouping.
- **Versatile**: You can read data from various formats (CSV, Excel, SQL, JSON, etc.).

## Key Pandas Operations

### DataFrames

The **DataFrame** is the primary data structure in Pandas. It’s like a table in a database or an Excel sheet.

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
