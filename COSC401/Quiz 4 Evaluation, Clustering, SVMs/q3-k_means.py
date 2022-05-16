import numpy as np
def euclidean_distance(x, y):
    """
    Euclidean distance between two points
    """
    return np.sqrt(np.sum((x - y)**2))
def closest_centroid(point, centroids):
    # np.linalg.norm finds distances, then square it and return the argmin. Argmin is the index of the minimum output value
    distances = [np.linalg.norm(point - centroid)**2 for centroid in centroids]
    return np.argmin(distances)

def k_means(dataset, centroids):
    """
    K means for a dataset
    """
    num_Clusters = len(centroids)
    dataset_rows, dataset_columns = dataset.shape
    #create empty numpy array to store the cluster labels
    cluster_labels = np.zeros(dataset_rows)

    #iterate through numpy dataset
    for i in range(dataset_rows):
        #cloesest_centroid contains the index (in centroids) of the closest centroid to the point
        cluster_labels[i] = closest_centroid(dataset[i], centroids)
        print(cluster_labels)

    #update centroids to mean of each cluster
    for i in range(len(centroids)):
        centroid = centroids[i]
        #get the value at the index of the cluster label where (cluster_labels == i)
        cluster = dataset[np.where(cluster_labels[i] == centroid)]
        #print(cluster)
        #calculate the mean of the cluster


        #get all the points in the cluster where the cluster label is equal to that centroid
        print(i)
        cluster_points = dataset[np.where(cluster_labels == i)]
        print(cluster_points)

        #update centroid

dataset = np.array([
    [0.1, 0.1],
    [0.2, 0.2],
    [0.3,0.3],
    [0.8, 0.8],
    [0.9, 0.9]
])
centroids = (np.array([0., 0.]), np.array([1., 1.]))
for c in k_means(dataset, centroids):
    print(c)