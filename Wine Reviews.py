import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/Justin Rice/Documents/projects/Wine Review/wine-reviews-exercise-Enditys/data/winemag-data-130k-v2.csv.zip')

# Calculate average points and number of reviews per country
summary_df = df.groupby('country').agg({'points': 'mean', 'title': 'count'}).reset_index()
summary_df.columns = ['Country', 'Average Points', 'Number of Reviews']
summary_df['Average Points'] = summary_df['Average Points'].round(1)

# Save the summary to a new CSV file
summary_df.to_csv('C:/Users/Justin Rice/Documents/projects/Wine Review/wine-reviews-exercise-Enditys/data/reviews-per-country.csv', index=False)
