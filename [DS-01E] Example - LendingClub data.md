# [DS-01E] Example - LendingClub data

## Introduction

**LendingClub** is a financial services company headquartered in San Francisco, California. It was the first **peer-to-peer lender** to register its offerings as securities with the Securities and Exchange Commission (SEC), and to offer loan trading on a secondary market. At its height, LendingClub was the world's largest peer-to-peer lending platform. The company reported that $15.98 billion in loans had been originated through its platform up to December 31, 2015. Renaud Laplanche, the company’s founder and CEO, also received The Economist Innovation Award in 2014 for the consumer products category.

LendingClub enabled borrowers to create unsecured personal loans between $1,000 and $40,000. The standard loan period was three years. Investors were able to search and browse the loan listings on LendingClub website and select loans that they wanted to invest in based on the information supplied about the borrower, amount of loan, loan grade, and loan purpose. Investors made money from the interest on these loans. LendingClub made money by charging borrowers an origination fee and investors a service fee. All personal loans offered by LendingClub were fixed rate loans.

Like other peer-to-peer lenders, LendingClub experienced increasing difficulty attracting investors during early 2016. This led the firm to increase the interest rate on three occasions during the first months of the year. The increase in interest rates and concerns over the impact of the slowing US economy caused a large drop in LendingClub's share price.

In April 2016, a LendingClub employee reported to Laplanche that the dates on approximately $3 million in the firm's loans appeared to have been altered. LendingClub's internal auditor engaged an outside firm to investigate the report. Additional problems with loans were found, including that $22 million in loans which had been sold to an investment bank did not in fact meet the bank's investment criteria. LendingClub bought these loans back from the bank and resold them.

The New York Times reported that the investigation found that Laplanche had not disclosed to the board that he owned part of an investment fund which LendingClub was considering purchasing.The Wall Street Journal also stated that Laplanche was found to have not fully disclosed what he knew about the problematic loans.

On May 6, LendingClub's board made it clear to Laplanche that he no longer had their confidence, leading to his resignation on 9 May. The Wall Street Journal reported that Laplanche had been fired by the board. Three of the firm's other managers had also been fired or had resigned by that time as a result of the problematic loans.[46] LendingClub's stock price fell by a further 34 percent after Laplanche's departure was announced. This placed the stock price at 70% of the price at the time of the firm's initial public offering. As a result of the incident, the Securities and Exchange Commission was reported to be investigating LendingClub's disclosures to investors.

In December 2017, the Financial Times reported that LendingClub "has struggled to overcome the effects of a governance scandal last May", and that the firm "has battled to keep big investors buying loans" despite improvements to its internal governance. These challenges have led it to raise its loss estimate, and have led to further drops in its share price. At this time many other peer to peer lending companies were also experiencing difficulties.

In an interview with Business Insider in December 2019, executive Valerie Kay noted that LendingClub had switched focus to institutional investors as well as its traditional peer-to-peer lending through a new project called "Scale", focused on delivering representative samples of loans instead of individual loans - labeled its "Select" program. LendingClub had grown to $10.8 billion in annual loan originations in the year 2018.[49]

In April 2020, the company announced it would lay off around one third of its employees in anticipation of the economic downturn resulting from the COVID-19 pandemic. In August, it discontinued its secondary trading platform, hosted by Folio, reducing liquidity for existing peer-to-peer investors. In October, LendingClub ceased all new loan accounts on their website as part of restructuring into a neobank after the acquisition of Radius Bank. In December 2020, the company ceased to operate as a peer-to-peer lender

## The data set

The file `lending.csv` contains data on the personal loans given from August 20812 to September 2020. The data set covers 2,925,493 loans. Only those loans for which the loan amount has been funded are included. This means excluding a 0.07% of the records.

The columns are:

* `id`, a unique identifier for the loan.

* `loan_amnt`, the listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value.

* `term`, the number of (monthly) payments on the loan. Values are either 36 or 60.

* `int_rate`, the interest rate on the loan (%).

* `installment`, the monthly payment owed by the borrower (US dollar).

* `grade`, the loan grade as assigned by Lending Club. A letter (A-G) plus a number (1-5). A1 is the best grade and G5 the worst one.

* `emp_title`, the job title supplied by the borrower when applying for the loan. Missing for about 260,000 loans.

* `emp_length`,	the employment length in years. Eleven possible values, from '< 1 year' to '10+ years'. Missing for about 205,000 loans.

* `home_ownership`, the home ownership status provided by the borrower during registration or obtained from the credit report. The values are 'ANY', 'MORTGAGE', 'NONE', 'OTHER', 'OWN' and 'RENT'.

* `annual_inc`, the self-reported annual income provided by the borrower during registration.

* `verification_status`, whether the borrower's income was verified by Lending Club, not verified, or the income source was verified.

* `issue_d`, the month the loan was funded. From 'Apr-2008' through 'Sep-2020'.

* `purpose`, a category provided by the borrower for the loan request. Fourteen values: 'car', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business', 'vacation' and 'wedding'.

* `addr_state`,	the state provided by the borrower in the loan application. 51 values, from 'AK' through 'WY'.

* `dti`, a ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested loan, divided by the borrower’s self-reported monthly income. Missing for about 3,100 loans.

* `fico`, the lower boundary range the borrower's FICO at loan origination belongs to.

* `open_acc`, the number of open credit lines in the borrower's credit file.

* `pub_rec`, the number of derogatory public records.

* `revol_bal`, the total credit revolving balance (US dollars).

* `revol_util`, the revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.

* `total_acc`, the total number of credit lines currently in the borrower's credit file.

* `initial_list_status`, the initial listing status of the loan. The possible values are 'w' (whole) and 'f' (fractional). Loans listed 'w' become available for fractional funding (and vice versa) if there are no buyers within a certain time frame.

* `out_prncp`, the remaining outstanding principal for the total amount funded.

* `total_pymnt`, payments received to date for the total amount funded.

* `total_rec_prncp`, the principal received to date.

* `total_rec_int`, the interest received to date.

* `application_type`, indicates whether the loan is an individual application or a joint application with two co-borrowers.

* `acc_now_delinq`, the number of accounts on which the borrower is now delinquent.

* `avg_cur_bal`, average current balance of all accounts.

* `chargeoff_within_12_mths`, number of charge-offs within 12 months.

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


## Code ##

# Import the data #
import pandas as pd
path = 'Dropbox (Personal)/lending/'
fname = path + 'lending.csv.zip'
df = pd.read_csv(fname, index_col=0)

# Exploring tha data #
df.info()
df.head()

# Dates #
df['issue_d'] = df['issue_d'].str[4:] + '-' + df['issue_d'].str[:3]
mo_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
no_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for i in range(12): df['issue_d'] = df['issue_d'].str.replace(mo_list[i], no_list[i])
df['issue_d'].value_counts().sort_index().plot(figsize=(10,6), color='black', linewidth=1);

# Trends #
pd.pivot_table(df, values='int_rate', index='issue_d', aggfunc='mean').plot(figsize=(10,6), color='black', linewidth=1);
pd.pivot_table(df, values='loan_amnt', index='issue_d', aggfunc='mean').plot(figsize=(10,6), color='black', linewidth=1);

# Missing values #
df.isna().sum()

# Current situation of loan status - Charged off rate #
df['loan_status'].value_counts()
past = df[df['loan_status'].isin(['Charged Off', 'Fully Paid'])]
(past['loan_status'] == 'Charged Off').mean().round(3)
past['fail'] = past['loan_status'] == 'Charged Off'
running = df[~df['loan_status'].isin(['Charged Off', 'Fully Paid'])]
running['current'] = running['loan_status'] == 'Current'

# Risky purposes
xx = pd.crosstab(past['purpose'], past['loan_status'])
xx
(xx['Charged Off']/xx['Fully Paid']).sort_values(ascending=False)

# Longer installments more risky #
pd.pivot_table(past, values='installment', index='loan_status', aggfunc='mean').round()
pd.pivot_table(running, values='installment', index='current', aggfunc='mean').round()

# Distribution of the loan amount and interest rate #
df['loan_amnt'].describe().round()
df['loan_amnt'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');
df['int_rate'].describe().round()
df['int_rate'].plot.hist(figsize=(8,6), color='gray', edgecolor='white');

# Higher interest rate more risky #
pd.pivot_table(past, values='int_rate', index='loan_status', aggfunc='mean').round()
pd.pivot_table(running, values='int_rate', index='current', aggfunc='mean').round()

# Grading #
df['grade'].value_counts().sort_index()
grade_rate = pd.pivot_table(df, values='int_rate', index='grade', aggfunc='mean').round()
grade_rate.plot(figsize=(6,6), color='black', linewidth=1);

# Risk by grade #
pd.pivot_table(running, values='current', index='grade', aggfunc='mean')
pd.pivot_table(past, values='fail', index='grade', aggfunc='mean')
