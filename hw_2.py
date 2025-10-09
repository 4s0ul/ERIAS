import numpy as np

user_similarity = np.random.rand(5, 5)
user_similarity = (user_similarity + user_similarity.T) / 2
np.fill_diagonal(user_similarity, 1.0)
print("User similarity matrix:\n", np.round(user_similarity, 3))
print("-"*10)

R = 0.6
users = [f"U{i+1}" for i in range(user_similarity.shape[0])]
curr_step = 0

print("Step ", curr_step)
print(user_similarity)

while user_similarity.shape[0] > 1:
    curr_step += 1
    print("-"*10, "Step ", curr_step)
    max_idx = np.unravel_index(np.argmax(user_similarity), user_similarity.shape)
    i, j = max_idx
    max_sim = user_similarity[i, j]
    
    if max_sim < R:
        break

    new_cluster = f"({users[i]}+{users[j]})"

    new_row = np.maximum(user_similarity[i, :], user_similarity[j, :])
    new_row = np.delete(new_row, [i, j])  # убираем старые элементы

    user_similarity = np.delete(user_similarity, [i, j], axis=0)
    user_similarity = np.delete(user_similarity, [i, j], axis=1)

    if user_similarity.shape[0] > 0:
        user_similarity = np.vstack([user_similarity, new_row])
        new_col = np.append(new_row, 0).reshape(-1, 1)
        user_similarity = np.hstack([user_similarity, new_col])

    users = [u for k, u in enumerate(users) if k not in (i, j)] + [new_cluster]

    print("New distance matrix:\n", np.round(user_similarity, 3))
    print(f"Current clusters:", users)

print("Final clusters:", users)
