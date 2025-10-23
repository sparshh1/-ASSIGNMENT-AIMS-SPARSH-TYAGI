## ORDINAL ENCODING  
(table format output of all the codes provided in the three distributed python file)

|   | Salary_LPA | Salary_level | Salary_level_encoded |
|---|------------|--------------|---------------------|
| 0 | 4          | low          | 1                   |
| 1 | 7          | medium       | 2                   |
| 2 | 2          | low          | 1                   |
| 3 | 9          | high         | 3                   |
| 4 | 8          | medium       | 2                   |

---

## ONE HOT ENCODING – fruit_apple only  

|   | fruit   | fruit_apple |
|---|---------|-------------|
| 0 | apple   | 1           |
| 1 | banana  | 0           |
| 2 | orange  | 0           |
| 3 | banana  | 0           |
| 4 | apple   | 1           |

---

## ONE HOT ENCODING – fruit_apple & fruit_banana  

|   | fruit   | fruit_apple | fruit_banana |
|---|---------|-------------|--------------|
| 0 | apple   | 1           | 0            |
| 1 | banana  | 0           | 1            |
| 2 | orange  | 0           | 0            |
| 3 | banana  | 0           | 1            |
| 4 | apple   | 1           | 0            |

---

## ONE HOT ENCODING – fruit_apple, fruit_banana, fruit_orange  

|   | fruit   | fruit_apple | fruit_banana | fruit_orange |
|---|---------|-------------|--------------|--------------|
| 0 | apple   | 1           | 0            | 0            |
| 1 | banana  | 0           | 1            | 0            |
| 2 | orange  | 0           | 0            | 1            |
| 3 | banana  | 0           | 1            | 0            |
| 4 | apple   | 1           | 0            | 0            |

---

## IMPUTATION  

|   | branch     | marks | marks_mean_imputed | branch_imputed |
|---|------------|-------|--------------------|----------------|
| 0 | mechanical | 80.0  | 80.0               | mechanical     |
| 1 | NaN        | 85.0  | 85.0               | notknown       |
| 2 | cse        | NaN   | NaN                | cse            |
| 3 | ece        | 90.0  | 90.0               | ece            |
| 4 | NaN        | 75.0  | 75.0               | notknown       |
| 5 | cse        | NaN   | NaN                | cse            |

