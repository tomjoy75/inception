import csv

with open("cancer.csv", "r") as file:
	reader = csv.reader(file)
	next(reader) #Way to pass the first line
	for row in reader:
		##print(row[3])
		favorite = row[3]
		print(favorite)