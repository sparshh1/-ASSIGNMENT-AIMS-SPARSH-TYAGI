import pandas as pd

data = {'Salary_LPA': [4, 7, 2, 9, 8],
     'Salary_level': ['low', 'medium', 'low', 'high', 'medium']}
df = pd.DataFrame(data)
#now mapping it
level_mapping ={'low': 1, 'medium' : 2, 'high': 3}
df['Salary_level_encoded'] = [level_mapping[val] for val in df['Salary_level']]

print(df)
