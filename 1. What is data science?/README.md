# 1. What is data science?

### Data science and data mining

The expression **data scientist** is common nowadays in job descriptions, referred to a mix of data analysis skills and a background of programming languages and data bases. It is, partially, a new name for an old job, since most of the methodology has been available for years. But data science is getting hot, owing to the explosion in the amount of data at hand (big data) and the technology for processing these data (cloud computing).

Data scientist is a broad job title coming in many forms, with the specific demands depending on the industry, the business and the role. So, certain skillsets suit certain positions better than others. Data scientists do not do anything essentially new. We have long had statisticians, analysts, and programmers. What is new is the way different skills are combined in a single profession.

An ancestor of data science is **data mining**, born in the computer science field. This generic expression applies to a heterogeneous set of methods, used to extract information from large data sets. It is understood as *mining knowledge from data*. The typical applications in management are related to Customer Relationship Management (CRM): market basket analysis, churn modeling, credit scoring, etc. From a technical perspective, the topics of many data mining courses do not differ much from those of a data science course.

Besides the technical skills, two traits are appreciated in data scientists:

* To be able to **ask the right questions**. This is harder to evaluate than specific skills, but essential. It involves **domain knowledge** and expertise, coupled with the ability to see the problem and the available data, and match up them. It also requires empathy, neglected in most technical education programs.

* To be able to **communicate**, creating narratives around their work. They should understand how to integrate the results into a larger story, recognizing that, if their results are not leading to action, they are meaningless.

### Core competencies

At the business place, the data scientist takes care of the **data pipeline**, which is a set of data processing elements connected in a series, in which the output of one element is the input of the next one. The core competencies are:

* **Data capture**. This starts by managing a data source, using database management skills. Data scientists must also understand the data domain so that they can look at the data and begin formulating questions. Finally, they must have data-modeling skills in order to understand how the data are connected.

* **Data wrangling**. is a generic expression which refers to the operations that are performed on the data until they get ready for the analysis. Regarded as the preliminary steps in a data pipeline, we call this **data preprocessing**. Typical preprocessing steps are: removing duplicates and redundant variables, renaming and/or combining levels of categorical variables, solving the issues associated to missing data, filtering out parts of the data, combining data sets by means of joins and unions and aggregating the data based on one or more grouping variables. When the data are extracted from a database, some of these operations can be integrated in the data extraction step by means of an appropriate query.

* **Analysis**. The analysis typically starts at an exploratory level, using basic statistical tools, much like those that just about everyone learns in college. In many cases, this is followed by an attack with more advanced machine learning tools.

* **Presentation**. Most people do not understand numbers well. They cannot see the patterns that the data scientist sees. It is important to provide a graphical presentation of these patterns to visualize what the data reveal and how to exploit them. More important, the presentation must tell a specific story so the impact of the data is not lost.

* **Developing data products**, such as a recommendation system, a pricing algorithm or a fraud detection procedure. **Machine learning** techniques are typically used here.

### A/B types

In a survey at Quora, including the title of this note as one of the questions, Michael Hochster made a distinction which has made fortune. Hochster distinguished between:

* **Type A** (analyst): focused on static data analysis. Essentially a statistician with coding skills. Very similar to a statistician, but knows all the practical details of working with data not taught in the statistics curriculum: data cleaning, methods for dealing with very large data sets, visualization, deep knowledge of a particular domain, writing about data, and so on. Task example: business intelligence.

* **Type B** (builder): focused on building data products. Essentially a software engineer with knowledge in machine learning and statistics. Also a very strong coder. The type B data scientist is mainly interested in using data "in production". Task example: recommendation systems.

Some people see the data scientist as an unapproachable nerd performing miracles on data with math. However, this perspective is changing. In many respects, the data scientist is seen now either as an adjunct to a developer or as a new type of developer. The ascendance of software applications which can learn drives this change. For an app to learn, it has to be able to manipulate large databases, discovering new patterns. In addition, it must be able to make predictions, creating new data based on the old data. The greater impact of the melding of data science and app development will be felt in terms of creating altogether new kinds of apps, some of which are not imagined with clarity yet.

### Data science in the computer

Users interact with data science software applications in three possible ways:

* Conventional menus and mouse-clicking, as in Tableau.

* Programming code.

* Visual programming, based on flow charts which are a graphical translation of code.

These notes are based on code. More specifically, they use Python, which is, currently, one of the leading choices of data scientists, in fierce competition with R. Just a few years ago, data mining textbooks, such as Larose (2005), were using visual programming or menus in their examples, but, nowadays, almost all the data science textbooks are based on R or Python, and the examples include code.

The majority of the data science tasks of are performed on **structured data**, that is, on data sets in tabular form, with rows and columns. The rows correspond to the samples, which are typically individuals, companies or transactions. The columns correspond to the features. Typically, the features are either **numeric**, as the amount paid in a transaction, or **categorical** (also called nominal), as gender. Nevertheless, there are also methods for dealing with **string** (text) data and **datetimes**. Categorical features are typically managed through with 1/0 valued **dummies**.

In the Python implementation of data science, tabular data sets are typically managed as objects called **data frames**. Data frames were born in R, but have been adopted by other languages, like Python and Scala. Roughly speaking, a data frame is a collection of data (column) vectors, all of the same length. All the data points in the same column are of the same type, but the data frame can contain columns of different types.

### References

1. S Berinato (2019), Data Science and the Art of Persuasion, *Harvard Business Review*, January-February.

2. JD Kelleher & B Tierney (2018), *Data Science*, MIT Press.

3. DT Larose (2005), *Discovering Knowledge in Data*, Wiley.

4. F Provost & T Fawcett (2013), *Data Science for Business --- What You Need to Know About Data Mining and Data-Analytic Thinking*, O'Reilly.
