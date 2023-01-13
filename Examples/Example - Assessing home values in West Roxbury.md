# Example - Assessing home values in West Roxbury

## Introduction

In the US, assessed valuation determines the value of a residence for tax purposes. The **assessed value** is the price placed on a home by the corresponding government municipality, in order to calculate property taxes. A model predicting the current assessed value from available, objective data could be useful for **automatic assessment** and for spotting assessment errors. Although, in general, the assessed value tends to be lower than the appraised fair market value of property, the data on assessed values could also provide rough estimates for the mortgage industry.

The objective of this example is to explore the relationship between the assessed value and some home features, based on a data set obtained in the West Roxbury neighborhood, in southwest Boston (Massachussets). The data include information on 5,801 single family owner-occupied homes.

## The data set

The data set (file `roxbury.csv`) contains 12 home features plus the total assessed value of the property. The variables included are:

* `value`, the total assessed value for property, in thousands of USD.

* `lot_sqft`, the total lot size of parcel in square feet.

* `yr_built`, the year the property was built.

* `gross_area`, the gross floor area.

* `living_area`, the total living area.

* `floors`, the number of floors.

* `rooms`, the number of rooms.

* `bedrooms`, the number of bedrooms.

* `full_bath`, the number of full baths.

* `half_bath`, the number of half baths.

* `kitchen`, the number of kitchens.

* `fireplace`, the number of fireplaces.

* `remodel`, a dummy for remodeled houses.

Source: G Shmueli, PC Bruce, I Yahav, NR Patel & KC Lichtendahl (2018), *Data Mining for Business Analytics*, Wiley (slightly edited).

## Questions

Q1. How is the distribution of the home assessed value in West Roxbury?

Q2. Popular wisdom suggests that there is a positive association between the size of a house and its value. How can we evaluate that?

Q3. Statistical measures of association are frequently affected by extreme values. Can this happen in this case? Explore this by trimming the data, retaining only those homes for which the most influential size measure falls between two threshold values that make sense for you. 

Q4. How is the distribution of the living area expressed as a percentage of the gross area? Is there an association with the home value?
