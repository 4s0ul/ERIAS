# ERIAS HW

Работу выполнили Гаврин И.А. и Панкратов А.Р.

## Установка

1. Убедитесь, что у вас установлен **Python 3.13+** и активировано виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
---

## hw_1.py

### Запуск:

```bash
python hw_1.py
```

### Вывод:

```
User matrix:
 [[3 5 9 2 7]
 [8 6 5 2 2]
 [7 2 2 8 5]
 [7 1 7 3 7]
 [8 9 3 7 9]]
User similarity:
 [[1.    0.839 0.775 0.887 0.873]
 [0.839 1.    0.719 0.752 0.829]
 [0.775 0.719 1.    0.582 0.851]
 [0.887 0.752 0.582 1.    0.864]
 [0.873 0.829 0.851 0.864 1.   ]]
Products similarity:
 [[1.    0.783 0.639 0.887 0.792]
 [0.783 1.    0.746 0.81  0.849]
 [0.639 0.746 1.    0.819 0.889]
 [0.887 0.81  0.819 1.    0.805]
 [0.792 0.849 0.889 0.805 1.   ]]
Closest users: 1 4
Closest products: 3 5
```

---

## hw_2.py

### Запуск:

```bash
python hw_2.py
```

### Вывод:

```
User similarity matrix:
 [[1.    0.766 0.332 0.092 0.781]
 [0.766 1.    0.494 0.566 0.074]
 [0.332 0.494 1.    0.476 0.373]
 [0.092 0.566 0.476 1.    0.495]
 [0.781 0.074 0.373 0.495 1.   ]]
----------
Step  0
[[1.         0.76608825 0.33228197 0.09244681 0.78053119]
 [0.76608825 1.         0.49379528 0.56600283 0.074498  ]
 [0.33228197 0.49379528 1.         0.47588061 0.37277445]
 [0.09244681 0.56600283 0.47588061 1.         0.49504056]
 [0.78053119 0.074498   0.37277445 0.49504056 1.        ]]
---------- Step  1
New distance matrix:
 [[1.    0.494 0.566 0.074 0.766]
 [0.494 1.    0.476 0.373 0.332]
 [0.566 0.476 1.    0.495 0.092]
 [0.074 0.373 0.495 1.    0.781]
 [0.766 0.332 0.092 0.781 0.   ]]
Current clusters: ['U2', 'U3', 'U4', 'U5', '(U1+U1)']
---------- Step  2
New distance matrix:
 [[1.    0.476 0.373 0.332 0.494]
 [0.476 1.    0.495 0.092 0.566]
 [0.373 0.495 1.    0.781 0.074]
 [0.332 0.092 0.781 0.    0.766]
 [0.494 0.566 0.074 0.766 0.   ]]
Current clusters: ['U3', 'U4', 'U5', '(U1+U1)', '(U2+U2)']
---------- Step  3
New distance matrix:
 [[1.    0.495 0.092 0.566 0.476]
 [0.495 1.    0.781 0.074 0.373]
 [0.092 0.781 0.    0.766 0.332]
 [0.566 0.074 0.766 0.    0.494]
 [0.476 0.373 0.332 0.494 0.   ]]
Current clusters: ['U4', 'U5', '(U1+U1)', '(U2+U2)', '(U3+U3)']
---------- Step  4
New distance matrix:
 [[1.    0.781 0.074 0.373 0.495]
 [0.781 0.    0.766 0.332 0.092]
 [0.074 0.766 0.    0.494 0.566]
 [0.373 0.332 0.494 0.    0.476]
 [0.495 0.092 0.566 0.476 0.   ]]
Current clusters: ['U5', '(U1+U1)', '(U2+U2)', '(U3+U3)', '(U4+U4)']
---------- Step  5
New distance matrix:
 [[0.    0.766 0.332 0.092 0.781]
 [0.766 0.    0.494 0.566 0.074]
 [0.332 0.494 0.    0.476 0.373]
 [0.092 0.566 0.476 0.    0.495]
 [0.781 0.074 0.373 0.495 0.   ]]
Current clusters: ['(U1+U1)', '(U2+U2)', '(U3+U3)', '(U4+U4)', '(U5+U5)']
---------- Step  6
New distance matrix:
 [[0.    0.494 0.566 0.766]
 [0.494 0.    0.476 0.373]
 [0.566 0.476 0.    0.495]
 [0.766 0.373 0.495 0.   ]]
Current clusters: ['(U2+U2)', '(U3+U3)', '(U4+U4)', '((U1+U1)+(U5+U5))']
---------- Step  7
New distance matrix:
 [[0.    0.476 0.494]
 [0.476 0.    0.566]
 [0.494 0.566 0.   ]]
Current clusters: ['(U3+U3)', '(U4+U4)', '((U2+U2)+((U1+U1)+(U5+U5)))']
---------- Step  8
Final clusters: ['(U3+U3)', '(U4+U4)', '((U2+U2)+((U1+U1)+(U5+U5)))']
```

---

## hw_3.py

### Запуск:

```bash
python hw_3.py
```

### Вывод:

```
=== Input matrix ===
[[3 4 2 4 4 1 2 2]
 [2 4 3 2 5 4 1 3]
 [5 5 1 3 4 0 3 1]
 [5 4 3 0 0 2 2 1]
 [3 3 5 5 5 2 3 3]
 [0 2 4 2 4 0 1 3]]

=== After filtration ===
[[3 4 2 4 4 1 2 2 2 4 3 2 5 4 1 3 5 5 1 3 4 3 1 5 4 3 2 2 1 3 3 5 5 5 2 3
  3 2 4 2 4 1 3]]

=== COO format ===
row indices: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0]
col indices: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42]
data: [3 4 2 4 4 1 2 2 2 4 3 2 5 4 1 3 5 5 1 3 4 3 1 5 4 3 2 2 1 3 3 5 5 5 2 3 3
 2 4 2 4 1 3]

=== CSR format ===
data: [3 4 2 4 4 1 2 2 2 4 3 2 5 4 1 3 5 5 1 3 4 3 1 5 4 3 2 2 1 3 3 5 5 5 2 3 3
 2 4 2 4 1 3]
indices: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42]
indptr: [ 0 43]

=== ELLPACK format ===
values:
 [[3 4 2 4 4 1 2 2 2 4 3 2 5 4 1 3 5 5 1 3 4 3 1 5 4 3 2 2 1 3 3 5 5 5 2 3
  3 2 4 2 4 1 3]]
column indices:
 [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42]]
max not null in row: 43
```

---

## hw_4.py

### Запуск:

```bash
python hw_4.py
```

### Вывод:

```
=== Input matrix ===
[[0 0 4 1 0]
 [1 3 4 4 3]
 [3 0 0 2 2]
 [0 3 3 3 3]
 [0 1 3 2 0]]
Average product ratings: [2.5   3.    2.333 3.    2.   ]
Top rated product: Product2 (rating 3.00)
User similarity matrix:
[[0.    1.    1.    0.707 0.789]
 [1.    0.    0.944 0.98  1.   ]
 [1.    0.944 0.    0.904 0.99 ]
 [0.707 0.98  0.904 0.    0.99 ]
 [0.789 1.    0.99  0.99  0.   ]]

=== Forecast for User1 by product Product5 ===
Neighbours: ['User2', 'User3']
Predicted rating: 1.083
Average rating User1: 2.000
Not recommended Product5: 1.08 < 4.0 or < average 2.00

=== Forecast for User2 by product Product4 ===
Neighbours: ['User5', 'User4']
Predicted rating: 2.799
Average rating User2: 2.333
Not recommended Product4: 2.80 < 4.0 or < average 2.33

Matrix with new user User6:
[[0 0 4 1 0 0]
 [1 3 4 4 3 0]
 [3 0 0 2 2 0]
 [0 3 3 3 3 0]
 [0 1 3 2 0 0]]

=== Forecast for User6 ===
User6 — new user, popularity-based approach is used
Top rated product: Product2 (average rating 3.00)
```

---

## hw_5.py

### Запуск:

```bash
python hw_5.py
```

### Вывод:

```
=== Input matrix ===
[[1 4 2 4 0]
 [2 4 3 1 0]
 [4 3 4 3 3]
 [0 3 2 0 0]
 [0 3 4 1 3]]
Average product ratings: [2.75 2.5  3.4  2.5  2.75]
Top rated product: Product3 (rating 3.40)
Item similarity matrix:
[[0.    0.84  0.837 0.992 0.784]
 [0.84  0.    0.904 0.998 0.962]
 [0.837 0.904 0.    0.943 0.954]
 [0.992 0.998 0.943 0.    0.943]
 [0.784 0.962 0.954 0.943 0.   ]]

=== Forecast for User2 by product Product4 ===
Similar items: ['Product2', 'Product1']
Predicted rating: 4.000
Average rating User2: 3.400
Recommend Product4: 4.00 ≥ 4.0 and ≥ average 3.40

=== Forecast for User5 by product Product3 ===
Similar items: ['Product5']
Predicted rating: 3.000
Average rating User5: 3.000
Not recommended Product3: 3.00 < 4.0 or < average 3.00
```
