import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\noahk\Downloads\Airbnb+Data\Airbnb Data\Listings.csv"
listings = pd.read_csv(file_path, encoding="ISO-8859-1", low_memory=False)

listings['host_since'] = pd.to_datetime(listings['host_since'], errors='coerce')

paris_listings = listings[listings['city'] == 'Paris'][['host_since', 'neighbourhood', 'city', 'accommodates', 'price']]

missing_values = paris_listings.isnull().sum()
print("Missing Values:\n", missing_values)

profile_metrics = {
    'min_price': paris_listings['price'].min(),
    'max_price': paris_listings['price'].max(),
    'average_price': paris_listings['price'].mean(),
    'min_accommodates': paris_listings['accommodates'].min(),
    'max_accommodates': paris_listings['accommodates'].max(),
    'average_accommodates': paris_listings['accommodates'].mean()
}
print("\nProfiling Metrics:\n", profile_metrics)

paris_listings_neighbourhood = (
    paris_listings.groupby('neighbourhood')['price']
    .mean()
    .sort_values()
    .reset_index()
)

most_expensive_neighbourhood = paris_listings_neighbourhood.iloc[-1]['neighbourhood']
print("\nMost Expensive Neighbourhood:", most_expensive_neighbourhood)

paris_listings_accommodations = (
    paris_listings[paris_listings['neighbourhood'] == most_expensive_neighbourhood]
    .groupby('accommodates')['price']
    .mean()
    .sort_values()
    .reset_index()
)

# Extract year from host_since and group by year
paris_listings['host_year'] = paris_listings['host_since'].dt.year
paris_listings_over_time = (
    paris_listings.groupby('host_year')
    .agg(average_price=('price', 'mean'), new_hosts=('host_year', 'count'))
    .reset_index()
)

# Step 6: Visualizations

# 1. Horizontal bar chart for average price by neighbourhood
plt.barh(paris_listings_neighbourhood['neighbourhood'], paris_listings_neighbourhood['price'])
plt.title("Average Price by Neighbourhood in Paris")
plt.xlabel("Average Price (€)")
plt.ylabel("Neighbourhood")
plt.show()

# 2. Horizontal bar chart for average price by accommodates in the most expensive neighbourhood
plt.barh(paris_listings_accommodations['accommodates'], paris_listings_accommodations['price'])
plt.title(f"Average Price by Accommodates in {most_expensive_neighbourhood}")
plt.xlabel("Average Price (€)")
plt.ylabel("Accommodates")
plt.show()

# 3. Line chart for count of new hosts over time
plt.plot(paris_listings_over_time['host_year'], paris_listings_over_time['new_hosts'], marker='o')
plt.title("Number of New Hosts Over Time")
plt.xlabel("Year")
plt.ylabel("Number of New Hosts")
plt.ylim(0)
plt.grid()
plt.show()

# 4. Line chart for average price over time
plt.plot(paris_listings_over_time['host_year'], paris_listings_over_time['average_price'], marker='o', color='orange')
plt.title("Average Price Over Time")
plt.xlabel("Year")
plt.ylabel("Average Price (€)")
plt.ylim(0)
plt.grid()
plt.show()

# 5. Dual-axis chart for new hosts and average price over time
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(paris_listings_over_time['host_year'], paris_listings_over_time['new_hosts'], 'g-', label="New Hosts")
ax2.plot(paris_listings_over_time['host_year'], paris_listings_over_time['average_price'], 'b-', label="Average Price")

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of New Hosts', color='g')
ax2.set_ylabel('Average Price (€)', color='b')

plt.title("New Hosts and Average Price Over Time")
fig.tight_layout()
plt.show()
