# Elbow function
# var sse = {};
# for (var k = 1; k <= maxK; ++k) {
#     sse[k] = 0;
#     clusters = kmeans(dataset, k);
#     clusters.forEach(function(cluster) {
#         mean = clusterMean(cluster);
#         cluster.forEach(function(datapoint) {
#             sse[k] += Math.pow(datapoint - mean, 2);
#         });
#     });
# }

def elbow_plot(data, maxK=10, seed_centroids=None):
    sse = {}
    for k in range(1, maxK):
        print "k: ", k
        if seed_centroids is not None:
            seeds = seed_centroids.head(k)
            kmeans = KMeans(n_clusters=k, max_iter=500, n_init=100, random_state=0, init=np.reshape(seeds, (k,1))).fit(data[['distance']])
            data["clusters"] = kmeans.labels_
            plt.figure()
            for i in range(1, k):
                cluster_generator(data,i,color_codes[i-1])
        else:
            kmeans = KMeans(n_clusters=k, max_iter=300, n_init=100, random_state=0).fit(data[['distance']])
            data["clusters"] = kmeans.labels_
            plt.figure()
            for i in range(1, k):
                cluster_generator(data,i,color_codes[i-1])
        # Inertia: Sum of distances of samples to their closest cluster center
        sse[k] = kmeans.inertia_
    plt.figure()
    plt.plot(sse.keys(), sse.values())
    return

# elbow_plot(data)
