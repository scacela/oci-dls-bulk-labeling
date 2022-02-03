import datetime
import sys
sys.path.append("..")
from config import *
import dls_create_annotation

def letter_to_label(letter):
	for l in labels:
		if letter == l[0] or letter.lower() == l[0]:
			return l 

def main(name, record_id):
	label = letter_to_label(letter=name[0])
	if label:
		dls_create_annotation.main(label=label, record_id=record_id)
	else:
		print("current time: " + str(datetime.datetime.now()))
		print("No label match for record " + str(n))
		print("with id: " + str(ids[count_records_in_batch]))
		print()