# %%
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=2,
                           n_clusters_per_class=1,
                           weights=[0.05, 0.95],
                           class_sep=0.8, random_state=0)

# %%
from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X, y)
# %%
from sklearn.svm import LinearSVC
clf = LinearSVC()
clf.fit(X, y)

clf_resampled = LinearSVC()
clf_resampled.fit(X_resampled, y_resampled)
# %%
import numpy as np
import matplotlib.pyplot as plt

def plot_data(X, y, nb_classes):
    for i in range(nb_classes):
        X_cls = X[np.where(y==i)]
        plt.scatter(X_cls[:, 0], X_cls[:, 1])
    plt.show()

plot_data(X, y, 2)
plot_data(X_resampled, y_resampled, 2)
# %%
