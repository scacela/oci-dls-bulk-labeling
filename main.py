import dls_list_records
import dls_create_annotation
import sys
from config import *
import datetime;

# first_letter algorithm
def letter_to_label(letter):
	for l in labels:
		if letter == l[0] or letter.lower() == l[0]:
			return l 

def main():
	num_records = list_records_limit
	count_batches=1
	count_records_total=0
	while num_records == list_records_limit: # if num_records < list_records_limit, that would indicate the last loop i.e. batch
		names, ids, num_records = dls_list_records.main()
		count_records_in_batch=0
		for n in names:
			# first letter algorithm
			if labeling_algorithm == "first_letter":
				label = letter_to_label(letter=n[0])
				if label:
					dls_create_annotation.main(label=label, record_id=ids[count_records_in_batch])
				else:
					print("current time: " + str(datetime.datetime.now()))
					print("No label match for record " + str(n))
					print("with id: " + str(ids[count_records_in_batch]))
					print()
			count_records_in_batch+=1
			count_records_total+=1
			print("current time: " + str(datetime.datetime.now()))
			print("current batch #: " + str(count_batches))
			print("# records labeled in current batch: " + str(count_records_in_batch))
		count_batches+=1
	count_batches-=1
	print("-----")
	print("TOTALS:")
	print("current time: " + str(datetime.datetime.now()))
	print("# batches: " + str(count_batches))
	print("# records labeled: " + str(count_records_total))
	print()
main()