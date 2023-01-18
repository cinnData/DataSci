# [DS-08] Recommender systems

## What is a recommender system?

A **recommender system** seeks to predict the rating or preference that a subject would give to a product (eg music, books or movies) or social element (eg people or groups) that he/she/it had not yet considered. These two sides of the system are called the **user** and the **item**, respectively.

Recommender systems are common nowadays. Some examples are:

* When viewing a product on **Amazon**, the store recommends additional items, based on information of what other shoppers bought along with the currently selected item.

* **Netflix** predicts the movies that a user might like to watch based on the user's previous ratings and watching habits, also taking into account the characteristics of the film.

* **Last.fm** creates a "station" of recommended songs by observing what bands and individual tracks the user has listened to on a regular basis and comparing them with the listening behavior of other users. Last.fm will propose tracks that do not appear in the user's library, but are often played by other users with similar interests.

* **Social networks**, such as Facebook and LinkedIn, recommend new friends, groups, and other social connections by examining the network of a user and his/her friends.

Recommendation can be user-specific or generic:

* In **user specific-recommendation**, the system generates a sorted list of recommended items for every user. These items can be then be recommended through various channels (eg email). 

* **Generic recommendations** are sent to all the users that satisfy certain conditions, typically that they have purchased a product, or visited its webpage. You have probably seen that at Amazon: "customers interested in this product are also interested in ...". These recommendations may come with a discount for buying both products. 

## Generic recommendation based on confidence

**Confidence** is a simple metric for the association between items. An **association rule** between two items takes usually the form $A \Rightarrow B$. The rule is read as *if A then B*. The confidence of the association is the proportion of users that have requested both items among those that have requested *A*:

$$\hbox{conf}\left(A \Rightarrow B\right) = \frac{\#(AB)}{\#A}\,.$$
The confidence can be regarded as an estimate of the **conditional probability** that a user who has requested *A* also requests *B*. Note that the association is directional, so, in general, $\hbox{conf}\left(A \Rightarrow B\right)\ne \hbox{conf}\left(B \Rightarrow A\right)$. Given an item *A*, you can extract a list of items *B* with the highest confidence $\hbox{conf}\left(A \Rightarrow B\right)$ and recommend those items on top of the list to all the users who show interest on *A*. 

## Collaborative filtering

Besides the simplistic approach of the association rules, there are three classic approaches to recommendation: collaborative filtering, content-based recommendation and knowledge-based recommendation. **Collaborative filtering** (CF) is used for user specific recommendation in many of the most successful recommender systems on the web. The recommendation is based on a list of **top-N** recommended products.

In e-commerce sites, CF systems recommend products to a target customer based on the opinions of other customers. Opinions can be given explicitly as **ratings**, or implicitly derived from purchase and/or browsing records. In this last case, we talk about **implicit ratings**. In a CF system, nothing has to be known about the customers and products, except ratings, either explicit or implicit.

There are two approaches, both based on the **neighbor** concept, used in many data mining methods. The concept is easily grasped in specific examples. For instance, in e-commerce sites like Amazon, the neighbors of a customer are those customers who buy the same products that he/she buys. The neighbors of a product are those products bought by the same customers that buy that product. In practice, the neighbors are extracted from the data by means of a **similarity measure**. 

* In **user-based** systems, every user has a set of *k* neighbors. The number of neighborhood *k* is based on the experience. $k=20$ is typical. Once the neighborhood is formed, the system calculates a predicted rating for every item by averaging the ratings given by the neighbors, averaged by the similarity. The recommendations are based on the ratings predicted for the items that the user has not previously considered. The underlying idea is that a customer is likely to do as similar customers do.

* In **item-based systems**, the neighborhoods are formed with the items. The idea is, now, that a customer is likely to buy products which are similar to those that he/she has already bought. Note that, in this context, the similarity between two items is not based on any characteristic of the items themselves, but on how they are regarded by the users.

## Challenges of CF algorithms

CF systems have been very successful in the past, but their widespread use has revealed some potential challenges such as:

* *Sparsity*. In many commercial systems, even the most active users purchase less than 1% of items. Example: if a bookseller offers 2 million books, a 1% of that would be 20,000 books, an impressive library for a single customer. 

* *Scalability*. In a neighbor algorithm, computation requirements grow with both the number of users and the number of items. With millions of users and items, a typical web-based recommender system may suffer serious scalability problems. 

* *Response time*. The bottleneck in conventional user-based CF algorithms is the search for neighbors among a large population of potential neighbors. Because the relationships between items are relatively static, item-based algorithms may require less online computation. The fact that the item neighborhood is less likely to change over time allows us to pre-compute it. This favors item-based systems. These pre-computed neighborhoods can also be used in generic recommendations.

## Content-based recommender systems

Roughly speaking, **content-based recommendation** is based on the match between the item characteristics and the **user profile**. For instance, a bookseller may recommend Tolstoy's *War and Peace* to a customer who is interested in historical novels. Content-based recommendation can be combined with a CF system, making it a **hybrid system**.

The user profiles may be entered by the users themselves in a template, and stored in a table whose fields have a set of predefined options. Higher complexity in the profile system allows for more sophistication in the recommendations. For instance, users of a movie rental website may enter information about their preferences: Western, thriller, Sci-Fi, etc. The item description will then contain information such as the genre or the director of a movie. Recommendations are based on matching user preferences with item descriptions, which depends strongly on a careful design.

Although user-provided profiles allow for recommendations without any purchase record, they are hard to get in e-commerce, specially rich profiles. So, they can be replaced by historical data on previous purchases by the customer. Then, similar products are recommended. Sometimes product description and similarity calculation are based on **keywords**.

Content-based recommendation has two advantages: (a) it does not require a large user group, and (b) new items can be immediately recommended, as soon as their characteristics are available. Even CF systems need this for new products, which nobody has rated/purchased before.

**Targeted advertising** is a form of content-based recommendation which is already ubiquitous in Internet. The profiles of the users are built with information of various sources, such as browsing activity in Internet and participation in social networks. The impulse of target advertising is such that data on potential customers are becoming a merchandise in this fast-expanding market.

## Knowledge-based recommender systems

Finally, there are recommender systems based on matching customer requirements and technical information about the products recommended. A typical example is the digital camera. These **knowledge-based recommender systems** sometimes allow the customers to send queries to the system.
