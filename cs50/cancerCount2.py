import csv

with open("cancer.csv", "r") as file:
	reader = csv.DictReader(file)
	counts = {}
	line = 0
	for row in reader:
		favorite = row["Region"]
		if favorite in counts:
			counts[favorite] += 1
		else:
			counts[favorite] = 1
		line += 1
	
# print(f"Number of Lines: {line}")
# print(f"Black: {black} ({black / line * 100:.2f}%)")
# print(f"White: {white} ({white / line * 100:.2f}%)")
# print(f"Hispano: {hispanic} ({hispanic / line * 100:.2f}%)")
# print(f"Asian: {asian} ({asian / line * 100:.2f}%)")
# print(f"Other: {other} ({other / line * 100:.2f}%)")

print("_____SORT BY KEY_____")
for favorite in sorted(counts):
	print(f"{favorite}: {counts[favorite]} ({counts[favorite] * 100 / line :.2f}%)")

print("_____SORT BY VALUE_____")
for favorite in sorted(counts, key=counts.get, reverse=True):
	print(f"{favorite}: {counts[favorite]} ({counts[favorite] * 100 / line :.2f}%)")

#https://cs50.harvard.edu/x/2025/weeks/7/
# 43' 