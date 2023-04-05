# Example - Amazon jobs

## Introduction

More than 50,000 job offers are posted at the **Amazon Jobs** website (`amazon.jobs/en-gb`). Given the interest of these data for the community, a **web scraping** project at IESE Business School was started, with the focus on this website. It was discovered that the information shown at the Amazon Jobs pages was loaded from JSON documents which could be accessed directly at `amazon.jobs/en-gb/search.json`. So the project was reoriented and the data were extracted directly from the JSON documents, captured by playing with the URL parameters at that site.

This example is based on a data subset resulting from selecting the job category **Software Development** and the business category **Amazon Web Services** (AWS).

## The data set

The file `amzn.csv` (zipped) contains data for 8,116 software developement positions at AWS, captured in November 2021. The variables are:

* `id`, a unique identifier for the position. Example: '996246'.

* `title`, the title of the job, more or less descriptive. Example: 'Senior Software Dev Engineer'.

* `company_name`, the name of the company, within the orbit of AWS. There 65 unique company names in this data set. Example: 'Amazon.com Services LLC'.

* `description`, a description of the job, containing specific detail, but also bombastic rhetoric. Example: 'Are you passionate about enterprise-wide scale compliance management? Are you excited about impactful technical projects ...'.

* `basic_qualifications`, a list of generic qualifications for the job. Example: '4+ years of professional software development experience. 3+ years of programming experience ...'.

* `preferred_qualifications`, a list of more specific qualifications. Example: '6+ years experience building high scale distributed systems that handle big amounts of data. Strong knowledge of data structures, algorithms, and designing for performance, scalability, availability, and internet and OS security fundamentals ...'.

* `job_type`, either 'full-time' or 'part-time' (a few cases).

* `location`, the location of the position. Example: 'US, WA, Seattle'.

* `posted_date`, the date the position was posted at Amazon Jobs website, in the format 'yyyy-mm-dd'.

* `updated_time`, time since the data were updated at the website. Example: '3 months'.

* `team`, a generic indication of the team in which the position is offered, in a a specific terminology of Amazon. There are 23 such teams in this data set. Example: 'team-sde-primary'.

### Questions

Q1. Leaving aside the job ID, which is unique for every job posting, how many duplicates do you find in this data set? Drop the duplicates, so all the positions are different, in at least one field. 

Q2. Which are the top-ten locations for software developement at AWS? Suppose that a potential candidate is interested in finding a position in India. Does Amazon have something for him/her? In which locations? Is the city always included in the location data?

Q3. Which programming languages are more often mentioned in the basic qualifications field? Perhaps Java or Python? Which flavor of C is preferred, C++ or C#? Is SQL still demanded?

Q4. How often is experience mentioned in the preferred qualifications field?
