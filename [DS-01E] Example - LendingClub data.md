# [DS-01E] Example - LendingClub data

## Introduction

**LendingClub** is a financial services company headquartered in San Francisco, California. It was the first **peer-to-peer lender** to register its offerings as securities with the Securities and Exchange Commission (SEC) and to offer loan trading on a secondary market. At its height, LendingClub was the world's largest peer-to-peer lending platform. The company reported that $15.98 billion in loans had been originated through its platform up to December 31, 2015. Renaud Laplanche, the company’s founder and CEO, received The Economist Innovation Award in 2014 for the consumer products category.

LendingClub enabled borrowers to create unsecured personal loans between $1,000 and $40,000. Investors were able to search and browse the loan listings on the LendingClub website, selecting loans on which to invest, based on the information supplied about the borrower, amount of loan, loan grade, and loan purpose. Those investors made money from the interest on these loans, while LendingClub made money by charging borrowers an **origination fee** and investors a **service fee**. All personal loans offered by LendingClub were **fixed rate** loans.

Like other peer-to-peer lenders, LendingClub experienced increasing difficulty attracting investors during early 2016. This led the firm to increase the interest rate on three occasions during the first months of the year. The increase in interest rates and concerns over the impact of the slowing US economy caused a large drop in the LendingClub's share price.

In April 2016, a LendingClub employee reported to Laplanche that the dates on approximately $3 million in the firm's loans appeared to have been altered. LendingClub's internal auditor engaged an outside firm to investigate the report. Additional problems with loans were found, including that $22 million in loans which had been sold to an investment bank did not in fact meet the bank's investment criteria. LendingClub bought these loans back from the bank and resold them.

*The New York Times* reported that the investigation found that Laplanche had not disclosed to the board that he owned part of an investment fund which LendingClub was considering purchasing. *The Wall Street Journal* also stated that Laplanche was found to have not fully disclosed what he knew about the problematic loans.

On May 6, LendingClub's board made it clear to Laplanche that he no longer had their confidence, leading to his resignation. Three of the firm's other managers had also been fired or had resigned by that time as a result of the problematic loans. LendingClub's stock price fell by a further 34% after Laplanche's departure was announced. This placed the stock price at 70% of the price at the time of the firm's initial public offering. The Securities and Exchange Commission was reported to be investigating the LendingClub's disclosures to investors.

In December 2017, *Financial Times* reported that LendingClub "has struggled to overcome the effects of a governance scandal last May", and that the firm "has battled to keep big investors buying loans" despite improvements to its internal governance. These challenges have led it to raise its loss estimate, and have led to further drops in its share price. At this time many other peer-to-peer lending companies were also experiencing difficulties. LendingClub grew to $10.8 billion in annual loan originations in the year 2018.

In an interview with *Business Insider* in December 2019, executive Valerie Kay noted that LendingClub had switched focus to institutional investors as well as its traditional peer-to-peer lending through a new project called "Scale", focused on delivering representative samples of loans instead of individual loans. 

In April 2020, the company announced it would lay off around one third of its employees in anticipation of the economic downturn resulting from the COVID-19 pandemic. In August, it discontinued its secondary trading platform, hosted by Folio, reducing liquidity for existing peer-to-peer investors. In October, LendingClub ceased all new loan accounts on their website as part of restructuring into a neobank after the acquisition of Radius Bank. In December 2020, the company ceased to operate as a peer-to-peer lender.

## The data set

The data set for this example contains data on the personal loans given by LendingClub from August 20812 through September 2020, split in four zipped CSV files. It covers 2,925,493 loans. Only those loans for which the loan amount was funded are included. This means excluding a 0.07% of the records.

The columns are:

* `id`, a unique identifier for the loan.

* `loan_amnt`, the listed amount of the loan applied for by the borrower.

* `term`, the number of (monthly) payments on the loan. Values are either 36 or 60.

* `int_rate`, the interest rate (%) on the loan.

* `installment`, the monthly payment owed by the borrower (US dollar).

* `grade`, the loan grade as assigned by LendingClub. A letter (A-G) plus a number (1-5). A1 is the best grade and G5 the worst one.

* `emp_title`, the job title supplied by the borrower when applying for the loan. Missing for about 260,000 loans.

* `emp_length`, the employment length in years. Eleven possible values, from '< 1 year' to '10+ years'. Missing for about 205,000 loans.

* `home_ownership`, the home ownership status provided by the borrower during registration or obtained from the credit report. The values are 'ANY', 'MORTGAGE', 'NONE', 'OTHER', 'OWN' and 'RENT'.

* `annual_inc`, the self-reported annual income provided by the borrower during registration.

* `verification_status`, whether the borrower's income was verified by LendingClub, not verified, or the income source was verified.

* `issued`, the month the loan was funded. From '2008-04' through '2020-10'.

* `purpose`, a category provided by the borrower for the loan request. Fourteen values: 'car', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business', 'vacation' and 'wedding'.

* `addr_state`, the state provided by the borrower in the loan application. 51 values, from 'AK' through 'WY'.

* `dti`, the **debt to income ratio** (%), calculated as the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested loan, divided by the borrower’s self-reported monthly income. Missing for about 3,100 loans.

* `fico`, the lower boundary range the borrower's **FICO score** at loan origination belongs to. FICO scores are assigned by the Fair Isaac Corporation (FICO). Lenders use FICO scores along with other details on borrowers credit reports to assess credit risk and determine whether to extend credit. They take into account data in five areas: payment history, the current level of indebtedness, types of credit used, length of credit history and new credit accounts.

* `initial_list_status`, the initial listing status of the loan. The possible values are 'w' (whole) and 'f' (fractional). Loans listed 'w' become available for fractional funding (and vice versa) if there are no buyers within a certain time frame.

* `application_type`, indicates whether the loan is an individual application or a joint application of two co-borrowers.

* `loan_status`, the current status of the loan. Eight values: 'Charged Off', 'Current', 'Default', 'Fully Paid', 'In Grace Period', 'Issued', 'Late (16-30 days)' and 'Late (31-120 days)'. LendingClub charges off a loan when further payments were not reasonably expected. Generally, charge-offs occur no later than 30 days after the loan enters the default status. Once a loan is charged off, the remaining principal balance is deducted from the account balance.

## Questions

Q1. Is there a clear **time trend** in the **number of loans** given by LendingClub along its working period as a peer-to-peer lender?

Q2. Some of the features in this data set have a relevant proportion of **missing values**. One of them is the **job title**. Has the proportion of missing job titles been about the same along this period, or there has been a substantial variation?

Q3. LendingClub **grades** the loans of an accepted borrowers based on a risk assessment of that borrower. Is the **interest rate** directly determined by the grade? How much variation can you expect among loans with the same grade?  

Q4. The **loan period** is either three or five years. Add this number of years to the date the loan was funded, to get a final date. Then use this date to filter out the loans whose final date is 2020-01 or later. In the resulting data set, only a few loans will have status different from 'Charged Off' and 'Fully Paid'. Drop them, so that `loan_status` becomes a binary variable. Has the **charged-off rate** been stable along this period?  

## Import the data

In this course, we use the Pandas function `read_csv()` to import the data from the source files. These files are CSV files, zipped when they are too big. First, we import that package.

```
In [1]: import pandas as pd
```

The source files for this course are in a **GitHub repository**, so we use a **remote path** to get access. This path will be the same for all the examples of this course. 

```
In [2]: path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
```

The source files of this example come zipped, but `read_csv()` can manage this without any extra argument if the file extension is `.zip`. With the argument `index_col=0`, the first column of the CSV files, whose header is `id`, is taken as the **index**, so the resulting data frames will have 18 columns.

``` 
In [3]: df1 = pd.read_csv(path + 'lending-1.csv.zip', index_col=0)
   ...: df2 = pd.read_csv(path + 'lending-2.csv.zip', index_col=0)
   ...: df3 = pd.read_csv(path + 'lending-3.csv.zip', index_col=0)
   ...: df4 = pd.read_csv(path + 'lending-4.csv.zip', index_col=0)
```

So, we have four data frames, one for each source file. With the Pandas function `concat`, we can get the **union** of the four data subsets.

```
In [4]: df = pd.concat([df1, df2, df3, df4])
```

## Exploring the data

To explore the data set, we use the standard Pandas methods. First, the method `.info()` prints a report of the data frame content. The default of this report includes the non-null counts only when the data frame is smaller than a certain size (specified somewhere), which is not the case here. The argument `show_counts=True` forces the counts to be printed, irrespective of the data frame's size. As explained in the introduction of this example, there are missing values in some columns.

```
In [5]: df.info(show_counts=True)
<class 'pandas.core.frame.DataFrame'>
Int64Index: 2923423 entries, 1077501 to 99799684
Data columns (total 18 columns):
 #   Column               Non-Null Count    Dtype  
---  ------               --------------    -----  
 0   loan_amnt            2923423 non-null  int64  
 1   term                 2923423 non-null  int64  
 2   int_rate             2923423 non-null  float64
 3   installment          2923423 non-null  float64
 4   grade                2923423 non-null  object 
 5   emp_title            2659461 non-null  object 
 6   emp_length           2718240 non-null  object 
 7   home_ownership       2923423 non-null  object 
 8   annual_inc           2923423 non-null  int64  
 9   verification_status  2923423 non-null  object 
 10  issued               2923423 non-null  object 
 11  purpose              2923423 non-null  object 
 12  addr_state           2923423 non-null  object 
 13  dti                  2920315 non-null  float64
 14  fico                 2923423 non-null  int64  
 15  initial_list_status  2923423 non-null  object 
 16  application_type     2923423 non-null  object 
 17  loan_status          2923423 non-null  object 
dtypes: float64(3), int64(4), object(11)
memory usage: 423.8+ MB
```

The method `.head()` displays the first five rows, which do not give us any surprise.

```
In [6]: df.head()
Out[6]: 
         loan_amnt  term  int_rate  installment grade  \
id                                                      
1077501       5000    36     10.65       162.87    B2   
1077430       2500    60     15.27        59.83    C4   
1077175       2400    36     15.96        84.33    C5   
1076863      10000    36     13.49       339.31    C1   
1075358       3000    60     12.69        67.79    B5   

                        emp_title emp_length home_ownership  annual_inc  \
id                                                                        
1077501                       NaN  10+ years           RENT       24000   
1077430                     Ryder   < 1 year           RENT       30000   
1077175                       NaN  10+ years           RENT       12252   
1076863       AIR RESOURCES BOARD  10+ years           RENT       49200   
1075358  University Medical Group     1 year           RENT       80000   

        verification_status   issued         purpose addr_state    dti  fico  \
id                                                                             
1077501            Verified  2011-12     credit_card         AZ  27.65   735   
1077430     Source Verified  2011-12             car         GA   1.00   740   
1077175        Not Verified  2011-12  small_business         IL   8.72   735   
1076863     Source Verified  2011-12           other         CA  20.00   690   
1075358     Source Verified  2011-12           other         OR  17.94   695   

        initial_list_status application_type  loan_status  
id                                                         
1077501                   f       Individual   Fully Paid  
1077430                   f       Individual  Charged Off  
1077175                   f       Individual   Fully Paid  
1076863                   f       Individual   Fully Paid  
1075358                   f       Individual   Fully Paid  
```
## Q1. Trend in the number of loans

By applying the method `.value_counts()` to the column `issued`, we get the number of occurrences of every value, so the number of loans for every month. This series is sorted top down, and the unique values of `issued` come in the index. With the method `.sort_index()`, we get the counts in chronological order.

```
In [7]: df['issued'].value_counts().sort_index()
Out[7]: 
2007-06       23
2007-07       59
2007-08       70
2007-09       53
2007-10       98
           ...  
2020-05     2755
2020-06     4134
2020-07     7849
2020-08     8372
2020-09    12178
Name: issued, Length: 160, dtype: int64
```

We can visualize now in a **line chart** (Figure 1) the variation of the number of loans along this period. There was, indeed, a trend upwards, which collapsed at the begining of the last year. 

```
In [8]: df['issued'].value_counts().sort_index().plot(figsize=(8,5),
   ...:        title='Figure 1. Number of loans', xlabel='', color='black', linewidth=1);
```

![](https://github.com/cinnData/DataSci/blob/main/Figures/fig_01e_1.png)

To get the plot, we use the method `.plot()`, whose default produces a line chart. The meaning of the graphic specifications is clear. Without `xlabel=''`, the name of the series, which is `issued`, will appear below the horizontal axis. Note the indexes are not recognized as dates, so the tickmarks in the horizontal axis cannot be set with a date logic. 

## Q2. Missing values

The missing values can already be counted in the report extracted in `In [5]`. Pandas has also the specific method `.isna()` for detecting missing values. Applied to a Pandas data container, it returns a Boolean Pandas container of the same shape, indicating whether a value is or is not missing, term by term. With `.sum()` we can then get the number of missing values for every column. With `.mean()`, the proportion.

```
In [9]: df.isna().sum()
Out[9]: 
loan_amnt                   0
term                        0
int_rate                    0
installment                 0
grade                       0
emp_title              263962
emp_length             205183
home_ownership              0
annual_inc                  0
verification_status         0
issued                      0
purpose                     0
addr_state                  0
dti                      3108
fico                        0
initial_list_status         0
application_type            0
loan_status                 0
dtype: int64
```

To explore how the missingness of the job title varies across months, we add a specific Boolean column.

```
In [10]: df['empl_title_na'] = df.emp_title.isna()
```

Now, we can **group by** month and **aggregate**, getting an aggregate value for every month. Given the variation in the number of loans across months, it is better to use the mean as the aggregate function, to get the proportion of missing values. 

```
In [11]: df[['issued', 'empl_title_na']].groupby('issued').mean()
Out[11]: 
         empl_title_na
issued                
2007-06       0.173913
2007-07       0.135593
2007-08       0.100000
2007-09       0.075472
2007-10       0.061224
...                ...
2020-05       0.096552
2020-06       0.086841
2020-07       0.081666
2020-08       0.082895
2020-09       0.087289

[160 rows x 1 columns]
```

The dates are in the index, already sorted, so we can ask directly for the line chart (Figure 2). This chart suggests that LendingClub has been more permissive with missing information in certain epochs.

```
In [12]: df[['issued', 'empl_title_na']].groupby('issued').mean().plot(figsize=(8,5),
    ...:        title='Figure 2. NA rate for job title', xlabel='', color='black', linewidth=1, legend=False);
```

![](https://github.com/cinnData/DataSci/blob/main/Figures/fig_01e_2.png)

*Note*. The argument `legend=False` is needed here because the default `.plot()`, applied to a data frame, includes legends. This was not needed in `In [8]`, since this method was applied to a series. 

# Q3. Interest rate as a function of the grade

We prepare now a statistical summary of the grade and the interest rate, in three columns. This can be done with the method `.groupby()`, as in `In [11]`, or with the function `pivot_table()`, as we do here. 

```
In [13]: grade_rate = pd.pivot_table(df, values='int_rate', index='grade',
    ...:        aggfunc=['count', 'mean', 'std']).round(2)
    ...: grade_rate.columns = ['count', 'mean', 'std']
    ...: grade_rate
Out[13]: 
        count   mean   std
grade                     
A1     133275   5.97  0.68
A2     101002   6.74  0.50
A3     106282   7.31  0.54
A4     158259   7.86  0.55
A5     156984   8.47  0.63
B1     163406   9.41  0.94
B2     164804  10.26  0.85
B3     162073  10.92  0.86
B4     185031  11.64  0.82
B5     181693  12.30  0.88
C1     178976  13.06  0.87
C2     161700  13.85  0.97
C3     158945  14.46  1.03
C4     153132  15.22  1.06
C5     149177  16.18  1.10
D1     100812  16.96  1.05
D2     108595  18.46  1.50
D3      83014  19.30  2.05
D4      67048  19.94  2.47
D5      56592  21.31  3.44
E1      34789  20.46  2.12
E2      30282  21.07  2.34
E3      27171  21.96  2.52
E4      23169  22.86  2.57
E5      23352  24.23  2.55
F1      13386  24.56  2.83
F2       9286  25.00  2.80
F3       7770  25.79  2.73
F4       6109  26.37  2.77
F5       5161  27.12  2.75
G1       4105  27.86  2.74
G2       2686  27.70  2.60
G3       2091  28.12  2.69
G4       1705  28.59  2.90
G5       1561  28.84  2.95
```

The first column shows that the bulk of the borrowers is in the range A-C, and that the worst grades seldom occur. The second column shows a relevant remarkable variation of the interest rate across grades. The average interest rate looks like a linear function of the grade, which is confirmed by  the following chart (Figure 3). The third column tells us about the within-grade variation of the interest rate.

```
In [14]: grade_rate['mean'].plot(figsize=(5,5), title='Figure 3. Average interest rate vs grade', 
    ...:        xlabel='Grade', color='black', linewidth=1);
```

![](https://github.com/cinnData/DataSci/blob/main/Figures/fig_01e_3.png)

The third column shows that the interest rate is not determined exclusively from the grade, but has a variation within grades (as measured by the standard deviation) which is more or less proportional to the average interest rate.

## Q4. Charged-off loans

To create a column with the final date, let us split `issued` in two parts. For instance `'2007-06'` is `'2007'` plus `'-06'`. The first part can be sliced out as `df['issued'].str[:4]` and the second part as `df['issued'].str[4:]`. We have to convert the first part to integer type and sum 3 or 5 years, depending on the loan term. This is obtained as `df['term']/12`. The double slash `//` denotes **integer division** in Python. Integer division is used here to get an integer as the outcome of the division, because the ordinary division returns type `float`, which will not work for a date.

Pasting the two parts:

```
In [15]: df['final'] = (df['issued'].str[:4].astype(int) + (df['term']//12)).astype(str) + df['issued'].str[4:]
    ...: df[['issued', 'term', 'final']]
Out[15]: 
            issued  term    final
id                               
1077501    2011-12    36  2014-12
1077430    2011-12    60  2016-12
1077175    2011-12    36  2014-12
1076863    2011-12    36  2014-12
1075358    2011-12    60  2016-12
...            ...   ...      ...
102556443  2017-04    60  2022-04
102653304  2017-04    36  2020-04
102628603  2017-04    36  2020-04
102196576  2017-04    36  2020-04
99799684   2017-04    60  2022-04
```

We filter out the loans whose final date is later than 2020, getting a subset of 1,070,945 loans.

```
In [16]: df_closed = df[df['final'] < '2020-01']
    ...: df_closed.shape
Out[16]: (1070945, 21)
```

Most of these loans are either fully paid or charged off, as expected.

```
In [17]: df_closed['loan_status'].value_counts()
Out[17]: 
loan_status
Fully Paid            899874
Charged Off           170938
Default                   64
Current                   34
Late (31-120 days)        26
In Grace Period            6
Late (16-30 days)          3
Name: count, dtype: int64
```

We retain the fully paid and the charged off loans, getting a binary feature. This is done with the method `.isin()`, which selects the rows for which the value of `loan_status` is one of the items of the list specified.

```
In [18]: df_closed = df_closed[df_closed['loan_status'].isin(['Fully Paid', 'Charged Off'])]
```

For clarity, we add a **dummy feature** for the loan being charged off.

```
In [19]: df_closed['charged_off'] = (df_closed['loan_status'] == 'Charged Off').astype(int)
```

Now, we obtain the monthly proportion of charged-off loans by using `.groupby()` as we have done in questions Q1 and Q2, displaying it in a line chart (Figure 4). The charged_off rate seems to have been controlled at about 15% for the last years.  

```
In [20]: df_closed[['issued', 'charged_off']].groupby('issued').mean().plot(figsize=(8,5),
    ...:        title='Figure 4. Charged off rate', xlabel='', color='black', linewidth=1, legend=False);
```

![](https://github.com/cinnData/DataSci/blob/main/Figures/fig_01e_4.png)

## Homework

1. The employment length also shows a relevant number of missing values. Does it change in the same way as the number of missing job titles?

2. The FICO score can be expected to have an influence on the grade. Could you conclude something more specific from the data?

3. Is there a trend in the interest rate?

4. The same for the debt to income ratio and the loan amount.

5. Is there an association between the loan amount and the grade given to the loan?

6. Does the charged-off rate depend on the interest rate as it could be expected, if higher interest rates are applied to riskier loans? Is this the same for the 3-year and the 5-year loans?
