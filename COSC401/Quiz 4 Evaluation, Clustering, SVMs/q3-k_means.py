import numpy as np


def closest_centroid(point, centroids):
    # np.linalg.norm finds distances, then square it and return the argmin. Argmin is the index of the minimum output value
    distances = [np.linalg.norm(point - centroid)**2 for centroid in centroids]
    return np.argmin(distances)

def k_means(dataset, centroids):
    """
    K means for a dataset
    """
    dataset_rows, dataset_columns = dataset.shape
    closest_clusters = np.zeros(dataset_rows)
    old_closest_clusters = np.zeros(dataset_rows)
    #convert centroids to a list
    centroids = list(centroids)

    # while the closest_clusters doesnt change
    while(True):
        #iterate through numpy dataset
        for i in range(dataset_rows):
            #cloesest_centroid contains the index (in centroids) of the closest centroid to the point
            closest_clusters[i] = closest_centroid(dataset[i], centroids)

        #update centroids to mean of each cluster
        for i in range(len(centroids)):

            #use logical indexing to get points in dataset whose index is i in closest_clusters
            bool_ind = (closest_clusters==i);
            cluster_points = dataset[bool_ind]

            # get the average of each column in cluster_points. Axis 0 is along the column
            if(cluster_points.size>0):
                new_centroid = np.mean(cluster_points, axis=0)
                centroids[i] = new_centroid



            # check for convergence
        bool_convergence = old_closest_clusters == closest_clusters

        if (bool_convergence.all()):
            return tuple(centroids)
        else:
            old_closest_clusters = closest_clusters.copy()

wine = sklearn.datasets.load_wine()
data, target = sklearn.utils.shuffle(wine.data, wine.target, random_state=0)
train_data, train_target = data[:-5, :], target[:-5]
test_data, test_target = data[-5:, :], target[-5:]


centroids = (
    np.array([13.0, 2.2, 2.4, 18.1, 107.9, 2.6,
              2.5, 0.3, 1.6, 5.2, 1.0, 3.0, 964.0]),
    np.array([14.5, 1.8, 2.5, 17.0, 106.0, 2.9,
              3.0, 0.3, 2.0, 6.6, 1.1, 3.0, 1300.0]),
    np.array([12.0, 3.1, 2.3, 20.7, 92.8, 2.0,
              1.6, 0.4, 1.0, 4.7, 0.9, 2.0, 550.9])
)
for c in k_means(train_data, centroids):
    print(c)