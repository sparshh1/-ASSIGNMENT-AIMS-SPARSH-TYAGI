## ORDINAl ENCODING

| Salary_LPA | Salary_level | Salary_level_encoded |
|------------|--------------|---------------------|
| 4          | low          | 1                   |
| 7          | medium       | 2                   |
| 2          | low          | 1                   |
| 9          | high         | 3                   |
| 8          | medium       | 2                   |

---

## ONE HOT ENCODING

| fruit_apple | fruit_banana | fruit_orange |
|-------------|--------------|--------------|
| True        | False        | False        |
| False       | True         | False        |
| False       | False        | True         |
| False       | True         | False        |
| True        | False        | False        |

---

## IMPUTATION

| branch     | marks | marks_mean_imputed | branch_imputed |
|------------|-------|--------------------|---------------|
| mechanical | 80.0  | 80.0               | mechanical    |
| NaN        | 85.0  | 85.0               | notknown      |
| cse        | NaN   | 82.5               | cse           |
| ece        | 90.0  | 90.0               | ece           |
| NaN        | 75.0  | 75.0               | notknown      |
| cse        | NaN   | 82.5               | cse           |

