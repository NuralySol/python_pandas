# Pandas and Api ( Python Data Science!)

## Introduction to Pandas

**Pandas** is a powerful Python library for data manipulation and analysis, built on top of NumPy. It provides flexible and intuitive data structures like **DataFrames** and **Series**, which allow for easy manipulation of structured data.

### Why Pandas?

- **Fast**: Pandas is built on NumPy, offering high-performance data analysis tools.
- **Flexible**: It provides numerous functions for data transformation, filtering, and grouping.
- **Versatile**: You can read data from various formats (CSV, Excel, SQL, JSON, etc.).

---

## Key Pandas Operations

### DataFrames

The **DataFrame** is the primary data structure in Pandas. It’s like a table in a database or an Excel sheet.

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
