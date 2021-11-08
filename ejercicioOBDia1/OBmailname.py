#might need to instal open openpyxl using pip on cmd (if Windows user)
#Author Jose Elias Azpillaga for OpenBootcamp

import pandas as pd

pd.options.display.max_rows = 999

df = pd.read_excel('info.xlsx')

mylist = df['email'].unique()

print(list(enumerate(mylist,start=1)))