import csv
from collections import defaultdict
import matplotlib.pyplot as plt

# Step 1: Read dataset
with open("light_data.csv", "r") as file:
    data = list(csv.DictReader(file))

# Step 2: Extract light exposure values
all_values = []
daily_data = defaultdict(list)

for row in data:
    lux = int(row["Light_Exposure_Lux"])
    date = row["Date"]

    all_values.append(lux)
    daily_data[date].append(lux)

# Step 3: Overall analysis
print("\n===== LIGHT EXPOSURE ANALYSIS =====")
print("Total Records:", len(all_values))
print("Average Light Exposure:", round(sum(all_values) / len(all_values), 2), "Lux")
print("Highest Light Exposure:", max(all_values), "Lux")
print("Lowest Light Exposure:", min(all_values), "Lux")

# Step 4: Daily analysis
print("\n===== DAILY ANALYSIS =====")

dates = []
averages = []

for date, values in daily_data.items():
    average = round(sum(values) / len(values), 2)

    dates.append(date)
    averages.append(average)

    print(date)
    print("Average:", average, "Lux")
    print("Highest:", max(values), "Lux")
    print("Lowest:", min(values), "Lux")
    print("--------------------")

# Step 5: Generate CSV report
with open("analysis_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Date", "Average_Lux", "Highest_Lux", "Lowest_Lux"])

    for date, values in daily_data.items():
        writer.writerow([
            date,
            round(sum(values) / len(values), 2),
            max(values),
            min(values)
        ])

# Step 6: Generate graph
plt.figure(figsize=(9, 5))
plt.plot(dates, averages, marker="o")
plt.title("Daily Average Light Exposure")
plt.xlabel("Date")
plt.ylabel("Average Light Exposure (Lux)")
plt.grid(True)
plt.tight_layout()

plt.savefig("light_exposure_graph.png")

print("\nAnalysis report generated successfully!")
print("Graph saved successfully!")

plt.show()