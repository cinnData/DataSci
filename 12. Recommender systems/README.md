# 12. Recommender systems

### What is a recommender system?

A **recommender system** seeks to predict the rating or preference that a subject would give to a product (eg music, books or movies) or social element (eg people or groups) that he/she/it had not yet considered. These two sides of the system are called the **user** and the **item**, respectively.

Recommender systems are common nowadays. Some examples are:

* When viewing a product on Amazon, the store recommends additional items, based on information of what other shoppers bought along with the currently selected item.

* Netflix predicts the movies that a user might like to watch based on the user's previous ratings and watching habits, also taking into account the characteristics of the film.

* Last.fm creates a "station" of recommended songs by observing what bands and individual tracks the user has listened to on a regular basis and comparing them with the listening behavior of other users. Last.fm will propose tracks that do not appear in the user's library, but are often played by other users with similar interests.

* Social networks, such as Facebook and LinkedIn, recommend new friends, groups, and other social connections by examining the network of a user and his/her friends.

Recommender systems can take three approaches. Most of this note is devoted to the collaborative filtering approach, based on previous data from users' preferences or ratings. Other approaches are content-based recommendation, based on the match between the item characteristics and the user profile, and knowledge-based recommendation, based on matching customer requirements and technical information about the products recommended. 

### Collaborative recommender systems

**Collaborative filtering** (CF) is used in many of the most successful recommender systems on the web. The recommendation is based on a list of **top-N** recommended products.

In e-commerce sites, CF systems recommend products to a target customer based on the opinions of other customers. Opinions can be given explicitly as **ratings** or can be implicitly derived from purchase and/or browsing records. In this last case, we talk about **implicit ratings**. In a CF system, nothing has to be known about the customers and products, except ratings, either explicit or implicit.

There are two approaches, both based on the **neighbor** concept, which is used in many data mining methods. Although there are various methods of determine the neighborhood, discussed later in this note, the concept is easily grasped in specific examples. For instance, in e-commerce sites like Amazon, the neighbors of a customer are those customers who buy the same products that he/she buys. The neighbors of a product are those products bought by the same customers that but that product. In practice, the neighbors are extracted from the data by means of **similarity measure**. 

* In **user-based** systems, every user has a set of neighbors, called the **neighborhood**. Once a set of neighbors is formed, the system calculates a predicted rating for every item by averaging the ratings given by the neighbors. The recommendations are based on the ratings predicted for the items that the user has not previously considered. The underlying idea is that a customer is likely to do as similar customers do.

* In **item-based systems**, the representation is the same, but the neighborhoods are formed with the items. The idea is, now, that a customer is likely to buy products which are similar to those that he/she has already bought. Note that, in this context, the similarity between two items is not based on any characteristic of the items themselves, but on how they are regarded by the users.

In a CF recommender system, the first step is representing the relationship between users and items as a **user/item matrix**, in which the entries are the ratings. Then, to calculate a predicted rating for a pair user/item: (a) we form the neighborhood with the top *k* users/items, and (c) the predicted rating is the (weighted) average of the neighbors' ratings. 

### Similarity measures

The similarity measures used in this context are typically variations of the **cosine formula**, which you may have seen in a linear algebra course. The cosine of two *n*-dimensional vectors *x* and *y* is defined as the dot product divided by the product of their norm,

<img src="https://render.githubusercontent.com/render/math?math=\large \cos(x,y)=\frac{\displaystyle x_1y_1 %2B \cdots %2B x_ny_n}{\displaystyle \sqrt{\big(x_1^2 %2B \cdots %2B x_n^2\big)\big(y_1^2 %2B \cdots %2B y_n^2\big)}}\,.">

Although you can find in other applications the cosine formula applied directly, it is recommended here a previous adjustment of the ratings by subtracting the corresponding user average. In this way we are taking into account the difference in rating scale (or the difference in purchasing power). The resulting formula is called the **adjusted cosine formula**.

In the user-based approach, the adjusted cosine formula is applied to calculate the similarity of two users, that is, of two rows of the user/item matrix. Only the items rated by both users can be used in the calculation (with implicit ratings, this is not an issue). If there are no items shared, or one of there is no variation in the ratings, the similarity is set to zero or coded as missing. As discussed below, if this happens too often, it could be a problem. In the item-based approach, the similarity of two items (columns) is calculated in a similar way. 

Note that, for users (not for items), the formula of the adjusted cosine is identical to that of the correlation. Nevertheless, in its practical application to ratings data, the results will be a bit different, because in the correlation the mean subtracted involves the shared items, while in the adjusted cosine it involves all the available items, shared or not. For implicit ratings, there is no difference.

### Collaborative filtering (1): The user-based approach

In order to simplify later calculations, the similarity of two users is set to zero the following cases:

* When the adjusted cosine formula returns a negative value.

* If the ratings of two customers have no intersection.

* When there no is variation in the two rows involved, so the adjusted cosine is 0/0.

The next step is the neighborhood formation. The neighbors of a customer are the customers with highest similarity. Although there is no definite idea about the optimal number of neighbors used in recommender systems, a number in the range 20--50 is reasonable, according to the experts. Because of the sparsity of the similarity data, some users may not have enough neighbors.

Once the neighbors of a user *u* have been determined, we can calculate a predicted rating for every item the user has not rated yet. The predicted rating is calculated as the weighted average of the ratings of the neighbors, if available, with the weights given by the similarities. The formula is

<img src="https://render.githubusercontent.com/render/math?math=\large \hat R(u,i) = \bar R(u) %2B \frac{\displaystyle \sum_v\big[R(v,i) - \bar R(v)\big]\,s(u,v)} {\displaystyle \sum_v s(u,v)}\,,">

where *R*(*u*,*i*) is the rating of restaurant *i* by user *u*, *s*(*u*,*v*) is the similarity between users *u* and *v*, and the sum is performed across the neighbors of the user *u* who rated item *i*.

Finally, we pick, for for each user, the *N* items with the highest predicted ratings.

### Collaborative filtering (2): The item-based approach

In item-based systems, we start by calculating the *between-item* similarities. Now, the adjusted cosine formula does not coincide with the correlation. To form the neighborhood of each item, we pick, among the other items, those with the highest similarity. 

To get the predicted ratings for an item *i*, needed only for the users who have not rated *i*, we calculate the weighted average of the ratings of the neighbors, with the weights given by the similarities:

<img src="https://render.githubusercontent.com/render/math?math=\large \hat R(u,i)=\frac{\displaystyle\sum_j R(u,j)\,s(i,j)}{\displaystyle\sum_j s(i,j)}\,.">

The sums are performed across the neighbors of item *i* that have been rated by user *u*. Again, the items with the top-*N* predicted ratings provide the recommendation for every user.

### Challenges of CF algorithms

CF systems have been very successful in the past, but their widespread use has revealed some potential challenges such as:

* *Sparsity*. In many commercial systems, even the most active users purchase less than 1% of items. Example: if a bookseller offers 2 million books, a 1% of that would be 20,000 books, an impressive library for a single customer. 

* *Scalability*. In a neighbor algorithm, computation requirements grow with both the number of users and the number of items. With millions of users and items, a typical web-based recommender system may suffer serious scalability problems. 

* *Response time*. The bottleneck in conventional user-based CF algorithms is the search for neighbors among a large population of potential neighbors. Because the relationships between items are relatively static, item-based algorithms may require less online computation. The fact that item neighborhood is less likely to change over time allows us to pre-compute it. This favors item-based systems.

These pre-computed neighborhoods can also be used in (not user specific) **generic recommendations**, such as those of Amazon (customers interested in this product are also interested in ...). These recommendations typically come with a discount for buying both products. 

### Recommendation based on association rules

**Association rules** can be used to develop top-*N* recommender systems in the following way. For each customer, we create a transaction containing the products that he/she has purchased in the past. We then use an association mining algorithm under minimum support and minimum confidence constraints. 

For a target customer, the top-*N* recommended products are selected as follows: (a) we find the rules in which this customer has purchased all the products in the left side of the rule, (b) we sort the products on the right side of these rules based on the confidence of the corresponding rule, and (c) we pick the *N* highest ranked products. 

Association rules can also be used on generic recommendations. We set the antecedent of the rule equal to a particular item and the length of the rule to 2, taking the rules with high confidence as recommendations.

### Content-based recommender systems

Roughly speaking, **content-based recommendation** is based on the match between the item characteristics and the **user profile**. For instance, a bookseller may recommend Tolstoy's *War and Peace* to a customer who is interested in historical novels. Content-based recommendation is frequently combined with a CF system, making it a **hybrid system**.

The user profile may be entered by the user themself in a template and stored in a table whose fields have a set of predefined options. Higher complexity in the profile system allows for more sophistication in the recommendations. For instance, users of a movie rental website may enter information about their preferences: Western, thriller, Sci-Fi, etc. The item description may contain information such as the genre or the director of a movie. Matching user preferences with item descriptions depends strongly on a careful design.

Although user-provided profiles allow for recommendations without any purchase record, they are hard to get in e-commerce, specially rich profiles. So, they can be replaced by historical data on previous purchases by the customer. Then, similar products are recommended. When the similarity is based on product description, it is still considered as content-based. Sometimes product description and similarity calculation can be based on keywords.

Content-based recommendation has two advantages: (a) it does not require a large user group, and (b) new items can be immediately recommended, as soon as their characteristics are available. Even CF systems need this for new products, which nobody has rated/purchased before.

**Targeted advertising** is a form of content-based recommendation which is already ubiquitous in Internet. The profiles of the users are built with information of various sources, such as browsing activity in Internet and participation in social networks. The impulse of target advertising is such that data on potential customers are becoming a merchandise in this fast-expanding market.

### Knowledge-based recommender systems

Finally, there are recommender systems based on matching customer requirements and technical information about the products recommended. A typical example is the digital camera. These **knowledge-based recommender systems** sometimes allow the customers send queries to the system.
