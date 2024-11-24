# Airbnb-Paris-Analysis
Paris Airbnb Data Analysis 🏠📊
Welcome to the Paris Airbnb Data Analysis repository! This project dives into an extensive dataset of over 250,000 Airbnb listings and 5 million guest reviews in Paris. The analysis uncovers pricing trends, evaluates neighborhood differences, and investigates the impact of regulatory changes on new hosts.

Project Goals 🎯
The objective of this project was to:

Analyze Airbnb listings in Paris to uncover trends.
Evaluate neighborhood-level pricing and accommodation differences.
Assess the impact of 2015 regulations on new hosts and pricing.
Dataset Details 📂
Source: Airbnb Open Data

Listings.csv: ~154MB, 250,000+ listings with details on hosts, neighborhoods, prices, and accommodations.
Reviews.csv: 5 million guest reviews for in-depth analysis of user experiences.
Key Features 🔑
Data Cleaning:

Filtered for Paris-specific data.
Handled missing values to ensure accurate insights.
Statistical Analysis:

Calculated metrics (e.g., min, max, and average prices).
Grouped data by neighborhood, host years, and accommodation types.
Visualization:

Bar charts, line charts, and dual-axis graphs built with Matplotlib.
Troubleshooting:

Resolved file encoding issues (UnicodeDecodeError) by setting encoding="ISO-8859-1" in Pandas.
Key Insights 📈
Regulatory Impact: A sharp decline in new Airbnb hosts post-2015 regulations.
Neighborhood Pricing: Élysée commands the highest prices, while other neighborhoods remain more affordable.
Accommodation Size: Larger accommodations drive higher prices, particularly in premium areas.
Market Trends: Pricing fluctuations have stabilized in recent years.
Tools and Libraries 🛠️
Python
Pandas: Data cleaning and manipulation
Matplotlib: Data visualization
Excel: Initial dataset exploration
Jupyter Notebook: Code execution and analysis
Visualizations 🖼️
Example Graphs:
Bar Chart: Average prices by neighborhood.
Line Chart: New host trends over time, showing the regulatory impact.
Dual-Axis Chart: Comparing the number of new hosts and average prices year-over-year.
Challenges Faced 🐛
Data Encoding:
Resolved UnicodeDecodeError by specifying the correct encoding format in pd.read_csv().
Large Dataset:
Efficiently handled large data files using optimized Pandas operations.
Next Steps 🔮
Implement geospatial analysis to map listings against city-wide factors like transit and tourism.
Explore advanced visualizations using libraries like Plotly or Seaborn.
Build a dashboard for interactive data exploration.
Contact 📬
Have questions or suggestions? Feel free to reach out:
