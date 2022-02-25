import dls_list_records
import dls_create_annotation
import sys
from config import *
import datetime
import labeling_schemes.first_letter as first_letter
import labeling_schemes.dir_name as dir_name

def main():
	num_records = list_records_limit
	count_batches=1
	count_records_total=0
	while num_records == list_records_limit: # if num_records < list_records_limit, that would indicate the last loop i.e. batch
		names, ids, num_records = dls_list_records.main()
		count_records_in_batch=0
		for n in names:
			# directory name algorithm
			if labeling_algorithm == "dir_name":
				dir_name.main(name=n, record_id=ids[count_records_in_batch])
			# first letter algorithm
			elif labeling_algorithm == "first_letter":
				first_letter.main(name=n, record_id=ids[count_records_in_batch])
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