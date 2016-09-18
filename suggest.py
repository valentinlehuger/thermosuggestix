import csv
import sys
import random

if __name__ == "__main__":

	with open(sys.argv[1], 'r') as f:
		reader = csv.DictReader(f)
		l = [x for x in reader]

	for line in random.sample(l, 3):
		print line["Nom de la recette"]
