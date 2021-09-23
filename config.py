# for help, run:
# python3 help.py

# compartment where DLS Dataset exists
compartment_id = "YOUR_COMPARTMENT_ID_NERE"
# ocid of the DLS Dataset
dataset_id = "YOUR_DATASET_ID_HERE"
# an array where the elements are all of the labels that you will use to annotate records in your DLS Dataset with. Each element is a separate label.
labels = ["cell", "debris", "stripe"]
# the algorithm that will be used to assign labels to DLS Dataset records
labeling_algorithm = "first_letter"
# maximum number of DLS Dataset records that can be retrieved from the list_records API operation for labeling
# limit=1000 is the hard limit for list_records
list_records_limit = 1000