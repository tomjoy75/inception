import csv

with open("cancer.csv", "r") as file:
	reader = csv.DictReader(file) ## Assume the first line gives key
	for row in reader:
		##print(row["Race"])
		favorite = row["Race"]
		print(favorite)