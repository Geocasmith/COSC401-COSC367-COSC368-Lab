import hashlib
import numpy as np
import math


def closest_centroid(point, centroids):
    # np.linalg.norm finds distances, then square it and return the argmin. Argmin is the index of the minimum output valued
    distances = [np.linalg.norm(point - centroid) ** 2 for centroid in centroids]
    return np.argmin(distances)

def k_means(dataset, centroids):
    """
    K means for a dataset
    """
    dataset_rows, dataset_columns = dataset.shape
    closest_clusters = np.zeros(dataset_rows)
    old_closest_clusters = np.zeros(dataset_rows)
    centroids = list(centroids)

    # while the closest_clusters doesnt change
    while (True):
        # iterate through numpy dataset
        for i in range(dataset_rows):
            # cloesest_centroid contains the index (in centroids) of the closest centroid to the point
            closest_clusters[i] = closest_centroid(dataset[i], centroids)

        # update centroids to mean of each cluster
        for i in range(len(centroids)):
            # use logical indexing to get points in dataset whose index is i in closest_clusters
            bool_ind = (closest_clusters == i);
            cluster_points = dataset[bool_ind]
            # get the average of each column in cluster_points. Axis 0 is along the column
            if (cluster_points.size > 0):
                new_centroid = np.mean(cluster_points, axis=0)
                centroids[i] = new_centroid
            # check for convergence
        bool_convergence = old_closest_clusters == closest_clusters

        if (bool_convergence.all()):
            return tuple(centroids)
        else:
            old_closest_clusters = closest_clusters.copy()

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

def cluster_points(new_centroids, dataset):
    clusters = [[] for _ in range(len(new_centroids))]

    # For each point in dataset, find closest centroid index and add it to the list for the corresponding cluster (index of centroid and index of clusters line up)
    for i in range(len(dataset)):
        data_point = dataset[i]
        clusters[closest_centroid(data_point, new_centroids)].append(data_point)
    return clusters

def separation(cluster1, cluster2):
    """Find the smallest distance between points in list cluster1 and list cluster2"""
    smallest_distance = np.inf
    for point1 in cluster1:
        for point2 in cluster2:
            #linalg.norm finds the distance between two points
            dist = np.linalg.norm(point1 - point2)**2
            if dist < smallest_distance:
                smallest_distance = dist
    return smallest_distance

def compactness(cluster1,cluster2):
    """Finds the largest distance between points in list cluster1 and list cluster2"""
    largest_distance = 0
    for point1 in cluster1:
        for point2 in cluster2:
            # linalg.norm finds the distance between two points
            dist = np.linalg.norm(point1 - point2)**2
            if dist > largest_distance:
                largest_distance = dist
    return largest_distance

def goodness(clusters):
    """Finds the goodness by dividing the mean separation of the clusters by the mean compactness of the clusters"""
    sum_separation = 0
    sum_compactness = 0
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if i != j:
                sum_separation += separation(clusters[i], clusters[j])
                sum_compactness += compactness(clusters[i], clusters[j])
    return np.mean(sum_separation)/np.mean(sum_compactness)


import sklearn.datasets
import sklearn.utils

iris = sklearn.datasets.load_iris()
data, target = sklearn.utils.shuffle(iris.data, iris.target, random_state=0)
train_data, train_target = data[:-5, :], target[:-5]
test_data, test_target = data[-5:, :], target[-5:]

centroids = k_means_random_restart(train_data, k=3, restarts=10)


# We suggest you check which centroid each
# element in test_data is closest to, then see test_target.
# Note cluster 0 -> label 1
#      cluster 1 -> label 2
#      cluster 2 -> label 0

for c in sorted([f"{x:7.2}" for x in centroid] for centroid in centroids):
    print(" ".join(c))