# KMeans algorithm and the Elbow criterion

"The idea behind k-Means Clustering is to take a bunch of data and determine if there are any natural clusters (groups of related objects) within the data.

The k-Means algorithm is a so-called unsupervised learning algorithm. We don't know in advance what patterns exist in the data -- it has no formal classification to it -- but we would like to see if we can divide the data into groups somehow.

For example, you can use k-Means to find what are the 3 most prominent colors in an image by telling it to group pixels into 3 clusters based on their color value. Or you can use it to group related news articles together, without deciding beforehand what categories to use. The algorithm will automatically figure out what the best groups are.

The "k" in k-Means is a number. The algorithm assumes that there are k centers within the data that the various data elements are scattered around. The data that is closest to these so-called centroids become classified or grouped together.

k-Means doesn't tell you what the classifier is for each particular data group. After dividing news articles into groups, it doesn't say that group 1 is about science, group 2 is about celebrities, group 3 is about the upcoming election, etc. You only know that related news stories are now together, but not necessarily what that relationship signifies. k-Means only assists in trying to find what clusters potentially exist."

-- taken from [Swift Algorithm Club](https://github.com/raywenderlich/swift-algorithm-club/tree/master/K-Means)'s explantation of the algorithm

Repository contains:
- Code for fitting [scikit-learn](http://scikit-learn.org/)'s [K-Means](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) model to the [iris dataset](https://archive.ics.uci.edu/ml/datasets/Iris).
- Code for determining optimal number of clusters for K-means algorithm using the '_elbow criterion_'.
- IPython notebook combining the above two as an interactive tutorial.

### Running the notebook:
- Clone the repo.
  `git clone https://github.com/analyticalmonk/KMeans_elbow`
- Change into the repo's directory.
  `cd KMeans_elbow`
- Install the requirements.
  `pip install -r requirements.txt`
- Start the notebook.
  `jupyter notebook kmeans_elbow.ipynb`

If you are new to Jupyter notebooks, check out the official [Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/).

Reference:
- [Coursera's Machine Learning: K-Means algorithm](https://www.coursera.org/learn/machine-learning/lecture/93VPG/k-means-algorithm)
- [Using the elbow method to determine the optimal number of clusters for k-means clustering](https://bl.ocks.org/rpgove/0060ff3b656618e9136b)
- [k-Means clustering](https://github.com/raywenderlich/swift-algorithm-club/tree/master/K-Means)
