
import json
import pandas as pd

# Sample JSON weather dataset
weather_json = '''
{
    "weather": [
        {
            "location": {
                "city": "Kochi",
                "country": "India"
            },
            "temperature": 32,
            "humidity": 75
        },
        {
            "location": {
                "city": "Delhi",
                "country": "India"
            },
            "temperature": 38,
            "humidity": 60
        },
        {
            "location": {
                "city": "Mumbai",
                "country": "India"
            },
            "temperature": 30,
            "humidity": 80
        },
        {
            "location": {
                "city": "Chennai",
                "country": "India"
            },
            "temperature": 35,
            "humidity": 70
        }
    ]
}
'''

# Parse JSON data
data = json.loads(weather_json)

# Convert nested JSON into tabular format
df = pd.json_normalize(data['weather'])

# Select required columns
df = df[['location.city', 'location.country',
         'temperature', 'humidity']]

# Rename columns
df.columns = ['City', 'Country', 'Temperature',
              'Humidity']

# Display weather information
print("===== WEATHER REPORT =====")
print(df.to_string(index=False))

# Calculate average temperature and humidity
avg_temp = df['Temperature'].mean()
avg_humidity = df['Humidity'].mean()

# Find highest and lowest temperature
max_temp = df['Temperature'].max()
min_temp = df['Temperature'].min()

# Display summary
print("\n===== WEATHER SUMMARY =====")
print("Average Temperature:", round(avg_temp, 2), "°C")
print("Average Humidity:", round(avg_humidity, 2), "%")
print("Highest Temperature:", max_temp, "°C")
print("Lowest Temperature:", min_temp, "°C")

# Display hottest city
hottest = df.loc[df['Temperature'].idxmax(), 'City']
print("Hottest City:", hottest)
