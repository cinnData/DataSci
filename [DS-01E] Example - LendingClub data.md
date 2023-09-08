# [DS-01E] Example - LendingClub data

## Introduction

**LendingClub** is a financial services company headquartered in San Francisco, California. It was the first **peer-to-peer lender** to register its offerings as securities with the Securities and Exchange Commission (SEC) and to offer loan trading on a secondary market. At its height, LendingClub was the world's largest peer-to-peer lending platform. The company reported that $15.98 billion in loans had been originated through its platform up to December 31, 2015. Renaud Laplanche, the company’s founder and CEO, received The Economist Innovation Award in 2014 for the consumer products category.

LendingClub enabled borrowers to create unsecured personal loans between $1,000 and $40,000. The standard loan period was three years. Investors were able to search and browse the loan listings on the LendingClub website, selecting loans on which to invest, based on the information supplied about the borrower, amount of loan, loan grade, and loan purpose. Those investors made money from the interest on these loans. LendingClub made money by charging borrowers an **origination fee** and investors a **service fee**. All personal loans offered by LendingClub were fixed **rate loans**.

Like other peer-to-peer lenders, LendingClub experienced increasing difficulty attracting investors during early 2016. This led the firm to increase the interest rate on three occasions during the first months of the year. The increase in interest rates and concerns over the impact of the slowing US economy caused a large drop in the LendingClub's share price.

In April 2016, a LendingClub employee reported to Laplanche that the dates on approximately $3 million in the firm's loans appeared to have been altered. LendingClub's internal auditor engaged an outside firm to investigate the report. Additional problems with loans were found, including that $22 million in loans which had been sold to an investment bank did not in fact meet the bank's investment criteria. LendingClub bought these loans back from the bank and resold them.

*The New York Times* reported that the investigation found that Laplanche had not disclosed to the board that he owned part of an investment fund which LendingClub was considering purchasing. *The Wall Street Journal* also stated that Laplanche was found to have not fully disclosed what he knew about the problematic loans.

On May 6, LendingClub's board made it clear to Laplanche that he no longer had their confidence, leading to his resignation on 9 May. The Wall Street Journal reported that Laplanche had been fired by the board. Three of the firm's other managers had also been fired or had resigned by that time as a result of the problematic loans. LendingClub's stock price fell by a further 34% after Laplanche's departure was announced. This placed the stock price at 70% of the price at the time of the firm's initial public offering. As a result of the incident, the Securities and Exchange Commission was reported to be investigating the LendingClub's disclosures to investors.

In December 2017, *Financial Times* reported that LendingClub "has struggled to overcome the effects of a governance scandal last May", and that the firm "has battled to keep big investors buying loans" despite improvements to its internal governance. These challenges have led it to raise its loss estimate, and have led to further drops in its share price. At this time many other peer-to-peer lending companies were also experiencing difficulties.

In an interview with *Business Insider* in December 2019, executive Valerie Kay noted that LendingClub had switched focus to institutional investors as well as its traditional peer-to-peer lending through a new project called "Scale", focused on delivering representative samples of loans instead of individual loans. LendingClub had grown to $10.8 billion in annual loan originations in the year 2018.

In April 2020, the company announced it would lay off around one third of its employees in anticipation of the economic downturn resulting from the COVID-19 pandemic. In August, it discontinued its secondary trading platform, hosted by Folio, reducing liquidity for existing peer-to-peer investors. In October, LendingClub ceased all new loan accounts on their website as part of restructuring into a neobank after the acquisition of Radius Bank. In December 2020, the company ceased to operate as a peer-to-peer lender

## The data set

The data set (split in several zipped CSV files) for this example contains data on the personal loans given by LendingClub from August 20812 through September 2020. It covers 2,925,493 loans. Only those loans for which the loan amount was funded are included. This means excluding a 0.07% of the records.

The columns are:

* `id`, a unique identifier for the loan.

* `loan_amnt`, the listed amount of the loan applied for by the borrower.

* `term`, the number of (monthly) payments on the loan. Values are either 36 or 60.

* `int_rate`, the interest rate on the loan (%).

* `installment`, the monthly payment owed by the borrower (US dollar).

* `grade`, the loan grade as assigned by LendingClub. A letter (A-G) plus a number (1-5). A1 is the best grade and G5 the worst one.

* `emp_title`, the job title supplied by the borrower when applying for the loan. Missing for about 260,000 loans.

* `emp_length`,	the employment length in years. Eleven possible values, from '< 1 year' to '10+ years'. Missing for about 205,000 loans.

* `home_ownership`, the home ownership status provided by the borrower during registration or obtained from the credit report. The values are 'ANY', 'MORTGAGE', 'NONE', 'OTHER', 'OWN' and 'RENT'.

* `annual_inc`, the self-reported annual income provided by the borrower during registration.

* `verification_status`, whether the borrower's income was verified by LendingClub, not verified, or the income source was verified.

* `issued`, the month the loan was funded. From '2008-04' through '2020-10'.

* `purpose`, a category provided by the borrower for the loan request. Fourteen values: 'car', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business', 'vacation' and 'wedding'.

* `addr_state`,	the state provided by the borrower in the loan application. 51 values, from 'AK' through 'WY'.

* `dti`, a ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested loan, divided by the borrower’s self-reported monthly income. Missing for about 3,100 loans.

* `fico`, the lower boundary range the borrower's FICO at loan origination belongs to.

* `open_acc`, the number of open credit lines in the borrower's credit file.

* `total_acc`, the total number of credit lines currently in the borrower's credit file.

* `initial_list_status`, the initial listing status of the loan. The possible values are 'w' (whole) and 'f' (fractional). Loans listed 'w' become available for fractional funding (and vice versa) if there are no buyers within a certain time frame.

* `out_prncp`, the remaining outstanding principal for the total amount funded.

* `total_pymnt`, payments received to date for the total amount funded.

* `total_rec_prncp`, the principal received to date.

* `total_rec_int`, the interest received to date.

* `application_type`, indicates whether the loan is an individual application or a joint application with two co-borrowers.

* `acc_now_delinq`, the number of accounts on which the borrower is now delinquent.

* `avg_cur_bal`, average current balance of all accounts.

* `delinq_amnt`, the past-due amount owed for the accounts on which the borrower is now delinquent.

* `mort_acc`, the number of mortgage accounts.

* `num_actv_bc_tl`,	the number of currently active bankcard accounts.

* `pub_rec_bankruptcies`, the number of public record bankruptcies.

* `tax_liens`, the number of tax liens. A tax lien is a legal claim against the assets of an individual or business that fails to pay taxes owed to the government.

* `total_il_high_credit_limit`, the total installment high credit/credit limit.

* `total_bal_ex_mort`, the total credit balance excluding mortgage.

* `hardship`, whether or not the borrower is on a hardship plan (1/0).

* `debt_settlement` whether or not the borrower, who has charged-off, is working with a debt-settlement company (1/0).

* `loan_status`, the current status of the loan. Eight values: 'Charged Off', 'Current', 'Default', 'Fully Paid', 'In Grace Period', 'Issued', 'Late (16-30 days)' and 'Late (31-120 days)'. LendingClub charges off a loan when we no longer reasonably expect further payments. Generally, charge-offs occur no later than 30 days after the loan enters the default status. Once a loan is charged off, the remaining principal balance is deducted from the account balance.

## Questions

Q1.

Q2.

Q3.


## Import the data

We use here the Pandas funcion `read_csv()` to import the data. First, we import the package:

```
In [1]: import pandas as pd
```

The source file is in a GitHub repository, so we use a remote path to get access. The source file comes zipped, but `.read_csv()` can manage this without any specification if the file extension is `.zip`. With the argument `index_col=0`, the first column of the CSV file, whose header is `id` is taken as the index, so the resulting data frame will have 34 columns.

``` 
In [2]: path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
   ...: filename = path + 'lending.csv.zip'
   ...: df = pd.read_csv(filename, index_col=0)
```

## Exploring tha data

To explore the data set, we use the standard Pandas methods. First, the method `.info()` prints a report of the data frame content. By default, the non-null count is shown only if the data frame is smaller than a certain size specified somewhere (don't ask), which is not the case in this example. The argument `show_counts=True` forces the counts to be printed, irrespective of the data frame's shape. As explained in the introduction of this example, there are missing values in some columns.

```
In [3]: df.info(show_counts=True)
<class 'pandas.core.frame.DataFrame'>
Int64Index: 2923423 entries, 1077501 to 99799684
Data columns (total 34 columns):
 #   Column                      Non-Null Count    Dtype  
---  ------                      --------------    -----  
 0   loan_amnt                   2923423 non-null  int64  
 1   term                        2923423 non-null  int64  
 2   int_rate                    2923423 non-null  float64
 3   installment                 2923423 non-null  float64
 4   grade                       2923423 non-null  object 
 5   emp_title                   2659461 non-null  object 
 6   emp_length                  2718240 non-null  object 
 7   home_ownership              2923423 non-null  object 
 8   annual_inc                  2923423 non-null  int64  
 9   verification_status         2923423 non-null  object 
 10  issued                      2923423 non-null  object 
 11  purpose                     2923423 non-null  object 
 12  addr_state                  2923423 non-null  object 
 13  dti                         2920315 non-null  float64
 14  fico                        2923423 non-null  int64  
 15  open_acc                    2923399 non-null  float64
 16  total_acc                   2923399 non-null  float64
 17  initial_list_status         2923423 non-null  object 
 18  out_prncp                   2923423 non-null  float64
 19  out_prncp_inv               2923423 non-null  float64
 20  total_pymnt                 2923423 non-null  float64
 21  total_rec_prncp             2923423 non-null  float64
 22  total_rec_int               2923423 non-null  float64
 23  application_type            2923423 non-null  object 
 24  acc_now_delinq              2923399 non-null  float64
 25  avg_cur_bal                 2855093 non-null  float64
 26  delinq_amnt                 2923399 non-null  float64
 27  mort_acc                    2875418 non-null  float64
 28  num_actv_bc_tl              2855205 non-null  float64
 29  pub_rec_bankruptcies        2922090 non-null  float64
 30  tax_liens                   2923325 non-null  float64
 31  total_bal_ex_mort           2875418 non-null  float64
 32  total_il_high_credit_limit  2855205 non-null  float64
 33  loan_status                 2923423 non-null  object 
dtypes: float64(19), int64(4), object(11)
memory usage: 780.6+ MB
```

The method `.head()` displays the first five rows.

```
In [4]: df.head()
Out[4]: 
         loan_amnt  term  int_rate  installment grade  \
id                                                      
1077501       5000     3     10.65       162.87    B2   
1077430       2500     6     15.27        59.83    C4   
1077175       2400     3     15.96        84.33    C5   
1076863      10000     3     13.49       339.31    C1   
1075358       3000     6     12.69        67.79    B5   

                        emp_title emp_length home_ownership  annual_inc  \
id                                                                        
1077501                       NaN  10+ years           RENT       24000   
1077430                     Ryder   < 1 year           RENT       30000   
1077175                       NaN  10+ years           RENT       12252   
1076863       AIR RESOURCES BOARD  10+ years           RENT       49200   
1075358  University Medical Group     1 year           RENT       80000   

        verification_status  ... acc_now_delinq avg_cur_bal delinq_amnt  \
id                           ...                                          
1077501            Verified  ...            0.0         NaN         0.0   
1077430     Source Verified  ...            0.0         NaN         0.0   
1077175        Not Verified  ...            0.0         NaN         0.0   
1076863     Source Verified  ...            0.0         NaN         0.0   
1075358     Source Verified  ...            0.0         NaN         0.0   

         mort_acc  num_actv_bc_tl  pub_rec_bankruptcies  tax_liens  \
id                                                                   
1077501       NaN             NaN                   0.0        0.0   
1077430       NaN             NaN                   0.0        0.0   
1077175       NaN             NaN                   0.0        0.0   
1076863       NaN             NaN                   0.0        0.0   
1075358       NaN             NaN                   0.0        0.0   

        total_bal_ex_mort  total_il_high_credit_limit  loan_status  
id                                                                  
1077501               NaN                         NaN   Fully Paid  
1077430               NaN                         NaN  Charged Off  
1077175               NaN                         NaN   Fully Paid  
1076863               NaN                         NaN   Fully Paid  
1075358               NaN                         NaN   Fully Paid  

[5 rows x 34 columns]
```
## Dates
df['issued'].value_counts().sort_index().plot(figsize=(10,6), color='black', linewidth=1);

## Trends
pd.pivot_table(df, values='int_rate', index='issued', aggfunc='mean').plot(figsize=(10,6), color='black', linewidth=1);
pd.pivot_table(df, values='loan_amnt', index='issued', aggfunc='mean').plot(figsize=(10,6), color='black', linewidth=1);

## Missing values
df.isna().sum()

## Current situation of loan status - Charged off rate
df['loan_status'].value_counts()
past = df[df['loan_status'].isin(['Charged Off', 'Fully Paid'])]
(past['loan_status'] == 'Charged Off').mean().round(3)
past['fail'] = past['loan_status'] == 'Charged Off'
running = df[~df['loan_status'].isin(['Charged Off', 'Fully Paid'])]
running['current'] = running['loan_status'] == 'Current'

## Riskier purposes
xx = pd.crosstab(past['purpose'], past['loan_status'])
xx
(xx['Charged Off']/xx['Fully Paid']).sort_values(ascending=False)

## Longer installments riskier
pd.pivot_table(past, values='installment', index='loan_status', aggfunc='mean').round()
pd.pivot_table(running, values='installment', index='current', aggfunc='mean').round()

## Distribution of the loan amount and interest rate
df['loan_amnt'].describe().round()
df['loan_amnt'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');
df['int_rate'].describe().round()
df['int_rate'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');

## Higher interest rate is riskier
pd.pivot_table(past, values='int_rate', index='loan_status', aggfunc='mean').round()
pd.pivot_table(running, values='int_rate', index='current', aggfunc='mean').round()

## Grading
df['grade'].value_counts().sort_index()
grade_rate = pd.pivot_table(df, values='int_rate', index='grade', aggfunc='mean').round()
grade_rate.plot(figsize=(6,6), color='black', linewidth=1);

## Risk by grade
pd.pivot_table(running, values='current', index='grade', aggfunc='mean')
pd.pivot_table(past, values='fail', index='grade', aggfunc='mean')

## Other topics
term
installment
missing employee title and length
annual income
dti
initial listing status
total payment over loan amount
application type
