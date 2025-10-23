import pandas as pd
import numpy as np

data={'branch':['mechanical',np.nan,'cse','ece',np.nan, 'cse'],
      'marks':[80,85,np.nan,90,75,np.nan]}
df=pd.DataFrame(data)

marks=df['marks'].values
mean_marks=np.mean(marks)
marks_imputed =[val if not np.isnan(val) else mean_marks for val in marks]
df['marks_mean_imputed'] = marks_imputed

branches = df['branch'].values
branch_imputed = [val if pd.notnull(val) else 'notknown' for val in branches]
df['branch_imputed'] = branch_imputed

print(df)