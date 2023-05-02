# Example - Barcelona Airbnb listings

## Introduction

**Airbnb** is a peer-to-peer online marketplace and homestay network, which enables people to list or rent short-term lodging in residential properties, with the cost of such accommodation set by the property owner. The company receives percentage service fees from both guests and hosts in conjunction with every booking. Starting in 2008, it has grown exponentially, and it currently has over 6 million listings in about 200 countries.

Airbnb currently releases and updates data at the Inside Airbnb site (`insideairbnb.com`). The updates posted in March 2023 cover 116 areas, most of them in US and Europe. This example uses data from Barcelona. In Barcelona, vacation apartments are subject to the highest rate of property tax, and platforms must share data with regulators.

## The data set

The file `airbnb.csv` contains data on 15,655 Airbnb listings in Barcelona. The language in the descriptions is typically English or Spanish (with exceptions). The text comes in UTF-8 encoding, so special characters may not be correctly shown (in Spanish words such as 'habitación') in some applications like Excel.

The variables are:

* `listing_id`, a unique listing's ID. An active listing is a property listed on Airbnb. Listings may include entire homes or apartments, private rooms or shared spaces.

* `host_id`, a unique host's ID.

* `host_since`, the date of the host's first listing in Airbnb, as yyyy-mm-dd.

* `name`, the listing's name. A minimal description (maximum 35 characters) of the place, intended to be appealing, such as 'Centric Bohemian next Ramblas & Macba'.

* `neighbourhood`, the neighbourhood (barrio) of the listing. The neighbourhoods are sourced from the city.

* `district`, the district of the listing. The districts, called neighbourhood groups at Airbnb, are sourced from the city. There are 10 districts in Barcelona, each grouping several neighbourhoods.

* `property_type`, the type of property listed. 75% of the listings come as 'Entire rental unit', or 'Private room in rental unit', but Airbnb admits many other possibilities.

* `room_type`, taking values 'Entire home/apt', 'Private room', 'Shared room' and 'Hotel room'.

* `bedrooms`, the number of available bedrooms.

* `price`, the daily listing's price on that date, in euros. The price shown is for the listing as a whole, not per person. The price that you see when you search Airbnb (with dates selected) is the total price divided by the number of nights you selected. When a listing has been booked for several days, the price can be lower, since the host can apply different prices depending on the number of days booked.

* `number_of_reviews`, the number of reviews of that listing that have been posted.

* `review_scores_rating`, the average reviewers' rating of overall experience (*What was your guest’s overall experience?*). Listings are rated in the range 1-100.

Source: Inside Airbnb, edited.

## Questions

Q1. How many duplicates do you find in this data set? Drop them.

Q2. The attribute `host_since` is the date of the host's first listing in Airbnb. For how many listings the host started before 2010? How many hosts started before that year?

Q3. What is the proportion of listings whose rating is missing?

Q4. Use a histogram to explore the distribution of the price. Is it useful? Maybe not, since some very expensive listings distort the whole picture. How can you trim the data, dropping the most expensive listings, to get a better picture?

Q5. What is the average price per room type? Given that the distribution of the price is quite skewed, is it better to use the median?

Q6. In which neighbourhoods do we find more listings? Are they more expensive?
