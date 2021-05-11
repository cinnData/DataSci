## [DS-01] What is data science?

### Data science and data mining

The expression **data scientist** is common nowadays in job descriptions, referred to a mix of data analysis skills and a background of programming languages and data bases. It is, partially, a new name for an old job, since most of the methodology has been available for years. But data science is getting hot, owing to the explosion in the amount of data at hand (big data) and the technology for processing these data (cloud computing).

Data scientist is a broad job title coming in many forms, with the specific demands depending on the industry, the business and the role. So, certain skillsets suit certain positions better than others. Data scientists do not do anything essentially new. We have long had statisticians, analysts, and programmers. What is new is the way different skills are combined in a single profession.

An ancestor of data science is **data mining**, born in the computer science field, This generic expression applies to a heterogeneous set of methods, used to extract information from large data sets. It is understood as *mining knowledge from data*. The typical applications in management are related to Customer Relationship Management (CRM): market basket analysis, churn modeling, credit scoring, etc. From a technical perspective, the topics of a data mining course do not differ much from those of a data science course.

Besides the technical skills, which are the object of the notes, two traits are appreciated in data scientists:

* To be able to ask the right questions. This is harder to evaluate than specific skills, but essential. It involves **domain knowledge** and expertise, coupled with the ability to see the problem, the available data, and match up them. It also requires empathy, neglected in most technical education programs.

* To be able to communicate, creating narratives around their work. They should not live in an abstract, mathematical world, but to understand how to integrate the results into a larger story, recognizing that, if their results are not leading to action, they are meaningless.

### Core competencies

At the business place, the data scientist takes care of the **data pipeline**, which is a set of data processing elements connected in a series, in which the output of one element is the input of the next one. The core competencies are:

* **Data capture**. This starts by managing a data source, using database management skills. However, raw data are not particularly useful in many situations. Data scientists must also understand the data domain so that they can look at the data and begin formulating questions. Finally, they must have data-modeling skills in order to understand how the data are connected.

* **Data wrangling**. This is a generic expression which refers to the operations that have to be performed on the data until they get ready for the analysis. Regarded as the preliminary steps in a data pipeline, we call it  **data preprocessing**. Typical preprocessing steps are: removing duplicates and redundant variables, renaming and/or combining levels of categorical variables, solving the issues associated to missing data, filtering out parts of the data, combining data sets by means of joins and unions and aggregating the data based on one or more grouping variables. When the data are extracted from a database, some of these operations can be integrated in the data extraction step by means of an appropriate query.

* **Analysis**. The analysis typically starts at an exploratory level, using basic statistical tools, much like those that just about everyone learns in college. In many cases, this is followed by an attack with more advanced machine learning tools.

* **Presentation**. Most people do not understand numbers well. They cannot see the patterns that the data scientist sees. It is important to provide a graphical presentation of these patterns to visualize what the data reveal and how to exploit them. More important, the presentation must tell a specific story so the impact of the data is not lost.

* **Developing data products**, such as a recommendation system, a pricing algorithm or a fraud detection procedure. Machine learning techniques (see below) are typically used here.

### A/B types

In a survey at Quora, including the title of this note as one of the questions, Michael Hochster made a distinction which has made fortune. Hochster distinguished between:

* **Type A** (analyst): focused on static data analysis. Essentially a statistician with coding skills. Very similar to a statistician, but knows all the practical details of working with data not taught in the statistics curriculum: data cleaning, methods for dealing with very large data sets, visualization, deep knowledge of a particular domain, writing about data, and so on. Task example: business intelligence.

* **Type B** (builder): focused on building data products. Essentially a software engineer with knowledge in machine learning and statistics. Also a very strong coder. The type B data scientist is mainly interested in using data "in production". Task example: recommendation systems.

Some people see the data scientist as an unapproachable nerd performing miracles on data with math. However, this perspective is changing. In many respects, the data scientist is seen now either an adjunct to a developer or as a new type of developer. The ascendance of software applications which can learn is the essence of this change. For an app to learn, it has to be able to manipulate large databases, discovering new patterns. In addition, it must be able to make predictions, creating new data based on the old data. The greater impact of the melding of data science and app development will be felt in terms of creating altogether new kinds of apps, some of which are not imagined with clarity yet.

### Machine learning

**Machine learning** (ML) is a branch of **artificial intelligence** (AI). You may have heard about other branches, such as robotics, or speech recognition. The objective of machine learning is the development and implementation of **algorithms** which learn from data how to accomplish difficult or tiring tasks.

In general, an algorithm is a set of rules that precisely define a sequence of operations. In the context of machine learning, it is the set of instructions a computer executes to learn from data. This process is called **training**, and we say that we have developed a **model**. For instance, a model which classifies the potential customers of a lending institution as good or bad creditors.

Sometimes, the model learnt from the **training data** is tested on different data which is then called **test data**. This is **model validation**. Validation is needed with models whose complexity allows them to overfit the data. **Overfitting** happens when the performance of a model with fresh data is significantly worse than its performance with the training data. Overfitting is a fact of life for many machine learning methods such as neural networks, so validation is integrated in the development of predictive models.

### Supervised and unsupervised learning

In machine learning, based on the structure of the data used in the training process, it is usual to distinguish between supervised and unsupervised learning. Roughly speaking, **supervised learning** is what the statisticians call prediction, that is, the description of one variable (*Y*), in terms of other variables (the *X*'s). In the ML context, *Y* is called **target**, and the *X*'s are called **features**. The units on which the features and the target are observed are called **samples** (this term has a different meaning in statistics).

The term **regression** applies to the prediction of a numeric target, and the term **classification** to the prediction of a categorical one. In **binary classification**, there are only two target values or **classes**, while, in **multi-class classification**, there can be three or more. The classification algorithm predicts a probability for every class.

In an example of regression, we may try to predict the price of a house from a set of attributes of that house. In one of classification, to predict whether a customer is going to quit our company, from his/her demographics plus some measures of customer activity.

In **unsupervised leaning**, there is no target to be predicted (only *X*'s). The objective is to learn patterns from the data. Unsupervised learning is more difficult, and more creative, than supervised learning. The two classics of unsupervised learning are **clustering**, which consists in grouping objects based on their similarity, and **association rules** mining, which consists in extracting from the data rules such as *if A, then B*. A typical application of clustering in business is **customer segmentation**. Association rules are applied in **market basket analysis**, to associate products that are purchased (or viewed in a website) together. Other relevant examples of unsupervised learning are **dimensionality reduction** and **anomaly detection**.

### Other variations

In-between supervised and unsupervised learning, we have **semisupervised learning**. Another variation is **reinforcement learning**, which is one of the currrent trending ML topics, because of its unexpected success in playing games like go and StarCraft II. It is not considered as supervised nor as unsupervised learning. For more information on this, see Chapter 1 of Géron (2017).

From the point of view of the practical implementation, we can also distinguish between batch and on-line learning. In **batch learning**, the algorithm is trained and tested on given data sets and applied for some time without modification. In **on-line training**, it is continuously retrained with the incoming data. The choice between batch and continuous learning depends on practical issues, rather than on theoretical arguments.

### Data science in the computer

The user interacts with data science software applications in three possible ways:

* Conventional menus and mouse-clicking, as in Excel.

* Programming code.

* Visual programming, based on flow charts which are a graphical translation of code.

These notes are based on code. More specifically, they use Python, which is, currently, one of the leading choices of data scientists, in fierce competition with R. Just a few years ago, data mining textbooks, such as Larose (2005), were using visual programming or menus in their examples, but, nowadays, almost all the data science textbooks are based on R or Python, and the examples include code.

The majority of the data science tasks of are performed on **structured data**, that is, on data sets in tabular form, with rows and columns. The rows correspond to the samples, which are typically individuals, companies or transactions. The columns correspond to the features. Typically, the features are either **numeric**, as the amount paid in a transaction, or **categorical** (also called nominal), as gender. Nevertheless, there are also methods for dealing with **string** (text) data and **datetimes**. Categorical features are typically managed through with 1/0 valued **dummies**.

In the Python implementation of data science, tabular data sets are typically managed as objects called **data frames**. Data frames were born in R, but have been adopted by other languages like Python and Scala. Roughly speaking, a data frame is a collection of data (column) vectors, all of the same length. All the data points in the same column are of the same type, but the data frame can contain columns of different types.

### References

1. E Alpaydin (2016), *Machine Learning*, MIT Press.

2. S Berinato (2019), Data Science and the Art of Persuasion, *Harvard Business Review*, January-February.

3. F Chollet (2017), *Deep Learning with Python*, Manning.

4. P Domingos (2015), *The Master Algorithm, Basic Books.

5. A Géron (2017), *Hands-On Machine Learning with Scikit-Learn & TensorFlow*, O'Reilly.

6. JD Kelleher & B Tierney (2018), *Data Science*, MIT Press.

7. DT Larose (2005), *Discovering Knowledge in Data*, Wiley.

8. F Provost & T Fawcett (2013), *Data Science for Business --- What You Need to Know About Data Mining and Data-Analytic Thinking*, O'Reilly.
