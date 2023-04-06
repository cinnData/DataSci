# [DS-08] Clustering

## What is a clustering algorithm?

A **clustering algorithm** groups samples into **clusters**, based on their similarity. Clustering methods have been applied for a long time in many fields, under specific names. For instance, in marketing, clustering customers is called **market segmentation**. 

There are many clustering methods, all based on the same principle, to achieve the maximum similarity within clusters and the minimum similarity between clusters. This is operationalized through a **similarity measure**. You will find, basically, two approaches to clustering: the **distance-based** methods, such as the $k$-means algorithm, and the **probability-based** methods, such as the EM clustering algorithm. Only the $k$-means algorithm is considered here, because most of the other methods, in spite of their popularity in textbooks, have **scalability** problems, meaning that they do not work, or become too slow, with big data sets.

A warning note: clustering algorithms always produce clusters. But the clusters you get could be useless for their intended application. For instance, if you expect them to help to understand your customers, they have to be described in a intelligible way. This would probably imply a low number of clusters.

Frequently, professors and teaching materials suggest that, for a clustering to be useful, the number of clusters have to be small, which can be adequate when the clusters are intended to be managed by humans. But that is not always the case in business applications. A big e-retailer like Amazon can easily manage hundreds of clusters, with no human mind understanding what they are. Also, in some cases, the clusters are used only to speed up computation. For instance, to get recommendations faster, you can search them within clusters of products.

## Similarities

In the distance-based methods, the similarity of two samples is measured by a distance formula, which is usually the **Euclidean distance**. The Euclidean distance is the ordinary, real-life distance. The following example illustrates this.

Pick two points in a 3-dimensional space, such as $x=(2,-1,3)$ and $y=(2,2,4)$. The distance between them is

$$\textrm{dist}(x,y) = \sqrt{(2-2)^2+((-1)-2)^2+(3-4)^2}=1.414.$$

The general formula, for a $p$-dimensional space, is

$$\textrm{dist}(x,y)=\sqrt{(x_1-y_1 )^2 + \cdots + (x_p-y_p)^2}.$$

This formula can be applied to any pair of rows of a data set with $p$ numeric columns. In the machine learning toolbox, the Euclidean distance is the default similarity measure. Nevertheless, in particular contexts, such as **text mining**, other measures, like the **cosine-based similarity**, are preferred.

## Normalization

It is not rare, in real data, that some features show a much higher variation than the rest. Formulas like the Euclidean distance make those features too influential on the clustering process. To prevent this, the features involved in the clustering process can be normalized. There are two favorite approaches to **normalization**, as we see next.

**In min-max normalization**, all the features are forced, through a linear transformation, into the 0-1 range. The formula for this transformation is

$$Z=\frac{X-\min(X)}{\max(X)-\min(X)}{\,}.$$

Some methods of statistical analysis require the variables to have zero mean and unit variance, so you may find in textbooks the formula

$$Z=\frac{X-\bar X}{\textrm{std}(X)}\,.$$

This is called **standardization**. These transformations are available in some Python packages, like scikit-learn. You can also create a specific function for your preferred normalization formula. For the min-max normalization, this would be:

```
def normalize(x): return (x - np.min(x))/(np.max(x) - np.min(x))
```
For the statistical standardization:

```
def standardize(x): return (x - np.mean(x))/np.std(x)
```

Irrespective of the formula chosen, mind that normalization can change significantly your clusters. In customer segmentation, for instance, this is a relevant issue.

## Cluster centers

Suppose that you wish to group the samples in $k$ clusters using $p$ numeric features. Many clustering methods are based on finding a set of $k$ points in the $p$-dimensional space of the features, called **centers**, and clustering the samples around the centers. Every sample will be assigned to the cluster whose center is most similar. Typically, the similarity is the Euclidean distance.

The centers can also be used to assign a cluster to a new sample which has not been used to find the centers. We just select the cluster whose center is closer to that new sample.

In real-world applications, we look at the center as an artificial sample which we consider as the ``typical element'' of the cluster. The values that this artificial sample takes for the different features are used to produce a description of the cluster, as far as that makes sense. This is the typical approach in customer segmentation. So a marketing manager can describe a segment of customers as individuals above 60, with annual family income between $100,000 and $250,000, who frequently watch soap opera TV comedy series. This would really be a description of the center of that segment.

The methods that use this approach differ on how the centers are extracted from the training data. Let us see how it works in the $k$-means clustering algorithm.

## *k*-means clustering

The **$k$-means algorithm** searches for a set of $k$ centers such that the corresponding clusters have any of the mathematically equivalent properties:

* The center is the average of the samples of the cluster.

* The **distortion**, which the sum of the squared (Euclidean) distances of the samples to the centers of their respective clusters, is minimum.

The $k$-means search is iterative. The steps are:

* Take a random choice of $k$ samples as the initial set of centers.

* Create $k$ clusters so that every sample is in the same cluster as the closest center (in the  Euclidean distance).

* Take the average of every cluster as the new center and reassign the samples based on the new centers.

* Iterate until a prespecified stopping criterion is met.

* The algorithm returns the collection of centers and a vector containing the **cluster labels**.

Despite some drawbacks, $k$-means remains the most widely used clustering algorithm. It is simple, easily understandable and reasonably scalable, and it can be easily modified to deal with streaming data.

In $k$-means clustering, you have to specify the number of clusters $k$. Even if this is something on which you do not have a definite number, you will probably have a preliminary idea, so you will work around that. For instance, you may wish to have a number of clusters from 3 to 6. You will then try $k = 3, 4, 5, 6$, comparing the results. You will probably consider the cluster sizes, since you do not want clusters which are too small, and you will monitor how the clusters change when you increase the number of clusters.

**Stability** is expected from a respectable segmentation. First, mind that, due to the random start, two runs of the $k$-means clustering can give different results. The difference should not be relevant. 

## *k*-means clustering in Python

*k*-means clustering is available in the Python packages **SciPy** and scikit-learn, both included in the Anaconda distribution. This is not difficult to manage if you have a clear mind about what you want to extract from the data, meaning:

* A vector, of length equal to the number of rows of the data set, containing the cluster labels.

* A matrix with one row for every center. For every row, the terms of that row would be the mean values of the features on the corresponding cluster.

I explain here the SciPy option. *k*-means clustering is provided by the subpackage `scipy.cluster.vq`. You can import it, with a friendly name, as:

```
import scipy.cluster.vq as cluster
```

Suppose that `X` is the data matrix (either a NumPy 2D array or a Pandas data frame). The centers are obtained as:

```
center = cluster.kmeans(data, k)[0]
```

Here, `k` is the number of clusters. `cluster.kmeans(X, k)` is a tuple containing two objects: the first one is the center matrix, as a 2D array, and the second one is the average (non-squared) Euclidean distance between the samples and the closest center. This number, which is similar to the distortion, decreases as the number of clusters increases (it would be zero if you extract as many clusters as the number of samples). It can be taken as a measure of the "quality" of a cluster, and use it to decide about the best number of clusters.

The labels are obtained as:

```
label = cluster.vq(data, center)[0]
```
Here, also, `cluster.vq(data, center)` contains two objects. The first one is the vector of cluster labels. The second one is the vector of distances from the samples to the closest center.
