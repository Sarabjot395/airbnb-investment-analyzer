# Airbnb Investment Analyzer

An end-to-end data analytics project that helps investors, real estate agents, and existing hosts identify the most profitable U.S. cities, neighborhoods, and property types for Airbnb investment — based on pricing, occupancy proxy, host behavior, and revenue potential.

[View the Interactive Dashboard on Tableau Public →](https://public.tableau.com/app/profile/sarabjot.singh6119/viz/AirbnbInvestmentAnalyzer/Dashboard1)**

---

## Business Problem

Airbnb investors currently lack a data-driven way to compare cities, neighborhoods, and property types on profitability and demand — leading to decisions based on gut feeling or hearsay rather than evidence. This project analyzes 226,000+ real U.S. Airbnb listings to answer:

- Which cities and neighborhoods offer the best return on investment?
- Which property types (entire home, private room, shared room, hotel room) are most profitable?
- Does higher pricing actually reduce occupancy?
- How do individual hosts compare to professional/business hosts?

## Dataset

Source: [US Airbnb Open Data](https://www.kaggle.com/datasets/kritikseth/us-airbnb-open-data) (Kaggle, derived from Inside Airbnb), covering 28 U.S. cities/regions and 226,030 listings.

Data is used for educational/research purposes, consistent with Inside Airbnb's public data licensing.

## Tech Stack

- Python(Pandas, NumPy, Matplotlib) — data cleaning, EDA, analysis
- SQL(SQLite, SQLAlchemy) — business question queries
- Tableau Public — interactive dashboard
- Git/GitHub — version control

## Project Workflow

```
1. Data Cleaning        →  Removed outliers, handled missing values, fixed data types
2. Exploratory Analysis →  Identified data quality issues before drawing conclusions
3. SQL Analysis         →  Answered business questions with aggregation queries
4. Business Analysis    →  Combined SQL + Python to build revenue estimates
5. Dashboard            →  Built an interactive Tableau dashboard for stakeholders
```

## Key Findings

**1. The biggest market isn't the best investment.** New York City has the most listings (45,541) of any city in the dataset, but ranks *last* out of 26 qualifying cities on estimated annual revenue potential — driven by low occupancy proxy, likely linked to stricter short-term rental regulation in the city during this period. Smaller markets like **Santa Cruz County, Asheville, and Nashville** show meaningfully stronger per-listing returns.

**2. Entire homes/apartments are the strongest single-property investment.** They generate the highest estimated annual revenue of any property type, narrowly ahead of hotel-room listings and well ahead of private and shared rooms.

**3. Higher price correlates with lower occupancy.** Listings above roughly $300–400/night show a clear, visible drop-off in bookings (measured via reviews-per-month, a standard Airbnb-market-analysis proxy for occupancy). Pricing too aggressively appears to cost hosts more in lost bookings than it gains in per-night margin.

**4. Individual hosts and professional/business hosts behave differently.** Professional hosts (10+ listings) price ~29% higher on average but see notably lower occupancy per listing than individual hosts — consistent with the price/occupancy trade-off found above.

## Methodology Notes (for technical reviewers)

- **Occupancy proxy:** Airbnb does not publish real booking calendars, so `reviews_per_month` is used as an industry-standard proxy for booking frequency.
- **Outlier handling:** Removed a data-entry error listing (`minimum_nights` = 100,000,000), $0 price listings, and the top 1% of prices (percentile-based, not an arbitrary cutoff) — approximately 1.07% of rows removed in total.
- **Missing data:** `neighbourhood_group` is missing in ~51% of rows — this is structural (some cities don't report this field), not random, and was labeled explicitly rather than imputed.
- **Revenue estimate:** `price × reviews_per_month × 12` is used as a directional proxy for annual revenue potential, not a precise financial forecast.

## Repository Structure

```
├── data/
│   ├── raw/              # Original, untouched dataset
│   └── processed/        # Cleaned data + SQLite database
├── notebooks/            # Numbered analysis notebooks (EDA → Cleaning → SQL → Analysis)
├── sql/
│   └── queries/          # Standalone .sql files, one per business question
├── images/               # Exported chart images
├── requirements.txt
└── README.md
```

## Next Steps

This project is actively being extended with:
- A Streamlit app for interactive investment recommendations by budget/city/rating
- Predictive modeling (price and occupancy prediction)
- An expanded SQL portfolio (50+ interview-style queries)
- Neighborhood-level clustering and investment scoring

## Author

Sarabjot Singh