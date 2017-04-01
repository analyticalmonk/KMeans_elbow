# KMeans_elbow
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
