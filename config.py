# for help, run:
# python3 help.py

# compartment where DLS Dataset exists
compartment_id = "YOUR_COMPARTMENT_ID_NERE"
# ocid of the Dataset
dataset_id = "YOUR_DATASET_ID_HERE"
labels = ["cell", "debris", "stripe"]
# the algorithm that will be used to assign labels to DLS Dataset records
labeling_algorithm = "first_letter"
# maximum number of DLS Dataset records that can be retrieved from the list_records API operation for labeling
list_records_limit = 10000