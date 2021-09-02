import dls_list_records
import dls_create_annotation
import sys
from config import *

# first_letter algorithm
def letter_to_label(letter):
	for l in labels:
		if letter == l[0] or letter.lower() == l[0]:
			return l 

def main():
	names, ids = dls_list_records.main()
	index=0
	for t in names:
		# first letter algorithm
		if labeling_algorithm == "first_letter":
			label = letter_to_label(letter=t[0])
			if label:
				dls_create_annotation.main(label=label, record_id=ids[index])
			else:
				print("No label match for record " + str(t))
				print("with id: " + str(ids[index]))
				print()
		index+=1
main()