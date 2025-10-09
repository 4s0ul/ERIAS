import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


user_prod_matrix = np.random.randint(1, 10, size=(5, 5))
print("User matrix:\n", user_prod_matrix)

user_similarity = cosine_similarity(user_prod_matrix.T)    
print("User similarity:\n", np.round(user_similarity, 3))

product_similarity = cosine_similarity(user_prod_matrix)
print("Products similarity:\n", np.round(product_similarity, 3))

np.fill_diagonal(user_similarity, 0)
np.fill_diagonal(product_similarity, 0)

u_i, u_j = np.unravel_index(np.argmax(user_similarity), user_similarity.shape)
p_i, p_j = np.unravel_index(np.argmax(product_similarity), product_similarity.shape)

print("Closest users:", u_i+1, u_j+1)
print("Closest products:", p_i+1, p_j+1)
