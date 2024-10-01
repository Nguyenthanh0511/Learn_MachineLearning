import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#column
col_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# Load the Iris dataset
df = pd.read_csv('./Dataset/iris.data')

# Display the first few rows of the dataset
print(df.head())