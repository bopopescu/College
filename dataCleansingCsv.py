import pandas as pd

data = pd.read_csv('CsvData.csv',header=None).values.reshape()

print(data)
