import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

# Generating random ratings matrix
np.random.seed(42)
users = 6
items = 8
ratings = np.random.randint(0, 6, size=(users, items))
print("=== Input matrix ===")
print(ratings)

# Removing inactive users
active_mask = np.any(ratings > 0, axis=1)
ratings = ratings[active_mask, :]

# Removing low rating products
avg_item_ratings = np.true_divide(ratings.sum(axis=0), (ratings != 0).sum(axis=0), where=(ratings != 0))
avg_item_ratings = np.nan_to_num(avg_item_ratings)
high_rating_mask = avg_item_ratings >= 2
ratings = ratings[high_rating_mask]

# In case of one dim
if ratings.ndim == 1:
    ratings = ratings.reshape(1, -1)

print("\n=== After filtration ===")
print(ratings)

# COO
coo = coo_matrix(ratings)
print("\n=== COO format ===")
print("row indices:", coo.row)
print("col indices:", coo.col)
print("data:", coo.data)

# CSR
csr = csr_matrix(ratings)
print("\n=== CSR format ===")
print("data:", csr.data)
print("indices:", csr.indices)
print("indptr:", csr.indptr)

# ELLPACK
max_nnz = np.max(np.count_nonzero(ratings, axis=1))
rows, cols = ratings.shape
ell_values = np.zeros((rows, max_nnz), dtype=int)
ell_col_idx = np.zeros((rows, max_nnz), dtype=int)

for i in range(rows):
    nz_cols = np.nonzero(ratings[i])[0]
    nz_vals = ratings[i, nz_cols]
    ell_values[i, :len(nz_vals)] = nz_vals
    ell_col_idx[i, :len(nz_cols)] = nz_cols

print("\n=== ELLPACK format ===")
print("values:\n", ell_values)
print("column indices:\n", ell_col_idx)
print(f"max not null in row: {max_nnz}")
