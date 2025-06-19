import csv

# Step 1: Open the CSV file
with open('drivers.csv', mode='r') as file:
    reader = csv.DictReader(file)
    drivers = [row for row in reader]

# Step 2: Convert points from text to number
for driver in drivers:
    driver['Points'] = int(driver['Points'])

# Step 3: Sort drivers by Points in descending order
drivers.sort(key=lambda x: x['Points'], reverse=True)

# Step 4: Print formatted leaderboard
print("\n🏁 F1 Driver Leaderboard (2025):\n")
for i, driver in enumerate(drivers[:10], start=1):  # Top 10
    name = driver['Driver']
    team = driver['Team']
    points = driver['Points']
    print(f"{i}. {name} ({team}) - {points} pts")
