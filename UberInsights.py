# ----------------------------
# Uber Ride Demand Analysis Template
# ----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import os

# ----------------------------
# 1. Load the Data
# ----------------------------
# Change to your actual file path
df = pd.read_csv(r"C:\Users\lukeh\python\.venv\Uber\ncr_ride_bookings.csv")

# ----------------------------
# 2. Data Cleaning 
# ----------------------------
# Convert Date/Time to datetime
df['Date/Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Extract time components
df['hour'] = df['Date/Time'].dt.hour
df['day'] = df['Date/Time'].dt.day
df['weekday'] = df['Date/Time'].dt.day_name()
df['month'] = df['Date/Time'].dt.month_name()

# Remove duplicates
df = df.drop_duplicates()

# ----------------------
# 3. Prepare Output Directory
# ----------------------
output_dir = "uber_analysis_charts"
os.makedirs(output_dir, exist_ok=True)
sns.set_style("whitegrid")

# ----------------------
# 4. Visualizations
# ----------------------

# Rides per hour
plt.figure(figsize=(10,6))
sns.countplot(x='hour', data=df, color='steelblue')
plt.title("Rides per Hour")
plt.savefig(f"{output_dir}/rides_per_hour.png")
plt.close()

# Rides per weekday
plt.figure(figsize=(10,6))
order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
sns.countplot(x='weekday', data=df, order=order, color='orange')
plt.title("Rides per Weekday")
plt.savefig(f"{output_dir}/rides_per_weekday.png")
plt.close()

# Booking Status distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Booking Status', data=df,  hue='Booking Status', legend=False, palette="Set2")
plt.title("Booking Status Distribution")
plt.savefig(f"{output_dir}/booking_status.png")
plt.close()

# Vehicle Type distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Vehicle Type', data=df, hue='Vehicle Type', legend=False, palette="Set3")
plt.title("Vehicle Type Popularity")
plt.savefig(f"{output_dir}/vehicle_type.png")
plt.close()

# Top 5 Pickup Locations
top_pickups = df['Pickup Location'].value_counts().head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=top_pickups.values, y=top_pickups.index,hue=top_pickups.index, legend=False, palette="viridis")
plt.title("Top 5 Pickup Locations")
plt.xlabel("Number of Rides")
plt.savefig(f"{output_dir}/top_pickup_locations.png")
plt.close()

# Top 5 Drop Locations
top_drops = df['Drop Location'].value_counts().head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=top_drops.values, y=top_drops.index, hue=top_drops.index, legend=False, palette="magma")
plt.title("Top 5 Drop Locations")
plt.xlabel("Number of Rides")
plt.savefig(f"{output_dir}/top_drop_locations.png")
plt.close()

# Cancellation reasons by customer
customer_cancel = df['Reason for cancelling by Customer'].value_counts().head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=customer_cancel.values, y=customer_cancel.index,hue=customer_cancel.index, legend=False, palette="coolwarm")
plt.title("Top 5 Customer Cancellation Reasons")
plt.xlabel("Number of Cancellations")
plt.savefig(f"{output_dir}/customer_cancellation_reasons.png")
plt.close()

# Average Booking Value by Vehicle Type
plt.figure(figsize=(8,5))
sns.barplot(x='Vehicle Type', y='Booking Value', data=df,hue='Vehicle Type', legend=False, palette="Set1")
plt.title("Average Booking Value by Vehicle Type")
plt.savefig(f"{output_dir}/avg_booking_value_by_vehicle.png")
plt.close()

# Average Driver Ratings
plt.figure(figsize=(8,5))
sns.histplot(df['Driver Ratings'].dropna(), bins=10, kde=True, color='green')
plt.title("Driver Ratings Distribution")
plt.savefig(f"{output_dir}/driver_ratings_distribution.png")
plt.close()

# Average Customer Ratings
plt.figure(figsize=(8,5))
sns.histplot(df['Customer Rating'].dropna(), bins=10, kde=True, color='purple')
plt.title("Customer Ratings Distribution")
plt.savefig(f"{output_dir}/customer_ratings_distribution.png")
plt.close()

# Payment Methods Distribution
plt.figure(figsize=(8,5))
sns.countplot(y='Payment Method', data=df, hue='Payment Method', legend=False, palette="pastel")
plt.title("Payment Methods Distribution")
plt.savefig(f"{output_dir}/payment_methods.png")
plt.close()

# ----------------------
# 5. Summary Statistics
# ----------------------
summary = {
    "Total Rides": len(df),
    "Completed Rides": len(df[df['Booking Status']=='Completed']),
    "Cancelled Rides": len(df[df['Booking Status']=='Cancelled']),
    "Incomplete Rides": len(df[df['Booking Status']=='Incomplete']),
    "Average Booking Value": df['Booking Value'].mean(),
    "Average Ride Distance": df['Ride Distance'].mean(),
    "Average Driver Rating": df['Driver Ratings'].mean(),
    "Average Customer Rating": df['Customer Rating'].mean()
}

print("----- Uber Insights Summary -----")
for k,v in summary.items():
    print(f"{k}: {v}")