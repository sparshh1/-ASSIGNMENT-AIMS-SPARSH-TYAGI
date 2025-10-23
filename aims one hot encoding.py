import pandas as pd

data={'fruit': ['apple', 'banana', 'orange', 'banana', 'apple']}
df_fruit = pd.DataFrame(data)

unique_fruit = sorted(set(df_fruit['fruit']))
#here im creating columns for the fruits
for fruit in unique_fruit:
    df_fruit['fruit_' + fruit] = [1 if val == fruit else 0 for val in df_fruit['fruit']]
    print(df_fruit)
