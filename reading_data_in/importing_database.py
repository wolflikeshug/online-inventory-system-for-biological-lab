import pandas as pd

excel_file = 'Sample_Data_one_freezer.xlsx'
df = pd.read_excel(excel_file)
print(df)