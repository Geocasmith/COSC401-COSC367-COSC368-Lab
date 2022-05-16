import hashlib
import numpy as np

def pseudo_random(seed=0xdeadbeef):
    """generate an infinite stream of pseudo-random numbers"""
    state = (0xffffffff & seed)/0xffffffff
    while True:
        h = hashlib.sha256()
        h.update(bytes(str(state), encoding='utf8'))
        bits = int.from_bytes(h.digest()[-8:], 'big')
        state = bits >> 32
        r = (0xffffffff & bits)/0xffffffff
        yield r

def generate_random_vector(bounds, r):
    return np.array([(high - low) * next(r) + low for low, high in bounds])


def k_means_random_restart(dataset, k, restarts, seed=None):
    bounds = list(zip(np.min(dataset, axis=0), np.max(dataset, axis=0)))
    r = pseudo_random(seed=seed) if seed else pseudo_random()
    models = []
    for _ in range(restarts):
        random_centroids = tuple(generate_random_vector(bounds, r)
                                 for _ in range(k))
        new_centroids = k_means(dataset, random_centroids)
        clusters = cluster_points(new_centroids, dataset)
        if any(len(c) == 0 for c in clusters):
            continue
        models.append((goodness(clusters), new_centroids))
    return max(models, key=lambda x: x[0])[1]