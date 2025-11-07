import numpy as np
from loguru import logger


def cosine_similarity_users(mat, u1, u2):
    u1_ratings = mat[:, u1]
    u2_ratings = mat[:, u2]
    mask = (u1_ratings != 0) & (u2_ratings != 0)
    if not np.any(mask):
        return 0.0
    a = u1_ratings[mask]
    b = u2_ratings[mask]
    num = np.dot(a, b)
    den = np.linalg.norm(a) * np.linalg.norm(b)
    return num / den if den != 0 else 0.0


def build_similarity_matrix(mat):
    n_users = mat.shape[1]
    S = np.zeros((n_users, n_users))
    for i in range(n_users):
        for j in range(i):
            S[i, j] = cosine_similarity_users(mat, i, j)
            S[j, i] = S[i, j]
    return S


def average_user_rating(mat, user_idx):
    ratings = mat[:, user_idx]
    nz = ratings[ratings != 0]
    return np.mean(nz) if nz.size > 0 else 0.0


def predict_rating(mat, S, user_idx, item_idx, k=2):
    n_users = mat.shape[1]
    candidates = [
        u for u in range(n_users) if (u != user_idx and mat[item_idx, u] != 0)
    ]
    if len(candidates) == 0:
        logger.warning("No users have rated this product yet")
        return None, []

    sims = np.array([S[user_idx, u] for u in candidates])
    if len(candidates) < k:
        top_idxs = np.argsort(-sims)
    else:
        top_idxs = np.argsort(-sims)[:k]
    neighbors = [candidates[i] for i in top_idxs]

    user_mean = average_user_rating(mat, user_idx)
    num, den = 0.0, 0.0
    for v in neighbors:
        sim = S[user_idx, v]
        v_mean = average_user_rating(mat, v)
        num += sim * (mat[item_idx, v] - v_mean)
        den += abs(sim)
    if den == 0:
        return None, neighbors
    pred = user_mean + num / den
    return pred, neighbors


def popularity_recommendation(mat):
    means = []
    for i in range(mat.shape[0]):
        row = mat[i, :]
        nz = row[row != 0]
        means.append(np.mean(nz) if nz.size > 0 else 0)
    means = np.array(means)
    return int(np.argmax(means)), means


def evaluate_recommendation(
    mat,
    S,
    user_idx,
    item_idx=None,
    k=2,
    threshold=4.0,
    user_names=None,
    item_names=None,
):
    u_name = user_names[user_idx] if user_names else f"User{user_idx + 1}"

    if np.all(mat[:, user_idx] == 0):
        print(f"\n=== Forecast for {u_name} ===")
        print(f"{u_name} — new user, popularity-based approach is used")
        best_idx, means = popularity_recommendation(mat)
        best_item = item_names[best_idx] if item_names else f"P{best_idx + 1}"
        print(f"Top rated product: {best_item} (average rating {means[best_idx]:.2f})")
        return

    i_name = item_names[item_idx] if item_names else f"P{item_idx + 1}"
    print(f"\n=== Forecast for {u_name} by product {i_name} ===")

    pred, neighbors = predict_rating(mat, S, user_idx, item_idx, k=k)
    if pred is None:
        logger.warning("Insufficient data to make a prediction")
        return

    print(
        f"Neighbours: {[user_names[n] for n in neighbors] if user_names else neighbors}"
    )
    print(f"Predicted rating: {pred:.3f}")
    u_mean = average_user_rating(mat, user_idx)
    print(f"Average rating {u_name}: {u_mean:.3f}")
    if pred >= threshold and pred >= u_mean:
        print(
            f"Recommend {i_name}: {pred:.2f} ≥ {threshold} and ≥ average {u_mean:.2f}"
        )
    else:
        print(
            f"Not recommended {i_name}: {pred:.2f} < {threshold} or < average {u_mean:.2f}"
        )


matrix = np.random.randint(0, 5, size=(5, 5))
user_names = ["User1", "User2", "User3", "User4", "User5"]
item_names = ["Product1", "Product2", "Product3", "Product4", "Product5"]

print("=== Input matrix ===")
print(matrix)

best_idx, means = popularity_recommendation(matrix)
print("Average product ratings:", np.round(means, 3))
print(f"Top rated product: {item_names[best_idx]} (rating {means[best_idx]:.2f})")

S = build_similarity_matrix(matrix)
print("User similarity matrix:")
print(np.round(S, 3))

evaluate_recommendation(
    matrix,
    S,
    user_idx=0,
    item_idx=4,
    k=2,
    threshold=4.0,
    user_names=user_names,
    item_names=item_names,
)
evaluate_recommendation(
    matrix,
    S,
    user_idx=1,
    item_idx=3,
    k=2,
    threshold=4.0,
    user_names=user_names,
    item_names=item_names,
)

matrix_new = np.column_stack([matrix, np.zeros(matrix.shape[0], dtype=int)])
user_names_new = user_names + ["User6"]

print("\nMatrix with new user User6:")
print(matrix_new)

evaluate_recommendation(
    matrix_new,
    S=None,
    user_idx=5,
    item_idx=None,
    user_names=user_names_new,
    item_names=item_names,
)
