import csv

with open("cancer.csv", "r") as file:
	reader = csv.DictReader(file)
	black, white, hispanic, asian, other, line = 0, 0, 0, 0, 0, 0
	for row in reader:
		line += 1
		race = row["Race"]
		if race == "Black":
			black += 1
		elif race == "White":
			white += 1
		elif race == "Hispanic":
			hispanic += 1
		elif race == "Asian":
			asian += 1
		elif race == "Other":
			other += 1
	
print(f"Number of Lines: {line}")
print(f"Black: {black} ({black / line * 100:.2f}%)")
print(f"White: {white} ({white / line * 100:.2f}%)")
print(f"Hispano: {hispanic} ({hispanic / line * 100:.2f}%)")
print(f"Asian: {asian} ({asian / line * 100:.2f}%)")
print(f"Other: {other} ({other / line * 100:.2f}%)")

#https://cs50.harvard.edu/x/2025/weeks/7/
# 22'07